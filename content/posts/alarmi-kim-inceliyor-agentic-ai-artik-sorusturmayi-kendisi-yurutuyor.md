---
title: "Alarmı Kim İnceliyor? Agentic AI Artık Soruşturmayı Kendisi Yürütüyor"
date: 2026-07-15
draft: false
categories: ["Teknoloji"]
tags: ["Agentic AI", "Yapay Zeka", "İşlem İzleme", "AML", "Uyum", "RegTech"]
description: "Agentic AI artık AML soruşturmasını uçtan uca yürütüyor. Rakamlar pilot aşamasını geçti ama otonomi tek başına yeterli değil. Açıklanabilirlik ve döngüde insan neden şart, uygulayıcı gözünden anlatıyor."
image: "/img/posts/alarmi-kim-inceliyor-agentic-ai-artik-sorusturmayi-kendisi-yurutuyor.png"
---

AML dünyasında uzun süredir sorulan soru şuydu: "Yapay zekanız var mı?" 2026'da bu soru anlamını yitirdi. Artık doğru soru şu: Yapay zeka gerçekten işi yapıyor mu, yoksa sadece analistin işini kolaylaştırıyor mu?

Sektör son iki yılda üç aşamadan geçti. Önce tahmine dayalı modeller geldi, alarmları risk sırasına diziyordu. Sonra üretken yapay zeka copilot'ları geldi, analiste özet çıkarıyor, bağlam sağlıyordu. Şimdi üçüncü aşamadayız. Agentic AI, yani ajan tabanlı yapay zeka. Bu sistemler alarmı sadece işaretlemiyor, soruşturmanın kendisini uçtan uca yürütüyor.

Bu ayrım kritik, çünkü uyum ekiplerinin en büyük derdi hiçbir zaman çaba eksikliği olmadı. Dert, analistin önüne düşen alarm hacminin insan kapasitesini aşması. Geleneksel AML sistemlerinde alarmların yüzde 95'e varan kısmı false positive. Tek bir şüpheli işlem bildirimi hazırlamak dört gün veya daha fazla sürebiliyor. Alarm hacmi büyüdükçe analist darboğaza dönüşüyor.

## Ajan Ne Yapıyor

Klasik copilot mantığında analist her vakaya dokunuyordu, sadece daha hızlı dokunuyordu. Ajan tabanlı yaklaşım farklı. L1 yani birinci seviye rutin vakaları analiste hiç ulaşmadan kendisi kapatıyor. Analist yalnızca eskalasyona, sınır vakalara ve nihai kararlara odaklanıyor.

Bir alarm geldiğinde ajan şunları otonom yapıyor. Alarm bağlamını topluyor, işlem geçmişini çekiyor, kişiyi yaptırım ve izleme listelerine karşı kontrol ediyor, karşı taraf ilişkilerini analiz ediyor, alarmı kurumun kendi standart operasyon prosedürlerine göre değerlendiriyor, bir soruşturma anlatısı taslağı yazıyor ve nihayetinde bir öneride bulunuyor. Üstelik tüm bunları, bir insan analist vakayı açmadan önce yapıyor ve muhakeme zincirinin tamamını görünür bırakıyor. Analist inceliyor, gerekirse geçersiz kılıyor, onaylıyor.

Tam kapsamlı vakalarda ise ajan, analistin en çok zaman harcadığı delil toplama işini üstleniyor. Kişi ağlarını genişletiyor, bağlantılı hesapları yüzeye çıkarıyor, farklı zaman dilimlerindeki ilişkili aktiviteleri eşleştiriyor ve soruşturma zaman çizelgesini kuruyor.

## Rakamlar Ne Diyor

Bu artık pilot aşamasında bir hikaye değil. Üretimde, gerçek ölçekte çalışan örnekler var.

Unit21'in ağında bugün 200'den fazla kurum yer alıyor ve platform aylık 4,5 milyardan fazla olayı izliyor, yarım milyondan fazla alarmı işliyor. Çarpıcı bir istatistik daha var. ABD'de düzenlenen tüm şüpheli işlem bildirimlerinin yaklaşık yüzde 5'i bu platformdan geçiyor.

Somut kurum sonuçları da açıklandı. Kripto şirketi Nexo, alarm incelemelerinin yüzde 57'sini yapay zeka ajanlarıyla otomatikleştirdi ve bu oranı yüzde 80'e çıkarmayı hedefliyor. Aynı dönemde eski kurum içi izleme sistemine kıyasla false positive oranını yüzde 90'ın üzerinde düşürdü. Underdog adlı platform alarm hacmini yüzde 72 azalttı. Uphold soruşturma süresini yüzde 44 kısalttı. Platform genelinde kurumlar false positive oranında yüzde 93'e varan düşüş ve soruşturma süresinde yüzde 80'e varan hızlanma raporluyor.

Bu rakamların ortak noktası şu. Ekip büyütmeden, yani ilave personel almadan daha fazla finansal suçun önüne geçilmesi. Alarm kuyruğunu yönetmek ile kuyruğu tümüyle eritmek arasındaki fark burada ortaya çıkıyor.

## Ama Otonomi Tek Başına Yeterli Değil

İşin cazip tarafı bu rakamlar. Ama asıl kritik nokta, çoğu kurumun bu sistemleri henüz tam üretime almamış olması ve bunun iyi bir gerekçesi olması.

Yeterli koruma önlemi olmadan ajana fazla otonomi vermek doğrudan risk demek. Sektördeki erken denemelerin çoğu zayıf modeller yüzünden değil, zayıf guardrail yani sınır kuralları yüzünden başarısız oluyor. En sık görülen hata "halüsinasyon gören soruşturmacı" dediğimiz durum. Ajana çok fazla bağlam ve fazla açık uçlu talimat verildiğinde ajan uydurmaya başlıyor.

Bu yüzden regülatör iki şeyi net şart koşuyor. Birincisi açıklanabilir yapay zeka. Ajan her kararı için okunabilir bir muhakeme zinciri sunmak zorunda. İkincisi human-in-the-loop, yani döngüde insan. Ajan hız ve bağlam sağlar ama nihai sorumluluk uyum görevlisinde kalır. Otomasyon hesap verebilirliği ortadan kaldırmıyor.

Risk seviyesine göre de eşik değişiyor. Rutin işlem izleme triyajında ajana geniş alan tanınabilir. Ama yaptırım taraması ve PEP yani siyasi nüfuz sahibi kişi kontrolü söz konusu olduğunda otonom karar önerilmiyor. Bu alanlarda insan müdahale eşiği düşük tutuluyor ve zorunlu üst düzey inceleme isteniyor, çünkü buradaki bir hata anında düzenleyici sonuç doğuruyor.

Bir başka kritik unsur da denetim izi. Her disposition, her eskalasyon, her doğrulanmış sonuç sisteme geri besleniyor ve ajanı zamanla keskinleştiriyor. Bu geri besleme döngüsü sayesinde sistem, tipolojiler değiştikçe kendini uyarlıyor. Hatta geçmiş kararları analiz edip ekibin farkında bile olmadığı eşik ayarlarını öneriyor.

## Uyum ve Denetim Ekipleri İçin Ne Anlama Geliyor

Bu dönüşüm, bir öncekiyle birlikte okununca daha anlamlı hale geliyor. Bir yanda yanlış konumlanmış tek bir eşiğin yıllarca yüzlerce milyon dolarlık şüpheli işlemi görünmez kıldığı vakalar var. Diğer yanda ise soruşturmanın tamamını dakikalar içinde kuran, muhakemesini şeffaf biçimde ortaya koyan ve her kararı denetime hazır tutan bir mimari yükseliyor.

Ama teknoloji tek başına çözüm değil. Ajan mimarisi ancak net politikalar, eğitimli personel, sağlam kontroller ve güçlü denetim izleri içeren bir yapının içine oturduğunda değer üretiyor. En etkili model, yapay zekayı bağımsız bir çözüm olarak değil, iyi yönetişilen ve insan liderliğindeki bir uyum çerçevesinin içine gömülü akıllı bir katman olarak konumlandıran model.

Türkiye açısından da tablo doğrudan uygulanabilir. Bankaların ve fintech şirketlerinin uyum ekipleri aynı alarm hacmi baskısıyla, aynı false positive yüküyle boğuşuyor. Ama burada bir güvenlik boyutu daha var. Banka verisi hassas veri. Bu yüzden yerel ve kurum içi çalışan çözümler, veri güvenliği gereksinimleriyle çok daha uyumlu. Ajan mimarisini kurarken sorulacak sorular da aynı. Ajan her kararının gerekçesini gösterebiliyor mu? Nihai karar hâlâ insanda mı? Yaptırım ve PEP tarafında zorunlu insan incelemesi var mı? Denetim izi eksiksiz mi?

Ajanın alarmı incelemesi bir kolaylık. Ama o incelemenin arkasında savunulabilir bir muhakeme, izlenen bir sorumluluk ve eksiksiz bir kayıt yoksa, elimizde hızlı bir asistan olabilir ama regülatöre karşı duran bir kontrol olmaz.
