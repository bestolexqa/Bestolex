import { isAdminRequest } from '~~/server/utils/adminAuth'
import { assets, withdrawn, copySabtechOne, verifySabtechOne, deleteSabtechOne, type RehostResult } from '~~/server/utils/sabtechRehost'

/**
 * Copies or verifies one batch of the sabtech.com.sa assets. The dashboard page
 * calls this repeatedly with a moving offset so a slow batch never times the
 * function out. Running it again is safe: a file already in the zone is skipped
 * unless force is set.
 *
 * mode 'purge' works on a different list: SAB TECH's own brochures and
 * datasheets, which must not sit on our zone at all. It deletes them.
 */
export default defineEventHandler(async (event) => {
  if (!isAdminRequest(event)) throw createError({ statusCode: 401, statusMessage: 'Unauthorized' })
  const body = await readBody<{ offset?: number, limit?: number, force?: boolean, mode?: 'copy' | 'verify' | 'purge' }>(event) || {}
  const offset = Math.max(0, Number(body.offset) || 0)
  const mode = body.mode === 'verify' || body.mode === 'purge' ? body.mode : 'copy'
  // Three files a batch: a certificate is 2.2 MB and each file costs an
  // existence check, a download and an upload in series.
  const batch = mode === 'copy' ? 3 : 20
  const limit = Math.min(mode === 'copy' ? 5 : 20, Math.max(1, Number(body.limit) || batch))
  const force = body.force === true

  const list = mode === 'purge' ? withdrawn() : assets()
  const slice = list.slice(offset, offset + limit)

  const results: RehostResult[] = []
  for (const a of slice) {
    if (mode === 'verify') results.push(await verifySabtechOne(a))
    else if (mode === 'purge') results.push(await deleteSabtechOne(a))
    else results.push(await copySabtechOne(a, force))
  }

  return {
    mode,
    total: list.length,
    offset,
    processed: slice.length,
    nextOffset: offset + slice.length,
    done: offset + slice.length >= list.length,
    copied: results.filter(r => r.status === 'copied').length,
    exists: results.filter(r => r.status === 'exists').length,
    verified: results.filter(r => r.status === 'verified').length,
    deleted: results.filter(r => r.status === 'deleted').length,
    absent: results.filter(r => r.status === 'absent').length,
    failed: results.filter(r => r.status === 'failed'),
    results
  }
})
