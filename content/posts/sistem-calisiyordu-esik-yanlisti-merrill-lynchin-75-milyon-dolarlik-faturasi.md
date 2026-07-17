---
title: "Sistem Çalışıyordu, Eşik Yanlıştı: Merrill Lynch'in 7,5 Milyon Dolarlık Faturası"
date: 2026-07-16
draft: false
categories: ["Vaka Analizi"]
tags: ["SAR", "İşlem İzleme", "SEC", "Merrill Lynch", "AML", "Uyum"]
description: "Merrill Lynch'in izleme sistemi çalışıyordu ama eşik yanlıştı. SEC 7,5 milyon dolar ceza kesti. Eşik yönetiminin neden sürekli bir uyum yükümlülüğü olduğunu anlatan vaka analizi."
image: "/img/posts/sistem-calisiyordu-esik-yanlisti-merrill-lynchin-75-milyon-dolarlik-faturasi.png"
---

29 Haziran 2026'da SEC, Bank of America'nın aracı kurum kolu Merrill Lynch'e 7,5 milyon dolar ceza kesti. Gerekçe çoğu enforcement vakasından farklıydı. Merrill'in şüpheli işlem izleme sistemi eksik değildi. Sistem vardı, çalışıyordu, işlemleri gruplayıp risk skoru üretiyordu. Sorun sistemin kendisinde değil, sistemin nasıl ayarlandığındaydı.

Bu ayrım önemli, çünkü uyum ekiplerinin çoğu hâlâ "izleme sistemimiz var mı" sorusuna odaklanıyor. Merrill vakası regülatörün artık çok daha zor bir soru sorduğunu gösteriyor. Sistemin var olması yetmiyor. Eşiğin neden o değerde olduğunu, en son ne zaman doğrulandığını ve testler bir zafiyet gösterdiğinde ne yapıldığını da savunabilmeniz gerekiyor.

## Şema Nasıl İşliyordu

Merrill, kendi BSA yükümlülüklerini yerine getirmek için Bank of America'nın kurumsal işlem izleme yazılımına bağımlıydı. Yazılımın adı Event Processor. Mantığı basit. Potansiyel şüpheli işlemleri "event group" adı verilen gruplara topluyor, her gruba bir risk skoru atıyor ve yalnızca belli bir eşiğin üzerindeki grupları insan incelemesine gönderiyordu.

O eşik 20 puandı. Skoru 20 ve üzerinde olan gruplar SAR incelemesine alınıyordu. 20 altındakiler hiç incelenmiyordu. Bir grup 13 ay içinde vaka statüsüne yükselmezse, eski kayıtlar hiç araştırılmadan sistemden düşüyordu.

Buraya kadar anlatılan yapı olağan dışı değil. Büyük bir kurumda milyonlarca işlem arasından öne çıkanları ayıklamanın, birinci hat analistleri boğmadan yüksek riski önceliklendirmenin bir yolu lazım. Eşik koymak riske dayalı bir sistemin doğal parçası. Sorun eşiğin varlığı değildi. Sorun o eşiğin yanlış yerde durması ve bunun yıllarca bilinmesiydi.

## Kırılma Noktası: Merrill Kendi Verisiyle Yakalandı

SEC'in kararında asıl ağırlığı taşıyan kısım şu. Bank of America ve Merrill, 20 puan eşiğinin altındaki gruplar üzerinde düzenli olarak örnekleme analizleri yapıyordu. Bu analizler tek bir soruyu ölçüyordu. Eğer bu düşük skorlu gruplar incelenseydi, ne kadarı gerçekten SAR gerektirirdi? İç yazışmalarda bu orana "SAR Yield" deniyordu.

Sonuç rahatsız ediciydi. En az Nisan 2020'den itibaren yapılan analizler, 20 puanın altındaki bazı grupların yüksek SAR Yield ürettiğini gösteriyordu. Bazı durumlarda bu oran, eşiğin üzerindeki grupların oranından bile yüksekti. Yani sistem, gerçekten şüpheli olan işlemleri incelenmeyen tarafa itiyordu ve Merrill bunu kendi ölçümleriyle biliyordu.

Buna rağmen eşik Aralık 2023'e kadar değiştirilmedi. Nisan 2020'den Aralık 2023'e üç buçuk yıldan uzun bir süre. Bu süre boyunca incelenmeyen ve raporlanmayan işlemler yüzlerce milyon doları buluyordu. İçlerinde ekonomik veya yasal bir amacı görünmeyen transferler, büyük ve yuvarlak tutarlı havaleler, yüksek riskli coğrafyalara giden ve oralardan gelen paralar, structuring görünümlü nakit hareketleri ve daha önce SAR düzenlenmiş kişilerin hesaplarındaki işlemler vardı.

Aralık 2023'te Merrill nihayet eşiği düşürdü, geriye dönük bir inceleme başlattı ve yıllar önce düzenlemesi gereken çok sayıda SAR'ı geç de olsa dosyaladı. Bu geriye dönük dosyalama tek başına her şeyi anlatıyor. İşlemler baştan beri raporlanabilir nitelikteydi. Aradaki tek engel yanlış konumlanmış bir sayıydı.

## Bu Neden Üçüncü Kez Oluyor

Merrill'in SAR cezası geçmişi yeni değil. 2017'de SEC, belirli hesapları şüpheli aktivite açısından düzgün izlemediği için Merrill'i cezalandırdı. 2023'te SEC ve FINRA birlikte 12 milyon dolarlık ceza kesti. O vakada Merrill, Bank of America devralması sırasında miras aldığı 25.000 dolarlık bir eşiği kullanmıştı. Oysa aracı kurumlar için doğru eşik 5.000 dolardı. On yıl boyunca yüzlerce SAR bu yüzden hiç düzenlenmedi.

2026 cezası bu iki vakadan ayrı, sonraki bir dönemi kapsıyor. Nisan 2020'de başlayıp Eylül 2024'e uzanan bir dönem. Yani tablo şu. Merrill iki ayrı çok yıllık dönemde, iki ayrı yanlış eşik yüzünden, aynı türden bir hatayı üst üste yaptı. Bu bir tesadüf değil. Eşik yönetiminin bir kez kurulup unutulan bir uygulama kararı gibi görülmesinin sonucu.

Bir ayrıntı daha var. Merrill, Event Processor'daki bu ölçek hatasını ilk kez 2020'de fark etti. Yani 2017 cezası daha hafızalardayken. Zafiyet Eylül 2024'e kadar sürdü. Yani 2023 cezası imzalandıktan sonra bile. Sorun şu soruya dönüşüyor. Test sonuçlarında ortaya çıkan eksikliklerden kim haberdar edildi, kim takip etmedi ve neden yıllarca kimse "bu neden hâlâ düzelmedi" diye sormadı.

23 Aralık 2024'te bu tabloya OCC de eklendi ve Bank of America'ya BSA ve yaptırım uyum programındaki eksiklikler için ayrı bir consent order verdi. Yani mesele tek bir aracı kurumun tek bir ayarından çok daha geniş bir yönetişim sorununa işaret ediyor.

## Uyum Ekipleri İçin Çıkarılacak Dersler

Bu vaka bir teknoloji arızası değil, yönetişim arızası. Ders de burada.

Birincisi, eşik bir kez kurulup unutulacak bir ayar değil, sürekli bir uyum yükümlülüğü. Bir eşik ilk konduğu gün doğru olabilir. Müşteri davranışı, tipolojiler ve suç yöntemleri değiştikçe aynı eşik zamanla kör noktalar üretmeye başlar. Düzenli valide edilmeyen bir eşik, hiç izleme yapmamakla aynı riski taşır.

İkincisi, kendi testinizin size söylediğini görmezden gelmek en ağır kısım. Merrill'in eşiği yanlış olmasından çok, yanlış olduğunu kendi verisinden bilip yıllarca harekete geçmemesi cezalandırıldı. Bir bulgu, arkasına izlenen bir düzeltme yükümlülüğü konmadan rapora giriyorsa o bir kayıttır, kontrol değildir. False positive azaltmak cazip. Ama alarm hacmini kısmak, gerçekten şüpheli davranışı kaçırma pahasına yapılıyorsa regülatör tam da buraya bakıyor.

Üçüncüsü, paylaşılan platform sizi sorumluluktan kurtarmıyor. Merrill, ana kurumdan miras aldığı yapılandırmayı kendi Rule 17a-8 yükümlülüklerine göre bağımsız olarak hiç doğrulamadı. SAR yükümlülüğü kurum seviyesinde işler. Aynı yazılımı kullanan bir grup şirketiyseniz, her bir tüzel kişinin kendi düzenleyici gereksinimlerine göre ayrı doğrulama yapmanız gerekir. Ana bankanın uyum duruşu sizi kapsamaz.

Türk bankaları ve aracı kurumları açısından da tablo tanıdık. Senaryo eşikleri, alarm skorları, SAR yani bizdeki şüpheli işlem bildirimi mantığı ve model doğrulama süreçleri aynı temel soruya bağlı. Eşiğinizi neden o değerde tuttuğunuzu, en son ne zaman test ettiğinizi ve testler bir açık gösterdiğinde ne kadar sürede kapattığınızı belge üzerinde gösterebiliyor musunuz? Merrill'in 7,5 milyon dolarlık cevabı, bu soruya "hayır" demenin bedelini net biçimde ortaya koyuyor.
