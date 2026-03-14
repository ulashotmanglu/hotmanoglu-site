# hotmanoglu.com — Deploy Rehberi

## Genel Bakış

Bu proje Hugo statik site generator kullanıyor. Markdown dosyası yazarsın → `hugo` komutu çalıştırırsın → HTML çıktı üretilir → GitHub Pages otomatik yayınlar. Wix editörüyle uğraşmak yok.

---

## ADIM 1: Hugo Kurulumu (Mac)

```bash
brew install hugo
hugo version   # v0.145+ olmalı
```

---

## ADIM 2: GitHub Repo Oluşturma

1. GitHub'da yeni repo oluştur: `hotmanoglu-site` (private olabilir)
2. Bu klasörü repo'ya bağla:

```bash
cd hotmanoglu-site
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin git@github.com:SENIN_KULLANICI_ADIN/hotmanoglu-site.git
git push -u origin main
```

---

## ADIM 3: GitHub Pages Ayarı

1. GitHub repo → **Settings** → **Pages**
2. **Source** kısmında: **GitHub Actions** seç
3. Push yaptığında otomatik build + deploy olacak

---

## ADIM 4: GoDaddy DNS Ayarları

GoDaddy hesabına gir → **DNS Management** → Mevcut Wix kayıtlarını sil ve şunları ekle:

### A Kayıtları (@ için):

| Type | Name | Value            |
|------|------|------------------|
| A    | @    | 185.199.108.153  |
| A    | @    | 185.199.109.153  |
| A    | @    | 185.199.110.153  |
| A    | @    | 185.199.111.153  |

### CNAME Kaydı (www için):

| Type  | Name | Value                                        |
|-------|------|----------------------------------------------|
| CNAME | www  | SENIN_KULLANICI_ADIN.github.io               |

### Mevcut Wix Kayıtlarını Silme

GoDaddy DNS'inde şu tarz kayıtlar varsa SİL:
- `CNAME www → ...wixdns.net`
- `A @ → ...wix IP'leri`
- Wix verification TXT kayıtları

**ÖNEMLİ:** DNS değişiklikleri 10 dakika ile 48 saat arası sürebilir. Genelde 30 dakikada aktif olur.

---

## ADIM 5: Custom Domain Doğrulama

1. GitHub repo → **Settings** → **Pages** → **Custom domain**
2. `www.hotmanoglu.com` yaz → **Save**
3. **Enforce HTTPS** kutusunu işaretle (DNS yayılınca aktif olur)

---

## GÜNLÜK KULLANIM: Yeni Yazı Ekleme

### Yeni yazı oluştur:

```bash
hugo new posts/yazi-basligi.md
```

### Markdown dosyasını düzenle:

```markdown
---
title: "Yazı Başlığı"
date: 2025-03-15
categories: ["Vaka Analizi"]
tags: ["OFAC", "Yaptırım"]
description: "Kısa açıklama (SEO ve kart açıklaması için)"
image: "/img/yazi-gorseli.jpg"
---

Yazı içeriği buraya. Normal Markdown yazabilirsin.

## Alt Başlık

Paragraf metni, **kalın**, *italik*, [link](https://ornek.com).

> Alıntı bloğu

- Liste item 1
- Liste item 2
```

### Kategori seçeneklerin:

- `Vaka Analizi` (kırmızı badge)
- `AML/CFT` (mavi badge)
- `Yaptırım` (mor badge)
- `Düzenleme` (yeşil badge)
- `Fraud` (turuncu badge)

### Görsel ekleme:

Görselleri `static/img/` klasörüne koy, yazıda şöyle referans ver:

```yaml
image: "/img/dosya-adi.jpg"
```

### Yayınla:

```bash
git add .
git commit -m "Yeni yazı: Başlık"
git push
```

Push yaptığın anda GitHub Actions otomatik build edip yayınlar. ~1 dakika içinde canlıda.

---

## YEREL TEST

Yayınlamadan önce kontrol etmek istersen:

```bash
hugo server -D
```

Tarayıcıda `http://localhost:1313` aç. Dosya değişikliklerinde otomatik yenilenir.

---

## WIX'TEN İÇERİK TAŞIMA

Wix'teki mevcut yazıları taşımak için:

1. Her yazıyı Wix'te aç
2. İçeriği kopyala
3. `content/posts/` altında yeni `.md` dosyası oluştur
4. Front matter'ı doldur (title, date, categories, tags)
5. İçeriği yapıştır (Markdown formatına çevir)

İpucu: Ben (Claude) bu taşıma işinde sana yardımcı olabilirim — Wix'teki yazılarını kopyala yapıştır yap, ben Markdown'a çevireyim.

---

## DOSYA YAPISI

```
hotmanoglu-site/
├── hugo.toml                    # Site ayarları
├── content/
│   ├── hakkimda.md              # Hakkımda sayfası
│   └── posts/                   # Blog yazıları
│       ├── yazi-1.md
│       └── yazi-2.md
├── layouts/
│   ├── _default/
│   │   ├── baseof.html          # Ana şablon
│   │   ├── list.html            # Liste sayfası
│   │   └── page.html            # Tekil sayfa
│   ├── partials/
│   │   ├── nav.html             # Navigasyon
│   │   ├── footer.html          # Alt bilgi
│   │   └── article-card.html    # Yazı kartı
│   ├── posts/
│   │   └── single.html          # Yazı detay sayfası
│   └── index.html               # Ana sayfa
├── static/
│   ├── css/style.css            # Tüm stiller
│   ├── js/main.js               # Animasyonlar
│   ├── img/                     # Görseller
│   └── CNAME                    # Domain ayarı
└── .github/
    └── workflows/
        └── hugo.yml             # Otomatik deploy
```

---

## SORUN GİDERME

**Site açılmıyor:** DNS yayılması bekle (48 saate kadar). `dig www.hotmanoglu.com` ile kontrol et.

**HTTPS çalışmıyor:** GitHub Pages → Settings → Enforce HTTPS'i tekrar aç. DNS yayılmadan çalışmaz.

**Yazı görünmüyor:** Front matter'da `draft: true` olmamalı. Tarih gelecekte olmamalı.

**Build hatası:** `hugo` komutunu lokalde çalıştır, hata mesajını oku.
