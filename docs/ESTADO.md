# Estado del proyecto
Fase actual: logo animado sin loop + curso Macroeconomía I publicado → manda más MDs · Última actualización: 2026-10-23

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
- Logo animado sin loop (2026-10-23, con el autor): GIF 183 KB → MP4 51 KB; se reproduce UNA vez al hover y al terminar vuelve al SVG (nunca loop, nunca negro); `preload=none`, `reduced-motion` respetado. Bloque de video en Navbar del autor, corregido: `webm` inexistente → mp4, fuera `loop`, handlers al contenedor, `object-contain` (16:9 en slot cuadrado).
- Curso Macroeconomía I (2026-10-23, sin tag de fase): 16 clases + 1 práctica convertidas desde `Clases macro/` (frontmatter real, sin bibliography, `\tag` renumerados C.N únicos, 1 ref manual ascendida a `$\ref$`, placeholder propio eliminado). Calidad: `check-math` nuevo en CI (cero fórmulas rotas, antes 14), entidades HTML decodificadas en `sanitizeTex`, typo `\\end` corregido. Hallazgo operativo: `node_modules/.astro/data-store.json` cachea renders por digest del .md — tras cambiar plugins/config hay que borrarlo (los builds parecían "verdes" con contenido rancio).
- Fix hero + piloto macro (2026-10-23, sin tag de fase): hero SVG rehecho (rectas de manual, excedentes sombreados, E exacto con halo, ejes con flechas, PE/QE, animación por `pathLength`); piloto renombrado a `macroeconomia-i` (curso + 2 clases con `git mv`, lección reescrita a PIB/demanda agregada con `\tag{pib}`+ref+glosario); docs actualizadas. `figures/` conserva namespace `microeconomia/` (temáticamente correcto: oferta/demanda es micro).
- Fase 8.b (imágenes + presupuestos): ✅ commit + tag `fase-8b-cerrada`. 252 imágenes muertas a `archive/` (29,4 MB), JPG activos optimizados (32,5→13,3 MB), favicon.ico archivado, robots por endpoint, `dist/` 95,6→25,7 MB (−73%), `comparativa.md`. Todo validado con check-links + decodificación real en navegador.
- Fase 8.a (base + SEO + CI): ✅ commit + tag `fase-8a-cerrada`. Cero `${base}` literales (helper `url()` en 14 archivos; `Card.baseCls` renombrado para grep limpio), `robots.txt` por endpoint, `check-links` + `check-seo` en verde, workflow `ci.yml` (build + figures + grep + checks). RSS pospuesto con motivo: sin fechas en el contenido.
- Fase 6 (curso/clase): ✅ commit + tag `fase-6-cerrada`. Listado con render único (vista por CSS `data-view`, sin duplicar markup), unidades por `<details>` con progreso, progreso real X/N hidratado + exportar/importar JSON, `Breadcrumbs` con `BreadcrumbList`, JSON-LD `LearningResource`, chips de conceptos → glosario. Eliminados: `setInterval` 3s, locks/`unlock.js`, `VideoPlayer`, campos `unlockMode`/`video*`, `typeBg` muerto.
- Fase 3.c (glosario): ✅ commit + tag `fase-3c-cerrada`. Campo `conceptos`, prebuild recolecta `<Term id>` + `conceptos` → `glosario.json` (solo publicado), página `/glosario` alfabética con letras y backlinks (en sitemap), `<Term>` enlazado por `enhance.js` (sin JS se lee igual por CSS), enlace en footer, seed real (3 términos), AUTORIA documentada.
- Fase 3.b (ecuaciones referenciables): ✅ commit + tag `fase-3b-cerrada`. Prebuild `gen-indices.cjs` (`\tag` → `ecuaciones.json`, falla en duplicados e ignora comentarios/drafts) + plugin `remarkEqrefs` (`$\ref{id}$` → enlace, ancla `eq-*` con `scroll-margin`) + validación de refs en prebuild (`exit 1` legible). Clase de ejemplo con `\tag{utilidad}` + ref reales. Hallazgo: Astro 7 tolera errores de render generando el artículo vacío → la garantía va en prebuild, no en el plugin.
- Fase 3.a (bloques + borradores): ✅ commit + tag `fase-3a-cerrada`. Plugin `remarkBlocks` (`:::tipo` numerado, `role=note`, compacto o con blancos), CSS por tipo en ambos temas, `draft:true` (página+listados+sitemap+búsqueda excluidos), clase de tortura verificada (10 bloques, matrices, `aligned`/`cases`/`tag`, tabla, `<details>`, footnotes; 0 desbordes en 360px) y devuelta a draft. Hallazgo mayor: Astro 7 ignora `markdown.remarkPlugins` legacy en contenido → migrado a `markdown.processor: unified({...})` (adiós warning deprecado).
- Fase 5.b (Pagefind): ✅ commit + tag `fase-5b-cerrada`. `SearchModal` (atajos `/`/`Ctrl+K`/`Esc`, lazy-load del índice, extractos con highlight, URLs con BASE_PATH, archivados excluidos, `data-pagefind-body` en `<main>`), botón en navbar desktop+móvil (IDs únicos), `pagefind` integrado al `build`. Bug real encontrado por test: filtro `estadistica-i` ⊂ `estadistica-ii` comía resultados → corregido por segmento.
- Fase 1.b (identidad): ✅ commit + tag `fase-1b-cerrada`. Logo SVG moderno (curvas O/D + punto de equilibrio, sin animación orbital; ~100 líneas CSS eliminadas), favicon a juego, paleta avivada (lima #65a30d/#84cc16 + primario #3f6212, btn/gradientes por vars), copy de economía (hero, título, meta, footer, acercade, defaults), stats en 0 ocultos, figura regenerada con la paleta.
- Fase 2.a (archivado): ✅ commit + tag `fase-2a-cerrada`. 123 clases + 10 cursos a `archive/` con `git mv` (historial intacto) + `manifest.json`; activas: estadistica-ii (24) + macroeconomia-i de ejemplo vía scaffold; `/admin` eliminado; stubs "archivado" (noindex) en las 133 URLs viejas; sitemap limpio (25+2+home+acerca+tablero); atribución `author` visible; píldoras en 0 ocultas.
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


