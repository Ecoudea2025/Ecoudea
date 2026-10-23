# Archive — cursos heredados (Fase 2.a)

Este directorio conserva los cursos retirados del sitio. **Nada se borró**: todo está
también en el historial git (tag `v1-legacy` = sitio original completo) y en las copias
de `D:\Proyectos_web\`.

## Contenido

- `courses/`: 9 archivos de curso retirados (frontmatter original intacto).
- `classes/`: 123 clases retiradas (cuerpo Markdown intacto, sin reescribir).
- `manifest.json`: inventario con ids y títulos; lo leen `cursos/[course].astro` y
  `cursos/[course]/[class].astro` para mostrar el aviso "curso archivado" en URLs viejas.

## Curso activo

Solo `estadistica-ii` (Estadística II, UdeA, 24 clases) permanece en `src/content/`,
con atribución visible al profesor Jorge Iván Pérez.

## Restaurar un curso

```bash
git mv archive/courses/<id>.md src/content/courses/<id>.md
# y sus clases: ver manifest.json → classes[] con course == <id>
git mv archive/classes/<prefijo>-*.md src/content/classes/
npm run build
```

## Imágenes

Las 349 imágenes siguen en `public/assets/images/` (compartidas entre cursos;
moverlas rompería referencias). No se tocó ninguna.
