import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';
import rehypeRaw from 'rehype-raw';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

const base = '/Ecoudea';

function remarkBaseImages() {
  return function (tree) {
    tree.children.push({ type: 'html', value: '<!--REMARK-RAN-->' });
    const visit = (node) => {
      if (node.type === 'image' && node.url && node.url.startsWith('/assets/')) {
        node.url = base + node.url;
      }
      if (node.children) node.children.forEach(visit);
    };
    visit(tree);
  };
}

// Las regiones <pre>/<code> son código fuente (R, Python...), nunca math:
// sus $ sueltos (operador $ de R, etc.) no deben parearse. Se procesa solo
// fuera de esas regiones; dentro quedan intactas.
function withCodeProtected(value, fn) {
  const parts = value.split(/(<pre[\s\S]*?<\/pre>|<code[\s\S]*?<\/code>)/gi);
  for (let i = 0; i < parts.length; i += 2) {
    parts[i] = fn(parts[i]);
  }
  return parts.join('');
}

function createDisplayMathNode(value) {
  // mdast-util-to-hast necesita estos metadatos; sin ellos, un nodo math
  // manual se degrada a texto plano.
  return {
    type: 'math',
    value,
    meta: null,
    data: {
      hName: 'pre',
      hChildren: [
        {
          type: 'element',
          tagName: 'code',
          properties: { className: ['language-math', 'math-display'] },
          children: [{ type: 'text', value }],
        },
      ],
    },
  };
}

function remarkDisplayMathBlocks() {
  // Pareo ESTRICTO: el interior no puede contener $ (permite \$ escapado).
  // Así un $$ nunca traga fórmulas vecinas ni prosa con $ sueltos.
  // Además el interior debe parecer LaTeX real: con backslash, o bien de
  // una sola línea (los $$ multilínea sin backslash suelen ser $$$$ vacíos
  // o texto con dólares que no debe tocarse).
  // Regex local (no compartida): la recursión corrompería lastIndex global.
  const looksLikeDisplay = (value) => {
    const inner = value.trim();
    if (!inner || inner.length > 4000) return false;
    if (/<\/?[A-Za-z!][^<>]*>/.test(inner)) return false;
    return /\\/.test(inner) || !inner.includes('\n');
  };
  const escapeAngles = (value) => value.replaceAll('<', '\\lt ').replaceAll('>', '\\gt ');
  const splitTextValue = (value) => {
    const parts = [];
    let lastIndex = 0;
    const pattern = /\$\$((?:\\\$|[^$])+?)\$\$/g;
    let match;
    while ((match = pattern.exec(value)) !== null) {
      if (!looksLikeDisplay(match[1])) {
        // Rebobinar tras el $$ de apertura para no consumir un cierre ajeno.
        pattern.lastIndex = match.index + 2;
        continue;
      }
      if (match.index > lastIndex) {
        parts.push({ type: 'text', value: value.slice(lastIndex, match.index) });
      }
      parts.push(createDisplayMathNode(escapeAngles(match[1])));
      lastIndex = match.index + match[0].length;
    }
    if (parts.length === 0) return null;
    if (lastIndex < value.length) {
      parts.push({ type: 'text', value: value.slice(lastIndex) });
    }
    return parts;
  };
  const hasRealTags = (value) => /<\/?[A-Za-z!][^<>]*>/.test(value);
  const escapeDelimitedAngles = (value) => withCodeProtected(value, (seg) => seg
    .replace(/\$\$((?:\\\$|[^$])+?)\$\$/g, (m, inner) => (hasRealTags(inner) ? m : '$$' + inner.replaceAll('<', '\\lt ').replaceAll('>', '\\gt ') + '$$'))
    .replace(/\$([^$\n]+?)\$/g, (m, inner) => (hasRealTags(inner) ? m : '$' + inner.replaceAll('<', '\\lt ').replaceAll('>', '\\gt ') + '$')));
  const visit = (node, index, parent) => {
    if (!node || !parent || typeof index !== 'number') return;
    // Nodos math malformados: el parser unió el cierre $$ con texto posterior
    // (y el \begin{...} quedó en node.meta, no en value). Se reconstruye el
    // bloque original y se vuelve a partir correctamente.
    if (node.type === 'math' && typeof node.value === 'string' && node.value.includes('$$')) {
      const full = '$$' + (node.meta ? node.meta + '\n' : '') + node.value;
      const parts = splitTextValue(full);
      if (parts) {
        parent.children.splice(index, 1, ...parts);
        parts.forEach((child, offset) => visit(child, index + offset, parent));
        return;
      }
    }
    if ((node.type === 'text' || node.type === 'html') && typeof node.value === 'string' && node.value.includes('$$')) {
      // Segmentar por regiones <pre>/<code>: su contenido nunca se toca.
      const segments = node.value.split(/(<pre[\s\S]*?<\/pre>|<code[\s\S]*?<\/code>)/gi);
      const newParts = [];
      let changed = false;
      segments.forEach((seg, si) => {
        if (si % 2 === 1 || !seg.includes('$$')) {
          newParts.push({ type: node.type, value: seg });
          return;
        }
        const parts = splitTextValue(seg);
        if (parts) {
          changed = true;
          parts.forEach((part) => {
            newParts.push(part.type === 'text' ? { type: node.type, value: part.value } : part);
          });
        } else {
          newParts.push({ type: node.type, value: seg });
        }
      });
      if (changed) {
        parent.children.splice(index, 1, ...newParts);
        newParts.forEach((child, offset) => visit(child, index + offset, parent));
        return;
      }
    }
    if (node.children) {
      for (let i = 0; i < node.children.length; i += 1) {
        visit(node.children[i], i, node);
      }
    }
  };

  return function (tree) {
    visit(tree, -1, null);
    // Recorrer hijos de la raíz de forma segura.
    for (let i = 0; i < (tree.children || []).length; i += 1) {
      visit(tree.children[i], i, tree);
    }
  };
}

function remarkPromoteDisplayMath() {
  // Solo construcciones que KaTeX no admite en modo inline se promueven
  // a bloque display.
  const DISPLAY_ENVIRONMENTS = /^\s*\\begin\{(align\*?|aligned|equation\*?|gather\*?|multline\*?|flalign\*?|alignat\*?)\}/;
  const DISPLAY_CLOSING = /\\end\{(align\*?|aligned|equation\*?|gather\*?|multline\*?|flalign\*?|alignat\*?)\}/;
  const ALIGNMENT_TAB = /(^|[^\\])&/;
  const isMeaningful = (node) => {
    if (!node) return false;
    if (node.type === 'text') return node.value.trim() !== '';
    if (node.type === 'inlineMath' || node.type === 'math') return true;
    return (node.children || []).some(isMeaningful);
  };

  return function (tree) {
    const visitParent = (parent) => {
      if (!parent?.children) return;
      for (let i = 0; i < parent.children.length; i += 1) {
        const child = parent.children[i];
        if (child.type === 'paragraph' && Array.isArray(child.children)) {
          for (let j = 0; j < child.children.length; j += 1) {
            const grandchild = child.children[j];
            const value = grandchild?.type === 'inlineMath' ? grandchild.value || '' : '';
            if (grandchild?.type === 'inlineMath' && (DISPLAY_ENVIRONMENTS.test(value) || DISPLAY_CLOSING.test(value) || ALIGNMENT_TAB.test(value))) {
              const before = child.children.slice(0, j).filter(isMeaningful);
              const after = child.children.slice(j + 1).filter(isMeaningful);
              const replacement = [
                ...(before.length ? [{ ...child, children: before }] : []),
                createDisplayMathNode(grandchild.value),
                ...(after.length ? [{ ...child, children: after }] : []),
              ];
              parent.children.splice(i, 1, ...replacement);
              // Reprocesar desde el primer nodo insertado: el párrafo `after`
              // puede contener más fórmulas display (antes se saltaba con i += ...).
              i -= 1;
              break;
            }
          }
        }
        if (child.children) visitParent(child);
      }
    };
    visitParent(tree);
  };
}

function remarkEscapeMath() {
  return function (tree) {
    const escapeAngles = (value) => value.replaceAll('<', '\\lt ').replaceAll('>', '\\gt ');
    const hasRealTags = (value) => /<\/?[A-Za-z!][^<>]*>/.test(value);
    const escapeDelimited = (value) => withCodeProtected(value, (seg) => seg
      .replace(/\$\$((?:\\\$|[^$])+?)\$\$/g, (m, inner) => (hasRealTags(inner) ? m : '$$' + escapeAngles(inner) + '$$'))
      .replace(/\$([^$\n]+?)\$/g, (m, inner) => (hasRealTags(inner) ? m : '$' + escapeAngles(inner) + '$')));
    const visit = (node) => {
      if ((node.type === 'inlineMath' || node.type === 'math') && typeof node.value === 'string') {
        node.value = escapeAngles(node.value);
      }
      // El HTML crudo (tablas y listas heredadas) es opaco para remark-math:
      // escapar < > solo dentro de sus delimitadores $...$ antes de rehypeRaw.
      if (node.type === 'html' && typeof node.value === 'string' && node.value.includes('$')) {
        node.value = escapeDelimited(node.value);
      }
      if (node.type === 'text' && typeof node.value === 'string' && node.value.includes('\\(')) {
        node.value = node.value.replace(/\\\(.*?\\\)/g, (m) => escapeAngles(m));
      }
      if (node.children) node.children.forEach(visit);
    };
    visit(tree);
  };
}

// Convierte $...$ restante (sobre todo dentro de HTML crudo como tablas,
// listas y acordeones <main>) en nodos math-*. remark-math ya procesó el
// Markdown normal; aquí solo quedan literales sin procesar. Se excluyen
// pre/code/script y nodos ya matemáticos para no duplicar renderizados.
// El pareo $$ es estricto (sin $ interior) para no tragar fórmulas vecinas.
function rehypeRawDollarMath() {
  // Regex LOCAL por invocación: una global compartida sufre carreras de
  // lastIndex cuando Astro renderiza archivos en paralelo.
  const makePattern = () => /\$\$((?:\\\$|[^$])+?)\$\$|\$((?:\\.|[^$\n])+?)\$/g;
  const hasMathClass = (properties) => {
    const classes = properties?.className;
    if (!classes) return false;
    const list = Array.isArray(classes) ? classes : [classes];
    return list.some((name) => ['katex', 'math-inline', 'math-display', 'language-math'].includes(name));
  };
  const isIgnoredTag = (tagName) => ['pre', 'code', 'script', 'style', 'textarea', 'noscript'].includes(tagName);
  const looksLikeDisplay = (value) => {
    const inner = (value || '').trim();
    if (!inner || inner.length > 4000) return false;
    if (/<\/?[A-Za-z!][^<>]*>/.test(inner)) return false;
    return /\\/.test(inner) || !inner.includes('\n');
  };

  function splitTextNode(text) {
    const nodes = [];
    let lastIndex = 0;
    const pattern = makePattern();
    let match;
    while ((match = pattern.exec(text)) !== null) {
      const explicitDisplay = match[0].startsWith('$$');
      const value = explicitDisplay ? match[1] : match[2];
      if (explicitDisplay && !looksLikeDisplay(value)) {
        pattern.lastIndex = match.index + 2;
        continue;
      }
      // No emparejar $ sobre etiquetas HTML reales (código R con spans):
      // dejar literal en vez de generar un span matemático inválido.
      if (!explicitDisplay && /<\/?[A-Za-z!][^<>]*>/.test(value || '')) {
        pattern.lastIndex = match.index + 1;
        continue;
      }

      if (match.index > lastIndex) {
        nodes.push({ type: 'text', value: text.slice(lastIndex, match.index) });
      }
      // align, cierres, saltos y tabuladores requieren modo display aunque
      // vengan dentro de HTML crudo sin clasificar.
      const display = explicitDisplay
        || /^\s*\\begin\{(align\*?|aligned|equation\*?|gather\*?|multline\*?|flalign\*?|alignat\*?)\}/.test(value || '')
        || /\\end\{(align\*?|aligned|equation\*?|gather\*?|multline\*?|flalign\*?|alignat\*?)\}/.test(value || '')
        || /(^|[^\\])\\\\/.test(value || '')
        || /(^|[^\\])&/.test(value || '');
      nodes.push({
        type: 'element',
        tagName: 'span',
        properties: { className: [display ? 'math-display' : 'math-inline'] },
        children: [{ type: 'text', value }],
      });
      lastIndex = match.index + match[0].length;
    }
    if (lastIndex < text.length) {
      nodes.push({ type: 'text', value: text.slice(lastIndex) });
    }
    return nodes;
  }

  function visitChildren(children, inIgnored) {
    const output = [];
    for (const child of children || []) {
      if (!child) continue;
      if (child.type === 'element') {
        const tagName = String(child.tagName || '').toLowerCase();
        const nextIgnored = inIgnored || isIgnoredTag(tagName) || hasMathClass(child.properties);
        child.children = visitChildren(child.children, nextIgnored);
        output.push(child);
      } else if (child.type === 'text' && !inIgnored && child.value.includes('$')) {
        output.push(...splitTextNode(child.value));
      } else {
        if (child.children) {
          child.children = visitChildren(child.children, inIgnored);
        }
        output.push(child);
      }
    }
    return output;
  }

  return function (tree) {
    tree.children = visitChildren(tree.children, false);
  };
}

function rehypeBaseImages() {
  return function (tree) {
    const visit = (node) => {
      if (node.type === 'element' && node.tagName === 'img') {
        const src = node.properties?.src;
        if (typeof src === 'string' && src.startsWith('/assets/')) {
          node.properties.src = base + src;
        }
      }
      if (node.children) node.children.forEach(visit);
    };
    visit(tree);
  };
}

export default defineConfig({
  site: 'https://ecoudea2025.github.io',
  base,
  trailingSlash: 'ignore',
  prefetch: true,
  integrations: [
    sitemap({
      filter: (page) => !page.includes('/admin'),
    }),
  ],
  markdown: {
    smartypants: false,
    syntaxHighlight: 'shiki',
    shikiConfig: {
      theme: 'one-dark-pro',
      wrap: false,
    },
    remarkPlugins: [remarkEscapeMath, remarkDisplayMathBlocks, remarkMath, remarkPromoteDisplayMath, remarkBaseImages],
    rehypePlugins: [
      rehypeRaw,
      rehypeRawDollarMath,
      [rehypeKatex, { strict: false, trust: true, output: 'htmlAndMathml' }],
      rehypeBaseImages,
    ],
  },
  vite: {
    plugins: [tailwindcss()],
  },
  build: {
    inlineStylesheets: 'auto',
  },
});
