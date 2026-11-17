import { getStoredArticles } from '~~/server/utils/blogStorage'

// GET /api/blog            → full articles (dashboard, sitemap)
// GET /api/blog?view=list  → cards only (no article bodies) for the homepage and blog index,
//                            which keeps their HTML payload small.
export default defineEventHandler(async (event) => {
  const articles = await getStoredArticles()
  if (getQuery(event).view !== 'list') return articles
  return articles.map(({ content, content_ar, content_en, ...card }: any) => card)
})
