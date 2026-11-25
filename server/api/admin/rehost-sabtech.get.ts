import { isAdminRequest } from '~~/server/utils/adminAuth'
import { assets, withdrawn, SABTECH_STORAGE_ZONE, SABTECH_CDN_HOST } from '~~/server/utils/sabtechRehost'

export default defineEventHandler((event) => {
  // The admin guard middleware covers this; the check is repeated here so a
  // change to that allow-list cannot open the endpoint silently.
  if (!isAdminRequest(event)) throw createError({ statusCode: 401, statusMessage: 'Unauthorized' })
  const list = assets()
  const name = (p: string) => p.split('/').pop()!
  const byKind = (prefix: string) => list.filter(a => name(a.path).startsWith(prefix)).length
  const pdfs = list.filter(a => name(a.path).endsWith('.pdf')).length
  return {
    total: list.length,
    zone: SABTECH_STORAGE_ZONE,
    cdnHost: SABTECH_CDN_HOST,
    keyConfigured: Boolean(process.env.BUNNY_NEW_STORAGE_KEY),
    products: new Set(list.map(a => a.product)).size,
    drawings: byKind('drawing-'),
    components: byKind('component-'),
    withdrawnCount: withdrawn().length,
    certificates: byKind('certificate') + byKind('crash'),
    pdfs,
    images: list.length - pdfs
  }
})
