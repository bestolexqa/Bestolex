import { familyContext } from '~~/server/utils/goldMining'

export default defineEventHandler((event) => {
  const ctx = familyContext(String(getRouterParam(event, 'id') || ''))
  if (!ctx) throw createError({ statusCode: 404, statusMessage: 'Not a gold-mining family' })
  setHeader(event, 'Cache-Control', 'public, max-age=300, s-maxage=3600')
  return ctx
})
