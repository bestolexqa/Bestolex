/**
 * Moves the product images, technical drawings and brochures that still load
 * from sabtech.com.sa onto the company's own Bunny zone, so no product page
 * depends on the manufacturer's website staying up or keeping its file paths.
 *
 * The source → destination list is fixed in server/assets/sabtech-rehost-map.json,
 * generated from data/products.json, so this endpoint and the repository data
 * agree on every path without either side recomputing names.
 *
 * Reads are plain public GETs from sabtech.com.sa. Writes use
 * BUNNY_NEW_STORAGE_KEY only; no other credential is involved.
 */
import rehostMap from '~~/server/assets/sabtech-rehost-map.json'

export type RehostAsset = { product: string, source: string, path: string }
export type RehostResult = RehostAsset & {
  status: 'copied' | 'exists' | 'verified' | 'failed'
  bytes?: number
  detail?: string
  url?: string
}

export const NEW_STORAGE_ZONE = process.env.BUNNY_NEW_STORAGE_ZONE || 'bestolex-products'
export const NEW_CDN_HOST = process.env.BUNNY_NEW_CDN_HOST || 'cdn.bestolex.com'
const STORAGE_BASE = process.env.BUNNY_STORAGE_BASE_URL || 'https://storage.bunnycdn.com'

export function assets(): RehostAsset[] {
  return rehostMap as RehostAsset[]
}

export function cdnUrl(path: string): string {
  return `https://${NEW_CDN_HOST}/${path}`
}

function contentType(path: string): string {
  const ext = path.split('.').pop()?.toLowerCase()
  if (ext === 'pdf') return 'application/pdf'
  if (ext === 'png') return 'image/png'
  if (ext === 'jpg' || ext === 'jpeg') return 'image/jpeg'
  if (ext === 'webp') return 'image/webp'
  if (ext === 'gif') return 'image/gif'
  return 'application/octet-stream'
}

/** Bunny Storage answers GET but not HEAD, so a one-byte ranged GET stands in. */
async function existsInZone(path: string, key: string): Promise<boolean> {
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

/** Checks the file as a visitor would see it, through the CDN hostname. */
export async function verifyOne(a: RehostAsset): Promise<RehostResult> {
  try {
    const res = await fetch(cdnUrl(encodeURI(a.path)), { headers: { Range: 'bytes=0-0' } })
    await res.arrayBuffer().catch(() => undefined)
    if (res.status === 200 || res.status === 206) return { ...a, status: 'verified', url: cdnUrl(a.path) }
    return { ...a, status: 'failed', detail: `cdn ${res.status}` }
  } catch (e: any) {
    return { ...a, status: 'failed', detail: `cdn error: ${e?.message || e}` }
  }
}

export async function copyOne(a: RehostAsset, force = false): Promise<RehostResult> {
  const key = process.env.BUNNY_NEW_STORAGE_KEY || ''
  if (!key) return { ...a, status: 'failed', detail: 'BUNNY_NEW_STORAGE_KEY is not set' }

  if (!force && await existsInZone(a.path, key)) {
    return { ...a, status: 'exists', url: cdnUrl(a.path) }
  }

  let body: ArrayBuffer
  try {
    const src = await fetch(a.source, {
      headers: { 'User-Agent': 'Mozilla/5.0 (compatible; BestolexAssetMigration/1.0)' }
    })
    if (!src.ok) return { ...a, status: 'failed', detail: `source ${src.status}` }
    body = await src.arrayBuffer()
  } catch (e: any) {
    return { ...a, status: 'failed', detail: `source error: ${e?.message || e}` }
  }
  if (!body.byteLength) return { ...a, status: 'failed', detail: 'source is empty' }

  try {
    const put = await fetch(`${STORAGE_BASE}/${NEW_STORAGE_ZONE}/${a.path}`, {
      method: 'PUT',
      headers: { AccessKey: key, 'Content-Type': contentType(a.path) },
      body
    })
    if (!put.ok) return { ...a, status: 'failed', detail: `upload ${put.status}` }
  } catch (e: any) {
    return { ...a, status: 'failed', detail: `upload error: ${e?.message || e}` }
  }
  return { ...a, status: 'copied', bytes: body.byteLength, url: cdnUrl(a.path) }
}
