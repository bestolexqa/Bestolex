import { bothLocales, pingIndexNow } from '~~/server/utils/indexnow'
import { getStoredArticles, saveStoredArticles } from '~~/server/utils/blogStorage'
import { useServerSupabase } from '~~/server/utils/supabase'

export default defineEventHandler(async (event) => {
  const id = getRouterParam(event, 'id')
  const body = await readBody(event)
  const supabase = useServerSupabase()

  // 1. Supabase update if configured
  if (supabase) {
    try {
      await supabase
        .from('articles')
        .update({
          title_ar: body.title_ar,
          title_en: body.title_en || body.title_ar,
          category_ar: body.category_ar,
          category_en: body.category_en,
          excerpt_ar: body.excerpt_ar,
          excerpt_en: body.excerpt_en,
          content_ar: body.content_ar,
          content_en: body.content_en,
          image: body.image,
          read_time_ar: body.read_time_ar,
          read_time_en: body.read_time_en,
          is_published: body.is_published,
          is_featured: body.is_featured,
          updated_at: new Date().toISOString()
        })
        .or(`id.eq.${id},slug.eq.${id}`)
    } catch (e) {
      console.warn('Supabase article update error:', e)
    }
  }

  // 2. Persistent storage update (Bunny + Local)
  const list = await getStoredArticles()
  const updatedList = list.map((item: any) => {
    if (item.id === id || item.slug === id) {
      return {
        ...item,
        title: { ar: body.title_ar, en: body.title_en || body.title_ar },
        category: { ar: body.category_ar, en: body.category_en || body.category_ar },
        desc: { ar: body.excerpt_ar || body.title_ar, en: body.excerpt_en || body.title_en },
        content: { ar: body.content_ar, en: body.content_en || body.content_ar },
        readTime: { ar: body.read_time_ar || '5 دقائق قراءة', en: body.read_time_en || '5 min read' },
        image: body.image || item.image,
        updatedAt: new Date().toISOString().split('T')[0],
        is_featured: body.is_featured !== undefined ? body.is_featured : item.is_featured
      }
    }
    return item
  })

  await saveStoredArticles(updatedList)
  await pingIndexNow(bothLocales([`/blog/${encodeURIComponent(String(id))}`]))

  return { success: true }
})
