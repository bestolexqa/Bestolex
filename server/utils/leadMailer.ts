/**
 * Sends the website's leads by email.
 *
 * Until 26 Nov 2026 this was hard-wired to Gmail with credentials that were
 * never set, and the handlers answered "sent successfully" whether the mail
 * went out or not - so every quote request and contact message was lost in
 * silence. The transport is now Zoho (the company's own mail), and a failure
 * here throws so the caller can answer honestly.
 */
import nodemailer from 'nodemailer'
import type { Transporter } from 'nodemailer'

export type LeadMail = {
  subject: string
  text: string
  html: string
  replyTo?: string
  /** Overrides the default recipients; used by the customer acknowledgement. */
  to?: string
  fromName?: string
}

type MailSettings = {
  host: string
  port: number
  user: string
  pass: string
  to: string
  service?: string
}

let cached: Transporter | null = null
let cachedKey = ''

/**
 * Read the environment first, runtimeConfig second.
 *
 * Nuxt resolves `runtimeConfig: { x: process.env.X }` when the site is BUILT,
 * and at run time only overrides it from NUXT_-prefixed variables. A plain
 * SMTP_PASS set in Vercel would therefore never reach the handler - which is
 * exactly why the old GMAIL_USER / GMAIL_PASS pair could not have worked.
 * Reading process.env here means the variable is named plainly in Vercel and
 * picked up without a rebuild.
 */
function pick(envName: string, configKey: string): string {
  const fromEnv = process.env[envName]
  if (fromEnv && String(fromEnv).trim()) return String(fromEnv).trim()
  try {
    const v = (useRuntimeConfig() as any)?.[configKey]
    return v ? String(v).trim() : ''
  } catch {
    return ''
  }
}

function settings(): MailSettings | null {
  const user = pick('SMTP_USER', 'smtpUser')
  const pass = pick('SMTP_PASS', 'smtpPass')
  if (user && pass) {
    return {
      host: pick('SMTP_HOST', 'smtpHost') || 'smtp.zoho.com',
      port: Number(pick('SMTP_PORT', 'smtpPort')) || 465,
      user,
      pass,
      to: pick('LEADS_TO', 'leadsTo') || user
    }
  }
  // Legacy Gmail variables, kept so an existing deployment does not go dark.
  const gUser = pick('GMAIL_USER', 'gmailUser')
  const gPass = pick('GMAIL_PASS', 'gmailPass')
  if (gUser && gPass) {
    return { host: '', port: 0, user: gUser, pass: gPass, to: gUser, service: 'gmail' }
  }
  return null
}

export function isMailConfigured(): boolean {
  return settings() !== null
}

/** The address leads are delivered to, for logs and error messages. */
export function leadRecipients(): string {
  return settings()?.to || ''
}

function transporter(s: MailSettings): Transporter {
  const key = `${s.service || s.host}:${s.port}:${s.user}`
  if (cached && cachedKey === key) return cached
  cached = nodemailer.createTransport(
    s.service
      ? { service: s.service, auth: { user: s.user, pass: s.pass } }
      : {
          host: s.host,
          port: s.port,
          // 465 is implicit TLS; 587 upgrades with STARTTLS.
          secure: s.port === 465,
          auth: { user: s.user, pass: s.pass },
          connectionTimeout: 15000,
          greetingTimeout: 15000,
          socketTimeout: 20000
        }
  )
  cachedKey = key
  return cached
}

/** Sends one message. Throws when it cannot be delivered. */
export async function sendLeadMail(mail: LeadMail): Promise<string> {
  const s = settings()
  if (!s) throw new Error('SMTP is not configured: set SMTP_USER and SMTP_PASS')
  const info = await transporter(s).sendMail({
    from: `"${mail.fromName || 'Bestolex Website'}" <${s.user}>`,
    to: mail.to || s.to,
    ...(mail.replyTo ? { replyTo: mail.replyTo } : {}),
    subject: mail.subject,
    text: mail.text,
    html: mail.html
  })
  return info.messageId
}
