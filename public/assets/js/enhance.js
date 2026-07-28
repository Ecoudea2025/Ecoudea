(function () {
  'use strict';

  // --- KaTeX: render immediately (enhance.js loads AFTER katex + auto-render) ---
  if (typeof renderMathInElement !== 'undefined') {
    var el = document.querySelector('.prose-class');
    if (el) {
      renderMathInElement(el, {
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
  }

  // --- Modernize old Show/Hide buttons ---
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
        // Re-render KaTeX inside newly visible content
        if (typeof renderMathInElement !== 'undefined') {
          renderMathInElement(wrapper, {
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

    // --- Table of Contents (TOC) ---
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
