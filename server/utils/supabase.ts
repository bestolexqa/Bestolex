import { createClient } from '@supabase/supabase-js'

/**
 * Two clients, two jobs.
 *
 * The public one carries the anon key: the RLS policies let it INSERT a quote
 * request or an appointment, which is all the website's forms need.
 *
 * Reading those rows back is a different matter. The SELECT policy requires
 * auth.role() to be 'authenticated' or 'service_role', and the anon key is
 * neither - so a read returns ZERO ROWS AND NO ERROR. That is why the
 * dashboard showed no requests even after one had been stored: it was not an
 * empty table, it was a silently filtered read. Admin reads therefore use the
 * service-role key, which bypasses RLS and must never leave the server. Every
 * route that uses it sits behind server/middleware/admin-guard.ts.
 *
 * Opening the rows to the anon key instead would publish every customer's
 * name, phone and message, because that key ships inside the browser bundle.
 */

let publicClient: any = null
let adminClient: any = null

const clean = (v?: string) => (v ? v.trim() : '')
const usable = (v: string, placeholder: string) => !!v && !v.includes(placeholder)

function url(): string {
  const u = clean(process.env.SUPABASE_URL)
  if (!usable(u, 'your-project')) return ''
  return u.replace(/\/rest\/v1\/?$/, '').replace(/\/$/, '')
}

/** Anon key. Enough to INSERT; cannot read the rows back. */
export const useServerSupabase = () => {
  const u = url()
  // SUPABASE_KE is the historical, misspelled name of this variable in Vercel.
  const key = clean(process.env.SUPABASE_KEY || process.env.SUPABASE_KE)
  if (!u || !usable(key, 'your-supabase')) return null
  if (!publicClient) publicClient = createClient(u, key)
  return publicClient
}

/**
 * Service-role key: bypasses RLS, for admin-guarded routes only.
 * Returns null when the key is absent, so callers can say so plainly
 * instead of reporting an empty list.
 */
export const useSupabaseAdmin = () => {
  const u = url()
  const key = clean(process.env.SUPABASE_SERVICE_ROLE_KEY || process.env.SUPABASE_SERVICE_KEY)
  if (!u || !key) return null
  if (!adminClient) {
    adminClient = createClient(u, key, { auth: { persistSession: false, autoRefreshToken: false } })
  }
  return adminClient
}

/** True when admin reads are possible at all. */
export const hasSupabaseAdmin = () => useSupabaseAdmin() !== null
