import { useSupabaseAdmin } from '~~/server/utils/supabase'

// Admin-only. Updating a status needs the service-role client for the same
// reason reading does: RLS hides the row from the anon key, so the UPDATE
// matched nothing and this handler still answered success.
export default defineEventHandler(async (event) => {
  const id = getRouterParam(event, 'id')
  const body = (await readBody(event)) || {}
  const supabase = useSupabaseAdmin()

  if (!id) throw createError({ statusCode: 400, statusMessage: 'Missing id' })
  if (!body.status) throw createError({ statusCode: 400, statusMessage: 'Missing status' })
  if (!supabase) {
    throw createError({
      statusCode: 503,
      statusMessage: 'Supabase admin key is not configured',
      data: { reason: 'missing_service_role_key' }
    })
  }

  const table = body.type === 'appointment' ? 'appointments' : 'quote_requests'
  const { data, error } = await supabase
    .from(table)
    .update({ status: body.status })
    .eq('id', id)
    .select('id')

  if (error) {
    console.error('[quotes] status update failed:', error)
    throw createError({ statusCode: 502, statusMessage: 'Could not update the status', data: { detail: String(error.message || error) } })
  }
  if (!data || data.length === 0) {
    throw createError({ statusCode: 404, statusMessage: 'Request not found' })
  }

  return { success: true, id, status: body.status }
})
