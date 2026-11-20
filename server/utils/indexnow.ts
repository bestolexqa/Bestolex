// IndexNow: tell Bing (Copilot), Yandex, Seznam, Naver and other participating engines that a URL changed,
// so new or edited pages are recrawled within hours instead of waiting for the next crawl.
// The key is public by design: it is served at /246c5833e60e424e88ca4468ee42bec1.txt to prove ownership of the host.
// Pings are sent only from production deployments and never block the request that triggered them.

export const INDEXNOW_KEY = '246c5833e60e424e88ca4468ee42bec1'
const HOST = 'www.bestolex.com'
const BASE = `https://${HOST}`

/** Absolute URLs (Arabic + English) for site paths such as "/blog/my-article". */
export function bothLocales(paths: string[]): string[] {
  return paths.flatMap((p) => {
    const clean = p.startsWith('/') ? p : `/${p}`
    return [`${BASE}${clean === '/' ? '' : clean}`, `${BASE}/en${clean === '/' ? '' : clean}`]
  })
}

export async function pingIndexNow(urls: string[]): Promise<{ sent: number, status?: number, skipped?: string }> {
  const urlList = [...new Set(urls)].filter(u => u.startsWith(BASE)).slice(0, 10000)
  if (!urlList.length) return { sent: 0, skipped: 'no urls' }
  if (process.env.VERCEL_ENV !== 'production') return { sent: 0, skipped: 'not production' }
  try {
    const res = await fetch('https://api.indexnow.org/indexnow', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json; charset=utf-8' },
      body: JSON.stringify({ host: HOST, key: INDEXNOW_KEY, keyLocation: `${BASE}/${INDEXNOW_KEY}.txt`, urlList }),
      signal: AbortSignal.timeout(8000)
    })
    console.info(`[indexnow] ${urlList.length} url(s) -> HTTP ${res.status}`)
    return { sent: urlList.length, status: res.status }
  } catch (err: any) {
    console.warn('[indexnow] ping failed:', err?.message || err)
    return { sent: 0, skipped: 'error' }
  }
}
