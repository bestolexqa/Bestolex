export default defineEventHandler((event) => {
  const id = String(getRouterParam(event, 'id') || '')
  const view = productView(id)
  if (!view) throw createError({ statusCode: 404, statusMessage: 'Product not found' })
  setHeader(event, 'Cache-Control', 'public, max-age=300, s-maxage=3600')
  return view
})
