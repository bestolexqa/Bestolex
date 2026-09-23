import { getStoredCategories, saveStoredCategories } from '~~/server/utils/blogStorage'
import { useServerSupabase } from '~~/server/utils/supabase'

export default defineEventHandler(async (event) => {
  const id = getRouterParam(event, 'id')
  const body = await readBody(event)
  const supabase = useServerSupabase()

  // 1. Supabase update if configured
  if (supabase) {
    try {
      await supabase
        .from('article_categories')
        .update({
          name_ar: body.name_ar,
          name_en: body.name_en,
          slug: body.slug || (body.name_en ? body.name_en.toLowerCase().trim().replace(/[^\w\u0621-\u064A]+/g, '-') : undefined)
        })
        .or(`id.eq.${id},slug.eq.${id}`)
    } catch (e) {
      console.warn('Supabase category update error:', e)
    }
  }

  // 2. Persistent storage update
  const list = await getStoredCategories()
  const updatedList = list.map((item: any) => {
    if (item.id === id || item.slug === id) {
      return {
        ...item,
        name_ar: body.name_ar || item.name_ar,
        name_en: body.name_en || item.name_en,
        slug: body.slug || item.slug
      }
    }
    return item
  })

  await saveStoredCategories(updatedList)

  return { success: true }
})
