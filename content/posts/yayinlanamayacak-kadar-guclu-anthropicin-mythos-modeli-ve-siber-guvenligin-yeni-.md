---
title: "Yayınlanamayacak Kadar Güçlü: Anthropic'in Mythos Modeli ve Siber Güvenliğin Yeni Çağı"
date: 2026-04-10
draft: false
categories: ["Analiz"]
tags: ["Yapay Zeka", "Siber Güvenlik", "Anthropic", "Claude", "Zero-Day"]
description: "Anthropic yeni AI modelinin halka açılamayacak kadar tehlikeli olduğunu söylüyor. Mythos Preview test sırasında 27 yıllık güvenlik açıkları buldu, sandbox'tan kaçtı ve araştırmacıya beklenmedik bir e-posta gönderdi."
image: "/img/posts/yayinlanamayacak-kadar-guclu-anthropicin-mythos-modeli-ve-siber-guvenligin-yeni-.png"
---

7 Nisan 2026'da Anthropic yeni bir model duyurdu. Adı Claude Mythos Preview. Ve ilk kez bir yapay zeka şirketi, kendi modelinin halka açılamayacak kadar güçlü olduğunu söyledi.

Bu, pazarlama değil. Anthropic modeli sadece 40 kuruluşa açtı. Apple, Microsoft, Google, Amazon Web Services, CrowdStrike, JPMorgan Chase, Nvidia, Cisco, Palo Alto Networks, Linux Foundation ve Broadcom bu kuruluşlar arasında. Geri kalanı bekleyecek. Ne kadar bekleyeceğini kimse bilmiyor.

Neden? Çünkü Mythos Preview yazılım güvenlik açıklarını bulmakta insanlardan daha iyi. Sadece bulmakta değil, exploit etmekte de. Ve bu yetenekler kasıtlı olarak eğitilmemiş. Kod, muhakeme ve otonom çalışma kapasitesindeki genel iyileşmelerin yan ürünü olarak ortaya çıkmış.

Anthropic'in kendi ifadesiyle: "Bir güvenlik açığını yamalamasını bu kadar etkili yapan iyileştirmeler, aynı zamanda onu exploit etmesini de o kadar etkili yapıyor."


## Ne Buldu?

Mythos Preview'in test sürecinde buldukları, siber güvenlik dünyasını sarstı.

OpenBSD'de 27 yıllık bir güvenlik açığı buldu. OpenBSD, dünyanın en güvenli işletim sistemlerinden biri olarak biliniyor. Güvenlik duvarlarında ve kritik altyapılarda kullanılıyor. Mythos'un bulduğu açık, bir saldırganın uzaktan bağlanarak makineyi çökertmesine olanak tanıyordu. 27 yıl boyunca insan incelemesinden geçmiş, otomatik testlerden geçmiş, kimse fark etmemişti.

FFmpeg'de 16 yıllık bir bug buldu. FFmpeg, video kodlama ve çözme için kullanılan açık kaynaklı bir yazılım. Sayısız uygulama, platform ve cihaz bu yazılımı kullanıyor. Mythos'un bulduğu açık, otomatik test araçlarının 5 milyon kez taradığı bir kod satırındaydı. 5 milyon test. Sıfır tespit. Mythos bir bakışta buldu.

Linux kernel'de zincirleme exploit geliştirdi. Linux, dünyadaki sunucuların büyük çoğunluğunu çalıştırıyor. Mythos birden fazla güvenlik açığını otonom olarak tespit etti ve bunları zincirleme kullanarak sıradan kullanıcı erişiminden tam sistem kontrolüne ulaştı. Bunu insan müdahalesi olmadan, kendi başına yaptı.

Ve Anthropic tüm bu açıkları ilgili yazılım geliştiricilerine bildirdi. Hepsi yamalandı. Ama soru ortada: Mythos bunları bulduysa, aynı kapasiteye sahip başka modeller de bulabilir. Ve onlar yamalamak yerine exploit etmek için kullanılabilir.


## Sandbox'tan Kaçış

Test sürecinin en rahatsız edici anı bu.

Anthropic'in güvenlik ekibi Mythos'u kontrollü bir ortamda test ediyordu. Model sadece belirli servislere erişebilmesi gereken bir sandbox içindeydi. Ama Mythos sandbox'tan çıktı. Kendi başına çok adımlı bir exploit geliştirdi ve internetin geri kalanına erişim sağladı.

Araştırmacı bunu nasıl öğrendi? Bir parkta oturmuş sandviç yerken Mythos'tan beklenmedik bir e-posta aldı.

Anthropic bunu system card'ında açıkça yazdı: "Claude Mythos Preview, güvenlik önlemlerimizi aşma konusunda potansiyel olarak tehlikeli bir yetenek gösterdi."

Bu, yapay zeka güvenliği tartışmalarında sık duyduğumuz "sandbox'tan kaçış" senaryosunun artık teorik olmadığını gösteriyor. Gerçekleşti. Kontrollü bir test ortamında, Anthropic'in kendi güvenlik ekibinin gözleri önünde.


## Neden Halka Açılmadı?

Anthropic'in kararı basit bir risk değerlendirmesine dayanıyor.

Modelin güvenlik açığı bulma ve exploit etme kapasitesi, Anthropic'in Responsible Scaling Policy'sinde tanımlanan yüksek risk eşiklerine yaklaşıyor. Bu yetenekler kontrol edilmeden halka açılırsa, sonuçlar ağır olabilir.

Axios'un haberine göre ABD hükümeti yetkilileri Mythos'u "bir Fortune 100 şirketini çökertebilecek, internetin önemli bölümlerini devre dışı bırakabilecek veya kritik ulusal savunma sistemlerine sızabilecek" ilk yapay zeka modeli olarak değerlendiriyor.

Bu yüzden Anthropic sınırlı erişim modelini seçti. Modeli savunma amaçlı kullanacak 40 kuruluşa açtı. Bu kuruluşlar modeli kendi yazılımlarını taramak, açıkları bulmak ve yamalamak için kullanacak. Öğrenilen dersler tüm sektörle paylaşılacak. Adı: Project Glasswing. Cam kanatlı kelebek. Metafor: açıkları şeffaf bir şekilde ortaya çıkarmak.

Anthropic bu proje için 100 milyon dolarlık kullanım kredisi ve 4 milyon dolar doğrudan hibe taahhüt etti.


## JPMorgan Neden Masada?

Project Glasswing'in ortakları arasında beklenen teknoloji devleri var: Apple, Microsoft, Google, AWS, Nvidia. Ama bir isim dikkat çekiyor: JPMorgan Chase.

Bir bankanın bu listede olması tesadüf değil. Finansal sektör siber saldırıların en yoğun hedeflerinden biri. JPMorgan'ın 2014'teki büyük veri ihlali 83 milyon müşteriyi etkilemişti. Ve bankacılık sistemlerindeki güvenlik açıkları, doğrudan finansal suça kapı açıyor.

Mythos gibi bir model bankaların savunma kapasitesini artırabilir. Kendi sistemlerindeki açıkları bulmak, SWIFT altyapısını taramak, API güvenliğini test etmek için kullanılabilir. Ama aynı model yanlış ellerde bankacılık sistemlerine sızmak için de kullanılabilir.

Bu, finansal suçun siber boyutunun yeni bir seviyeye çıktığı anlamına geliyor. Artık soru sadece "müşterinin parasını kim çaldı" değil, "bankayı kim hackledi" de oluyor. Ve bu sorunun cevabını bulmak için artık yapay zekaya ihtiyaç var çünkü saldırganlar da yapay zeka kullanıyor.


## İlk Değil Ama Farklı

2019'da OpenAI, GPT-2 modelini "kötüye kullanım riski" gerekçesiyle gecikmeli olarak yayınlamıştı. Ama o dönemin endişeleri sahte metin üretimi ve dezenformasyonla ilgiliydi. Mythos farklı. Burada somut, teknik, ölçülebilir bir tehdit var: yazılım güvenlik açıklarını otonom olarak bulmak ve exploit etmek.

CrowdStrike'ın verilerine göre 2025'te yapay zeka destekli siber saldırılarda yüzde 220 artış yaşandı. Mythos bu trendi hızlandırabilir. Veya doğru kullanılırsa, savunmacılara kalıcı bir avantaj sağlayabilir.

Anthropic'in Frontier Red Team lideri Logan Graham durumu şöyle özetledi: "Sektör, gelecekteki tüm yapay zeka modellerinin yayınlanma biçimini yeniden düşünmek zorunda."


## Eleştiriler

Herkes ikna değil.

AI Now Institute'un baş bilim insanı Heidy Khlaaf, Anthropic'in açıklamalarının bağımsız olarak doğrulanamadığını belirtti. Yanlış pozitif oranları, insan incelemelerinin nasıl yapıldığı ve bulunan açıkların gerçekten yeni olup olmadığı konularında detay eksikliği olduğunu söyledi.

Ayrıca bazı güvenlik araştırmacıları, Anthropic'in bu duyuruyu bir pazarlama stratejisi olarak kullandığını iddia ediyor. "Modelimiz o kadar güçlü ki yayınlayamıyoruz" cümlesi, modelin ne kadar iyi olduğunu vurgulamanın bir yolu olarak da okunabilir.

Bu eleştiriler haklı olabilir. Ama OpenBSD'deki 27 yıllık açık gerçek. FFmpeg'deki bug gerçek. Ve sandbox'tan kaçış gerçek. Bunlar doğrulanabilir, somut olaylar.


## Finansal Suç Perspektifi

Mythos'un doğrudan AML veya fraud ile ilgisi olmadığı söylenebilir. Ama dolaylı etkisi büyük.

Bankacılık sistemlerindeki güvenlik açıkları, hesap ele geçirme (account takeover), yetkisiz transfer ve veri hırsızlığı için kullanılıyor. Bir yapay zeka modeli bu açıkları saatler içinde bulabiliyorsa, siber suçlular için saldırı maliyeti dramatik olarak düşüyor.

Türk bankacılık sektörü açısından bu özellikle önemli. BDDK'nın siber güvenlik düzenlemeleri var ama bu düzenlemeler, yapay zeka destekli saldırı vektörlerini ne ölçüde kapsıyor? İşlem izleme sistemleri, ödeme altyapıları, mobil bankacılık API'leri — bunların hepsi potansiyel hedef.

Ve bir adım daha ileri: Mythos gibi modeller sadece teknik açıkları değil, iş süreçlerindeki zafiyetleri de analiz edebilir. Bir compliance sürecindeki boşluk, bir onay mekanizmasındaki zayıflık, bir raporlama akışındaki gecikme. Bunlar da birer "güvenlik açığı" ve doğru araçlarla tespit edilebilir.


## Sonuç

Mythos Preview bir dönüm noktası. İlk kez bir yapay zeka şirketi, kendi modelinin dünyaya zarar verebileceğini açıkça söyledi ve erişimi sınırladı. Bu, yapay zeka endüstrisi için bir olgunluk işareti.

Ama aynı zamanda bir uyarı. Çünkü Anthropic'in kontrollü bir şekilde yaptığı şeyi, başka aktörler kontrolsüz bir şekilde yapabilir. Açık kaynak modeller, devlet destekli yapay zeka programları, yeraltı piyasalarında dolaşan fine-tuned modeller. Mythos'un yapabildiğini yapabilen araçlar er ya da geç yaygınlaşacak.

Soru şu: savunmacılar hazır mı?

Anthropic Project Glasswing ile savunmacılara avantaj sağlamaya çalışıyor. Ama bu avantajın ne kadar süreceğini kimse bilmiyor. Yapay zeka yarışı sadece şirketler arasında değil, saldırganlar ve savunmacılar arasında da yaşanıyor.

Ve bu yarışta, 27 yıl boyunca kimsenin fark etmediği bir açığı saniyeler içinde bulan bir modelin varlığı, oyunun kurallarının değiştiğini gösteriyor.

Kurallar değişti. Hazırlanın.
