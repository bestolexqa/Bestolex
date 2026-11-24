// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  srcDir: '.', // Use root directory for app files
  devtools: { enabled: true },
  // Function region (monitoring log, improvement 15). Vercel has no Gulf region (dxb1 is rejected).
  // Measured on 19 Nov 2026, the first read of articles.json from Bunny Storage in a new server
  // instance took 1.02-1.20 s from bom1 (Mumbai), 0.84 s from iad1 (Washington, the old default)
  // and 0.19 s from fra1 (Frankfurt). The site has little traffic, so new instances are common;
  // fra1 keeps that read short, is closer to Qatar than iad1 and sits next to Supabase (eu-west-1).
  // Written by Nitro into the function's .vc-config.json, so it travels with the code.
  nitro: {
    vercel: {
      functions: {
        regions: ['fra1']
      }
    }
  },
  routeRules: {
    // Basic security headers on every response (item 25). A Content-Security-Policy comes later,
    // once GTM/GA4 and the CDN hosts are final.
    '/**': {
      headers: {
        'X-Content-Type-Options': 'nosniff',
        'X-Frame-Options': 'SAMEORIGIN',
        'Referrer-Policy': 'strict-origin-when-cross-origin',
        'Permissions-Policy': 'camera=(), microphone=(), geolocation=(), payment=()'
      }
    },
    // Edge caching (plan item 26): Vercel ISR serves these pages from the CDN and re-renders them in the
    // background after the given seconds. Product and category pages come from data/products.json, which only
    // changes with a deploy (a deploy clears the cache), so they can stay an hour. Home and blog show articles,
    // including scheduled ones that appear at their publish time, so they refresh every 10 minutes.
    // Not cached: /contact (reads ?product=), the dashboard and every /api route.
    '/products': { isr: 3600 },
    '/products/**': { isr: 3600 },
    '/en/products': { isr: 3600 },
    '/en/products/**': { isr: 3600 },
    '/about': { isr: 3600 },
    '/en/about': { isr: 3600 },
    '/services': { isr: 3600 },
    '/en/services': { isr: 3600 },
    '/privacy': { isr: 3600 },
    '/en/privacy': { isr: 3600 },
    '/terms': { isr: 3600 },
    '/en/terms': { isr: 3600 },
    '/': { isr: 600 },
    '/en': { isr: 600 },
    '/blog': { isr: 600 },
    '/blog/**': { isr: 600 },
    '/en/blog': { isr: 600 },
    '/en/blog/**': { isr: 600 },
    // Old product slugs that carried an uncertified "PAS68" claim → permanent redirects.
    '/products/high-security-road-blocker-pas68': { redirect: { to: '/products/high-security-road-blocker', statusCode: 301 } },
    '/en/products/high-security-road-blocker-pas68': { redirect: { to: '/en/products/high-security-road-blocker', statusCode: 301 } },
    '/products/high-security-shallow-road-blocker-pas68': { redirect: { to: '/products/high-security-shallow-road-blocker', statusCode: 301 } },
    '/en/products/high-security-shallow-road-blocker-pas68': { redirect: { to: '/en/products/high-security-shallow-road-blocker', statusCode: 301 } }
  },
  modules: [
    '@nuxtjs/tailwindcss',
    '@nuxtjs/i18n',
    '@vueuse/nuxt',
    '@nuxtjs/supabase',
    '@nuxt/image'
  ],
  image: {
    format: ['webp', 'avif', 'jpeg', 'png'],
    quality: 80,
    domains: [
      'cdn.bestolex.com',
      // kept until the live article records are rewritten to the new host
      'electrocreative-cdn.b-cdn.net',
      'sabtech.com.sa',
      'cdn-bdndb.nitrocdn.com',
      'images.unsplash.com'
    ]
  },
  runtimeConfig: {
    gmailUser: process.env.GMAIL_USER,
    gmailPass: process.env.GMAIL_PASS,
    bunnyStorageZoneName: process.env.BUNNY_STORAGE_ZONE_NAME || 'bestolex-products',
    bunnyStorageAccessKey: process.env.BUNNY_NEW_STORAGE_KEY || process.env.BUNNY_STORAGE_ACCESS_KEY || '',
    bunnyStorageBaseUrl: process.env.BUNNY_STORAGE_BASE_URL || 'https://storage.bunnycdn.com',
    public: {
      bunnyPullZoneUrl: process.env.BUNNY_PULL_ZONE_URL ? (process.env.BUNNY_PULL_ZONE_URL.startsWith('http') ? process.env.BUNNY_PULL_ZONE_URL : `https://${process.env.BUNNY_PULL_ZONE_URL}`) : 'https://cdn.bestolex.com'
    }
  },
  i18n: {
    locales: [
      { code: 'ar', language: 'ar-QA', dir: 'rtl', name: 'العربية' },
      { code: 'en', language: 'en', dir: 'ltr', name: 'English' }
    ],
    defaultLocale: 'ar',
    strategy: 'prefix_except_default',
    baseUrl: 'https://www.bestolex.com',
    detectBrowserLanguage: false
  },
  supabase: {
    url: process.env.SUPABASE_URL || 'https://example.supabase.co',
    key: process.env.SUPABASE_KEY || 'example-key',
    redirect: false
  },
  css: [
    'aos/dist/aos.css'
  ],
  app: {
    head: {
      title: 'بيستوليكس قطر | معدات التحميل والنفايات والحماية والأبواب الصناعية',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'robots', content: 'index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' },
        { name: 'author', content: 'بيستوليكس لتجارة الآلات والمعدات الثقيلة (ذ.م.م) | Bestolex Trading of Heavy Equipment and Machinery W.L.L.' },
        { name: 'theme-color', content: '#E99E15' },
        { name: 'geo.region', content: 'QA' },
        { name: 'geo.placename', content: 'Doha, Qatar' },
        { property: 'og:site_name', content: 'Bestolex Qatar | بيستوليكس قطر' },
        { property: 'og:type', content: 'website' },
        { name: 'twitter:card', content: 'summary_large_image' }
      ],
      link: [
        { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
        { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' },
        { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700;800;900&display=swap' },
        // Light icon set (item 30): ICO 16/32/48 (3 KB) instead of the 47 KB logo, plus app icons and a manifest
        { rel: 'icon', href: '/favicon.ico', sizes: '48x48' },
        { rel: 'icon', type: 'image/png', sizes: '192x192', href: '/icon-192.png' },
        { rel: 'apple-touch-icon', sizes: '180x180', href: '/apple-touch-icon.png' },
        { rel: 'manifest', href: '/site.webmanifest' }
      ],
      script: [
        {
          innerHTML: `
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            // 1. Google Consent Mode v2: Mandatory default state (Always DENIED for all 4 parameters)
            gtag('consent', 'default', {
              'ad_storage': 'denied',
              'ad_user_data': 'denied',
              'ad_personalization': 'denied',
              'analytics_storage': 'denied',
              'wait_for_update': 500
            });
            // 2. If user previously saved consent, apply update immediately
            try {
              var savedConsent = localStorage.getItem('bestolex_cookie_consent');
              if (savedConsent) {
                var parsed = JSON.parse(savedConsent);
                gtag('consent', 'update', {
                  'ad_storage': parsed.marketing ? 'granted' : 'denied',
                  'ad_user_data': parsed.marketing ? 'granted' : 'denied',
                  'ad_personalization': parsed.marketing ? 'granted' : 'denied',
                  'analytics_storage': parsed.analytics ? 'granted' : 'denied'
                });
              }
            } catch (e) {}
          `,
          tagPosition: 'head'
        },
        {
          innerHTML: `(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-NPWXWRD5');`,
          tagPosition: 'head'
        }
      ],
      noscript: [
        {
          innerHTML: `<iframe src="https://www.googletagmanager.com/ns.html?id=GTM-NPWXWRD5" height="0" width="0" style="display:none;visibility:hidden"></iframe>`,
          tagPosition: 'bodyOpen'
        }
      ]
    }
  }
})
