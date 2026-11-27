// Shared by the product quote form, the contact form and /api/contact (item 21 in the plan:
// fewer required fields, plus request type, product and project location).

export const REQUEST_TYPES = [
  { id: 'quote', ar: 'عرض سعر', en: 'Quotation' },
  { id: 'site-survey', ar: 'معاينة موقع', en: 'Site survey' },
  { id: 'maintenance', ar: 'صيانة أو قطع غيار', en: 'Maintenance or spare parts' },
  { id: 'technical', ar: 'استفسار فني', en: 'Technical question' },
  { id: 'sourcing', ar: 'توريد حسب الطلب', en: 'Sourcing on request' },
  { id: 'other', ar: 'أخرى', en: 'Other' }
] as const

export type RequestTypeId = typeof REQUEST_TYPES[number]['id']

export function requestTypeLabel(id: string | undefined, locale: string = 'ar'): string {
  const t = REQUEST_TYPES.find(r => r.id === id)
  if (!t) return ''
  return locale === 'ar' ? t.ar : t.en
}

// WhatsApp deep link to the primary number with a prefilled message.
export function whatsappLink(text: string): string {
  return `https://wa.me/97451505014?text=${encodeURIComponent(text)}`
}
