import { clearSessionCookie } from '~~/server/utils/adminAuth'

export default defineEventHandler((event) => {
  clearSessionCookie(event)
  return { success: true }
})
