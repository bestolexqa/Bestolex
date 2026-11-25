<template>
  <div class="article-page bg-gray-50 dark:bg-gray-900 min-h-screen transition-colors duration-300 py-12 md:py-20">
    
    <!-- 404 / Loading State -->
    <div v-if="!article" class="min-h-[50vh] flex flex-col items-center justify-center text-center px-4">
      <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-4">
        {{ locale === 'ar' ? 'المقال غير موجود' : 'Article Not Found' }}
      </h2>
      <NuxtLink :to="localePath('/blog')" class="bg-primary text-white font-bold px-6 py-3 rounded-xl hover:bg-orange-600 transition">
        {{ locale === 'ar' ? 'العودة إلى المدونة' : 'Back to Blog' }}
      </NuxtLink>
    </div>

    <!-- Article Content View -->
    <article v-else class="container mx-auto px-4 md:px-8 max-w-4xl">
      
      <!-- Back Navigation & Category -->
      <div class="flex items-center justify-between gap-4 mb-8" data-aos="fade-down">
        <NuxtLink :to="localePath('/blog')" class="inline-flex items-center gap-2 text-sm font-bold text-gray-500 hover:text-primary transition">
          <span class="rtl:rotate-180 text-base">&larr;</span>
          <span>{{ locale === 'ar' ? 'العودة إلى المدونة' : 'Back to Blog' }}</span>
        </NuxtLink>

        <span class="bg-[#191919] dark:bg-gray-800 text-[#E99E05] font-black text-xs px-4 py-1.5 rounded-full border border-[#E99E05]/30">
          {{ article.category[locale] }}
        </span>
      </div>

      <!-- Title Header -->
      <header class="mb-10 text-center md:text-start" data-aos="fade-up">
        <h1 class="text-3xl sm:text-4xl md:text-5xl font-black text-gray-900 dark:text-white leading-tight mb-6">
          {{ article.title[locale] }}
        </h1>

        <!-- Meta Info -->
        <div class="flex flex-wrap items-center gap-6 text-sm font-bold text-gray-500 dark:text-gray-400 border-y border-gray-200 dark:border-gray-800 py-4">
          <div class="flex items-center gap-2">
            <span>👤</span>
            <span>{{ locale === 'ar' ? 'فريق بيستوليكس الهندسي' : 'Bestolex Engineering Team' }}</span>
          </div>
          <div v-if="article.reviewer?.[locale]" class="flex items-center gap-2">
            <span>✔️</span>
            <span>{{ locale === 'ar' ? 'مراجعة فنية:' : 'Technical review:' }} {{ article.reviewer[locale] }}</span>
          </div>
          <div v-if="article.updatedAt && article.updatedAt !== article.date" class="flex items-center gap-2">
            <span>🔄</span>
            <span>{{ locale === 'ar' ? 'آخر تحديث' : 'Updated' }} {{ article.updatedAt }}</span>
          </div>
          <div class="flex items-center gap-2">
            <span>📅</span>
            <span>{{ article.date }}</span>
          </div>
          <div class="flex items-center gap-2">
            <span>⏱️</span>
            <span>{{ article.readTime[locale] }}</span>
          </div>
        </div>
      </header>

      <!-- Featured Image -->
      <div class="relative h-[300px] sm:h-[450px] rounded-3xl overflow-hidden shadow-2xl mb-12 border border-gray-100 dark:border-gray-800" data-aos="zoom-in">
        <NuxtImg 
          :src="article.image" 
          :alt="article.imageAlt?.[locale] || article.title[locale]" 
          class="w-full h-full object-cover" 
          format="webp" 
          loading="eager" 
        />
      </div>

      <!-- Main Body Text -->
      <div class="prose prose-lg dark:prose-invert max-w-none bg-white dark:bg-gray-800 rounded-3xl p-6 sm:p-12 shadow-xl border border-gray-100 dark:border-gray-700 mb-16 text-gray-800 dark:text-gray-200 leading-relaxed text-base sm:text-lg article-content" data-aos="fade-up" v-html="articleHtml">
      </div>

      <!-- FAQ (repo articles; mirrored in FAQPage structured data) -->
      <section v-if="faqItems.length" class="bg-white dark:bg-gray-800 rounded-3xl p-6 sm:p-10 shadow-xl border border-gray-100 dark:border-gray-700 mb-16" data-aos="fade-up">
        <h2 class="text-2xl md:text-3xl font-black text-gray-900 dark:text-white mb-6">
          {{ locale === 'ar' ? 'أسئلة شائعة' : 'Frequently Asked Questions' }}
        </h2>
        <div class="divide-y divide-gray-100 dark:divide-gray-700">
          <details v-for="(item, i) in faqItems" :key="i" class="py-4 group" :open="i === 0">
            <summary class="cursor-pointer font-bold text-gray-900 dark:text-white text-base sm:text-lg list-none flex items-start justify-between gap-4">
              <span>{{ item.q }}</span>
              <span class="text-primary transition group-open:rotate-45 text-xl leading-none">+</span>
            </summary>
            <p class="mt-3 text-gray-700 dark:text-gray-300 leading-relaxed">{{ item.a }}</p>
          </details>
        </div>
      </section>

      <!-- Products discussed in the article, each with a quote request -->
      <section v-if="relatedProducts.length" class="mb-16" data-aos="fade-up">
        <h2 class="text-2xl font-black text-gray-900 dark:text-white mb-8 text-center md:text-start">
          {{ locale === 'ar' ? 'المنتجات المذكورة في المقال' : 'Products in This Article' }}
        </h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          <div v-for="p in relatedProducts" :key="p.id" class="bg-white dark:bg-gray-800 rounded-2xl overflow-hidden shadow border border-gray-100 dark:border-gray-700 flex flex-col">
            <NuxtLink :to="localePath(`/products/${p.id}`)" class="block h-44 overflow-hidden bg-white">
              <NuxtImg v-if="p.image" :src="p.image" :alt="p.name?.[locale]" class="w-full h-full object-contain p-2" format="webp" loading="lazy" sizes="400px" />
            </NuxtLink>
            <div class="p-5 flex-1 flex flex-col gap-4 justify-between">
              <NuxtLink :to="localePath(`/products/${p.id}`)" class="font-bold text-gray-900 dark:text-white hover:text-primary transition">
                {{ p.name?.[locale] }}
              </NuxtLink>
              <a :href="quoteLink(p)" target="_blank" rel="noopener" class="bg-primary hover:bg-orange-600 text-white text-sm font-bold px-4 py-2.5 rounded-xl text-center transition">
                {{ locale === 'ar' ? 'اطلب عرض سعر' : 'Request a Quote' }}
              </a>
            </div>
          </div>
        </div>
      </section>

      <!-- Call to Action Banner inside Article -->
      <div class="bg-gradient-to-r from-[#191919] to-[#1e2d42] text-white rounded-3xl p-8 md:p-10 shadow-2xl text-center mb-16" data-aos="fade-up">
        <h3 class="text-2xl md:text-3xl font-black mb-4">
          {{ locale === 'ar' ? 'هل تحتاج استشارة هندسية لمشروعك؟' : 'Need Technical Advice for Your Project?' }}
        </h3>
        <p class="text-gray-300 max-w-2xl mx-auto mb-6 text-sm md:text-base">
          {{ locale === 'ar' 
            ? 'فريقنا المتخصص جاهز للإجابة على استفساراتكم وتقديم الدعم الفني وتوريد أفضل المعدات والحلول الصناعية.' 
            : 'Our dedicated team is ready to answer inquiries, provide technical support, and supply high-quality industrial solutions.' 
          }}
        </p>
        <div class="flex flex-wrap justify-center gap-4">
          <NuxtLink :to="localePath('/contact')" class="bg-primary hover:bg-orange-600 text-white font-bold px-8 py-3.5 rounded-xl transition shadow-lg">
            {{ locale === 'ar' ? 'تواصل معنا' : 'Contact Us' }}
          </NuxtLink>
        </div>
      </div>

      <!-- Related Articles -->
      <div v-if="relatedArticles.length" class="mt-16" data-aos="fade-up">
        <h3 class="text-2xl font-black text-gray-900 dark:text-white mb-8 text-center md:text-start">
          {{ locale === 'ar' ? 'مقالات ذات صلة' : 'Related Articles' }}
        </h3>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div 
            v-for="rel in relatedArticles" 
            :key="rel.id" 
            class="bg-white dark:bg-gray-800 rounded-2xl overflow-hidden shadow border border-gray-100 dark:border-gray-700 hover:shadow-xl transition group flex flex-col"
          >
            <div class="h-40 overflow-hidden">
              <NuxtImg :src="rel.image" :alt="rel.title[locale]" class="w-full h-full object-cover group-hover:scale-105 transition duration-500" format="webp" loading="lazy" />
            </div>
            <div class="p-5 flex-1 flex flex-col justify-between">
              <h4 class="font-bold text-gray-900 dark:text-white mb-3 group-hover:text-primary transition line-clamp-2">
                <NuxtLink :to="localePath(`/blog/${rel.id}`)">
                  {{ rel.title[locale] }}
                </NuxtLink>
              </h4>
              <NuxtLink :to="localePath(`/blog/${rel.id}`)" class="text-primary font-bold text-sm hover:underline inline-flex items-center gap-1">
                <span>{{ locale === 'ar' ? 'قراءة المزيد' : 'Read More' }}</span>
                <span class="rtl:rotate-180">&rarr;</span>
              </NuxtLink>
            </div>
          </div>
        </div>
      </div>

    </article>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { useI18n } from 'vue-i18n'
import mockArticles from '@/data/articles.json'

const { locale } = useI18n()
const localePath = useLocalePath()
const route = useRoute()

const articleId = computed(() => route.params.id)
const { data: dynamicArticle } = await useFetch(() => `/api/blog/${route.params.id}`)

const article = computed(() => {
  if (dynamicArticle.value && (dynamicArticle.value.title || dynamicArticle.value.title_ar)) return dynamicArticle.value
  // data/articles.json carries cards without bodies, so a card alone must not
  // stand in for an article: an empty body would render a soft 200.
  const card = mockArticles.find(a => a.id === articleId.value || a.slug === articleId.value)
  return (card && (card.content || card.content_ar)) ? card : undefined
})

// Unknown article slugs, and cards with no body, must return a real 404.
if (!article.value) {
  throw createError({ statusCode: 404, statusMessage: 'Article not found', fatal: true })
}

const relatedArticles = computed(() => {
  if (!article.value) return []
  if (Array.isArray(article.value.related) && article.value.related.length) return article.value.related.slice(0, 2)
  return mockArticles.filter(a => a.id !== article.value.id && a.slug !== article.value.id).slice(0, 2)
})

// Repo articles (server/assets/blog) may carry FAQ items and the products they discuss.
const faqItems = computed(() => (Array.isArray(article.value?.faq) ? article.value.faq : [])
  .map(item => ({ q: item?.q?.[locale.value] || '', a: item?.a?.[locale.value] || '' }))
  .filter(item => item.q && item.a))
const relatedProducts = computed(() => (Array.isArray(article.value?.relatedProducts) ? article.value.relatedProducts : [])
  .filter(p => p?.id))
const quoteLink = (p) => {
  const name = p?.name?.[locale.value] || p?.id
  const text = locale.value === 'ar'
    ? `مرحباً، أرغب في عرض سعر لـ: ${name}`
    : `Hello, I would like a quotation for: ${name}`
  return `https://wa.me/97451505014?text=${encodeURIComponent(text)}`
}

const isAr = computed(() => locale.value === 'ar')

const articleTitle = computed(() => article.value?.title?.[locale.value] || article.value?.title?.ar || '')
const articleUrl = computed(() => `${SITE_URL}${localePath(`/blog/${articleId.value}`)}`)
// Article bodies may contain their own <h1>; keep the page title as the only H1.
const articleHtml = computed(() => demoteH1(article.value?.content?.[locale.value] || article.value?.content?.ar || ''))
const articleDesc = computed(() => seoDescription(
  article.value?.desc?.[locale.value] || article.value?.excerpt?.[locale.value] || article.value?.desc?.ar || article.value?.excerpt_ar || ''
))

useSeoMeta({
  title: () => article.value
    ? (article.value?.seoTitle?.[locale.value] || seoTitle(articleTitle.value, locale.value))
    : (isAr.value ? 'المقال | مدونة بيستوليكس' : 'Article | Bestolex Blog'),
  description: articleDesc,
  ogTitle: () => articleTitle.value || 'Bestolex Article',
  ogDescription: articleDesc,
  ogImage: () => (article.value?.image ? (article.value.image.startsWith('/') ? `${SITE_URL}${article.value.image}` : article.value.image) : BUSINESS.image),
  ogType: 'article'
})

useHead(() => ({
  script: [
    {
      type: 'application/ld+json',
      key: 'ld-article',
      innerHTML: JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'BlogPosting',
        '@id': `${articleUrl.value}#article`,
        'headline': articleTitle.value || 'Engineering Article',
        'description': articleDesc.value,
        'image': article.value?.image ? [article.value.image.startsWith('/') ? `${SITE_URL}${article.value.image}` : article.value.image] : [BUSINESS.image],
        'datePublished': article.value?.date || undefined,
        'dateModified': article.value?.updatedAt || article.value?.date || undefined,
        'inLanguage': isAr.value ? 'ar-QA' : 'en',
        'author': { '@id': ORG_ID },
        'publisher': { '@id': ORG_ID },
        'isPartOf': { '@id': WEBSITE_ID },
        'mainEntityOfPage': { '@type': 'WebPage', '@id': articleUrl.value }
      })
    },
    ...(faqItems.value.length ? [{
      type: 'application/ld+json',
      key: 'ld-faq',
      innerHTML: JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'FAQPage',
        'mainEntity': faqItems.value.map(item => ({
          '@type': 'Question',
          'name': item.q,
          'acceptedAnswer': { '@type': 'Answer', 'text': item.a }
        }))
      })
    }] : []),
    {
      type: 'application/ld+json',
      key: 'ld-breadcrumb',
      innerHTML: JSON.stringify(breadcrumbLd([
        [isAr.value ? 'الرئيسية' : 'Home', `${SITE_URL}${localePath('/')}`.replace(/\/$/, '')],
        [isAr.value ? 'المدونة' : 'Blog', `${SITE_URL}${localePath('/blog')}`],
        [articleTitle.value, articleUrl.value]
      ]))
    }
  ]
}))
</script>

<style scoped>
/* Article HTML content styling */
.article-content :deep(h1),
.article-content :deep(h2),
.article-content :deep(h3),
.article-content :deep(h4),
.article-content :deep(h5),
.article-content :deep(h6) {
  font-weight: 800;
  line-height: 1.3;
  margin-top: 1.5em;
  margin-bottom: 0.75em;
  color: #111827;
}

.dark .article-content :deep(h1),
.dark .article-content :deep(h2),
.dark .article-content :deep(h3),
.dark .article-content :deep(h4) {
  color: #f9fafb;
}

.article-content :deep(h1) { font-size: 1.875rem; }
.article-content :deep(h2) { font-size: 1.5rem; }
.article-content :deep(h3) { font-size: 1.25rem; }

.article-content :deep(p) {
  margin-bottom: 1.25em;
  line-height: 1.8;
}

.article-content :deep(ul),
.article-content :deep(ol) {
  padding-inline-start: 1.5rem;
  margin-bottom: 1.25em;
}

.article-content :deep(li) {
  margin-bottom: 0.5em;
  line-height: 1.7;
}

.article-content :deep(ul) { list-style-type: disc; }
.article-content :deep(ol) { list-style-type: decimal; }

.article-content :deep(strong),
.article-content :deep(b) {
  font-weight: 700;
}

.article-content :deep(em),
.article-content :deep(i) {
  font-style: italic;
}

.article-content :deep(.table-wrap) {
  overflow-x: auto;
  margin: 1.5em 0;
  border-radius: 0.75rem;
  border: 1px solid #e5e7eb;
}

.article-content :deep(table) {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.95em;
  line-height: 1.5;
}

.article-content :deep(th) {
  background: #191919;
  color: #ffffff;
  font-weight: 700;
  text-align: start;
  padding: 0.75em 1em;
  white-space: nowrap;
}

.article-content :deep(td) {
  padding: 0.7em 1em;
  border-top: 1px solid #e5e7eb;
  vertical-align: top;
}

.article-content :deep(tbody tr:nth-child(even) td) {
  background: #fafafa;
}

.dark .article-content :deep(.table-wrap) { border-color: #374151; }
.dark .article-content :deep(td) { border-top-color: #374151; }
.dark .article-content :deep(tbody tr:nth-child(even) td) { background: #1f2937; }

.article-content :deep(figure) {
  margin: 1.75em 0;
}

.article-content :deep(figure img) {
  width: 100%;
  height: auto;
  max-height: 480px;
  object-fit: contain;
  background: #ffffff;
  border-radius: 1rem;
  border: 1px solid #e5e7eb;
}

.article-content :deep(figcaption) {
  font-size: 0.85em;
  color: #6b7280;
  margin-top: 0.5em;
  text-align: center;
}

.article-content :deep(.key-takeaways) {
  background: #fff8e8;
  border-inline-start: 4px solid #E99E05;
  border-radius: 0.75rem;
  padding: 1em 1.25em;
  margin: 1.5em 0;
}

.dark .article-content :deep(.key-takeaways) {
  background: #2a2316;
}

.article-content :deep(a) {
  color: #E99E05;
  text-decoration: underline;
}

.article-content :deep(blockquote) {
  border-inline-start: 4px solid #E99E05;
  padding-inline-start: 1rem;
  margin: 1.5em 0;
  font-style: italic;
  color: #6b7280;
}

.article-content :deep(img) {
  max-width: 100%;
  border-radius: 0.75rem;
  margin: 1.5em auto;
}

.article-content :deep(hr) {
  border: none;
  border-top: 1px solid #e5e7eb;
  margin: 2em 0;
}

/* Light column dividers, also for tables in older dashboard articles. */
.article-content :deep(td) {
  border-inline: 1px solid #f0f0f0;
}
</style>
