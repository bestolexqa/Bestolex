import { collectPaths, copyOne, type FileResult } from '~~/server/utils/cdnMigration'

/**
 * Copies one batch. The dashboard page calls this repeatedly with a moving
 * offset so a slow batch never times the function out.
 */
export default defineEventHandler(async (event) => {
  const body = await readBody<{ offset?: number, limit?: number, force?: boolean }>(event) || {}
  const offset = Math.max(0, Number(body.offset) || 0)
  const limit = Math.min(25, Math.max(1, Number(body.limit) || 10))
  const force = body.force === true

  const paths = await collectPaths()
  const slice = paths.slice(offset, offset + limit)

  const results: FileResult[] = []
  for (const path of slice) {
    results.push(await copyOne(path, force))
  }

  return {
    total: paths.length,
    offset,
    processed: slice.length,
    nextOffset: offset + slice.length,
    done: offset + slice.length >= paths.length,
    copied: results.filter(r => r.status === 'copied').length,
    exists: results.filter(r => r.status === 'exists').length,
    failed: results.filter(r => r.status === 'failed'),
    results
  }
})
