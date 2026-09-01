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

  // ── REPARAR DELIMITADORES LaTeX perdidos (\( \) → ( )) ─────────────
  // El parser markdown strippea \(` y `\)`, dejando `( ... )` sin formato.
  // Restaura `\(` y `\)` alrededor de contenido que parece LaTeX.
  function repairDelimiters(article) {
    var html = article.innerHTML;
    // Patrones LaTeX que indican fórmula matemática
    var latexRe = /([_(\\][^<]*?)/;
    // Encontrar `(` seguido de contenido LaTeX y `)` que no fue renderizado
    var fixed = html.replace(/\(([A-Za-z\\{}_^()\s,.\d]+?)\)(?=[.,;) <]|$)/g, function (match, inner) {
      // Solo restaurar si el contenido parece LaTeX (tiene _, ^, \, {, })
      if (/[\\{}^_]/.test(inner) && inner.length > 2 && inner.length < 500) {
        return '\\(' + inner + '\\)';
      }
      return match;
    });
    if (fixed !== html) {
      article.innerHTML = fixed;
    }
  }

  // ── REPARAR HTML GARBADO (LaTeX con <X parseado como tag HTML) ──────
  // El parser de markdown interpreta <Z, <z, etc. como tags HTML.
  // Restaura el LaTeX original antes de que KaTeX lo procese.
  function repairGarbledHtml(article) {
    var html = article.innerHTML;
    // Patrón: <x \leq="" ...)\)="" &#x3C;="" ...=""> seguido de </x>
    var fixed = html.replace(
      /<([a-zA-Z])\s[^>]*?=&quot;[^>]*?&#x3C;[^>]*?>[\s\S]*?<\/\1>/g,
      function (match) {
        // Extraer el contenido del tag garbado
        var inner = match.replace(/<[^>]+>/g, '').replace(/=&quot;/g, '').replace(/&#x3C;/g, '<').replace(/\s+/g, ' ').trim();
        return inner;
      }
    );
    if (fixed !== html) {
      article.innerHTML = fixed;
    }
  }

  // ── REPARAR RUTAS DE IMÁGENES (falta base URL en paths de markdown) ──
  // Markdown genera /assets/images/... pero con base=/Ecoudea debería ser /Ecoudea/assets/images/...
  function fixImagePaths(scope) {
    var base = document.querySelector('meta[name="astro-base"]')?.content
      || window.location.pathname.match(/^(\/[^/]+)\/?/)?.[1]
      || '';
    if (!base || base === '/assets') return; // sin base o en root
    var imgs = (scope || document).querySelectorAll('img[src^="/assets/"]');
    imgs.forEach(function (img) {
      img.src = base + img.src.replace(/^\/+/, '/');
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
      repairDelimiters(article);
      repairGarbledHtml(article);
      repairMathMangling(article);
      fixImagePaths(article);
      renderKatex(article);
      optimizeImages(article);
    }
  });

  // Fallback por si DOMContentLoaded ya pasó
  if (document.readyState === 'complete' || document.readyState === 'interactive') {
    var articleEl = document.querySelector('.prose-class');
    if (articleEl) {
      repairDelimiters(articleEl);
      repairGarbledHtml(articleEl);
      repairMathMangling(articleEl);
      fixImagePaths(articleEl);
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
        repairGarbledHtml(wrapper);
        repairMathMangling(wrapper);
        fixImagePaths(wrapper);
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
