// Model tables for product families (doors, the solar pages, then the generator pages). The data lives in
// server/assets/catalog/<group>/<id>.json so it never ships in the client
// bundle: a page fetches only the family it shows.
const FAMILY_FILES: Record<string, string> = {
  'high-speed-doors': 'catalog/doors/high-speed-doors.json',
  'industrial-sectional-doors': 'catalog/doors/industrial-sectional-doors.json',
  'industrial-shutters': 'catalog/doors/industrial-shutters.json',
  'solar-panels': 'catalog/solar/solar-panels.json',
  'solar-lighting': 'catalog/solar/solar-lighting.json',
  'solar-inverters-controllers': 'catalog/solar/solar-inverters-controllers.json',
  'solar-batteries-storage': 'catalog/solar/solar-batteries-storage.json',
  'solar-home-systems-portable': 'catalog/solar/solar-home-systems-portable.json',
  'solar-mounting-cables-protection': 'catalog/solar/solar-mounting-cables-protection.json',
  'solar-commercial-industrial': 'catalog/solar/solar-commercial-industrial.json',
  'solar-appliances': 'catalog/solar/solar-appliances.json',
  'diesel-generator-sets': 'catalog/generators/diesel-generator-sets.json',
  'generator-sets-by-engine': 'catalog/generators/generator-sets-by-engine.json',
  'gas-generators-alternators': 'catalog/generators/gas-generators-alternators.json',
  'portable-generators': 'catalog/generators/portable-generators.json',
  'diesel-petrol-engines': 'catalog/generators/diesel-petrol-engines.json',
  'generator-controls-load-banks': 'catalog/generators/generator-controls-load-banks.json'
}

const cache = new Map<string, any>()

export default defineEventHandler(async (event) => {
  const id = String(getRouterParam(event, 'id') || '')
  const key = Object.hasOwn(FAMILY_FILES, id) ? FAMILY_FILES[id] : undefined
  if (!key) throw createError({ statusCode: 404, statusMessage: 'Family not found' })

  if (!cache.has(id)) {
    let item: any = await useStorage('assets:server').getItem(key)
    if (typeof item === 'string') {
      try { item = JSON.parse(item) } catch { item = null }
    }
    if (!item || !Array.isArray(item.types)) {
      throw createError({ statusCode: 500, statusMessage: 'Family data unreadable' })
    }
    // `_internal` holds maker codes and source links for our records only.
    const strip = (m: any) => { const { _internal, ...rest } = m; return rest }
    cache.set(id, { ...item, types: item.types.map((t: any) => ({ ...t, models: (t.models || []).map(strip) })) })
  }

  setResponseHeader(event, 'Cache-Control', 'public, max-age=300, s-maxage=3600')
  return cache.get(id)
})
