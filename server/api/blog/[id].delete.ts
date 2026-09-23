import { getStoredArticles, saveStoredArticles } from '~~/server/utils/blogStorage'
import { useServerSupabase } from '~~/server/utils/supabase'

export default defineEventHandler(async (event) => {
  const id = getRouterParam(event, 'id')
  const supabase = useServerSupabase()

  // 1. Supabase delete if configured
  if (supabase) {
    try {
      await supabase
        .from('articles')
        .delete()
        .or(`id.eq.${id},slug.eq.${id}`)
    } catch (e) {
      console.warn('Supabase article delete error:', e)
    }
  }

  // 2. Persistent storage delete
  const list = await getStoredArticles()
  const filtered = list.filter((item: any) => item.id !== id && item.slug !== id)
  await saveStoredArticles(filtered)

  return { success: true }
})
