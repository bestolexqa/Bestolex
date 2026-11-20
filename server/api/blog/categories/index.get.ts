import { getStoredCategories } from '~~/server/utils/blogStorage'
import { isAdminRequest } from '~~/server/utils/adminAuth'
import { BLOG_CATEGORIES } from '~~/server/utils/blogCategories'

export default defineEventHandler(async (event) => {
  // Visitors (header menu, blog) get the five fixed categories that every article is shown under;
  // a signed-in admin still sees the stored list in the dashboard.
  return isAdminRequest(event) ? await getStoredCategories() : BLOG_CATEGORIES
})
