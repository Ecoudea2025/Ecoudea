import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';
import rehypeRaw from 'rehype-raw';

const base = '/Ecoudea';

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
  site: 'https://ecoudea2025.github.io',
  base,
  trailingSlash: 'ignore',
  prefetch: true,
  integrations: [
    sitemap({
      filter: (page) => !page.includes('/admin'),
    }),
  ],
  markdown: {
    syntaxHighlight: 'shiki',
    shikiConfig: {
      theme: 'one-dark-pro',
      wrap: false,
    },
    remarkPlugins: [remarkBaseImages],
    rehypePlugins: [rehypeRaw, rehypeBaseImages],
  },
  vite: {
    plugins: [tailwindcss()],
  },
  build: {
    inlineStylesheets: 'auto',
  },
});
