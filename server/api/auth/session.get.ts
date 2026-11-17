import { isAdminRequest } from '~~/server/utils/adminAuth'

export default defineEventHandler((event) => {
  setResponseHeader(event, 'Cache-Control', 'no-store')
  return { authenticated: isAdminRequest(event) }
})
