# Ecoudea

Plataforma de cursos de estadística, probabilidad y programación.

> ⚠️ **Aviso de atribución**: Este proyecto es un **remake moderno** de la página web del profesor **Jorge Iván Pérez** (Estadístico y Economista, Universidad de Antioquia). El contenido académico (cursos, clases, prácticas, guías y materiales) **no es de nuestra autoría** y pertenece al profesor Jorge. Este sitio fue reconstruido con una nueva tecnología (Astro + Tailwind CSS) como proyecto de aprendizaje y referencia. Para el contenido original, visita la página del profesor.

## 🚀 Tecnología

- [Astro](https://astro.build) — Framework estático
- [Tailwind CSS v4](https://tailwindcss.com) — Estilos
- [KaTeX](https://katex.org) — Renderizado de fórmulas matemáticas (LaTeX)
- [GitHub Actions](https://github.com/features/actions) — Deploy automático a GitHub Pages

## 📁 Estructura

```text
/
├── public/
│   └── assets/          # Imágenes, CSS, JS (KaTeX, fonts, etc.)
├── scripts/             # Scripts de migración y utilidades
├── src/
│   ├── content/
│   │   ├── courses/     # Metadatos de cada curso
│   │   └── classes/     # Contenido de las clases (Markdown)
│   ├── components/      # Componentes Astro
│   ├── layouts/         # Layouts (Base, páginas de curso/clase)
│   ├── pages/           # Páginas generadas
│   └── styles/          # CSS global
└── package.json
```

## ✨ Funcionalidades

- 🎓 **9 cursos** con 147 clases migradas del contenido original
- 📐 **LaTeX renderizado** con KaTeX (fórmulas inline y display)
- 📑 **Tabla de contenidos** lateral en cada clase
- 🔍 **Vista lista/cuadrícula** para navegar las clases de un curso
- ⚙️ **Ajustes de lectura** (tamaño de fuente, tipografía, interlineado)
- 📱 **Diseño responsive** (mobile-first)
- ✅ **Progreso de estudio** guardado en el navegador (localStorage)

## 🧞 Comandos

| Comando           | Acción                                      |
| :---------------- | :------------------------------------------ |
| `npm install`     | Instala dependencias                        |
| `npm run dev`     | Servidor local en `localhost:4321`          |
| `npm run build`   | Build de producción a `./dist/`             |
| `npm run preview` | Previsualiza el build localmente            |

## 📝 Licencia

El código de este proyecto es de uso libre para fines educativos. El contenido académico pertenece a su autor original (Prof. Jorge Iván Pérez).
