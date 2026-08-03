// ── Animaciones profesionales (inspiradas en GSAPify) ────────────────
// Implementadas con APIs nativas (IntersectionObserver, rAF) — sin librerías pesadas.
(function () {
  'use strict';

  // ── 1. Barra de progreso de scroll (ScrollTrigger) ────────────────
  function initScrollProgress() {
    var bar = document.createElement('div');
    bar.className = 'scroll-progress';
    document.body.appendChild(bar);
    var ticking = false;
    function update() {
      var h = document.documentElement;
      var max = h.scrollHeight - h.clientHeight;
      bar.style.width = (max > 0 ? (h.scrollTop / max) * 100 : 0) + '%';
      ticking = false;
    }
    window.addEventListener('scroll', function () {
      if (!ticking) { ticking = true; requestAnimationFrame(update); }
    }, { passive: true });
    update();
  }

  // ── 2. Scroll reveal + stagger (ScrollTrigger + stagger) ───────────
  function initReveals() {
    var items = document.querySelectorAll('.reveal');
    if (!items.length || !('IntersectionObserver' in window)) {
      items.forEach(function (el) { el.classList.add('is-visible'); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    items.forEach(function (el) { io.observe(el); });
  }

  // ── 3. Contadores animados (stats del hero) ────────────────────────
  function animateCount(el) {
    var target = parseInt(el.dataset.count, 10) || 0;
    var duration = 1200;
    var start = null;
    function step(ts) {
      if (!start) start = ts;
      var progress = Math.min((ts - start) / duration, 1);
      var eased = 1 - Math.pow(1 - progress, 4); // easeOutQuart
      el.textContent = Math.round(target * eased);
      if (progress < 1) requestAnimationFrame(step);
      else el.textContent = target;
    }
    requestAnimationFrame(step);
  }
  function initCounters() {
    var counters = document.querySelectorAll('[data-count]');
    if (!counters.length) return;
    if (!('IntersectionObserver' in window)) {
      counters.forEach(function (el) { el.textContent = el.dataset.count; });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          animateCount(entry.target);
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });
    counters.forEach(function (el) { io.observe(el); });
  }

  // ── 4. Typewriter en el hero (SplitText/TextPlugin simplificado) ───
  function initTypewriter(el) {
    if (!el) return;
    var text = el.textContent;
    el.textContent = '';
    el.classList.add('typewriter');
    var i = 0;
    var speed = 38;
    function type() {
      if (i < text.length) {
        el.textContent = text.substring(0, i + 1);
        i++;
        setTimeout(type, speed);
      } else {
        el.classList.remove('typewriter');
      }
    }
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) { type(); io.unobserve(entry.target); }
        });
      }, { threshold: 0.4 });
      io.observe(el);
    } else { type(); }
  }

  // ── 5. 3D Tilt en tarjetas (hover, estilo GSAP) ────────────────────
  function initTilt() {
    var cards = document.querySelectorAll('.tilt-card');
    cards.forEach(function (card) {
      var inner = card.querySelector('.tilt-inner') || card;
      var raf = null;
      function onMove(e) {
        if (raf) return;
        raf = requestAnimationFrame(function () {
          var r = card.getBoundingClientRect();
          var x = (e.clientX - r.left) / r.width - 0.5;
          var y = (e.clientY - r.top) / r.height - 0.5;
          inner.style.transform =
            'perspective(800px) rotateY(' + (x * 10).toFixed(2) + 'deg) rotateX(' + (-y * 10).toFixed(2) + 'deg) translateY(-4px)';
          raf = null;
        });
      }
      function onLeave() {
        inner.style.transform = '';
      }
      card.addEventListener('mousemove', onMove);
      card.addEventListener('mouseleave', onLeave);
    });
  }

  // ── 6. Parallax sutil en elementos decorativos del hero ────────────
  function initParallax() {
    var els = document.querySelectorAll('[data-parallax]');
    if (!els.length) return;
    var ticking = false;
    function update() {
      var y = window.scrollY;
      els.forEach(function (el) {
        var speed = parseFloat(el.dataset.parallax) || 0.1;
        el.style.transform = 'translateY(' + (y * speed).toFixed(1) + 'px)';
      });
      ticking = false;
    }
    window.addEventListener('scroll', function () {
      if (!ticking) { ticking = true; requestAnimationFrame(update); }
    }, { passive: true });
    update();
  }

  // ── Init ────────────────────────────────────────────────────────────
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      initScrollProgress();
      initReveals();
      initCounters();
      initTypewriter(document.querySelector('[data-typewriter]'));
      initTilt();
      initParallax();
    });
  } else {
    initScrollProgress();
    initReveals();
    initCounters();
    initTypewriter(document.querySelector('[data-typewriter]'));
    initTilt();
    initParallax();
  }
})();
