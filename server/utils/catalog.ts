// Product data lives in data/products.json, which only the server reads. Pages get what they show
// through /api/catalog/* (nav, category, product), so the browser no longer downloads the whole
// catalogue (805 KB on 27 Nov 2026, and the gold-mining section would multiply it).
import productCategories from '~~/data/products.json'

type Loc = { ar?: string, en?: string }
export const catalog = productCategories as any[]

export const catProducts = (c: any): any[] =>
  [...(c.products || []), ...((c.subcategories || []).flatMap((s: any) => s.products || []))]

const navProduct = (p: any) => ({ id: p.id, name: p.name })

const cut = (s?: string, n = 240) => {
  if (!s) return s
  const t = s.replace(/\s+/g, ' ').trim()
  return t.length > n ? `${t.slice(0, n).replace(/\s+\S*$/, '')}…` : t
}
const snippet = (d?: Loc) => (d ? { ar: cut(d.ar), en: cut(d.en) } : undefined)

export const cardProduct = (p: any) => ({
  id: p.id,
  name: p.name,
  image: p.image,
  cardImage: p.cardImage,
  coverImage: p.coverImage,
  images: (p.images || []).slice(0, 1),
  description: snippet(p.description)
})

// Header, footer, home, contact, error page: ids, titles and product names only.
export const navTree = () => catalog.map(c => ({
  id: c.id,
  title: c.title,
  description: c.description,
  image: c.image,
  subcategories: (c.subcategories || []).map((s: any) => ({ id: s.id, title: s.title, products: (s.products || []).map(navProduct) })),
  products: (c.products || []).map(navProduct)
}))

// Category page: the category with product cards (short descriptions).
export const categoryView = (id: string) => {
  const c = catalog.find(x => x.id === id)
  if (!c) return null
  const { products, subcategories, ...rest } = c
  return {
    ...rest,
    subcategories: (subcategories || []).map((s: any) => ({ ...s, products: (s.products || []).map(cardProduct) })),
    products: (products || []).map(cardProduct)
  }
}

// Product page: the product, its category and up to four related products (same subcategory first).
export const productView = (id: string) => {
  for (const c of catalog) {
    const all = catProducts(c)
    const p = all.find(x => x.id === id)
    if (!p) continue
    const sub = (c.subcategories || []).find((s: any) => (s.products || []).some((x: any) => x.id === id))
    const own = (sub?.products || []).filter((x: any) => x.id !== id)
    const rest = all.filter(x => x.id !== id && !own.includes(x))
    return {
      product: p,
      category: { id: c.id, title: c.title },
      related: [...own, ...rest].slice(0, 4).map(cardProduct)
    }
  }
  return null
}
