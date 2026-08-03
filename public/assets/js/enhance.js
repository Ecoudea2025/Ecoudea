(function () {
  'use strict';

  // ── REPARAR MATEMÁTICAS MANGLED ──────────────────────────────────
  // Markdown convierte `_{P_1}` (subíndice LaTeX) en `<em>{P_1}`
  // porque `_` es énfasis. Esto corrompe el LaTeX antes de que KaTeX lo vea.
  // Solución: dentro de bloques $...$ / $$...$$, restaurar los guiones bajos.
  function repairMathMangling(article) {
    var html = article.innerHTML;

    // Bloques display: $$ ... $$
    html = html.replace(/\$\$([\s\S]*?)\$\$/g, function (match, inner) {
      if (inner.indexOf('<em>') === -1 && inner.indexOf('</em>') === -1) return match;
      var fixed = inner
        .replace(/<em>([\s\S]*?)<\/em>/g, '_$1_')
        .replace(/<\/?em>/g, '');
      return '$$' + fixed + '$$';
    });

    // Inline: $ ... $ (solo si contiene <em>, para no tocar signos de dólar comunes)
    html = html.replace(/\$([^$\n]+)\$/g, function (match, inner) {
      if (inner.indexOf('<em>') === -1 && inner.indexOf('</em>') === -1) return match;
      var fixed = inner
        .replace(/<em>([\s\S]*?)<\/em>/g, '_$1_')
        .replace(/<\/?em>/g, '');
      return '$' + fixed + '$';
    });

    if (html !== article.innerHTML) {
      article.innerHTML = html;
    }
  }

  // ── KATEX: renderizar ─────────────────────────────────────────────
  function renderKatex(target) {
    if (typeof renderMathInElement === 'undefined') return;
    renderMathInElement(target, {
      delimiters: [
        { left: '$$', right: '$$', display: true },
        { left: '$', right: '$', display: false },
        { left: '\\[', right: '\\]', display: true },
        { left: '\\(', right: '\\)', display: false }
      ],
      ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre'],
      trust: true
    });
  }

  // ── OPTIMIZAR IMÁGENES DEL CONTENIDO ──────────────────────────────
  // Lazy-load + decoding async para no bloquear el renderizado.
  function optimizeImages(scope) {
    var imgs = (scope || document).querySelectorAll('.prose-class img:not([loading])');
    imgs.forEach(function (img) {
      img.loading = 'lazy';
      img.decoding = 'async';
    });
  }

  // Inicial: reparar + renderizar
  document.addEventListener('DOMContentLoaded', function () {
    var article = document.querySelector('.prose-class');
    if (article) {
      repairMathMangling(article);
      renderKatex(article);
      optimizeImages(article);
    }
  });

  // Fallback por si DOMContentLoaded ya pasó
  if (document.readyState === 'complete' || document.readyState === 'interactive') {
    var articleEl = document.querySelector('.prose-class');
    if (articleEl) {
      repairMathMangling(articleEl);
      renderKatex(articleEl);
      optimizeImages(articleEl);
    }
  }

  // ── Modernizar botones Show/Hide ─────────────────────────────────
  document.addEventListener('DOMContentLoaded', function () {
    var buttons = document.querySelectorAll('button[id^="Show"]');
    buttons.forEach(function (btn) {
      var num = btn.id.replace('Show', '');
      var content = document.getElementById('botoncito' + num);
      var hideBtn = document.getElementById('Hide' + num);
      if (!content) return;

      var wrapper = document.createElement('div');
      wrapper.className = 'overflow-hidden transition-all duration-500 ease-in-out my-3 rounded-xl border border-accent/20 bg-elevated/30';
      wrapper.style.maxHeight = '0';
      wrapper.style.opacity = '0';
      content.parentNode.insertBefore(wrapper, content);
      wrapper.appendChild(content);
      content.style.display = 'block';
      content.style.border = 'none';
      content.style.margin = '0';
      content.style.padding = '1.25rem';

      btn.className = 'inline-flex items-center gap-2 px-4 py-2.5 rounded-xl bg-accent text-white text-sm font-medium cursor-pointer hover:bg-accent-hover transition-all duration-200 border-0 shadow-sm hover:shadow-md mb-1';

      if (hideBtn) {
        hideBtn.className = 'inline-flex items-center gap-2 px-4 py-2.5 rounded-xl bg-secondary text-white text-sm font-medium cursor-pointer hover:bg-secondary-hover transition-all duration-200 border-0 shadow-sm hover:shadow-md mb-1';
        hideBtn.style.display = 'none';
      }

      btn.addEventListener('click', function () {
        wrapper.style.maxHeight = wrapper.scrollHeight + 'px';
        wrapper.style.opacity = '1';
        btn.style.display = 'none';
        if (hideBtn) hideBtn.style.display = 'inline-flex';
        // Reparar + renderizar KaTeX dentro del contenido recién visible
        repairMathMangling(wrapper);
        renderKatex(wrapper);
        optimizeImages(wrapper);
      });

      if (hideBtn) {
        hideBtn.addEventListener('click', function () {
          wrapper.style.maxHeight = '0';
          wrapper.style.opacity = '0';
          btn.style.display = 'inline-flex';
          hideBtn.style.display = 'none';
        });
      }
    });

    // ── Table of Contents (TOC) ──────────────────────────────────────
    var tocNav = document.querySelector('#class-toc nav');
    var article = document.querySelector('.prose-class');
    if (article && tocNav) {
      var headings = article.querySelectorAll('h2, h3');
      if (headings.length > 0) {
        var list = document.createElement('ul');
        list.className = 'space-y-1';
        headings.forEach(function (h, i) {
          if (!h.id) h.id = 'toc-' + i;
          var li = document.createElement('li');
          li.className = h.tagName === 'H3' ? 'pl-4' : '';
          var a = document.createElement('a');
          a.href = '#' + h.id;
          a.className = 'block text-xs py-1.5 px-2 rounded-lg text-text-muted hover:text-accent hover:bg-accent-soft transition-colors no-underline';
          a.textContent = h.textContent;
          li.appendChild(a);
          list.appendChild(li);
        });
        tocNav.appendChild(list);
      }
    }
  });
})();
