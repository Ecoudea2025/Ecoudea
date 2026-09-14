/**
 * Plugins de Markdown para renderizar KaTeX en tiempo de build (SSR).
 *
 * El contenido viene de R Markdown / Bookdown del sitio original y mezcla
 * varios formatos de matemáticas:
 *   - code-spans:            `$X$`, `$$...$$`
 *   - texto markdown:        $X$ y $$...$$  (los reconoce remark-math)
 *   - HTML crudo:            <li>... $Y$ ...</li>, <code>$Z$</code>
 *   - scripts heredados:     <script type="math/tex">\frac{1}{16}</script>
 *
 * remark-math protege `_`, `\\` y `<`/`>` en el nivel markdown, pero:
 *   - guarda el TeX en `data.hChildren`, así que hay que normalizarlo ahí;
 *   - no toca code-spans, HTML crudo ni scripts.
 * Lo demás lo completan `rehypeMathNormalize` + rehype-katex, sin JS en el
 * cliente (nada de parpadeo ni recuadro gris).
 */

const DISPLAY_ENVS =
  /\\begin\{(?:align|align\*|alignat|alignat\*|equation|equation\*|gather|gather\*|multline|multline\*|flalign|flalign\*|split|CD)\}/

/** Detecta si un texto es exactamente una expresión matemática delimitada. */
function parseDelims(value) {
  let m
  if ((m = /^\$\$([\s\S]+?)\$\$$/.exec(value))) return { tex: m[1], display: true }
  if ((m = /^\$([^$\n]+?)\$$/.exec(value))) return { tex: m[1], display: false }
  if ((m = /^\\\(([\s\S]+?)\\\)$/.exec(value))) return { tex: m[1], display: false }
  if ((m = /^\\\[([\s\S]+?)\\\]$/.exec(value))) return { tex: m[1], display: true }
  return null
}

/**
 * Sanea el TeX para KaTeX: elimina comandos no soportados y escapa caracteres
 * problemáticos dentro de `\text{...}` (KaTeX no admite `#` ni `_` sin escapar).
 */
export function sanitizeTex(tex) {
  return tex
    .replace(/\\label\{[^}]*\}/g, '')
    .replace(/\\nonumber\b/g, '')
    .replace(/\\notag\b/g, '')
    .replace(/(?<!\\)\$/g, '\\$')
    .replace(/</g, '\\lt ')
    .replace(/>/g, '\\gt ')
    .replace(/\\text\{([^}]*)\}/g, (_m, inner) => `\\text{${inner.replace(/(?<!\\)([#_])/g, '\\$1')}}`)
}

/* ─────────────────────────── mdast (remark) ─────────────────────────── */

/** Construye un nodo de math con el TeX ya saneado en `data.hChildren`. */
function mdastMath(tex, display) {
  tex = sanitizeTex(tex)
  return display
    ? {
        type: 'math',
        value: tex,
        meta: null,
        data: {
          hName: 'code',
          hProperties: { className: ['language-math', 'math-display'] },
          hChildren: [{ type: 'text', value: tex }],
        },
      }
    : {
        type: 'inlineMath',
        value: tex,
        data: {
          hName: 'code',
          hProperties: { className: ['language-math', 'math-inline'] },
          hChildren: [{ type: 'text', value: tex }],
        },
      }
}

/**
 * Normaliza todos los nodos de math:
 *   - convierte code-spans con LaTeX (`$X$`, `$$...$$`) en math;
 *   - promueve a display los `$...$` que eran `$$...$$` con entornos display;
 *   - escribe el TeX saneado en `data.hChildren` (lo que remark-math ignora).
 * Debe ejecutarse DESPUÉS de remark-math.
 */
export function remarkNormalizeMath() {
  return (tree) => {
    const walk = (node) => {
      if (!Array.isArray(node.children)) return
      for (let i = 0; i < node.children.length; i++) {
        const child = node.children[i]
        if (child.type === 'inlineMath' || child.type === 'math') {
          const display = child.type === 'math' || DISPLAY_ENVS.test(child.value || '')
          node.children[i] = mdastMath(child.value || '', display)
          continue
        }
        if (child.type === 'inlineCode') {
          const parsed = parseDelims(child.value.trim())
          if (parsed) {
            node.children[i] = mdastMath(parsed.tex, parsed.display)
            continue
          }
        }
        walk(child)
      }
    }
    walk(tree)
  }
}

/* ─────────────────────────── hast (rehype) ─────────────────────────── */

function hastMath(tex, display) {
  return {
    type: 'element',
    tagName: 'span',
    properties: { className: display ? ['math', 'math-display'] : ['math', 'math-inline'] },
    children: [{ type: 'text', value: sanitizeTex(tex) }],
  }
}

function textContent(node) {
  if (node.type === 'text') return node.value || ''
  if (Array.isArray(node.children)) return node.children.map(textContent).join('')
  return ''
}

function hasLanguageMath(node) {
  if (node.type === 'element') {
    const cls = node.properties && node.properties.className
    if (Array.isArray(cls) && cls.includes('language-math')) return true
  }
  return Array.isArray(node.children) && node.children.some(hasLanguageMath)
}

const SPLIT_RE = /(\$\$[\s\S]*?\$\$|\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)|\$[^$\n]+?\$)/g

function splitText(value) {
  // Fragmentos de HTML crudo o código: nunca contienen math real.
  if (value.indexOf('<') !== -1 || value.indexOf('>') !== -1) {
    return [{ type: 'text', value }]
  }
  if (value.indexOf('$') === -1 && value.indexOf('\\(') === -1 && value.indexOf('\\[') === -1) {
    return [{ type: 'text', value }]
  }
  const parts = value.split(SPLIT_RE)
  const nodes = []
  for (const part of parts) {
    if (!part) continue
    const parsed = parseDelims(part)
    if (parsed && parsed.tex.trim()) nodes.push(hastMath(parsed.tex, parsed.display))
    else nodes.push({ type: 'text', value: part })
  }
  return nodes.length ? nodes : [{ type: 'text', value }]
}

/**
 * Normaliza el HTML crudo antes de rehype-katex:
 *   1. <script type="math/tex"> → math
 *   2. desenvuelve <code> que envuelve math (evita el recuadro gris)
 *   3. parte texto con delimitadores LaTeX en nodos de math
 */
export function rehypeMathNormalize() {
  return (tree) => {
    const normalize = (parent) => {
      const out = []
      for (const child of parent.children || []) {
        if (child.type === 'element') {
          const props = child.properties || {}
          const cls = Array.isArray(props.className) ? props.className : []

          if (
            child.tagName === 'script' &&
            typeof props.type === 'string' &&
            props.type.startsWith('math/tex')
          ) {
            const display = props.type.includes('mode=display')
            const tex = textContent(child).trim()
            if (tex) {
              out.push(hastMath(tex, display))
              continue
            }
          }

          if (child.tagName === 'code' && !cls.includes('language-math')) {
            if (hasLanguageMath(child)) {
              out.push(...child.children)
              continue
            }
            const tex = textContent(child).trim()
            const parsed = parseDelims(tex)
            if (parsed && parsed.tex.trim()) {
              out.push(hastMath(parsed.tex, parsed.display))
              continue
            }
          }

          if (cls.includes('language-math')) {
            out.push(child)
            continue
          }

          // Elementos opacos: no escanear su texto interno (código, scripts).
          if (['pre', 'code', 'script', 'style', 'textarea'].includes(child.tagName)) {
            out.push(child)
            continue
          }

          normalize(child)
          out.push(child)
          continue
        }

        if (child.type === 'text') {
          out.push(...splitText(child.value || ''))
          continue
        }

        if (Array.isArray(child.children)) normalize(child)
        out.push(child)
      }
      parent.children = out
    }

    normalize(tree)
  }
}
