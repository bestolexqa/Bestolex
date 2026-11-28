import { QUOTE_STORE } from '~/composables/useQuoteCart'

// Restore the quote request after hydration, so the first client render matches the server (empty cart).
export default defineNuxtPlugin((nuxtApp) => {
  nuxtApp.hook('app:mounted', () => {
    const items = useState<any[]>('quote-cart', () => [])
    try {
      const saved = JSON.parse(localStorage.getItem(QUOTE_STORE) || '[]')
      if (Array.isArray(saved) && saved.length) items.value = saved.filter(x => x && x.key && x.model)
    } catch { /* storage unavailable: the request lives for this visit only */ }
  })
})
