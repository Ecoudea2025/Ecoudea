const CACHE='ecoudea-v1';

function base() {
  try { return new URL(self.registration.scope).pathname.replace(/\/$/, ''); }
  catch (e) { return ''; }
}

const PRECACHE = [
  '/',
  '/offline/',
  '/favicon.svg',
  '/assets/images/logo-ecoudea.svg',
  '/assets/js/animations.js',
  '/assets/js/enhance.js',
].map((p) => base() + p);

self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE).then((c) => c.addAll(PRECACHE)).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => !k.startsWith('ecoudea-')).map((k) => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

const MAX_ASTRO = 80;
const MAX_IMG = 60;

async function trimCategory(cache, predicate, max) {
  const keys = await cache.keys();
  const matching = keys.filter(predicate);
  if (matching.length <= max) return;
  const toDelete = matching.length - max;
  for (let i = 0; i < toDelete; i++) await cache.delete(matching[i]);
}

self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET') return;
  let url;
  try { url = new URL(req.url); } catch (err) { return; }
  if (url.origin !== location.origin) return;

  const path = url.pathname;
  const b = base();

  // Navegaciones: network-first con timeout 2.5s -> cache -> /offline/
  if (req.mode === 'navigate') {
    e.respondWith((async () => {
      const cache = await caches.open(CACHE);
      try {
        const res = await Promise.race([
          fetch(req),
          new Promise((_, rej) => setTimeout(() => rej(new Error('timeout')), 2500)),
        ]);
        if (res && res.ok) cache.put(req, res.clone());
        return res;
      } catch (err) {
        const cached = await cache.match(req);
        if (cached) return cached;
        const offline = await cache.match(b + '/offline/');
        if (offline) return offline;
        return fetch(b + '/offline/');
      }
    })());
    return;
  }

  // /_astro/* : cache-first (inmutables)
  if (path.indexOf('/_astro/') !== -1) {
    e.respondWith((async () => {
      const cache = await caches.open(CACHE);
      const cached = await cache.match(req);
      if (cached) return cached;
      const res = await fetch(req);
      if (res && res.ok) {
        await cache.put(req, res.clone());
        await trimCategory(cache, (r) => new URL(r.url).pathname.indexOf('/_astro/') !== -1, MAX_ASTRO);
      }
      return res;
    })());
    return;
  }

  // pagefind/* : stale-while-revalidate
  if (path.indexOf('/pagefind/') !== -1) {
    e.respondWith((async () => {
      const cache = await caches.open(CACHE);
      const cached = await cache.match(req);
      const fp = fetch(req).then((res) => {
        if (res && res.ok) cache.put(req, res.clone());
        return res;
      }).catch(() => cached);
      return cached || fp;
    })());
    return;
  }

  // Imagenes mismo-origen: cache-first con tope 60 FIFO
  if (req.destination === 'image') {
    e.respondWith((async () => {
      const cache = await caches.open(CACHE);
      const cached = await cache.match(req);
      if (cached) return cached;
      const res = await fetch(req);
      if (res && res.ok) {
        await cache.put(req, res.clone());
        await trimCategory(cache, (r) => /\.(png|jpe?g|webp|svg|gif|avif|ico)$/i.test(new URL(r.url).pathname), MAX_IMG);
      }
      return res;
    })());
    return;
  }
});
