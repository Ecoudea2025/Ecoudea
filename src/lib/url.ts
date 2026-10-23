/**
 * Helper canónico para construir URLs internas con el base path.
 * Una sola fuente de verdad: import.meta.env.BASE_URL (Astro) o BASE_PATH.
 *
 * Uso en .astro:
 *   import { url } from '../lib/url';
 *   <a href={url(`/cursos/${id}`)}>…</a>
 *   <img src={url('/assets/images/logo.svg')} />
 */
export function url(path: string, base?: string): string {
  const b =
    base ??
    (typeof import.meta !== 'undefined' && (import.meta as any).env?.BASE_URL) ??
    '';
  const normBase = b === '/' ? '' : b.replace(/\/$/, '');
  if (!path) return normBase || '/';
  if (/^(https?:|mailto:|tel:|#)/.test(path)) return path;
  const p = path.startsWith('/') ? path : `/${path}`;
  return `${normBase}${p}`;
}
