import { assets, NEW_STORAGE_ZONE, NEW_CDN_HOST } from '~~/server/utils/sabtechRehost'

export default defineEventHandler(() => {
  const list = assets()
  const byKind = (prefix: string) => list.filter(a => a.path.split('/').pop()!.startsWith(prefix)).length
  return {
    total: list.length,
    zone: NEW_STORAGE_ZONE,
    cdnHost: NEW_CDN_HOST,
    keyConfigured: Boolean(process.env.BUNNY_NEW_STORAGE_KEY),
    products: new Set(list.map(a => a.product)).size,
    drawings: byKind('drawing-'),
    components: byKind('component-'),
    brochures: byKind('brochure'),
    other: list.length - byKind('drawing-') - byKind('component-') - byKind('brochure')
  }
})
