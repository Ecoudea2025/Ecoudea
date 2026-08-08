import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://ecoudea2025.github.io',
  base: '/Ecoudea',
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
  },
  vite: {
    plugins: [tailwindcss()],
  },
  build: {
    inlineStylesheets: 'auto',
  },
});
