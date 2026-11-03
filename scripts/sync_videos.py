#!/usr/bin/env python3
"""YouTube kanalındaki videoları data/videos.json'a eşitler.

Kaynak kanalın RSS akışıdır (yalnızca son 15 video). Daha eski videolar
bir kez --ids ile izleme sayfalarından eklenir; dosyada kalan kayıt
silinmez, böylece arşiv RSS'in 15'lik penceresinden bağımsız büyür.

Kapak görselleri static/img/videos/<id>.jpg olarak indirilir; site
Google sunucusundan görsel çekmez, Hugo bunları WebP'ye çevirir.

Yalnızca standart kütüphane kullanır (GitHub Actions'ta kurulum yok).
"""
import argparse
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

CHANNEL_ID = "UCJW06ju5sCuTiA2V3cmv1-w"
FEED = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"
ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "videos.json"
THUMBS = ROOT / "static" / "img" / "videos"
NS = {
    "a": "http://www.w3.org/2005/Atom",
    "yt": "http://www.youtube.com/xml/schemas/2015",
    "media": "http://search.yahoo.com/mrss/",
}
ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")


def utc(stamp):
    """RSS ve izleme sayfası farklı saat dilimi yazar; sıralama için UTC'ye çevrilir."""
    d = datetime.fromisoformat(stamp.replace("Z", "+00:00"))
    return d.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def fetch(url, binary=False):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "tr"})
    with urllib.request.urlopen(req, timeout=30) as r:
        body = r.read()
    return body if binary else body.decode("utf-8")


def clean_title(raw):
    """Başlıktan #etiketleri ve emojiyi atar."""
    t = re.sub(r"#\w+", "", raw)
    t = re.sub(r"[\U0001F000-\U0001FAFF☀-➿️]", "", t)
    return re.sub(r"\s+", " ", t).strip()


def headline(title, description):
    """Kartlarda kullanılan kısa başlık: açıklamanın ilk cümlesi.

    YouTube Shorts başlıkları 100 karakterde kesilir; açıklama tamdır.
    """
    text = clean_title(description or title)
    m = re.match(r"(.+?[.!?])(\s|$)", text)
    first = (m.group(1) if m else text).strip()
    if len(first) > 110:
        first = clean_title(title)
    return first.rstrip(".")


def parse_feed(xml_text):
    root = ET.fromstring(xml_text)
    out = []
    for e in root.findall("a:entry", NS):
        vid = e.findtext("yt:videoId", namespaces=NS)
        if not vid or not ID_RE.match(vid):
            continue
        title = e.findtext("a:title", default="", namespaces=NS)
        desc = e.findtext("media:group/media:description", default="", namespaces=NS)
        out.append({
            "id": vid,
            "title": clean_title(title),
            "headline": headline(title, desc),
            "description": desc.strip(),
            "published": utc(e.findtext("a:published", namespaces=NS)),
        })
    return out


def parse_watch(html, vid):
    m = re.search(r"ytInitialPlayerResponse\s*=\s*(\{.+?\});(?:var |</script>)", html)
    if not m:
        raise ValueError(f"{vid}: izleme sayfasında video bilgisi yok")
    d = json.loads(m.group(1))
    v = d["videoDetails"]
    mf = d.get("microformat", {}).get("playerMicroformatRenderer", {})
    if v.get("videoId") != vid:
        raise ValueError(f"{vid}: sayfa başka bir video döndürdü")
    desc = v.get("shortDescription", "")
    return {
        "id": vid,
        "title": clean_title(v["title"]),
        "headline": headline(v["title"], desc),
        "description": desc.strip(),
        "published": utc(mf["publishDate"]),
    }


def merge(existing, fresh):
    """Yeni bilgiyi id'ye göre işler; dosyadaki eski kayıtlar korunur."""
    by_id = {v["id"]: v for v in existing}
    for v in fresh:
        by_id[v["id"]] = {**by_id.get(v["id"], {}), **v}
    return sorted(by_id.values(), key=lambda v: v["published"], reverse=True)


def save_thumb(vid):
    dest = THUMBS / f"{vid}.jpg"
    if dest.exists():
        return
    # oar2: Shorts için dikey kapak; yoksa yatay hq kapak.
    for name in ("oar2.jpg", "hqdefault.jpg"):
        try:
            body = fetch(f"https://i.ytimg.com/vi/{vid}/{name}", binary=True)
        except Exception:
            continue
        if body[:3] == b"\xff\xd8\xff":
            THUMBS.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(body)
            return
    raise RuntimeError(f"{vid}: kapak görseli indirilemedi")


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--ids", nargs="*", default=[], help="RSS'te olmayan eski videolar")
    args = ap.parse_args(argv)

    existing = json.loads(DATA.read_text()) if DATA.exists() else []
    fresh = parse_feed(fetch(FEED))
    for vid in args.ids:
        if not ID_RE.match(vid):
            sys.exit(f"geçersiz video id: {vid}")
        fresh.append(parse_watch(fetch(f"https://www.youtube.com/watch?v={vid}"), vid))

    videos = merge(existing, fresh)
    for v in videos:
        save_thumb(v["id"])
    DATA.write_text(json.dumps(videos, ensure_ascii=False, indent=1) + "\n")
    print(f"{len(videos)} video ({len(videos) - len(existing)} yeni)")


if __name__ == "__main__":
    main()
