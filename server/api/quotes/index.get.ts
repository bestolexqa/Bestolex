import { useSupabaseAdmin, adminKeyProblem } from '~~/server/utils/supabase'

// Admin-only: server/middleware/admin-guard.ts denies this route without a session.
// Reads go through the service-role client because RLS hides the rows from the
// anon key - silently, which is what made the dashboard look empty.
export default defineEventHandler(async () => {
  const supabase = useSupabaseAdmin()

  if (!supabase) {
    throw createError({
      statusCode: 503,
      statusMessage: 'Supabase admin key is not configured',
      data: { reason: 'missing_service_role_key', problem: adminKeyProblem(), detail: 'Set SUPABASE_SERVICE_ROLE_KEY in Vercel' }
    })
  }

  const [q, a] = await Promise.all([
    supabase.from('quote_requests').select('*').order('created_at', { ascending: false }),
    supabase.from('appointments').select('*').order('created_at', { ascending: false })
  ])

  // An empty list must mean an empty table, never a failed query.
  const failure = q.error || a.error
  if (failure) {
    console.error('[quotes] read failed:', failure)
    throw createError({
      statusCode: 502,
      statusMessage: 'Could not read the requests',
      data: { detail: String(failure.message || failure) }
    })
  }

  return { quotes: q.data || [], appointments: a.data || [] }
})
