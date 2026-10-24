# Guía de autoría — cómo subir cursos propios

> Requisito: Node ≥22, Python 3.12 con `matplotlib`, git. Comandos desde la raíz del repo.

## 1. Crear un curso

```bash
npm run new:course -- microeconomia-i --title "Microeconomía I" --description "Preferencias, utilidad y demanda" --category "Cursos"
```

Esto crea `src/content/courses/microeconomia-i.md`. Edita el frontmatter:

```yaml
title: "Microeconomía I"
description: "…"
category: "Cursos"            # Cursos | Guías y Semilleros | Sesiones Especiales
order: 12                     # posición en el directorio
image: "/assets/images/mi-portada.jpg"   # opcional
```

## 2. Crear clases

```bash
npm run new:lesson -- microeconomia-i unidad-1-preferencias --title "Preferencias y utilidad" --type clase
```

Crea `src/content/classes/microeconomia-i-unidad-1-preferencias.md` con plantilla comentada. Frontmatter:

```yaml
title: "Preferencias y utilidad"
course: "microeconomia-i"     # = nombre del archivo del curso
order: 1                      # orden dentro del curso
classType: "clase"            # clase | practica | guia | resumen
description: "Resumen (aparece en listados y SEO)"
math: true                    # true si hay LaTeX
unit: "Unidad 1"              # opcional: agrupa el listado del curso
conceptos: ["A", "B"]         # opcional: alimenta el glosario
draft: true                   # opcional: borrador, no se publica
```

## 3. Escribir contenido

- Títulos `##` / `###` generan el índice (TOC) automáticamente, en escritorio y móvil.
- Fórmulas: `$x^2$` inline, `$$…$$` display. **Macros globales** (valen en clases y en `/tablero-latex`): `\E \Var \Cov \Corr \Prob \R \N \Z \iid \dd \argmax \argmin \given \xb`. Definidas en `src/lib/katex-macros.mjs`.
- Bloques didácticos: `:::definicion Título` … `:::` (tipos: definicion, teorema, lema, proposicion, demostracion, ejemplo, ejercicio, ideaclave, nota, advertencia, intuicion). Numerados y accesibles sin JS. Colapsables con `<details>` nativo.
- Ecuaciones referenciables: `$$ … \tag{id} $$` + `$\ref{id}$` en cualquier clase → enlace automático. Un `\ref` a etiqueta inexistente **rompe el build**.
- Glosario: `<Term id="elasticidad">elasticidad</Term>` en el texto + `conceptos: ["A", "B"]` en el frontmatter. El prebuild genera `/glosario` solo con contenido publicado.
- Borradores: `draft: true` excluye la clase de la página, listados, sitemap y búsqueda.
- Figuras: genera el SVG (`npm run figures -- <id>`) e insértala con `<Figure id="…" caption="…" alt="…" />`. El `alt` es obligatorio (el build falla sin él).
- Videos: sube el Manim a YouTube y usa `<Video youtubeId="…" title="…" />` (carga al clic, con enlace a transcripción).
- Antes de publicar: `npm run content:fix && npm run build`.

## 4. Checklist de publicación por clase

- [ ] `order` único y secuencial dentro del curso
- [ ] `description` escrita (no vacía)
- [ ] Toda `<Figure>` con `alt` descriptivo
- [ ] Todo `<Video>` con transcripción o resumen equivalente en el texto
- [ ] Fórmulas revisadas en 360px (sin scroll horizontal de página) y en ambos temas
- [ ] Imágenes en `public/assets/images/` referenciadas por nombre exacto
- [ ] Build verde (`npm run build`)

## 4.bis Progreso del estudiante

Cada clase tiene un botón ✓ que guarda el avance en el navegador
(`localStorage`). En la página del curso se ve el X/N por unidad, y los botones
**Exportar/Importar** permiten llevar el progreso a otro dispositivo en JSON.

## 5. Publicar

```bash
git add src/content/courses/<curso>.md src/content/classes/<curso>-*.md
git commit -m "feat(<curso>): add <tema>"
git push origin master   # deploy automático a GitHub Pages (~2 min)
```

## 6. Figuras (pipeline)

1. Copia `figures/oferta_demanda.py` como base; usa `figures/style.py` (`setup`, `save`, `PALETTE`).
2. Registra la figura en `figures/manifest.json` (id, script, fecha).
3. `npm run figures -- <id>` genera `<id>-light.svg` y `<id>-dark.svg` en `src/assets/figures/`.
4. El CI valida que cada `<Figure id>` tenga su SVG y su `alt`.

## 7. Convenciones

- **Una clase = un archivo.** Commits atómicos con Conventional Commits (`feat:`, `fix:`, …).
- Nunca edites `public/assets/` a ciegas: las imágenes se referencian por nombre desde el Markdown.
- Prohibido: hardcodear el base path (usa el helper `src/lib/url.ts`), añadir dependencias sin justificar peso, animar sin respetar `prefers-reduced-motion`.
