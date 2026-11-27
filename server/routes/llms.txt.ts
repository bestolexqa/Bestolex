import productCategories from '~~/data/products.json'
import { getCachedArticles } from '~~/server/utils/blogStorage'
import { withRepoArticles } from '~~/server/utils/repoArticles'
import { BUSINESS, SITE_URL } from '~~/utils/seo'

// GET /llms.txt — a short Markdown map of the site for AI assistants and agents (https://llmstxt.org).
// Built from the same data as the pages, so it never drifts from the site. Google Search does not use it;
// it is a convenience for other assistants and agentic browsers.

const clean = (s: string) => (s || '').replace(/\s+/g, ' ').trim()

export default defineEventHandler(async (event) => {
  const lines: string[] = []
  lines.push(`# ${BUSINESS.legalNameEn} (Bestolex / بيستوليكس)`)
  lines.push('')
  lines.push(`> ${BUSINESS.descriptionEn}`)
  lines.push('')
  lines.push('Key facts:')
  lines.push(`- Arabic name: ${BUSINESS.legalNameAr}`)
  lines.push('- Exclusive agent of SAB TECH (also written SABTECH) products in Qatar. Core lines: loading and warehouse systems, waste and recycling, perimeter protection, industrial doors. Heavy equipment is supplied on request.')
  lines.push('- Services: site survey and requirements study, technical and commercial offer, supply and logistics, installation or technical supervision, testing and commissioning, operator training, preventive and corrective maintenance, spare parts and after-sales service.')
  lines.push(`- Phone and WhatsApp: ${BUSINESS.phonePrimary} (primary), ${BUSINESS.phoneSecondary}. Email: ${BUSINESS.email}`)
  lines.push('- Address: Al Muntazah, Zone 24, Street 830, Building 16, Floor 7, Office 714, Doha, Qatar. Hours: 07:00–18:00, Sunday–Thursday and Saturday.')
  lines.push('- Prices are not published; quotes are given on request after the requirements are known.')
  lines.push('- Sourcing on request (procurement on the customer\'s behalf): Bestolex sources and supplies any machine, equipment, device, production line or spare part that is not in its own product sections, for any activity in Qatar (construction and scaffolding, spare parts, pumps and compressors, metalwork and welding, restaurants and hotels, printing, agriculture, tailoring, carpentry, production lines, cleaning, garages, laboratories), from factories worldwide, with shipping, customs clearance, installation, training and maintenance. Details and request form: '+SITE_URL+'/en/sourcing')
  lines.push('- Authorised distributor for many international manufacturers and companies. Also: solar energy systems for Qatar, the Middle East and Africa; gold-mining and energy equipment for projects in the Middle East and Africa, covering the whole gold-mining chain from one supplier (exploration and drilling, crushing and grinding, washing and concentration, processing plants, pumps, smelting and refining, laboratory, fleet support, safety and site supplies).')
  lines.push('- 25+ years of experience, ISO 9001 and CE marking belong to SAB TECH, the manufacturing partner, not to Bestolex. Crash-test ratings (PAS 68, IWA 14-1, ASTM F2656) apply only to specific models backed by an official test certificate.')
  lines.push('- The site is in Arabic (default, no prefix) and English (/en).')
  lines.push('')

  lines.push('## Product categories')
  lines.push('')
  for (const c of productCategories as any[]) {
    const desc = clean(c.seo?.description?.en || c.description?.en || '')
    lines.push(`- [${c.title?.en}](${SITE_URL}/en/products/category/${c.id}): ${desc}`)
  }
  lines.push('')

  lines.push('## Products')
  lines.push('')
  const seen = new Set<string>()
  for (const c of productCategories as any[]) {
    const products = [...(c.products || []), ...((c.subcategories || []).flatMap((s: any) => s.products || []))]
    for (const p of products) {
      if (!p?.id || seen.has(p.id)) continue
      seen.add(p.id)
      const desc = clean(p.summary?.en || p.seo?.description?.en || '')
      lines.push(`- [${p.name?.en}](${SITE_URL}/en/products/${p.id}) (${c.title?.en}; Arabic: ${SITE_URL}/products/${p.id}): ${desc}`)
    }
  }
  lines.push('')

  lines.push('## Company pages')
  lines.push('')
  lines.push(`- [About Bestolex](${SITE_URL}/en/about)`)
  lines.push(`- [Sourcing on request: equipment for any activity](${SITE_URL}/en/sourcing) (Arabic: ${SITE_URL}/sourcing)`)
  lines.push(`- [Services](${SITE_URL}/en/services)`)
  lines.push(`- [Contact and location](${SITE_URL}/en/contact)`)
  lines.push(`- [Blog](${SITE_URL}/en/blog)`)
  lines.push('')

  const articles = (await withRepoArticles(await getCachedArticles().catch(() => [])) as any[])
    .filter(a => (a?.id || a?.slug) && a.isPublished !== false && a.is_published !== false)
    .slice(0, 30)
  if (articles.length) {
    lines.push('## Optional')
    lines.push('')
    for (const a of articles) {
      const id = encodeURIComponent(String(a.id || a.slug))
      const title = clean(a.title?.ar || a.title?.en || '')
      lines.push(`- [${title}](${SITE_URL}/blog/${id})`)
    }
    lines.push('')
  }

  setHeader(event, 'Content-Type', 'text/plain; charset=utf-8')
  setHeader(event, 'Cache-Control', 'public, max-age=3600, s-maxage=86400')
  return lines.join('\n')
})
