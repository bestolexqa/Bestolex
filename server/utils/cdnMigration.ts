/**
 * Helpers for the one-off migration of Bunny files from the old developer
 * storage zone to the company's own zone.
 *
 * Reads come from the OLD pull zone, which is public, so the old storage key
 * is never needed here. Writes use BUNNY_NEW_STORAGE_KEY only.
 */
import bundledPaths from '~~/server/assets/cdn-migration-paths.json'
import { getStoredArticles } from '~~/server/utils/blogStorage'

export const OLD_CDN_HOST = 'electrocreative-cdn.b-cdn.net'
export const NEW_STORAGE_ZONE = process.env.BUNNY_NEW_STORAGE_ZONE || 'bestolex-products'
export const NEW_CDN_HOST = process.env.BUNNY_NEW_CDN_HOST || 'cdn.bestolex.com'
const STORAGE_BASE = process.env.BUNNY_STORAGE_BASE_URL || 'https://storage.bunnycdn.com'

const PATH_RE = new RegExp(`https?://${OLD_CDN_HOST.replace(/\./g, '\\.')}/([^"'\\\\ )<>]+)`, 'g')

function clean(raw: string): string | null {
  const path = raw.split(/[?#]/)[0].replace(/\\u002F/gi, '/').replace(/^\/+/, '')
  if (!path || path.endsWith('/')) return null
  const last = path.split('/').pop() || ''
  return last.includes('.') ? path : null
}

/** Paths referenced in the repository plus any extra ones in the live articles. */
export async function collectPaths(): Promise<string[]> {
  const set = new Set<string>()
  for (const p of bundledPaths as string[]) {
    const c = clean(p)
    if (c) set.add(c)
  }
  try {
    const articles = await getStoredArticles()
    const text = JSON.stringify(articles)
    for (const m of text.matchAll(PATH_RE)) {
      const c = clean(m[1])
      if (c) set.add(c)
    }
  } catch {
    // live articles unavailable: the bundled list still covers the site itself
  }
  return [...set].sort()
}

export type FileResult = { path: string, status: 'copied' | 'exists' | 'failed' | 'verified', bytes?: number, detail?: string }

/**
 * Bunny Storage answers GET but not HEAD, so presence is checked with a
 * one-byte ranged GET rather than a HEAD request.
 */
async function existsInNewZone(path: string, key: string): Promise<boolean> {
  try {
    const res = await fetch(`${STORAGE_BASE}/${NEW_STORAGE_ZONE}/${path}`, {
      headers: { AccessKey: key, Range: 'bytes=0-0' }
    })
    await res.arrayBuffer().catch(() => undefined)
    return res.status === 200 || res.status === 206
  } catch {
    return false
  }
}

/** Checks the file as a visitor would see it, through the new CDN hostname. */
export async function verifyOne(path: string): Promise<FileResult> {
  try {
    const res = await fetch(`https://${NEW_CDN_HOST}/${encodeURI(path)}`, { headers: { Range: 'bytes=0-0' } })
    await res.arrayBuffer().catch(() => undefined)
    if (res.status === 200 || res.status === 206) return { path, status: 'verified' }
    return { path, status: 'failed', detail: `cdn ${res.status}` }
  } catch (e: any) {
    return { path, status: 'failed', detail: `cdn error: ${e?.message || e}` }
  }
}

/** Copies one file, unless it is already in the new zone. */
export async function copyOne(path: string, force = false): Promise<FileResult> {
  const target = `${STORAGE_BASE}/${NEW_STORAGE_ZONE}/${path}`
  const key = process.env.BUNNY_NEW_STORAGE_KEY || ''
  if (!key) return { path, status: 'failed', detail: 'BUNNY_NEW_STORAGE_KEY is not set' }

  if (!force && await existsInNewZone(path, key)) return { path, status: 'exists' }

  let body: ArrayBuffer
  try {
    const src = await fetch(`https://${OLD_CDN_HOST}/${path}`)
    if (!src.ok) return { path, status: 'failed', detail: `source ${src.status}` }
    body = await src.arrayBuffer()
  } catch (e: any) {
    return { path, status: 'failed', detail: `source error: ${e?.message || e}` }
  }
  if (!body.byteLength) return { path, status: 'failed', detail: 'source is empty' }

  try {
    const put = await fetch(target, {
      method: 'PUT',
      headers: { AccessKey: key, 'Content-Type': 'application/octet-stream' },
      body
    })
    if (!put.ok) return { path, status: 'failed', detail: `upload ${put.status}` }
  } catch (e: any) {
    return { path, status: 'failed', detail: `upload error: ${e?.message || e}` }
  }
  return { path, status: 'copied', bytes: body.byteLength }
}
