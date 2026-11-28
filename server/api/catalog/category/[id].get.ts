export default defineEventHandler((event) => {
  const id = String(getRouterParam(event, 'id') || '')
  const view = categoryView(id)
  if (!view) throw createError({ statusCode: 404, statusMessage: 'Category not found' })
  setHeader(event, 'Cache-Control', 'public, max-age=300, s-maxage=3600')
  return view
})
