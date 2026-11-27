import { isAdminRequest } from '~~/server/utils/adminAuth'

/**
 * Server-side protection for every admin API.
 * Public endpoints: reading the blog and the product-family model tables, submitting the contact / quote / appointment forms,
 * analytics event tracking, and the login/session endpoints themselves.
 */
const PUBLIC_RULES: Array<{ method: string, test: (path: string) => boolean }> = [
  { method: 'GET', test: p => p === '/api/blog' || p.startsWith('/api/blog/') },
  { method: 'GET', test: p => p.startsWith('/api/catalog/family/') },
  { method: 'POST', test: p => p === '/api/contact' },
  { method: 'POST', test: p => p === '/api/book-appointment' },
  { method: 'POST', test: p => p === '/api/analytics/track' },
  { method: 'POST', test: p => p === '/api/auth/login' },
  { method: 'POST', test: p => p === '/api/auth/logout' },
  { method: 'GET', test: p => p === '/api/auth/session' }
]

export default defineEventHandler((event) => {
  const path = getRequestURL(event).pathname.replace(/\/+$/, '') || '/'
  if (!path.startsWith('/api/')) return

  const method = event.method.toUpperCase()
  const isPublic = PUBLIC_RULES.some(rule => (rule.method === method || (rule.method === 'GET' && method === 'HEAD')) && rule.test(path))
  if (isPublic) return

  if (!isAdminRequest(event)) {
    throw createError({ statusCode: 401, statusMessage: 'Unauthorized' })
  }
})
