import { getCachedCategories, getStoredCategories } from '~~/server/utils/blogStorage'
import { isAdminRequest } from '~~/server/utils/adminAuth'

export default defineEventHandler(async (event) => {
  // Visitors get the in-memory copy; a signed-in admin always sees the stored version.
  return isAdminRequest(event) ? await getStoredCategories() : await getCachedCategories()
})
