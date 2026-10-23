# Baseline v1-legacy (2026-10-23, commit 6c6c598)

Medido con `npm run build` (astro build + gzip). Sin Lighthouse (pendiente: correr en CI Fase 8).

## Totales
- `dist/`: **95,6 MB** (el peso son las 349 imágenes sin optimizar en `public/assets/images/`)
- Páginas HTML: **171**
- Ahorro por gzip: ~33,11 MB en transferencia (182 archivos precomprimidos)

## Home (`/index.html`)
- 49,8 KB → 7,9 KB gz

## Páginas más pesadas (HTML sin gzip)
| Página | Peso |
|---|---|
| especializacion-socioeconomica-clase-01-sesion-04 | 2222 KB |
| especializacion-socioeconomica-clase-02-sesion-03 | 1102 KB |
| estadistica-ii-clase-22 | 1061 KB |
| probabilidad-inferencia-clase-08 | 1015 KB |
| probabilidad-inferencia-clase-07 | 932 KB |

## JS/CSS por página
- CSS contenido (`_astro_content`): 75,3 KB → 13,8 KB gz (KaTeX + global, en páginas con fórmulas)
- KaTeX CSS: 28,6 KB → 7,6 KB gz
- `page.*.js`: 2,4 KB → 1,1 KB gz (islas mínimas Astro)
- Tablero LaTeX JS: **261,3 KB → 77,9 KB gz** (KaTeX en cliente, solo en `/tablero-latex`)
- Fuentes: Inter latin 47 KB, Sora latin 33 KB, Fraunces latin 36 KB (woff2); KaTeX trae woff2+woff+ttf por familia (triplicado, optimizable en Fase 8)

## Deuda visible en el baseline
- Contadores SSR en `0` y typewriter vacían contenido sin JS (falso "0 cursos").
- 5 páginas >900 KB: revisar qué las infla (imágenes base64 o KaTeX masivo) en Fase 8.
- Fuentes KaTeX ×3 formatos;Subsetear en Fase 8.
