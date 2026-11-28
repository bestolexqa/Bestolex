// Anchor of a model row in a gold-mining family table (search results link to it).
export const rowId = (code: string, model: string) =>
  `m-${`${code}-${model}`.toLowerCase().normalize('NFKD').replace(/×/g, 'x').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '')}`

// Gold mining has its own section page; every other category keeps /products/category/<id>.
export const categoryPath = (id: string) => (id === 'gold-mining' ? '/gold-mining' : `/products/category/${id}`)
