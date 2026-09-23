import { getStoredArticles } from '~~/server/utils/blogStorage'

export default defineEventHandler(async () => {
  return await getStoredArticles()
})
