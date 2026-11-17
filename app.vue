<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>

<script setup>
// Per-language <html lang/dir>, self-referencing canonical, hreflang alternates (ar-QA, en, x-default) and og:locale.
const i18nHead = useLocaleHead({ lang: true, dir: true, seo: true })

useHead(() => ({
  htmlAttrs: {
    lang: i18nHead.value.htmlAttrs?.lang,
    dir: i18nHead.value.htmlAttrs?.dir
  },
  link: [...(i18nHead.value.link || [])],
  meta: [...(i18nHead.value.meta || [])]
}))
</script>

<style>
@tailwind base;
@tailwind components;
@tailwind utilities;
</style>
