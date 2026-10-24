(function () {
  'use strict';

  // ── REPARAR RUTAS DE IMÁGENES (fallback; el build ya antepone el base) ──
  function fixImagePaths(scope) {
    var base = document.querySelector('meta[name="astro-base"]')?.content
      || window.location.pathname.match(/^(\/[^/]+)\/?/)?.[1]
      || '';
    if (!base || base === '/assets') return;
    var imgs = (scope || document).querySelectorAll('img[src^="/assets/"]');
    imgs.forEach(function (img) {
      img.src = base + img.src.replace(/^\/+/, '/');
    });
  }

  // ── OPTIMIZAR IMÁGENES DEL CONTENIDO (lazy + async) ───────────────
  function optimizeImages(scope) {
    var imgs = (scope || document).querySelectorAll('.prose-class img:not([loading])');
    imgs.forEach(function (img) {
      img.loading = 'lazy';
      img.decoding = 'async';
    });
  }

  function enhanceContent(scope) {
    fixImagePaths(scope);
    optimizeImages(scope);
    accessibleMath(scope);
    copyableMath(scope);
    linkTerms(scope);
  }

  // ── TÉRMINOS DEL GLOSARIO (<Term id> → enlace) ────────────────────
  // Sin JS el término se lee igual (estilo punteado por CSS); con JS enlaza.
  function linkTerms(scope) {
    var base = document.querySelector('meta[name="astro-base"]')?.content || '';
    var terms = (scope || document).querySelectorAll('term[id]:not([data-linked])');
    terms.forEach(function (t) {
      t.setAttribute('data-linked', '1');
      var a = document.createElement('a');
      a.href = base + '/glosario#term-' + t.getAttribute('id');
      a.className = 'term-ref';
      while (t.firstChild) a.appendChild(t.firstChild);
      t.appendChild(a);
    });
  }

  // ── FÓRMULAS DISPLAY ACCESIBLES CON TECLADO ─────────────────────
  // El scroll horizontal funciona sin JS; esto añade rol + etiqueta.
  function accessibleMath(scope) {
    var displays = (scope || document).querySelectorAll('.katex-display:not([data-a11y])');
    displays.forEach(function (d) {
      d.setAttribute('data-a11y', '1');
      d.setAttribute('tabindex', '0');
      d.setAttribute('role', 'region');
      d.setAttribute('aria-label', 'Fórmula matemática (desplaza horizontalmente si se desborda)');
    });
  }

  // ── BOTÓN "COPIAR TEX" EN FÓRMULAS DISPLAY ───────────────────────
  // Lee el <annotation encoding="application/x-tex"> que emite KaTeX.
  function copyableMath(scope) {
    var displays = (scope || document).querySelectorAll('.katex-display:not([data-copy])');
    displays.forEach(function (d) {
      d.setAttribute('data-copy', '1');
      var ann = d.querySelector('annotation[encoding="application/x-tex"]');
      if (!ann || !navigator.clipboard) return;
      var tex = ann.textContent;
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.textContent = 'Copiar TeX';
      btn.className = 'copy-tex-btn';
      btn.style.cssText = 'display:block;margin:0.25rem auto 0;font-size:11px;padding:0.2rem 0.7rem;border-radius:9999px;border:1px solid var(--color-border-subtle);background:transparent;color:var(--color-text-muted);cursor:pointer;';
      btn.addEventListener('click', function () {
        navigator.clipboard.writeText(tex).then(function () {
          btn.textContent = 'Copiado ✓';
          setTimeout(function () { btn.textContent = 'Copiar TeX'; }, 1500);
        }).catch(function () {});
      });
      d.appendChild(btn);
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    var article = document.querySelector('.prose-class');
    if (article) enhanceContent(article);

    // ── Modernizar botones Show/Hide ────────────────────────────────
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
        enhanceContent(wrapper);
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

    // ── Table of Contents (TOC jerárquico + scrollspy, escritorio y móvil) ──
    var tocNavs = Array.prototype.slice.call(document.querySelectorAll('#class-toc nav, #class-toc-mobile nav'));
    var article = document.querySelector('.prose-class');
    if (article && tocNavs.length) {
      var headings = Array.prototype.slice.call(article.querySelectorAll('h2, h3'));
      if (headings.length === 0) {
        var mobileToc = document.getElementById('class-toc-mobile');
        if (mobileToc) mobileToc.classList.add('hidden');
      }
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
        tocNavs.forEach(function (tocNav) {
          tocNav.appendChild(list.cloneNode(true));
        });

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
          // Aplica a todos los navs (escritorio + móvil); los grupos se
          // resuelven por estructura DOM, no por referencias únicas.
          tocNavs.forEach(function (tocNav) {
            tocNav.querySelectorAll('a[data-toc-id]').forEach(function (a) {
              a.classList.toggle('toc-active', a.getAttribute('data-toc-id') === activeId);
            });
            tocNav.querySelectorAll('.toc-group').forEach(function (li) {
              var ids = Array.prototype.map.call(
                li.querySelectorAll('a[data-toc-id]'),
                function (a) { return a.getAttribute('data-toc-id'); }
              );
              var sub = li.querySelector('.toc-sub');
              var h2 = li.querySelector('.toc-h2');
              var open = !!activeId && ids.indexOf(activeId) !== -1;
              if (sub) sub.classList.toggle('open', open);
              if (h2) h2.classList.toggle('toc-parent-active', open && ids[0] !== activeId);
            });
          });
          ticking = false;
        }
        window.addEventListener('scroll', function () {
          if (!ticking) { ticking = true; requestAnimationFrame(updateSpy); }
        }, { passive: true });
        updateSpy();
        setTimeout(updateSpy, 500);
      }
    }
  });
})();
