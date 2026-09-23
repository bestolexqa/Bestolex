import { getStoredCategories } from '~~/server/utils/blogStorage'

export default defineEventHandler(async () => {
  return await getStoredCategories()
})
