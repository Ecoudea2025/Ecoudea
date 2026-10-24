const site = process.env.SITE_URL || 'https://ecoudea2025.github.io';
const base = process.env.BASE_PATH || '/Ecoudea';

export async function GET() {
  const body = `User-agent: *
Allow: /
Disallow: ${base}/admin/
Disallow: ${base}/styleguide/

Sitemap: ${site}${base}/sitemap-index.xml
`;
  return new Response(body.trimStart(), {
    headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
}
