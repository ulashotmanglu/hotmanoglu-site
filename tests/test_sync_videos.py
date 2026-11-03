"""scripts/sync_videos.py için ağ gerektirmeyen testler.
Çalıştırma: python3 -m unittest discover -s tests -p 'test_*.py'"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import sync_videos as sv  # noqa: E402

FEED = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns:yt="http://www.youtube.com/xml/schemas/2015" xmlns:media="http://search.yahoo.com/mrss/" xmlns="http://www.w3.org/2005/Atom">
 <entry>
  <yt:videoId>LeySei7I0aM</yt:videoId>
  <title>6,3 milyar dolar, yaklaşık 20 dakikada. Kayıtlardaki en büyük kripto soygunu olabilir. #Shorts</title>
  <published>2026-10-31T14:00:00+00:00</published>
  <media:group><media:description>6,3 milyar dolar, yaklaşık 20 dakikada. Kayıtlardaki en büyük kripto soygunu olabilir.

Source: TRM Labs</media:description></media:group>
 </entry>
 <entry>
  <yt:videoId>bad id!</yt:videoId>
  <title>x</title><published>2026-10-31T14:00:00+00:00</published>
 </entry>
</feed>"""


class SyncVideosTest(unittest.TestCase):
    def test_feed_parsing(self):
        [v] = sv.parse_feed(FEED)  # geçersiz id atlanır
        self.assertEqual(v["id"], "LeySei7I0aM")
        self.assertEqual(v["headline"], "6,3 milyar dolar, yaklaşık 20 dakikada")
        self.assertNotIn("#Shorts", v["title"])
        self.assertEqual(v["published"], "2026-10-31T14:00:00Z")

    def test_utc_normalizes_offsets(self):
        self.assertEqual(sv.utc("2026-11-02T07:19:49-08:00"), "2026-11-02T15:19:49Z")

    def test_headline_strips_emoji_and_falls_back_when_long(self):
        self.assertEqual(sv.headline("t", "Sevgili gerçek değildi 😳 Devamı."), "Sevgili gerçek değildi Devamı")
        long = "a " * 80 + "."
        self.assertEqual(sv.headline("Kısa başlık #Shorts", long), "Kısa başlık")

    def test_merge_keeps_old_and_sorts_newest_first(self):
        old = [{"id": "AAAAAAAAAAA", "published": "2026-10-01T00:00:00Z", "title": "eski"}]
        new = [{"id": "BBBBBBBBBBB", "published": "2026-10-02T00:00:00Z", "title": "yeni"},
               {"id": "AAAAAAAAAAA", "published": "2026-10-01T00:00:00Z", "title": "güncel"}]
        out = sv.merge(old, new)
        self.assertEqual([v["id"] for v in out], ["BBBBBBBBBBB", "AAAAAAAAAAA"])
        self.assertEqual(out[1]["title"], "güncel")

    def test_watch_page_rejects_other_video(self):
        html = 'var ytInitialPlayerResponse = {"videoDetails":{"videoId":"OTHERIDxxxx","title":"t"}};var x'
        with self.assertRaises(ValueError):
            sv.parse_watch(html, "LeySei7I0aM")


if __name__ == "__main__":
    unittest.main()
