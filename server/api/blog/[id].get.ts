import { getCachedArticles, getStoredArticles } from '~~/server/utils/blogStorage'
import { isAdminRequest } from '~~/server/utils/adminAuth'
import { withRepoArticles } from '~~/server/utils/repoArticles'

export default defineEventHandler(async (event) => {
  const id = getRouterParam(event, 'id')
  // Visitors get the in-memory copy; a signed-in admin always sees the stored version.
  const stored = isAdminRequest(event) ? await getStoredArticles() : await getCachedArticles()
  const list = await withRepoArticles(stored)

  const found = list.find((a: any) => a.id === id || a.slug === id)
  if (found) {
    // Up to three related articles: same category first, then the newest others.
    const catOf = (a: any) => String(a?.category?.ar || a?.category_ar || '').trim()
    const others = list.filter((a: any) => a && a !== found && a.id !== found.id && a.isPublished !== false && a.is_published !== false)
    const sameCat = others.filter((a: any) => catOf(a) && catOf(a) === catOf(found))
    const related = [...sameCat, ...others.filter((a: any) => !sameCat.includes(a))]
      .slice(0, 3)
      .map((a: any) => ({ id: a.id || a.slug, title: a.title, image: a.image, date: a.date, category: a.category }))
    return {
      ...found,
      related,
      title_ar: found.title?.ar || found.title_ar,
      title_en: found.title?.en || found.title_en,
      category_ar: found.category?.ar || found.category_ar,
      category_en: found.category?.en || found.category_en,
      excerpt_ar: found.desc?.ar || found.excerpt_ar,
      excerpt_en: found.desc?.en || found.excerpt_en,
      content_ar: found.content?.ar || found.content_ar,
      content_en: found.content?.en || found.content_en,
      read_time_ar: found.readTime?.ar || found.read_time_ar,
      read_time_en: found.readTime?.en || found.read_time_en
    }
  }

  throw createError({ statusCode: 404, statusMessage: 'Article not found' })
})
