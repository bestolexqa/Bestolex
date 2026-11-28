import { hubView, publishedCounts } from '~~/server/utils/goldMining'

export default defineEventHandler(async (event) => {
  setHeader(event, 'Cache-Control', 'public, max-age=300, s-maxage=3600')
  return hubView(await publishedCounts())
})
