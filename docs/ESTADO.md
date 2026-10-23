# Estado del proyecto
Fase actual: 0 (en curso) · Última actualización: 2026-10-23

## Decisiones tomadas
- 2026-10-23 · Raíz canónica `D:\Ecoudea-master` con git restaurado desde `origin/master` (`6c6c598`) · el contenido `src/`+`public/` era byte-idéntico al clon · cómo revertir: `git checkout v1-legacy`
- 2026-10-23 · Tag `v1-legacy` + rama `legacy` como red de seguridad · revertir: `git tag -d v1-legacy`
- 2026-10-23 · **Cambio de alcance**: se conservan los 10 cursos + se rescatan las 20 clases huérfanas (nuevo curso `estadistica-y-probabilidades`) en lugar de archivar a solo Estadística II · motivo: el pedido es una página final "igual de funcional que la original pero mucho mejor" · revertir: archivar según ORQUESTADOR Fase 2
- 2026-10-23 · `BASE_PATH`/`SITE_URL` por entorno + helper `src/lib/url.ts` · default `/Ecoudea` · revertir: hardcode en `astro.config.mjs`
- 2026-10-23 · `/admin` se conserva (es funcionalidad existente) pero se documenta su debilidad (hash client-side, password por defecto) · revertir: eliminar según plan original

## Hecho
- Fase 0 (parcial): ✅ git restaurado, ✅ `v1-legacy`, ✅ `url()` + env, ✅ AGENTS.md/CLAUDE.md corregidos · pendiente: baseline Lighthouse, inventario formal, commit

## Deuda pendiente
- 52 usos literales de `${base}` → migrar a `url()` (cierre Fase 8 con grep)
- `bibliography: referencias.bib` inexistente en 147 clases (decidir: eliminar campo en Fase 2)
- `pagefind` y `space-grotesk` instalados sin uso (Fase 5 / Fase 1)
- `Accordion`, `BackToTop` sin importar; `VideoPlayer` sin contenido que lo use
- Filtro de categoría del navbar roto (query tras el `#`) → Fase 4
- `setInterval` 3 s en `[course].astro` → Fase 6
- Listado de curso con doble render → Fase 6
- Sin `prefers-reduced-motion`, sin tema claro, sin `aria-current` → Fase 1/4

## Inventario de código muerto (Fase 0)
| Ítem | Evidencia | Decisión | Fase |
|---|---|---|---|
| `tags` + `/tags/[tag]` | 0 clases con `tags` | Mantener ruta, alimentar con `conceptos` o eliminar | 2 |
| `video*` + `VideoPlayer` | 0 clases con `video` | Reemplazar por `<Video>` con fachada (Fase 7) | 7 |
| `unlockMode: sequential` + `unlock.js` | 0 cursos lo usan | Eliminar bloqueo, conservar progreso como "completado" | 6 |
| `bibliography` | `referencias.bib` no existe, ningún `.astro` lo lee | Eliminar campo + sección `lecturas` en frontmatter nuevo | 2 |
| `Accordion` | sin imports | Reusar como base de `<details>` en unidades | 6 |
| `BackToTop` | sin imports (duplica FloatingButtons) | Fusionar en controles flotantes ≥44px | 4 |
| `Space Grotesk` | 0 usos | Retirar de deps | 1 |
| `pagefind` | 0 usos | Activar búsqueda real | 5 |
| campo `color` de curso | sin uso | Reemplazar por `area` + color por área | 1-2 |
| `/admin` | auth client-side débil | Conservar UI, documentar; gestión real por git+PR | 2 |

## Métricas
| Página | Perf | A11y | LCP | CLS | JS (KB) |
|---|---|---|---|---|---|
| home (baseline) | — | — | — | — | — |
| curso (baseline) | — | — | — | — | — |
| clase (baseline) | — | — | — | — | — |

## Siguiente paso
- Terminar `npm install`, correr `npm run build`, guardar baseline (peso, requests, páginas), commit Fase 0
