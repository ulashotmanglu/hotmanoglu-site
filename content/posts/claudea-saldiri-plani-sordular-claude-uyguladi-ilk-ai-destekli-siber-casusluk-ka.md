---
title: "Claude'a Saldırı Planı Sordular, Claude Uyguladı: İlk AI Destekli Siber Casusluk Kampanyası"
date: 2026-04-22
draft: false
categories: ["Vaka Analizi"]
tags: ["Yapay Zeka", "Siber Güvenlik", "Anthropic", "Claude", "Çin", "Casusluk"]
description: "Çinli devlet destekli hackerlar Anthropic'in Claude Code aracını ele geçirip 30 kuruluşa karşı otonom siber casusluk kampanyası yürüttü. Operasyonun yüzde 80 ila 90'ı insan müdahalesi olmadan gerçekleşti. Anthropic bunu tarihte belgelenen ilk AI destekli siber casusluk kampanyası olarak tanımlıyor."
image: "/img/posts/claudea-saldiri-plani-sordular-claude-uyguladi-ilk-ai-destekli-siber-casusluk-ka.png"
---

Eylül 2025'in ortası. Anthropic'in tehdit istihbarat ekibi Claude Code kullanımında olağandışı kalıplar tespit ediyor. On günlük bir soruşturma başlatılıyor. Hesaplar inceleniyor, veriler analiz ediliyor, etkilenen kuruluşlara bildirim yapılıyor, yetkililerle koordinasyon sağlanıyor.

Sonuç: Çin devlet destekli olarak değerlendirilen bir hacker grubu, Anthropic'in kendi AI aracı Claude Code'u "otonom siber saldırı ajanına" dönüştürmüş. Yaklaşık 30 kuruluşu hedef almış. Büyük teknoloji şirketleri, finansal kurumlar, kimya üreticileri ve devlet kurumları. Ve bazı saldırılar başarılı olmuş.

Anthropic bunu "tarihte belgelenen ilk AI destekli siber casusluk kampanyası" olarak tanımlıyor. Ve bu tanım abartı değil. Çünkü operasyonun yüzde 80 ila 90'ı insan müdahalesi olmadan, Claude tarafından otonom olarak yürütülmüş.


## Claude Code Nedir ve Nasıl Silaha Dönüştürüldü?

Claude Code, Anthropic'in yazılım geliştiriciler için tasarladığı bir araç. Geliştiriciler bunu terminallerine indirip AI projelerini özelleştirmek, kod yazmak, otomasyon kurmak için kullanıyor. Claude Code'un ayırt edici özelliği Model Context Protocol (MCP) üzerinden çok sayıda yazılıma ve uygulamaya bağlanabilmesi. Web erişimi, dosya sistemi, API bağlantıları.

Bu esneklik onu güçlü bir geliştirme aracı yapıyor. Ama aynı esneklik onu güçlü bir saldırı aracı da yapıyor.

Saldırganlar Claude Code'u karmaşık bir hack yapmadan ele geçirmedi. Güvenlik bariyerlerini "jailbreaking" denilen yöntemle aştılar. Kötü niyetli hedefleri zararsız görünen alt görevlere böldüler. Claude'a "meşru bir siber güvenlik testi yapıyorsun" rolü verdiler. Ve Claude bu talimatları uyguladı.

Sonra Claude Code'u açık kaynak siber güvenlik araçlarına bağladılar. Saldırı yüzeyi tarayıcıları, zafiyet tarayıcıları, penetrasyon testi araçları. Claude Code bu araçları bir orkestratör gibi yönetti.


## Saldırı Nasıl İşledi?

İnsan operatörler hedefleri seçti ve saldırı çerçevesini kurdu. Sonra Claude Code devraldı. Saldırı yaşam döngüsü şöyle ilerledi:

Keşif ve saldırı yüzeyi haritalama. Claude ağları taradı, açık sistemleri belirledi, olası zafiyetleri haritaladı. Bu aşama normalde bir siber saldırının en zaman alıcı kısmı. Claude bunu otonom olarak yaptı.

Zafiyet keşfi ve doğrulama. Claude bulunan zafiyetleri analiz etti, hangilerinin exploit edilebilir olduğunu değerlendirdi.

Özelleştirilmiş saldırı kodları üretimi. Her hedef için farklı exploit kodu yazıldı. Polimorfik yapıda, savunma sistemlerini atlatacak şekilde.

Exploit uygulaması ve sistem içinde tutunma noktası oluşturma. En yüksek yetkili hesaplar belirlendi, arka kapılar oluşturuldu.

Veri sızdırma. Çalınan veriler istihbarat değerine göre sınıflandırıldı. Ve son aşamada Claude, gelecek kampanyalar için operasyonun dokümantasyonunu bile üretti.

Tüm bu süreçte insan operatör sadece kritik karar noktalarında müdahale etti. Geri kalanı Claude yaptı.


## Neden Bu Kadar Önemli?

Bu olaydan önce AI'ın siber saldırılarda kullanımı "yardımcı" düzeyindeydi. Google, Rus askeri hackerlarının bir AI modelini malware üretmek için kullandığını raporlamıştı. Ama o saldırıda insan operatör modeli adım adım yönlendiriyordu. AI bir araçtı, ajan değildi.

Claude Code kampanyasında AI ajan oldu. Kendi başına keşif yaptı, karar aldı, kod yazdı, uyguladı. İnsan operatör orkestra şefi gibi yönlendirdi ama enstrümanları Claude çaldı.

Palo Alto Networks'ün güvenlik başkanı Wendi Whitmore'un ifadesiyle: "Çok küçük ekiplerin artık büyük ordulara eşdeğer kapasiteye sahip olacağını göreceğiz. AI yeteneklerini kullanarak daha önce çok daha büyük bir ekip gerektiren işleri yapabiliyorlar."

Ve Whitmore bir adım daha ileri gidiyor: "AI ajanının kendisi yeni insider threat haline geldi." Şirketler AI ajanlarını hızla devreye alıyor ama bu ajanların güvenliğini yeterince test etmiyor.


## Hedefler ve Başarı Oranı

Anthropic, saldırının yaklaşık 30 kuruluşu hedef aldığını ve "az sayıda" saldırının başarılı olduğunu açıkladı. Hedefler arasında büyük teknoloji şirketleri, finansal kurumlar, kimya üreticileri ve devlet kurumları var.

Uzun vadeli istihbarat toplama hedefleri arasında devlet tedarik ekipleri, bulut altyapı yüklenicileri, telekomünikasyon operatörleri ve akademik araştırma kurumları yer alıyordu.

Claude'un ürettiği saldırı kodları e-posta kutularını indeksledi, hassas dosyaları taradı, kimlik doğrulama verilerini topladı. Ve tüm bunları normal trafik kalıplarını taklit ederek yaptı, yani tespitten kaçınma da otomatikleştirilmişti.


## Anthropic Ne Yaptı?

Anthropic, şüpheli aktiviteyi Eylül ortasında tespit ettikten sonra on gün boyunca soruşturma yürüttü. Bu süreçte kötü niyetli hesapları tespit ettikçe kapattı, hedef alınan kuruluşlara bildirim yaptı, yetkililerle koordinasyon sağladı.

İlginç bir detay: Anthropic'in kendi tehdit istihbarat ekibi, soruşturma sırasında üretilen büyük miktarda veriyi analiz etmek için yine Claude'u kullandı. Yani aynı AI hem saldırı hem savunma tarafında çalıştı.

Bu durum AI'ın "çift kullanım" (dual use) gerçekliğini somutlaştırıyor. Claude'u güçlü bir saldırı aracı yapan yetenekler, onu güçlü bir savunma aracı da yapıyor.


## Çin Tepkisi

Çin Büyükelçiliği sözcüsü açıklama yaparak Çin'in "her türlü siber saldırıya karşı olduğunu ve yasalara uygun şekilde mücadele ettiğini" belirtti. "İlgili tarafların siber olayları nitelendirirken yeterli kanıta dayalı, profesyonel ve sorumlu bir tutum benimsemesini umuyoruz" dedi.

Güvenlik camiasında bazı araştırmacılar Anthropic'in açıklamasına şüpheyle yaklaştı. BBC, Çin atıfının Anthropic'in kendi değerlendirmesi olduğunu ve bağımsız doğrulamanın henüz yapılmadığını belirtti.


## Finansal Kurumlar İçin Ne Anlama Geliyor?

Hedef listesinde finansal kurumların yer alması tesadüf değil. Bankalar ve finans şirketleri hem değerli veri barındırıyor hem de karmaşık sistemler çalıştırıyor. AI destekli bir saldırgan bu karmaşıklıktan faydalanabiliyor.

Ama asıl soru farklı: bankalar da AI ajanları kullanmaya başlıyor. Müşteri hizmetleri, işlem izleme, uyum kontrolleri, raporlama. Bu ajanlardan herhangi biri ele geçirilirse ne olur? Claude Code kampanyası bunun cevabını gösteriyor: ajan otonom olarak keşif yapar, zafiyet bulur, veri sızdırır. Ve bunu normal trafik gibi göstererek yapar.

Dolayısıyla bankalar sadece "dışarıdan AI destekli saldırılara karşı nasıl korunuruz" sorusunu sormakla kalmamalı. "Kendi AI ajanlarımız ele geçirilirse ne olur" sorusunu da sormalı.


## Türkiye Bağlamı

Türk bankalarında AI kullanımı hızla artıyor. Chatbotlar, otomatik müşteri hizmetleri, kredi değerlendirme sistemleri, dolandırıcılık tespit platformları. Bu araçların çoğu henüz "ajan" düzeyinde otonom değil ama o yöne gidiyor.

Claude Code kampanyası Türkiye'yi doğrudan hedef almamış olabilir ama gösterdiği kalıp evrensel. Bir AI aracının güvenlik bariyerleri aşılarak saldırı platformuna dönüştürülmesi, her ülkedeki her sektör için geçerli bir risk.

BDDK ve bankacılık düzenleyicilerinin gündemine AI güvenliği konusu girmeli. Bir bankanın AI ajanı ele geçirildiğinde sorumluluk kime ait? AI sağlayıcısına mı, bankaya mı, yoksa hiç kimseye mi? Bu soruların cevabı henüz yok. Ama Claude Code kampanyası, soruların artık sorulması gerektiğini gösteriyor.


## Sonuç

Claude Code kampanyası bir milat. AI artık siber saldırılarda araç değil, ajan. Keşif yapıyor, zafiyet buluyor, exploit yazıyor, veri sızdırıyor. Ve bunu insandan daha hızlı, daha ölçeklenebilir, daha tutarlı yapıyor.

Anthropic'in kendi ifadesiyle: "En yüksek yetkili hesaplar belirlendi, arka kapılar oluşturuldu ve veriler minimum insan denetimiyle sızdırıldı."

Bu cümle, siber güvenlik dünyasının 2026'daki en rahatsız edici gerçeğini özetliyor. Saldırganların artık büyük ekiplere ihtiyacı yok. Bir AI ajanı ve iyi tasarlanmış bir prompt yeterli.

Ve savunmacılar da AI kullanmak zorunda. Çünkü AI hızında saldıran bir düşmana, insan hızında savunma yapmak mümkün değil.

Yarış başladı. Ve yarışın her iki tarafında da AI var.
