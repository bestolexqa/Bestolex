import { bothLocales, pingIndexNow } from '~~/server/utils/indexnow'
import { getStoredArticles, saveStoredArticles } from '~~/server/utils/blogStorage'
import { useServerSupabase } from '~~/server/utils/supabase'

export default defineEventHandler(async (event) => {
  const body = await readBody(event)
  const supabase = useServerSupabase()

  const slug = body.slug || (body.title_ar ? body.title_ar.trim().toLowerCase().replace(/[^\w\u0621-\u064A]+/g, '-') : 'article-' + Date.now())

  const newArticleRecord = {
    slug,
    title_ar: body.title_ar,
    title_en: body.title_en || body.title_ar,
    category_ar: body.category_ar || 'النظم الهيدروليكية المتقدمة',
    category_en: body.category_en || 'Advanced Hydraulic Systems',
    excerpt_ar: body.excerpt_ar || '',
    excerpt_en: body.excerpt_en || '',
    content_ar: body.content_ar,
    content_en: body.content_en || body.content_ar,
    image: body.image || 'https://cdn.bestolex.com/bestolex/news/news1.jpg',
    read_time_ar: body.read_time_ar || '5 دقائق قراءة',
    read_time_en: body.read_time_en || '5 min read',
    is_published: body.is_published !== false,
    is_featured: !!body.is_featured
  }

  // 1. If Supabase configured, attempt insert
  if (supabase) {
    try {
      await supabase.from('articles').insert([newArticleRecord])
    } catch (e) {
      console.warn('Supabase article insert failed, falling back to persistent cloud storage:', e)
    }
  }

  // 2. Save persistently to Bunny Storage & Local
  try {
    const list = await getStoredArticles()

    const formatted = {
      id: slug,
      slug: slug,
      title: { ar: body.title_ar, en: body.title_en || body.title_ar },
      category: { ar: body.category_ar || 'النظم الهيدروليكية المتقدمة', en: body.category_en || 'Advanced Hydraulic Systems' },
      date: new Date().toISOString().split('T')[0],
      readTime: { ar: body.read_time_ar || '5 دقائق قراءة', en: body.read_time_en || '5 min read' },
      image: body.image || 'https://cdn.bestolex.com/bestolex/news/news1.jpg',
      is_featured: !!body.is_featured,
      desc: { ar: body.excerpt_ar || body.title_ar, en: body.excerpt_en || body.title_en },
      content: { ar: body.content_ar, en: body.content_en || body.content_ar }
    }

    // Add to the beginning of the list
    list.unshift(formatted)
    await saveStoredArticles(list)
    // Let Bing/Copilot and other IndexNow engines know about the new article (and the blog index)
    await pingIndexNow(bothLocales([`/blog/${encodeURIComponent(String(slug))}`, '/blog']))

    return { success: true, data: formatted }
  } catch (err: any) {
    console.error('Error saving article:', err)
    return { success: false, error: err.message }
  }
})
