import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';
import { unified } from '@astrojs/markdown-remark';
import rehypeRaw from 'rehype-raw';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import {
  remarkNormalizeMath,
  rehypeMathNormalize,
} from './src/lib/markdown-math.mjs';
import { katexMacros } from './src/lib/katex-macros.mjs';
import { remarkBlocks } from './src/lib/remark-blocks.mjs';
import archiveManifest from './archive/manifest.json' with { type: 'json' };

const archivedPaths = new Set([
  ...archiveManifest.courses.map((c) => `/cursos/${c.id}`),
  ...archiveManifest.classes.map((c) => `/cursos/${c.course}/${c.id}`),
]);

const base = process.env.BASE_PATH || '/Ecoudea';
const site = process.env.SITE_URL || 'https://ecoudea2025.github.io';

function remarkBaseImages() {
  return function (tree) {
    const visit = (node) => {
      if (node.type === 'image' && node.url && node.url.startsWith('/assets/')) {
        node.url = base + node.url;
      }
      if (node.children) node.children.forEach(visit);
    };
    visit(tree);
  };
}

function rehypeBaseImages() {
  return function (tree) {
    const visit = (node) => {
      if (node.type === 'element' && node.tagName === 'img') {
        const src = node.properties?.src;
        if (typeof src === 'string' && src.startsWith('/assets/')) {
          node.properties.src = base + src;
        }
      }
      if (node.children) node.children.forEach(visit);
    };
    visit(tree);
  };
}

export default defineConfig({
  site,
  base,
  trailingSlash: 'ignore',
  prefetch: true,
  integrations: [
    sitemap({
      filter: (page) => {
        if (page.includes('/admin')) return false;
        if (page.includes('/styleguide')) return false;
        if (page.includes('/offline')) return false;
        try {
          const u = new URL(page);
          const rel = u.pathname.replace(new RegExp(`^${base}`), '').replace(/\/$/, '') || '/';
          if (archivedPaths.has(rel)) return false;
        } catch {}
        return true;
      },
    }),
  ],
  markdown: {
    syntaxHighlight: 'shiki',
    shikiConfig: {
      theme: 'one-dark-pro',
      wrap: false,
    },
    // Astro 7: el contenido usa `processor` (unified); las claves sueltas
    // remarkPlugins/rehypePlugins no llegan al renderer. No volver atrás.
    processor: unified({
      remarkPlugins: [remarkMath, remarkNormalizeMath, remarkBlocks, remarkBaseImages],
      rehypePlugins: [rehypeRaw, rehypeMathNormalize, rehypeBaseImages, [rehypeKatex, { trust: true, strict: false, macros: katexMacros }]],
    }),
  },
  vite: {
    plugins: [tailwindcss()],
  },
  build: {
    inlineStylesheets: 'auto',
  },
});
