<template>
  <div class="bg-white dark:bg-gray-900 text-[#191919] dark:text-white">
    <!-- Breadcrumb -->
    <div class="bg-white dark:bg-gray-900 border-b border-[#E8E9E9] dark:border-gray-700">
      <div class="max-w-[1200px] mx-auto px-6 py-4">
        <nav :aria-label="isAr ? 'مسار الصفحة' : 'Breadcrumb'">
          <ol class="flex flex-wrap gap-2 text-[15px] text-[#5E5F5F] dark:text-gray-400">
            <li><NuxtLink :to="localePath('/')" class="hover:text-[#191919] dark:hover:text-white">{{ isAr ? 'الرئيسية' : 'Home' }}</NuxtLink></li>
            <li aria-hidden="true">/</li>
            <li><NuxtLink :to="localePath('/gold-mining')" class="hover:text-[#191919] dark:hover:text-white">{{ isAr ? 'تعدين الذهب' : 'Gold Mining' }}</NuxtLink></li>
            <li aria-hidden="true">/</li>
            <li><NuxtLink :to="localePath(`/gold-mining/${ctx.stage.id}`) + (ctx.group ? `#${ctx.group.id}` : '')" class="hover:text-[#191919] dark:hover:text-white">{{ t(ctx.group && ctx.stage.id === 'crushing-grinding-screening' ? ctx.group.title : ctx.stage.title) }}</NuxtLink></li>
            <li aria-hidden="true">/</li>
            <li aria-current="page" class="text-[#191919] dark:text-white font-bold">{{ t(product.name) }}</li>
          </ol>
        </nav>
      </div>
    </div>

    <!-- Hero: approved board "3 · صفحة عائلة: الكسارات الفكية" -->
    <section class="bg-white dark:bg-gray-900">
      <div class="max-w-[1200px] mx-auto px-6 pt-8 md:pt-12 pb-12 md:pb-14 flex flex-wrap gap-8 md:gap-12 items-center">
        <div class="flex-[1_1_460px] flex flex-col gap-5 md:gap-[22px] order-2 md:order-1">
          <span v-if="ctx.badge" class="self-start text-sm font-bold border border-[#191919] dark:border-gray-300 rounded-md px-2.5 py-1">{{ t(ctx.badge) }}</span>
          <div class="flex flex-col gap-1.5">
            <h1 class="m-0 font-display font-extrabold leading-[1.15] text-[clamp(32px,4.4vw,56px)]">{{ t(product.name) }}</h1>
            <span :lang="isAr ? 'en' : 'ar'" class="text-[17px] text-[#5E5F5F] dark:text-gray-400">{{ isAr ? product.name.en : product.name.ar }}</span>
          </div>
          <p class="m-0 text-[17px] md:text-[18px] leading-[1.8] text-[#333434] dark:text-gray-300">{{ intro }}</p>
          <div class="flex flex-wrap gap-y-3.5 border-y border-[#E1E3E3] dark:border-gray-700 py-4">
            <div v-for="(st, k) in heroStats" :key="k" class="flex flex-col gap-0.5 px-[18px] first:ps-0" :class="k ? 'border-s border-[#E1E3E3] dark:border-gray-700' : ''">
              <span class="font-display font-bold text-[22px] md:text-[26px] leading-tight"><bdi>{{ st.value }}</bdi></span>
              <span class="text-[13px] md:text-sm text-[#5E5F5F] dark:text-gray-400">{{ st.label }}</span>
            </div>
          </div>
          <div class="flex flex-wrap gap-3">
            <a href="#models" class="gm-btn-gold">{{ isAr ? 'اطلب عرض سعر' : 'Request a quote' }}</a>
            <a v-if="ctx.stage.catalogue" :href="ctx.stage.catalogue" download class="gm-btn-line">{{ isAr ? 'تنزيل الكتالوج (PDF)' : 'Download the catalogue (PDF)' }}</a>
            <a v-else :href="waCatalogue" target="_blank" rel="noopener" class="gm-btn-line">{{ isAr ? `اطلب كتالوج ${ctx.stage.code}` : `Request catalogue ${ctx.stage.code}` }}</a>
          </div>
        </div>
        <figure class="flex-[1_1_480px] m-0 flex flex-col gap-2.5 order-1 md:order-2 w-full">
          <div class="aspect-[4/3] rounded-[18px] bg-[#EEF0F0] overflow-hidden">
            <img :src="images[shot]" :alt="t(product.name)" class="w-full h-full object-contain p-5 md:p-7 mix-blend-multiply block" fetchpriority="high">
          </div>
          <div v-if="images.length > 1" class="flex gap-2">
            <button v-for="(im, i) in images" :key="im" type="button" class="w-16 h-16 rounded-lg bg-[#EEF0F0] overflow-hidden border-2" :class="i === shot ? 'border-[#191919] dark:border-[#E99E05]' : 'border-transparent'" :aria-label="(isAr ? 'الصورة ' : 'Image ') + (i + 1)" @click="shot = i">
              <img :src="im" alt="" class="w-full h-full object-contain mix-blend-multiply">
            </button>
          </div>
          <figcaption class="text-sm text-[#5E5F5F] dark:text-gray-400">{{ isAr ? `الصورة من كتالوج ${ctx.stage.code}، الإصدار ${ctx.stage.edition}` : `Image from catalogue ${ctx.stage.code}, edition ${ctx.stage.edition}` }}</figcaption>
        </figure>
      </div>
    </section>

    <!-- Models and specifications, with the quote panel -->
    <section id="models" class="bg-[#F4F5F5] dark:bg-gray-800 scroll-mt-20">
      <div class="max-w-[1200px] mx-auto px-4 md:px-6 pt-10 md:pt-12 pb-28 md:pb-[72px] flex flex-wrap gap-8 items-start">
        <div class="flex-[999_1_720px] min-w-0 flex flex-col gap-7">
          <div class="flex flex-wrap items-center justify-between gap-4">
            <h2 class="m-0 font-display font-bold text-[26px] md:text-[32px]">{{ isAr ? 'الموديلات والمواصفات' : 'Models and specifications' }}</h2>
            <div v-if="capBands" role="group" :aria-label="isAr ? 'الطاقة الإنتاجية' : 'Capacity'" class="flex items-center gap-2 overflow-x-auto max-w-full pb-1">
              <span class="text-[15px] text-[#444545] dark:text-gray-300 whitespace-nowrap">{{ isAr ? 'الطاقة الإنتاجية:' : 'Capacity:' }}</span>
              <button v-for="b in bands" :key="b.id" type="button" class="gm-chip whitespace-nowrap" :aria-pressed="band === b.id ? 'true' : 'false'" @click="band = b.id">{{ b.label }}</button>
            </div>
          </div>

          <template v-for="tp in series" :key="tp.id">
            <section v-if="tp.rows.length" class="flex flex-col gap-3">
              <!-- desktop header / mobile accordion button -->
              <button type="button" class="md:hidden flex items-center justify-between gap-3 text-start bg-white dark:bg-gray-900 border border-[#E1E3E3] dark:border-gray-700 rounded-xl px-4 py-3.5 min-h-[56px]" :aria-expanded="isOpen(tp.id) ? 'true' : 'false'" @click="toggleOpen(tp.id)">
                <span class="flex flex-col">
                  <span class="font-display font-semibold text-[17px]">{{ t(tp.label) }}</span>
                  <span class="text-[13px] text-[#5E5F5F] dark:text-gray-400"><template v-if="tp.code"><bdi>{{ tp.code }}</bdi>، </template>{{ countLabel(tp) }}</span>
                </span>
                <svg aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path :d="isOpen(tp.id) ? 'M6 15l6-6 6 6' : 'M6 9l6 6 6-6'" /></svg>
              </button>
              <div class="hidden md:flex flex-wrap items-baseline gap-x-3.5 gap-y-1.5">
                <h3 class="m-0 font-display font-semibold text-[23px]">{{ t(tp.label) }}</h3>
                <span v-if="tp.code" class="font-display font-medium text-[15px] text-[#5E5F5F] dark:text-gray-400"><bdi>{{ tp.code }}</bdi></span>
                <span class="text-[15px] text-[#5E5F5F] dark:text-gray-400">{{ countLabel(tp) }}</span>
              </div>
              <p v-if="tp.intro" class="m-0 text-[15px] text-[#444545] dark:text-gray-300" :class="isOpen(tp.id) ? '' : 'hidden md:block'">{{ t(tp.intro) }}</p>

              <!-- Desktop table: one row per model -->
              <div class="hidden md:block overflow-x-auto bg-white dark:bg-gray-900 border border-[#E1E3E3] dark:border-gray-700 rounded-xl">
                <table class="w-full border-collapse text-[15px]" :style="{ minWidth: Math.max(600, 230 + tp.cols.length * 92) + 'px' }">
                  <thead>
                    <tr>
                      <th scope="col" class="gm-th">{{ isAr ? 'الموديل' : 'Model' }}</th>
                      <th v-for="c in tp.cols" :key="c.key" scope="col" class="gm-th">{{ t(c.label) }}</th>
                      <th scope="col" class="gm-th gm-stick">{{ isAr ? 'طلب العرض' : 'Quote' }}</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="r in tp.rows" :id="r.anchor" :key="r.key" class="border-b border-[#EEF0F0] dark:border-gray-800 last:border-0 scroll-mt-24" :class="cart.has(r.key) ? 'gm-picked bg-[#FFF6E3] dark:bg-[#3a2f12]' : ''">
                      <th scope="row" class="px-3 py-2.5 text-start font-display font-bold text-base whitespace-nowrap align-top">
                        <bdi>{{ t(r.name) }}</bdi>
                        <span v-if="!tp.code" class="block font-sans font-normal text-xs text-[#5E5F5F] dark:text-gray-400 mt-0.5"><bdi>{{ r.code }}</bdi></span>
                      </th>
                      <td v-for="c in tp.cols" :key="c.key" class="px-3 py-2.5 text-[#2E2F2F] dark:text-gray-200 align-top" :class="wide(r, c) ? 'min-w-[200px]' : 'whitespace-nowrap'" style="font-variant-numeric: tabular-nums">
                        <bdi>{{ cell(r, c) }}</bdi>
                      </td>
                      <td class="px-3 py-1.5 align-top gm-stick">
                        <button type="button" class="gm-add" :aria-pressed="cart.has(r.key) ? 'true' : 'false'" :aria-label="(cart.has(r.key) ? (isAr ? 'إزالة ' : 'Remove ') : (isAr ? 'إضافة ' : 'Add ')) + t(r.name) + (isAr ? ' إلى طلب العرض' : ' to the quote')" @click="toggle(r)">
                          <svg v-if="cart.has(r.key)" aria-hidden="true" width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 8.5l3 3 7-7" /></svg>
                          {{ cart.has(r.key) ? (isAr ? 'في الطلب' : 'Added') : (isAr ? 'أضف' : 'Add') }}
                        </button>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>

              <!-- Mobile: one card per model -->
              <div v-show="isOpen(tp.id)" class="md:hidden flex flex-col border border-[#E1E3E3] dark:border-gray-700 rounded-xl bg-white dark:bg-gray-900 overflow-hidden">
                <div v-for="r in tp.rows" :id="r.anchor + '-m'" :key="r.key" class="border-t first:border-t-0 border-[#EEF0F0] dark:border-gray-800 px-4 py-3.5 flex flex-col gap-3" :class="cart.has(r.key) ? 'bg-[#FFF6E3] dark:bg-[#3a2f12]' : ''">
                  <div class="flex items-center justify-between gap-3">
                    <span class="flex flex-col min-w-0">
                      <span class="font-display font-bold text-[18px] leading-snug"><bdi>{{ t(r.name) }}</bdi></span>
                      <span v-if="!tp.code" class="text-xs text-[#5E5F5F] dark:text-gray-400"><bdi>{{ r.code }}</bdi></span>
                    </span>
                    <button type="button" class="gm-add flex-none" :aria-pressed="cart.has(r.key) ? 'true' : 'false'" :aria-label="(cart.has(r.key) ? (isAr ? 'إزالة ' : 'Remove ') : (isAr ? 'إضافة ' : 'Add ')) + t(r.name) + (isAr ? ' إلى طلب العرض' : ' to the quote')" @click="toggle(r)">
                      {{ cart.has(r.key) ? (isAr ? 'في الطلب' : 'Added') : (isAr ? 'أضف' : 'Add') }}
                    </button>
                  </div>
                  <dl class="m-0 grid grid-cols-3 gap-2">
                    <div v-for="c in tp.keyCols" :key="c.key" class="flex flex-col min-w-0">
                      <dt class="text-xs text-[#5E5F5F] dark:text-gray-400 leading-snug">{{ t(c.label) }}</dt>
                      <dd class="m-0 font-display font-semibold text-[15px] leading-snug break-words"><bdi>{{ cell(r, c) }}</bdi></dd>
                    </div>
                  </dl>
                  <dl v-if="more[r.key]" class="m-0 flex flex-col gap-1.5 text-sm bg-[#FAFAFA] dark:bg-gray-800 rounded-lg p-3">
                    <div v-for="c in tp.cols" :key="c.key" class="flex justify-between gap-3">
                      <dt class="text-[#5E5F5F] dark:text-gray-400">{{ t(c.label) }}</dt>
                      <dd class="m-0 text-end"><bdi>{{ cell(r, c) }}</bdi></dd>
                    </div>
                  </dl>
                  <button v-if="tp.cols.length > tp.keyCols.length" type="button" class="self-start text-sm font-bold underline decoration-[#E99E05] decoration-2 underline-offset-4 min-h-[36px]" :aria-expanded="more[r.key] ? 'true' : 'false'" @click="more[r.key] = !more[r.key]">
                    {{ more[r.key] ? (isAr ? 'إخفاء التفاصيل' : 'Hide details') : (isAr ? 'كل المواصفات' : 'All specifications') }}
                  </button>
                </div>
              </div>
            </section>
          </template>
          <p class="m-0 text-sm text-[#5E5F5F] dark:text-gray-400">{{ t(family.source) }}</p>
        </div>

        <!-- Quote panel (desktop) -->
        <aside :aria-label="isAr ? 'طلب العرض' : 'Quote request'" class="hidden md:flex flex-[1_1_300px] sticky top-24 bg-[#191919] text-white rounded-2xl p-6 flex-col gap-4">
          <div class="flex items-center justify-between">
            <h2 class="m-0 font-display font-bold text-[22px]">{{ isAr ? 'طلب العرض' : 'Quote request' }}</h2>
            <span class="min-w-[32px] h-8 px-2 rounded-2xl bg-[#E99E05] text-[#191919] inline-flex items-center justify-center font-display font-bold text-[17px]">{{ cart.count.value }}</span>
          </div>
          <p v-if="!cart.count.value" class="m-0 text-[15px] leading-[1.7] text-[#C4C5C5]">{{ isAr ? 'اضغط «أضف» بجانب أي موديل. يمكنك الجمع بين موديلات من أقسام مختلفة في طلب واحد.' : 'Press “Add” next to any model. One request can mix models from different sections.' }}</p>
          <ul v-else class="list-none m-0 p-0 flex flex-col max-h-[320px] overflow-y-auto">
            <li v-for="it in cart.items.value" :key="it.key" class="flex justify-between items-center gap-3 py-3 border-t border-[#333434]">
              <span class="flex flex-col gap-0.5 min-w-0">
                <span class="font-display font-bold text-[16px] leading-snug"><bdi>{{ it.label ? t(it.label) : it.model }}</bdi></span>
                <span class="text-[13px] text-[#B9BABA]"><bdi>{{ it.code }}</bdi></span>
              </span>
              <span class="text-sm text-[#C4C5C5] whitespace-nowrap">{{ isAr ? (it.qty === 1 ? '1 وحدة' : `${it.qty} وحدات`) : `${it.qty} ${it.qty === 1 ? 'unit' : 'units'}` }}</span>
            </li>
          </ul>
          <NuxtLink :to="localePath('/quote')" class="flex items-center justify-center min-h-[52px] rounded-[10px] bg-[#E99E05] text-[#191919] text-[17px] font-extrabold">{{ isAr ? 'مراجعة الطلب وإرساله' : 'Review and send' }}</NuxtLink>
          <a :href="waAsk" target="_blank" rel="noopener" class="text-[15px] text-white text-center underline">{{ isAr ? 'أو اسأل عبر واتساب' : 'or ask on WhatsApp' }} <span dir="ltr">+974 5150 5014</span></a>
        </aside>
      </div>
    </section>

    <!-- Mobile: sticky review bar -->
    <div v-if="cart.count.value" class="md:hidden sticky bottom-0 z-30 bg-white dark:bg-gray-900 border-t border-[#E1E3E3] dark:border-gray-700 px-4 pt-3 pb-4">
      <NuxtLink :to="localePath('/quote')" class="flex items-center justify-center min-h-[52px] rounded-[10px] bg-[#E99E05] text-[#191919] text-[17px] font-extrabold">
        {{ isAr ? `مراجعة الطلب (${cart.count.value})` : `Review the request (${cart.count.value})` }}
      </NuxtLink>
    </div>

    <!-- How to choose, features, FAQ, related families -->
    <section class="bg-white dark:bg-gray-900">
      <div class="max-w-[1200px] mx-auto px-6 py-14 md:py-[72px] flex flex-col gap-14 md:gap-16">
        <div v-if="ctx.how" class="flex flex-col gap-6">
          <h2 class="m-0 font-display font-bold text-[26px] md:text-[32px]">{{ isAr ? `كيف تختار ${howName}` : `How to choose ${howName}` }}</h2>
          <div class="grid gap-7 grid-cols-[repeat(auto-fit,minmax(min(240px,100%),1fr))]">
            <div v-for="(h, i) in ctx.how" :key="i" class="flex flex-col gap-2 border-t-[3px] border-[#191919] dark:border-[#E99E05] pt-4">
              <h3 class="m-0 font-display font-semibold text-xl">{{ t(h.title) }}</h3>
              <p class="m-0 text-base leading-[1.8] text-[#444545] dark:text-gray-300">{{ t(h.text) }}</p>
            </div>
          </div>
        </div>
        <div v-if="features.length" class="flex flex-col gap-5">
          <h2 class="m-0 font-display font-bold text-[24px] md:text-[28px]">{{ isAr ? 'ما في هذه العائلة' : 'What this family covers' }}</h2>
          <ul class="list-none m-0 p-0 grid gap-x-8 gap-y-3 grid-cols-[repeat(auto-fit,minmax(min(320px,100%),1fr))]">
            <li v-for="(f, i) in features" :key="i" class="flex gap-3 text-base leading-[1.75] text-[#333434] dark:text-gray-300">
              <span aria-hidden="true" class="mt-2.5 w-2 h-2 rounded-full bg-[#E99E05] flex-none"></span><span>{{ f }}</span>
            </li>
          </ul>
        </div>
        <div class="flex flex-wrap gap-12">
          <div class="flex-[1_1_520px] flex flex-col gap-2">
            <h2 class="m-0 mb-2 font-display font-bold text-[26px] md:text-[32px]">{{ isAr ? 'أسئلة شائعة' : 'Frequently asked questions' }}</h2>
            <details v-for="(f, i) in faqs" :key="i" class="border-b border-[#E1E3E3] dark:border-gray-700" :open="i === 0">
              <summary class="cursor-pointer py-[18px] font-display font-semibold text-[18px] md:text-[19px]">{{ f.q }}</summary>
              <p class="m-0 mb-[18px] text-base leading-[1.8] text-[#333434] dark:text-gray-300">{{ f.a }}</p>
            </details>
          </div>
          <div v-if="ctx.related.length" class="flex-[1_1_420px] flex flex-col gap-5">
            <h2 class="m-0 font-display font-bold text-[26px] md:text-[32px]">{{ isAr ? 'عائلات مرتبطة' : 'Related families' }}</h2>
            <div class="grid grid-cols-2 gap-5">
              <NuxtLink v-for="c in ctx.related" :key="c.id" :to="localePath(`/products/${c.id}`)" class="gm-card flex flex-col gap-3 text-[#191919] dark:text-white">
                <div class="gm-frame aspect-[4/3] border border-[#E1E3E3] dark:border-gray-700 rounded-xl overflow-hidden bg-white transition"><img :src="c.image" :alt="t(c.name)" loading="lazy" class="w-full h-full object-contain block"></div>
                <h3 class="m-0 font-display font-semibold text-[17px] md:text-lg leading-snug">{{ t(c.name) }}</h3>
              </NuxtLink>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { whatsappLink } from '~/utils/leads'
import { rowId } from '~/utils/miningUi'

const props = defineProps({
  product: { type: Object, required: true },
  family: { type: Object, required: true },
  ctx: { type: Object, required: true },
  locale: { type: String, default: 'ar' }
})

const localePath = useLocalePath()
const cart = useQuoteCart()
// The mobile review bar sits at the bottom; lift the floating WhatsApp, back-to-top and cookie buttons above it.
if (import.meta.client) {
  const setBar = (on) => document.documentElement.classList.toggle('bx-has-bar', !!on)
  watch(() => cart.count.value, n => setBar(n > 0))
  onMounted(() => setBar(cart.count.value > 0))
  onBeforeUnmount(() => setBar(false))
}
const isAr = computed(() => props.locale === 'ar')
const t = (v) => (v && typeof v === 'object' ? (v[props.locale] || v.ar || '') : (v || ''))
const plain = (s) => String(s || '').replace(/[⁦-⁩⁠]/g, '')

const intro = computed(() => t(props.product.description).split('\n')[0])
const images = computed(() => (props.product.images?.length ? props.product.images : [props.product.image]).filter(Boolean))
const shot = ref(0)
const features = computed(() => props.product.features?.[props.locale] || [])
const faqs = computed(() => props.product.faq?.[props.locale] || [])
const howName = computed(() => {
  const n = t(props.product.name)
  return isAr.value ? n : n.toLowerCase()
})

// Columns of one type: the family rows that hold a value for at least one of its models.
const has = (m, key) => !!(m.specs && m.specs[key] && t(m.specs[key]))
const baseCode = (code) => String(code || '').split(' / ')[0]
const series = computed(() => (props.family.types || []).map((tp) => {
  const cols = (props.family.rows || []).filter(r => tp.models.some(m => has(m, r.key)))
  const keys = (tp.keyRows || props.family.keyRows || []).filter(k => cols.some(c => c.key === k))
  const keyCols = (keys.length ? keys.map(k => cols.find(c => c.key === k)) : cols.slice(0, 3)).slice(0, 3)
  const codes = [...new Set(tp.models.map(m => baseCode(m.code)))]
  const rows = tp.models.filter(m => inBand(m, tp)).map((m) => {
    const code = baseCode(m.code)
    const model = m.name?.en || m.name?.ar || ''
    return { key: `${code} / ${model}`, code, model, name: m.name, specs: m.specs, anchor: rowId(code, plain(model)) }
  })
  return { id: tp.id, label: tp.label, intro: tp.intro, countUnit: tp.countUnit, total: tp.models.length, code: codes.length === 1 ? codes[0] : '', cols, keyCols, rows }
}))
const cell = (r, c) => (r.specs?.[c.key] ? t(r.specs[c.key]) : (isAr.value ? '—' : '—'))
const wide = (r, c) => cell(r, c).length > 28

const countLabel = (tp) => {
  const n = tp.total
  const u = tp.countUnit || props.family.countUnit
  if (u) return isAr.value ? (n === 1 ? u.ar[0] : n === 2 ? u.ar[1] : `${n} ${u.ar[2]}`) : `${n} ${n === 1 ? u.en[0] : u.en[1]}`
  return isAr.value ? (n === 1 ? 'موديل واحد' : n === 2 ? 'موديلان' : n <= 10 ? `${n} موديلات` : `${n} موديلاً`) : `${n} ${n === 1 ? 'model' : 'models'}`
}

// Capacity filter (t/h), shown when the family lists capacities per model.
const band = ref('all')
const capKey = (tp) => (props.family.rows || []).find(r => /t\/h/.test(r.label?.en || '') && tp.models.some(m => has(m, r.key)))?.key
const maxCap = (m, key) => {
  const nums = plain(m.specs?.[key]?.en || '').replace(/,/g, '').match(/\d+(\.\d+)?/g)
  return nums ? Math.max(...nums.map(Number)) : null
}
function inBand (m, tp) {
  if (band.value === 'all') return true
  const key = capKey(tp)
  if (!key) return true
  const v = maxCap(m, key)
  if (v === null) return true
  if (band.value === 'small') return v <= 20
  if (band.value === 'mid') return v > 20 && v <= 200
  return v > 200
}
const capBands = computed(() => {
  const types = props.family.types || []
  const n = types.reduce((a, tp) => a + (capKey(tp) ? tp.models.length : 0), 0)
  return n >= 8
})
const bands = computed(() => [
  { id: 'all', label: isAr.value ? 'الكل' : 'All' },
  { id: 'small', label: isAr.value ? 'حتى 20 طن/ساعة' : 'Up to 20 t/h' },
  { id: 'mid', label: '20–200' },
  { id: 'large', label: isAr.value ? 'أكثر من 200' : 'Over 200' }
])

// Hero figures: the page stats, then the number of series or lines.
const heroStats = computed(() => {
  const out = (props.ctx.stats || []).map(s => ({ value: plain(t(s.value)), label: t(s.label) }))
  const n = (props.family.types || []).length
  if (n > 1 && out.length < 4) out.push({ value: String(n), label: isAr.value ? (n <= 10 ? 'سلاسل وأنواع' : 'سلسلة ونوعاً') : 'series and types' })
  return out
})

// Mobile accordions: the first series open.
const opened = reactive({})
const isOpen = (id) => (id in opened ? opened[id] : id === (props.family.types || [])[0]?.id)
const toggleOpen = (id) => { opened[id] = !isOpen(id) }
const more = reactive({})

const toggle = (r) => cart.toggle({
  code: r.code, model: plain(r.model), label: { ar: plain(r.name?.ar || r.model), en: plain(r.name?.en || r.model) },
  familyId: props.product.id, family: { ar: props.product.name.ar, en: props.product.name.en }, section: { ar: 'تعدين الذهب', en: 'Gold Mining' }
})

const waCatalogue = computed(() => whatsappLink(isAr.value ? `السلام عليكم، أرجو إرسال كتالوج ${props.ctx.stage.code}.` : `Hello, please send me catalogue ${props.ctx.stage.code}.`))
const waAsk = computed(() => whatsappLink(isAr.value ? `السلام عليكم، لدي سؤال عن ${props.product.name.ar}.` : `Hello, I have a question about ${props.product.name.en}.`))

// Open the series of a model linked from the search (#m-…) on phones.
onMounted(() => {
  const h = decodeURIComponent(window.location.hash || '').slice(1)
  if (!h) return
  for (const tp of series.value) {
    if (tp.rows.some(r => r.anchor === h)) {
      opened[tp.id] = true
      nextTick(() => document.getElementById(window.innerWidth < 768 ? `${h}-m` : h)?.scrollIntoView({ block: 'center' }))
    }
  }
})
</script>

<style scoped>
.gm-th { text-align: start; vertical-align: bottom; padding: 10px 12px; font-size: 13px; line-height: 1.35; font-weight: 700; color: #444545; min-width: 72px; border-bottom: 1px solid #E1E3E3; background: #FAFAFA; }
:global(.dark) .gm-th { color: #d1d5db; background: #111827; border-color: #374151; }
.gm-add { font-size: 14px; font-weight: 700; min-height: 44px; min-width: 96px; padding: 0 14px; border-radius: 8px; cursor: pointer; white-space: nowrap; display: inline-flex; align-items: center; justify-content: center; gap: 6px; background: #fff; color: #191919; border: 1px solid #8F9090; }
/* The quote column stays in view when a wide table scrolls sideways. */
.gm-stick { position: sticky; inset-inline-end: 0; box-shadow: -8px 0 12px -10px rgba(0,0,0,.25); }
:global([dir='rtl']) .gm-stick { box-shadow: 8px 0 12px -10px rgba(0,0,0,.25); }
th.gm-stick { background: #FAFAFA; }
td.gm-stick { background: #fff; }
tr.gm-picked td.gm-stick { background: #FFF6E3; }
:global(.dark) th.gm-stick { background: #111827; }
:global(.dark) td.gm-stick { background: #111827; }
:global(.dark) tr.gm-picked td.gm-stick { background: #3a2f12; }
.gm-add[aria-pressed='true'] { background: #191919; color: #fff; border-color: #191919; }
</style>
