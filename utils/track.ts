// Pushes a conversion event to the GTM dataLayer. GTM decides what to send
// (GA4 / Google Ads) and Consent Mode decides whether cookies may be used.
// Only non-personal fields are sent: never name, phone, email or message text.
export function trackLead (params: { formName: string, requestType?: string, productId?: string }) {
  if (typeof window === 'undefined') return
  const w = window as any
  w.dataLayer = w.dataLayer || []
  w.dataLayer.push({
    event: 'generate_lead',
    form_name: params.formName,
    request_type: params.requestType || '',
    product_id: params.productId || ''
  })
}
