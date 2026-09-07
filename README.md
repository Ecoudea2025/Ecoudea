# Ecoudea

Plataforma de cursos de estadística, probabilidad y programación.

> ⚠️ **Aviso de atribución**: Este proyecto es un **remake moderno** de la página web del profesor **Jorge Iván Pérez** (Estadístico y Economista, Universidad de Antioquia). El contenido académico (cursos, clases, prácticas, guías y materiales) **no es de nuestra autoría** y pertenece al profesor Jorge. Este sitio fue reconstruido con una nueva tecnología (Astro + Tailwind CSS) como proyecto de aprendizaje y referencia. Para el contenido original, visita la página del profesor.

## 🚀 Tecnología

- [Astro](https://astro.build) — Framework estático (v7, con prefetch)
- [Tailwind CSS v4](https://tailwindcss.com) — Estilos
- [KaTeX](https://katex.org) — Fórmulas matemáticas renderizadas en el build (LaTeX, CSS self-hosted, sin JS en cliente)
- [GitHub Actions](https://github.com/features/actions) — Deploy automático a GitHub Pages

## 📁 Estructura

```text
/
├── public/
│   └── assets/          # Imágenes, videos, CSS, JS (KaTeX, animations, unlock)
├── scripts/             # Scripts de build y utilidades (gzip.mjs)
├── tools/               # Herramientas locales (optimize-images.ps1, optimize-videos.ps1)
├── src/
│   ├── content/
│   │   ├── courses/     # Metadatos de cada curso (frontmatter)
│   │   └── classes/     # Contenido de las clases (Markdown)
│   ├── components/      # Componentes Astro (Navbar, Footer, VideoPlayer, ...)
│   ├── layouts/         # BaseLayout (SEO, KaTeX condicional, unlock)
│   ├── pages/           # Páginas generadas (index, cursos, admin, ...)
│   └── styles/          # CSS global
└── package.json
```

## ✨ Funcionalidades

- 🎓 **10 cursos** con 147 clases migradas del contenido original
- 📐 **LaTeX renderizado** con KaTeX (fórmulas inline y display)
- 📑 **Tabla de contenidos** lateral en cada clase
- 🔍 **Vista lista/cuadrícula** para navegar las clases de un curso
- ⚙️ **Ajustes de lectura** (tamaño de fuente, tipografía, interlineado)
- 📱 **Diseño responsive** (mobile-first)
- ✅ **Progreso de estudio** guardado en el navegador (localStorage)
- 🎬 **Videos en clases**: reproductor propio (HTML5) con poster, lazy-load, subtítulos y fallback a YouTube/Vimeo
- 🔒 **Desbloqueo progresivo** configurable por curso (abierto o secuencial)
- 🛠 **Panel de administración** en `/admin` (configuración de cursos + resumen de clases)
- 🗺 **SEO**: sitemap.xml, robots.txt, JSON-LD (schema Course), Open Graph
- ⚡ **Rendimiento**: prefetch, KaTeX renderizado en build con CSS condicional, gzip precompresión, lazy images

## 🎬 Agregar un video a una clase

Edita el frontmatter del archivo de la clase en `src/content/classes/`:

```yaml
---
video: "/assets/videos/estadistica-i/clase-03.mp4"   # video local (máx. ~100MB en GitHub Pages)
videoPoster: "/assets/images/poster-clase-03.jpg"    # opcional: imagen de portada
videoFallback: "https://youtu.be/xxxxx"              # opcional: YouTube/Vimeo si no hay local
videoCaptions: "/assets/videos/clase-03.es.vtt"      # opcional: subtítulos
---
```

Optimiza los videos antes de subirlos:

```powershell
.\tools\optimize-videos.ps1 -Source "D:\videos-curso" -Out "D:\videos-web" -MaxWidth 1280 -Crf 28
```

Genera H.264 MP4 con `+faststart` (buscar posición de video funciona en GitHub Pages) y opcionalmente WebM VP9 con `-Webm`.

## 🔒 Desbloqueo progresivo

Cada curso declara en su frontmatter (`src/content/courses/<id>.md`):

```yaml
unlockMode: "open"          # por defecto: todo accesible
unlockMode: "sequential"    # clase N exige completar la clase N-1
```

- El progreso se guarda por navegador (localStorage `ecoudea-progress-<curso>`).
- En `sequential`, las clases bloqueadas muestran candado y no navegan; el acceso directo por URL muestra una pantalla de bloqueo.
- **Desbloqueo total (admin)**: abre la consola del navegador y ejecuta `localStorage.setItem('ecoudea-unlock-all', '1')`, o usa el botón del curso en el panel `/admin`.

## 🛠 Panel de administración

- Ruta: `/admin` (login con contraseña; sesión por pestaña).
- Contraseña por defecto: `ecoudea-admin` — **cámbiala** definiendo el secret `ADMIN_PASSWORD` en GitHub Actions (Settings → Secrets and variables → Actions) y usándolo en el workflow como `env: ADMIN_PASSWORD`.
- Permite: editar la configuración de cada curso (título, descripción, categoría, orden, imagen, modo de desbloqueo), generar el frontmatter YAML listo para pegar/descargar, y consultar el resumen de clases (tipo, título, math, video).
- El panel es `noindex` y se excluye del sitemap.

## 🧞 Comandos

| Comando           | Acción                                      |
| :---------------- | :------------------------------------------ |
| `npm install`     | Instala dependencias                        |
| `npm run dev`     | Servidor local en `localhost:4321`          |
| `npm run build`   | Build de producción a `./dist/` + gzip      |
| `npm run preview` | Previsualiza el build localmente            |

## 📝 Licencia

El código de este proyecto es de uso libre para fines educativos. El contenido académico pertenece a su autor original (Prof. Jorge Iván Pérez).
