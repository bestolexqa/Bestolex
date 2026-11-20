// Blog articles kept as JSON files in server/assets/blog/ (one file per article).
// They are published through git: a file merged into main and deployed appears on the site
// once its `publishAt` time has passed, without touching the dashboard or Bunny storage.
// The tools that write, check and illustrate these files live in tools/blog/.
//
// Dashboard articles (Bunny/Supabase) and repo articles are merged for every public reader:
// /api/blog, /api/blog/[id], /sitemap.xml and /llms.txt. Repo articles are read-only in the
// dashboard (edits go through git).

import blogRedirects from '~~/server/blog-meta/redirects.json'
import blogOverrides from '~~/server/blog-meta/overrides.json'
import { normalizeBlogCategory } from '~~/server/utils/blogCategories'

type RepoArticle = Record<string, any>

// Merged articles: the old URL answers 301 to the article it was merged into
// (server/middleware/blog-redirects.ts) and drops out of every list, the sitemap and llms.txt.
const REDIRECTS = new Map<string, string>(
  ((blogRedirects as any).redirects || []).map((r: any) => [String(r.from), String(r.to)])
)

export function blogRedirectTarget(id: string): string | undefined {
  return REDIRECTS.get(id)
}

// Metadata corrections for dashboard articles (category, SEO title, description, image alt)
// kept in git so they survive the dashboard data. Repo articles carry their own metadata.
const OVERRIDES: Record<string, any> = (blogOverrides as any).articles || {}

function withOverride(article: any): any {
  if (!article || article.source === 'repo') return article
  const o = OVERRIDES[article.id || article.slug] || {}
  const out: any = { ...article }
  // Fixed category: the override first, else the old dashboard name mapped onto the fixed list.
  const category = o.category || normalizeBlogCategory(article.category?.ar ?? article.category_ar ?? article.category)
  if (category) Object.assign(out, { category, category_ar: category.ar, category_en: category.en })
  if (o.seoTitle) out.seoTitle = o.seoTitle
  if (o.desc) Object.assign(out, { desc: o.desc, excerpt_ar: o.desc.ar, excerpt_en: o.desc.en })
  if (o.imageAlt) out.imageAlt = o.imageAlt
  return out
}

let repoArticles: RepoArticle[] | null = null

async function loadRepoArticles(): Promise<RepoArticle[]> {
  if (repoArticles) return repoArticles
  const list: RepoArticle[] = []
  try {
    const storage = useStorage('assets:server')
    const keys = (await storage.getKeys('blog')).filter((key) => key.endsWith('.json'))
    for (const key of keys) {
      let item: any = await storage.getItem(key)
      if (typeof item === 'string') {
        try { item = JSON.parse(item) } catch { item = null }
      }
      if (item && typeof item === 'object' && (item.id || item.slug) && item.title && item.content) {
        // `keyword` and `review` are working notes for the editorial pipeline, not page data.
        const { keyword, review, ...article } = item
        list.push({ ...article, id: item.id || item.slug, slug: item.slug || item.id, source: 'repo', readOnly: true })
      } else {
        console.warn(`[repoArticles] skipped ${key}: missing id, title or content`)
      }
    }
  } catch (err) {
    console.error('[repoArticles] could not read server/assets/blog:', err)
  }
  repoArticles = list
  return list
}

// Preview deployments show scheduled articles so they can be checked before they go live.
function showScheduled(): boolean {
  return process.env.VERCEL_ENV === 'preview' || process.env.NUXT_SHOW_SCHEDULED === '1'
}

export function isPublishedNow(article: RepoArticle, now = Date.now()): boolean {
  if (article.isPublished === false || article.is_published === false) return false
  if (!article.publishAt) return true
  const at = Date.parse(article.publishAt)
  return Number.isNaN(at) || at <= now
}

// Live repo articles first for the same date, then dashboard articles, newest first.
// Visitors: merged (redirected) articles are left out, and dashboard articles get their metadata
// overrides and fixed category. The signed-in dashboard (`admin: true`) sees the stored data as is.
export async function withRepoArticles(list: any[], opts: { admin?: boolean } = {}): Promise<any[]> {
  const scheduled = showScheduled()
  const repo = (await loadRepoArticles())
    .filter((a) => scheduled || isPublishedNow(a))
    .map((a) => ({ ...a }))
  const taken = new Set(repo.flatMap((a) => [a.id, a.slug]))
  const kept = (a: any) => opts.admin || (!REDIRECTS.has(a?.id) && !REDIRECTS.has(a?.slug))
  const dashboard = list.filter((a) => a && !taken.has(a?.id) && !taken.has(a?.slug) && kept(a))
  const merged = [...repo.filter(kept), ...(opts.admin ? dashboard : dashboard.map(withOverride))]
  return merged.sort((a, b) => String(b?.date || '').localeCompare(String(a?.date || '')))
}
