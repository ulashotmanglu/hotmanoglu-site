---
title: "Tarihte İlk: Hackerlar AI ile Zero-Day Zafiyet Üretti, Google Son Anda Engelledi"
date: 2026-05-12
draft: false
categories: ["Teknoloji"]
tags: ["Yapay Zeka", "Siber Güvenlik", "Google", "Zero-Day", "Hacking"]
description: "Google Threat Intelligence Group dün tarihte ilk kez bir suç grubunun yapay zeka kullanarak zero-day exploit geliştirdiğini doğruladı. Hedef: popüler bir sistem yönetim aracının iki faktörlü kimlik doğrulamasını atlatmak. Toplu saldırı planlanıyordu. Google son anda yakaladı."
image: "/img/posts/tarihte-ilk-hackerlar-ai-ile-zero-day-zafiyet-uretti-google-son-anda-engelledi.png"
---

Google'ın Threat Intelligence Group (GTIG) dün yayınladığı raporda siber güvenlik tarihinde bir ilki belgeledi. Bir suç grubu, yapay zeka modelini kullanarak daha önce bilinmeyen bir güvenlik açığı (zero-day) keşfetti ve bu açığı silaha dönüştürdü. Hedef büyüktü: toplu bir exploit operasyonu. Binlerce sisteme aynı anda saldırı.

Google bunu son anda yakaladı. Etkilenen yazılım sağlayıcısıyla koordineli çalışarak zafiyet yamalandı ve saldırı başlamadan engellendi.

GTIG Baş Analisti John Hultquist'in ifadesi durumu özetliyor: "AI zafiyet yarışının yaklaştığı yanılgısı var. Gerçek şu ki yarış çoktan başladı. AI'a izini sürebildiğimiz her zero-day için muhtemelen dışarıda daha fazlası var."


## Ne Oldu?

GTIG araştırmacıları, bir siber suç grubunun toplu zafiyet exploit operasyonu planladığını tespit etti. Operasyonla ilişkili exploit'ler analiz edildiğinde bir Python betiği ortaya çıktı. Bu betik, popüler bir açık kaynak web tabanlı sistem yönetim aracında iki faktörlü kimlik doğrulamayı (2FA) atlatmayı sağlıyordu.

Zafiyet teknik olarak bir "semantic logic flaw" yani anlamsal mantık hatasıydı. Yazılımın geliştiricileri belirli bir güven varsayımını kodun içine sabit olarak yazmıştı (hard-coded trust assumption). Bu varsayım uygulamanın kimlik doğrulama mantığıyla çelişiyordu. Sonuç: geçerli kullanıcı bilgilerine sahip olan birisi 2FA'yı tamamen atlayabiliyordu.

Google ne yazılımın ne de suç grubunun adını açıkladı. Ama güvenlik açığının yamalandığını ve toplu saldırının büyük olasılıkla engellendiğini doğruladı.


## AI Kullanıldığının Kanıtları

GTIG, exploit'in AI tarafından üretildiğine "yüksek güvenle" (high confidence) inanıyor. Kanıtlar kodun yapısında gizli.

Python betiği, bir insan geliştiricinin exploit koduna asla eklemeyeceği unsurlar içeriyordu. Eğitim amaçlı açıklama satırları (educational docstrings). Var olmayan, halüsine edilmiş bir CVSS skoru. Yapılandırılmış, ders kitabı formatında Python kodu. Detaylı yardım menüleri. Temiz ANSI renk sınıfları. Bunların hepsi büyük dil modellerinin eğitim verileriyle tutarlı kalıplar.

Bir insan hacker exploit kodu yazarken açıklama satırı eklemez, CVSS skoru yazmaz, yardım menüsü oluşturmaz. Bunlar LLM çıktısının parmak izleri.

Google, kendi Gemini modelinin veya Anthropic'in Mythos modelinin kullanılmadığından emin olduğunu belirtti. Ama hangi AI modelinin kullanıldığını açıklamadı. Piyasada OpenClaw ve OneClaw gibi güvenlik araştırması için tasarlanmış açık kaynak AI araçları mevcut ve raporda bu araçların tehdit aktörleri tarafından aktif olarak kullanıldığı belgeleniyor.


## Neden Önemli?

Bu vaka üç nedenle çığır açıcı.

Birincisi: AI artık sadece yardımcı değil, keşifçi. Daha önceki vakalarda hackerlar AI'ı mevcut zafiyetleri analiz etmek veya exploit kodunu iyileştirmek için kullanıyordu. Bu vakada AI, daha önce bilinmeyen bir zafiyeti kendisi keşfetti. Yani AI artık bilinen sorunları işlemiyor, bilinmeyen sorunları buluyor.

İkincisi: keşfedilen zafiyet türü dikkat çekici. Bellek bozulması veya hatalı girdi doğrulama gibi teknik hatalar değil, anlamsal bir mantık hatası. Geliştiricinin bir güven varsayımını yanlış kodlaması. Bu tür hatalar genellikle kodun bütünsel mantığını anlayan ve sorgulayan birisi tarafından bulunur. LLM'ler tam da bu tür üst düzey mantık hatalarını tespit etmekte giderek daha iyi hale geliyor.

Üçüncüsü: ölçek. Bu tek bir hedefi vurmak için tasarlanmış bir saldırı değildi. Toplu exploit operasyonu planlanıyordu. Binlerce sisteme aynı anda saldırı. Siber suçlular zero-day'leri genellikle hızlı, geniş çaplı saldırılarda kullanır çünkü zafiyet yamalanmadan önce mümkün olduğunca fazla sisteme sızmak isterler.


## Devlet Destekli Gruplar Ne Yapıyor?

Google'ın raporu sadece bu tek vakayla sınırlı değil. Daha geniş bir tablo çiziyor.

Kuzey Kore bağlantılı APT45 grubu, AI'a binlerce tekrarlayan sorgu göndererek zafiyetleri analiz ediyor ve proof-of-concept exploit'leri doğruluyor. Manuel olarak yönetilmesi pratik olmayan bir cephanelik oluşturuyor.

Çin bağlantılı UNC2814 grubu, Gemini'nin güvenlik bariyerlerini aşmaya çalışıyor. "Gömülü sistemlerde uzmanlaşmış güvenlik uzmanı" rolü vererek modeli TP-Link yönlendiricilerindeki uzaktan kod çalıştırma zafiyetlerini araştırmaya yönlendirmeye çalıştı.

Rusya bağlantılı aktörler iki malware ailesi (CANFAIL ve LONGSTREAM) geliştirdi. Bu malware'ler AI tarafından üretilen sahte kod blokları içeriyor. Amaç: gerçek zararlı kodu, anlamsız ama meşru görünen kodun içine gömerek tespitten kaçınmak. CANFAIL'in içinde LLM'nin açıkça "bu kullanılmayan dolgu kodudur" yazdığı yorumlar var. Yani tehdit aktörü modelden kasıtlı olarak büyük hacimli gereksiz kod üretmesini istemiş.


## Tedarik Zinciri Saldırısı: LiteLLM

Raporun bir başka dikkat çekici bulgusu tedarik zinciri tarafında. Mart 2026'da TeamPCP (UNC6780) adlı bir siber suç grubu, popüler AI gateway kütüphanesi LiteLLM'in GitHub depolarını ele geçirdi. PyPI paketlerine ve zararlı pull request'lere SANDCLOCK adlı bir kimlik bilgisi çalan yazılım yerleştirdi.

Çalınan bilgiler: AWS anahtarları ve GitHub token'ları. Bu bilgiler fidye yazılımı gruplarıyla ortaklık kurularak paraya çevrildi.

LiteLLM bir AI gateway kütüphanesi. Birçok kuruluş bu kütüphaneyi farklı AI sağlayıcılarına bağlanmak için kullanıyor. Bu kütüphanedeki API sırlarının çalınması, saldırganlara kuruluşun AI ortamına doğrudan erişim sağlıyor.

Bu, DeepMind'ın "AI Agent Traps" araştırmasında teorik olarak tartışılan senaryonun pratikte gerçekleşmesi. AI altyapısı artık bir saldırı yüzeyi.


## Türkiye Bağlamı

Türkiye'de kamu ve özel sektörde web tabanlı sistem yönetim araçları yaygın olarak kullanılıyor. Webmin, cPanel, Plesk gibi araçlar binlerce sunucuda aktif. Bu araçlardan herhangi birinde 2FA atlatma zafiyeti varsa ve bir suç grubu bunu toplu olarak exploit ederse, Türkiye'deki altyapı da hedef olabilir.

GTIG raporunun en önemli mesajı Türk siber güvenlik ekipleri için şu: AI destekli zafiyet keşfi artık gerçek. Yama yönetimi (patch management) her zamankinden daha kritik. Bir zafiyet açıklandığında yama uygulamak için artık haftalar değil, saatler var. Çünkü AI, exploit üretim süresini dramatik olarak kısaltıyor.

Ve savunma tarafı da AI kullanmak zorunda. Google'ın kendi Big Sleep ajanı ve CodeMender aracı savunma amaçlı zafiyet keşfi ve otomatik yama üretimi yapıyor. AI hızında saldırıya insan hızında savunma yetişmiyor.


## Sonuç

Google'ın dünkü raporu bir milat. Yapay zekanın zero-day zafiyet keşfettiği ve silaha dönüştürdüğü ilk doğrulanmış vaka.

Kanıtlar kodun içinde gizliydi. Halüsine edilmiş CVSS skoru. Ders kitabı formatında Python. Eğitim amaçlı açıklama satırları. Bir insan bu şekilde exploit yazmaz. Ama bir LLM yazar.

Hultquist'in sözleri tekrar etmeye değer: "Muhtemelen buzdağının görünen kısmı. Ve kesinlikle son değil."

Yarış başladı. Ve artık her iki tarafta da yapay zeka var. Saldırganlar AI ile zafiyet buluyor. Savunmacılar AI ile zafiyet yamalıyor. Arada kalan zaman penceresi her geçen gün daralıyor.

Google bu sefer pencereyi kapattı. Bir sonraki sefer kim kapatacak?
