// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  srcDir: '.', // Use root directory for app files
  devtools: { enabled: true },
  // Run the server function near the Gulf instead of Vercel's default iad1 (Washington), since
  // every page is rendered on request (monitoring log, improvement 15). bom1 (Mumbai) is the
  // closest region Vercel offers to Qatar; there is no Gulf region (dxb1 is rejected). Written by
  // Nitro into the function's .vc-config.json, so it travels with the code and applies on deploy.
  nitro: {
    vercel: {
      functions: {
        regions: ['iad1']
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
      'electrocreative-cdn.b-cdn.net',
      'sabtech.com.sa',
      'cdn-bdndb.nitrocdn.com',
      'images.unsplash.com'
    ]
  },
  runtimeConfig: {
    gmailUser: process.env.GMAIL_USER,
    gmailPass: process.env.GMAIL_PASS,
    bunnyStorageZoneName: process.env.BUNNY_STORAGE_ZONE_NAME || 'electrocreative-zone',
    bunnyStorageAccessKey: process.env.BUNNY_STORAGE_ACCESS_KEY || '',
    bunnyStorageBaseUrl: process.env.BUNNY_STORAGE_BASE_URL || 'https://storage.bunnycdn.com',
    public: {
      bunnyPullZoneUrl: process.env.BUNNY_PULL_ZONE_URL ? (process.env.BUNNY_PULL_ZONE_URL.startsWith('http') ? process.env.BUNNY_PULL_ZONE_URL : `https://${process.env.BUNNY_PULL_ZONE_URL}`) : 'https://electrocreative-cdn.b-cdn.net'
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
        { rel: 'icon', type: 'image/png', href: '/logo.png' }
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
