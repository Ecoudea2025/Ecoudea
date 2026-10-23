// Macros KaTeX compartidas entre el contenido (build) y /tablero-latex (cliente).
// Una sola fuente de verdad: astro.config.mjs las inyecta a rehype-katex y
// tablero-latex.astro las importa para el preview en vivo.
// Sintaxis KaTeX: "\\NOMBRe": "expansión" (#1..#9 para argumentos).
export const katexMacros = {
  '\\E': '\\mathbb{E}',
  '\\Var': '\\operatorname{Var}',
  '\\Cov': '\\operatorname{Cov}',
  '\\Corr': '\\operatorname{Corr}',
  '\\Prob': '\\mathbb{P}',
  '\\R': '\\mathbb{R}',
  '\\N': '\\mathbb{N}',
  '\\Z': '\\mathbb{Z}',
  '\\iid': '\\mathrm{iid}',
  '\\dd': '\\mathrm{d}',
  '\\argmax': '\\operatorname*{arg\\,max}',
  '\\argmin': '\\operatorname*{arg\\,min}',
  '\\given': '\\,|\\,',
  '\\xb': '\\bar{x}',
};
