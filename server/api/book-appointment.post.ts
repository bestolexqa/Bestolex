import { useServerSupabase } from '~~/server/utils/supabase'
import { isMailConfigured, leadRecipients, sendLeadMail } from '~~/server/utils/leadMailer'

// Appointment requests from the booking dialog.
// Like the contact form, this used to be wired to Gmail credentials that were
// never set. It also failed the whole request when the customer's
// acknowledgement bounced, even though the booking itself had arrived.

const clip = (v: unknown, max = 200) => (typeof v === 'string' ? v.trim().slice(0, max) : '')
const esc = (s: string) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;')
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/

export default defineEventHandler(async (event) => {
  const body = (await readBody(event)) || {}
  const supabase = useServerSupabase()

  const name = clip(body.name, 120)
  const email = clip(body.email, 160)
  const phone = clip(body.phone, 40)
  const date = clip(body.date, 40)
  const time = clip(body.time, 40)
  const locale = body.locale === 'en' ? 'en' : 'ar'
  const isArabic = locale === 'ar'

  if (!name || !email || !phone || !date || !time) {
    throw createError({ statusCode: 400, statusMessage: 'Missing required fields' })
  }
  if (!EMAIL_RE.test(email)) {
    throw createError({ statusCode: 400, statusMessage: 'Invalid email address' })
  }

  let stored = false
  if (supabase) {
    try {
      await supabase.from('appointments').insert([{ name, email, phone, date, time, locale, status: 'new' }])
      stored = true
    } catch (dbErr) {
      console.warn('Supabase appointment insertion error:', dbErr)
    }
  }

  const rows: [string, string][] = [
    ['الاسم', name], ['البريد الإلكتروني', email], ['رقم الهاتف', phone],
    ['التاريخ', date], ['الوقت', time]
  ]
  const adminText = ['طلب حجز موعد جديد', ...rows.map(([k, v]) => `${k}: ${v}`)].join('\n')
  const adminHtml = `
    <div dir="rtl" style="font-family: Tahoma, Arial, sans-serif; padding: 24px; color: #191919;">
      <h2 style="color: #E99E05; margin: 0 0 16px;">طلب حجز موعد جديد</h2>
      ${rows.map(([k, v]) => `<p style="margin:6px 0;"><strong>${esc(k)}:</strong> ${esc(v)}</p>`).join('')}
    </div>`

  console.log('=== APPOINTMENT REQUEST ===')
  console.log(adminText)

  let mailError: unknown = null
  let delivered = false
  if (isMailConfigured()) {
    try {
      const messageId = await sendLeadMail({
        subject: `طلب حجز موعد - ${name}`,
        text: adminText,
        html: adminHtml,
        replyTo: email,
        fromName: 'Bestolex Booking'
      })
      delivered = true
      console.log(`[appointment] delivered to ${leadRecipients()} (${messageId})`)
    } catch (error) {
      mailError = error
      console.error('[appointment] SMTP delivery failed:', error)
    }
  } else {
    console.error('[appointment] SMTP is not configured; no mail was sent')
  }

  if (!delivered && !stored) {
    throw createError({
      statusCode: 502,
      statusMessage: 'Appointment could not be delivered',
      data: {
        reason: mailError ? 'smtp_failed' : 'smtp_not_configured',
        detail: mailError ? String(mailError) : 'SMTP_USER / SMTP_PASS are not set'
      }
    })
  }

  // The customer's acknowledgement is a courtesy: a failure here must not
  // tell the customer their booking did not go through, because it did.
  if (delivered) {
    const ackHtml = isArabic
      ? `<div dir="rtl" style="font-family: Tahoma, Arial, sans-serif; padding: 24px; line-height: 1.8; color: #191919;">
           <h2 style="color: #E99E05; margin: 0 0 12px;">مرحباً ${esc(name)}،</h2>
           <p>شكراً لتواصلك مع بيستوليكس. استلمنا طلب حجز موعدك:</p>
           <p><strong>التاريخ:</strong> ${esc(date)} &nbsp;|&nbsp; <strong>الوقت:</strong> ${esc(time)}</p>
           <p>سيتواصل معك فريقنا لتأكيد الموعد. وللاستعجال: +974 51505014.</p>
           <p style="margin-top:20px;">فريق بيستوليكس</p>
         </div>`
      : `<div dir="ltr" style="font-family: Arial, sans-serif; padding: 24px; line-height: 1.8; color: #191919;">
           <h2 style="color: #E99E05; margin: 0 0 12px;">Hello ${esc(name)},</h2>
           <p>Thank you for contacting Bestolex. We have received your appointment request:</p>
           <p><strong>Date:</strong> ${esc(date)} &nbsp;|&nbsp; <strong>Time:</strong> ${esc(time)}</p>
           <p>Our team will contact you to confirm. For anything urgent: +974 51505014.</p>
           <p style="margin-top:20px;">Bestolex Team</p>
         </div>`
    try {
      await sendLeadMail({
        to: email,
        subject: isArabic ? 'تأكيد استلام طلب موعد - بيستوليكس' : 'Appointment request received - Bestolex',
        text: isArabic
          ? `مرحباً ${name}، استلمنا طلب حجز موعدك يوم ${date} الساعة ${time}. سيتواصل معك فريقنا. +974 51505014`
          : `Hello ${name}, we have received your appointment request on ${date} at ${time}. Our team will contact you. +974 51505014`,
        html: ackHtml,
        fromName: 'Bestolex'
      })
    } catch (ackErr) {
      console.warn('[appointment] customer acknowledgement failed:', ackErr)
    }
  }

  return { success: true, delivered, stored }
})
