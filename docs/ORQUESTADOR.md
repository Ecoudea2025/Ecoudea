# Orquestador Ecoudea → Plataforma de estudio de economía

Cómo usar este archivo:

1. Este archivo + `docs/ESTADO.md` son la fuente de verdad del plan. Una sesión nueva de Claude Code **por fase**: pegar primero el Prompt maestro (§1) y luego el Prompt de la fase.
2. No avanzar de fase hasta cumplir los criterios de aceptación y exista el tag de cierre (`fase-N-cerrada`).
3. Si una fase toca más de ~15 archivos, partirla en sub-fases (N.a, N.b…) y anotar pendientes en ESTADO.md.

## 0. Decisiones previas (valores por defecto)

| Decisión | Valor por defecto |
|---|---|
| Raíz canónica del repo | `D:\Ecoudea-master` (git restaurado de `origin/master`, tag `v1-legacy`) |
| Alcance de contenido | **Se conservan todos los cursos** (decisión 2026-10-23: página final igual de funcional que la original). Las 20 clases huérfanas de `estadistica-y-probabilidades` se rescatan con su propio archivo de curso |
| Curso nuevo piloto | Microeconomía I – Unidad 1 (placeholder real, 4-5 clases, Fase 9) |
| Formato de contenido | MDX en Astro Content Collections con schema Zod estricto (Fase 2) |
| Matemáticas | `remark-math` + `rehype-katex` en build (cero JS de KaTeX en cliente) |
| Gráficos estáticos | Matplotlib → SVG, scripts en `/figures` |
| Animaciones | Manim → YouTube con fachada (sin iframe hasta el clic) |
| Interactivos | Islas Astro `client:visible`, SVG nativo, sin frameworks pesados |
| Tema | Claro + oscuro, default `prefers-color-scheme`, selector manual persistido |
| Idioma | Español (`lang="es"`), preparado para i18n sin implementarlo |
| Dominio / base | `SITE_URL` y `BASE_PATH` por entorno; hoy `/Ecoudea` en GitHub Pages |
| `/admin` | Se conserva la UI; la gestión real es git + PRs (el hash client-side no es seguridad real) |
| `/tablero-latex` | Se conserva y comparte macros con el contenido (Fase 3); responsive en Fase 4 |

Atribución: el material heredado es del profesor Jorge Iván Pérez. Crédito visible en cada curso heredado y en `/acercade`. Si el repo es público, confirmar licencia con él.

### 0.2 Hechos verificados del repo (ground truth 2026-10-23)

- Git restaurado en `D:\Ecoudea-master` desde `origin/master` (`6c6c598`); `src/`+`public/` eran byte-idénticos al clon.
- Contenido: 147 clases · 11 ids de curso · 10 archivos de curso → `estadistica-y-probabilidades` (20 clases) huérfano. Tipos: 107 clase, 26 practica, 7 presentacion, 7 guia.
- Metadatos muertos: `bibliography` → `referencias.bib` inexistente (147 clases); `tags` 0; `video*` 0; `sequential` 0; `color` sin uso.
- 52 usos literales de `${base}`; helper `src/lib/url.ts` creado en Fase 0.
- 349 imágenes en `public/assets/images/`; `logo-ecoudea.png` 1,1 MB.
- Deps sin uso: `pagefind@1.5.2`, `@fontsource-variable/space-grotesk`. Componentes sin importar: `Accordion`, `BackToTop`.
- Grafo cbm: proyecto `D-Ecoudea-master`; el índice viejo solo describía secciones Markdown, no UI.

## 1. PROMPT MAESTRO (pegar al inicio de CADA sesión)

```text
Eres el arquitecto principal y desarrollador senior de Ecoudea, plataforma de estudio de
economía (base matemática y estadística) en GitHub Pages con Astro. Estética: editorial
académico moderno, no "dashboard tech".

OBJETIVO GLOBAL
Convertir el sitio actual en una plataforma editorial de estudio: LaTeX impecable, cursos
propios, gráficos y animaciones por concepto, excelente móvil, WCAG 2.2 AA, transiciones
suaves y rendimiento casi perfecto en hosting estático. Sin perder funcionalidad existente.

ESTADO REAL
Lee docs/ORQUESTADOR.md §0.2 y docs/ESTADO.md. Re-verifica con comandos; si el disco
contradice el doc, gana el disco y lo anotas.

CÓMO TRABAJAS
1. Trabaja SOLO en la fase indicada. No adelantes fases ni refactorices fuera de alcance.
2. Antes de codificar: inspecciona el repo real y entrega un plan breve con archivos a tocar.
   Ejecuta sin pedir confirmación, salvo decisión irreversible (borrar, licencia, publicar).
3. Si tocas >~15 archivos, divide en sub-fases (N.a, N.b…).
4. Nunca borres contenido de cursos: muévelo a /archive o a un tag. Todo borrado de código
   muerto va justificado en el commit.
5. Commits atómicos con Conventional Commits. Tag `fase-N-cerrada` al cerrar.
6. Verifica de verdad: build, astro check, pruebas de la fase. Sin evidencia no hay "listo".
   Cero placeholders, cero APIs inventadas.
7. Restricciones permanentes: estático (sin SSR); cero hardcode de base (helper url());
   JS mínimo (HTML+CSS primero, islas client:visible/idle); todo movimiento tras
   prefers-reduced-motion; tokens CSS, no valores sueltos; teclado + lector + táctil ≥44px;
   legible con JS desactivado; sin deps nuevas sin justificar peso y alternativa nativa.
8. La calidad matemática es prioridad #1: nada degrada el LaTeX; todo legible en móvil.
9. Cierre: actualiza ESTADO.md, lista criterios ✅/❌ con evidencia, propone arranque de la
   fase siguiente si hay ajustes.

FORMATO: plan breve → ejecución → informe de cierre. Directo, una frase de justificación
por decisión de diseño.
```

## 2. Contexto técnico

- Astro 7, Tailwind 4 (@theme inline), KaTeX en build, Shiki one-dark-pro, sitemap, deploy en push a `master`. Base `/Ecoudea`.
- Rutas: `/`, `/cursos/[course]`, `/cursos/[course]/[class]`, `/acercade`, `/tablero-latex`, `/tags/[tag]` (muerta), `/admin*`, `/404`.
- UI: Navbar, Footer, CourseCard, FloatingButtons (ajustes de lectura), Accordion*, BackToTop*, VideoPlayer* (* = sin importar).
- Estilos: `src/styles/global.css` (542 líneas), solo oscuro, acento `#6c9a06` + teal `#0e7774`, Fraunces en h1-h5.
- JS: `animations.js` (scroll-progress, reveal, contadores, typewriter, tilt, parallax), `enhance.js` (TOC+scrollspy, Show-Hide), `unlock.js`. Cero `prefers-reduced-motion`.

Problemas a resolver: monotonía (un acento, tarjeta `gradient-bg+rounded-2xl+border` ×11, hero≈CTA, todo centrado); sin modo claro/reduced-motion/aria-current; flotantes 40px; typewriter vacía el hero; contadores SSR en 0; sin TOC móvil; menú sin focus-trap/Esc; filtro navbar roto (query tras `#`); Pagefind sin usar; doble render lista+grid; `setInterval` 3 s; 349 imgs sin optimizar; base ×52; CLAUDE/AGENTS con rutas viejas (corregido Fase 0). Conservar: Ajustes de lectura, tablero-latex, KaTeX en build, JS nativo ligero.

## 3. Mapa de fases

| Fase | Nombre | Resultado clave |
|---|---|---|
| 0 | Línea base y red de seguridad | Git + tag, baseline, docs, `url()` |
| 1 | Fundaciones de diseño | Tokens, claro/oscuro, reduced-motion, primitivos, styleguide |
| 2 | Contenido y scaffold | Schema, curso huérfano rescatado, `new:course`/`new:lesson` |
| 3 | Lectura matemática | Macros, refs, móvil, bloques teóricos, glosario |
| 4 | Shell y móvil | Navbar a11y, TOC móvil, View Transitions, tablero responsive |
| 5 | Home con identidad | Hero asimétrico, stats SSR, áreas, Pagefind |
| 6 | Curso y clase | Render único, progreso real, unidades, JSON-LD |
| 7 | Gráficos y media | SVG, `<Figure>`, `<Video>`, islas |
| 8 | Perf, a11y, SEO, CI | Assets, presupuestos, Actions |
| 9 | Piloto y autoría | Curso real + `AUTORIA.md` |

## FASE 0 — Línea base y red de seguridad

Tareas: git restaurado ✅; rama `legacy` + tag `v1-legacy` ✅; baseline Lighthouse (home, curso, clase con LaTeX) + peso/requests/CLS/LCP/INP en `docs/baseline/`; CLAUDE/AGENTS corregidos ✅; `SITE_URL`/`BASE_PATH` + `url()` ✅ (migrar los 52 usos al tocar cada archivo); ESTADO.md ✅; inventario de código muerto ✅.
Aceptación: `git status` limpio sobre `master`; tag existe y compila; baseline guardado; build verde; docs reales; ESTADO inicializado.

## FASE 1 — Fundaciones de diseño

Dirección: editorial/académico; color en 3 capas (primitivos→semánticos→componentes); claro (papel cálido) + oscuro (tinta) AA; acento por área de economía (Micro, Macro, Econometría, Estadística/Probabilidad, Matemáticas, Historia) con color+icono+etiqueta; display serif títulos, serif lectura en cuerpo, mono código; escala `clamp()`; motivo curvas/ejes en SVG sutil; tokens de espacio/radio/sombra/movimiento.
Tareas: `src/styles/tokens.css` + `[data-theme]` + anti-FOUC + selector claro/oscuro/sistema; `prefers-reduced-motion` global (apagar tilt/parallax/typewriter/órbitas); primitivos `Section, SectionHeader, Card, Badge, Stat, Button, Prose, Breadcrumbs, Icon`; retirar Space Grotesk; `/_styleguide` (noindex).
Aceptación: tema persiste sin parpadeo; AA ambos temas; cero animación con reduced-motion; styleguide completo; foco visible siempre.

## FASE 2 — Contenido y scaffold

Tareas: schema Zod (estricto para lo nuevo, compatible con lo heredado); rescatar huérfanas creando `estadistica-y-probabilidades.md`; scripts `new:course`/`new:lesson`; decidir `bibliography` (eliminar campo, 147 archivos vía script); documentar `/admin`; redirecciones si se archiva algo; validación por conteos.
Aceptación: build verde con 11 cursos; frontmatter inválido (nuevo) falla con error legible; scaffolds generan contenido que compila; nada borrado sin tag; informe de migración.

## FASE 3 — Lectura matemática

Tareas: macros globales en un archivo compartido con tablero (`\E \Var \R \argmax \dd`…); `aligned/cases/matrices/\tag`; ecuaciones numeradas con resolución propia (`ecuaciones.json` en build + plugin rehype para `\ref`, falla si el label no existe — KaTeX no lo hace nativo); `.katex-display` con scroll accesible (`tabindex=0 role=region`) sin scroll de página en 360px; MathML visible a lectores; copiar-LaTeX progresivo; bloques `<Definicion> <Teorema> <Lema> <Proposicion> <Demostracion>(details) <Ejemplo> <Ejercicio> <IdeaClave> <Nota> <Advertencia> <Intuicion>`; footnotes + lecturas; glosario `<Term>` + `/glosario`; prosa 60-75ch; integrar Ajustes de lectura; clase de tortura `prueba-latex.mdx` (noindex).
Aceptación: tortura OK en 360/768/desktop × claro/oscuro; `\ref` entre clases funciona y el inválido rompe el build; MathML leído; bloques sin JS y con teclado; KaTeX sin JS cliente; tablero con mismas macros.

## FASE 4 — Shell, navegación, móvil y transiciones

Tareas: navbar con `aria-current`, dropdown con `<button aria-expanded>`, filtro por ruta `/cursos?area=…` (bug query-tras-# corregido); menú móvil con focus-trap/Esc/retorno-foco/`inert`; flotantes ≥44px fusionando BackToTop; TOC móvil (`<details>` sticky) + progreso de lectura; tablero apilado en móvil sin resizer; safe-areas; View Transitions (`<ClientRouter/>`) con transiciones nombradas, off con reduced-motion; scripts en `astro:page-load`/`astro:after-swap`; skip-link/landmarks/anuncio de página.
Aceptación: teclado completo; 360px sin solapamientos; transiciones OK y ausentes con reduced-motion; 10 navegaciones sin leaks; a11y ≥95.

## FASE 5 — Home con identidad

Tareas: hero asimétrico (texto + SVG oferta/demanda que se dibuja; estático con reduced-motion; párrafo completo en HTML); stats SSR reales; mapa de áreas; "continúa donde lo dejaste"; directorio con filtros (área/nivel/estado) y currículo con prerequisitos; Pagefind real (peso a títulos+`conceptos`, UI con `/` o `Ctrl+K`, verificado con BASE_PATH); CTA final distinto del hero; romper el patrón tarjeta-gradiente.
Aceptación: home completa sin JS; búsqueda dentro de clases con teclado/móvil/base; hero≠CTA; LCP ≤2,5 s, CLS <0,05; vacíos diseñados.

## FASE 6 — Curso y clase

Tareas: **un solo render** (vista por CSS `data-view`); cabecera con autor/nivel/prerequisitos/objetivos/tiempo + progreso X/N (`localStorage`, export/import JSON); unidades (`<details>`) con progreso; clase con objetivos/tiempo/progreso/TOC/"Qué sigue"/recursos/"completada" accesible; modo estudio opcional; eliminar `setInterval`, locks y `VideoPlayer` huérfano; JSON-LD `Course`/`LearningResource`/`BreadcrumbList`.
Aceptación: markup único; progreso sobrevive a navegación+recarga; cero intervalos/huérfanos/campos sin uso; schema válido.

## FASE 7 — Gráficos y media

Matplotlib→SVG: `figures/` + `style.py` + `requirements.txt`; salida `src/assets/figures/<curso>/<id>.svg` claro/oscuro; `npm run figures`; `manifest.json`; CI valida existencia. Plantillas: oferta/demanda, elasticidades, ppto/indiferencia, isocuantas, CMg/CMe, competencia/monopolio, IS-LM, OA-DA, Phillips, Lorenz, series, distribuciones, regresión. `<Figure>` (alt obligatorio —rompe build—, número, fuente, descarga, `<figcaption>`, desc. larga) + `<FigRef>`.
Manim→YouTube: `animations/manifest.json`; `<Video>` con fachada (`youtube-nocookie`, clic→iframe, sin CLS, transcripción obligatoria).
Interactivos: `<Interactive>` (`client:visible`, fallback estático, teclado, ARIA, reduced-motion); 2 laboratorios (oferta/demanda; región de rechazo).
Aceptación: figures determinista; tema OK; video sin carga previa ni CLS; <30 KB JS c/u; flujo en AUTORIA.md.

## FASE 8 — Rendimiento, a11y, SEO y CI

Tareas: `astro:assets` (WebP/AVIF, srcset, w/h, lazy); logo SVG; JS <60 KB/página; cerrar grep `${base}`→`url()` (cero); a11y completa (AA×2 temas, zoom 200/400, foco, contrast/forzado, alts); SEO (sitemap, robots, canonical, OG por curso, JSON-LD, RSS); Actions por PR (build, check, enlaces, Lighthouse CI ≥90/95/95/95, axe, validación Figure); política videos-fuera-del-repo.
Aceptación: métricas en 3 páginas; LCP/CLS/INP; CI falla con caso malo (demostrado en rama); grep cero; `comparativa.md`.

## FASE 9 — Piloto y autoría

Tareas: Microeconomía I U1 (4-5 clases, todo el sistema); `docs/AUTORIA.md` (curso/unidad/clase, LaTeX+macros, figura, animación, publicar, checklist); checklist por clase; backlog (i18n, comentarios, PWA, PDF, quizzes).
Aceptación: piloto pasa CI; un tercero crea una clase solo con la guía; móvil real ×2 temas; ESTADO cerrado.

## Anexo A — rescate y revisión

Rescate (sesión perdida): "Detente. Lee ORQUESTADOR y ESTADO. Resume en 5 líneas fase/hecho/falta/❌. Revisa `git status` y `git log -10`. No codifiques hasta confirmar; sigue solo con lo que falta."
Revisión adversarial (cierre, sesión nueva): "Revisor externo de la fase N. No confíes en ESTADO: ejecuta build/pruebas/auditorías. Busca LaTeX roto, foco perdido, JS duplicado, base hardcodeado, imgs sin dimensiones, animación con reduced-motion, contenido huérfano. Reporta bloqueantes/importantes/menores con evidencia. No arregles nada."
