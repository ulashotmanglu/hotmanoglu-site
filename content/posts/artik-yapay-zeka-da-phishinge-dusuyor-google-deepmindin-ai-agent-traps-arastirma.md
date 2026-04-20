---
title: "Artık Yapay Zeka da Phishing'e Düşüyor: Google DeepMind'ın \"AI Agent Traps\" Araştırması"
date: 2026-04-20
draft: false
categories: ["Analiz"]
tags: ["Yapay Zeka", "Siber Güvenlik", "Google DeepMind", "AI Agent", "Fraud"]
description: "Google DeepMind, otonom AI ajanlarını hedef alan 6 saldırı kategorisi belirledi. HTML'e gizlenen komutlar yüzde 86 başarı oranıyla ajanları ele geçiriyor. Tek bir manipüle edilmiş e-posta Microsoft Copilot'un tüm gizli verisini sızdırdı."
image: "/img/posts/artik-yapay-zeka-da-phishinge-dusuyor-google-deepmindin-ai-agent-traps-arastirma.png"
---

Yapay zeka ajanları artık sadece sorulara cevap vermiyor. İnternette geziyor, e-postaları okuyor, alışveriş yapıyor, API'lerle etkileşiyor, işlem onaylıyor. Bu otonom yetenekler yapay zekayı güçlü kılıyor. Ama aynı yetenekler onu savunmasız da yapıyor.

Google DeepMind araştırmacıları Nisan 2026'da "AI Agent Traps" başlıklı bir makale yayınladı. Bu, otonom AI ajanlarına yönelik saldırıları sistematik olarak sınıflandıran ilk akademik çerçeve. Ve bulguları rahatsız edici: web siteleri, e-postalar ve dijital kaynaklar, ziyaret eden AI ajanlarını manipüle etmek, kandırmak ve silah olarak kullanmak için tasarlanabiliyor.

Başka bir deyişle: artık sadece insanlar phishing'e düşmüyor. Yapay zeka da düşüyor.


## 6 Tuzak Kategorisi

DeepMind araştırmacıları Matija Franklin, Nenad Tomasev, Julian Jacobs, Joel Z. Leibo ve Simon Osindero, AI ajanlarının çalışma döngüsünün her aşamasını hedef alan altı tuzak kategorisi belirledi. Her biri farklı bir zafiyeti exploit ediyor.

Birinci kategori: İçerik Enjeksiyonu (Content Injection Traps). Bu, insanın gördüğü ile AI'ın ayrıştırdığı arasındaki farkı kullanıyor. Bir web sayfasının HTML'inde, CSS'inde veya meta verilerinde gizlenen komutlar, insan ziyaretçiye görünmüyor ama AI ajanı bunları talimat olarak algılıyor. HTML yorumlarına, erişilebilirlik etiketlerine veya görünmez CSS'e yerleştirilen yönergeler, ajana "şu veriyi şuraya gönder" diyebiliyor. WASP benchmark testlerine göre bu basit enjeksiyonlar yüzde 86 başarı oranına ulaşıyor.

İkinci kategori: Anlamsal Manipülasyon (Semantic Manipulation Traps). Komut enjekte etmek yerine, metni çerçeveleme, otorite sinyalleri ve duygusal yüklü dil ile doldurarak ajanın muhakemesini çarpıtmak. Büyük dil modelleri insanlarla aynı bilişsel önyargıları gösteriyor. Aynı bilgiyi farklı şekilde sunmak, ajanın çıktısını dramatik olarak değiştirebiliyor.

Üçüncü kategori: Bilişsel Durum Tuzakları (Cognitive State Traps). AI ajanlarının uzun süreli hafıza olarak kullandığı veritabanlarını zehirlemek. RAG (Retrieval-Augmented Generation) bilgi tabanına birkaç optimize edilmiş belge enjekte etmek, ajanın belirli sorgulara verdiği cevapları güvenilir şekilde yönlendirmeye yetiyor. Yüzde 80'in üzerinde başarı oranı. Ve veri kontaminasyonu yüzde 0.1'in altında. Yani neredeyse tespit edilemez.

Dördüncü kategori: Davranışsal Kontrol Tuzakları (Behavioral Control Traps). Ajanın ne yaptığını doğrudan ele geçirmek. Araştırmacılar somut bir vaka sunuyor: tek bir manipüle edilmiş e-posta, Microsoft M365 Copilot'un güvenlik sınıflandırıcılarını aşmasını ve tüm ayrıcalıklı bağlamını sızdırmasını sağladı. 10 denemede 10 başarı. Columbia Üniversitesi ve Maryland Üniversitesi araştırmacıları bu tür saldırıların "uygulaması önemsiz derecede kolay" olduğunu ve "sıfır makine öğrenimi uzmanlığı gerektirdiğini" belirtti.

Beşinci kategori: Sistemik Tuzaklar (Systemic Traps). Çoklu ajan sistemlerini hedef alan saldırılar. Bir orkestratör ajan, alt ajanlar oluşturabiliyorsa, saldırgan zehirlenmiş bir sistem komutuyla çalışan sahte bir "kritik ajan" başlatabilir. Başarı oranı yüzde 58 ile 90 arasında. Ve en tehlikeli senaryo: sahte bir finansal rapor, birden fazla ticaret ajanında eşzamanlı satış tetikleyebilir. Dijital bir flash crash.

Altıncı kategori: İnsan Denetçi Tuzakları (Human-in-the-Loop Traps). AI ajanının insan denetçisinin bilişsel önyargılarını exploit etmek. Ajan, kararlarını insana onaylatıyor ama sunuş şekli manipüle edilmiş. İnsan "onay" düğmesine basıyor çünkü ajan öyle çerçevelemiş.


## Neden Bu Kadar Tehlikeli?

Bu tuzakların tehlikesi üç katmanlı.

Birincisi, ölçek. AI ajanları otomatik çalışıyor. Bir insanı dolandırmak için zaman ve emek harcamak gerekiyor. Ama bir tuzak web sayfası kurup beklemek yeterli. Binlerce AI ajanı o sayfayı ziyaret edebilir ve hepsi aynı tuzağa düşebilir.

İkincisi, görünmezlik. İçerik enjeksiyonu tuzaklarında, insan sayfayı ziyaret ettiğinde hiçbir şey anormal görünmüyor. Tuzak sadece AI ajanının ayrıştırdığı katmanda var. Dolayısıyla geleneksel güvenlik incelemesi bunu yakalamaz.

Üçüncüsü, etki alanı. AI ajanları artık finansal işlemler yapıyor, e-posta gönderiyor, API'lere bağlanıyor, veritabanlarını sorguluyor. Ele geçirilen bir ajan sadece veri sızdırmıyor, aktif olarak zarar verebiliyor. Sahte sipariş onaylayabilir, yetkisiz transfer başlatabilir, gizli bilgileri dışarı gönderebilir.


## Finansal Sistemler İçin Ne Anlama Geliyor?

DeepMind'ın araştırması doğrudan finans sektörünü ilgilendiriyor. Ve bu bağlantı teorik değil.

Araştırmada beşinci kategori olan sistemik tuzaklar kapsamında şu senaryo tartışılıyor: sahte bir finansal rapor, birden fazla otonom ticaret ajanında eşzamanlı satış emri tetikliyor. Sonuç: dijital bir flash crash. Piyasada ani ve yapay bir çöküş.

Bu senaryo gerçekçi mi? 2010'da gerçek bir flash crash yaşandı. O zaman neden yüksek frekanslı ticaret algoritmalarıydı. Şimdi AI ticaret ajanları çok daha yaygın ve çok daha otonom. Manipüle edilmiş bir haber kaynağı, sahte bir kazanç raporu veya zehirlenmiş bir veri akışı, bu ajanları senkronize hareket ettirmek için yeterli olabilir.

Bankacılık tarafında ise AI ajanları giderek daha fazla kullanılıyor. Müşteri hizmetleri, işlem izleme, dolandırıcılık tespiti, uyum kontrolleri. Bu ajanlardan herhangi biri ele geçirilirse ne olur? Dolandırıcılık tespit sistemi tuzağa düşüp gerçek dolandırıcılığı görmezden gelebilir. Uyum kontrol ajanı manipüle edilip riskli bir işlemi onaylayabilir.

OpenAI'ın Aralık 2025'te yaptığı bir itiraf durumu özetliyor: "Prompt injection muhtemelen hiçbir zaman tamamen çözülmeyecek." Ve şu anda hiçbir yasa, ele geçirilen bir AI ajanının gerçekleştirdiği finansal suçun sorumluluğunu tanımlamıyor.


## Türkiye Bağlamı

Türk bankalarında AI kullanımı hızla yaygınlaşıyor. Chatbotlar, otomatik müşteri hizmetleri, kredi değerlendirme modelleri, işlem izleme sistemleri. Bu araçların çoğu şu anda "ajan" düzeyinde otonom değil ama o yöne gidiyor.

Soru şu: bu araçlar internetten veri çekiyorsa, harici kaynaklarla etkileşiyorsa, e-postaları işliyorsa, DeepMind'ın tanımladığı tuzaklara karşı savunmasız mı? Bir AI müşteri hizmetleri botu, müşteriden gelen manipüle edilmiş bir mesajla güvenlik protokollerini atlatabilir mi? Bir otomatik uyum tarama aracı, zehirlenmiş bir veritabanından yanlış bilgi çekebilir mi?

Bu sorular henüz Türkiye'de geniş çapta tartışılmıyor. Ama dünya bu tartışmayı yapıyor. Ve DeepMind'ın çerçevesi, bu tartışmanın temelini oluşturuyor.


## Sonuç

Google DeepMind'ın "AI Agent Traps" araştırması bir uyandırma çağrısı. Yapay zeka ajanlarını güçlü kılan her şey — otonom karar alma, internet erişimi, araç kullanımı, bellek — aynı zamanda onu savunmasız kılıyor.

Ve savunmasızlık noktaları şaşırtıcı derecede basit. HTML yorumuna gizlenmiş bir komut. Zehirlenmiş bir belge. Manipüle edilmiş bir e-posta. Bunlar sofistike saldırılar değil. Araştırmacıların ifadesiyle "uygulaması önemsiz derecede kolay" ve "sıfır makine öğrenimi uzmanlığı gerektiriyor."

Yüzde 86 başarı oranı. 10'da 10 veri sızdırma. Yüzde 0.1'in altında kontaminasyonla hafıza zehirleme.

Yapay zeka dünyası şu anda yeteneklere odaklanıyor. Ne yapabilir, ne kadar hızlı yapabilir, ne kadar ucuza yapabilir. Ama DeepMind'ın araştırması farklı bir soruyu gündeme getiriyor: yapay zeka ne kadar kolay kandırılabilir?

Cevap: çok kolay. Ve bu, 2026'nın en rahatsız edici teknolojik gerçeklerinden biri.
