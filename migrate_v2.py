#!/usr/bin/env python3
"""
hotmanoglu.com Wix → Hugo Migrasyon Scripti v2
================================================
Tüm bilinen yazı URL'leri dahil edildi.

Kullanım:
    python3 migrate_v2.py
"""

import requests
from bs4 import BeautifulSoup
import re
import os
import time
from urllib.parse import unquote
from datetime import datetime, timedelta

SITE_URL = "https://www.hotmanoglu.com"
OUTPUT_DIR = "content/posts"
IMG_DIR = "static/img/posts"

# Siteden bilinen tüm yazı URL'leri
KNOWN_URLS = [
    "/post/vaka-analizi-kuzey-kore-nin-görünmez-ordusu-sahte-yazılımcılar-800-milyon-dolar-ofac-yaptırımı",
    "/post/vaka-analizi-banka-tezgahının-arkasındaki-adam",
    "/post/bilmiyordum-yetmedi-oligark-fonu-51-i̇hlal-11-5-milyon-dolar",
    "/post/i̇çeriden-tehdit-banka-çalışanı-10-milyar-dolarlık-dolandırıcılık-şebekesinin-kapısını-nasıl-açtı",
    "/post/fatf-tan-tarihi-uyarı-stablecoin-ler-artık-kara-para-aklamanın-birincil-aracı",
    "/post/50-dolarlık-rüşvet-5-5-milyon-dolarlık-kara-para-td-bank-kasiyer-davası",
    "/post/kripto-vergi-düzenlemesi-tbmm-de-üç-katmanlı-bir-yapı-geliyor",
    "/post/vaka-analizi-5-i̇l-6-örgüt-394-milyon-tl-dijital-yatırım-vaadiyle-katmanlanan-fraud-operasyonu",
    "/post/kripto-platformlarına-yapay-zekâ-kapısı-açıldı-ama-anahtar-masak-ta",
    "/post/i̇sviçre-nin-gizli-bankası-rusya-ve-i̇ran-ın-kasası-çıktı-fincen-mbaer-i-dolar-sisteminden-kesiyor",
    "/post/vaka-analizi-tek-adam-beş-unvan-sıfır-denetim-first-national-bank-of-lindsay-in-çöküşü",
    "/post/ofac-tan-dolandırıcılık-ağlarına-yaptırım-timeshare-fraud-i̇lk-kez-sdn-listesinde",
    "/post/brüksel-de-deprem-ab-kurumlarına-arka-arkaya-yolsuzluk-baskını",
    "/post/abd-de-tarihi-skandal-sosyal-yardım-programlarından-milyarlarca-dolar-nasıl-çalındı",
    "/post/abd-den-çin-bağlantılı-kara-para-aklama-ağlarına-operasyon-yeraltı-bankacılığı-ve-kripto-hatları-me",
    "/post/vaka-analizi-kddi-de-1-5-milyar-dolarlık-sahte-gelir-skandalı",
    "/post/fca-dan-sektör-genelinde-aml-i̇ncelemesi-250-den-fazla-varlık-yönetim-şirketi-denetim-altında",
    "/post/ofac-tan-şubat-güncellemesi-i-ran-a-yeni-yaptırımlar-venezuela-i-çin-lisans-ve-rehber-değişiklikleri",
    "/post/dolandırıcılık-fabrikası-ortaya-çıkarıldı-kamboçya-da-endüstriyel-ölçekte-fraud-operasyonu",
    "/post/almanya-da-heraeus-a-fraud-i̇ddiası-i̇hbar-hattı-yıllarca-görmezden-gelindi",
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

TR_MONTHS = {
    "oca": 1, "şub": 2, "mar": 3, "nis": 4, "may": 5, "haz": 6,
    "tem": 7, "ağu": 8, "eyl": 9, "eki": 10, "kas": 11, "ara": 12,
}


def slugify(text):
    text = text.lower().strip()
    tr_map = str.maketrans("çğıöşüâîûÇĞİÖŞÜÂÎÛ", "cgiosuaiuCGIOSUAIU")
    text = text.translate(tr_map)
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')[:80]


def parse_date(text):
    text = text.strip().lower()
    m = re.search(r'(\d+)\s*gün\s*önce', text)
    if m:
        return (datetime.now() - timedelta(days=int(m.group(1)))).strftime("%Y-%m-%d")
    m = re.search(r'(\d+)\s*saat\s*önce', text)
    if m:
        return datetime.now().strftime("%Y-%m-%d")
    m = re.search(r'(\d{1,2})\s+(\w+?)(?:\s+(\d{4}))?$', text)
    if m:
        day = int(m.group(1))
        month_str = m.group(2)[:3].lower()
        year = int(m.group(3)) if m.group(3) else datetime.now().year
        for key, val in TR_MONTHS.items():
            if month_str.startswith(key[:3]):
                return f"{year}-{val:02d}-{day:02d}"
    return datetime.now().strftime("%Y-%m-%d")


def guess_category(title, content=""):
    text = (title + " " + content[:500]).lower()
    if "vaka analizi" in text or "vaka inceleme" in text:
        return "Vaka Analizi"
    elif any(w in text for w in ["ofac", "yaptırım", "sdn", "fincen"]):
        return "Yaptırım"
    elif any(w in text for w in ["fatf", "aml", "cft", "masak"]):
        return "AML/CFT"
    elif any(w in text for w in ["düzenleme", "tbmm", "kanun", "yönetmelik", "fca"]):
        return "Düzenleme"
    elif any(w in text for w in ["fraud", "dolandırıcılık", "içeriden tehdit", "rüşvet"]):
        return "Fraud"
    return "Analiz"


def extract_tags(title, content):
    tags = set()
    text = (title + " " + content).lower()
    kw = {
        "OFAC": ["ofac"], "FATF": ["fatf"], "FinCEN": ["fincen"],
        "Kara Para Aklama": ["kara para"], "Yaptırım": ["yaptırım"],
        "Kripto": ["kripto", "bitcoin", "stablecoin", "blockchain"],
        "Fraud": ["fraud", "dolandırıcılık"], "İç Tehdit": ["içeriden tehdit", "insider"],
        "Rusya": ["rusya", "oligark"], "ABD": ["abd", "doj"],
        "Türkiye": ["türkiye", "masak", "tbmm"], "Kuzey Kore": ["kuzey kore"],
        "Çin": ["çin bağlantılı"], "İran": ["iran"], "TD Bank": ["td bank"],
    }
    for tag, patterns in kw.items():
        if any(p in text for p in patterns):
            tags.add(tag)
    return sorted(list(tags))[:6]


def download_image(img_url, slug):
    try:
        os.makedirs(IMG_DIR, exist_ok=True)
        ext = ".png" if ".png" in img_url else ".jpg"
        filepath = os.path.join(IMG_DIR, f"{slug}{ext}")
        if os.path.exists(filepath):
            return f"/img/posts/{slug}{ext}"
        resp = requests.get(img_url, headers=HEADERS, timeout=15)
        if resp.status_code == 200 and len(resp.content) > 1000:
            with open(filepath, 'wb') as f:
                f.write(resp.content)
            return f"/img/posts/{slug}{ext}"
    except Exception as e:
        print(f"  ⚠ Görsel: {e}")
    return ""


def fetch_post(url):
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.encoding = 'utf-8'
        soup = BeautifulSoup(resp.text, 'html.parser')
    except Exception as e:
        print(f"  ❌ Fetch hatası: {e}")
        return None

    # Başlık
    title = ""
    for h1 in soup.find_all('h1'):
        t = h1.get_text(strip=True)
        if t.upper() != "HOTMANOGLU" and len(t) > 5:
            title = t
            break
    if not title:
        title = unquote(url.split('/post/')[-1]).replace('-', ' ').title()

    # Tarih
    date_str = datetime.now().strftime("%Y-%m-%d")
    for span in soup.find_all('span'):
        t = span.get_text(strip=True)
        if re.search(r'\d+\s*(gün|saat)\s*önce', t) or re.search(r'\d{1,2}\s+(oca|şub|mar|nis|may|haz|tem|ağu|eyl|eki|kas|ara)', t, re.I):
            date_str = parse_date(t)
            break

    # Görsel
    image_path = ""
    og = soup.find('meta', property='og:image')
    if og and og.get('content') and 'wixstatic' in og['content']:
        slug = slugify(title)
        image_path = download_image(og['content'], slug)

    # İçerik — body text approach (daha güvenilir)
    body_text = soup.get_text(separator='\n')
    lines = body_text.split('\n')

    content_lines = []
    capturing = False
    skip_phrases = [
        'ana sayfa', 'hakkımda', 'blog', 'more', 'all posts', 'ara',
        'etik & uyum', 'hotmanoglu', 'son yazılar', 'hepsini gör',
        'yorumlar', 'bir yorum yazın', 'bottom of page', 'top of page',
        'use tab to navigate', 'dakikada okunur', 'gün önce', 'saat önce',
    ]

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Başlığı bulduysa, sonraki satırdan itibaren içerik başlar
        if line == title:
            capturing = True
            continue

        if not capturing:
            continue

        # Bitiş sinyalleri
        line_lower = line.lower()
        if any(line_lower == s or line_lower.startswith(s) for s in ['son yazılar', 'yorumlar', 'bir yorum yazın', 'bottom of page']):
            break

        # Atlanacak satırlar
        if any(s in line_lower for s in skip_phrases):
            continue
        if re.match(r'^\d+\s*(gün|saat)\s*önce$', line):
            continue
        if re.match(r'^\d+\s*dakikada\s*okunur$', line):
            continue
        if len(line) < 3:
            continue

        # Markdown dönüşümü — basit heuristik
        # Kısa, bold görünen satırlar → heading olabilir
        # Wix'te h2'ler genelde kısa cümleler
        content_lines.append(line)

    # Heading tespiti: Wix sayfasındaki h2/h3'leri bul
    headings = set()
    for h in soup.find_all(['h2', 'h3']):
        ht = h.get_text(strip=True)
        if ht and ht not in ['HOTMANOGLU', 'Son Yazılar', 'Yorumlar'] and len(ht) > 3:
            headings.add(ht)

    # Content'i oluştur
    final_lines = []
    for line in content_lines:
        if line in headings:
            final_lines.append(f"\n## {line}\n")
        else:
            final_lines.append(line)
            final_lines.append("")

    content = "\n".join(final_lines).strip()

    # Bold koruma — Wix'ten gelen ** işaretleri korunmuş olabilir
    # Ekstra temizlik
    content = re.sub(r'\n{3,}', '\n\n', content)

    category = guess_category(title, content)
    tags = extract_tags(title, content)
    desc = re.sub(r'[#*\[\]()]', '', content.split('\n\n')[0] if content else "")[:160].strip()
    slug = slugify(title)
    safe_title = title.replace('"', '\\"')

    md = f'''---
title: "{safe_title}"
date: {date_str}
draft: false
categories: ["{category}"]
tags: [{', '.join(f'"{t}"' for t in tags)}]
description: "{desc}"
image: "{image_path}"
---

{content}
'''

    return {"slug": slug, "title": title, "date": date_str, "markdown": md}


def discover_extra_urls():
    """Sitemap ve sayfalardan ek URL bulmaya çalış."""
    extra = set()

    # Sitemap dene
    for sitemap_url in [f"{SITE_URL}/sitemap.xml", f"{SITE_URL}/sitemap-posts.xml"]:
        try:
            resp = requests.get(sitemap_url, headers=HEADERS, timeout=10)
            if resp.status_code == 200:
                for match in re.findall(r'<loc>(.*?)</loc>', resp.text):
                    if '/post/' in match:
                        path = match.replace(SITE_URL, '')
                        extra.add(path)
        except:
            pass

    # Ana sayfa ve blog sayfasından link çek
    for page_url in [SITE_URL, f"{SITE_URL}/blog"]:
        try:
            resp = requests.get(page_url, headers=HEADERS, timeout=10)
            for match in re.findall(r'href="(/post/[^"]+)"', resp.text):
                extra.add(match)
            for match in re.findall(r'href="(https://www\.hotmanoglu\.com/post/[^"]+)"', resp.text):
                extra.add(match.replace(SITE_URL, ''))
        except:
            pass

    return extra


def main():
    print("=" * 60)
    print("🔄 hotmanoglu.com Wix → Hugo Migrasyon v2")
    print("=" * 60)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(IMG_DIR, exist_ok=True)

    # Bilinen URL'ler + dinamik keşif
    all_paths = set(KNOWN_URLS)
    print(f"\n📋 Bilinen URL: {len(all_paths)}")

    print("📡 Ek URL'ler aranıyor...")
    extra = discover_extra_urls()
    new_count = len(extra - all_paths)
    all_paths.update(extra)
    print(f"  ✅ {new_count} ek URL bulundu → Toplam: {len(all_paths)}")

    # Önce mevcut dosyaları kontrol et — zaten çekilmişleri atla
    existing = set()
    if os.path.exists(OUTPUT_DIR):
        for f in os.listdir(OUTPUT_DIR):
            if f.endswith('.md'):
                existing.add(f)

    urls = sorted(all_paths)
    print(f"\n📝 {len(urls)} yazı işlenecek...\n")

    success = 0
    skipped = 0
    failed = 0

    for i, path in enumerate(urls, 1):
        full_url = SITE_URL + path if path.startswith('/') else path
        preview = unquote(path.split('/post/')[-1])[:55]
        print(f"[{i}/{len(urls)}] {preview}...")

        result = fetch_post(full_url)
        if result:
            filename = f"{result['slug']}.md"

            # Zaten varsa atla
            if filename in existing:
                print(f"  ⏩ Zaten mevcut, atlanıyor")
                skipped += 1
            else:
                filepath = os.path.join(OUTPUT_DIR, filename)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(result['markdown'])
                print(f"  ✅ {filename} ({result['date']})")
                success += 1
        else:
            print(f"  ❌ Başarısız")
            failed += 1

        time.sleep(1.5)

    print()
    print("=" * 60)
    print(f"✅ Yeni: {success}  ⏩ Mevcut: {skipped}  ❌ Hata: {failed}")
    print(f"📂 {OUTPUT_DIR}/")
    print()
    print("Sıradaki:")
    print("  hugo server -D")
    print("=" * 60)


if __name__ == "__main__":
    main()
