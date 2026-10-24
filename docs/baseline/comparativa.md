# Baseline vs. rework (Fase 8.b)

Medido con `npm run build` (astro + pagefind + gzip). Sin Lighthouse en este
entorno (queda para el CI con `lhci` contra producción en la Fase 8 final).

| Métrica | v1-legacy (`v1-legacy`) | Rework (Fase 8.b) |
|---|---|---|
| `dist/` total | 95,6 MB | **25,7 MB (−73%)** |
| Páginas HTML | 171 | 165 (25 activas + 133 stubs + 7 sistema) |
| Home sin gzip / gz | 49,8 KB / 7,9 KB | 68 KB / 12,2 KB (+modal, índice embebido, SVG hero) |
| Página más pesada | 2222 KB (arch.) | 1080 KB (KaTeX legítimo, gz mediante) |
| Tablero JS | 261 KB / 78 KB gz | igual (solo se carga en `/tablero-latex`) |
| Imágenes en `dist` | 330 (54,5 MB en `public/`) | 78 (+ iconos); 252 a `archive/` (29,4 MB) |
| JPG activos | ~1 MB c/u | max 1400px, q82 (32,5 → 13,3 MB) |
| `favicon.ico` 1,1 MB sin uso | sí | no (a `archive/`) |
| KaTeX woff2+woff+ttf | triplicado (~1,4 MB) | igual (subsets: pendiente, ver nota) |
| `${base}` literales | 52 | **0** (helper `url()`) |
| Búsqueda | filtro de 10 títulos | Pagefind real en 165 páginas |

## Notas

- El peso restante grande es legítimo: KaTeX por página con fórmulas y las
  figuras JPG del contenido heredado (ya comprimidas).
- KaTeX triplica formatos (woff2+woff+ttf ≈ 1,4 MB). Subsetear requiere
  `fonttools` + lista de glifos usados: backlog documentado, no bloqueante
  (las fuentes se cachean y solo cargan en páginas con fórmulas).
- `og:image` sigue siendo el PNG del logo (0,97 MB tras recompresión):
  las redes no aceptan SVG. Generar un OG de 1200×630 queda para Fase 9.
