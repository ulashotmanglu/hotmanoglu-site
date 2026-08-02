/* ==========================================================================
   HOTMANOGLU — main.js
   Minimum vanilla JS. Hiçbiri kritik değil: JS çalışmazsa sayfa okunur kalır.
   Bölümler: tema · mobil çekmece · arama · bağlantı kopyala · masthead · reveal
   ========================================================================== */
(function () {
  'use strict';

  var root = document.documentElement;
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ── TEMA ───────────────────────────────────────────────────────────── */
  var themeBtn = document.getElementById('themeBtn');
  function currentTheme() {
    return root.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
  }
  function syncThemeBtn() {
    if (!themeBtn) return;
    var dark = currentTheme() === 'dark';
    themeBtn.setAttribute('aria-label', dark ? 'Açık temaya geç' : 'Koyu temaya geç');
  }
  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      var next = currentTheme() === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem('hm-theme', next); } catch (e) {}
      syncThemeBtn();
    });
    syncThemeBtn();
  }

  /* ── ODAK / GÖVDE KİLİDİ ────────────────────────────────────────────── */
  var lastFocused = null;
  function lockBody(on) {
    document.body.classList.toggle('is-locked', !!on);
  }
  function trapFocus(container, e) {
    var f = container.querySelectorAll('a[href], button:not([disabled]), input, [tabindex]:not([tabindex="-1"])');
    if (!f.length) return;
    var first = f[0], last = f[f.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  }

  /* ── MOBİL ÇEKMECE ──────────────────────────────────────────────────── */
  var menuBtn = document.getElementById('menuBtn');
  var drawer = document.getElementById('drawer');
  var drawerClose = document.getElementById('drawerClose');

  function openDrawer() {
    if (!drawer) return;
    lastFocused = document.activeElement;
    drawer.hidden = false;
    requestAnimationFrame(function () { drawer.classList.add('is-open'); });
    if (menuBtn) menuBtn.setAttribute('aria-expanded', 'true');
    lockBody(true);
    if (drawerClose) drawerClose.focus();
  }
  function closeDrawer() {
    if (!drawer || drawer.hidden) return;
    drawer.classList.remove('is-open');
    if (menuBtn) menuBtn.setAttribute('aria-expanded', 'false');
    lockBody(false);
    var done = function () { drawer.hidden = true; };
    if (reduceMotion) done(); else setTimeout(done, 180);
    if (lastFocused && lastFocused.focus) lastFocused.focus();
  }
  if (menuBtn) menuBtn.addEventListener('click', openDrawer);
  if (drawerClose) drawerClose.addEventListener('click', closeDrawer);
  if (drawer) {
    drawer.addEventListener('click', function (e) { if (e.target === drawer) closeDrawer(); });
    drawer.addEventListener('keydown', function (e) { if (e.key === 'Tab') trapFocus(drawer, e); });
    drawer.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', closeDrawer); });
  }

  /* ── ARAMA ──────────────────────────────────────────────────────────── */
  var searchBtn = document.getElementById('searchBtn');
  var overlay = document.getElementById('searchOverlay');
  var input = document.getElementById('searchInput');
  var results = document.getElementById('searchResults');
  var searchClose = document.getElementById('searchClose');
  var index = null, loading = false;

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  // Türkçe duyarsız karşılaştırma için sadeleştirme
  function norm(s) {
    return String(s).toLocaleLowerCase('tr')
      .replace(/ı/g, 'i').replace(/İ/g, 'i')
      .replace(/ş/g, 's').replace(/ğ/g, 'g')
      .replace(/ü/g, 'u').replace(/ö/g, 'o').replace(/ç/g, 'c')
      .replace(/â/g, 'a').replace(/î/g, 'i').replace(/û/g, 'u');
  }

  function loadIndex() {
    if (index || loading) return Promise.resolve();
    loading = true;
    return fetch('/index.json')
      .then(function (r) { return r.ok ? r.json() : []; })
      .then(function (d) { index = Array.isArray(d) ? d : []; loading = false; })
      .catch(function () { index = []; loading = false; });
  }

  function render(q) {
    if (!results) return;
    var term = norm(q).trim();
    if (term.length < 2) {
      results.innerHTML = '<p class="search-hint">En az iki karakter yazın.</p>';
      return;
    }
    if (!index) {
      results.innerHTML = '<p class="search-hint">Yükleniyor…</p>';
      return;
    }
    var words = term.split(/\s+/);
    var hits = index.map(function (it) {
      var hay = norm(it.t + ' ' + it.d + ' ' + it.c + ' ' + it.g);
      var score = 0;
      for (var i = 0; i < words.length; i++) {
        if (hay.indexOf(words[i]) === -1) return null;
        if (norm(it.t).indexOf(words[i]) !== -1) score += 3;
        score += 1;
      }
      return { it: it, score: score };
    }).filter(Boolean).sort(function (a, b) { return b.score - a.score; }).slice(0, 12);

    if (!hits.length) {
      results.innerHTML = '<p class="search-hint">“' + esc(q) + '” için sonuç bulunamadı.</p>';
      return;
    }
    results.innerHTML = '<ul class="search-list">' + hits.map(function (h) {
      var it = h.it;
      return '<li><a href="' + esc(it.u) + '">' +
        '<span class="search-item-meta">' + (it.c ? esc(it.c) + ' · ' : '') + esc(it.y) + ' · ' + esc(it.r) + ' dk</span>' +
        '<span class="search-item-title">' + esc(it.t) + '</span>' +
        (it.d ? '<span class="search-item-desc">' + esc(it.d) + '</span>' : '') +
        '</a></li>';
    }).join('') + '</ul>';
  }

  function openSearch() {
    if (!overlay) return;
    lastFocused = document.activeElement;
    overlay.hidden = false;
    requestAnimationFrame(function () { overlay.classList.add('is-open'); });
    lockBody(true);
    if (input) { input.value = ''; input.focus(); }
    render('');
    loadIndex().then(function () { if (input) render(input.value); });
  }
  function closeSearch() {
    if (!overlay || overlay.hidden) return;
    overlay.classList.remove('is-open');
    lockBody(false);
    var done = function () { overlay.hidden = true; };
    if (reduceMotion) done(); else setTimeout(done, 150);
    if (lastFocused && lastFocused.focus) lastFocused.focus();
  }
  if (searchBtn) searchBtn.addEventListener('click', openSearch);
  if (searchClose) searchClose.addEventListener('click', closeSearch);
  if (overlay) {
    overlay.addEventListener('click', function (e) { if (e.target === overlay) closeSearch(); });
    overlay.addEventListener('keydown', function (e) { if (e.key === 'Tab') trapFocus(overlay, e); });
  }
  if (input) {
    var t;
    input.addEventListener('input', function () {
      clearTimeout(t);
      var v = input.value;
      t = setTimeout(function () { render(v); }, 90);
    });
  }

  /* ── KLAVYE ─────────────────────────────────────────────────────────── */
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { closeSearch(); closeDrawer(); }
    if (e.key === '/' && !/^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName)) {
      e.preventDefault(); openSearch();
    }
  });

  /* ── BAĞLANTI KOPYALA ───────────────────────────────────────────────── */
  document.querySelectorAll('[data-copy-link]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var url = btn.getAttribute('data-copy-link');
      var done = function () {
        var old = btn.textContent;
        btn.textContent = 'Kopyalandı';
        setTimeout(function () { btn.textContent = old; }, 1600);
      };
      if (navigator.clipboard) navigator.clipboard.writeText(url).then(done, function () {});
    });
  });


  /* ── OKUMA İLERLEMESİ ───────────────────────────────────────────────── */
  var bar = document.getElementById('progressBar');
  var body = document.getElementById('articleBody');
  if (bar && body) {
    var ticking = false;
    var update = function () {
      var r = body.getBoundingClientRect();
      var total = r.height - window.innerHeight * 0.4;
      var done = -r.top + window.innerHeight * 0.4;
      var pct = total > 0 ? Math.min(1, Math.max(0, done / total)) : 0;
      bar.style.transform = 'scaleX(' + pct + ')';
      ticking = false;
    };
    var onScroll = function () {
      if (!ticking) { ticking = true; requestAnimationFrame(update); }
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll, { passive: true });
    update();
  }

  /* ── İÇİNDEKİLER — aktif bölüm ──────────────────────────────────────── */
  var rail = document.getElementById('tocRail');
  if (rail && body && 'IntersectionObserver' in window) {
    var links = {};
    rail.querySelectorAll('a[href^="#"]').forEach(function (a) {
      links[decodeURIComponent(a.getAttribute('href').slice(1))] = a;
    });
    var heads = [].slice.call(body.querySelectorAll('h2[id]'));
    var setActive = function (id) {
      rail.querySelectorAll('a').forEach(function (a) { a.removeAttribute('aria-current'); });
      if (links[id]) links[id].setAttribute('aria-current', 'true');
    };
    var seenMap = {};
    var io2 = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { seenMap[en.target.id] = en.isIntersecting ? en.boundingClientRect.top : null; });
      var current = null;
      for (var i = 0; i < heads.length; i++) {
        if (heads[i].getBoundingClientRect().top < window.innerHeight * 0.35) current = heads[i].id;
      }
      if (current) setActive(current);
    }, { rootMargin: '-10% 0px -70% 0px', threshold: 0 });
    heads.forEach(function (h) { io2.observe(h); });
  }

  /* ── MASTHEAD — scroll'da sıkışır ───────────────────────────────────── */
  var mh = document.getElementById('masthead');
  if (mh) {
    var onS = function () { mh.classList.toggle('is-compact', window.scrollY > 120); };
    window.addEventListener('scroll', onS, { passive: true });
    onS();
  }

  /* ── MASTHEAD (eski) ────────────────────────────────────────────────── */
  var masthead = document.getElementById('masthead');
  if (masthead) {
    var onScroll = function () { masthead.classList.toggle('is-scrolled', window.scrollY > 40); };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ── REVEAL ─────────────────────────────────────────────────────────── */
  var revealables = document.querySelectorAll('.reveal');
  if (revealables.length) {
    if (reduceMotion || !('IntersectionObserver' in window)) {
      revealables.forEach(function (el) { el.classList.add('is-visible'); });
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) { en.target.classList.add('is-visible'); io.unobserve(en.target); }
        });
      }, { threshold: 0.05, rootMargin: '0px 0px -40px 0px' });
      revealables.forEach(function (el) { io.observe(el); });
    }
  }
})();
