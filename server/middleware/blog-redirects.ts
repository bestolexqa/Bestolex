import { blogRedirectTarget } from '~~/server/utils/repoArticles'
import { isAdminRequest } from '~~/server/utils/adminAuth'

/**
 * 301 for blog articles merged into another article (server/blog-meta/redirects.json):
 *   /blog/<old>, /en/blog/<old>  → the same page of the article it was merged into
 *   GET /api/blog/<old>          → /api/blog/<new> (client-side navigation; not for the signed-in
 *                                  dashboard, which still reads the stored article)
 * Ids are Arabic, so the path is decoded before the lookup and the target re-encoded.
 */
export default defineEventHandler((event) => {
  const method = event.method.toUpperCase()
  if (method !== 'GET' && method !== 'HEAD') return
  const url = getRequestURL(event)
  if (!url.pathname.includes('/blog/')) return
  let path: string
  try {
    path = decodeURIComponent(url.pathname)
  } catch {
    return
  }
  const m = path.match(/^(\/en|\/api)?\/blog\/([^/]+?)\/?$/)
  if (!m) return
  const to = blogRedirectTarget(m[2])
  if (!to) return
  if (m[1] === '/api' && isAdminRequest(event)) return
  const prefix = m[1] === '/api' ? '/api/blog/' : `${m[1] || ''}/blog/`
  return sendRedirect(event, `${prefix}${encodeURIComponent(to)}${url.search}`, 301)
})
