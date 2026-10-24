// Referencias a ecuaciones entre clases: `$\ref{etiqueta}$` standalone
// se convierte en enlace al ancla de la ecuación (`\tag{etiqueta}`).
// El índice lo genera scripts/gen-indices.cjs (prebuild).
// Un \ref a una etiqueta inexistente ROMPE el build con el archivo culpable.
import index from './ecuaciones.json' with { type: 'json' };

const base = process.env.BASE_PATH || '/Ecoudea';
const REF = /^\\ref\{([A-Za-z0-9:_-]+)\}$/;
const TAG = /\\tag\{([A-Za-z0-9:_-]+)\}/;

export function remarkEqrefs() {
  return function (tree, file) {
    const name = (file?.history?.[0] || '').split(/[\\/]/).pop() || '?';
    const visit = (node) => {
      if (!node) return;
      if ((node.type === 'math' || node.type === 'inlineMath') && typeof node.value === 'string') {
        const m = node.value.trim().match(REF);
        if (m) {
          const label = m[1];
          const hit = index[label];
          if (!hit) {
            throw new Error(
              `[eqref] referencia a ecuación inexistente "${label}" en ${name}. ` +
              `Etiqueta con \\tag{${label}} en alguna clase publicada o corrige el \\ref.`
            );
          }
          node.type = 'html';
          node.value = `<a class="eq-ref" href="${base}/cursos/${hit.course}/${hit.class}#eq-${label}">(${label})</a>`;
          delete node.data;
          return;
        }
      }
      if (node.children) {
        const kids = [];
        for (const child of node.children) {
          visit(child);
          // ancla para ecuaciones display etiquetadas (el \tag lo renderiza KaTeX)
          if (child.type === 'math' && typeof child.value === 'string') {
            const t = child.value.match(TAG);
            if (t) kids.push({ type: 'html', value: `<span class="eq-anchor" id="eq-${t[1]}" aria-hidden="true"></span>` });
          }
          kids.push(child);
        }
        node.children = kids;
      }
    };
    visit(tree);
  };
}
