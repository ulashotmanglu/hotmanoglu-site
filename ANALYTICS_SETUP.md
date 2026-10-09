# Analytics yayın kontrolü

Mevcut public akış: property `523555863`, stream `13561452048`, measurement
`G-KKHBRTL8LJ`. Yeni akış/property veya API secret gerekmez. Hedef yalnız
`https://www.hotmanoglu.com`; Sanal Ofis ve public admin ölçülmez.

## Yayın öncesi

- Mevcut GA4 saklama süresini ve yeni kullanıcı etkinliğiyle sıfırlama ayarını
  **okuyup**, `content/gizlilik.md` içindeki geçici saklama paragrafını gerçek
  değerlerle tamamlayın; süreyi sessizce genişletmeyin.
- Stream'in enhanced measurement anahtarını **kapalı** doğrulayın. Kod tek
  manuel `page_view`, yazıda bir kez yüzde 90 `scroll`, sabit etiketli
  `outbound_click` ve `site_cta` gönderir. Otomatik arama, form, video, dosya,
  dış bağlantı ve history-pageview ölçümü kullanılmaz. GA4'ün temel
  session/engagement ölçümü korunur.
- Google Signals, kullanıcı tarafından sağlanan veri toplama ve reklam
  bağlantıları açılmamalı. Ayrıntılı konum/cihaz ölçümünü dar kapsam için
  kapalı doğrulayın. E-posta redaction açık kalsın; URL redaction ek savunma
  olarak email, token, access_token, auth, code, q, s, search, query, term,
  utm_term, utm_content, gclid, dclid, fbclid, msclkid için etkinleştirilebilir.
  Kod query/fragment'i zaten bütünüyle temizler.
- Bunlar doğrulanmadan `[params.analytics].enabled = true` yapılmaz.
- `main` push'u otomatik GitHub Pages deploy eder. Draft PR review ve bu
  kontroller tamamlanmadan merge edilmez.

## Veri sınırları

Kabul öncesi Google etiketi yüklenmez. Fontlar da aynı tipografi korunarak
yerelden sunulur; ilk ziyaret/reddetme Google Fonts isteği oluşturmaz.
Analytics izinleri kabulde granted, reklam izinlerinin üçü sürekli denied.
Public-host GA çerezleri 180 gün, `cookie_update=false`; tercih de 180 gün.
İzni geri çekme disable bayrağını hemen uygular, public-host GA çerezlerini
siler ve yüklenmiş kütüphaneyi tamamen kaldırmak için sayfayı yeniler. Daha
önce gönderilen veriler bu işlemle Analytics'ten silinmez.

Tercih yazması read-back ile doğrulanır. Ret yazılamazsa otomatik reload
yapılmaz; disable bayrağı uygulanır, eski izin silinmeye çalışılır. Oturum
saklaması ve host-only `hm-analytics-denied=1` zorunlu tercih çerezi eski
granted kaydının önüne geçer. BroadcastChannel, localStorage storage event'i
oluşmasa da diğer açık sekmelerde ölçümü durdurur. Yeni sekmeler de ret
çerezini okuyarak eski grant'i kullanmaz. Ret saklanamıyorsa durum mesajı
gösterilir. Otomatik başlatmada localStorage yazılabilirliği ayrıca doğrulanır;
okunabilen ama yazılamayan eski grant yeterli sayılmaz. Tercih çerezinin
ömrü 180 gündür; açık ve doğrulanmış yeni izin bu ret korumasını kaldırır.

Sayfa adresi Hugo'nun yayınlanan canonical yoludur. Query/fragment izin
sonrası adres çubuğundan da kaldırılır. Önceki sayfanın query/path bölümü
gönderilmez; yalnız tanımlı kaynak alanları kabul edilir, bilinmeyen referrer
atlanır. Ham outbound adresi, link metni, arama ve form girdisi gönderilmez.
UTM source: linkedin/x/twitter/instagram/youtube/google/bing/newsletter;
medium: social/organic/referral/email; campaign: editorial/article/profile.
Tanımsız değerler atılır; term/content/ID ve reklam click ID'leri gönderilmez.
Bu daraltma bilinmeyen referral ve kampanyaların raporlanmasını sınırlar.

## Yerel doğrulama

Test bağımlılığını ayrı geçici dizine kurun:

```sh
npm install --prefix /tmp/hotmanoglu-analytics-test --no-audit --no-fund playwright
printf '[params.analytics]\nenabled = true\n' > /tmp/hotmanoglu-analytics-test.toml
hugo --config hugo.toml,/tmp/hotmanoglu-analytics-test.toml --minify --destination /tmp/hotmanoglu-analytics-build --cacheDir /tmp/hotmanoglu-analytics-cache
PLAYWRIGHT_MODULE=/tmp/hotmanoglu-analytics-test/node_modules/playwright ANALYTICS_BUILD_DIR=/tmp/hotmanoglu-analytics-build node tests/analytics-consent.cjs
```

Testler ayrı geçici Chrome profili kullanır, kullanıcının Safari oturumuna
dokunmaz. Mac varsayılan Chrome path'i dışında `CHROME_EXECUTABLE` verilebilir.
Google kütüphanesi bir test double ile değiştirilir ve tüm dış istekler
intercept edilir. Bu testler **canlı GA teslimatını doğrulamaz**.

## Canlı doğrulama

Deploy sonrası temiz tarayıcı profiliyle önce hiçbir seçim yapmadan, sonra
reddederek ağ ve çerez kontrolü yapın: hiçbir Google isteği ve `_ga*` çerezi
olmamalı. Kabulde yalnız tek tag/ilk pageview, temiz `dl`/`dr`, sabit event
alanları, doğru measurement ID ve denied reklam izinleri doğrulanmalı.
Bilerek eklenen sentetik query/referrer/UTM değerlerinin Google payload'ında
olmadığını denetleyin. Scroll/CTA/outbound ve geri çekme testlerini yapın.
Test event'i Realtime'da doğrulayın; gerekirse geçici `debug_mode` ile yalnız
test trafiğini DebugView'da inceleyin ve debug değişikliğini kaldırın.
Normal edinme/engagement raporlarının gecikmesi Realtime başarısından ayrı
değerlendirilir. Eski dönem verisi üretilemez veya bu kurulumla geri gelmez.
