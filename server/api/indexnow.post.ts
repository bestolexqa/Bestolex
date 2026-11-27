import productCategories from '~~/data/products.json'
import { getStoredArticles } from '~~/server/utils/blogStorage'
import { bothLocales, pingIndexNow } from '~~/server/utils/indexnow'

// POST /api/indexnow (admin only, enforced by server/middleware/admin-guard.ts)
// Body: { "paths": ["/products/road-blocker", ...] }  → submit those pages in both languages
//       { "all": true }                                → submit every public page (after a release)
export default defineEventHandler(async (event) => {
  const body = await readBody(event).catch(() => ({})) || {}
  let paths: string[] = Array.isArray(body.paths) ? body.paths.filter((p: any) => typeof p === 'string') : []

  if (body.all === true) {
    paths = ['/', '/about', '/sourcing', '/services', '/products', '/blog', '/contact', '/training']
    for (const category of productCategories as any[]) {
      paths.push(`/products/category/${category.id}`)
      const products = [...(category.products || []), ...((category.subcategories || []).flatMap((s: any) => s.products || []))]
      for (const p of products) if (p?.id) paths.push(`/products/${p.id}`)
    }
    const articles = await getStoredArticles().catch(() => [])
    for (const a of articles as any[]) {
      const id = a?.id || a?.slug
      if (id && a.isPublished !== false && a.is_published !== false) paths.push(`/blog/${encodeURIComponent(String(id))}`)
    }
  }

  if (!paths.length) throw createError({ statusCode: 400, statusMessage: 'Provide "paths" or "all": true' })
  return await pingIndexNow(bothLocales(paths))
})
