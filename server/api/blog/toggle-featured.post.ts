import { getStoredArticles, saveStoredArticles } from '~~/server/utils/blogStorage'
import { useServerSupabase } from '~~/server/utils/supabase'

export default defineEventHandler(async (event) => {
  const body = await readBody(event)
  const { id, is_featured } = body
  const supabase = useServerSupabase()

  // 1. Update Supabase if configured
  if (supabase) {
    try {
      await supabase
        .from('articles')
        .update({ is_featured: !!is_featured })
        .or(`id.eq.${id},slug.eq.${id}`)
    } catch (e) {
      console.warn('Supabase toggle featured error:', e)
    }
  }

  // 2. Persistent storage update
  const list = await getStoredArticles()
  const updatedList = list.map((item: any) => {
    if (item.id === id || item.slug === id) {
      return {
        ...item,
        is_featured: !!is_featured,
        isFeatured: !!is_featured
      }
    }
    return item
  })

  await saveStoredArticles(updatedList)

  return { success: true }
})
