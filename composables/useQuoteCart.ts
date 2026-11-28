// Quote request ("طلب العرض"): models added from any family table, kept in the browser (localStorage) until
// the request is sent by WhatsApp or e-mail from /quote. One request can mix gold mining and energy models.
type L = { ar: string, en: string }
export type QuoteItem = {
  key: string        // code + " / " + model
  code: string
  model: string
  label?: L          // model name in both languages (series rows have Arabic names)
  familyId: string
  family: L
  section: L
  qty: number
}

export const QUOTE_STORE = 'bx-quote-v1'

export const useQuoteCart = () => {
  const items = useState<QuoteItem[]>('quote-cart', () => [])
  // Loaded from localStorage after hydration (plugins/quote-cart.client.ts), so server and client render alike.

  const save = () => {
    if (!import.meta.client) return
    try { localStorage.setItem(QUOTE_STORE, JSON.stringify(items.value)) } catch { /* ignore */ }
  }

  const has = (key: string) => items.value.some(x => x.key === key)
  const add = (it: Omit<QuoteItem, 'qty' | 'key'> & { qty?: number }) => {
    const key = `${it.code} / ${it.model}`
    if (has(key)) return
    items.value = [...items.value, { ...it, key, qty: it.qty || 1 }]
    save()
  }
  const remove = (key: string) => { items.value = items.value.filter(x => x.key !== key); save() }
  const toggle = (it: Omit<QuoteItem, 'qty' | 'key'>) => {
    const key = `${it.code} / ${it.model}`
    if (has(key)) remove(key)
    else add(it)
  }
  const setQty = (key: string, qty: number) => {
    items.value = items.value.map(x => (x.key === key ? { ...x, qty: Math.max(1, Math.min(999, Math.round(qty) || 1)) } : x))
    save()
  }
  const clear = () => { items.value = []; save() }
  const count = computed(() => items.value.length)

  return { items, count, has, add, remove, toggle, setQty, clear }
}
