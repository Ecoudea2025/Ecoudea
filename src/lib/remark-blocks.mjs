// Bloques teóricos para clases: sintaxis `:::tipo Título opcional` … `:::`
// Funciona en .md (sin MDX): convierte el rango en <div> accesible y numerado.
// Acepta formato compacto (todo en un párrafo) o con líneas en blanco.
// Tipos: definicion, teorema, lema, proposicion, demostracion, ejemplo,
//         ejercicio, ideaclave, nota, advertencia, intuicion.
const TYPES = {
  definicion: 'Definición',
  teorema: 'Teorema',
  lema: 'Lema',
  proposicion: 'Proposición',
  demostracion: 'Demostración',
  ejemplo: 'Ejemplo',
  ejercicio: 'Ejercicio',
  ideaclave: 'Idea clave',
  nota: 'Nota',
  advertencia: 'Advertencia',
  intuicion: 'Intuición',
};

// Texto inline de un párrafo (recursivo: negritas, enlaces, math, código…).
// Devuelve null si hay nodos que no se pueden serializar de forma segura.
function inlineText(node) {
  if (!node || node.type !== 'paragraph' || !node.children) return null;
  let s = '';
  const walk = (n) => {
    if (!n) return true;
    if (n.type === 'text' || n.type === 'inlineCode' || n.type === 'inlineMath') {
      s += n.value || '';
      return true;
    }
    if (n.type === 'image') {
      s += n.alt || '';
      return true;
    }
    if (n.type === 'html') {
      s += n.value || '';
      return true;
    }
    if (n.type === 'break') {
      s += '\n';
      return true;
    }
    if (n.type === 'strong' || n.type === 'emphasis' || n.type === 'link' || n.type === 'delete') {
      return (n.children || []).every(walk);
    }
    return false;
  };
  if (!node.children.every(walk)) return null;
  return s;
}

function openDiv(type, n, extra) {
  const label = `${TYPES[type]} ${n}${extra ? '. ' + extra : ''}`;
  const safe = label.replace(/"/g, '&quot;');
  return { type: 'html', value: `<div class="eco-block eco-${type}" role="note" aria-label="${safe}">\n<p class="eco-block-title">${label}</p>` };
}
const closeDiv = () => ({ type: 'html', value: '</div>' });

export function remarkBlocks() {
  return function (tree) {
    const counters = {};
    const kids = tree.children || [];
    const out = [];
    let i = 0;
    const emit = (type, extra, body) => {
      counters[type] = (counters[type] || 0) + 1;
      out.push(openDiv(type, counters[type], extra));
      if (body && body.length) {
        const hasContent = body.some(
          (n) => n.type !== 'text' || (n.value || '').trim() !== ''
        );
        if (hasContent) out.push({ type: 'paragraph', children: body });
      }
      out.push(closeDiv());
    };

    while (i < kids.length) {
      const node = kids[i];
      const full = inlineText(node);
      if (full !== null) {
        const lines = full.split('\n');
        const m = lines[0].match(/^:::\s*([a-z]+)(?:\s+(.*))?$/);
        if (m && TYPES[m[1]]) {
          const type = m[1];
          const extra = (m[2] || '').trim();
          const last = lines[lines.length - 1].trim();
          if (lines.length > 1 && last === ':::') {
            // ── Formato compacto: abrir y cerrar en el mismo párrafo ──
            const body = node.children.map((c) => ({ ...c }));
            // quitar primera línea del primer hijo de texto
            const first = body[0];
            if (first && first.type === 'text' && first.value.startsWith(lines[0])) {
              first.value = first.value.slice(lines[0].length).replace(/^\n/, '');
            } else {
              out.push(node);
              i++;
              continue;
            }
            // quitar última línea `:::` del último hijo de texto
            let ok = false;
            for (let k = body.length - 1; k >= 0; k--) {
              const c = body[k];
              if (c.type === 'text' && /\n:::\s*$/.test(c.value)) {
                c.value = c.value.replace(/\n:::\s*$/, '');
                ok = true;
                break;
              }
              if (c.type === 'text' && c.value.trim() !== '') break;
            }
            if (!ok) {
              out.push(node);
              i++;
              continue;
            }
            emit(type, extra, body);
            i++;
            continue;
          }
          if (lines.length === 1) {
            // ── Formato con líneas en blanco: buscar `:::` propio ──
            let j = i + 1;
            while (j < kids.length) {
              const t = inlineText(kids[j]);
              if (t !== null && t.trim() === ':::') break;
              j++;
            }
            if (j < kids.length) {
              // emitir: el opener no se copia; el closer tampoco
              counters[type] = (counters[type] || 0) + 1;
              out.push(openDiv(type, counters[type], extra));
              for (let k = i + 1; k < j; k++) out.push(kids[k]);
              out.push(closeDiv());
              i = j + 1;
              continue;
            }
          }
        }
      }
      out.push(node);
      i++;
    }
    tree.children = out;
  };
}
