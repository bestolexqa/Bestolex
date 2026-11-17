import { createHash, createHmac, timingSafeEqual } from 'node:crypto'
import type { H3Event } from 'h3'

export const ADMIN_COOKIE = 'bestolex_admin_session'
const SESSION_TTL_SECONDS = 60 * 60 * 12 // 12 hours

/**
 * Admin credentials come ONLY from environment variables (set in Vercel).
 * There is deliberately no fallback: if they are missing, admin login is disabled.
 */
export function getAdminCredentials(): { email: string, password: string } | null {
  // Trim accidental spaces/newlines pasted into the Vercel dashboard
  const email = (process.env.ADMIN_EMAIL || '').trim().toLowerCase()
  const password = (process.env.ADMIN_PASSWORD || '').trim()
  if (!email || password.length < 12) return null
  return { email, password }
}

function signingKey(password: string): Buffer {
  const secret = process.env.ADMIN_SESSION_SECRET || `bestolex-admin-session:${password}`
  return createHash('sha256').update(secret).digest()
}

function sign(payload: string, password: string): string {
  return createHmac('sha256', signingKey(password)).update(payload).digest('base64url')
}

export function safeEqual(a: string, b: string): boolean {
  const ha = createHash('sha256').update(a).digest()
  const hb = createHash('sha256').update(b).digest()
  return timingSafeEqual(ha, hb)
}

export function createSessionToken(email: string, password: string): string {
  const exp = Math.floor(Date.now() / 1000) + SESSION_TTL_SECONDS
  const payload = Buffer.from(`${email}|${exp}`).toString('base64url')
  return `${payload}.${sign(payload, password)}`
}

export function verifySessionToken(token: string | undefined | null): boolean {
  const creds = getAdminCredentials()
  if (!creds || !token || !token.includes('.')) return false
  const [payload, signature] = token.split('.')
  if (!payload || !signature) return false
  if (!safeEqual(signature, sign(payload, creds.password))) return false
  const [email, exp] = Buffer.from(payload, 'base64url').toString().split('|')
  if (email !== creds.email) return false
  return Number(exp) > Math.floor(Date.now() / 1000)
}

export function setSessionCookie(event: H3Event, token: string) {
  setCookie(event, ADMIN_COOKIE, token, {
    httpOnly: true,
    secure: process.env.NODE_ENV === 'production',
    sameSite: 'strict',
    path: '/',
    maxAge: SESSION_TTL_SECONDS
  })
}

export function clearSessionCookie(event: H3Event) {
  deleteCookie(event, ADMIN_COOKIE, { path: '/' })
}

export function isAdminRequest(event: H3Event): boolean {
  return verifySessionToken(getCookie(event, ADMIN_COOKIE))
}
