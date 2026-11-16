import { createSessionToken, getAdminCredentials, safeEqual, setSessionCookie } from '~~/server/utils/adminAuth'

// Basic brute-force slowdown (per server instance).
const attempts = new Map<string, { count: number, first: number }>()
const WINDOW_MS = 15 * 60 * 1000
const MAX_ATTEMPTS = 8

export default defineEventHandler(async (event) => {
  const creds = getAdminCredentials()
  if (!creds) {
    throw createError({ statusCode: 503, statusMessage: 'Admin login is not configured' })
  }

  const ip = getRequestIP(event, { xForwardedFor: true }) || 'unknown'
  const now = Date.now()
  const record = attempts.get(ip)
  if (record && now - record.first < WINDOW_MS && record.count >= MAX_ATTEMPTS) {
    throw createError({ statusCode: 429, statusMessage: 'Too many attempts, try again later' })
  }

  const body = await readBody(event)
  const email = String(body?.email || '').trim().toLowerCase()
  const password = String(body?.password || '')

  if (safeEqual(email, creds.email) && safeEqual(password, creds.password)) {
    attempts.delete(ip)
    setSessionCookie(event, createSessionToken(creds.email, creds.password))
    return { success: true }
  }

  if (!record || now - record.first >= WINDOW_MS) attempts.set(ip, { count: 1, first: now })
  else record.count++

  await new Promise(resolve => setTimeout(resolve, 600))
  throw createError({ statusCode: 401, statusMessage: 'Invalid credentials' })
})
