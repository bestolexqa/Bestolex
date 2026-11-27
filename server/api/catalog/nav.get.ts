export default defineEventHandler((event) => {
  setHeader(event, 'Cache-Control', 'public, max-age=300, s-maxage=3600')
  return navTree()
})
