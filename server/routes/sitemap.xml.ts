import productCategories from '~~/data/products.json'
import { getCachedArticles } from '~~/server/utils/blogStorage'
import { withRepoArticles } from '~~/server/utils/repoArticles'
import { STAGES, stageView } from '~~/server/utils/goldMining'

const BASE = 'https://www.bestolex.com'

// Pages that exist in both languages. Arabic is the default (no prefix), English uses /en.
const STATIC_PATHS = ['/', '/about', '/sourcing', '/services', '/products', '/blog', '/contact', '/training', '/privacy', '/terms']

const xmlEscape = (s: string) => s
  .replace(/&/g, '&amp;')
  .replace(/</g, '&lt;')
  .replace(/>/g, '&gt;')
  .replace(/"/g, '&quot;')
  .replace(/'/g, '&apos;')

const arUrl = (p: string) => `${BASE}${p === '/' ? '' : p}`
const enUrl = (p: string) => `${BASE}/en${p === '/' ? '' : p}`

function entry(path: string, lastmod?: string): string {
  const alternates = [
    `<xhtml:link rel="alternate" hreflang="ar-QA" href="${xmlEscape(arUrl(path))}"/>`,
    `<xhtml:link rel="alternate" hreflang="en" href="${xmlEscape(enUrl(path))}"/>`,
    `<xhtml:link rel="alternate" hreflang="x-default" href="${xmlEscape(arUrl(path))}"/>`
  ].join('')
  const mod = lastmod ? `<lastmod>${lastmod}</lastmod>` : ''
  return [arUrl(path), enUrl(path)]
    .map(loc => `<url><loc>${xmlEscape(loc)}</loc>${mod}${alternates}</url>`)
    .join('\n')
}

export default defineEventHandler(async (event) => {
  const paths: Array<{ path: string, lastmod?: string }> = STATIC_PATHS.map(path => ({ path }))

  // Gold mining: its section page and the stage pages that already list families (the others are noindex).
  paths.push({ path: '/gold-mining' })
  for (const st of STAGES) {
    if ((stageView(st.id)?.cards.length || 0) > 0) paths.push({ path: `/gold-mining/${st.id}` })
  }

  for (const category of productCategories as any[]) {
    // The old gold-mining category URL redirects to /gold-mining.
    if (category.id !== 'gold-mining') paths.push({ path: `/products/category/${category.id}` })
    const products = [
      ...(category.products || []),
      ...((category.subcategories || []).flatMap((sub: any) => sub.products || []))
    ]
    for (const product of products) {
      if (product?.id) paths.push({ path: `/products/${product.id}` })
    }
  }

  const articles = await withRepoArticles(await getCachedArticles().catch(() => []))
  for (const article of articles as any[]) {
    const id = article?.id || article?.slug
    if (!id) continue
    if (article.isPublished === false || article.is_published === false) continue
    const raw = article.updatedAt || article.date
    const date = typeof raw === 'string' && /^\d{4}-\d{2}-\d{2}/.test(raw) ? raw.slice(0, 10) : undefined
    paths.push({ path: `/blog/${encodeURIComponent(String(id))}`, lastmod: date })
  }

  // De-duplicate (some products are listed in more than one sub-category)
  const seen = new Set<string>()
  const unique = paths.filter(p => (seen.has(p.path) ? false : (seen.add(p.path), true)))

  const body = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
${unique.map(p => entry(p.path, p.lastmod)).join('\n')}
</urlset>`

  setResponseHeader(event, 'Content-Type', 'application/xml; charset=utf-8')
  setResponseHeader(event, 'Cache-Control', 'public, max-age=0, s-maxage=3600, stale-while-revalidate=86400')
  return body
})
