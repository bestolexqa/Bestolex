import { assets, copyOne, verifyOne, type RehostResult } from '~~/server/utils/sabtechRehost'

/**
 * Copies or verifies one batch of the sabtech.com.sa assets. The dashboard page
 * calls this repeatedly with a moving offset so a slow batch never times the
 * function out. Running it again is safe: a file already in the zone is skipped
 * unless force is set.
 */
export default defineEventHandler(async (event) => {
  const body = await readBody<{ offset?: number, limit?: number, force?: boolean, mode?: 'copy' | 'verify' }>(event) || {}
  const offset = Math.max(0, Number(body.offset) || 0)
  const mode = body.mode === 'verify' ? 'verify' : 'copy'
  const limit = Math.min(25, Math.max(1, Number(body.limit) || (mode === 'verify' ? 20 : 8)))
  const force = body.force === true

  const list = assets()
  const slice = list.slice(offset, offset + limit)

  const results: RehostResult[] = []
  for (const a of slice) {
    results.push(mode === 'verify' ? await verifyOne(a) : await copyOne(a, force))
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
    failed: results.filter(r => r.status === 'failed'),
    results
  }
})
