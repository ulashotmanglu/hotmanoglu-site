---
title: "Dijital Müfettiş Geliyor: AI Forensics Nedir, Ne Değildir?"
date: 2026-03-21
draft: false
categories: ["Analiz"]
tags: ["Yapay Zeka", "AML", "Fraud", "Compliance", "Teknoloji"]
description: "Compliance ekiplerinin kronik sorunu alert yığılması. AI Forensics bu soruna farklı bir yerden yaklaşıyor: tespit değil, soruşturma."
image: ""
---

Compliance'ta herkesin bildiği ama kimsenin çözemediği bir sorun var: alert yığılması.

Sistemler alarm üretiyor. Çok fazla alarm. Analistler inceliyor. Çoğu yanlış alarm çıkıyor. Ama her birini incelemek zorundasın çünkü düzenleyici öyle bekliyor. Sonuç? Ekipler sürekli geride kalıyor, backlog büyüyor, gerçekten şüpheli işlemler gürültünün içinde kayboluyor.

Rakam şu: legacy AML sistemlerinin ürettiği alarmların yüzde 90 ila 95'i false positive. Bu Wipro'nun araştırması, benim uydurduğum bir rakam değil. Yani her 100 alarmdan en fazla 5-10 tanesi gerçekten şüpheli bir şeye işaret ediyor. Geri kalan 90'ı analistin zamanını yiyor.

Bu probleme genellikle "daha iyi tespit" tarafından yaklaşılıyor. Daha akıllı kurallar yazalım, eşik değerleri ayarlayalım, machine learning ile false positive'leri azaltalım. Bunların hepsi doğru ve gerekli. Ama son birkaç ayda farklı bir yaklaşım dikkatimi çekti: tespit tarafını değil, soruşturma tarafını otomatize etmek. Buna "AI Forensics" deniyor.


## Ne Demek Bu?

Flagright'ın CTO'su Madhu Nadig geçen hafta PYMNTS'e verdiği röportajda bunu güzel özetledi. Diyor ki: "AI forensics, her biri belirli bir soruşturma görevini yerine getirmek için tasarlanmış özel AI ajanları ailesidir. Dijital müfettişler olarak düşünün. Kurumunuzun standart operasyon prosedürlerini aynen takip ediyorlar, tıpkı analistlerinizin yaptığı gibi. Ama bunu otonom olarak, ölçeklenebilir şekilde ve saniyeler içinde yapıyorlar."

Yani mesele şu: kural tabanlı sistem bir alarm üretiyor. Diyelim ki "bu hesapta son 30 günde 10.000 doların üzerinde nakit işlem var." Alarm doğru, kural çalışmış. Ama bu alarmın anlamını değerlendirmek için bir analistin o hesabın geçmişine bakması, müşteri profilini incelemesi, daha önceki işlem kalıplarıyla karşılaştırması, varsa ek bilgi toplaması ve sonuçta "bu şüpheli mi değil mi" kararını vermesi gerekiyor.

İşte AI Forensics bu katmana giriyor. Tespit değil, tespit sonrası. Alarmı üreten sistem değişmiyor. Alarmı soruşturan süreç değişiyor.


## Nasıl Çalışıyor?

En ilginç kısmı bu aslında. Sistem, kurumun kendi SOP'larına (Standart Operasyon Prosedürleri) göre yapılandırılıyor. Yani genel bir "AI modeli" değil. Bankanın kendi soruşturma adımlarını takip eden, o kuruma özel bir dijital müfettiş.

Nadig'in anlattığına göre süreç şöyle işliyor: kurum SOP dokümanını sisteme yüklüyor. AI ajanı bu dokümanı okuyor ve soruşturma adımlarını otomatik olarak yapılandırıyor. Hangi veri kaynaklarına bakılacak, hangi kontroller yapılacak, hangi kriterlere göre karar verilecek — hepsi SOP'tan geliyor.

Sonra iki modda çalışabiliyor. Birincisi yarı otonom mod: AI ajanı veri topluyor, özet hazırlıyor, bulgularını sunuyor, son kararı analist veriyor. İkincisi tam otonom mod: düşük riskli alarmlar için AI ajanı soruşturmayı baştan sona yapıp kapatıyor, insan müdahalesine gerek kalmıyor.

Nadig bir örnek veriyor: "Bir analistin ortalama alarm soruşturma süresi 5 dakika diyelim. AI ajanı bunu 1 dakikaya düşürebilir. Ve eğer 100.000 alarm backlogunuz varsa, düşük riskli olanlar için bu ajanları otonom olarak çalıştırabilirsiniz. Dakikalar içinde backlog temizlenir."

Kulağa fazla iyimser gelebilir. Ama mantığı anlaşılır: düşük riskli, pattern'ı net, konteksti basit alarmlar için gerçekten bir insan analistin 5 dakika harcamasına gerek var mı? Muhtemelen yok.


## Ne Değildir?

Burada dikkatli olmak lazım. AI Forensics kural tabanlı sistemlerin yerine geçmiyor. Nadig bunu açıkça söylüyor: "Kurallar düşman değil. 10.000 doların üzerindeki nakit işlemi işaretle diyen iyi yazılmış bir kural hızlıdır, şeffaftır ve düzenleyici beklentiyi karşılar."

Sorun kuralda değil, kuralın ürettiği alarmın arkasındaki süreçte. Kural sana "burada bir şey var" diyor. Ama o "şeyin" ne olduğunu anlamak için soruşturma gerekiyor. AI Forensics soruşturma katmanında devreye giriyor.

Bu ayrım önemli çünkü regülatörler kural tabanlı izleme beklentisinden vazgeçmedi. FATF hâlâ risk bazlı yaklaşım ve transaction monitoring bekliyor. MASAK hâlâ şüpheli işlem bildirimi bekliyor. AI burada kuralı değil, kuralın arkasındaki iş yükünü hafifletiyor.

Bir de şeffaflık meselesi var. "AI öyle dedi" cevabı düzenleyiciler için kabul edilebilir değil. Neden bu alarm kapatıldı, hangi verilere bakıldı, hangi sonuca nasıl ulaşıldı — bunların hepsinin açıklanabilir olması gerekiyor. SOP bazlı çalışan bir sistem bu açıdan avantajlı çünkü adımlar önceden tanımlı ve izlenebilir.


## Peki Bu Gerçekçi mi?

Dürüst olmak gerekirse, kavram çekici ama pratikte birçok soru işareti var.

Birincisi, SOP kalitesi. Eğer kurumun SOP'ları zaten yetersizse, AI ajanı yetersiz prosedürleri çok hızlı bir şekilde takip edecek. Çöp girerse çöp çıkar. Bu, AI'ın genel bir sınırlaması ama burada özellikle kritik çünkü sonuçta düzenleyici raporlama ve hukuki sorumluluk söz konusu.

İkincisi, "düşük risk" tanımı. Hangi alarmlar otonom kapatılabilir, hangilerinde insan kararı şart? Bu sınırı kim çiziyor? Yanlış çizilirse, gerçekten şüpheli bir işlem otonom olarak kapatılabilir. Risk iştahı kurumdan kuruma değişir ama hata payı çok düşük.

Üçüncüsü, regülatör kabulü. MASAK, BDDK veya herhangi bir düzenleyici "bu alarmları AI kapattı" dediğinizde ne tepki verir? Henüz bu konuda net bir düzenleyici çerçeve yok. FCA Supercharged AI Sandbox'ta bu tip çözümleri test ediyor ama Türkiye'de böyle bir sandbox mevcut değil.

Dördüncüsü, veri kalitesi. AI ajanının doğru soruşturma yapması için doğru veriye erişmesi lazım. Türk bankacılık sisteminde veri siloları hâlâ yaygın. Core banking, kart sistemi, dijital kanallar, müşteri şikayet sistemi — bunlar çoğu zaman birbirleriyle konuşmuyor. AI ajanı silolar arasında veri toplayamıyorsa, soruşturma kalitesi düşer.


## Türkiye'de Neredeyiz?

Açık konuşmak gerekirse, erken aşamadayız.

Büyük Türk bankaları machine learning tabanlı fraud tespit modelleri kullanıyor. Özellikle kart dolandırıcılığı ve online bankacılık fraud'unda ML modelleri yaygınlaştı. Ama AML tarafında — transaction monitoring, alarm soruşturması, SAR hazırlama — çoğu kurum hâlâ kural tabanlı sistemlerle çalışıyor.

Bunun nedeni sadece teknolojik değil. Düzenleyici beklenti de belirleyici. MASAK'ın mevcut çerçevesi, AI tabanlı soruşturmayı açıkça ne teşvik ediyor ne de yasaklıyor. Bu belirsizlik, bankaların "bekle gör" modunda kalmasına yol açıyor.

Ama şunu da söylemek lazım: alert overload Türkiye'de de gerçek bir sorun. Özellikle dijital bankacılığın ve anlık ödeme sistemlerinin yaygınlaşmasıyla alarm hacimleri artıyor. Compliance ekiplerinin büyüklüğü ise aynı oranda artmıyor. Bu gerilim er ya da geç bir çözüm arayışını zorunlu kılacak.


## Benim Değerlendirmem

AI Forensics kavramı henüz olgun değil. Ama işaret ettiği yön doğru.

Compliance'ın geleceği, daha fazla insan istihdam etmek değil. Mevcut insanları daha yüksek değerli işlere yönlendirmek. Bir analistin günde 200 düşük riskli alarmı inceleyip "sorun yok" demesinin kimseye faydası yok. O analistin zamanını, gerçekten karmaşık ve şüpheli vakalara harcaması gerekiyor.

AI Forensics — ya da ona benzer yaklaşımlar — bu dönüşümün aracı olabilir. Ama bu aracın düzgün çalışması için SOP'ların sağlam olması, veri altyapısının yeterli olması, regülatör kabulün netleşmesi ve insan gözetiminin korunması gerekiyor.

Sonuçta dijital müfettiş, insan müfettişin yerini almıyor. İnsan müfettişin yaptığı işin en sıkıcı kısmını devralıyor. Ve o sıkıcı kısım, bugün compliance ekiplerinin zamanının büyük çoğunluğunu yiyor.

Bu değişecek. Soru ne zaman, nasıl ve kimin öncülüğünde.
