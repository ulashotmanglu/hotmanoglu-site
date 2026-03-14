---
title: "OFAC'tan Kripto Mikserlere Yeni Dalga: Tornado Cash Sonrası Dönem"
date: 2026-03-14
draft: false
categories: ["Yaptırım"]
tags: ["Etiketler: OFAC", "Kripto", "Yaptırım", "Tornado Cash", "Kara Para Aklama"]
description: "OFAC'ın kripto mikser hizmetlerine yönelik artan baskısı ve uyum dünyası için çıkarımlar."
image: "/img/posts/ofactan-kripto-mikserlere-yeni-dalga-tornado-cash-sonrasi-donem.png"
---

ABD Hazine Bakanlığı'nın yaptırım birimi OFAC, 2022'den bu yana kripto mikser hizmetlerine yönelik sistematik bir baskı kampanyası yürütüyor. Blender.io ile başlayan süreç, Tornado Cash kararıyla zirveye ulaştı. 2024-2025 döneminde bu baskı yeni bir evreye girdi: artık sadece platformlar değil, bu platformlarla etkileşime giren bireysel cüzdanlar ve aracı yapılar da hedefte.

## Mikser Hizmetleri Neden Hedefte?

Kripto mikserler — veya teknik adıyla "tumbler" hizmetleri — blockchain üzerindeki işlem izini kırmak için tasarlandı. Kullanıcı fonlarını bir havuza gönderir, protokol bu fonları diğer kullanıcıların fonlarıyla karıştırır ve farklı adreslerden farklı zamanlarda çıkış yapar. Sonuç: gönderici ile alıcı arasındaki bağlantı kopar.

Bu mekanizma, meşru gizlilik talebi için de kullanılabilir. Ancak OFAC'ın odağı farklı: Lazarus Group başta olmak üzere Kuzey Kore bağlantılı aktörler, bu hizmetleri yaptırım rejimlerini aşmak ve çalınan fonları aklamak için sistematik biçimde kullandı.

Rakamlar bunu doğruluyor. Chainalysis verilerine göre, 2022-2024 döneminde Kuzey Kore bağlantılı hack operasyonlarından elde edilen fonların yaklaşık 1.1 milyar doları mikser hizmetleri üzerinden geçirildi. Bu, OFAC'ın "teknik altyapıyı hedef alma" stratejisinin arkasındaki temel gerekçe.

## Tornado Cash Kararının Hukuki Boyutu

Ağustos 2022'de OFAC, Tornado Cash'i SDN listesine ekledi. Bu karar birçok açıdan emsal niteliğindeydi.

İlk kez merkezi olmayan, açık kaynak kodlu bir protokol yaptırım listesine alınıyordu. Karar, "bir yazılım yaptırıma tabi olabilir mi?" tartışmasını başlattı. Coinbase destekli bir dava açıldı, ilk derece mahkemesi OFAC lehine karar verdi, ancak temyiz mahkemesi 2024'te kararı kısmen bozdu.

Hukuki belirsizlik devam ediyor. Ancak pratik etki net: Tornado Cash ile etkileşime giren cüzdan adresleri otomatik olarak risk skoru yükseltiyor. Büyük borsalar bu adresleri izliyor ve işlem kısıtlaması uyguluyor.

## Blender.io'dan Sinbad'a: Hedefler Değişiyor, Strateji Aynı

OFAC'ın mikser stratejisi kronolojik olarak şöyle gelişti:

- **Mayıs 2022:** Blender.io SDN listesine eklendi. İlk kez bir kripto mikser doğrudan yaptırıma tabi tutuldu. Gerekçe: Lazarus Group'un Axie Infinity hack'inden elde ettiği 620 milyon doların bir kısmının bu platform üzerinden aklanması.

- **Ağustos 2022:** Tornado Cash SDN listesine eklendi. 455 milyon doların üzerinde yasadışı fonun bu protokol üzerinden geçirildiği tespit edildi.

- **Kasım 2023:** Sinbad.io yaptırıma tabi tutuldu. OFAC, Sinbad'ı doğrudan Blender.io'nun rebrand edilmiş versiyonu olarak tanımladı. Bu, operatörlerin "kapatıp yeniden açma" stratejisinin işe yaramadığını gösterdi.

Her üç vakada ortak nokta aynı: Kuzey Kore bağlantısı ve OFAC'ın "follow the money" yaklaşımıyla altyapı hedeflemesi.

## Compliance Ekipleri İçin Pratik Çıkarımlar

Bu gelişmeler, özellikle kripto borsaları ve VASP'lar için somut aksiyon gerektiriyor.

**Cüzdan tarama zorunluluğu.** SDN listesindeki akıllı kontrat adresleri ve bunlarla etkileşime girmiş cüzdanların gerçek zamanlı taranması artık temel bir beklenti. Chainalysis, Elliptic veya TRM Labs gibi araçlar bu taramayı otomatize ediyor, ancak kuralların düzenli güncellenmesi gerekiyor.

**Mikser kalıplarının izlenmesi.** Transaction monitoring sistemlerinde mikser kullanım kalıpları — eşit tutarlı çoklu transferler, zaman gecikmeli çıkışlar, yeni oluşturulmuş cüzdanlara dağıtım — ayrı bir senaryo seti olarak tanımlanmalı. Geleneksel bankacılık AML kuralları bu kalıpları yakalamakta yetersiz kalıyor.

**İkincil riskler.** Bir müşterinin doğrudan mikser kullanmamış olması yeterli değil. "Tainted funds" analizi — yani fonların geçmişte mikser hizmetinden geçip geçmediğinin kontrolü — giderek standart hale geliyor. Bu, özellikle DeFi protokollerinden gelen fonlar için kritik.

**Düzenleyici iletişim.** OFAC yaptırımları, yerel düzenleyiciler tarafından da referans alınıyor. Türkiye'de MASAK, kripto varlık hizmet sağlayıcılarından bu tür kontrolleri beklemeye başladı. SPK'nın yeni kripto düzenlemesi kapsamında bu beklentilerin formalize edilmesi muhtemel.

## Sonuç

OFAC'ın mikser stratejisi açık: altyapıyı hedef al, maliyeti artır, alternatif kaçış yollarını sistematik olarak kapat. Tornado Cash davası hukuki belirsizlik yaratmış olsa da, pratik etki tartışmasız.

Kripto compliance ekipleri için mesaj net: mikser etkileşimi artık sadece bir "risk faktörü" değil, potansiyel bir yaptırım ihlali tetikleyicisi. Programların bu gerçekliğe göre kalibre edilmesi gerekiyor.
