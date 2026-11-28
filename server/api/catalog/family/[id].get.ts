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
  'generator-controls-load-banks': 'catalog/generators/generator-controls-load-banks.json',
  'geophysical-survey-instruments': 'catalog/mining/geophysical-survey-instruments.json',
  'metal-detectors-water-well-drill-rigs': 'catalog/mining/metal-detectors-water-well-drill-rigs.json',
  'core-rc-exploration-drill-rigs': 'catalog/mining/core-rc-exploration-drill-rigs.json',
  'air-leg-rock-drills': 'catalog/mining/air-leg-rock-drills.json',
  'hand-held-gasoline-rock-drills': 'catalog/mining/hand-held-gasoline-rock-drills.json',
  'dth-water-well-drill-rigs': 'catalog/mining/dth-water-well-drill-rigs.json',
  'diesel-air-compressors': 'catalog/mining/diesel-air-compressors.json',
  'pneumatic-picks-wedges-cracking-mortar': 'catalog/mining/pneumatic-picks-wedges-cracking-mortar.json',
  'paving-breakers-electric-hammers-hydraulic-power-packs': 'catalog/mining/paving-breakers-electric-hammers-hydraulic-power-packs.json',
  'hydraulic-rock-splitters': 'catalog/mining/hydraulic-rock-splitters.json',
  'line-drilling-machines-compact-dth-drillers': 'catalog/mining/line-drilling-machines-compact-dth-drillers.json',
  'diamond-wire-saws': 'catalog/mining/diamond-wire-saws.json',
  'block-pushing-handling': 'catalog/mining/block-pushing-handling.json',
  'mine-ventilation-fans-ground-support-mesh': 'catalog/mining/mine-ventilation-fans-ground-support-mesh.json',
  'dth-hammers-bits': 'catalog/mining/dth-hammers-bits.json',
  'high-pressure-dth-bits': 'catalog/mining/high-pressure-dth-bits.json',
  'low-medium-pressure-dth-tools': 'catalog/mining/low-medium-pressure-dth-tools.json',
  'overburden-casing-systems': 'catalog/mining/overburden-casing-systems.json',
  'dth-pipes-back-hammers-breakout-benches': 'catalog/mining/dth-pipes-back-hammers-breakout-benches.json',
  'reverse-circulation-rc-tools': 'catalog/mining/reverse-circulation-rc-tools.json',
  'tricone-pdc-core-drilling-tools': 'catalog/mining/tricone-pdc-core-drilling-tools.json',
  'tapered-threaded-drilling-tools': 'catalog/mining/tapered-threaded-drilling-tools.json',
  'button-bit-grinders': 'catalog/mining/button-bit-grinders.json',
  'cutter-picks-additional-cir-hammers': 'catalog/mining/cutter-picks-additional-cir-hammers.json',
  'jaw-crushers': 'catalog/mining/jaw-crushers.json',
  'gyratory-impact-crushers': 'catalog/mining/gyratory-impact-crushers.json',
  'c-series-jaw-gyratory-impact-crushers': 'catalog/mining/c-series-jaw-gyratory-impact-crushers.json',
  'hydraulic-cone-crushers': 'catalog/mining/hydraulic-cone-crushers.json',
  'single-cylinder-cone-crushers': 'catalog/mining/single-cylinder-cone-crushers.json',
  'symons-spring-cone-crushers': 'catalog/mining/symons-spring-cone-crushers.json',
  'gp-hps-hydraulic-cone-crushers': 'catalog/mining/gp-hps-hydraulic-cone-crushers.json',
  'vertical-shaft-impact-crushers': 'catalog/mining/vertical-shaft-impact-crushers.json',
  'sand-makers-fine-crushers': 'catalog/mining/sand-makers-fine-crushers.json',
  'hammer-crushers': 'catalog/mining/hammer-crushers.json',
  'fine-double-rotor-crushers': 'catalog/mining/fine-double-rotor-crushers.json',
  'impact-fine-crushers': 'catalog/mining/impact-fine-crushers.json',
  'roller-crushers': 'catalog/mining/roller-crushers.json',
  'mobile-crushing-plants': 'catalog/mining/mobile-crushing-plants.json',
  'tyre-crawler-mounted-crushing-plants': 'catalog/mining/tyre-crawler-mounted-crushing-plants.json',
  'induction-gold-smelting-furnaces': 'catalog/mining/induction-gold-smelting-furnaces.json',
  'gold-melting-furnaces': 'catalog/mining/gold-melting-furnaces.json',
  'firebricks-electrodes-induction-units': 'catalog/mining/firebricks-electrodes-induction-units.json',
  'fused-quartz-silicon-carbide-crucibles': 'catalog/mining/fused-quartz-silicon-carbide-crucibles.json',
  'refractories-quartz-glass-ceramics': 'catalog/mining/refractories-quartz-glass-ceramics.json',
  'ceramic-fibre-furnace-insulation': 'catalog/mining/ceramic-fibre-furnace-insulation.json'
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
