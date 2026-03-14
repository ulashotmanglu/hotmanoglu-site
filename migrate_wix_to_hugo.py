#!/usr/bin/env python3
"""
hotmanoglu.com Wix → Hugo Migrasyon Scripti
============================================
Bu script Wix sitesindeki tüm blog yazılarını çeker ve
Hugo-uyumlu Markdown dosyalarına dönüştürür.

Kullanım:
    pip install requests beautifulsoup4
    python3 migrate_wix_to_hugo.py

Çıktı: content/posts/ klasörüne .md dosyaları
"""

import requests
from bs4 import BeautifulSoup
import re
import os
import time
import unicodedata
from urllib.parse import unquote, urlparse
from datetime import datetime

SITE_URL = "https://www.hotmanoglu.com"
OUTPUT_DIR = "content/posts"
IMG_DIR = "static/img/posts"

# Türkçe ay isimleri → sayı
TR_MONTHS = {
    "oca": 1, "şub": 2, "mar": 3, "nis": 4, "may": 5, "haz": 6,
    "tem": 7, "ağu": 8, "eyl": 9, "eki": 10, "kas": 11, "ara": 12,
    "ocak": 1, "şubat": 2, "mart": 3, "nisan": 4, "mayıs": 5, "haziran": 6,
    "temmuz": 7, "ağustos": 8, "eylül": 9, "ekim": 10, "kasım": 11, "aralık": 12,
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
}


def slugify(text):
    """Türkçe uyumlu slug oluştur."""
    text = text.lower().strip()
    # Türkçe karakter dönüşümü
    tr_map = str.maketrans("çğıöşüâîûÇĞİÖŞÜÂÎÛ", "cgiosuaiuCGIOSUAIU")
    text = text.translate(tr_map)
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    text = text.strip('-')
    return text[:80]


def parse_wix_date(date_text):
    """Wix tarih formatını parse et. '3 gün önce', '5 Mar', '10 Şub 2025' vs."""
    date_text = date_text.strip().lower()
    
    # "X gün önce" formatı
    match = re.search(r'(\d+)\s*gün\s*önce', date_text)
    if match:
        from datetime import timedelta
        days = int(match.group(1))
        return (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    
    # "X saat önce" formatı
    match = re.search(r'(\d+)\s*saat\s*önce', date_text)
    if match:
        return datetime.now().strftime("%Y-%m-%d")
    
    # "5 Mar" veya "5 Mar 2025" formatı
    match = re.search(r'(\d{1,2})\s+(\w+?)(?:\s+(\d{4}))?$', date_text)
    if match:
        day = int(match.group(1))
        month_str = match.group(2).lower()
        year = int(match.group(3)) if match.group(3) else datetime.now().year
        
        # Ay ismini bul
        month = None
        for key, val in TR_MONTHS.items():
            if month_str.startswith(key[:3]):
                month = val
                break
        
        if month:
            return f"{year}-{month:02d}-{day:02d}"
    
    # Fallback
    return datetime.now().strftime("%Y-%m-%d")


def guess_category(title, content=""):
    """Başlık ve içerikten kategori tahmin et."""
    text = (title + " " + content[:500]).lower()
    
    if "vaka analizi" in text or "vaka inceleme" in text:
        return "Vaka Analizi"
    elif "ofac" in text or "yaptırım" in text or "sdn" in text:
        return "Yaptırım"
    elif "fatf" in text or "aml" in text or "cft" in text or "masak" in text:
        return "AML/CFT"
    elif "düzenleme" in text or "tbmm" in text or "kanun" in text or "yönetmelik" in text:
        return "Düzenleme"
    elif "fraud" in text or "dolandırıcılık" in text or "içeriden tehdit" in text or "insider" in text:
        return "Fraud"
    else:
        return "Analiz"


def extract_tags(title, content):
    """İçerikten otomatik tag çıkar."""
    tags = set()
    text = title + " " + content
    
    keywords = {
        "OFAC": ["ofac", "sdn listesi"],
        "FATF": ["fatf"],
        "FinCEN": ["fincen"],
        "Kara Para Aklama": ["kara para", "money laundering", "aml"],
        "Yaptırım": ["yaptırım", "sanction"],
        "Kripto": ["kripto", "bitcoin", "stablecoin", "blockchain", "tron", "ethereum"],
        "Fraud": ["fraud", "dolandırıcılık"],
        "İç Tehdit": ["içeriden tehdit", "insider threat", "banka çalışanı"],
        "Rusya": ["rusya", "russia", "oligark"],
        "ABD": ["abd", "doj", "fbi", "dea"],
        "Türkiye": ["türkiye", "masak", "tbmm", "bddk", "spk"],
        "Kuzey Kore": ["kuzey kore", "dprk"],
        "Çin": ["çin bağlantılı", "china"],
        "İran": ["iran"],
        "TD Bank": ["td bank"],
        "Rüşvet": ["rüşvet", "bribe"],
    }
    
    text_lower = text.lower()
    for tag, patterns in keywords.items():
        if any(p in text_lower for p in patterns):
            tags.add(tag)
    
    return sorted(list(tags))[:6]  # Max 6 tag


def download_image(img_url, slug):
    """Wix görselini indir."""
    try:
        # Wix URL'den orijinal görseli al (daha kaliteli)
        clean_url = re.sub(r'/v1/fill/.*?/', '/v1/fill/w_1200,h_630,al_c,q_90,enc_auto/', img_url)
        
        os.makedirs(IMG_DIR, exist_ok=True)
        ext = ".jpg"
        if ".png" in img_url:
            ext = ".png"
        
        filepath = os.path.join(IMG_DIR, f"{slug}{ext}")
        
        resp = requests.get(clean_url, headers=HEADERS, timeout=15)
        if resp.status_code == 200:
            with open(filepath, 'wb') as f:
                f.write(resp.content)
            return f"/img/posts/{slug}{ext}"
    except Exception as e:
        print(f"  ⚠ Görsel indirilemedi: {e}")
    
    return ""


def fetch_all_post_urls():
    """Sitemap veya blog sayfalarından tüm yazı URL'lerini çek."""
    urls = set()
    
    # Önce sitemap dene
    print("📡 Sitemap kontrol ediliyor...")
    try:
        resp = requests.get(f"{SITE_URL}/sitemap.xml", headers=HEADERS, timeout=10)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'html.parser')
            for loc in soup.find_all('loc'):
                url = loc.text.strip()
                if '/post/' in url:
                    urls.add(url)
            if urls:
                print(f"  ✅ Sitemap'ten {len(urls)} yazı bulundu")
                return sorted(urls)
    except Exception:
        pass
    
    # Sitemap yoksa blog sayfalarını tara
    print("📡 Blog sayfaları taranıyor...")
    
    # Ana sayfa
    try:
        resp = requests.get(SITE_URL, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(resp.text, 'html.parser')
        for a in soup.find_all('a', href=True):
            href = a['href']
            if '/post/' in href:
                if href.startswith('/'):
                    href = SITE_URL + href
                urls.add(href)
    except Exception as e:
        print(f"  ⚠ Ana sayfa: {e}")
    
    # Blog sayfası
    try:
        resp = requests.get(f"{SITE_URL}/blog", headers=HEADERS, timeout=10)
        soup = BeautifulSoup(resp.text, 'html.parser')
        for a in soup.find_all('a', href=True):
            href = a['href']
            if '/post/' in href:
                if href.startswith('/'):
                    href = SITE_URL + href
                urls.add(href)
    except Exception as e:
        print(f"  ⚠ Blog: {e}")
    
    print(f"  ✅ Toplam {len(urls)} yazı bulundu")
    return sorted(urls)


def fetch_and_convert_post(url):
    """Tek bir yazıyı fetch et ve Hugo Markdown'a çevir."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.encoding = 'utf-8'
        soup = BeautifulSoup(resp.text, 'html.parser')
    except Exception as e:
        print(f"  ❌ Fetch hatası: {e}")
        return None
    
    # Başlık
    title = ""
    h1 = soup.find('h1')
    if h1:
        title = h1.get_text(strip=True)
        # "HOTMANOGLU" başlığını atla
        if title.upper() == "HOTMANOGLU":
            h1_tags = soup.find_all('h1')
            for h in h1_tags:
                t = h.get_text(strip=True)
                if t.upper() != "HOTMANOGLU":
                    title = t
                    break
    
    if not title:
        # URL'den tahmin et
        slug_part = url.split('/post/')[-1]
        title = unquote(slug_part).replace('-', ' ').title()
    
    # Tarih
    date_str = datetime.now().strftime("%Y-%m-%d")
    # Wix'te tarih genelde belirli bir class'ta oluyor
    for span in soup.find_all('span'):
        text = span.get_text(strip=True)
        if re.search(r'\d+\s*(gün|saat)\s*önce', text) or re.search(r'\d{1,2}\s+(oca|şub|mar|nis|may|haz|tem|ağu|eyl|eki|kas|ara)', text, re.I):
            date_str = parse_wix_date(text)
            break
    
    # Ana görsel
    image_path = ""
    og_image = soup.find('meta', property='og:image')
    if og_image and og_image.get('content'):
        img_url = og_image['content']
        if 'wixstatic' in img_url:
            slug = slugify(title)
            image_path = download_image(img_url, slug)
    
    # İçerik
    # Wix blog post content genelde belirli bir div içinde
    content_parts = []
    main_content_found = False
    
    # Tüm metin bloklarını bul
    for elem in soup.find_all(['p', 'h2', 'h3', 'h4', 'blockquote', 'ul', 'ol']):
        text = elem.get_text(strip=True)
        
        # Nav, footer vs. elementleri atla
        if not text or len(text) < 5:
            continue
        if text in ['Ana Sayfa', 'Hakkımda', 'Blog', 'More', 'All Posts', 'Ara', 'Etik & Uyum']:
            continue
        if 'yorum yaz' in text.lower() or 'son yazılar' in text.lower():
            continue
        if text.startswith('Hepsini Gör'):
            continue
        if 'dakikada okunur' in text:
            continue
        
        # Başlığı tekrar yazma
        if text == title:
            main_content_found = True
            continue
        
        if not main_content_found:
            # Title'ı bulduktan sonra içerik başlar
            if elem.name == 'h1':
                continue
            # İlk paragrafla başla
            if elem.name == 'p' and len(text) > 50:
                main_content_found = True
        
        if main_content_found:
            # "Son Yazılar" bölümünden sonrasını kes
            if text == "Son Yazılar" or elem.name in ['h2'] and 'son yazılar' in text.lower():
                break
            if text == "Yorumlar":
                break
            
            # Markdown formatına çevir
            if elem.name == 'h2':
                content_parts.append(f"\n## {text}\n")
            elif elem.name == 'h3':
                content_parts.append(f"\n### {text}\n")
            elif elem.name == 'h4':
                content_parts.append(f"\n#### {text}\n")
            elif elem.name == 'blockquote':
                content_parts.append(f"\n> {text}\n")
            elif elem.name in ['ul', 'ol']:
                for li in elem.find_all('li'):
                    li_text = li.get_text(strip=True)
                    if li_text:
                        prefix = "-" if elem.name == 'ul' else "1."
                        content_parts.append(f"{prefix} {li_text}")
                content_parts.append("")
            else:
                # Paragraf — bold/italic koru
                paragraph = ""
                for child in elem.children:
                    if hasattr(child, 'name'):
                        child_text = child.get_text()
                        if child.name == 'strong' or child.name == 'b':
                            paragraph += f"**{child_text}**"
                        elif child.name == 'em' or child.name == 'i':
                            paragraph += f"*{child_text}*"
                        elif child.name == 'a' and child.get('href'):
                            href = child['href']
                            if href.startswith('/'):
                                href = SITE_URL + href
                            paragraph += f"[{child_text}]({href})"
                        else:
                            paragraph += child_text
                    else:
                        paragraph += str(child)
                
                if paragraph.strip():
                    content_parts.append(paragraph.strip())
                    content_parts.append("")  # Boş satır
    
    content = "\n".join(content_parts).strip()
    
    # Çok kısaysa fallback — raw text al
    if len(content) < 100:
        # Tüm body text'i al
        body_text = soup.get_text(separator='\n')
        lines = body_text.split('\n')
        in_content = False
        fallback_parts = []
        for line in lines:
            line = line.strip()
            if line == title:
                in_content = True
                continue
            if in_content:
                if line in ['Son Yazılar', 'Yorumlar', 'bottom of page']:
                    break
                if 'dakikada okunur' in line:
                    continue
                if line and len(line) > 10:
                    fallback_parts.append(line)
                    fallback_parts.append("")
        content = "\n".join(fallback_parts).strip()
    
    # Kategori ve tag'ler
    category = guess_category(title, content)
    tags = extract_tags(title, content)
    
    # Description (ilk 160 karakter)
    first_para = content.split('\n\n')[0] if content else ""
    description = re.sub(r'[#*\[\]()]', '', first_para)[:160].strip()
    if description and not description.endswith('.'):
        description = description.rsplit(' ', 1)[0] + '...'
    
    # Slug
    slug = slugify(title)
    
    # Front matter + content
    # Title'da tırnak varsa escape et
    safe_title = title.replace('"', '\\"')
    
    md = f"""---
title: "{safe_title}"
date: {date_str}
draft: false
categories: ["{category}"]
tags: [{', '.join(f'"{t}"' for t in tags)}]
description: "{description}"
image: "{image_path}"
---

{content}
"""
    
    return {
        "slug": slug,
        "title": title,
        "date": date_str,
        "markdown": md,
    }


def main():
    print("=" * 60)
    print("🔄 hotmanoglu.com Wix → Hugo Migrasyon")
    print("=" * 60)
    print()
    
    # Klasörleri oluştur
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(IMG_DIR, exist_ok=True)
    
    # Tüm yazı URL'lerini bul
    urls = fetch_all_post_urls()
    
    if not urls:
        print("❌ Hiç yazı bulunamadı!")
        return
    
    print(f"\n📝 {len(urls)} yazı dönüştürülecek...\n")
    
    success = 0
    failed = 0
    
    for i, url in enumerate(urls, 1):
        slug_preview = unquote(url.split('/post/')[-1])[:50]
        print(f"[{i}/{len(urls)}] {slug_preview}...")
        
        result = fetch_and_convert_post(url)
        
        if result:
            filepath = os.path.join(OUTPUT_DIR, f"{result['slug']}.md")
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(result['markdown'])
            print(f"  ✅ {result['slug']}.md ({result['date']})")
            success += 1
        else:
            print(f"  ❌ Başarısız")
            failed += 1
        
        # Rate limiting — Wix'i yormamak için
        time.sleep(1.5)
    
    print()
    print("=" * 60)
    print(f"✅ Tamamlandı: {success} başarılı, {failed} başarısız")
    print(f"📂 Dosyalar: {OUTPUT_DIR}/")
    print(f"🖼  Görseller: {IMG_DIR}/")
    print()
    print("Sonraki adım:")
    print("  1. hugo server -D   → lokalde kontrol et")
    print("  2. git add . && git commit && git push   → yayınla")
    print("=" * 60)


if __name__ == "__main__":
    main()
