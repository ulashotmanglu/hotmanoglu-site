# HOTMANOGLU

[www.hotmanoglu.com](https://www.hotmanoglu.com) — teknoloji, ekonomi ve finansal suçlar üzerine bağımsız Türkçe yayın.

Hugo (extended) ile üretilir, GitHub Actions üzerinden GitHub Pages'e deploy edilir.
Özel alan adı `static/CNAME` ile bağlıdır.

```bash
hugo server --disableFastRender   # yerel geliştirme
hugo --gc --minify                # production build
```

---

## Yazı front matter

### Zorunlu alanlar (sanal-ofis publisher bu yedi alanı yazar)

```yaml
---
title: "Başlık"
date: 2026-08-03
draft: false
categories: ["Vaka Analizi"]
tags: ["OFAC", "Yaptırım"]
description: "Bir iki cümlelik özet."
image: "/img/posts/slug.png"
---
```

Bu yedi alanla yazı eksiksiz render edilir. Aşağıdaki alanların hiçbiri zorunlu
değildir; yoksa ilgili arayüz parçası hiç basılmaz.

### Opsiyonel alanlar

| Alan | Tip | Etkisi |
|---|---|---|
| `author` | string | Künyedeki yazar adı. Yoksa `content_origin`'e göre belirlenir. |
| `content_origin` | `ulas` \| `ai` \| `hybrid` | Üretim notu metni; `ulas` ise yazı Blog bölümünde listelenir ve yazar kutusu büyür. Alan yoksa geriye dönük sınıflandırma yapılmaz. |
| `updated` | tarih | Künyede "Güncellendi" ve `article:modified_time`. |
| `key_points` | string listesi | Veri olarak saklanır, yazı sayfasında gösterilmez. |
| `sources` | liste | Yazı sonunda "Kaynaklar" bölümü (aşağıya bakınız). |
| `image_alt` | string | Görsel alt metni. Yoksa görsel dekoratif sayılır (`alt=""`). |
| `image_caption` | string | Kapak görselinin altındaki açıklama. |
| `series` | string | Künyede seri etiketi. |
| `aliases` | URL listesi | Eski URL'leri bu yazıya yönlendirir. |

### `sources` — kaynak listesi

Belgelenmiş şema:

```yaml
sources:
  - title: "Kaynak başlığı"
    url: "https://..."
    publisher: "Kurum veya yayın"
    date: "2026-08-01"
    accessed: "2026-08-03"
```

`url` zorunludur; diğerleri opsiyoneldir. Davranış:

- `sources` yoksa bölüm hiç görünmez.
- `title` yoksa bağlantı metni olarak alan adı kullanılır — uzun URL ham basılmaz.
- `publisher`, `date`, `accessed` yalnızca varsa gösterilir; tarihler Türkçe biçimlenir.
- Dış bağlantılar `target="_blank" rel="noopener noreferrer"` alır.
- Liste, makale gövdesinin iki yana yaslama stilinden etkilenmez.

Geriye dönük olarak şu biçimler de kabul edilir:

```yaml
sources:
  - "https://example.com"          # düz URL
  - name: "SEC"                    # eski anahtar adları
    link: "https://..."
```

---

## Bölüm (hub) eşlemesi

Üst navigasyondaki konu bölümleri `data/sections.yaml` ile tanımlanır. Hiçbir
yazının front matter'ı değiştirilmez; eşleme yalnızca okuma sırasında yapılır.

```yaml
- key: ekonomi-finans
  title: "Ekonomi & Finans"
  nav_title: "Ekonomi"
  url: "/ekonomi-finans/"
  categories: ["Ekonomi"]
  tags: ["Enflasyon", "Fed", "OPEC", ...]
  exclude_categories: ["Fraud", "AML/CFT", "Yaptırım", "Vaka Analizi"]
  exclude_tags: ["OFAC", "FATF", ...]
```

Bir yazı, `categories` **veya** `tags` listesiyle kesişiyorsa bölümde görünür;
`exclude_categories` / `exclude_tags` ile kesişiyorsa görünmez. Dışlama alanları
opsiyoneldir ve bir bölümün konusu dışındaki içerikleri (örneğin Ekonomi'ye düşen
fraud vakalarını) kapsam dışı bırakmak için kullanılır.

`mode: all` verilen bölüm (Gündem) tüm yazıları listeler.

---

## Ana sayfa kürasyonu

`data/homepage.yaml`:

- `hero.lead` / `hero.secondary` — manşet seçimi (boşsa en yeni yazılar)
- `discover` — "Keşfet" konu girişleri; hedef URL ve içerik sayısı `section_key`
  üzerinden `data/sections.yaml`'dan hesaplanır, sabit URL yazılmaz
- `collections` — "Arşivden" bloğunun editoryal seçkisi

Bulunamayan bir yol sessizce atlanır; build kırılmaz.

---

## Görseller

Yazı görselleri `static/img/posts/<slug>.png|jpg` altındadır.
`data/imagesizes.yaml` her görselin gerçek piksel boyutunu tutar; şablonlar bunu
`width`/`height` niteliği olarak basar. Görsel eklendiğinde/değiştiğinde bu dosya
yeniden üretilmelidir:

```bash
python3 - <<'PY'
from PIL import Image; import glob, os, io
rows = {}
for f in sorted(glob.glob("static/img/posts/*")):
    if not f.lower().endswith((".png", ".jpg", ".jpeg", ".webp")): continue
    with Image.open(f) as im: rows["/img/posts/" + os.path.basename(f)] = im.size
out = ["# Otomatik üretildi.", "sizes:"]
out += [f'  "{k}": {{ w: {w}, h: {h} }}' for k, (w, h) in rows.items()]
io.open("data/imagesizes.yaml", "w", encoding="utf-8").write("\n".join(out) + "\n")
PY
```

Kayıt eksikse görünüm bozulmaz — tüm görsel kaplarında CSS `aspect-ratio` tanımlıdır.

---

## Arayüz metni kuralları

- "Editoryal" (❌ Editöryal), "Yapay Zeka" (❌ Yapay Zekâ)
- Yeni arayüz metinlerinde şapkalı `â î û` kullanılmaz; `ç ğ ı ö ş ü` korunur
- "Ulaş'tan" ifadesi kullanılmaz; kişisel bölümün adı **Blog**

Bu kurallar şablonlar, config, data dosyaları ve politika sayfaları içindir.
`content/posts/` altındaki yazı metinleri tarihsel kayıttır, toplu değiştirilmez.

---

## Asset pipeline

`assets/css/style.css` ve `assets/js/main.js`, Hugo Pipes ile minify + SHA-256
fingerprint edilerek yayımlanır (`/css/style.min.<hash>.css`). İçerik değiştiğinde
URL değişir, deploy sonrası eski cache kalmaz; `integrity` (SRI) niteliği de üretilir.
Bu dosyaları `static/` altına geri taşımayın.
