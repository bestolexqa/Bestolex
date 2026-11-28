<template>
  <div class="gm bg-white dark:bg-gray-900 text-[#191919] dark:text-white">
    <!-- Hero: approved board "2 · صفحة فرعية: التكسير والطحن والغربلة" -->
    <section class="ct-gold text-white gm-cut-48">
      <div class="flex flex-wrap items-stretch min-h-[520px] lg:min-h-[560px]">
        <div class="gm-hero-copy flex-[1_1_520px] flex flex-col justify-center" style="padding-bottom: 104px">
          <div class="max-w-[600px] flex flex-col gap-6">
            <nav :aria-label="isAr ? 'مسار الصفحة' : 'Breadcrumb'">
              <ol class="flex flex-wrap gap-2 text-[15px]">
                <li><NuxtLink :to="localePath('/')" class="text-[#B9BABA] hover:text-white">{{ isAr ? 'الرئيسية' : 'Home' }}</NuxtLink></li>
                <li aria-hidden="true" class="text-[#B9BABA]">/</li>
                <li><NuxtLink :to="localePath('/gold-mining')" class="text-[#B9BABA] hover:text-white">{{ isAr ? 'تعدين الذهب' : 'Gold Mining' }}</NuxtLink></li>
                <li aria-hidden="true" class="text-[#B9BABA]">/</li>
                <li aria-current="page" class="text-white font-bold">{{ t(stage.title) }}</li>
              </ol>
            </nav>
            <div class="flex flex-wrap items-center gap-3.5">
              <template v-if="stage.kind === 'line'">
                <div role="img" :aria-label="progressLabel" class="flex gap-1.5">
                  <span v-for="i in stage.lineTotal" :key="i" class="w-[26px] sm:w-[34px] h-1.5 rounded-[3px]" :class="i === stage.n ? 'bg-[#E99E05]' : 'bg-[#8F9090]'"></span>
                </div>
                <span class="text-[15px] text-[#D4D5D5]">{{ progressLabel }}</span>
              </template>
              <span v-else class="text-[15px] text-[#D4D5D5]">{{ isAr ? 'قسم مساند لخط الإنتاج' : 'Support section of the production line' }}</span>
            </div>
            <h1 class="m-0 font-display font-extrabold leading-[1.15] text-[clamp(34px,4.6vw,58px)]">{{ t(stage.title) }}</h1>
            <p class="m-0 text-[17px] md:text-[18px] leading-[1.8] text-[#D4D5D5]">{{ t(stage.lead) }}</p>
            <div class="flex flex-wrap gap-8">
              <div class="flex items-baseline gap-1.5"><span class="font-display font-bold text-[32px]">{{ fmt(stage.families) }}</span><span class="text-[15px] text-[#B9BABA]">{{ isAr ? 'عائلة' : 'families' }}</span></div>
              <div class="flex items-baseline gap-1.5"><span class="font-display font-bold text-[32px]">{{ fmt(stage.models) }}</span><span class="text-[15px] text-[#B9BABA]">{{ isAr ? 'موديلاً' : 'models' }}</span></div>
              <div class="flex items-baseline gap-1.5"><span class="text-[15px] text-[#B9BABA]">{{ isAr ? `في كتالوج ${stage.code}` : `in catalogue ${stage.code}` }}</span></div>
            </div>
            <div class="flex flex-wrap gap-3">
              <NuxtLink :to="localePath('/quote')" class="gm-btn-gold">{{ isAr ? 'اطلب عرض سعر' : 'Request a quote' }}</NuxtLink>
              <a v-if="stage.catalogue" :href="stage.catalogue" download class="gm-btn-ghost" @click="trackDownload">{{ isAr ? `تنزيل كتالوج ${stage.code} (PDF)` : `Download ${stage.code} (PDF)` }}</a>
              <a v-else :href="waCatalogue" target="_blank" rel="noopener" class="gm-btn-ghost">{{ isAr ? `اطلب كتالوج ${stage.code}` : `Request ${stage.code}` }}</a>
            </div>
          </div>
        </div>
        <div class="relative flex-[1_1_560px] min-h-[280px] md:min-h-[440px]">
          <img v-if="stage.cover" :src="stage.cover" :alt="isAr ? `معدات ${t(stage.title)} من غلاف كتالوج ${stage.code}` : `${t(stage.title)} equipment from the ${stage.code} catalogue cover`"
            class="absolute inset-0 w-full h-full object-cover gm-mask" style="object-position: 50% 80%" fetchpriority="high">
        </div>
      </div>
    </section>

    <!-- Group tabs (BXC-04: crushers, grinding, feeding, wear parts) -->
    <nav v-if="stage.groups.length > 1" :aria-label="isAr ? 'أقسام الصفحة' : 'Page sections'" class="border-b border-[#E1E3E3] dark:border-gray-700 bg-white dark:bg-gray-900">
      <div class="max-w-[1200px] mx-auto px-6 pt-2 flex flex-wrap gap-x-8 gap-y-1">
        <template v-for="g in stage.groups" :key="g.id">
          <a v-if="g.count" :href="`#${g.id}`" :aria-current="currentGroup === g.id ? 'true' : undefined" class="flex items-center min-h-[56px] px-1 text-[17px] text-[#191919] dark:text-white" :class="currentGroup === g.id ? 'font-extrabold shadow-[inset_0_-3px_0_#191919] dark:shadow-[inset_0_-3px_0_#E99E05]' : 'font-semibold hover:shadow-[inset_0_-3px_0_#A9AAAA]'" @click="activeGroup = g.id">{{ t(g.title) }}</a>
          <span v-else class="flex items-center gap-2 min-h-[56px] px-1 text-[17px] font-medium text-[#6F7070] dark:text-gray-400">{{ t(g.title) }} <span class="text-[13px]">{{ isAr ? '(قريباً)' : '(soon)' }}</span></span>
        </template>
      </div>
    </nav>

    <!-- Family cards, by group -->
    <template v-for="g in stage.groups" :key="g.id">
      <section v-if="g.count" :id="g.id" class="bg-white dark:bg-gray-900 scroll-mt-24">
        <div class="max-w-[1200px] mx-auto px-6 pt-14 pb-[72px] md:pb-[88px] flex flex-col gap-7">
          <div class="flex flex-wrap justify-between items-end gap-5">
            <div class="flex flex-col gap-2.5 max-w-[620px]">
              <h2 class="m-0 font-display font-bold text-[32px] md:text-[40px] leading-[1.2]">{{ stage.groups.length > 1 ? t(g.title) : (isAr ? 'عائلات المنتجات' : 'Product families') }}</h2>
              <p class="m-0 text-[17px] leading-[1.8] text-[#444545] dark:text-gray-300">{{ familiesLine(g) }}</p>
            </div>
            <div v-if="typesFor(g).length > 1" role="group" :aria-label="isAr ? 'النوع' : 'Type'" class="flex flex-wrap gap-2">
              <button type="button" class="gm-chip" :aria-pressed="(picked[g.id] || 'all') === 'all' ? 'true' : 'false'" @click="picked[g.id] = 'all'">
                {{ isAr ? 'الكل' : 'All' }}<span class="font-display text-sm font-semibold opacity-75">{{ cardsOf(g).length }}</span>
              </button>
              <button v-for="tp in typesFor(g)" :key="tp.id" type="button" class="gm-chip" :aria-pressed="picked[g.id] === tp.id ? 'true' : 'false'" @click="picked[g.id] = tp.id">
                {{ t(tp.chip) }}<span class="font-display text-sm font-semibold opacity-75">{{ cardsOf(g).filter(c => c.type === tp.id).length }}</span>
              </button>
            </div>
          </div>
          <div class="grid gap-x-6 gap-y-10 grid-cols-[repeat(auto-fit,minmax(min(260px,100%),1fr))]">
            <NuxtLink v-for="c in shown(g)" :key="c.id" :to="localePath(`/products/${c.id}`)" class="gm-card flex flex-col gap-4 text-[#191919] dark:text-white">
              <div class="gm-frame relative aspect-[4/3] border border-[#E1E3E3] dark:border-gray-700 rounded-[14px] overflow-hidden bg-white transition">
                <img :src="c.image" :alt="t(c.name)" loading="lazy" class="w-full h-full object-contain block">
                <span v-if="c.badge" class="absolute top-3 start-3 bg-[#191919] text-white text-[13px] font-bold px-2.5 py-1 rounded-md">{{ t(c.badge) }}</span>
              </div>
              <div class="flex flex-col gap-0.5">
                <h3 class="m-0 font-display font-semibold text-[21px] leading-[1.35]">{{ t(c.name) }}</h3>
                <span :lang="isAr ? 'en' : 'ar'" class="text-sm text-[#6F7070] dark:text-gray-400">{{ isAr ? c.name.en : c.name.ar }}</span>
              </div>
              <dl class="m-0 grid grid-cols-3 border-t border-[#E6E7E7] dark:border-gray-700 pt-3">
                <div v-for="(st, k) in c.stats" :key="k" class="flex flex-col gap-0.5 min-w-0" :class="k ? 'border-s border-[#E6E7E7] dark:border-gray-700 ps-2.5' : ''">
                  <dt class="text-[13px] text-[#5E5F5F] dark:text-gray-400 leading-snug">{{ t(st.label) }}</dt>
                  <dd class="m-0 font-display font-semibold text-[17px] leading-snug"><bdi>{{ t(st.value) }}</bdi></dd>
                </div>
              </dl>
            </NuxtLink>
          </div>
        </div>
      </section>
    </template>

    <!-- A stage whose family pages are not published yet -->
    <section v-if="!stage.cards.length" class="bg-white dark:bg-gray-900">
      <div class="max-w-[1200px] mx-auto px-6 py-14 md:py-20 flex flex-wrap gap-8 items-start">
        <div class="flex-[2_1_520px] flex flex-col gap-4">
          <h2 class="m-0 font-display font-bold text-[30px] md:text-[36px] leading-[1.25]">{{ isAr ? 'صفحات العائلات تُضاف قريباً' : 'Family pages coming soon' }}</h2>
          <p class="m-0 text-[17px] leading-[1.8] text-[#444545] dark:text-gray-300">
            {{ isAr
              ? `جداول موديلات هذا القسم في كتالوج ${stage.code}، وننشرها على الموقع تباعاً. إلى ذلك الحين ${stage.catalogue ? 'نزّل الكتالوج' : 'اطلب الكتالوج'} أو أرسل لنا ما تحتاجه، ونرد بعرض فني ومالي.`
              : `The model tables of this section are in catalogue ${stage.code} and go on the site soon. Meanwhile, ${stage.catalogue ? 'download the catalogue' : 'request the catalogue'} or send us what you need and we reply with a technical and commercial offer.` }}
          </p>
        </div>
        <div class="flex-[1_1_300px] flex flex-wrap gap-3">
          <a v-if="stage.catalogue" :href="stage.catalogue" download class="gm-btn-line" @click="trackDownload">{{ isAr ? `تنزيل كتالوج ${stage.code} (PDF)` : `Download ${stage.code} (PDF)` }}</a>
          <a v-else :href="waCatalogue" target="_blank" rel="noopener" class="gm-btn-line">{{ isAr ? `اطلب كتالوج ${stage.code}` : `Request ${stage.code}` }}</a>
          <NuxtLink :to="localePath('/quote')" class="gm-btn-gold">{{ isAr ? 'اطلب عرض سعر' : 'Request a quote' }}</NuxtLink>
        </div>
      </div>
    </section>

    <!-- Next in the production line -->
    <section v-if="stage.next.length" class="bg-[#F4F5F5] dark:bg-gray-800">
      <div class="max-w-[1200px] mx-auto px-6 py-14 md:py-16 flex flex-col gap-7">
        <h2 class="m-0 font-display font-bold text-[26px] md:text-[30px]">{{ nextTitle }}</h2>
        <div class="grid gap-7 grid-cols-[repeat(auto-fit,minmax(min(340px,100%),1fr))]">
          <NuxtLink v-for="s in stage.next" :key="s.id" :to="localePath(`/gold-mining/${s.id}`)" class="gm-card flex items-center gap-[18px] text-[#191919] dark:text-white">
            <div class="gm-frame flex-[0_0_132px] aspect-[4/3] border border-[#E1E3E3] dark:border-gray-600 rounded-xl overflow-hidden bg-white transition">
              <img :src="s.image" :alt="t(s.title)" loading="lazy" class="w-full h-full object-contain block">
            </div>
            <div class="flex flex-col gap-1.5 min-w-0">
              <h3 class="m-0 font-display font-semibold text-xl">{{ t(s.title) }}</h3>
              <p class="m-0 text-[15px] leading-[1.7] text-[#444545] dark:text-gray-300">{{ isAr ? `المرحلة ${s.n}: ` : `Stage ${s.n}: ` }}{{ t(s.short) }}</p>
            </div>
          </NuxtLink>
        </div>
      </div>
    </section>

    <!-- Help band -->
    <section class="bg-[#E99E05] text-[#191919]">
      <div class="max-w-[1200px] mx-auto px-6 py-12 md:py-14 flex flex-wrap items-center justify-between gap-6">
        <div class="flex-[1_1_520px] flex flex-col gap-2.5">
          <h2 class="m-0 font-display font-bold text-[26px] md:text-[32px] leading-[1.3]">{{ t(stage.cta.title) }}</h2>
          <p class="m-0 text-[17px] md:text-[18px] leading-[1.8]">{{ t(stage.cta.text) }}</p>
        </div>
        <a :href="waAsk" target="_blank" rel="noopener" class="inline-flex items-center gap-2.5 min-h-[56px] px-[26px] rounded-[10px] bg-[#191919] text-white text-[17px] font-extrabold">
          {{ isAr ? 'اسأل عبر واتساب' : 'Ask on WhatsApp' }} <span dir="ltr">+974 5150 5014</span>
        </a>
      </div>
    </section>
  </div>
</template>

<script setup>
import { whatsappLink } from '~/utils/leads'

const { locale } = useI18n()
const localePath = useLocalePath()
const route = useRoute()
const isAr = computed(() => locale.value === 'ar')
const activeGroup = ref(null)
const currentGroup = computed(() => activeGroup.value || stage.value?.groups?.find(g => g.count)?.id)
const t = (v) => (v && typeof v === 'object' ? (v[locale.value] || v.ar || '') : (v || ''))
const fmt = (n) => (typeof n === 'number' ? n.toLocaleString('en-US') : '')

const id = String(route.params.stage || '')
const { data: stage } = await useFetch(`/api/gold-mining/stage/${id}`, { key: `gold-mining-stage-${id}`, default: () => null })
if (!stage.value) throw createError({ statusCode: 404, statusMessage: 'Page not found', fatal: true })

const progressLabel = computed(() => isAr.value ? `المرحلة ${stage.value.n} من ${stage.value.lineTotal} في خط الإنتاج` : `Stage ${stage.value.n} of ${stage.value.lineTotal} in the production line`)
const nextTitle = computed(() => stage.value.kind === 'line'
  ? (isAr.value ? `بعد ${t(stage.value.title)} في خط الإنتاج` : `After ${t(stage.value.title).toLowerCase()} in the production line`)
  : (isAr.value ? 'مراحل خط الإنتاج' : 'Production line stages'))

const picked = reactive({})
const cardsOf = (g) => stage.value.cards.filter(c => c.group === g.id)
const typesFor = (g) => stage.value.types.filter(tp => cardsOf(g).some(c => c.type === tp.id))
const shown = (g) => cardsOf(g).filter(c => !picked[g.id] || picked[g.id] === 'all' || c.type === picked[g.id])
const familiesLine = (g) => {
  const n = cardsOf(g).length
  const base = isAr.value ? (n === 1 ? 'عائلة واحدة.' : n === 2 ? 'عائلتان.' : `${n} عائلة.`) : `${n} ${n === 1 ? 'family' : 'families'}.`
  return g.note ? `${base} ${t(g.note)}` : base
}

const waCatalogue = computed(() => whatsappLink(isAr.value ? `السلام عليكم، أرجو إرسال كتالوج ${stage.value.code} (${stage.value.title.ar}).` : `Hello, please send me the ${stage.value.code} catalogue (${stage.value.title.en}).`))
const waAsk = computed(() => whatsappLink(isAr.value ? `السلام عليكم، أحتاج مساعدة في اختيار معدات ${stage.value.title.ar}.` : `Hello, I need help choosing ${stage.value.title.en} equipment.`))
const trackDownload = () => {
  try { $fetch('/api/analytics/track', { method: 'POST', body: { event_type: 'datasheet_request', target_name: `كتالوج ${stage.value.code}` } }) } catch (e) {}
}

const SITE = 'https://www.bestolex.com'
const title = computed(() => isAr.value ? `${stage.value.title.ar}: معدات تعدين الذهب | بيستوليكس` : `${stage.value.title.en}: Gold Mining Equipment | Bestolex`)
const desc = computed(() => `${t(stage.value.lead)} ${isAr.value ? 'التوريد للشرق الأوسط وأفريقيا.' : 'Supply to the Middle East and Africa.'}`)
useSeoMeta({
  title, description: desc, ogTitle: title, ogDescription: desc, ogType: 'website', twitterCard: 'summary_large_image',
  ogImage: () => (stage.value.cover ? `${SITE}${stage.value.cover}` : `${SITE}/gold-mining/hero.webp`),
  // A stage with no family pages yet stays out of the index until its pages are published.
  robots: () => (stage.value.cards.length ? 'index, follow' : 'noindex, follow')
})
useHead(() => ({
  script: [{
    type: 'application/ld+json',
    innerHTML: JSON.stringify({
      '@context': 'https://schema.org',
      '@graph': [
        { '@type': 'CollectionPage', name: title.value, description: desc.value, url: `${SITE}${localePath(`/gold-mining/${id}`)}`, inLanguage: isAr.value ? 'ar' : 'en' },
        { '@type': 'BreadcrumbList', itemListElement: [
          { '@type': 'ListItem', position: 1, name: isAr.value ? 'الرئيسية' : 'Home', item: `${SITE}${localePath('/')}` },
          { '@type': 'ListItem', position: 2, name: isAr.value ? 'تعدين الذهب' : 'Gold Mining', item: `${SITE}${localePath('/gold-mining')}` },
          { '@type': 'ListItem', position: 3, name: t(stage.value.title), item: `${SITE}${localePath(`/gold-mining/${id}`)}` }
        ] },
        ...(stage.value.cards.length ? [{ '@type': 'ItemList', itemListElement: stage.value.cards.map((c, i) => ({ '@type': 'ListItem', position: i + 1, name: t(c.name), url: `${SITE}${localePath(`/products/${c.id}`)}` })) }] : [])
      ]
    })
  }]
}))
</script>
