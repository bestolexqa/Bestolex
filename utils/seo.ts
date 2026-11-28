// Shared SEO helpers: page titles and meta descriptions that are never cut mid-word,
// plus the business facts reused by every structured-data block.

export const SITE_URL = 'https://www.bestolex.com'

export const BUSINESS = {
  legalNameEn: 'Bestolex Trading of Heavy Equipment and Machinery W.L.L.',
  legalNameAr: 'بيستوليكس لتجارة الآلات والمعدات الثقيلة (ذ.م.م)',
  phonePrimary: '+974 5150 5014',
  phoneSecondary: '+974 5070 8833',
  email: 'info@bestolex.com',
  logo: `${SITE_URL}/logo.png`,
  image: 'https://cdn.bestolex.com/bestolex/about/showroom-v2.jpg',
  address: {
    '@type': 'PostalAddress',
    streetAddress: 'Al Muntazah, Zone 24, Street 830, Building 16, Floor 7, Office 714',
    postOfficeBoxNumber: '37439',
    addressLocality: 'Doha',
    addressCountry: 'QA'
  },
  // Official profiles of the same entity (schema.org sameAs). Instagram/Facebook are the links already shown
  // in the site footer; the Google Maps entry is the verified Google Business Profile (CID from the contact-page map).
  sameAs: [
    'https://maps.google.com/?cid=12312827937338030265',
    'https://www.instagram.com/bestolex',
    'https://www.facebook.com/Bestolex'
  ],
  // One-sentence entity definition reused in Organization/LocalBusiness so every engine reads the same facts.
  descriptionEn: 'Bestolex Trading of Heavy Equipment and Machinery W.L.L. is a Qatari company in Doha, the exclusive SAB TECH agent in Qatar and an authorised distributor for many international manufacturers. It supplies, installs and maintains loading and warehouse systems, waste and recycling equipment, perimeter protection and industrial doors, provides energy solutions, sources any equipment on request, and supplies gold-mining and energy equipment to the Middle East and Africa.',
  descriptionAr: 'بيستوليكس لتجارة الآلات والمعدات الثقيلة (ذ.م.م) شركة قطرية في الدوحة، والوكيل الحصري لمنتجات ساب تك في قطر، وموزّع معتمد للعديد من المصانع العالمية. تورّد وتركّب وتصون أنظمة التحميل والمستودعات ومعدات النفايات وإعادة التدوير والحماية المحيطية والأبواب الصناعية، وتقدّم حلول الطاقة، وتورّد أي معدة حسب الطلب، ومعدات تعدين الذهب والطاقة للشرق الأوسط وأفريقيا.',
  knowsAbout: [
    'Dock levelers', 'Dock shelters', 'Scissor lift tables', 'Cargo lifts',
    'Cardboard balers', 'Waste compactors', 'Recycling equipment',
    'Road blockers', 'Tyre killers', 'Automatic bollards', 'Turnstiles', 'Under vehicle surveillance systems',
    'High-speed doors', 'Industrial sectional doors',
    'Solar energy systems', 'Diesel generators', 'Hybrid energy systems',
    'Equipment sourcing and procurement', 'Gold mining equipment'
  ],
  slogan: 'Power That Drives Your Business. Trust That Lasts',
  // Open Sunday–Thursday and Saturday, 07:00–18:00 (Friday closed)
  openingHours: [
    {
      '@type': 'OpeningHoursSpecification',
      dayOfWeek: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Saturday'],
      opens: '07:00',
      closes: '18:00'
    }
  ]
}

export const ORG_ID = `${SITE_URL}/#organization`
export const WEBSITE_ID = `${SITE_URL}/#website`

const TITLE_MAX = 60
const DESC_MAX = 158

/** "<name> | <brand>" when it fits in ~60 characters, otherwise the full name alone (never truncated with "…"). */
export function seoTitle(name: string, locale: string, opts: { brand?: string } = {}): string {
  const clean = (name || '').replace(/\s+/g, ' ').trim()
  const brand = opts.brand ?? (locale === 'ar' ? 'بيستوليكس' : 'Bestolex')
  const withBrand = `${clean} | ${brand}`
  return withBrand.length <= TITLE_MAX ? withBrand : clean
}

/**
 * Meta description that ends on a complete sentence when possible, otherwise on a whole word.
 * Strips HTML and line breaks. Never adds an ellipsis.
 */
export function seoDescription(text: string, max = DESC_MAX): string {
  const clean = (text || '')
    .replace(/<[^>]+>/g, ' ')
    .replace(/&nbsp;/g, ' ')
    .replace(/\s+/g, ' ')
    .trim()
  if (clean.length <= max) return clean
  const slice = clean.slice(0, max)
  // Prefer the last full sentence (., !, ?, ؟, ؛) if it leaves a meaningful description
  const sentenceEnd = Math.max(
    slice.lastIndexOf('. '), slice.lastIndexOf('! '), slice.lastIndexOf('? '),
    slice.lastIndexOf('؟ '), slice.lastIndexOf('۔ ')
  )
  if (sentenceEnd >= 90) return slice.slice(0, sentenceEnd + 1).trim()
  const lastSpace = slice.lastIndexOf(' ')
  const cut = slice.slice(0, lastSpace > 0 ? lastSpace : max).replace(/[\s،,؛;:\-–]+$/, '')
  return `${cut}.`
}

const DESC_HARD_MAX = 170
// Words a list must not end on once it is cut ("…, tongs and." reads as broken).
const DANGLING = /[\s،,؛;:\-–]+(and|or|with|for|of|the|to|in|from|plus|مع|من|في|إلى|أو|على|حتى)$/i

/**
 * Keeps a hand-written description as written when it fits in `max` (170) characters; otherwise ends it
 * on the last complete sentence, or the last complete list item, that fits. Never adds an ellipsis.
 */
export function clampDescription(text: string, max = DESC_HARD_MAX): string {
  const clean = (text || '').replace(/\s+/g, ' ').trim()
  if (clean.length <= max) return clean
  const slice = clean.slice(0, max + 1)
  const enough = Math.min(90, Math.floor(max / 2))
  const sentenceEnd = Math.max(
    slice.lastIndexOf('. '), slice.lastIndexOf('! '), slice.lastIndexOf('? '), slice.lastIndexOf('؟ ')
  )
  if (sentenceEnd >= enough) return slice.slice(0, sentenceEnd + 1).trim()
  const lastSep = (s: string) => Math.max(s.lastIndexOf('، '), s.lastIndexOf(', '), s.lastIndexOf('؛ '), s.lastIndexOf('; '))
  let listEnd = lastSep(slice)
  // In English only the final item takes "and"; one that is followed by more items opens a nested
  // list ("and splitting, cutting and ventilation tools"), so cut before it instead.
  const prev = listEnd > 0 ? lastSep(slice.slice(0, listEnd)) : -1
  if (prev >= enough && /^and /i.test(slice.slice(prev + 2, listEnd))) listEnd = prev
  const lastSpace = slice.lastIndexOf(' ', max - 1)
  let cut = slice.slice(0, listEnd >= enough ? listEnd : (lastSpace > 0 ? lastSpace : max - 1))
  for (let i = 0; i < 3 && DANGLING.test(cut); i++) cut = cut.replace(DANGLING, '')
  return `${cut.replace(/[\s،,؛;:\-–]+$/, '')}.`
}

/** BreadcrumbList for a list of [name, absolute url] pairs. */
export function breadcrumbLd(items: Array<[string, string]>) {
  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: items.map(([name, item], i) => ({
      '@type': 'ListItem',
      position: i + 1,
      name,
      item
    }))
  }
}

/** Demote any <h1> inside rich article HTML to <h2> so each page keeps a single H1 (the article title). */
export function demoteH1(html: string): string {
  return (html || '').replace(/<h1(\s[^>]*)?>/gi, '<h2$1>').replace(/<\/h1>/gi, '</h2>')
}
