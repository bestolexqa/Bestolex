<template>
  <div class="bg-[#F4F5F5] dark:bg-gray-800 min-h-[70vh] text-[#191919] dark:text-white">
    <!-- Approved board "4 · سلة طلب العرض" -->
    <div class="max-w-[720px] mx-auto px-4 py-8 md:py-12 flex flex-col gap-6">
      <div class="flex items-center gap-2">
        <button type="button" class="w-11 h-11 flex items-center justify-center rounded-lg hover:bg-white dark:hover:bg-gray-700" :aria-label="isAr ? 'رجوع' : 'Back'" @click="goBack">
          <svg aria-hidden="true" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" :class="isAr ? '' : 'rotate-180'"><path d="M9 6l6 6-6 6" /></svg>
        </button>
        <h1 class="m-0 font-display font-bold text-[26px] md:text-[32px]">{{ isAr ? 'طلب عرض سعر' : 'Quote request' }}</h1>
      </div>

      <div v-if="sent" class="bg-white dark:bg-gray-900 border border-[#E1E3E3] dark:border-gray-700 rounded-xl p-6 flex flex-col gap-3" role="status">
        <h2 class="m-0 font-display font-bold text-[22px]">{{ isAr ? 'وصل طلبك' : 'Your request is in' }}</h2>
        <p class="m-0 text-base leading-[1.8] text-[#333434] dark:text-gray-300">{{ isAr ? 'يتولى طلبك فريق مبيعات خلال الساعة الأولى، ونرسل عرض السعر خلال 3 أيام عمل.' : 'A sales team takes up your request within the first hour, and we send the quotation within 3 working days.' }}</p>
        <NuxtLink :to="localePath('/gold-mining')" class="gm-link self-start">{{ isAr ? 'العودة إلى تعدين الذهب' : 'Back to gold mining' }}</NuxtLink>
      </div>

      <template v-else>
        <section class="flex flex-col gap-3">
          <div class="flex items-baseline justify-between">
            <h2 class="m-0 font-display font-semibold text-[19px]">{{ isAr ? `الموديلات (${cart.count.value})` : `Models (${cart.count.value})` }}</h2>
            <span v-if="sections > 1" class="text-sm text-[#5E5F5F] dark:text-gray-400">{{ isAr ? (sections === 2 ? 'من قسمين مختلفين' : `من ${sections} أقسام`) : `from ${sections} sections` }}</span>
          </div>
          <p v-if="!cart.count.value" class="m-0 bg-white dark:bg-gray-900 border border-[#E1E3E3] dark:border-gray-700 rounded-xl p-4 text-[15px] leading-[1.7] text-[#444545] dark:text-gray-300">
            {{ isAr ? 'لم تضف موديلات بعد. اضغط «أضف» بجانب أي موديل في جداول العائلات، أو اكتب ما تحتاجه في الملاحظات وأرسل الطلب.' : 'No models yet. Press “Add” next to any model in the family tables, or write what you need in the notes and send.' }}
          </p>
          <ul v-else class="list-none m-0 p-0 flex flex-col gap-2.5">
            <li v-for="it in cart.items.value" :key="it.key" class="bg-white dark:bg-gray-900 border border-[#E1E3E3] dark:border-gray-700 rounded-xl p-4 flex flex-col gap-3">
              <div class="flex justify-between items-start gap-3">
                <div class="flex flex-col gap-0.5 min-w-0">
                  <span class="font-display font-bold text-[19px] leading-snug"><bdi>{{ it.label ? t(it.label) : it.model }}</bdi></span>
                  <NuxtLink :to="localePath(`/products/${it.familyId}`)" class="text-sm text-[#444545] dark:text-gray-300 hover:underline">{{ t(it.family) }}، {{ t(it.section) }}</NuxtLink>
                  <span class="text-[13px] text-[#5E5F5F] dark:text-gray-400"><bdi>{{ it.code }}</bdi></span>
                </div>
                <button type="button" class="w-11 h-11 flex-none flex items-center justify-center rounded-lg border border-[#E1E3E3] dark:border-gray-600" :aria-label="(isAr ? 'إزالة ' : 'Remove ') + it.model + (isAr ? ' من الطلب' : ' from the request')" @click="cart.remove(it.key)">
                  <svg aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18" /></svg>
                </button>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-[15px] text-[#444545] dark:text-gray-300">{{ isAr ? 'الكمية' : 'Quantity' }}</span>
                <div class="flex items-center border border-[#A9AAAA] rounded-[10px]">
                  <button type="button" class="w-11 h-11 text-xl" :aria-label="isAr ? 'زيادة الكمية' : 'Increase'" @click="cart.setQty(it.key, it.qty + 1)">+</button>
                  <span class="min-w-[32px] text-center font-display font-bold text-[17px]">{{ it.qty }}</span>
                  <button type="button" class="w-11 h-11 text-xl" :aria-label="isAr ? 'إنقاص الكمية' : 'Decrease'" @click="cart.setQty(it.key, it.qty - 1)">−</button>
                </div>
              </div>
            </li>
          </ul>
          <NuxtLink :to="localePath('/gold-mining')" class="gm-btn-line self-start bg-white dark:bg-transparent">{{ isAr ? 'أضف موديلات أخرى' : 'Add more models' }}</NuxtLink>
        </section>

        <form class="bg-white dark:bg-gray-900 border border-[#E1E3E3] dark:border-gray-700 rounded-xl p-5 flex flex-col gap-4" @submit.prevent="sendMail">
          <h2 class="m-0 font-display font-semibold text-[19px]">{{ isAr ? 'بياناتك' : 'Your details' }}</h2>
          <div class="flex flex-col gap-1.5">
            <label for="q-name" class="text-[15px] font-bold">{{ isAr ? 'الاسم' : 'Name' }} <span class="font-normal text-[#5E5F5F] dark:text-gray-400">{{ isAr ? '(مطلوب)' : '(required)' }}</span></label>
            <input id="q-name" v-model.trim="form.name" type="text" autocomplete="name" required class="gm-input">
          </div>
          <div class="flex flex-col gap-1.5">
            <label for="q-phone" class="text-[15px] font-bold">{{ isAr ? 'الهاتف أو واتساب' : 'Phone or WhatsApp' }} <span class="font-normal text-[#5E5F5F] dark:text-gray-400">{{ isAr ? '(مطلوب)' : '(required)' }}</span></label>
            <input id="q-phone" v-model.trim="form.phone" type="tel" dir="ltr" autocomplete="tel" required placeholder="+974" class="gm-input">
          </div>
          <div class="flex flex-col gap-1.5">
            <label for="q-email" class="text-[15px] font-bold">{{ isAr ? 'البريد الإلكتروني' : 'E-mail' }} <span class="font-normal text-[#5E5F5F] dark:text-gray-400">{{ isAr ? '(اختياري)' : '(optional)' }}</span></label>
            <input id="q-email" v-model.trim="form.email" type="email" dir="ltr" autocomplete="email" class="gm-input">
          </div>
          <div class="flex flex-col gap-1.5">
            <label for="q-country" class="text-[15px] font-bold">{{ isAr ? 'بلد الموقع' : 'Site country' }}</label>
            <select id="q-country" v-model="form.country" class="gm-input">
              <option v-for="c in countries" :key="c.en" :value="c.en">{{ isAr ? c.ar : c.en }}</option>
            </select>
          </div>
          <div class="flex flex-col gap-1.5">
            <label for="q-notes" class="text-[15px] font-bold">{{ isAr ? 'ملاحظات' : 'Notes' }} <span class="font-normal text-[#5E5F5F] dark:text-gray-400">{{ isAr ? '(اختياري)' : '(optional)' }}</span></label>
            <textarea id="q-notes" v-model="form.notes" rows="3" class="gm-input min-h-[96px] py-3" :placeholder="isAr ? 'نوع الخام، الطاقة المطلوبة، مصدر الكهرباء في الموقع' : 'Ore type, capacity you need, power available on site'"></textarea>
          </div>
          <button type="button" class="min-h-[52px] rounded-[10px] bg-[#E99E05] text-[#191919] text-[17px] font-extrabold disabled:opacity-60" :disabled="!ready" @click="sendWhatsapp">{{ isAr ? 'إرسال الطلب عبر واتساب' : 'Send by WhatsApp' }}</button>
          <button type="submit" class="min-h-[52px] rounded-[10px] border border-[#191919] dark:border-gray-300 text-[17px] font-bold disabled:opacity-60" :disabled="!ready || busy">{{ busy ? (isAr ? 'جارٍ الإرسال…' : 'Sending…') : (isAr ? 'إرسال بالبريد' : 'Send by e-mail') }}</button>
          <p v-if="error" class="m-0 text-[15px] text-[#B42318]" role="alert">{{ error }}</p>
          <p class="m-0 text-sm leading-[1.7] text-[#444545] dark:text-gray-300">{{ isAr ? 'نراجع الطلب ونرسل لك عرض السعر والتفاصيل الفنية. ونراجع كل طلب وفق قواعد العقوبات والتصدير قبل إرسال عرض السعر.' : 'We review the request and send you the quotation and technical details. Every request is checked against the applicable sanctions and export rules before we quote.' }}</p>
        </form>
      </template>
    </div>
  </div>
</template>

<script setup>
import { whatsappLink } from '~/utils/leads'
import { trackLead } from '~/utils/track'

const { locale } = useI18n()
const localePath = useLocalePath()
const router = useRouter()
const cart = useQuoteCart()
const isAr = computed(() => locale.value === 'ar')
const t = (v) => (v && typeof v === 'object' ? (v[locale.value] || v.ar || '') : (v || ''))

const countries = [
  { ar: 'مصر', en: 'Egypt' }, { ar: 'المملكة العربية السعودية', en: 'Saudi Arabia' }, { ar: 'قطر', en: 'Qatar' },
  { ar: 'مالي', en: 'Mali' }, { ar: 'بوركينا فاسو', en: 'Burkina Faso' }, { ar: 'غينيا', en: 'Guinea' }, { ar: 'النيجر', en: 'Niger' },
  { ar: 'بلد آخر', en: 'Other' }
]
const form = reactive({ name: '', phone: '', email: '', country: 'Egypt', notes: '' })
const ready = computed(() => !!form.name && !!form.phone && (cart.count.value > 0 || !!form.notes.trim()))
const sections = computed(() => new Set(cart.items.value.map(i => i.section?.en)).size)
const busy = ref(false)
const error = ref('')
const sent = ref(false)

const countryLabel = computed(() => {
  const c = countries.find(x => x.en === form.country)
  return c ? `${c.ar} / ${c.en}` : form.country
})
const lines = () => cart.items.value.map((it, i) => `${i + 1}. ${it.model} — ${it.code} — ${it.family.ar} (${it.section.ar}) × ${it.qty}`)
const message = () => [
  isAr.value ? 'طلب عرض سعر من الموقع' : 'Quote request from the website',
  ...lines(),
  form.notes.trim() ? `${isAr.value ? 'ملاحظات' : 'Notes'}: ${form.notes.trim()}` : '',
  `${isAr.value ? 'الاسم' : 'Name'}: ${form.name}`,
  `${isAr.value ? 'الهاتف' : 'Phone'}: ${form.phone}`,
  form.email ? `${isAr.value ? 'البريد' : 'E-mail'}: ${form.email}` : '',
  `${isAr.value ? 'بلد الموقع' : 'Site country'}: ${countryLabel.value}`
].filter(Boolean).join('\n')

const sendWhatsapp = () => {
  if (!ready.value) return
  trackLead({ formName: 'quote_cart_whatsapp', requestType: 'quote', productId: cart.items.value[0]?.familyId })
  window.open(whatsappLink(message()), '_blank', 'noopener')
}

const sendMail = async () => {
  if (!ready.value || busy.value) return
  busy.value = true
  error.value = ''
  try {
    const names = cart.items.value.map(i => i.model)
    await $fetch('/api/contact', {
      method: 'POST',
      body: {
        name: form.name, phone: form.phone, email: form.email, requestType: 'quote', location: countryLabel.value,
        productId: cart.items.value[0]?.familyId || '',
        productName: names.length ? `${names.slice(0, 6).join('، ')}${names.length > 6 ? ` (+${names.length - 6})` : ''}` : 'طلب عام',
        categoryTitle: [...new Set(cart.items.value.map(i => i.section.ar))].join('، ') || 'تعدين الذهب',
        productUrl: typeof window !== 'undefined' ? window.location.origin + localePath('/quote') : '',
        message: message(),
        isQuoteRequest: true
      }
    })
    trackLead({ formName: 'quote_cart_email', requestType: 'quote', productId: cart.items.value[0]?.familyId })
    cart.clear()
    sent.value = true
  } catch (e) {
    error.value = isAr.value ? 'تعذّر الإرسال. حاول مرة أخرى أو أرسل الطلب عبر واتساب +974 51505014.' : 'Sending failed. Try again or send the request by WhatsApp +974 51505014.'
  } finally {
    busy.value = false
  }
}

const goBack = () => (window.history.length > 1 ? router.back() : navigateTo(localePath('/gold-mining')))

useSeoMeta({
  title: () => (isAr.value ? 'طلب عرض سعر | بيستوليكس' : 'Quote request | Bestolex'),
  description: () => (isAr.value ? 'راجع الموديلات التي أضفتها وأرسل طلب عرض السعر عبر واتساب أو البريد.' : 'Review the models you added and send the quote request by WhatsApp or e-mail.'),
  robots: 'noindex, follow'
})
</script>

<style scoped>
.gm-input { min-height: 48px; box-sizing: border-box; border: 1px solid #A9AAAA; border-radius: 10px; padding: 0 14px; font-size: 16px; font-family: inherit; background: #fff; color: #191919; width: 100%; }
:global(.dark) .gm-input { background: #111827; color: #fff; border-color: #4b5563; }
</style>
