import { getStoredCategories, saveStoredCategories } from '~~/server/utils/blogStorage'
import { useServerSupabase } from '~~/server/utils/supabase'

export default defineEventHandler(async (event) => {
  const body = await readBody(event)
  const supabase = useServerSupabase()

  if (!body.name_ar) {
    throw createError({ statusCode: 400, message: 'اسم القسم بالعربية مطلوب' })
  }

  const slug = body.slug || (body.name_en ? body.name_en.toLowerCase().trim().replace(/[^\w\u0621-\u064A]+/g, '-') : 'cat-' + Date.now())
  const name_en = body.name_en || body.name_ar

  const newCategory = {
    id: 'cat-' + Date.now(),
    name_ar: body.name_ar,
    name_en,
    slug
  }

  // 1. Insert to Supabase if connected
  if (supabase) {
    try {
      await supabase.from('article_categories').insert([newCategory])
    } catch (e) {
      console.warn('Supabase category insert error:', e)
    }
  }

  // 2. Persistent storage (Bunny + Local)
  const list = await getStoredCategories()
  list.push(newCategory)
  await saveStoredCategories(list)

  return { success: true, data: newCategory }
})
