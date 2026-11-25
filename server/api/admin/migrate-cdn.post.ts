import { isAdminRequest } from '~~/server/utils/adminAuth'
import { collectPaths, copyOne, verifyOne, migrateBlogData, type FileResult } from '~~/server/utils/cdnMigration'

/**
 * Copies or verifies one batch. The dashboard page calls this repeatedly with
 * a moving offset so a slow batch never times the function out.
 *
 * mode "copy"   — copy anything not already in the new zone
 * mode "verify" — only check that each file answers through the new CDN
 */
export default defineEventHandler(async (event) => {
  if (!isAdminRequest(event)) throw createError({ statusCode: 401, statusMessage: 'Unauthorized' })
  const body = await readBody<{ offset?: number, limit?: number, force?: boolean, mode?: 'copy' | 'verify' | 'blog' }>(event) || {}
  const offset = Math.max(0, Number(body.offset) || 0)
  const mode = body.mode === 'verify' ? 'verify' : (body.mode === 'blog' ? 'blog' : 'copy')

  if (mode === 'blog') {
    const results = await migrateBlogData()
    return {
      mode, total: results.length, offset: 0, processed: results.length,
      nextOffset: results.length, done: true,
      copied: results.filter(r => r.status === 'copied').length,
      exists: 0, verified: 0,
      failed: results.filter(r => r.status === 'failed'),
      results
    }
  }
  const limit = Math.min(50, Math.max(1, Number(body.limit) || (mode === 'verify' ? 25 : 10)))
  const force = body.force === true

  const paths = await collectPaths()
  const slice = paths.slice(offset, offset + limit)

  const results: FileResult[] = []
  for (const path of slice) {
    results.push(mode === 'verify' ? await verifyOne(path) : await copyOne(path, force))
  }

  return {
    mode,
    total: paths.length,
    offset,
    processed: slice.length,
    nextOffset: offset + slice.length,
    done: offset + slice.length >= paths.length,
    copied: results.filter(r => r.status === 'copied').length,
    exists: results.filter(r => r.status === 'exists').length,
    verified: results.filter(r => r.status === 'verified').length,
    failed: results.filter(r => r.status === 'failed'),
    results
  }
})
