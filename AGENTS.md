## Development

When starting the dev server, use background mode:

```
astro dev --background
```

Manage the background server with `astro dev stop`, `astro dev status`, and `astro dev logs`.

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
~/.local/bin/codebase-memory-mcp.exe cli index_repository --repo-path "D:\Ecoudea.github.io" --mode moderate
```

## Documentation

Full documentation: https://docs.astro.build

Consult these guides before working on related tasks:

- [Adding pages, dynamic routes, or middleware](https://docs.astro.build/en/guides/routing/)
- [Working with Astro components](https://docs.astro.build/en/basics/astro-components/)
- [Using React, Vue, Svelte, or other framework components](https://docs.astro.build/en/guides/framework-components/)
- [Adding or managing content](https://docs.astro.build/en/guides/content-collections/)
- [Adding styles or using Tailwind](https://docs.astro.build/en/guides/styling/)
- [Supporting multiple languages](https://docs.astro.build/en/guides/internationalization/)

