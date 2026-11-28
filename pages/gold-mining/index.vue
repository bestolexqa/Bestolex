<template>
  <div class="gm bg-white dark:bg-gray-900 text-[#191919] dark:text-white" :dir="isAr ? 'rtl' : 'ltr'">
    <!-- Hero: approved board "1 · صفحة قسم تعدين الذهب" -->
    <section class="ct-gold text-white gm-cut-64">
      <div class="flex flex-wrap items-stretch min-h-[600px] lg:min-h-[680px]">
        <div class="gm-hero-copy flex-[1_1_520px] flex flex-col justify-center">
          <div class="max-w-[580px] flex flex-col gap-[26px]">
            <nav :aria-label="isAr ? 'مسار الصفحة' : 'Breadcrumb'">
              <ol class="flex flex-wrap gap-2 text-[15px]">
                <li><NuxtLink :to="localePath('/')" class="text-[#B9BABA] hover:text-white">{{ isAr ? 'الرئيسية' : 'Home' }}</NuxtLink></li>
                <li aria-hidden="true" class="text-[#B9BABA]">/</li>
                <li aria-current="page" class="text-white font-bold">{{ isAr ? 'تعدين الذهب' : 'Gold Mining' }}</li>
              </ol>
            </nav>
            <h1 class="m-0 font-display font-extrabold leading-[1.15] text-[clamp(38px,5vw,64px)]">
              <template v-if="isAr">معدات تعدين الذهب<br>من التنقيب حتى السبيكة</template>
              <template v-else>Gold mining equipment<br>from exploration to bullion</template>
            </h1>
            <p class="m-0 text-[17px] md:text-[19px] leading-[1.8] text-[#D4D5D5] max-w-[520px]">
              {{ isAr
                ? 'آلات وقطع غيار ومستهلكات لكل مرحلة في خط إنتاج الذهب، للمعدّنين وشركات التعدين في الشرق الأوسط وأفريقيا. بيستوليكس وكيل وموزّع لكثير من المصانع العالمية في الشرق الأوسط وأفريقيا.'
                : 'Machines, spare parts and consumables for every stage of the gold production line, for miners and mining companies in the Middle East and Africa. Bestolex is an agent and distributor for many international manufacturers in the Middle East and Africa.' }}
            </p>
            <div class="flex flex-wrap gap-3">
              <NuxtLink :to="localePath('/quote')" class="gm-btn-gold">{{ isAr ? 'ابدأ طلب عرض سعر' : 'Start a quote request' }}</NuxtLink>
              <a :href="waLink" target="_blank" rel="noopener" class="gm-btn-ghost" :aria-label="isAr ? 'تواصل عبر واتساب على الرقم +974 5150 5014' : 'WhatsApp +974 5150 5014'">
                {{ isAr ? 'واتساب' : 'WhatsApp' }} <span dir="ltr">+974 5150 5014</span>
              </a>
            </div>
            <form role="search" class="flex flex-col gap-2.5 mt-2" @submit.prevent="runSearch">
              <label for="hub-search" class="text-[15px] text-[#D4D5D5]">
                {{ isAr ? `ابحث بين ${fmt(hub?.published?.models)} موديلاً في ${fmt(hub?.published?.families)} عائلة` : `Search ${fmt(hub?.published?.models)} models in ${fmt(hub?.published?.families)} families` }}
              </label>
              <div class="flex">
                <input id="hub-search" v-model="q" type="search" autocomplete="off" :placeholder="isAr ? 'اسم الآلة أو كود BX، مثل: كسارة فكية' : 'Machine name or BX code, e.g. jaw crusher'"
                  class="flex-1 min-w-0 h-14 border-0 px-[18px] text-[17px] text-[#191919] bg-white rounded-s-[10px] rounded-e-none font-sans">
                <button type="submit" class="h-14 px-[26px] border-0 rounded-e-[10px] rounded-s-none bg-[#E99E05] text-[#191919] text-[17px] font-extrabold cursor-pointer">{{ isAr ? 'بحث' : 'Search' }}</button>
              </div>
              <div v-if="searched" aria-live="polite" class="bg-white text-[#191919] rounded-[10px] max-h-[360px] overflow-y-auto">
                <p v-if="!hits.length" class="m-0 px-4 py-3 text-[15px] text-[#444545]">
                  {{ isAr ? 'لا نتيجة على الموقع بعد. أرسل اسم الآلة أو الكود على واتساب ونرد عليك.' : 'No match on the site yet. Send us the machine name or code on WhatsApp.' }}
                </p>
                <ul v-else class="list-none m-0 p-0">
                  <li v-for="(h, i) in hits" :key="i" class="border-b border-[#EEF0F0] last:border-0">
                    <NuxtLink :to="localePath(`/products/${h.id}`) + (h.kind === 'model' ? `#${rowId(h.code, t(h.model))}` : '')" class="flex flex-col gap-0.5 px-4 py-2.5 hover:bg-[#FFF6E3]">
                      <span class="font-display font-bold text-[16px]"><bdi>{{ h.kind === 'model' ? t(h.model) : t(h.name) }}</bdi></span>
                      <span class="text-[13px] text-[#5E5F5F]">
                        <template v-if="h.kind === 'model'"><bdi>{{ h.code }}</bdi> · {{ t(h.family) }}</template>
                        <template v-else>{{ t(h.stage.title) }}</template>
                      </span>
                    </NuxtLink>
                  </li>
                </ul>
              </div>
            </form>
          </div>
        </div>
        <div class="relative flex-[1_1_560px] min-h-[300px] md:min-h-[440px]">
          <img src="/gold-mining/hero.webp" :alt="isAr ? 'معدات الغسيل وتركيز الذهب من غلاف كتالوج BXC-05: مجاري حلزونية وأجهزة جيج ومركّز طارد مركزي' : 'Washing and gold concentration equipment from the BXC-05 catalogue cover: spirals, jigs and a centrifugal concentrator'"
            class="absolute inset-0 w-full h-full object-cover gm-mask" style="object-position: 50% 78%" fetchpriority="high">
        </div>
      </div>
    </section>

    <!-- Production line -->
    <section class="bg-white dark:bg-gray-900">
      <div class="max-w-[1200px] mx-auto px-6 pt-14 pb-[88px] flex flex-col gap-6">
        <div class="flex flex-col gap-3 max-w-[680px]">
          <h2 class="m-0 font-display font-bold text-[32px] md:text-[42px] leading-[1.2]">{{ isAr ? 'خط الإنتاج، مرحلة بمرحلة' : 'The production line, stage by stage' }}</h2>
          <p class="m-0 text-[17px] md:text-[18px] leading-[1.8] text-[#444545] dark:text-gray-300">
            {{ isAr ? 'سبع مراحل بترتيب العمل في الموقع، من البحث عن الخام إلى صب السبيكة. لكل مرحلة كتالوج وعائلات منتجات.' : 'Seven stages in the order of work on site, from finding the ore to pouring the bar. Each stage has its catalogue and product families.' }}
          </p>
        </div>
        <ol class="list-none m-0 p-0">
          <li v-for="(s, i) in line" :key="s.id" class="relative flex flex-wrap items-start gap-5 md:gap-7 py-6 md:py-8" :class="i < line.length - 1 ? 'border-b border-[#E4E6E6] dark:border-gray-700' : ''">
            <div aria-hidden="true" class="absolute w-0.5 bg-[#E99E05] gm-rail" :style="railStyle(i)"></div>
            <div aria-hidden="true" class="relative flex-[0_0_56px] h-14 rounded-full bg-[#191919] text-[#E99E05] flex items-center justify-center font-display font-extrabold text-2xl">{{ s.n }}</div>
            <div class="flex-[1_1_240px] min-w-0 flex flex-col gap-3 pt-1.5">
              <div class="flex items-start gap-3">
              <div class="flex-1 min-w-0 flex flex-wrap items-baseline gap-x-3.5 gap-y-1.5">
                <h3 class="m-0 font-display font-bold text-[23px] md:text-[28px] leading-[1.3]">
                  <span class="sr-only">{{ isAr ? `المرحلة ${s.n}: ` : `Stage ${s.n}: ` }}</span>{{ t(s.title) }}
                </h3>
                <span class="font-display font-medium text-base text-[#5E5F5F] dark:text-gray-400">{{ s.code }}</span>
                <span v-if="s.licensed" class="text-sm font-bold border border-[#191919] dark:border-gray-300 rounded-md px-2.5 py-0.5">{{ isAr ? 'للجهات المرخّصة فقط' : 'Licensed buyers only' }}</span>
              </div>
              <!-- Mobile: a small photo beside the title keeps each stage row short -->
              <img :src="s.image" alt="" aria-hidden="true" loading="lazy" class="md:hidden flex-none w-[84px] h-[64px] rounded-[10px] bg-[#EEF0F0] object-cover">
              </div>
              <p class="m-0 text-[16px] md:text-[17px] leading-[1.8] text-[#444545] dark:text-gray-300 max-w-[560px]">{{ t(s.short) }}</p>
              <div class="flex flex-wrap items-baseline gap-x-7 gap-y-3">
                <div class="flex items-baseline gap-1.5"><span class="font-display font-bold text-[22px] md:text-[26px]">{{ fmt(s.families) }}</span><span class="text-[15px] text-[#5E5F5F] dark:text-gray-400">{{ isAr ? 'عائلة' : 'families' }}</span></div>
                <div class="flex items-baseline gap-1.5"><span class="font-display font-bold text-[22px] md:text-[26px]">{{ fmt(s.models) }}</span><span class="text-[15px] text-[#5E5F5F] dark:text-gray-400">{{ isAr ? 'موديلاً' : 'models' }}</span></div>
                <NuxtLink v-if="!s.licensed" :to="localePath(`/gold-mining/${s.id}`)" class="ms-auto gm-link" :aria-label="(isAr ? 'تصفّح مرحلة ' : 'Browse the stage ') + t(s.title)">{{ isAr ? 'تصفّح المرحلة' : 'Browse the stage' }}</NuxtLink>
                <NuxtLink v-else :to="localePath('/contact')" class="ms-auto gm-link">{{ isAr ? 'استفسر عن التوريد' : 'Ask about supply' }}</NuxtLink>
              </div>
            </div>
            <div class="hidden md:block flex-[0_1_320px] aspect-[16/10] rounded-[14px] overflow-hidden bg-[#EEF0F0]">
              <img :src="s.image" :alt="t(s.title)" loading="lazy" class="w-full h-full object-cover">
            </div>
          </li>
        </ol>
        <p class="m-0 text-sm text-[#5E5F5F] dark:text-gray-400">
          {{ isAr ? 'أعداد العائلات والموديلات من كتالوجاتنا الحالية، وصفحاتها على الموقع تُضاف مرحلة بعد مرحلة.' : 'Family and model counts come from our current catalogues; their pages are added to the site stage by stage.' }}
        </p>
      </div>
    </section>

    <!-- Support sections -->
    <section class="ct-gold text-white">
      <div class="max-w-[1200px] mx-auto px-6 py-16 md:py-[88px] flex flex-col gap-9">
        <div class="flex flex-col gap-3 max-w-[680px]">
          <h2 class="m-0 font-display font-bold text-[32px] md:text-[42px] leading-[1.2]">{{ isAr ? 'الأقسام المساندة' : 'Support sections' }}</h2>
          <p class="m-0 text-[17px] md:text-[18px] leading-[1.8] text-[#D4D5D5]">{{ isAr ? 'ما يحتاجه الموقع حول خط الإنتاج: نقل اللب، والمختبر، والأسطول، والسلامة.' : 'What the site needs around the line: slurry handling, the laboratory, the fleet and safety.' }}</p>
        </div>
        <div class="grid gap-5 grid-cols-[repeat(auto-fit,minmax(min(260px,100%),1fr))]">
          <NuxtLink v-for="s in support" :key="s.id" :to="localePath(`/gold-mining/${s.id}`)" class="flex flex-col text-white bg-[#222323] border border-[#343535] rounded-[14px] overflow-hidden hover:border-[#E99E05] transition">
            <img :src="s.image" :alt="t(s.title)" loading="lazy" class="w-full aspect-video object-cover block">
            <div class="px-5 pt-5 pb-6 flex flex-col gap-2.5">
              <span class="font-display font-medium text-[15px] text-[#B9BABA]">{{ s.code.replace(' · ', isAr ? ' و ' : ' & ') }}</span>
              <h3 class="m-0 font-display font-semibold text-[23px] leading-[1.3]">{{ t(s.title) }}</h3>
              <p class="m-0 text-base leading-[1.75] text-[#C4C5C5]">{{ t(s.short) }}</p>
              <div class="flex gap-5 mt-1">
                <div class="flex items-baseline gap-1.5"><span class="font-display font-bold text-[22px]">{{ fmt(s.families) }}</span><span class="text-[15px] text-[#B9BABA]">{{ isAr ? 'عائلة' : 'families' }}</span></div>
                <div class="flex items-baseline gap-1.5"><span class="font-display font-bold text-[22px]">{{ fmt(s.models) }}</span><span class="text-[15px] text-[#B9BABA]">{{ isAr ? 'موديلاً' : 'models' }}</span></div>
              </div>
            </div>
          </NuxtLink>
        </div>
        <div class="grid gap-5 grid-cols-[repeat(auto-fit,minmax(min(480px,100%),1fr))]">
          <NuxtLink :to="localePath('/sourcing')" class="flex flex-wrap text-white bg-[#222323] border border-[#343535] rounded-[14px] overflow-hidden hover:border-[#E99E05] transition">
            <div class="flex-[1_1_260px] p-7 flex flex-col gap-3 justify-center">
              <span class="self-start text-sm font-bold text-[#191919] bg-[#E99E05] rounded-md px-2.5 py-0.5">{{ isAr ? 'عند الطلب' : 'On request' }}</span>
              <h3 class="m-0 font-display font-semibold text-[25px] leading-[1.3]">{{ isAr ? 'المعدات الثقيلة' : 'Heavy equipment' }}</h3>
              <p class="m-0 text-base leading-[1.75] text-[#C4C5C5]">{{ isAr ? 'شاحنات تعدين، ورافعات على شاحنات، ولوادر للمناجم تحت الأرض، نورّدها حسب الطلب.' : 'Mining trucks, truck-mounted cranes and underground loaders, supplied on request.' }}</p>
            </div>
            <img src="/gold-mining/support/heavy-equipment.webp" :alt="isAr ? 'شاحنة تعدين ورافعة على شاحنة من غلاف كتالوج BXH-01' : 'Mining truck and truck-mounted crane from the BXH-01 catalogue cover'" loading="lazy" class="flex-[1_1_240px] min-w-0 h-60 object-cover block">
          </NuxtLink>
          <NuxtLink :to="localePath('/products/category/energy-solutions')" class="flex flex-wrap text-white bg-[#222323] border border-[#343535] rounded-[14px] overflow-hidden hover:border-[#E99E05] transition">
            <div class="flex-[1_1_260px] p-7 flex flex-col gap-3 justify-center">
              <span class="self-start text-sm font-bold text-[#191919] bg-[#E99E05] rounded-md px-2.5 py-0.5">{{ isAr ? 'قسم مستقل' : 'Separate section' }}</span>
              <h3 class="m-0 font-display font-semibold text-[25px] leading-[1.3]">{{ isAr ? 'الطاقة للموقع: مولدات الديزل والغاز' : 'Site power: diesel and gas generators' }}</h3>
              <p class="m-0 text-base leading-[1.75] text-[#C4C5C5]">{{ isAr ? 'مجموعات توليد ومولدات محمولة ومحركات لتشغيل الكسارات ومصانع المعالجة بعيداً عن الشبكة.' : 'Generator sets, portable generators and engines to run crushers and processing plants off the grid.' }}</p>
            </div>
            <div class="flex-[1_1_240px] min-w-0 h-60 bg-[#EEF0F0]">
              <img src="/products/diesel-generator-sets/diesel-genset-silent.webp" :alt="isAr ? 'مجموعة توليد ديزل صامتة' : 'Silent diesel generator set'" loading="lazy" class="w-full h-full object-contain p-4 mix-blend-multiply">
            </div>
          </NuxtLink>
        </div>
      </div>
    </section>

    <!-- Quote in three steps, with the owner's terms (28 Nov 2026) -->
    <section class="bg-white dark:bg-gray-900">
      <div class="max-w-[1200px] mx-auto px-6 py-16 md:py-[88px] flex flex-wrap gap-10 md:gap-14 items-start">
        <div class="flex-[1_1_320px] flex flex-col gap-[18px] items-start">
          <h2 class="m-0 font-display font-bold text-[30px] md:text-[38px] leading-[1.25]">{{ isAr ? 'اطلب عرض السعر في ثلاث خطوات' : 'Request a quote in three steps' }}</h2>
          <p class="m-0 text-[17px] md:text-[18px] leading-[1.8] text-[#444545] dark:text-gray-300">{{ isAr ? 'طلب واحد يجمع موديلات من مراحل مختلفة، ومن قسم حلول الطاقة أيضاً.' : 'One request can hold models from different stages, and from the energy section too.' }}</p>
          <NuxtLink :to="localePath('/quote')" class="gm-btn-gold">{{ isAr ? 'ابدأ طلب عرض سعر' : 'Start a quote request' }}</NuxtLink>
        </div>
        <div class="flex-[2_1_560px] flex flex-col gap-10">
          <ol class="list-none m-0 p-0 grid gap-7 grid-cols-[repeat(auto-fit,minmax(min(200px,100%),1fr))]">
            <li v-for="(st, i) in steps" :key="i" class="border-t-[3px] border-[#E99E05] pt-5 flex flex-col gap-3">
              <span class="font-display font-extrabold text-5xl leading-none">{{ i + 1 }}</span>
              <p class="m-0 text-[17px] leading-[1.8] text-[#333434] dark:text-gray-300">{{ st }}</p>
            </li>
          </ol>
          <ul class="list-none m-0 p-0 grid gap-x-8 gap-y-3 grid-cols-[repeat(auto-fit,minmax(min(260px,100%),1fr))] bg-[#F4F5F5] dark:bg-gray-800 rounded-[14px] p-6">
            <li v-for="(term, i) in terms" :key="i" class="flex gap-3 text-[15px] leading-[1.7] text-[#333434] dark:text-gray-300">
              <span aria-hidden="true" class="mt-2 w-2 h-2 rounded-full bg-[#E99E05] flex-none"></span>{{ term }}
            </li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Catalogues -->
    <section class="bg-[#F4F5F5] dark:bg-gray-800">
      <div class="max-w-[1200px] mx-auto px-6 py-16 md:py-20 flex flex-col gap-7">
        <div class="flex flex-wrap justify-between items-end gap-x-6 gap-y-3">
          <h2 class="m-0 font-display font-bold text-[30px] md:text-[38px] leading-[1.25]">{{ isAr ? 'كتالوجات القسم' : 'Section catalogues' }}</h2>
          <p class="m-0 text-[17px] text-[#5E5F5F] dark:text-gray-400">{{ isAr ? `${catalogues.length} كتالوجاً بصيغة PDF` : `${catalogues.length} PDF catalogues` }}</p>
        </div>
        <ul class="list-none m-0 p-0 grid gap-x-10 grid-cols-[repeat(auto-fit,minmax(min(360px,100%),1fr))]">
          <li v-for="c in catalogues" :key="c.code" class="border-t border-[#D5D7D7] dark:border-gray-600">
            <a :href="c.file || waCatalogue(c)" :target="c.file ? undefined : '_blank'" :rel="c.file ? undefined : 'noopener'" :download="c.file ? '' : undefined"
              class="flex items-center gap-4 min-h-[60px] text-[#191919] dark:text-white hover:bg-white/60 dark:hover:bg-gray-700/50"
              :aria-label="c.file ? (isAr ? `تنزيل كتالوج ${t(c.title)}، الإصدار ${c.edition}، PDF` : `Download the ${t(c.title)} catalogue, edition ${c.edition}, PDF`) : (isAr ? `اطلب نسخة من كتالوج ${t(c.title)} عبر واتساب` : `Request the ${t(c.title)} catalogue on WhatsApp`)" @click="c.file && trackDownload(c)">
              <span class="flex-[0_0_76px] font-display font-bold text-[17px]">{{ c.code }}</span>
              <span class="flex-1 text-[16px] md:text-[17px] font-medium">{{ t(c.title) }}</span>
              <span class="text-sm text-[#5E5F5F] dark:text-gray-400 whitespace-nowrap">{{ isAr ? `الإصدار ${c.edition}` : `Ed. ${c.edition}` }}</span>
              <span v-if="c.file" class="text-[13px] font-bold border border-[#191919] dark:border-gray-300 rounded-[5px] px-[7px] py-0.5">PDF</span>
              <span v-else class="text-[13px] font-bold text-[#5E5F5F] dark:text-gray-400 whitespace-nowrap">{{ isAr ? 'اطلب نسخة' : 'Request' }}</span>
            </a>
          </li>
        </ul>
        <p class="m-0 text-sm text-[#5E5F5F] dark:text-gray-400">{{ isAr ? 'الكتالوجات التي عليها «اطلب نسخة» تُحدَّث إصداراتها، ونرسلها لك على واتساب أو البريد.' : 'Catalogues marked “Request” are being updated; we send them by WhatsApp or e-mail.' }}</p>
      </div>
    </section>
  </div>
</template>

<script setup>
import { whatsappLink } from '~/utils/leads'
import { rowId } from '~/utils/miningUi'

const { locale } = useI18n()
const localePath = useLocalePath()
const isAr = computed(() => locale.value === 'ar')
const t = (v) => (v && typeof v === 'object' ? (v[locale.value] || v.ar || '') : (v || ''))
const fmt = (n) => (typeof n === 'number' ? n.toLocaleString('en-US') : '')

const { data: hub } = await useFetch('/api/gold-mining', { key: 'gold-mining-hub', default: () => null })
const line = computed(() => hub.value?.line || [])
const support = computed(() => hub.value?.support || [])
const catalogues = computed(() => hub.value?.catalogues || [])

const railStyle = (i) => {
  const last = line.value.length - 1
  const side = isAr.value ? { right: '27px' } : { left: '27px' }
  if (i === 0) return { ...side, top: '60px', bottom: '0' }
  if (i === last) return { ...side, top: '0', height: '60px' }
  return { ...side, top: '0', bottom: '0' }
}

const waLink = computed(() => whatsappLink(isAr.value ? 'السلام عليكم، أريد عرض سعر لمعدات تعدين الذهب.' : 'Hello, I would like a quote for gold mining equipment.'))
const waCatalogue = (c) => whatsappLink(isAr.value ? `السلام عليكم، أرجو إرسال كتالوج ${c.code} (${c.title.ar}).` : `Hello, please send me the ${c.code} catalogue (${c.title.en}).`)
const trackDownload = (c) => {
  try { $fetch('/api/analytics/track', { method: 'POST', body: { event_type: 'datasheet_request', target_name: `كتالوج ${c.code}` } }) } catch (e) {}
}

const steps = computed(() => isAr.value
  ? ['أضف الموديلات التي تحتاجها من أي مرحلة إلى طلب العرض.', 'اكتب اسمك وهاتفك وبلد الموقع، وأرسل الطلب عبر واتساب أو البريد.', 'نرسل لك عرض السعر والتفاصيل الفنية للموديلات المطلوبة.']
  : ['Add the models you need, from any stage, to the quote request.', 'Enter your name, phone and site country, and send the request by WhatsApp or e-mail.', 'We send you the quotation and the technical details of the models.'])
const terms = computed(() => isAr.value
  ? ['يتولى طلبك فريق مبيعات خلال الساعة الأولى.', 'نرسل عرض السعر خلال 3 أيام عمل.', 'شروط التصدير والتسليم نتفق عليها حسب كل طلب وبلد الوجهة.', 'نراجع كل طلب وفق قواعد العقوبات والتصدير قبل إرسال عرض السعر.']
  : ['A sales team takes up your request within the first hour.', 'We send the quotation within 3 working days.', 'Export and delivery terms are agreed for each order and destination.', 'Every request is checked against the applicable sanctions and export rules before we quote.'])

// Search: family names, model names and BX codes on the site.
const q = ref('')
const hits = ref([])
const searched = ref(false)
const runSearch = async () => {
  if (!q.value.trim()) { searched.value = false; return }
  const res = await $fetch('/api/gold-mining/search', { query: { q: q.value } }).catch(() => ({ hits: [] }))
  hits.value = res.hits || []
  searched.value = true
}

const SITE = 'https://www.bestolex.com'
const title = computed(() => isAr.value ? 'معدات تعدين الذهب من التنقيب حتى السبيكة | بيستوليكس' : 'Gold Mining Equipment from Exploration to Bullion | Bestolex')
const desc = computed(() => isAr.value
  ? 'معدات تعدين الذهب لكل مرحلة في خط الإنتاج: التنقيب والحفر، ومستهلكات الحفر، والتكسير والطحن، والغسيل والتركيز، والمعالجة والصهر، مع المختبر والمضخات والسلامة. التوريد للشرق الأوسط وأفريقيا.'
  : 'Gold mining equipment for every stage of the production line: exploration and drilling, drilling consumables, crushing and grinding, washing and concentration, processing and smelting, plus laboratory, pumps and safety. Supply to the Middle East and Africa.')
useSeoMeta({ title, description: desc, ogTitle: title, ogDescription: desc, ogImage: `${SITE}/gold-mining/hero.webp`, ogType: 'website', twitterCard: 'summary_large_image' })
useHead(() => ({
  script: [{
    type: 'application/ld+json',
    innerHTML: JSON.stringify({
      '@context': 'https://schema.org',
      '@graph': [
        { '@type': 'CollectionPage', name: title.value, description: desc.value, url: `${SITE}${localePath('/gold-mining')}`, inLanguage: isAr.value ? 'ar' : 'en' },
        { '@type': 'BreadcrumbList', itemListElement: [
          { '@type': 'ListItem', position: 1, name: isAr.value ? 'الرئيسية' : 'Home', item: `${SITE}${localePath('/')}` },
          { '@type': 'ListItem', position: 2, name: isAr.value ? 'تعدين الذهب' : 'Gold Mining', item: `${SITE}${localePath('/gold-mining')}` }
        ] },
        { '@type': 'ItemList', itemListElement: line.value.filter(s => !s.licensed).map((s, i) => ({ '@type': 'ListItem', position: i + 1, name: t(s.title), url: `${SITE}${localePath(`/gold-mining/${s.id}`)}` })) }
      ]
    })
  }]
}))
</script>
