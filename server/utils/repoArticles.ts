// Blog articles kept as JSON files in server/assets/blog/ (one file per article).
// They are published through git: a file merged into main and deployed appears on the site
// once its `publishAt` time has passed, without touching the dashboard or Bunny storage.
// The tools that write, check and illustrate these files live in tools/blog/.
//
// Dashboard articles (Bunny/Supabase) and repo articles are merged for every public reader:
// /api/blog, /api/blog/[id], /sitemap.xml and /llms.txt. Repo articles are read-only in the
// dashboard (edits go through git).

type RepoArticle = Record<string, any>

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
export async function withRepoArticles(list: any[]): Promise<any[]> {
  const scheduled = showScheduled()
  const repo = (await loadRepoArticles())
    .filter((a) => scheduled || isPublishedNow(a))
    .map((a) => ({ ...a }))
  if (!repo.length) return list
  const taken = new Set(repo.flatMap((a) => [a.id, a.slug]))
  const merged = [...repo, ...list.filter((a) => !taken.has(a?.id) && !taken.has(a?.slug))]
  return merged.sort((a, b) => String(b?.date || '').localeCompare(String(a?.date || '')))
}
