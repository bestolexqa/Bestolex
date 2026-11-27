<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>

<script setup>
// Per-language <html lang/dir>, self-referencing canonical, hreflang alternates (ar-QA, en, x-default) and og:locale.
const i18nHead = useLocaleHead({ lang: true, dir: true, seo: true })

// Site-wide entity graph: one Organization and one WebSite, referenced by @id from page-level schema.
const siteGraph = JSON.stringify({
  '@context': 'https://schema.org',
  '@graph': [
    {
      '@type': 'Organization',
      '@id': ORG_ID,
      name: BUSINESS.legalNameEn,
      alternateName: [BUSINESS.legalNameAr, 'Bestolex', 'بيستوليكس'],
      legalName: BUSINESS.legalNameEn,
      url: SITE_URL,
      description: BUSINESS.descriptionEn,
      logo: BUSINESS.logo,
      sameAs: BUSINESS.sameAs,
      areaServed: [{ '@type': 'Country', name: 'Qatar' }, { '@type': 'Place', name: 'Middle East' }, { '@type': 'Place', name: 'Africa' }],
      knowsAbout: BUSINESS.knowsAbout,
      slogan: BUSINESS.slogan,
      identifier: { '@type': 'PropertyValue', propertyID: 'Qatar Commercial Registration', value: '248416' },
      email: BUSINESS.email,
      telephone: BUSINESS.phonePrimary,
      address: BUSINESS.address,
      contactPoint: [
        { '@type': 'ContactPoint', telephone: BUSINESS.phonePrimary, contactType: 'sales', areaServed: 'QA', availableLanguage: ['ar', 'en'] },
        { '@type': 'ContactPoint', telephone: BUSINESS.phoneSecondary, contactType: 'customer service', areaServed: 'QA', availableLanguage: ['ar', 'en'] }
      ]
    },
    {
      '@type': 'WebSite',
      '@id': WEBSITE_ID,
      url: SITE_URL,
      name: 'Bestolex Qatar',
      alternateName: 'بيستوليكس قطر',
      inLanguage: ['ar-QA', 'en'],
      publisher: { '@id': ORG_ID }
    }
  ]
})

useHead(() => ({
  htmlAttrs: {
    lang: i18nHead.value.htmlAttrs?.lang,
    dir: i18nHead.value.htmlAttrs?.dir
  },
  link: [...(i18nHead.value.link || [])],
  meta: [...(i18nHead.value.meta || [])],
  script: [{ type: 'application/ld+json', key: 'ld-site', innerHTML: siteGraph }]
}))
</script>

<style>
@tailwind base;
@tailwind components;
@tailwind utilities;
</style>
