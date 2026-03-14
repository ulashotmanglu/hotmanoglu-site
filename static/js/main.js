// ═══ MOBILE MENU ═══
const menuBtn = document.getElementById('menuBtn');
const navCenter = document.querySelector('.nav-center');
if (menuBtn && navCenter) {
  menuBtn.addEventListener('click', () => {
    navCenter.classList.toggle('mobile-open');
    menuBtn.classList.toggle('active');
  });
  // Close menu when a link is clicked
  navCenter.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      navCenter.classList.remove('mobile-open');
      menuBtn.classList.remove('active');
    });
  });
}

// ═══ NAV SCROLL ═══
const nav = document.getElementById('nav');
if (nav) {
  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 80);
  });
  // Initial check
  nav.classList.toggle('scrolled', window.scrollY > 80);
}

// ═══ SCROLL REVEAL ═══
const observerOpts = { threshold: 0.08, rootMargin: '0px 0px -40px 0px' };
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, observerOpts);

document.querySelectorAll('.reveal, .reveal-left').forEach(el => observer.observe(el));

// ═══ COUNTER ANIMATION ═══
const counterObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const el = entry.target;
      const target = parseInt(el.dataset.count);
      if (isNaN(target)) return;
      const duration = 1500;
      const start = Date.now();
      const animate = () => {
        const elapsed = Date.now() - start;
        const progress = Math.min(elapsed / duration, 1);
        const eased = 1 - Math.pow(1 - progress, 3);
        el.textContent = Math.round(eased * target);
        if (progress < 1) requestAnimationFrame(animate);
        else el.textContent = target + '+';
      };
      animate();
      counterObserver.unobserve(el);
    }
  });
}, { threshold: 0.5 });

document.querySelectorAll('[data-count]').forEach(el => counterObserver.observe(el));

// ═══ SMOOTH PARALLAX ON HERO ORBS ═══
const hero = document.querySelector('.hero');
if (hero) {
  window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;
    const heroHeight = hero.offsetHeight;
    if (scrollY < heroHeight) {
      const ratio = scrollY / heroHeight;
      document.querySelectorAll('.hero-orb').forEach((orb, i) => {
        orb.style.transform = `translateY(${ratio * (30 + i * 20)}px)`;
      });
    }
  });
}
