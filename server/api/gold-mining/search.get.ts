import { searchMining } from '~~/server/utils/goldMining'

export default defineEventHandler(async (event) => {
  const q = String(getQuery(event).q || '').slice(0, 80)
  setHeader(event, 'Cache-Control', 'public, max-age=300, s-maxage=3600')
  return { q, hits: await searchMining(q) }
})
