import fs from 'node:fs'
import path from 'node:path'
import defaultArticles from '~~/data/articles.json'
import defaultCategories from '~~/data/categories.json'
import { useServerSupabase } from './supabase'

const BUNNY_STORAGE_ACCESS_KEY = process.env.BUNNY_STORAGE_ACCESS_KEY || ''
const BUNNY_STORAGE_ZONE = process.env.BUNNY_STORAGE_ZONE_NAME || 'electrocreative-zone'
const BUNNY_PULL_ZONE = process.env.BUNNY_PULL_ZONE_URL || 'electrocreative-cdn.b-cdn.net'

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

// ---------------- ARTICLES ----------------

export async function getStoredArticles(): Promise<any[]> {
  const supabase = useServerSupabase()

  // 1. Try Supabase
  if (supabase) {
    try {
      const { data, error } = await supabase
        .from('articles')
        .select('*')
        .order('created_at', { ascending: false })

      if (!error && data && data.length > 0) {
        return data.map((item: any) => ({
          id: item.id || item.slug,
          slug: item.slug,
          title: { ar: item.title_ar, en: item.title_en || item.title_ar },
          category: { ar: item.category_ar, en: item.category_en || item.category_ar },
          excerpt: { ar: item.excerpt_ar, en: item.excerpt_en || item.excerpt_ar },
          desc: { ar: item.excerpt_ar || item.title_ar, en: item.excerpt_en || item.title_en },
          content: { ar: item.content_ar, en: item.content_en || item.content_ar },
          image: item.image || 'https://electrocreative-cdn.b-cdn.net/bestolex/news/news1.jpg',
          date: item.created_at ? item.created_at.split('T')[0] : '2026-08-15',
          readTime: { ar: item.read_time_ar || '5 دقائق قراءة', en: item.read_time_en || '5 min read' },
          read_time_ar: item.read_time_ar,
          read_time_en: item.read_time_en,
          isPublished: item.is_published,
          is_featured: !!item.is_featured
        }))
      }
    } catch (e) {
      // Supabase unavailable, continue
    }
  }

  // 2. Try Bunny Storage CDN
  const bunnyArticles = await readFromBunny('data/articles.json')
  if (bunnyArticles) {
    return bunnyArticles
  }

  // 3. Try Local filesystem (e.g. during local dev)
  try {
    const localPath = path.resolve(process.cwd(), 'data/articles.json')
    if (fs.existsSync(localPath)) {
      const raw = fs.readFileSync(localPath, 'utf-8')
      const parsed = JSON.parse(raw)
      if (Array.isArray(parsed) && parsed.length > 0) {
        return parsed
      }
    }
  } catch (err) {}

  // 4. Guaranteed bundled fallback
  return defaultArticles || []
}

export async function saveStoredArticles(articles: any[]): Promise<boolean> {
  const supabase = useServerSupabase()

  // 1. Try Bunny Storage (Always persistent across Vercel serverless)
  await writeToBunny('data/articles.json', articles)

  // 2. Try Local filesystem write (if writable)
  try {
    const localPath = path.resolve(process.cwd(), 'data/articles.json')
    fs.writeFileSync(localPath, JSON.stringify(articles, null, 2), 'utf-8')
  } catch (err) {
    // Read-only filesystem on serverless is expected
  }

  return true
}

// ---------------- CATEGORIES ----------------

export async function getStoredCategories(): Promise<any[]> {
  const supabase = useServerSupabase()

  // 1. Try Supabase
  if (supabase) {
    try {
      const { data, error } = await supabase
        .from('article_categories')
        .select('*')
        .order('created_at', { ascending: true })

      if (!error && data && data.length > 0) {
        return data
      }
    } catch (e) {
      // Supabase unavailable, continue
    }
  }

  // 2. Try Bunny Storage CDN
  const bunnyCategories = await readFromBunny('data/categories.json')
  if (bunnyCategories) {
    return bunnyCategories
  }

  // 3. Try Local filesystem
  try {
    const localPath = path.resolve(process.cwd(), 'data/categories.json')
    if (fs.existsSync(localPath)) {
      const raw = fs.readFileSync(localPath, 'utf-8')
      const parsed = JSON.parse(raw)
      if (Array.isArray(parsed) && parsed.length > 0) {
        return parsed
      }
    }
  } catch (err) {}

  // 4. Guaranteed bundled fallback
  return defaultCategories || []
}

export async function saveStoredCategories(categories: any[]): Promise<boolean> {
  // 1. Try Bunny Storage
  await writeToBunny('data/categories.json', categories)

  // 2. Try Local filesystem write
  try {
    const localPath = path.resolve(process.cwd(), 'data/categories.json')
    fs.writeFileSync(localPath, JSON.stringify(categories, null, 2), 'utf-8')
  } catch (err) {}

  return true
}
