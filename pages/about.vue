<template>
  <div class="bg-white dark:bg-secondary text-ink dark:text-gray-100">

    <!-- Hero -->
    <section class="relative bg-[#191919] text-white overflow-hidden">
      <NuxtImg
        src="https://cdn.bestolex.com/bestolex/about/showroom-v2.jpg"
        alt=""
        aria-hidden="true"
        class="absolute inset-0 w-full h-full object-cover opacity-20"
        format="webp"
        loading="eager"
      />
      <div class="absolute inset-0 bg-gradient-to-l from-[#191919] via-[#191919]/85 to-[#191919]/60 rtl:bg-gradient-to-r"></div>
      <div class="container mx-auto px-4 md:px-8 py-16 md:py-24 relative">
        <nav class="text-sm text-gray-400 mb-8" :aria-label="t('مسار التنقل', 'Breadcrumb')">
          <NuxtLink :to="localePath('/')" class="hover:text-primary">{{ t('الرئيسية', 'Home') }}</NuxtLink>
          <span class="mx-2">/</span>
          <span class="text-gray-200">{{ t('من نحن', 'About us') }}</span>
        </nav>
        <div class="max-w-4xl">
          <p class="text-primary font-bold mb-4">{{ t('من نحن', 'About us') }}</p>
          <h1 class="font-display text-4xl md:text-6xl font-extrabold leading-[1.2] md:leading-[1.25] mb-5">
            {{ t('بيستوليكس لتجارة الآلات والمعدات الثقيلة', 'Bestolex Trading of Heavy Equipment and Machinery') }}
          </h1>
          <p class="font-display text-xl md:text-2xl text-primary font-bold mb-6">
            {{ t('قوة تدفع أعمالكم... ثقة تدوم', 'Power That Drives Your Business. Trust That Lasts') }}
          </p>
          <p class="text-lg md:text-xl text-gray-300 leading-relaxed max-w-[65ch] mb-8">
            {{ t('شركة قطرية في الدوحة، والوكيل الحصري لمنتجات ساب تك في قطر، وموزّعون معتمدون للعديد من المصانع والشركات العالمية. نورّد ونركّب ونصون أنظمة التحميل والمستودعات، ومعدات النفايات وإعادة التدوير، والحماية المحيطية، والأبواب الصناعية، ونقدّم حلول الطاقة، ونورّد حسب الطلب أي آلة أو خط إنتاج من مصانع حول العالم.',
                 'A Qatari company based in Doha, the exclusive SAB TECH agent in Qatar, and an authorised distributor for many international manufacturers and companies. We supply, install and maintain loading and warehouse systems, waste and recycling equipment, perimeter protection and industrial doors, provide energy solutions, and source any machine or production line on request from factories worldwide.') }}
          </p>
          <div class="flex flex-wrap gap-3">
            <NuxtLink :to="localePath('/contact')" class="bg-primary text-[#191919] font-bold px-7 py-3.5 rounded-lg hover:bg-[#f2b02a] transition">
              {{ t('اطلب عرض سعر', 'Request a quote') }}
            </NuxtLink>
            <NuxtLink :to="localePath('/sourcing')" class="border border-gray-500 text-white font-bold px-7 py-3.5 rounded-lg hover:border-primary hover:text-primary transition">
              {{ t('التوريد حسب الطلب', 'Sourcing on request') }}
            </NuxtLink>
          </div>
        </div>
        <dl class="grid grid-cols-2 lg:grid-cols-4 gap-4 mt-14">
          <div v-for="f in heroFacts" :key="f.ar" class="border-t-2 border-primary pt-4">
            <dt class="text-sm text-gray-400">{{ t(f.lar, f.len) }}</dt>
            <dd class="font-display text-lg md:text-xl font-bold mt-1">{{ t(f.ar, f.en) }}</dd>
          </div>
        </dl>
      </div>
    </section>

    <!-- Who we are -->
    <section class="py-16 md:py-24">
      <div class="container mx-auto px-4 md:px-8">
        <h2 class="font-display text-3xl md:text-4xl font-bold mb-10">{{ t('بيستوليكس في سطور', 'Bestolex at a glance') }}</h2>
        <div class="grid lg:grid-cols-3 gap-8 lg:gap-10">
          <div v-for="w in whoWeAre" :key="w.lar" class="border-t-2 border-primary pt-5">
            <p class="text-primary font-bold text-sm mb-3">{{ t(w.lar, w.len) }}</p>
            <p class="text-lg leading-relaxed text-slate dark:text-gray-300">{{ t(w.ar, w.en) }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Vision, mission -->
    <section class="py-16 md:py-20 bg-surface dark:bg-[#0f1216]">
      <div class="container mx-auto px-4 md:px-8 grid md:grid-cols-2 gap-6">
        <div class="bg-white dark:bg-gray-800 border border-line dark:border-gray-700 rounded-2xl p-8 md:p-10">
          <p class="text-primary font-bold mb-2">{{ t('رؤيتنا', 'Our vision') }}</p>
          <p class="font-display text-xl md:text-2xl font-bold leading-relaxed">
            {{ t('أن تكون بيستوليكس الشريك الموثوق الذي تعتمد عليه المنشآت الصناعية واللوجستية في قطر لرفع كفاءتها التشغيلية وتعزيز سلامتها واستدامتها.',
                 'For Bestolex to be the trusted partner that industrial and logistics facilities in Qatar rely on to raise their operating efficiency, safety and sustainability.') }}
          </p>
        </div>
        <div class="bg-white dark:bg-gray-800 border border-line dark:border-gray-700 rounded-2xl p-8 md:p-10">
          <p class="text-primary font-bold mb-2">{{ t('رسالتنا', 'Our mission') }}</p>
          <p class="font-display text-xl md:text-2xl font-bold leading-relaxed">
            {{ t('توفير حلول هندسية وتجارية متكاملة تلائم المتطلبات الفعلية لكل مشروع، من الاستشارة الفنية واختيار المعدات إلى التوريد والتركيب والتشغيل والصيانة، مع الالتزام بالجودة والسلامة وموثوقية الخدمة.',
                 'To deliver integrated engineering and commercial solutions tailored to the actual requirements of each project, from technical consultation and equipment selection to supply, installation, commissioning and maintenance, while maintaining quality, safety and service reliability.') }}
          </p>
        </div>
      </div>
    </section>

    <!-- Business areas -->
    <section class="py-16 md:py-24">
      <div class="container mx-auto px-4 md:px-8">
        <div class="max-w-3xl mb-10">
          <h2 class="font-display text-3xl md:text-4xl font-bold mb-3">{{ t('مجالات عملنا', 'What we do') }}</h2>
          <p class="text-slate dark:text-gray-400 text-lg">{{ t('أربعة خطوط بوكالة حصرية، وحلول طاقة، ومعدات ثقيلة، وتوريد حسب الطلب في قطر، ومعدات تعدين وطاقة للمشاريع في الشرق الأوسط وأفريقيا.', 'Four exclusive lines, energy solutions, heavy equipment and sourcing on request in Qatar, plus mining and energy equipment for projects in the Middle East and Africa.') }}</p>
        </div>

        <h3 class="font-display text-xl font-bold mb-5 flex items-center gap-3">
          <span class="w-2 h-6 bg-primary rounded-full" aria-hidden="true"></span>
          {{ t('الخطوط الأربعة عبر وكالة ساب تك الحصرية', 'The four lines, through the exclusive SAB TECH agency') }}
        </h3>
        <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-5 mb-14">
          <NuxtLink v-for="a in agencyLines" :key="a.link" :to="localePath(a.link)" class="group border border-line dark:border-gray-700 rounded-2xl overflow-hidden bg-white dark:bg-gray-800 hover:border-primary transition flex flex-col">
            <NuxtImg :src="a.img" :alt="t(a.ar, a.en)" class="w-full aspect-[4/3] object-cover" width="600" height="450" format="webp" loading="lazy" />
            <div class="p-5 flex-1 flex flex-col">
              <h4 class="font-display text-lg font-bold mb-2 group-hover:text-primary transition">{{ t(a.ar, a.en) }}</h4>
              <p class="text-sm text-slate dark:text-gray-400 leading-relaxed flex-1">{{ t(a.dar, a.den) }}</p>
              <span class="text-primary font-bold text-sm mt-4">{{ t('عرض المنتجات', 'View products') }} <span class="rtl:rotate-180 inline-block" aria-hidden="true">&rarr;</span></span>
            </div>
          </NuxtLink>
        </div>

        <h3 class="font-display text-xl font-bold mb-5 flex items-center gap-3">
          <span class="w-2 h-6 bg-primary rounded-full" aria-hidden="true"></span>
          {{ t('حلول ومجالات أخرى في قطر', 'More solutions in Qatar') }}
        </h3>
        <div class="grid md:grid-cols-3 gap-5 mb-14">
          <NuxtLink v-for="a in otherLines" :key="a.ar" :to="localePath(a.link) + (a.hash || '')" class="group border border-line dark:border-gray-700 rounded-2xl overflow-hidden bg-white dark:bg-gray-800 hover:border-primary transition flex flex-col">
            <div v-if="a.icons" class="w-full aspect-[16/9] bg-[#191919] grid grid-cols-4 place-items-center p-5 gap-3" aria-hidden="true">
              <span v-for="ic in a.icons" :key="ic" class="w-11 h-11 rounded-xl bg-primary/15 text-primary flex items-center justify-center"><SourcingIcon :name="ic" class="w-6 h-6" /></span>
            </div>
            <NuxtImg v-else :src="a.img" :alt="t(a.ar, a.en)" class="w-full aspect-[16/9] object-cover" width="800" height="450" format="webp" loading="lazy" />
            <div class="p-5 flex-1 flex flex-col">
              <h4 class="font-display text-lg font-bold mb-2 group-hover:text-primary transition">{{ t(a.ar, a.en) }}</h4>
              <p class="text-sm text-slate dark:text-gray-400 leading-relaxed flex-1">{{ t(a.dar, a.den) }}</p>
              <span class="text-primary font-bold text-sm mt-4">{{ t(a.car, a.cen) }} <span class="rtl:rotate-180 inline-block" aria-hidden="true">&rarr;</span></span>
            </div>
          </NuxtLink>
        </div>

        <h3 class="font-display text-xl font-bold mb-5 flex items-center gap-3">
          <span class="w-2 h-6 bg-primary rounded-full" aria-hidden="true"></span>
          {{ t('التصدير والمشاريع الدولية', 'Export and international projects') }}
        </h3>
        <div class="grid lg:grid-cols-12 gap-0 border border-line dark:border-gray-700 rounded-2xl overflow-hidden bg-[#191919] text-white">
          <NuxtImg src="/about/gold-mining.webp" :alt="t('مجاري حلزونية وجهاز جيج ومركّز طارد مركزي وغربال أسطواني لغسيل الذهب وتركيزه', 'Spiral chutes, a jig, a centrifugal concentrator and a trommel for gold washing and concentration')" class="lg:col-span-5 w-full h-full min-h-[260px] object-cover" width="1200" height="967" format="webp" loading="lazy" />
          <div class="lg:col-span-7 p-6 md:p-10">
            <h4 class="font-display text-2xl font-bold mb-3">{{ t('تعدين الذهب في الشرق الأوسط وأفريقيا: السلسلة كاملة من مورّد واحد', 'Gold mining in the Middle East and Africa: the whole chain from one supplier') }}</h4>
            <p class="text-gray-300 leading-relaxed mb-6">
              {{ t('موقع تعدين الذهب يحتاج عادةً عدة مورّدين: للحفر، وللتكسير، وللغسيل، وللمعالجة، وللصهر، وللمختبر. نحن نجمعها في مورّد واحد، بصفتنا موزّعين معتمدين للعديد من المصانع والشركات العالمية في المنطقة، من التنقيب حتى الصبّ، مع قطع الغيار والمستهلكات التي تُبقي الموقع يعمل.',
                   'A gold-mining site usually needs several suppliers: for drilling, crushing, washing, processing, smelting and the lab. We bring them together in one supplier, as authorised distributors for many international manufacturers and companies in the region, from exploration to pouring, with the spare parts and consumables that keep the site running.') }}
            </p>
            <dl class="grid grid-cols-3 gap-3 mb-6">
              <div v-for="g in goldStats" :key="g.ar" class="bg-white/[0.06] rounded-xl px-3 py-3 text-center">
                <dt class="sr-only">{{ t(g.lar, g.len) }}</dt>
                <dd><span class="block font-display text-2xl md:text-3xl font-extrabold text-primary">{{ g.n }}</span><span class="block text-xs text-gray-300 mt-1">{{ t(g.ar, g.en) }}</span></dd>
              </div>
            </dl>
            <ul class="grid sm:grid-cols-2 gap-x-6 gap-y-2 text-sm text-gray-200 mb-8">
              <li v-for="m in miningAreas" :key="m.ar" class="flex gap-2"><span class="text-primary" aria-hidden="true">•</span>{{ t(m.ar, m.en) }}</li>
            </ul>
            <NuxtLink :to="localePath('/contact')" class="inline-block bg-primary text-[#191919] font-bold px-6 py-3 rounded-lg hover:bg-[#f2b02a] transition">
              {{ t('اطلب عرض سعر لمشروعك', 'Request a quote for your project') }}
            </NuxtLink>
          </div>
        </div>
      </div>
    </section>

    <!-- SAB TECH partnership -->
    <section class="py-16 md:py-20 bg-surface dark:bg-[#0f1216]">
      <div class="container mx-auto px-4 md:px-8 grid lg:grid-cols-12 gap-10 items-center">
        <div class="lg:col-span-8">
          <p class="text-primary font-bold mb-2">{{ t('شريكنا الاستراتيجي والجهة المصنِّعة', 'Our strategic partner and manufacturer') }}</p>
          <h2 class="font-display text-3xl md:text-4xl font-bold mb-5">{{ t('ساب تك', 'SAB TECH') }}</h2>
          <p class="text-lg text-slate dark:text-gray-300 leading-relaxed mb-6">
            {{ t('بيستوليكس هي الوكيل الحصري في قطر لشركة أساس السعودية لأعمال التقنية المحدودة (ساب تك). لساب تك خبرة تتجاوز 25 عاماً في التصنيع والحلول الهندسية، وهي حاصلة على شهادة إدارة الجودة ISO&nbsp;9001:2015. وتحمل علامةَ CE منتجاتُها المشمولة بوثائقها الفنية.',
                 'Bestolex is the exclusive agent in Qatar for Saudi Basis for Technical Works Ltd. (SAB TECH). SAB TECH brings more than 25 years of manufacturing and engineering experience and holds ISO 9001:2015 quality management certification. Products covered by its technical documentation carry CE marking.') }}
          </p>
          <ul class="flex flex-wrap gap-3 text-sm font-bold">
            <li class="bg-white dark:bg-gray-800 border border-line dark:border-gray-700 rounded-lg px-4 py-2">{{ t('ساب تك: أكثر من 25 عاماً', 'SAB TECH: 25+ years') }}</li>
            <li class="bg-white dark:bg-gray-800 border border-line dark:border-gray-700 rounded-lg px-4 py-2"><bdi>{{ t('ساب تك: ISO 9001:2015', 'SAB TECH: ISO 9001:2015') }}</bdi></li>
            <li class="bg-white dark:bg-gray-800 border border-line dark:border-gray-700 rounded-lg px-4 py-2">{{ t('علامة CE على منتجات ساب تك المشمولة', 'CE marking on covered SAB TECH products') }}</li>
          </ul>
        </div>
        <div class="lg:col-span-4">
          <div class="bg-white rounded-2xl border border-line p-8 text-center">
            <NuxtImg src="/partners/sabtech-logo.png" :alt="t('شعار ساب تك', 'SAB TECH logo')" class="h-16 mx-auto object-contain mb-4" format="webp" loading="lazy" />
            <p class="text-ink font-bold">{{ t('الوكيل الحصري في قطر: بيستوليكس', 'Exclusive agent in Qatar: Bestolex') }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- How we work -->
    <section class="py-16 md:py-24">
      <div class="container mx-auto px-4 md:px-8">
        <h2 class="font-display text-3xl md:text-4xl font-bold mb-3">{{ t('كيف نعمل', 'How we work') }}</h2>
        <p class="text-slate dark:text-gray-400 text-lg mb-10 max-w-[70ch]">{{ t('ثماني مراحل من دراسة الاحتياج إلى خدمة ما بعد البيع، وجهة واحدة تتابع المشروع في كلها.', 'Eight stages from the requirements study to after-sales service, with one company following the project throughout.') }}</p>
        <ol class="grid sm:grid-cols-2 lg:grid-cols-4 gap-5">
          <li v-for="(s, i) in stages" :key="i" class="border border-line dark:border-gray-700 rounded-2xl p-6 bg-white dark:bg-gray-800">
            <div class="flex items-center gap-3 mb-3">
              <span class="w-9 h-9 shrink-0 rounded-full bg-[#191919] text-primary font-display font-bold flex items-center justify-center">{{ i + 1 }}</span>
              <h3 class="font-bold leading-snug">{{ t(s.ar, s.en) }}</h3>
            </div>
            <p class="text-sm text-slate dark:text-gray-400 leading-relaxed">{{ t(s.dar, s.den) }}</p>
          </li>
        </ol>
        <p class="mt-6 text-sm text-slate dark:text-gray-400">{{ t('الخدمات الهيدروليكية متاحة عند الطلب عبر شريك فني.', 'Hydraulic services are available on request through a technical partner.') }}</p>
        <div class="mt-10 flex flex-col md:flex-row md:items-center justify-between gap-5 bg-[#191919] text-white rounded-2xl p-6 md:p-8">
          <p class="font-display text-xl font-bold">{{ t('تحتاج حلاً لمنشأتك في قطر؟ اطلب عرض سعر أو معاينة لموقعك.', 'Need a solution for your facility in Qatar? Request a quote or a site survey.') }}</p>
          <div class="flex flex-wrap gap-3">
            <NuxtLink :to="localePath('/contact')" class="bg-primary text-[#191919] font-bold px-6 py-3 rounded-lg hover:bg-[#f2b02a] transition w-full sm:w-auto text-center">{{ t('اطلب عرض سعر', 'Request a quote') }}</NuxtLink>
            <NuxtLink :to="localePath('/services')" class="border border-gray-500 font-bold px-6 py-3 rounded-lg hover:border-primary hover:text-primary transition w-full sm:w-auto text-center">{{ t('تفاصيل خدماتنا', 'Our services in detail') }}</NuxtLink>
          </div>
        </div>
      </div>
    </section>

    <!-- Sectors -->
    <section class="py-16 md:py-20 bg-surface dark:bg-[#0f1216]">
      <div class="container mx-auto px-4 md:px-8">
        <h2 class="font-display text-3xl md:text-4xl font-bold mb-8">{{ t('القطاعات التي نخدمها', 'Sectors we serve') }}</h2>
        <ul class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
          <li v-for="s in sectors" :key="s.ar" class="bg-white dark:bg-gray-800 border border-line dark:border-gray-700 rounded-xl p-5 font-bold leading-snug">
            {{ t(s.ar, s.en) }}
          </li>
        </ul>
      </div>
    </section>

    <!-- Values, why us -->
    <section class="py-16 md:py-24">
      <div class="container mx-auto px-4 md:px-8 grid lg:grid-cols-2 gap-14">
        <div>
          <h2 class="font-display text-3xl font-bold mb-8">{{ t('قيمنا', 'Our values') }}</h2>
          <dl class="space-y-5">
            <div v-for="v in values" :key="v.ar" class="border-s-4 border-primary ps-5">
              <dt class="font-display text-lg font-bold">{{ t(v.ar, v.en) }}</dt>
              <dd class="text-slate dark:text-gray-400 leading-relaxed mt-1">{{ t(v.dar, v.den) }}</dd>
            </div>
          </dl>
        </div>
        <div>
          <h2 class="font-display text-3xl font-bold mb-8">{{ t('لماذا بيستوليكس', 'Why Bestolex') }}</h2>
          <ol class="space-y-5">
            <li v-for="(w, i) in whyUs" :key="w.ar" class="flex gap-4">
              <span class="w-9 h-9 shrink-0 rounded-lg bg-primary/15 text-primary font-display font-bold flex items-center justify-center">{{ i + 1 }}</span>
              <div>
                <h3 class="font-display text-lg font-bold">{{ t(w.ar, w.en) }}</h3>
                <p class="text-slate dark:text-gray-400 leading-relaxed mt-1">{{ t(w.dar, w.den) }}</p>
              </div>
            </li>
          </ol>
        </div>
      </div>
    </section>

    <!-- Principles and goals -->
    <section class="py-16 md:py-20 bg-surface dark:bg-[#0f1216]">
      <div class="container mx-auto px-4 md:px-8 grid lg:grid-cols-2 gap-6">
        <div class="bg-white dark:bg-gray-800 border border-line dark:border-gray-700 rounded-2xl p-8">
          <h2 class="font-display text-2xl font-bold mb-5">{{ t('مبادئ العمل', 'Working principles') }}</h2>
          <ul class="space-y-3">
            <li v-for="p in principles" :key="p.ar" class="flex gap-3 leading-relaxed"><span class="text-primary font-bold" aria-hidden="true">✓</span>{{ t(p.ar, p.en) }}</li>
          </ul>
        </div>
        <div class="bg-white dark:bg-gray-800 border border-line dark:border-gray-700 rounded-2xl p-8">
          <h2 class="font-display text-2xl font-bold mb-5">{{ t('أهدافنا', 'Our goals') }}</h2>
          <ul class="space-y-3">
            <li v-for="g in goals" :key="g.ar" class="flex gap-3 leading-relaxed"><span class="text-primary font-bold" aria-hidden="true">✓</span>{{ t(g.ar, g.en) }}</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="py-16 md:py-20 bg-[#191919] text-white">
      <div class="container mx-auto px-4 md:px-8 grid lg:grid-cols-12 gap-8 items-center">
        <div class="lg:col-span-7">
          <h2 class="font-display text-3xl md:text-4xl font-bold mb-4">{{ t('اطلب عرض سعر أو معاينة لموقعك', 'Request a quote or a site survey') }}</h2>
          <p class="text-gray-300 text-lg leading-relaxed">{{ t('أرسل لنا نوع المعدة والكمية ومقاسات الموقع أو المخططات والموعد المطلوب، ونعود إليك بعرض فني وتجاري. نردّ خلال ساعات العمل: 7:00–18:00، الأحد إلى الخميس والسبت.', 'Send us the equipment type, quantity, site dimensions or drawings and the date you need it, and we come back with a technical and commercial offer. We reply during working hours: 7:00–18:00, Sunday to Thursday and Saturday.') }}</p>
        </div>
        <div class="lg:col-span-5 flex flex-wrap gap-3 lg:justify-end">
          <NuxtLink :to="localePath('/contact')" class="bg-primary text-[#191919] font-bold px-7 py-3.5 rounded-lg hover:bg-[#f2b02a] transition">{{ t('اطلب عرض سعر', 'Request a quote') }}</NuxtLink>
          <a :href="waLink" target="_blank" rel="noopener" class="border border-gray-500 font-bold px-7 py-3.5 rounded-lg hover:border-primary hover:text-primary transition">
            {{ t('واتساب', 'WhatsApp') }} <span dir="ltr" class="font-normal">+974 5150 5014</span>
          </a>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
import mockProducts from '@/data/products.json'
import { whatsappLink } from '~/utils/leads'
import { SOURCING_SECTORS } from '~/utils/sourcing'

const { locale } = useI18n()
const localePath = useLocalePath()
const isAr = computed(() => locale.value === 'ar')
const t = (ar, en) => (isAr.value ? ar : en)

const waLink = computed(() => whatsappLink(t('مرحباً بيستوليكس، ', 'Hello Bestolex, ')))
const catImage = id => (mockProducts.find(c => c.id === id) || {}).image

const heroFacts = [
  { lar: 'الوكالة', len: 'Agency', ar: 'الوكيل الحصري لساب تك في قطر', en: 'Exclusive SAB TECH agent in Qatar' },
  { lar: 'التوزيع', len: 'Distribution', ar: 'موزّعون معتمدون لمصانع وشركات عالمية', en: 'Authorised distributor for international manufacturers' },
  { lar: 'تعدين الذهب', len: 'Gold mining', ar: 'السلسلة كاملة من مورّد واحد', en: 'The whole chain from one supplier' },
  { lar: 'الأسواق', len: 'Markets', ar: 'قطر، والشرق الأوسط وأفريقيا', en: 'Qatar, the Middle East and Africa' }
]

const whoWeAre = [
  { lar: 'في قطر: وكالة حصرية', len: 'In Qatar: an exclusive agency', ar: 'بيستوليكس لتجارة الآلات والمعدات الثقيلة (ذ.م.م) شركة قطرية تخدم المنشآت الصناعية واللوجستية والتجارية والحكومية، والوكيل الحصري في قطر لشركة ساب تك، شريكنا الاستراتيجي والجهة المصنِّعة، في خطوطها الأربعة: أنظمة التحميل والمستودعات، والنفايات وإعادة التدوير، والحماية المحيطية، والأبواب الصناعية.', en: 'Bestolex Trading of Heavy Equipment and Machinery W.L.L. is a Qatari company serving industrial, logistics, commercial and government facilities, and the exclusive agent in Qatar for SAB TECH, our strategic partner and manufacturer, across its four lines: loading and warehouse systems, waste and recycling, perimeter protection and industrial doors.' },
  { lar: 'وما بعد الوكالة', len: 'Beyond the agency', ar: 'نقدّم حلول الطاقة: الطاقة الشمسية، ومحركات الديزل والمولدات، والحلول الهجينة، ونورّد المعدات الثقيلة عند الطلب. وما لا يدخل في أقسامنا نورّده حسب الطلب لأي نشاط، من المقاولات والمصانع والورش إلى المستشفيات والمطاعم والمزارع: تصف لنا ما تحتاجه، فندرس الخيارات مع الجهات المصنّعة ونرشّح الأنسب، ثم نتولّى الشراء والشحن والتركيب والتدريب والصيانة.', en: 'We provide energy solutions: solar energy, diesel engines and generators, and hybrid systems, and supply heavy equipment on request. Anything outside our sections we source on request for any activity, from contracting, factories and workshops to hospitals, restaurants and farms: you tell us what you need, we study the options with the manufacturers and recommend the best fit, then handle purchasing, shipping, installation, training and maintenance.' },
  { lar: 'خارج قطر', len: 'Outside Qatar', ar: 'نحن موزّعون معتمدون للعديد من المصانع والشركات العالمية، ولنا شراكات تجارية قوية مع شركات ومصانع عالمية كبرى في تعدين الذهب وحلول الطاقة: الطاقة الشمسية، ومحركات الديزل، والحلول الهجينة. ونورّد معدات تعدين الذهب والطاقة إلى مشاريع الشرق الأوسط وأفريقيا، وفي تعدين الذهب نغطي السلسلة كاملة من مورّد واحد، من التنقيب والحفر إلى الصهر والمختبر.', en: 'We are authorised distributors for many international manufacturers and companies, with strong commercial partnerships with major international companies and manufacturers in gold mining and energy: solar, diesel engines and hybrid systems. We supply gold-mining and energy equipment to projects in the Middle East and Africa, and in gold mining we cover the whole chain from one supplier, from exploration and drilling to smelting and the lab.' }
]

const agencyLines = [
  { link: '/products/category/docking-systems', img: catImage('docking-systems'), ar: 'أنظمة التحميل والمستودعات', en: 'Loading and warehouse systems', dar: 'أرصفة التحميل الثابتة والمتحركة، ومظلات الأرصفة، والرافعات المقصية، ومصاعد البضائع.', den: 'Fixed and mobile dock levelers, dock shelters, scissor lifts and goods lifts.' },
  { link: '/products/category/waste-management', img: catImage('waste-management'), ar: 'النفايات وإعادة التدوير', en: 'Waste and recycling', dar: 'مكابس الكرتون والبلاستيك والحديد والأقمشة، وضواغط النفايات، ومنها ضاغط يعمل بالطاقة الشمسية.', den: 'Cardboard, plastic, metal and textile balers, and waste compactors, including a solar-powered compactor.' },
  { link: '/products/category/perimeter-protection', img: catImage('perimeter-protection'), ar: 'الحماية المحيطية', en: 'Perimeter protection', dar: 'مصدات الطريق ومفجرات الإطارات والبولارد الهيدروليكي والبوابات الدوارة وأنظمة الكشف تحت المركبات.', den: 'Road blockers, tyre killers, hydraulic bollards, turnstiles and under-vehicle inspection systems.' },
  { link: '/products/category/industrial-doors', img: catImage('industrial-doors'), ar: 'الأبواب الصناعية', en: 'Industrial doors', dar: 'الأبواب المقطعية والسريعة والشتر الصناعي والأبواب الخاصة للمنشآت.', den: 'Sectional, high-speed, rolling shutter and special doors for facilities.' }
]

const otherLines = [
  { link: '/products/category/energy-solutions', img: catImage('energy-solutions'), ar: 'حلول الطاقة', en: 'Energy solutions', dar: 'الطاقة الشمسية بأنظمتها كاملة، ومحركات الديزل والمولدات، والحلول الهجينة، عبر شراكات تجارية مع شركات ومصانع عالمية كبرى، للمنشآت في قطر والمشاريع في الشرق الأوسط وأفريقيا.', den: 'Complete solar energy systems, diesel engines and generators, and hybrid systems, through commercial partnerships with major international companies and manufacturers, for facilities in Qatar and projects in the Middle East and Africa.', car: 'منتجات الطاقة', cen: 'Energy products' },
  { link: '/contact', img: '/about/heavy-equipment.webp', ar: 'المعدات الثقيلة عند الطلب', en: 'Heavy equipment on request', dar: 'الحفارات واللوادر وشاحنات القلاب والرافعات ومعدات الأنفاق والمناجم، نورّدها حسب المواصفة المطلوبة.', den: 'Excavators, loaders, dump trucks, cranes and tunnelling and mining equipment, supplied to the required specification.', car: 'اطلب معدة', cen: 'Request equipment' },
  { link: '/sourcing', icons: SOURCING_SECTORS.slice(0, 8).map(x => x.icon), ar: 'التوريد حسب الطلب', en: 'Sourcing on request', dar: 'أي آلة أو معدة ليست في أقسامنا، لأي نشاط: معدات البناء والسقالات، وقطع الغيار، والمضخات والضواغط، ومكائن الورش، ومعدات المطاعم والمستشفيات والمزارع، من مصانع حول العالم.', den: 'Any machine or equipment outside our sections, for any activity: construction equipment and scaffolding, spare parts, pumps and compressors, workshop machines, and equipment for restaurants, hospitals and farms, from factories worldwide.', car: 'التوريد حسب الطلب', cen: 'Sourcing on request' },
]

// From the approved families sheet (current catalogue editions, process chemicals excluded): 10 sections, 175 families, 1,955 model rows
const goldStats = [
  { n: '10', lar: 'أقسام', len: 'sections', ar: 'أقسام تغطي الموقع كاملاً', en: 'sections covering the whole site' },
  { n: '+170', lar: 'عائلات', len: 'families', ar: 'عائلة منتجات', en: 'product families' },
  { n: '~2,000', lar: 'موديلات', len: 'models', ar: 'موديل في كتالوجاتنا', en: 'models in our catalogues' }
]

const miningAreas = [
  { ar: 'التنقيب والحفر واستخراج الخام', en: 'Exploration, drilling and extraction' },
  { ar: 'مستهلكات الحفر', en: 'Drilling consumables' },
  { ar: 'التكسير والطحن والغربلة', en: 'Crushing, grinding and screening' },
  { ar: 'الغسيل وتركيز الذهب', en: 'Washing and gold concentration' },
  { ar: 'معالجة الخام والمصانع المتكاملة', en: 'Ore processing and complete plants' },
  { ar: 'المضخات ونقل اللب', en: 'Pumps and slurry handling' },
  { ar: 'الصهر والتنقية', en: 'Smelting and refining' },
  { ar: 'المختبر والتحليل', en: 'Laboratory and assay' },
  { ar: 'دعم الأسطول', en: 'Fleet support' },
  { ar: 'السلامة ومرافق الموقع', en: 'Safety and site facilities' }
]

const stages = [
  { ar: 'دراسة المتطلبات والمعاينة الميدانية', en: 'Requirements study and site survey', dar: 'نعاين الموقع ونفهم ظروف التشغيل والمتطلبات الفنية قبل أي عرض.', den: 'We survey the site and understand operating conditions and technical requirements before any offer.' },
  { ar: 'اختيار الحل والعرض الفني والتجاري', en: 'Solution selection and technical and commercial proposal', dar: 'نختار الحل المناسب للموقع ونقدّم عرضاً فنياً وتجارياً واضحاً.', den: 'We select the right solution for the site and submit a clear technical and commercial offer.' },
  { ar: 'التوريد والخدمات اللوجستية', en: 'Supply and logistics', dar: 'ننسّق التوريد والشحن والتخليص الجمركي حتى وصول المعدات إلى الموقع.', den: 'We coordinate supply, shipping and customs clearance until the equipment reaches the site.' },
  { ar: 'التركيب أو الإشراف الفني', en: 'Installation or technical supervision', dar: 'نركّب المعدات أو نشرف على تركيبها عبر فنيين مؤهلين وفق إجراءات السلامة.', den: 'We install the equipment, or supervise its installation, through qualified technicians following safety procedures.' },
  { ar: 'الاختبار والتشغيل والتسليم', en: 'Testing, commissioning and handover', dar: 'نختبر النظام ونشغّله ونسلّمه جاهزاً للعمل.', den: 'We test, commission and hand over a working system.' },
  { ar: 'تدريب المشغلين', en: 'Operator training', dar: 'ندرّب فريقك على التشغيل الصحيح والاستخدام الآمن وإجراءات الطوارئ.', den: 'We train your team on correct operation, safe use and emergency procedures.' },
  { ar: 'الصيانة الوقائية والتصحيحية', en: 'Preventive and corrective maintenance', dar: 'صيانة دورية واستجابة للأعطال للحفاظ على استمرارية التشغيل.', den: 'Scheduled maintenance and fault response to keep operations running.' },
  { ar: 'قطع الغيار وخدمة ما بعد البيع', en: 'Spare parts and after-sales service', dar: 'نوفّر قطع الغيار ونتابع المعدات بعد التسليم.', den: 'We supply spare parts and support the equipment after handover.' }
]

const sectors = [
  { ar: 'المستودعات واللوجستيات', en: 'Warehouses and logistics' },
  { ar: 'الجهات الحكومية والمنشآت الحساسة', en: 'Government and critical facilities' },
  { ar: 'الموانئ والمرافق', en: 'Ports and utilities' },
  { ar: 'المجمعات التجارية والفنادق', en: 'Malls and hotels' },
  { ar: 'المصانع', en: 'Factories' },
  { ar: 'المقاولون', en: 'Contractors' }
]

const values = [
  { ar: 'الجودة', en: 'Quality', dar: 'نختار ونورّد حلولاً ومعدات تلبي المتطلبات الفنية ومعايير الجودة ذات الصلة.', den: 'We select and supply solutions and equipment that meet the relevant technical and quality requirements.' },
  { ar: 'النزاهة', en: 'Integrity', dar: 'نتعامل بشفافية ووضوح في المعلومات الفنية والتجارية.', den: 'We are transparent and clear in technical and commercial information.' },
  { ar: 'السلامة', en: 'Safety', dar: 'نراعي متطلبات السلامة في الحلول والمعدات والخدمات التي نقدمها.', den: 'We build safety requirements into the solutions, equipment and services we provide.' },
  { ar: 'الالتزام', en: 'Commitment', dar: 'نحترم نطاق العمل والمتطلبات التعاقدية وجداول التوريد المتفق عليها.', den: 'We respect the agreed scope of work, contractual requirements and delivery schedules.' },
  { ar: 'الشراكة طويلة الأمد', en: 'Long-term partnership', dar: 'نبني علاقات مستدامة مع العملاء والمصنّعين والشركاء على أساس الثقة والقيمة المتبادلة.', den: 'We build lasting relationships with customers, manufacturers and partners based on trust and mutual value.' }
]

const whyUs = [
  { ar: 'حضور محلي في الدوحة', en: 'Local presence in Doha', dar: 'فهم مباشر لمتطلبات السوق القطري والمنشآت والمشاريع، ومعاينة في موقعك.', den: "A direct understanding of Qatar's market, facilities and projects, and site surveys at your premises." },
  { ar: 'وكالة حصرية وتوزيع معتمد', en: 'Exclusive agency and authorised distribution', dar: 'الوكيل الحصري لساب تك في قطر، وموزّعون معتمدون للعديد من المصانع والشركات العالمية.', den: 'The exclusive SAB TECH agent in Qatar, and authorised distributors for many international manufacturers and companies.' },
  { ar: 'جهة واحدة لاحتياجات متعددة', en: 'One company for many needs', dar: 'الخطوط الأربعة وحلول الطاقة والمعدات الثقيلة والتوريد حسب الطلب من جهة واحدة، بعرض واحد ومتابعة واحدة.', den: 'The four lines, energy solutions, heavy equipment and sourcing on request from one company, with one offer and one point of follow-up.' },
  { ar: 'ترشيح على قدر حاجتك', en: 'Recommendations sized to your need', dar: 'نرشّح ما يناسب تشغيلك وميزانيتك، ونقول لك صراحة متى يكفيك حل أصغر.', den: 'We recommend what suits your operation and budget, and tell you plainly when a smaller solution will do.' },
  { ar: 'دعم بعد التسليم', en: 'Support after handover', dar: 'تدريب وصيانة وقطع غيار وفق طبيعة المنتج ونطاق المشروع.', den: 'Training, maintenance and spare parts according to the product and project scope.' }
]

const principles = [
  { ar: 'وضع احتياج العميل في صميم كل قرار تجاري وهندسي.', en: "Putting the customer's need at the heart of every commercial and engineering decision." },
  { ar: 'الالتزام بالمواعيد التعاقدية وجداول التوريد.', en: 'Keeping to contractual dates and delivery schedules.' },
  { ar: 'المصداقية في المعلومات الفنية والتجارية.', en: 'Accuracy in technical and commercial information.' },
  { ar: 'التطوير المستمر لكفاءات الفريق الهندسي والفني.', en: 'Continuous development of our engineering and technical team.' },
  { ar: 'دعم التنمية الصناعية في قطر بما يتوافق مع رؤية قطر الوطنية 2030.', en: "Supporting Qatar's industrial development in line with Qatar National Vision 2030." }
]

const goals = [
  { ar: 'ترسيخ حضورنا وكيلاً وموزّعاً موثوقاً للمعدات الصناعية في قطر.', en: 'Establishing ourselves as a trusted agent and distributor of industrial equipment in Qatar.' },
  { ar: 'تقديم محفظة متكاملة من الحلول الصناعية واللوجستية والأمنية وحلول الطاقة.', en: 'Offering an integrated portfolio of industrial, logistics, security and energy solutions.' },
  { ar: 'توسيع شبكة المصانع التي نمثّلها ونورّد منها إقليمياً وعالمياً.', en: 'Expanding the network of factories we represent and source from, regionally and globally.' },
  { ar: 'خدمة مشاريع التعدين والطاقة في الشرق الأوسط وأفريقيا.', en: 'Serving mining and energy projects in the Middle East and Africa.' },
  { ar: 'تطوير الدعم الفني وخدمات ما بعد البيع باستمرار.', en: 'Continuously improving technical support and after-sales service.' }
]

const pageTitle = computed(() => t('من نحن | بيستوليكس، الوكيل الحصري لساب تك ومورّد المعدات في قطر', 'About Bestolex | Exclusive SAB TECH Agent in Doha, Qatar'))
const pageDesc = computed(() => t(
  'بيستوليكس شركة قطرية، الوكيل الحصري لساب تك وموزّع معتمد لمصانع عالمية: أنظمة التحميل والنفايات والحماية والأبواب، وحلول الطاقة، ومعدات تعدين الذهب.',
  'Qatari company, exclusive SAB TECH agent and authorised distributor for global manufacturers: loading, waste, security, doors, energy and gold mining.'
))

useSeoMeta({
  title: pageTitle,
  description: pageDesc,
  ogTitle: pageTitle,
  ogDescription: pageDesc,
  ogImage: BUSINESS.image
})

useHead(() => ({
  script: [
    {
      type: 'application/ld+json',
      key: 'ld-about',
      innerHTML: JSON.stringify({
        '@context': 'https://schema.org',
        '@graph': [
          {
            '@type': 'AboutPage',
            '@id': `${SITE_URL}${localePath('/about')}#webpage`,
            name: pageTitle.value,
            description: pageDesc.value,
            url: `${SITE_URL}${localePath('/about')}`,
            inLanguage: isAr.value ? 'ar' : 'en',
            isPartOf: { '@id': WEBSITE_ID },
            about: { '@id': ORG_ID },
            mainEntity: { '@id': ORG_ID },
            breadcrumb: { '@id': `${SITE_URL}${localePath('/about')}#breadcrumb` },
            mentions: { '@id': `${SITE_URL}/#sabtech` }
          },
          {
            '@type': 'Organization',
            '@id': `${SITE_URL}/#sabtech`,
            name: 'SAB TECH',
            alternateName: ['SABTECH', 'ساب تك', 'Saudi Basis for Technical Works Ltd.', 'شركة أساس السعودية لأعمال التقنية المحدودة'],
            description: t('الشريك الاستراتيجي والجهة المصنِّعة، وبيستوليكس وكيلها الحصري في قطر.', 'Strategic partner and manufacturer; Bestolex is its exclusive agent in Qatar.')
          },
          {
            '@type': 'BreadcrumbList',
            '@id': `${SITE_URL}${localePath('/about')}#breadcrumb`,
            itemListElement: [
              { '@type': 'ListItem', position: 1, name: t('الرئيسية', 'Home'), item: `${SITE_URL}${localePath('/')}` },
              { '@type': 'ListItem', position: 2, name: t('من نحن', 'About us'), item: `${SITE_URL}${localePath('/about')}` }
            ]
          }
        ]
      })
    }
  ]
}))
</script>
