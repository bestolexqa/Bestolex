import { getStoredCategories, saveStoredCategories } from '~~/server/utils/blogStorage'
import { useServerSupabase } from '~~/server/utils/supabase'

export default defineEventHandler(async (event) => {
  const id = getRouterParam(event, 'id')
  const supabase = useServerSupabase()

  // 1. Supabase delete if configured
  if (supabase) {
    try {
      await supabase
        .from('article_categories')
        .delete()
        .or(`id.eq.${id},slug.eq.${id}`)
    } catch (e) {
      console.warn('Supabase category delete error:', e)
    }
  }

  // 2. Persistent storage delete
  const list = await getStoredCategories()
  const filtered = list.filter((item: any) => item.id !== id && item.slug !== id)
  await saveStoredCategories(filtered)

  return { success: true }
})
