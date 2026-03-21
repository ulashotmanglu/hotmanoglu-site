---
title: "Dijital Analist Geliyor: AI Forensics Nedir, Ne Değildir?"
date: 2026-03-21
draft: false
categories: ["Analiz"]
tags: ["Yapay Zeka", "AML", "Fraud", "Compliance", "Teknoloji"]
description: "Compliance ekiplerinin kronik sorunu alert yÄ±ÄÄ±lmasÄ±. AI Forensics bu soruna farklÄ± bir yerden yaklaÅÄ±yor: tespit deÄil, soruÅturma."
image: ""
---

Compliance'ta herkesin bildiÄi ama kimsenin Ã§Ã¶zemediÄi bir sorun var: alert yÄ±ÄÄ±lmasÄ±.

Sistemler alarm Ã¼retiyor. Ãok fazla alarm. Analistler inceliyor. ÃoÄu yanlÄ±Å alarm Ã§Ä±kÄ±yor. Ama her birini incelemek zorundasÄ±n Ã§Ã¼nkÃ¼ dÃ¼zenleyici Ã¶yle bekliyor. SonuÃ§? Ekipler sÃ¼rekli geride kalÄ±yor, backlog bÃ¼yÃ¼yor, gerÃ§ekten ÅÃ¼pheli iÅlemler gÃ¼rÃ¼ltÃ¼nÃ¼n iÃ§inde kayboluyor.

Rakam Åu: legacy AML sistemlerinin Ã¼rettiÄi alarmlarÄ±n yÃ¼zde 90 ila 95'i false positive. Bu Wipro'nun araÅtÄ±rmasÄ±, benim uydurduÄum bir rakam deÄil. Yani her 100 alarmdan en fazla 5-10 tanesi gerÃ§ekten ÅÃ¼pheli bir Åeye iÅaret ediyor. Geri kalan 90'Ä± analistin zamanÄ±nÄ± yiyor.

Bu probleme genellikle "daha iyi tespit" tarafÄ±ndan yaklaÅÄ±lÄ±yor. Daha akÄ±llÄ± kurallar yazalÄ±m, eÅik deÄerleri ayarlayalÄ±m, machine learning ile false positive'leri azaltalÄ±m. BunlarÄ±n hepsi doÄru ve gerekli. Ama son birkaÃ§ ayda farklÄ± bir yaklaÅÄ±m dikkatimi Ã§ekti: tespit tarafÄ±nÄ± deÄil, soruÅturma tarafÄ±nÄ± otomatize etmek. Buna "AI Forensics" deniyor.


## Ne Demek Bu?

Flagright'Ä±n CTO'su Madhu Nadig geÃ§en hafta PYMNTS'e verdiÄi rÃ¶portajda bunu gÃ¼zel Ã¶zetledi. Diyor ki: "AI forensics, her biri belirli bir soruÅturma gÃ¶revini yerine getirmek iÃ§in tasarlanmÄ±Å Ã¶zel AI ajanlarÄ± ailesidir. Dijital mÃ¼fettiÅler olarak dÃ¼ÅÃ¼nÃ¼n. Kurumunuzun standart operasyon prosedÃ¼rlerini aynen takip ediyorlar, tÄ±pkÄ± analistlerinizin yaptÄ±ÄÄ± gibi. Ama bunu otonom olarak, Ã¶lÃ§eklenebilir Åekilde ve saniyeler iÃ§inde yapÄ±yorlar."

Yani mesele Åu: kural tabanlÄ± sistem bir alarm Ã¼retiyor. Diyelim ki "bu hesapta son 30 gÃ¼nde 10.000 dolarÄ±n Ã¼zerinde nakit iÅlem var." Alarm doÄru, kural Ã§alÄ±ÅmÄ±Å. Ama bu alarmÄ±n anlamÄ±nÄ± deÄerlendirmek iÃ§in bir analistin o hesabÄ±n geÃ§miÅine bakmasÄ±, mÃ¼Återi profilini incelemesi, daha Ã¶nceki iÅlem kalÄ±plarÄ±yla karÅÄ±laÅtÄ±rmasÄ±, varsa ek bilgi toplamasÄ± ve sonuÃ§ta "bu ÅÃ¼pheli mi deÄil mi" kararÄ±nÄ± vermesi gerekiyor.

Ä°Åte AI Forensics bu katmana giriyor. Tespit deÄil, tespit sonrasÄ±. AlarmÄ± Ã¼reten sistem deÄiÅmiyor. AlarmÄ± soruÅturan sÃ¼reÃ§ deÄiÅiyor.


## NasÄ±l ÃalÄ±ÅÄ±yor?

En ilginÃ§ kÄ±smÄ± bu aslÄ±nda. Sistem, kurumun kendi SOP'larÄ±na (Standart Operasyon ProsedÃ¼rleri) gÃ¶re yapÄ±landÄ±rÄ±lÄ±yor. Yani genel bir "AI modeli" deÄil. BankanÄ±n kendi soruÅturma adÄ±mlarÄ±nÄ± takip eden, o kuruma Ã¶zel bir dijital mÃ¼fettiÅ.

Nadig'in anlattÄ±ÄÄ±na gÃ¶re sÃ¼reÃ§ ÅÃ¶yle iÅliyor: kurum SOP dokÃ¼manÄ±nÄ± sisteme yÃ¼klÃ¼yor. AI ajanÄ± bu dokÃ¼manÄ± okuyor ve soruÅturma adÄ±mlarÄ±nÄ± otomatik olarak yapÄ±landÄ±rÄ±yor. Hangi veri kaynaklarÄ±na bakÄ±lacak, hangi kontroller yapÄ±lacak, hangi kriterlere gÃ¶re karar verilecek â hepsi SOP'tan geliyor.

Sonra iki modda Ã§alÄ±Åabiliyor. Birincisi yarÄ± otonom mod: AI ajanÄ± veri topluyor, Ã¶zet hazÄ±rlÄ±yor, bulgularÄ±nÄ± sunuyor, son kararÄ± analist veriyor. Ä°kincisi tam otonom mod: dÃ¼ÅÃ¼k riskli alarmlar iÃ§in AI ajanÄ± soruÅturmayÄ± baÅtan sona yapÄ±p kapatÄ±yor, insan mÃ¼dahalesine gerek kalmÄ±yor.

Nadig bir Ã¶rnek veriyor: "Bir analistin ortalama alarm soruÅturma sÃ¼resi 5 dakika diyelim. AI ajanÄ± bunu 1 dakikaya dÃ¼ÅÃ¼rebilir. Ve eÄer 100.000 alarm backlogunuz varsa, dÃ¼ÅÃ¼k riskli olanlar iÃ§in bu ajanlarÄ± otonom olarak Ã§alÄ±ÅtÄ±rabilirsiniz. Dakikalar iÃ§inde backlog temizlenir."

KulaÄa fazla iyimser gelebilir. Ama mantÄ±ÄÄ± anlaÅÄ±lÄ±r: dÃ¼ÅÃ¼k riskli, pattern'Ä± net, konteksti basit alarmlar iÃ§in gerÃ§ekten bir insan analistin 5 dakika harcamasÄ±na gerek var mÄ±? Muhtemelen yok.


## Ne DeÄildir?

Burada dikkatli olmak lazÄ±m. AI Forensics kural tabanlÄ± sistemlerin yerine geÃ§miyor. Nadig bunu aÃ§Ä±kÃ§a sÃ¶ylÃ¼yor: "Kurallar dÃ¼Åman deÄil. 10.000 dolarÄ±n Ã¼zerindeki nakit iÅlemi iÅaretle diyen iyi yazÄ±lmÄ±Å bir kural hÄ±zlÄ±dÄ±r, ÅeffaftÄ±r ve dÃ¼zenleyici beklentiyi karÅÄ±lar."

Sorun kuralda deÄil, kuralÄ±n Ã¼rettiÄi alarmÄ±n arkasÄ±ndaki sÃ¼reÃ§te. Kural sana "burada bir Åey var" diyor. Ama o "Åeyin" ne olduÄunu anlamak iÃ§in soruÅturma gerekiyor. AI Forensics soruÅturma katmanÄ±nda devreye giriyor.

Bu ayrÄ±m Ã¶nemli Ã§Ã¼nkÃ¼ regÃ¼latÃ¶rler kural tabanlÄ± izleme beklentisinden vazgeÃ§medi. FATF hÃ¢lÃ¢ risk bazlÄ± yaklaÅÄ±m ve transaction monitoring bekliyor. MASAK hÃ¢lÃ¢ ÅÃ¼pheli iÅlem bildirimi bekliyor. AI burada kuralÄ± deÄil, kuralÄ±n arkasÄ±ndaki iÅ yÃ¼kÃ¼nÃ¼ hafifletiyor.

Bir de ÅeffaflÄ±k meselesi var. "AI Ã¶yle dedi" cevabÄ± dÃ¼zenleyiciler iÃ§in kabul edilebilir deÄil. Neden bu alarm kapatÄ±ldÄ±, hangi verilere bakÄ±ldÄ±, hangi sonuca nasÄ±l ulaÅÄ±ldÄ± â bunlarÄ±n hepsinin aÃ§Ä±klanabilir olmasÄ± gerekiyor. SOP bazlÄ± Ã§alÄ±Åan bir sistem bu aÃ§Ä±dan avantajlÄ± Ã§Ã¼nkÃ¼ adÄ±mlar Ã¶nceden tanÄ±mlÄ± ve izlenebilir.


## Peki Bu GerÃ§ekÃ§i mi?

DÃ¼rÃ¼st olmak gerekirse, kavram Ã§ekici ama pratikte birÃ§ok soru iÅareti var.

Birincisi, SOP kalitesi. EÄer kurumun SOP'larÄ± zaten yetersizse, AI ajanÄ± yetersiz prosedÃ¼rleri Ã§ok hÄ±zlÄ± bir Åekilde takip edecek. ÃÃ¶p girerse Ã§Ã¶p Ã§Ä±kar. Bu, AI'Ä±n genel bir sÄ±nÄ±rlamasÄ± ama burada Ã¶zellikle kritik Ã§Ã¼nkÃ¼ sonuÃ§ta dÃ¼zenleyici raporlama ve hukuki sorumluluk sÃ¶z konusu.

Ä°kincisi, "dÃ¼ÅÃ¼k risk" tanÄ±mÄ±. Hangi alarmlar otonom kapatÄ±labilir, hangilerinde insan kararÄ± Åart? Bu sÄ±nÄ±rÄ± kim Ã§iziyor? YanlÄ±Å Ã§izilirse, gerÃ§ekten ÅÃ¼pheli bir iÅlem otonom olarak kapatÄ±labilir. Risk iÅtahÄ± kurumdan kuruma deÄiÅir ama hata payÄ± Ã§ok dÃ¼ÅÃ¼k.

ÃÃ§Ã¼ncÃ¼sÃ¼, regÃ¼latÃ¶r kabulÃ¼. MASAK, BDDK veya herhangi bir dÃ¼zenleyici "bu alarmlarÄ± AI kapattÄ±" dediÄinizde ne tepki verir? HenÃ¼z bu konuda net bir dÃ¼zenleyici Ã§erÃ§eve yok. FCA Supercharged AI Sandbox'ta bu tip Ã§Ã¶zÃ¼mleri test ediyor ama TÃ¼rkiye'de bÃ¶yle bir sandbox mevcut deÄil.

DÃ¶rdÃ¼ncÃ¼sÃ¼, veri kalitesi. AI ajanÄ±nÄ±n doÄru soruÅturma yapmasÄ± iÃ§in doÄru veriye eriÅmesi lazÄ±m. TÃ¼rk bankacÄ±lÄ±k sisteminde veri silolarÄ± hÃ¢lÃ¢ yaygÄ±n. Core banking, kart sistemi, dijital kanallar, mÃ¼Återi Åikayet sistemi â bunlar Ã§oÄu zaman birbirleriyle konuÅmuyor. AI ajanÄ± silolar arasÄ±nda veri toplayamÄ±yorsa, soruÅturma kalitesi dÃ¼Åer.


## TÃ¼rkiye'de Neredeyiz?

AÃ§Ä±k konuÅmak gerekirse, erken aÅamadayÄ±z.

BÃ¼yÃ¼k TÃ¼rk bankalarÄ± machine learning tabanlÄ± fraud tespit modelleri kullanÄ±yor. Ãzellikle kart dolandÄ±rÄ±cÄ±lÄ±ÄÄ± ve online bankacÄ±lÄ±k fraud'unda ML modelleri yaygÄ±nlaÅtÄ±. Ama AML tarafÄ±nda â transaction monitoring, alarm soruÅturmasÄ±, SAR hazÄ±rlama â Ã§oÄu kurum hÃ¢lÃ¢ kural tabanlÄ± sistemlerle Ã§alÄ±ÅÄ±yor.

Bunun nedeni sadece teknolojik deÄil. DÃ¼zenleyici beklenti de belirleyici. MASAK'Ä±n mevcut Ã§erÃ§evesi, AI tabanlÄ± soruÅturmayÄ± aÃ§Ä±kÃ§a ne teÅvik ediyor ne de yasaklÄ±yor. Bu belirsizlik, bankalarÄ±n "bekle gÃ¶r" modunda kalmasÄ±na yol aÃ§Ä±yor.

Ama Åunu da sÃ¶ylemek lazÄ±m: alert overload TÃ¼rkiye'de de gerÃ§ek bir sorun. Ãzellikle dijital bankacÄ±lÄ±ÄÄ±n ve anlÄ±k Ã¶deme sistemlerinin yaygÄ±nlaÅmasÄ±yla alarm hacimleri artÄ±yor. Compliance ekiplerinin bÃ¼yÃ¼klÃ¼ÄÃ¼ ise aynÄ± oranda artmÄ±yor. Bu gerilim er ya da geÃ§ bir Ã§Ã¶zÃ¼m arayÄ±ÅÄ±nÄ± zorunlu kÄ±lacak.


## Benim DeÄerlendirmem

AI Forensics kavramÄ± henÃ¼z olgun deÄil. Ama iÅaret ettiÄi yÃ¶n doÄru.

Compliance'Ä±n geleceÄi, daha fazla insan istihdam etmek deÄil. Mevcut insanlarÄ± daha yÃ¼ksek deÄerli iÅlere yÃ¶nlendirmek. Bir analistin gÃ¼nde 200 dÃ¼ÅÃ¼k riskli alarmÄ± inceleyip "sorun yok" demesinin kimseye faydasÄ± yok. O analistin zamanÄ±nÄ±, gerÃ§ekten karmaÅÄ±k ve ÅÃ¼pheli vakalara harcamasÄ± gerekiyor.

AI Forensics â ya da ona benzer yaklaÅÄ±mlar â bu dÃ¶nÃ¼ÅÃ¼mÃ¼n aracÄ± olabilir. Ama bu aracÄ±n dÃ¼zgÃ¼n Ã§alÄ±ÅmasÄ± iÃ§in SOP'larÄ±n saÄlam olmasÄ±, veri altyapÄ±sÄ±nÄ±n yeterli olmasÄ±, regÃ¼latÃ¶r kabulÃ¼n netleÅmesi ve insan gÃ¶zetiminin korunmasÄ± gerekiyor.

SonuÃ§ta dijital mÃ¼fettiÅ, insan mÃ¼fettiÅin yerini almÄ±yor. Ä°nsan mÃ¼fettiÅin yaptÄ±ÄÄ± iÅin en sÄ±kÄ±cÄ± kÄ±smÄ±nÄ± devralÄ±yor. Ve o sÄ±kÄ±cÄ± kÄ±sÄ±m, bugÃ¼n compliance ekiplerinin zamanÄ±nÄ±n bÃ¼yÃ¼k Ã§oÄunluÄunu yiyor.

Bu deÄiÅecek. Soru ne zaman, nasÄ±l ve kimin Ã¶ncÃ¼lÃ¼ÄÃ¼nde.
