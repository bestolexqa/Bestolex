// Dashboard route guard. The session cookie is httpOnly, so the client asks the server.
export default defineNuxtRouteMiddleware(async (to) => {
  const isDashboard = /(^|\/)dashboard(\/|$)/.test(to.path)
  if (!isDashboard) return

  const isLogin = /\/dashboard\/login\/?$/.test(to.path)
  const requestFetch = useRequestFetch()
  const session = await requestFetch<{ authenticated: boolean }>('/api/auth/session')
    .catch(() => ({ authenticated: false }))

  if (!isLogin && !session.authenticated) {
    return navigateTo('/dashboard/login')
  }
  if (isLogin && session.authenticated) {
    return navigateTo('/dashboard')
  }
})
