import fs from 'node:fs'
import path from 'node:path'
import defaultArticles from '~~/data/articles.json'
import defaultCategories from '~~/data/categories.json'
import { useServerSupabase } from './supabase'

const BUNNY_STORAGE_ACCESS_KEY = process.env.BUNNY_NEW_STORAGE_KEY || process.env.BUNNY_STORAGE_ACCESS_KEY || ''
const BUNNY_STORAGE_ZONE = process.env.BUNNY_STORAGE_ZONE_NAME || 'bestolex-products'
const BUNNY_PULL_ZONE = process.env.BUNNY_PULL_ZONE_URL || 'cdn.bestolex.com'

// Helper to upload a JSON string to Bunny Storage
async function writeToBunny(remoteFilePath: string, data: any): Promise<boolean> {
  try {
    const jsonString = JSON.stringify(data, null, 2)
    const url = `https://storage.bunnycdn.com/${BUNNY_STORAGE_ZONE}/${remoteFilePath}`
    const res = await fetch(url, {
      method: 'PUT',
      headers: {
        'AccessKey': BUNNY_STORAGE_ACCESS_KEY,
        'Content-Type': 'application/json'
      },
      body: jsonString
    })
    return res.ok
  } catch (err) {
    console.error(`Failed to write ${remoteFilePath} to Bunny Storage:`, err)
    return false
  }
}

// Helper to read JSON from Bunny Storage directly (instant origin, zero cache delay)
async function readFromBunny(remoteFilePath: string): Promise<any | null> {
  try {
    const url = `https://storage.bunnycdn.com/${BUNNY_STORAGE_ZONE}/${remoteFilePath}`
    const res = await fetch(url, {
      headers: {
        'AccessKey': BUNNY_STORAGE_ACCESS_KEY
      }
    })
    if (res.ok) {
      const json = await res.json()
      if (Array.isArray(json) && json.length > 0) {
        return json
      }
    }
  } catch (err) {
    // Silently fall through to local fallback
  }
  return null
}

// ---------------- READ CACHE (monitoring log, improvement 14) ----------------
// Public pages (article pages, blog list, header, sitemap) used to download the whole
// articles.json (~1.5 MB) from Bunny Storage on every request. The cached readers below keep
// the list in memory per server instance: 5 minutes when it came from Supabase or Bunny,
// 30 seconds when only a fallback copy was available, so a short Bunny outage does not pin
// old content. Admin writes keep using getStoredArticles()/getStoredCategories(), which always
// read fresh, so a save never starts from a stale copy. A save refreshes this instance's cache
// at once; other instances pick the change up within the TTL.

type ListSource = 'supabase' | 'bunny' | 'local' | 'bundled'
type LoadedList = { list: any[], source: ListSource }
type CacheName = 'articles' | 'categories'
type CacheSlot = { list: any[] | null, expires: number, generation: number, pending: Promise<any[]> | null }

const CACHE_TTL_MS = 5 * 60 * 1000
const FALLBACK_TTL_MS = 30 * 1000

const readCache: Record<CacheName, CacheSlot> = {
  articles: { list: null, expires: 0, generation: 0, pending: null },
  categories: { list: null, expires: 0, generation: 0, pending: null }
}

// Callers get their own array and item objects, so nothing they change leaks into the cache.
function copyList(list: any[]): any[] {
  return list.map((item) => (item && typeof item === 'object' ? { ...item } : item))
}

function storeInCache(name: CacheName, loaded: LoadedList) {
  const slot = readCache[name]
  const durable = loaded.source === 'supabase' || loaded.source === 'bunny'
  slot.list = copyList(loaded.list)
  slot.expires = Date.now() + (durable ? CACHE_TTL_MS : FALLBACK_TTL_MS)
}

// Called after every save: newer data wins over any read still in flight.
function afterSave(name: CacheName, list: any[], savedToBunny: boolean) {
  const slot = readCache[name]
  slot.generation++
  slot.pending = null
  if (savedToBunny) {
    storeInCache(name, { list, source: 'bunny' })
  } else {
    slot.list = null
    slot.expires = 0
  }
}

async function readThroughCache(name: CacheName, load: () => Promise<LoadedList>): Promise<any[]> {
  const slot = readCache[name]
  if (slot.list && Date.now() < slot.expires) return copyList(slot.list)

  if (!slot.pending) {
    const generation = slot.generation
    const started = Date.now()
    const pending: Promise<any[]> = load()
      .then((loaded) => {
        if (slot.generation === generation) storeInCache(name, loaded)
        console.info(`[blogStorage] ${name} cache refreshed: ${loaded.list.length} items from ${loaded.source} in ${Date.now() - started} ms`)
        return loaded.list
      })
      .finally(() => {
        if (slot.pending === pending) slot.pending = null
      })
    slot.pending = pending
  }
  return copyList(await slot.pending)
}

// Cached readers for public, read-only routes.
export function getCachedArticles(): Promise<any[]> {
  return readThroughCache('articles', loadArticles)
}

export function getCachedCategories(): Promise<any[]> {
  return readThroughCache('categories', loadCategories)
}

// ---------------- ARTICLES ----------------

// Always reads fresh (used by admin writes). Public routes use getCachedArticles().
export async function getStoredArticles(): Promise<any[]> {
  return (await loadArticles()).list
}

async function loadArticles(): Promise<LoadedList> {
  const supabase = useServerSupabase()

  // 1. Try Supabase
  if (supabase) {
    try {
      const { data, error } = await supabase
        .from('articles')
        .select('*')
        .order('created_at', { ascending: false })

      if (!error && data && data.length > 0) {
        return { source: 'supabase', list: data.map((item: any) => ({
          id: item.id || item.slug,
          slug: item.slug,
          title: { ar: item.title_ar, en: item.title_en || item.title_ar },
          category: { ar: item.category_ar, en: item.category_en || item.category_ar },
          excerpt: { ar: item.excerpt_ar, en: item.excerpt_en || item.excerpt_ar },
          desc: { ar: item.excerpt_ar || item.title_ar, en: item.excerpt_en || item.title_en },
          content: { ar: item.content_ar, en: item.content_en || item.content_ar },
          image: item.image || 'https://cdn.bestolex.com/bestolex/news/news1.jpg',
          date: item.created_at ? item.created_at.split('T')[0] : '2026-08-15',
          updatedAt: item.updated_at ? item.updated_at.split('T')[0] : undefined,
          readTime: { ar: item.read_time_ar || '5 دقائق قراءة', en: item.read_time_en || '5 min read' },
          read_time_ar: item.read_time_ar,
          read_time_en: item.read_time_en,
          isPublished: item.is_published,
          is_featured: !!item.is_featured
        })) }
      }
    } catch (e) {
      // Supabase unavailable, continue
    }
  }

  // 2. Try Bunny Storage CDN
  const bunnyArticles = await readFromBunny('data/articles.json')
  if (bunnyArticles) {
    return { source: 'bunny', list: bunnyArticles }
  }

  // 3. Try Local filesystem (e.g. during local dev)
  try {
    const localPath = path.resolve(process.cwd(), 'data/articles.json')
    if (fs.existsSync(localPath)) {
      const raw = fs.readFileSync(localPath, 'utf-8')
      const parsed = JSON.parse(raw)
      if (Array.isArray(parsed) && parsed.length > 0) {
        return { source: 'local', list: parsed }
      }
    }
  } catch (err) {}

  // 4. Guaranteed bundled fallback
  return { source: 'bundled', list: defaultArticles || [] }
}

export async function saveStoredArticles(articles: any[]): Promise<boolean> {
  const supabase = useServerSupabase()

  // 1. Try Bunny Storage (Always persistent across Vercel serverless)
  const savedToBunny = await writeToBunny('data/articles.json', articles)

  // 2. Try Local filesystem write (if writable)
  try {
    const localPath = path.resolve(process.cwd(), 'data/articles.json')
    fs.writeFileSync(localPath, JSON.stringify(articles, null, 2), 'utf-8')
  } catch (err) {
    // Read-only filesystem on serverless is expected
  }

  afterSave('articles', articles, savedToBunny)
  return true
}

// ---------------- CATEGORIES ----------------

// Always reads fresh (used by admin writes). Public routes use getCachedCategories().
export async function getStoredCategories(): Promise<any[]> {
  return (await loadCategories()).list
}

async function loadCategories(): Promise<LoadedList> {
  const supabase = useServerSupabase()

  // 1. Try Supabase
  if (supabase) {
    try {
      const { data, error } = await supabase
        .from('article_categories')
        .select('*')
        .order('created_at', { ascending: true })

      if (!error && data && data.length > 0) {
        return { source: 'supabase', list: data }
      }
    } catch (e) {
      // Supabase unavailable, continue
    }
  }

  // 2. Try Bunny Storage CDN
  const bunnyCategories = await readFromBunny('data/categories.json')
  if (bunnyCategories) {
    return { source: 'bunny', list: bunnyCategories }
  }

  // 3. Try Local filesystem
  try {
    const localPath = path.resolve(process.cwd(), 'data/categories.json')
    if (fs.existsSync(localPath)) {
      const raw = fs.readFileSync(localPath, 'utf-8')
      const parsed = JSON.parse(raw)
      if (Array.isArray(parsed) && parsed.length > 0) {
        return { source: 'local', list: parsed }
      }
    }
  } catch (err) {}

  // 4. Guaranteed bundled fallback
  return { source: 'bundled', list: defaultCategories || [] }
}

export async function saveStoredCategories(categories: any[]): Promise<boolean> {
  // 1. Try Bunny Storage
  const savedToBunny = await writeToBunny('data/categories.json', categories)

  // 2. Try Local filesystem write
  try {
    const localPath = path.resolve(process.cwd(), 'data/categories.json')
    fs.writeFileSync(localPath, JSON.stringify(categories, null, 2), 'utf-8')
  } catch (err) {}

  afterSave('categories', categories, savedToBunny)
  return true
}
