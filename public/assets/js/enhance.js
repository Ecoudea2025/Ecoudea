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

  // ── CONVERTIR <script type="math/tex"> → delimitadores KaTeX ──────
  // Tablas antiguas usan <script type="math/tex">\frac{1}{16}</script>
  // Rehype-raw los deja como <script> pero auto-render los ignora.
  function convertScriptMath(scope) {
    var scripts = scope.querySelectorAll('script[type="math/tex"], script[type="math/tex; mode=display"]');
    scripts.forEach(function (s) {
      var display = (s.getAttribute('type') || '').indexOf('mode=display') !== -1;
      var tex = (s.textContent || s.innerHTML || '').trim();
      if (!tex) return;
      var span = document.createElement('span');
      span.textContent = display ? '$$' + tex + '$$' : '\\(' + tex + '\\)';
      // Marcar para que no sea procesado como script ignorado
      s.parentNode.replaceChild(span, s);
    });
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

  // ── REPARAR DELIMITADORES LaTeX (desactivado: fuente ahora usa $...$ directamente)
  function repairDelimiters(article) { return; }

  // ── REPARAR HTML GARBADO (fallback por si remarkEscapeMath no cubrió algo) ──
  function repairGarbledHtml(article) {
    // Buscar elementos <z> / <Z> creados por el parser a partir de <Z en LaTeX
    var tags = article.querySelectorAll('z, Z');
    tags.forEach(function (el) {
      var text = (el.textContent || '').replace(/\s+/g, ' ').trim();
      var parent = el.parentNode;
      if (parent) {
        var tn = document.createTextNode('<' + el.tagName.toLowerCase() + (text ? ' ' + text : ''));
        parent.replaceChild(tn, el);
      }
    });
    // Decodificar entidades sueltas sin destruir DOM
    var walker = document.createTreeWalker(article, NodeFilter.SHOW_TEXT, null, false);
    var n;
    while ((n = walker.nextNode())) {
      if (n.nodeValue.indexOf('&#x3C;') !== -1 || n.nodeValue.indexOf('&#x3E;') !== -1) {
        n.nodeValue = n.nodeValue.replace(/&#x3C;/g, '<').replace(/&#x3E;/g, '>').replace(/&#x26;/g, '&');
      }
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
      convertScriptMath(article);
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
      convertScriptMath(articleEl);
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
        repairDelimiters(wrapper);
        repairGarbledHtml(wrapper);
        repairMathMangling(wrapper);
        convertScriptMath(wrapper);
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

    // ── Table of Contents (TOC jerárquico + scrollspy) ────────────────
    // Solo H2 como títulos principales; H3 se despliegan al entrar en su
    // sección y se pliegan al salir. El activo se marca en verde.
    var tocNav = document.querySelector('#class-toc nav');
    var article = document.querySelector('.prose-class');
    if (article && tocNav) {
      var headings = Array.prototype.slice.call(article.querySelectorAll('h2, h3'));
      if (headings.length > 0) {
        var list = document.createElement('ul');
        list.className = 'space-y-1 toc-root';
        var groups = [];
        var currentGroup = null;
        var linkById = {};
        headings.forEach(function (h, i) {
          if (!h.id) h.id = 'toc-' + i;
          var a = document.createElement('a');
          a.href = '#' + h.id;
          a.setAttribute('data-toc-id', h.id);
          if (h.tagName === 'H2') {
            var li = document.createElement('li');
            li.className = 'toc-group';
            a.className = 'toc-h2 block text-xs font-semibold py-1.5 px-2 rounded-lg text-text-muted hover:text-accent hover:bg-accent-soft transition-colors no-underline';
            a.innerHTML = h.innerHTML;
            li.appendChild(a);
            var sub = document.createElement('ul');
            sub.className = 'toc-sub space-y-0.5 mt-0.5';
            li.appendChild(sub);
            list.appendChild(li);
            currentGroup = { h2: a, sub: sub, ids: [h.id] };
            groups.push(currentGroup);
            linkById[h.id] = a;
          } else {
            var sli = document.createElement('li');
            a.className = 'toc-h3 block text-[11px] py-1 px-2 pl-4 rounded-lg text-text-muted/80 hover:text-accent hover:bg-accent-soft transition-colors no-underline border-l border-transparent';
            a.innerHTML = h.innerHTML;
            sli.appendChild(a);
            if (currentGroup) {
              currentGroup.sub.appendChild(sli);
              currentGroup.ids.push(h.id);
            } else {
              var topLi = document.createElement('li');
              topLi.appendChild(a);
              list.appendChild(topLi);
            }
            linkById[h.id] = a;
          }
        });
        tocNav.appendChild(list);

        var OFFSET = 140;
        var ticking = false;
        function headingTop(el) {
          var r = el.getBoundingClientRect();
          return r.top + window.scrollY;
        }
        function updateSpy() {
          var y = window.scrollY + OFFSET;
          var activeId = headings.length ? headings[0].id : null;
          headings.forEach(function (h) {
            if (headingTop(h) <= y) activeId = h.id;
          });
          Object.keys(linkById).forEach(function (id) {
            linkById[id].classList.toggle('toc-active', id === activeId);
          });
          groups.forEach(function (g) {
            var open = activeId && g.ids.indexOf(activeId) !== -1;
            g.sub.classList.toggle('open', !!open);
            g.h2.classList.toggle('toc-parent-active', !!open && activeId !== g.ids[0]);
          });
          ticking = false;
        }
        window.addEventListener('scroll', function () {
          if (!ticking) { ticking = true; requestAnimationFrame(updateSpy); }
        }, { passive: true });
        updateSpy();
        setTimeout(updateSpy, 500); // tras KaTeX / imágenes (cambian alturas)
      }
    }
  });
})();
