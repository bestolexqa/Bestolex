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
import { createHash } from 'node:crypto'
import rehostMap from '~~/server/assets/sabtech-rehost-map.json'
import withdrawnMap from '~~/server/assets/sabtech-withdrawn.json'

export type RehostAsset = { product: string, source: string, path: string }
export type RehostResult = RehostAsset & {
  status: 'copied' | 'exists' | 'verified' | 'deleted' | 'absent' | 'failed'
  bytes?: number
  detail?: string
  url?: string
}

// blogStorage.ts reads BUNNY_STORAGE_ZONE_NAME for the same zone; both are
// accepted here so a missing variable cannot write to a different zone.
export const SABTECH_STORAGE_ZONE = process.env.BUNNY_NEW_STORAGE_ZONE || process.env.BUNNY_STORAGE_ZONE_NAME || 'bestolex-products'
export const SABTECH_CDN_HOST = process.env.BUNNY_NEW_CDN_HOST || 'cdn.bestolex.com'
const STORAGE_BASE = process.env.BUNNY_STORAGE_BASE_URL || 'https://storage.bunnycdn.com'

export function assets(): RehostAsset[] {
  return rehostMap as RehostAsset[]
}

/**
 * SAB TECH's own documents: brochures, datasheets and the crash-test
 * certificates. The owner's rule is that no SAB TECH catalogue is hosted by us
 * or attached to a product, and on 26 Nov he ruled the two certificates out of
 * publication as well, so these are kept here as the list to delete from the
 * zone and never to copy again - not in assets(). The compliance claim itself
 * stays on the product page (rating, model, certificate number, lab); only the
 * document is withheld, and a copy goes out with the technical proposal.
 */
export function withdrawn(): RehostAsset[] {
  return withdrawnMap as RehostAsset[]
}

export function cdnUrl(path: string): string {
  return `https://${SABTECH_CDN_HOST}/${path}`
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
    const res = await fetch(`${STORAGE_BASE}/${SABTECH_STORAGE_ZONE}/${encodeURI(path)}`, {
      headers: { AccessKey: key, Range: 'bytes=0-0' },
      signal: AbortSignal.timeout(15000)
    })
    await res.arrayBuffer().catch(() => undefined)
    return res.status === 200 || res.status === 206
  } catch {
    return false
  }
}

/** Checks the file as a visitor would see it, through the CDN hostname. */
export async function verifySabtechOne(a: RehostAsset): Promise<RehostResult> {
  try {
    const res = await fetch(cdnUrl(encodeURI(a.path)), { headers: { Range: 'bytes=0-0' }, signal: AbortSignal.timeout(15000) })
    await res.arrayBuffer().catch(() => undefined)
    if (res.status === 200 || res.status === 206) return { ...a, status: 'verified', url: cdnUrl(a.path) }
    return { ...a, status: 'failed', detail: `cdn ${res.status}` }
  } catch (e: any) {
    return { ...a, status: 'failed', detail: `cdn error: ${e?.message || e}` }
  }
}

export async function copySabtechOne(a: RehostAsset, force = false): Promise<RehostResult> {
  const key = process.env.BUNNY_NEW_STORAGE_KEY || ''
  if (!key) return { ...a, status: 'failed', detail: 'BUNNY_NEW_STORAGE_KEY is not set' }

  if (!force && await existsInZone(a.path, key)) {
    return { ...a, status: 'exists', url: cdnUrl(a.path) }
  }

  let body: ArrayBuffer
  let declared = 0
  try {
    const src = await fetch(a.source, {
      headers: { 'User-Agent': 'Mozilla/5.0 (compatible; BestolexAssetMigration/1.0)' },
      signal: AbortSignal.timeout(15000)
    })
    if (!src.ok) return { ...a, status: 'failed', detail: `source ${src.status}` }
    const type = (src.headers.get('content-type') || '').toLowerCase()
    if (type.startsWith('text/html')) {
      return { ...a, status: 'failed', detail: 'source answered an HTML page, not the file' }
    }
    declared = Number(src.headers.get('content-length') || 0)
    body = await src.arrayBuffer()
  } catch (e: any) {
    return { ...a, status: 'failed', detail: `source error: ${e?.message || e}` }
  }
  if (!body.byteLength) return { ...a, status: 'failed', detail: 'source is empty' }
  // A cut-off download answers 200 with a short body. Without this check it is
  // written to the zone and then reads back as 'exists' and 'verified' for ever.
  if (declared && body.byteLength !== declared) {
    return { ...a, status: 'failed', detail: `short download ${body.byteLength}/${declared} bytes` }
  }

  // Bunny compares this digest against what it received and rejects a mismatch,
  // so the integrity check happens at the storage end, not only here.
  const checksum = createHash('sha256').update(Buffer.from(body)).digest('hex').toUpperCase()
  try {
    const put = await fetch(`${STORAGE_BASE}/${SABTECH_STORAGE_ZONE}/${encodeURI(a.path)}`, {
      method: 'PUT',
      headers: { AccessKey: key, 'Content-Type': contentType(a.path), Checksum: checksum },
      body,
      signal: AbortSignal.timeout(60000)
    })
    if (!put.ok) return { ...a, status: 'failed', detail: `upload ${put.status}` }
  } catch (e: any) {
    return { ...a, status: 'failed', detail: `upload error: ${e?.message || e}` }
  }
  return { ...a, status: 'copied', bytes: body.byteLength, url: cdnUrl(a.path) }
}

/** Removes a withdrawn file from the zone. A file already gone counts as done. */
export async function deleteSabtechOne(a: RehostAsset): Promise<RehostResult> {
  const key = process.env.BUNNY_NEW_STORAGE_KEY || ''
  if (!key) return { ...a, status: 'failed', detail: 'BUNNY_NEW_STORAGE_KEY is not set' }
  try {
    const res = await fetch(`${STORAGE_BASE}/${SABTECH_STORAGE_ZONE}/${encodeURI(a.path)}`, {
      method: 'DELETE',
      headers: { AccessKey: key },
      signal: AbortSignal.timeout(15000)
    })
    await res.arrayBuffer().catch(() => undefined)
    if (res.ok) return { ...a, status: 'deleted' }
    if (res.status === 404) return { ...a, status: 'absent' }
    return { ...a, status: 'failed', detail: `delete ${res.status}` }
  } catch (e: any) {
    return { ...a, status: 'failed', detail: `delete error: ${e?.message || e}` }
  }
}
