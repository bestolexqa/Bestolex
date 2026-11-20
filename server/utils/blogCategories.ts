// The five fixed blog categories. Every public reader shows articles under these names only;
// old dashboard names are mapped onto them (normalizeBlogCategory). Same list as tools/blog/qa.py.
export const BLOG_CATEGORIES = [
  { id: 'loading-systems', slug: 'loading-systems', name_ar: 'أنظمة التحميل والمستودعات', name_en: 'Loading & Warehouse Systems' },
  { id: 'waste-recycling', slug: 'waste-recycling', name_ar: 'النفايات وإعادة التدوير', name_en: 'Waste & Recycling' },
  { id: 'perimeter-protection', slug: 'perimeter-protection', name_ar: 'الحماية المحيطية', name_en: 'Perimeter Protection' },
  { id: 'industrial-doors', slug: 'industrial-doors', name_ar: 'الأبواب الصناعية', name_en: 'Industrial Doors' },
  { id: 'heavy-equipment', slug: 'heavy-equipment', name_ar: 'المعدات الثقيلة', name_en: 'Heavy Equipment' }
]

const BY_AR = new Map(BLOG_CATEGORIES.map(c => [c.name_ar, c]))

// Names used in the dashboard before the fixed list (whitespace is ignored).
const OLD_NAMES: Record<string, string> = {
  'المخلفات والتدوير': 'النفايات وإعادة التدوير',
  'انظمة التحميل': 'أنظمة التحميل والمستودعات',
  'أنظمة التحميل': 'أنظمة التحميل والمستودعات',
  'أنظمة حديثة وموثوقة التحميل': 'أنظمة التحميل والمستودعات',
  'منصات وأنظمة التحميل اللوجستية': 'أنظمة التحميل والمستودعات',
  'أنظمة حماية المحيط الأمنية': 'الحماية المحيطية',
  'الابواب الصناعية': 'الأبواب الصناعية',
  'الات ومعدات ثقيله': 'المعدات الثقيلة',
  'النظم الهيدروليكية المتقدمة': 'المعدات الثقيلة',
  'الصيانة الشاملة والدعم الفني': 'المعدات الثقيلة',
  'الصيانة دورية متقدمة والدعم الفني': 'المعدات الثقيلة'
}

/** The fixed category for an article's Arabic category name, or undefined if it is unknown. */
export function normalizeBlogCategory(nameAr: unknown): { ar: string, en: string } | undefined {
  const key = String(nameAr || '').replace(/\s+/g, ' ').trim()
  const c = BY_AR.get(key) || BY_AR.get(OLD_NAMES[key] || '')
  return c ? { ar: c.name_ar, en: c.name_en } : undefined
}
