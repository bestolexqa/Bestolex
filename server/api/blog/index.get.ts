import { getCachedArticles, getStoredArticles } from '~~/server/utils/blogStorage'
import { isAdminRequest } from '~~/server/utils/adminAuth'

// GET /api/blog            → full articles (dashboard, sitemap)
// GET /api/blog?view=list  → cards only (no article bodies) for the homepage and blog index,
//                            which keeps their HTML payload small.
export default defineEventHandler(async (event) => {
  // Visitors get the in-memory copy; a signed-in admin (dashboard) always sees the stored version.
  const articles = isAdminRequest(event) ? await getStoredArticles() : await getCachedArticles()
  if (getQuery(event).view !== 'list') return articles
  return articles.map(({ content, content_ar, content_en, ...card }: any) => card)
})
