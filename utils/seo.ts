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
  descriptionEn: 'Bestolex Trading of Heavy Equipment and Machinery W.L.L. is a Qatari company in Doha and the exclusive SABTECH agent in Qatar, supplying, installing and maintaining loading and warehouse systems, waste and recycling equipment, perimeter protection and industrial doors.',
  descriptionAr: 'بيستوليكس لتجارة الآلات والمعدات الثقيلة (ذ.م.م) شركة قطرية في الدوحة والوكيل الحصري لمنتجات ساب تك في قطر، تورّد وتركّب وتصون أنظمة التحميل والمستودعات ومعدات النفايات وإعادة التدوير والحماية المحيطية والأبواب الصناعية.',
  knowsAbout: [
    'Dock levelers', 'Dock shelters', 'Scissor lift tables', 'Cargo lifts',
    'Cardboard balers', 'Waste compactors', 'Recycling equipment',
    'Road blockers', 'Tyre killers', 'Automatic bollards', 'Turnstiles', 'Under vehicle surveillance systems',
    'High-speed doors', 'Industrial sectional doors'
  ],
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
