## Development

When starting the dev server, use background mode:

```
astro dev --background
```

Manage the background server with `astro dev stop`, `astro dev status`, and `astro dev logs`.

## Build & Deploy

```
npm run build    # astro build + gzip precompression (GitHub Pages)
```

- `dist/` is gzip-precompressed by `scripts/gzip.mjs` — GitHub Pages serves `.gz` automatically.
- Deploy is automatic via `.github/workflows/deploy.yml` on push to `master` (~2 min).
- `npm install` (not `npm ci`) — the lockfile can drift.
- Settings → Pages → Source must be "GitHub Actions".

## Content Structure (for efficient commits)

```
src/content/courses/*.md   # course metadata (title, description, category, order)
src/content/classes/*.md   # one file per class (frontmatter + Markdown body)
src/pages/                 # routes (index, cursos/[course], cursos/[course]/[class], acercade)
src/components/            # Astro components (Navbar, Footer, CourseCard, ...)
public/assets/             # static: images, KaTeX, fonts, JS helpers
```

Guidelines:

- **One class = one file.** Editing a class never touches other files → small, reviewable commits.
- **Never edit `public/assets/` blindly.** Images there are referenced by name from Markdown; use `tools/optimize-images.ps1` for optimization (writes to a separate folder, never overwrites).
- **Frontmatter of classes:** `title`, `course` (course id), `order` (sequential), `classType` (`clase`|`practica`|`presentacion`|`guia`), optional `description`, `tags`, `math` (`true` if LaTeX — controls KaTeX CSS; rendering happens at build time).
- **New course:** add `src/content/courses/<id>.md` + classes referencing `course: <id>`.

## Commit Convention

Conventional Commits, one logical change per commit:

```
feat:       new feature / new course / new class
fix:        bug fix (e.g. LaTeX, links, layout)
perf:       performance (gzip, prefetch, images)
refactor:   code changes without behavior change
style:      typography, colors, spacing
docs:       AGENTS.md, README, comments
chore:      tooling, config, deps
```

Examples: `feat: add estadistica-iii course`, `fix: repair LaTeX in clase-04`, `perf: gzip assets`.

Commit scoped to content: `git add src/content/classes/estadistica-i-clase-05.md` + `feat(estadistica-i): add clase-05`.

## Image Optimization

`tools/optimize-images.ps1` — safe ffmpeg-based optimizer (WebP/AVIF, resizes, never touches originals):

```
.\tools\optimize-images.ps1 -Source "D:\Ecoudea.github.io\public\assets\images" -Out "D:\imgs-web" -MaxWidth 1200
```

## Code Intelligence (MCP)

This project is indexed with **codebase-memory-mcp** (DeusData). The knowledge graph is served via MCP and available as the `codebase-memory` server in OpenCode.

**Before reading many files, use MCP tools to answer structural questions in far fewer tokens:**

- `search_graph` — find functions/classes/routes by name or semantic meaning
- `get_architecture` — overall structure of components, modules, dependencies
- `trace_path` — call chains (who calls what, depth up to 5)
- `get_code_snippet` — fetch exact code by node ID
- `query_graph` — Cypher-style multi-hop queries

The indexed project name is `D-Ecoudea.github.io` (root: `D:/Ecoudea.github.io`). The index is stored locally and auto-syncs on file changes.

To re-index after major changes (or on a new machine), run:

```
codebase-memory-mcp cli index_repository --repo-path "D:\Ecoudea.github.io" --mode moderate
```

(Binary is the npm global install; UI option `--ui=true` serves a 3D graph at `http://localhost:9749`.)

## Documentation

Full documentation: https://docs.astro.build

Consult these guides before working on related tasks:

- [Adding pages, dynamic routes, or middleware](https://docs.astro.build/en/guides/routing/)
- [Working with Astro components](https://docs.astro.build/en/basics/astro-components/)
- [Using React, Vue, Svelte, or other framework components](https://docs.astro.build/en/guides/framework-components/)
- [Adding or managing content](https://docs.astro.build/en/guides/content-collections/)
- [Adding styles or using Tailwind](https://docs.astro.build/en/guides/styling/)
- [Supporting multiple languages](https://docs.astro.build/en/guides/internationalization/)
