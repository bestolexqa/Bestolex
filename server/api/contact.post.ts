import nodemailer from 'nodemailer'
import { useServerSupabase } from '~~/server/utils/supabase'
import { REQUEST_TYPES, requestTypeLabel } from '~~/utils/leads'

// Receives the product quote form and the contact form.
// Required: a name, plus a phone number or an email (item 21: fewer required fields).
// Optional: company, job title, request type, product, project location, message.

const clip = (v: unknown, max = 500) => (typeof v === 'string' ? v.trim().slice(0, max) : '')
const esc = (s: string) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;')
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/

export default defineEventHandler(async (event) => {
  const body = (await readBody(event)) || {}
  const config = useRuntimeConfig()
  const supabase = useServerSupabase()

  const lead = {
    name: clip(body.name, 120),
    company: clip(body.company, 160),
    jobTitle: clip(body.jobTitle, 120),
    email: clip(body.email, 160),
    phone: clip(body.phone, 40),
    requestType: REQUEST_TYPES.some(r => r.id === body.requestType) ? String(body.requestType) : '',
    location: clip(body.location, 160),
    productId: clip(body.productId, 120),
    productName: clip(body.productName, 300),
    categoryTitle: clip(body.categoryTitle, 160),
    productUrl: clip(body.productUrl, 500),
    message: clip(body.message, 5000)
  }

  if (!lead.name || (!lead.phone && !lead.email)) {
    throw createError({ statusCode: 400, statusMessage: 'A name and a phone number or email are required' })
  }
  if (lead.email && !EMAIL_RE.test(lead.email)) {
    throw createError({ statusCode: 400, statusMessage: 'Invalid email address' })
  }
  if (lead.productUrl && !/^https?:\/\//.test(lead.productUrl)) lead.productUrl = ''

  const isQuote = !!body.isQuoteRequest || !!lead.productName || lead.requestType === 'quote'
  const typeAr = requestTypeLabel(lead.requestType, 'ar')
  const productName = lead.productName || 'غير محدد'
  const na = 'غير محدد'

  // Details that have no column of their own in quote_requests are kept in the message.
  const extraLines = [
    typeAr && `نوع الطلب: ${typeAr}`,
    lead.location && `موقع المشروع: ${lead.location}`,
    lead.company && `مقدم الطلب: ${lead.name}`
  ].filter(Boolean) as string[]
  const storedMessage = [lead.message, extraLines.join('\n')].filter(Boolean).join('\n\n')

  if (supabase) {
    try {
      await supabase.from('quote_requests').insert([{
        company_name: lead.company || lead.name,
        job_title: lead.jobTitle || na,
        email: lead.email || na,
        phone: lead.phone || na,
        product_id: lead.productId || null,
        product_name: lead.productName || null,
        category_title: lead.categoryTitle || null,
        product_url: lead.productUrl || null,
        message: storedMessage,
        is_quote_request: isQuote,
        status: 'new'
      }])
    } catch (dbErr) {
      console.warn('Supabase quote insertion error:', dbErr)
    }
  }

  const subject = isQuote
    ? `طلب ${typeAr || 'عرض سعر'}: ${productName} - من ${lead.name}`
    : `رسالة جديدة من الموقع${typeAr ? ` (${typeAr})` : ''}: ${lead.name}`

  const rows: [string, string][] = [
    ['الاسم', lead.name],
    ['الشركة', lead.company || na],
    ['المسمى الوظيفي', lead.jobTitle || na],
    ['رقم الهاتف', lead.phone || na],
    ['البريد الإلكتروني', lead.email || na],
    ['نوع الطلب', typeAr || na],
    ['موقع المشروع', lead.location || na],
    ['المنتج', productName],
    ['القسم', lead.categoryTitle || na]
  ]

  const plainText = [
    '===============================================',
    isQuote ? 'طلب جديد من الموقع (New Website Request)' : 'رسالة جديدة من تواصل معنا (New Contact Message)',
    '===============================================',
    ...rows.map(([k, v]) => `${k}: ${v}`),
    lead.productUrl ? `رابط المنتج: ${lead.productUrl}` : '',
    '',
    'الرسالة:',
    lead.message || 'لا توجد رسالة'
  ].join('\n')

  const htmlRows = rows.map(([k, v], i) => `
            <tr${i ? ' style="border-top: 1px solid #f5f5f5;"' : ''}>
              <td style="padding: 10px 0; color: #777; width: 140px; font-weight: bold;">${esc(k)}:</td>
              <td style="padding: 10px 0; color: #111; font-weight: 600;">${esc(v)}</td>
            </tr>`).join('')

  const htmlContent = `
    <div style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; direction: rtl; text-align: right; background-color: #f4f6f9; padding: 30px; color: #333;">
      <div style="max-width: 650px; margin: 0 auto; background: #ffffff; border-radius: 16px; overflow: hidden; border: 1px solid #e1e8ed;">
        <div style="background: #191919; padding: 25px 30px; text-align: center; border-bottom: 4px solid #E99E05;">
          <h1 style="color: #ffffff; margin: 0; font-size: 22px; font-weight: bold;">${esc(isQuote ? `طلب ${typeAr || 'عرض سعر'}` : 'رسالة من صفحة تواصل معنا')}</h1>
          <p style="color: #E99E05; margin: 8px 0 0 0; font-size: 14px; font-weight: 600;">موقع بيستوليكس</p>
        </div>
        <div style="padding: 30px;">
          ${lead.productName ? `<div style="background-color: #fff9ed; border: 2px solid #fce3b5; border-radius: 12px; padding: 20px; margin-bottom: 25px;">
            <div style="font-size: 13px; color: #b87500; font-weight: bold; margin-bottom: 6px;">المنتج المطلوب:</div>
            <div style="font-size: 20px; color: #191919; font-weight: 800;">${esc(lead.productName)}</div>
            ${lead.productUrl ? `<div style="font-size: 13px; margin-top: 8px;"><a href="${esc(lead.productUrl)}" style="color: #E99E05; font-weight: bold;">فتح صفحة المنتج</a></div>` : ''}
          </div>` : ''}
          <table style="width: 100%; border-collapse: collapse; margin-bottom: 25px; font-size: 15px;">${htmlRows}
          </table>
          <h3 style="color: #191919; border-bottom: 2px solid #f0f0f0; padding-bottom: 8px;">الرسالة:</h3>
          <div style="background: #f9fbfd; border-radius: 8px; padding: 15px; border-right: 4px solid #191919; font-size: 14px; line-height: 1.6; color: #444;">
            ${lead.message ? esc(lead.message).replace(/\n/g, '<br>') : '<em style="color: #999;">لا توجد رسالة</em>'}
          </div>
        </div>
      </div>
    </div>`

  console.log('=== WEBSITE REQUEST ===')
  console.log('Subject:', subject)
  console.log(plainText)

  if (config.gmailUser && config.gmailPass) {
    try {
      const transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: { user: config.gmailUser, pass: config.gmailPass }
      })
      const info = await transporter.sendMail({
        from: config.gmailUser,
        to: config.gmailUser,
        ...(lead.email ? { replyTo: lead.email } : {}),
        subject,
        text: plainText,
        html: htmlContent
      })
      return { success: true, messageId: info.messageId }
    } catch (error) {
      console.error('Error sending email via Nodemailer:', error)
      return { success: true, warning: 'Logged to console fallback', error: String(error) }
    }
  }

  return { success: true, devMode: true, message: 'Request logged successfully' }
})
