import { stageView } from '~~/server/utils/goldMining'

export default defineEventHandler((event) => {
  const view = stageView(String(getRouterParam(event, 'id') || ''))
  if (!view) throw createError({ statusCode: 404, statusMessage: 'Stage not found' })
  setHeader(event, 'Cache-Control', 'public, max-age=300, s-maxage=3600')
  return view
})
