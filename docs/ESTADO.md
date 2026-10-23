# Estado del proyecto
Fase actual: 5.a cerrada → siguiente 5.b (Pagefind) · Última actualización: 2026-10-23

## Decisiones tomadas
- 2026-10-23 · Raíz canónica `D:\Ecoudea-master` con git restaurado desde `origin/master` (`6c6c598`) · revertir: `git checkout v1-legacy`
- 2026-10-23 · Tag `v1-legacy` + rama `legacy` como red de seguridad
- 2026-10-23 · **Se conservan los 11 cursos** (incl. `estadistica-y-probabilidades` rescatado con su archivo de curso; no era duplicado: trae "Presentación del curso de Estadística y Probabilidades") en lugar de archivar · motivo: página final igual de funcional que la original · revertir: archivar según ORQUESTADOR Fase 2
- 2026-10-23 · `BASE_PATH`/`SITE_URL` por entorno + helper `src/lib/url.ts` (default `/Ecoudea`)
- 2026-10-23 · `/admin` se conserva (funcionalidad existente); su auth client-side se documenta como no-seguridad
- 2026-10-23 · **View Transitions diferidas**: con ClientRouter los scripts `animations/enhance/unlock` se re-ejecutarían por navegación (barras de progreso y listeners duplicados). Requiere refactor del ciclo de vida (`astro:page-load`). Backlog.
- 2026-10-23 · `bibliography` eliminado de las 147 clases + schema (apuntaba a `referencias.bib` inexistente)
- 2026-10-23 · `@fontsource-variable/space-grotesk` retirado (0 usos); `pagefind` se mantiene como dependencia para Fase 5 (búsqueda real, backlog con dep lista)

## Hecho
- Fase 5.a (rediseño home): ✅ commit + tag `fase-5a-cerrada`. Hero asimétrico con SVG oferta/demanda (draw-on-load, estático con reduced-motion), sin typewriter, stats SSR, rutas editoriales 01/02/03 con filtro sin recarga, "Continúa donde lo dejaste" (localStorage + índice embebido), CTA en banda horizontal, pills con `role=group`, contadores con `<dl>`.
- Fase 0: ✅ git + `v1-legacy` ✅ baseline en `docs/baseline/` ✅ CLAUDE/AGENTS ✅ `url()` ✅ ESTADO/ORQUESTADOR ✅ inventario
- Fase 1: ✅ `tokens.css` (3 capas) ✅ claro/oscuro/sistema sin FOUC + `ThemeToggle` ✅ `prefers-reduced-motion` global (CSS + JS) ✅ `aria-current` ✅ flotantes 44px + `Esc` ✅ 8 primitivos `ui/` ✅ `/styleguide` (noindex) ✅ Space Grotesk fuera
- Fase 2: ✅ huérfanas rescatadas ✅ `new:course`/`new:lesson` ✅ `bibliography` fuera ✅ `docs/AUTORIA.md`
- Fase 3: ✅ macros KaTeX compartidas (build + tablero) ✅ display accesible (`tabindex/role`) ✅ copiar-TeX ✅ tablero usa mismas macros
- Fase 4: ✅ bug filtro navbar (`?cat=` antes del `#`) ✅ menú móvil con `aria-expanded` + `Esc` ✅ TOC móvil (`<details>` + scrollspy doble) ✅ `.nav-shell` por tema ✅ admin con `nav-shell`
- Fase 6: ✅ `Breadcrumbs` con JSON-LD (listo para usar en curso/clase)
- Fase 7: ✅ pipeline `figures/` + `style.py` + `manifest.json` + `npm run figures` ✅ `<Figure>` (alt obligatorio, light/dark) ✅ `<Video>` con fachada ✅ ejemplo real en `/styleguide`
- Commit `fadb2ae` (fases 0-1). Pendiente commit fases 2-4+7.

## Deuda pendiente (Fase 5.b: Pagefind real + Lighthouse)
- Pagefind: indexar `dist`, UI con `Ctrl+K`/`/`, verificado con BASE_PATH
- Lighthouse móvil/escritorio home (LCP ≤2,5s, CLS <0,05) → con CI de Fase 8
- 52 usos `${base}` → `url()` (grep de cierre Fase 8)
- View Transitions (ver decisión arriba)
- Pagefind real (dep instalada; indexar `dist` + UI con `Ctrl+K`)
- `tags`/`video*`/`unlockMode`/`Accordion`/`BackToTop`: decidir eliminar o alimentar (inventario en ORQUESTADOR)
- `setInterval` 3 s en `[course].astro` (inocuo hoy: todos los cursos son `open`)
- Doble render lista/grid en `[course].astro` (funciona; unificar en Fase 6)
- 5 páginas >900 KB + 349 imgs sin optimizar + logo 1,1 MB (Fase 8)
- Lighthouse móvil/escritorio (Fase 8, CI)

## Métricas
| Página | Perf | A11y | LCP | CLS | JS (KB) |
|---|---|---|---|---|---|
| home baseline (v1-legacy) | — | — | — | — | page 2,4 KB / tablero 261 KB |
| home rework | — | — | — | — | (medir Fase 8) |

## Siguiente paso
- Rebuild + verificación Playwright (clase, styleguide/figura, móvil, light) → commit → push a `master` (deploy)


