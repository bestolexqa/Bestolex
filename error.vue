<template>
  <NuxtLayout>
    <section class="min-h-[60vh] flex items-center justify-center px-4 py-20 bg-white dark:bg-gray-900">
      <div class="max-w-3xl w-full text-center">
        <p class="text-primary font-black text-6xl mb-4">{{ is404 ? '404' : error?.statusCode || 500 }}</p>
        <h1 class="text-2xl md:text-3xl font-black text-gray-900 dark:text-white mb-4">
          <template v-if="is404">{{ isAr ? 'الصفحة غير موجودة' : 'Page not found' }}</template>
          <template v-else>{{ isAr ? 'حدث خطأ غير متوقع' : 'Something went wrong' }}</template>
        </h1>
        <p class="text-gray-600 dark:text-gray-300 mb-10">
          {{ isAr
            ? 'ربما تغيّر الرابط أو حُذفت الصفحة. تصفّح أقسام منتجاتنا أو تواصل معنا مباشرة.'
            : 'The link may have changed or the page was removed. Browse our product categories or contact us directly.' }}
        </p>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 mb-10">
          <NuxtLink
            v-for="cat in categories"
            :key="cat.id"
            :to="localePath(`/products/category/${cat.id}`)"
            class="block border border-gray-200 dark:border-gray-700 rounded-xl px-4 py-3 font-bold text-gray-800 dark:text-gray-100 hover:border-primary hover:text-primary transition"
            @click="clear"
          >
            {{ cat.title?.[isAr ? 'ar' : 'en'] }}
          </NuxtLink>
        </div>

        <div class="flex flex-wrap gap-3 justify-center">
          <NuxtLink :to="localePath('/')" class="bg-primary text-white px-6 py-3 rounded-lg font-bold hover:bg-orange-600 transition" @click="clear">
            {{ isAr ? 'الصفحة الرئيسية' : 'Home page' }}
          </NuxtLink>
          <a href="https://wa.me/97451505014" target="_blank" rel="noopener noreferrer" class="border-2 border-green-600 text-green-700 dark:text-green-400 px-6 py-3 rounded-lg font-bold hover:bg-green-600 hover:text-white transition">
            {{ isAr ? 'واتساب: ' : 'WhatsApp: ' }}<span dir="ltr">+974 5150 5014</span>
          </a>
        </div>
      </div>
    </section>
  </NuxtLayout>
</template>

<script setup>

const props = defineProps({ error: { type: Object, default: null } })

const { locale } = useI18n()
const localePath = useLocalePath()
const isAr = computed(() => locale.value !== 'en')
const is404 = computed(() => props.error?.statusCode === 404)
const { data: navData } = useCatalogNav()
const categories = computed(() => (navData.value || []).map(c => ({ id: c.id, title: c.title })))

useHead(() => ({
  htmlAttrs: { lang: isAr.value ? 'ar-QA' : 'en', dir: isAr.value ? 'rtl' : 'ltr' },
  title: is404.value
    ? (isAr.value ? 'الصفحة غير موجودة | بيستوليكس' : 'Page not found | Bestolex')
    : (isAr.value ? 'خطأ | بيستوليكس' : 'Error | Bestolex'),
  meta: [{ name: 'robots', content: 'noindex, follow' }]
}))

const clear = () => clearError()
</script>
