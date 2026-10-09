/* GA4 basic consent: no Google tag or measurement before explicit permission.
   Enhanced measurement must be OFF for this stream before deployment.
   Only published canonical paths and fixed interaction labels leave the site. */
(function () {
  'use strict';
  var settings = document.getElementById('analyticsSettings');
  var banner = document.getElementById('analyticsConsent');
  if (!settings || !banner || location.hostname !== 'www.hotmanoglu.com') return;
  var id = settings.dataset.measurementId;
  if (id !== 'G-KKHBRTL8LJ') return;
  var canonical;
  try { canonical = new URL(settings.dataset.pageLocation); } catch (e) { return; }
  // Do not measure unknown routes, aliases, admin pages, or other hosts.
  if (canonical.origin !== 'https://www.hotmanoglu.com' || canonical.pathname !== location.pathname) return;
  canonical.search = ''; canonical.hash = '';
  var preferenceKey = 'hm-analytics-consent-v1';
  var revokedKey = 'hm-analytics-revoked-v1';
  var denialCookie = 'hm-analytics-denied';
  var maxAge = 180 * 24 * 60 * 60 * 1000;
  var active = false, started = false, scrollSent = false;
  var tag = null;
  var forcedDenied = false, persistenceFailed = false, channel = null;
  var closeButton = banner.querySelector('[data-analytics-close]');
  var status = document.getElementById('analyticsConsentStatus');
  var consent = { analytics_storage: 'granted', ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied' };

  function storedPreference() {
    try {
      var saved = JSON.parse(localStorage.getItem(preferenceKey));
      if (saved && (saved.choice === 'granted' || saved.choice === 'denied') &&
          typeof saved.at === 'number' && saved.at <= Date.now() && Date.now() - saved.at < maxAge) return saved.choice;
    } catch (e) {}
    return null;
  }
  function preference() {
    if (forcedDenied) return 'denied';
    if (document.cookie.split(';').some(function (part) { return part.trim() === denialCookie + '=1'; })) return 'denied';
    try { if (sessionStorage.getItem(revokedKey) === 'denied') return 'denied'; } catch (e) {}
    return storedPreference();
  }
  function remember(choice) {
    var value = JSON.stringify({ choice: choice, at: Date.now() });
    try {
      localStorage.setItem(preferenceKey, value);
      return localStorage.getItem(preferenceKey) === value;
    } catch (e) { return false; }
  }
  function writableGrant() {
    // A readable but unwritable old grant is not sufficient to restart GA.
    // Preserve its original timestamp rather than extending consent on visits.
    try {
      var probe = preferenceKey + '-write-check';
      var value = String(Date.now()) + ':' + String(Math.random());
      localStorage.setItem(probe, value);
      var written = localStorage.getItem(probe) === value;
      localStorage.removeItem(probe);
      return written;
    } catch (e) { return false; }
  }
  function latchDenial() {
    forcedDenied = true;
    try { sessionStorage.setItem(revokedKey, 'denied'); } catch (e) {}
    // A strictly necessary host-only rejection marker protects newly opened
    // tabs too when the old localStorage grant cannot be overwritten/deleted.
    document.cookie = denialCookie + '=1; Max-Age=15552000; Path=/; SameSite=Lax; Secure';
  }
  function withdraw(broadcast) {
    latchDenial();
    var persisted = storedPreference() === 'denied' || remember('denied');
    persistenceFailed = !persisted;
    if (!persisted) {
      // Quota failures often still permit deletion. Never retain the old grant
      // merely because writing a new preference failed.
      try { localStorage.removeItem(preferenceKey); } catch (e) {}
    }
    if (broadcast && channel) channel.postMessage('denied');
    stop(persisted);
    if (!persisted) show();
  }
  function clearCookies() {
    ['_ga', '_ga_KKHBRTL8LJ'].forEach(function (name) {
      document.cookie = name + '=; Max-Age=0; Path=/; SameSite=Lax; Secure';
      document.cookie = name + '=; Max-Age=0; Path=/; Domain=www.hotmanoglu.com; SameSite=Lax; Secure';
    });
  }
  function context() {
    var referrer = '';
    try {
      var host = new URL(document.referrer).hostname;
      // Unknown hosts can contain identifiers in subdomains; omit those too.
      if (['www.hotmanoglu.com', 'google.com', 'www.google.com', 'www.google.com.tr', 'bing.com', 'www.bing.com',
           'linkedin.com', 'www.linkedin.com', 'l.linkedin.com', 'x.com', 'twitter.com', 't.co',
           'instagram.com', 'www.instagram.com', 'l.instagram.com', 'youtube.com', 'www.youtube.com'].indexOf(host) >= 0) referrer = 'https://' + host + '/';
    } catch (e) {}
    return { page_location: canonical.href, page_referrer: referrer,
      page_title: settings.dataset.pageTitle, content_type: settings.dataset.pageType };
  }
  function event(name, fields) {
    if (!active || preference() === 'denied' || window['ga-disable-' + id]) return;
    window.gtag('event', name, Object.assign(context(), fields || {}, { send_to: id }));
  }
  function start() {
    if (started) return;
    active = true; started = true;
    window['ga-disable-' + id] = false;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('consent', 'default', { analytics_storage: 'denied', ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied' });
    window.gtag('consent', 'update', consent);
    window.gtag('js', new Date());
    window.gtag('set', Object.assign(context(), { allow_google_signals: false, allow_ad_personalization_signals: false }));
    var config = Object.assign(context(), { send_page_view: false, allow_google_signals: false,
      allow_ad_personalization_signals: false, cookie_domain: 'www.hotmanoglu.com', cookie_expires: 15552000,
      cookie_update: false, cookie_flags: 'SameSite=Lax;Secure' });
    // Never forward arbitrary campaign values, terms, content, IDs, or URL parameters.
    var query = new URLSearchParams(location.search);
    var source = query.get('utm_source'), medium = query.get('utm_medium'), campaign = query.get('utm_campaign');
    if (['linkedin', 'x', 'twitter', 'instagram', 'youtube', 'google', 'bing', 'newsletter'].indexOf(source) >= 0 &&
        ['social', 'organic', 'referral', 'email'].indexOf(medium) >= 0) {
      config.campaign_source = source; config.campaign_medium = medium;
      if (['editorial', 'article', 'profile'].indexOf(campaign) >= 0) config.campaign_name = campaign;
    }
    // Remove raw parameters before the third-party library can inspect the URL.
    // replaceState leaves the reader's current scroll position unchanged.
    if (location.search || location.hash) history.replaceState(history.state, '', canonical.pathname);
    window.gtag('config', id, config);
    event('page_view');
    tag = document.createElement('script');
    tag.async = true; tag.referrerPolicy = 'no-referrer';
    tag.src = 'https://www.googletagmanager.com/gtag/js?id=' + id;
    document.head.appendChild(tag);
  }
  function stop(canReload) {
    active = false;
    window['ga-disable-' + id] = true;
    if (tag) tag.remove();
    clearCookies();
    // A fresh document removes the already loaded library and its automatic listeners.
    // Do not send a denied-consent ping; basic consent sends nothing after rejection.
    // Reload only after the replacement denial was read back successfully.
    // Otherwise keep the disable flag in this document; reloading could read
    // an old stored grant. The session latch also protects manual navigation.
    if (started && canReload) location.reload();
  }
  function show() {
    var saved = preference();
    closeButton.hidden = !saved;
    status.textContent = saved === 'granted' ? 'Mevcut tercih: analitik açık.' : saved === 'denied' ? 'Mevcut tercih: analitik kapalı.' : '';
    if (persistenceFailed) status.textContent = 'Analitik kapalı. Tercih kaydedilemedi; eski izin kullanılmıyor. Bu sekmede ölçüm durdu. Kalıcı ret için tarayıcınızın site verilerini temizleyebilirsiniz.';
    banner.hidden = false;
  }
  banner.querySelectorAll('[data-analytics-choice]').forEach(function (button) {
    button.addEventListener('click', function () {
      var choice = button.dataset.analyticsChoice;
      if (choice === 'denied') { banner.hidden = true; withdraw(true); return; }
      // Grant must persist too. Never silently start when storage is blocked.
      var persisted = remember('granted');
      if (persisted) {
        try { sessionStorage.removeItem(revokedKey); persisted = sessionStorage.getItem(revokedKey) !== 'denied'; } catch (e) { persisted = false; }
        document.cookie = denialCookie + '=; Max-Age=0; Path=/; SameSite=Lax; Secure';
        if (document.cookie.split(';').some(function (part) { return part.trim() === denialCookie + '=1'; })) persisted = false;
      }
      if (!persisted) { latchDenial(); persistenceFailed = true; stop(false); show(); return; }
      forcedDenied = false; persistenceFailed = false; banner.hidden = true;
      if (started && !active) location.reload(); else start();
    });
  });
  closeButton.addEventListener('click', function () { banner.hidden = true; });
  document.querySelectorAll('[data-analytics-preferences]').forEach(function (button) {
    button.addEventListener('click', function () { show(); banner.querySelector('[data-analytics-choice]').focus(); });
  });
  window.addEventListener('storage', function (e) {
    if (e.key !== preferenceKey) return;
    if (storedPreference() !== 'granted') { latchDenial(); stop(storedPreference() === 'denied'); show(); }
    // Granting permission in another tab does not silently start this tab.
  });
  window.addEventListener('pageshow', function (e) {
    if (e.persisted && preference() !== 'granted') stop(storedPreference() === 'denied');
  });
  try {
    channel = new BroadcastChannel('hm-analytics-consent-v1');
    channel.onmessage = function (e) {
      // Rejection is shared even when no localStorage storage event can fire.
      // No grant message can turn tracking on in another tab.
      if (e.data === 'denied') withdraw(false);
    };
  } catch (e) {}

  document.addEventListener('click', function (e) {
    if (!active) return;
    var target = e.target.closest('a[href], [data-copy-link]');
    if (!target) return;
    if (target.hasAttribute('data-copy-link')) { event('site_cta', { cta_name: 'copy_link' }); return; }
    var url;
    try { url = new URL(target.href); } catch (err) { return; }
    if (url.protocol !== 'https:' && url.protocol !== 'http:') return;
    if (url.hostname !== location.hostname) {
      var kind = /(^|\.)linkedin\.com$/.test(url.hostname) ? 'linkedin' : /(^|\.)(twitter|x)\.com$/.test(url.hostname) ? 'x' : 'external';
      event('outbound_click', { destination_type: kind });
      if (url.pathname === '/sharing/share-offsite/' || url.pathname === '/intent/tweet') event('site_cta', { cta_name: 'share_' + kind });
    } else if (url.pathname === '/index.xml') event('site_cta', { cta_name: 'rss' });
    else if (url.pathname === '/iletisim/') event('site_cta', { cta_name: 'contact' });
  });
  window.addEventListener('scroll', function () {
    if (!active || scrollSent || settings.dataset.pageType !== 'article') return;
    if (window.scrollY + window.innerHeight >= document.documentElement.scrollHeight * 0.9) {
      scrollSent = true; event('scroll', { percent_scrolled: 90 });
    }
  }, { passive: true });
  if (preference() === 'granted' && writableGrant()) start();
  else if (preference() === 'granted') { latchDenial(); persistenceFailed = true; stop(false); show(); }
  else { window['ga-disable-' + id] = true; clearCookies(); if (!preference()) show(); }
})();
