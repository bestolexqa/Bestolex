<template>
  <div class="bg-white dark:bg-secondary text-ink dark:text-gray-100">
    <!-- Hero -->
    <section class="bg-[#191919] text-white relative overflow-hidden">
      <div class="absolute inset-0 opacity-[0.18] pointer-events-none" style="background-image: radial-gradient(circle at 80% 20%, #E99E05 0, transparent 45%), radial-gradient(circle at 10% 90%, #6F7070 0, transparent 40%)"></div>
      <div class="container mx-auto px-4 md:px-8 py-14 md:py-20 relative">
        <nav class="text-sm text-gray-400 mb-6" :aria-label="t('مسار التنقل', 'Breadcrumb')">
          <NuxtLink :to="localePath('/')" class="hover:text-primary">{{ t('الرئيسية', 'Home') }}</NuxtLink>
          <span class="mx-2">/</span>
          <span class="text-gray-200">{{ t('التوريد حسب الطلب', 'Sourcing on request') }}</span>
        </nav>
        <div class="grid lg:grid-cols-12 gap-10 items-center">
          <div class="lg:col-span-7">
            <p class="text-primary font-bold tracking-wide mb-3">{{ t('التوريد حسب الطلب', 'Sourcing on request') }}</p>
            <h1 class="font-display text-4xl md:text-5xl font-extrabold leading-[1.2] mb-6">
              {{ t('تحتاج آلة لا تجدها في السوق المحلي؟', "Need a machine you can't find locally?") }}
            </h1>
            <p class="text-lg text-gray-300 leading-relaxed max-w-[60ch] mb-8">
              {{ t('صف لنا العمل الذي تريد إنجازه. يقارن مهندسونا الخيارات المتاحة في المصانع العالمية التي نمثّلها وغيرها، ويرشّحون لك الأنسب لتشغيلك وميزانيتك، ثم نتولى الشراء والشحن والتركيب والتدريب والصيانة.',
                   'Describe the job you need done. Our engineers compare what the international factories we represent, and others, can offer, recommend the best fit for your operation and budget, then handle purchasing, shipping, installation, training and maintenance.') }}
            </p>
            <div class="flex flex-wrap gap-3">
              <a href="#request" class="inline-flex items-center gap-2 bg-primary text-[#191919] font-bold px-7 py-3.5 rounded-lg hover:bg-[#f2b02a] transition">
                {{ t('صف احتياجك', 'Describe your need') }}
              </a>
              <a :href="waLink" target="_blank" rel="noopener" class="inline-flex items-center gap-2 border border-gray-500 text-white font-bold px-7 py-3.5 rounded-lg hover:border-primary hover:text-primary transition" @click="trackWa">
                {{ t('واتساب', 'WhatsApp') }} <span dir="ltr" class="font-normal">+974 5150 5014</span>
              </a>
            </div>
          </div>
          <div class="lg:col-span-5">
            <NuxtImg src="/sourcing/heavy-equipment.webp" :alt="t('شاحنة تعدين ورافعة على شاحنة من كتالوج المعدات الثقيلة', 'Mining truck and truck-mounted crane from our heavy equipment catalogue')" class="w-full rounded-2xl" width="900" height="510" format="webp" loading="eager" />
          </div>
        </div>
        <ul class="grid sm:grid-cols-3 gap-4 mt-12">
          <li v-for="c in chips" :key="c.a" class="border border-white/15 rounded-xl px-5 py-4">
            <p class="font-display font-bold text-lg text-white">{{ t(c.a, c.ae) }}</p>
            <p class="text-sm text-gray-400 mt-1">{{ t(c.b, c.be) }}</p>
          </li>
        </ul>
      </div>
    </section>

    <!-- What we supply -->
    <section class="py-16 md:py-20">
      <div class="container mx-auto px-4 md:px-8">
        <h2 class="font-display text-3xl font-bold mb-3">{{ t('ما الذي نورّده', 'What we supply') }}</h2>
        <p class="text-slate dark:text-gray-400 mb-10 max-w-[70ch]">{{ t('خمسة أنواع من الطلبات. إن لم يكن طلبك منها، أرسله على أي حال ونخبرك إن كنا نستطيع.', "Five kinds of request. If yours isn't one of them, send it anyway and we'll tell you whether we can help.") }}</p>
        <div class="grid sm:grid-cols-2 lg:grid-cols-5 gap-5">
          <article v-for="(k, i) in kinds" :key="k.id" class="border border-line dark:border-gray-700 rounded-2xl p-6 bg-surface dark:bg-gray-800/40">
            <span class="font-display text-primary font-bold text-sm">0{{ i + 1 }}</span>
            <h3 class="font-display text-lg font-bold mt-2 mb-2">{{ t(k.ar, k.en) }}</h3>
            <p class="text-sm text-slate dark:text-gray-400 leading-relaxed">{{ t(k.dar, k.den) }}</p>
          </article>
        </div>
      </div>
    </section>

    <!-- How we work: the eight service stages -->
    <section class="py-16 md:py-20 bg-surface dark:bg-[#0f1216]">
      <div class="container mx-auto px-4 md:px-8">
        <h2 class="font-display text-3xl font-bold mb-3">{{ t('كيف نعمل', 'How we work') }}</h2>
        <p class="text-slate dark:text-gray-400 mb-10 max-w-[70ch]">{{ t('ثماني مراحل من دراسة الاحتياج إلى قطع الغيار وخدمة ما بعد البيع، وأنت تتعامل مع جهة واحدة في كلها.', 'Eight stages from the requirements study to spare parts and after-sales service, with one company to deal with throughout.') }}</p>
        <ol class="grid sm:grid-cols-2 lg:grid-cols-4 gap-5">
          <li v-for="(s, i) in stages" :key="i" class="bg-white dark:bg-gray-800 border border-line dark:border-gray-700 rounded-2xl p-6">
            <div class="flex items-center gap-3 mb-3">
              <span class="w-9 h-9 shrink-0 rounded-full bg-[#191919] text-primary font-display font-bold flex items-center justify-center">{{ i + 1 }}</span>
              <h3 class="font-bold leading-snug">{{ t(s.ar, s.en) }}</h3>
            </div>
            <p class="text-sm text-slate dark:text-gray-400 leading-relaxed">{{ t(s.dar, s.den) }}</p>
          </li>
        </ol>
      </div>
    </section>

    <!-- Why leave the search to us -->
    <section class="py-16 md:py-20">
      <div class="container mx-auto px-4 md:px-8 grid lg:grid-cols-12 gap-10">
        <div class="lg:col-span-7">
          <h2 class="font-display text-3xl font-bold mb-8">{{ t('لماذا تترك البحث لنا', 'Why leave the search to us') }}</h2>
          <div class="grid sm:grid-cols-2 gap-6">
            <div v-for="w in whyUs" :key="w.ar" class="border-t-2 border-primary pt-4">
              <h3 class="font-bold text-lg mb-2">{{ t(w.ar, w.en) }}</h3>
              <p class="text-sm text-slate dark:text-gray-400 leading-relaxed">{{ t(w.dar, w.den) }}</p>
            </div>
          </div>
        </div>
        <aside class="lg:col-span-5 bg-[#191919] text-white rounded-2xl p-8 self-start">
          <h2 class="font-display text-2xl font-bold mb-4">{{ t('من أين نورّد', 'Where we source from') }}</h2>
          <p class="text-gray-300 leading-relaxed">
            {{ t('ما تنتجه ساب تك نورّده بصفتنا وكيلها الحصري في قطر. وما عداه نبحث عنه لك في مصانع حول العالم، ونرشّح ما يطابق مواصفتك ويتوفر له دعم فني وقطع غيار على المدى الطويل.',
                 'What SAB TECH makes we supply as its exclusive agent in Qatar. Everything else we look for in factories around the world, recommending what matches your specification and has long-term technical support and spare parts.') }}
          </p>
        </aside>
      </div>
    </section>

    <!-- What we need from you -->
    <section class="py-16 md:py-20 bg-surface dark:bg-[#0f1216]">
      <div class="container mx-auto px-4 md:px-8 grid lg:grid-cols-2 gap-10">
        <div>
          <h2 class="font-display text-3xl font-bold mb-3">{{ t('ما نحتاجه منك لنبدأ', 'What we need from you to start') }}</h2>
          <p class="text-slate dark:text-gray-400 mb-4">{{ t('كلما كان الوصف أدق، كان العرض أسرع وأقرب لاحتياجك.', 'The more precise the description, the faster and closer the offer.') }}</p>
          <p class="text-slate dark:text-gray-400">{{ t('وإن لم تعرف المواصفة الفنية، لا بأس. يكفي أن تصف العمل الذي تريد إنجازه، ونحن نستخرج المواصفة معك.', "If you don't know the technical specification, that's fine. Describe the job and we'll work out the specification with you.") }}</p>
        </div>
        <ul class="space-y-3">
          <li v-for="n in needs" :key="n.ar" class="flex gap-3 bg-white dark:bg-gray-800 border border-line dark:border-gray-700 rounded-xl p-4">
            <span class="text-primary font-bold" aria-hidden="true">✓</span>
            <span class="leading-relaxed">{{ t(n.ar, n.en) }}</span>
          </li>
        </ul>
      </div>
    </section>

    <!-- Examples -->
    <section class="py-16 md:py-20">
      <div class="container mx-auto px-4 md:px-8">
        <h2 class="font-display text-3xl font-bold mb-2">{{ t('أمثلة من مجالات نورّد فيها', 'Examples of what we supply') }}</h2>
        <p class="text-slate dark:text-gray-400 mb-8">{{ t('الصور من كتالوجاتنا.', 'Photos from our catalogues.') }}</p>
        <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
          <figure v-for="e in examples" :key="e.img" class="rounded-2xl overflow-hidden bg-[#191919]">
            <NuxtImg :src="e.img" :alt="t(e.altAr, e.altEn)" class="w-full aspect-[900/510] object-cover" width="900" height="510" format="webp" loading="lazy" />
            <figcaption class="text-white font-bold px-5 py-4">{{ t(e.ar, e.en) }}</figcaption>
          </figure>
        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section class="py-16 md:py-20 bg-surface dark:bg-[#0f1216]">
      <div class="container mx-auto px-4 md:px-8 max-w-4xl">
        <h2 class="font-display text-3xl font-bold mb-8">{{ t('أسئلة شائعة', 'Frequently asked questions') }}</h2>
        <div class="divide-y divide-line dark:divide-gray-700 border-y border-line dark:border-gray-700">
          <details v-for="f in faq" :key="f.q.ar" class="group py-5">
            <summary class="flex justify-between items-center gap-4 cursor-pointer font-bold text-lg list-none">
              {{ t(f.q.ar, f.q.en) }}
              <span class="text-primary text-2xl leading-none group-open:rotate-45 transition" aria-hidden="true">+</span>
            </summary>
            <p class="mt-3 text-slate dark:text-gray-400 leading-relaxed">{{ t(f.a.ar, f.a.en) }}</p>
          </details>
        </div>
      </div>
    </section>

    <!-- Request form -->
    <section id="request" class="py-16 md:py-20 scroll-mt-24">
      <div class="container mx-auto px-4 md:px-8 grid lg:grid-cols-12 gap-10">
        <div class="lg:col-span-4">
          <h2 class="font-display text-3xl font-bold mb-4">{{ t('صف احتياجك', 'Describe your need') }}</h2>
          <p class="text-slate dark:text-gray-400 mb-8 leading-relaxed">{{ t('املأ النموذج، أو أرسل لنا رسالة واتساب بوصف مختصر. نرد عليك بأسئلة فنية قصيرة إن لزم، ثم بالعرض.', 'Fill in the form, or send us a short WhatsApp message. We reply with a few technical questions if needed, then with the offer.') }}</p>
          <dl class="space-y-4 text-sm">
            <div><dt class="text-slate dark:text-gray-400">{{ t('واتساب', 'WhatsApp') }}</dt><dd><a :href="waLink" target="_blank" rel="noopener" class="font-bold hover:text-primary" dir="ltr" @click="trackWa">+974 5150 5014</a></dd></div>
            <div><dt class="text-slate dark:text-gray-400">{{ t('هاتف', 'Phone') }}</dt><dd><a href="tel:+97450708833" class="font-bold hover:text-primary" dir="ltr">+974 5070 8833</a></dd></div>
            <div><dt class="text-slate dark:text-gray-400">{{ t('البريد', 'Email') }}</dt><dd><a href="mailto:info@bestolex.com" class="font-bold hover:text-primary">info@bestolex.com</a></dd></div>
            <div><dt class="text-slate dark:text-gray-400">{{ t('ساعات العمل', 'Working hours') }}</dt><dd class="font-bold"><span dir="ltr">7:00–18:00</span>{{ t('، الأحد إلى الخميس والسبت', ', Sunday to Thursday and Saturday') }}</dd></div>
          </dl>
        </div>
        <form class="lg:col-span-8 bg-surface dark:bg-gray-800/50 border border-line dark:border-gray-700 rounded-2xl p-6 md:p-8 grid sm:grid-cols-2 gap-5" @submit.prevent="submit">
          <label class="block">
            <span class="text-sm font-bold">{{ t('الاسم', 'Name') }} <span class="text-slate font-normal">{{ t('(مطلوب)', '(required)') }}</span></span>
            <input v-model="form.name" required autocomplete="name" class="mt-1 w-full rounded-lg border border-line dark:border-gray-600 bg-white dark:bg-gray-900 px-4 py-3" />
          </label>
          <label class="block">
            <span class="text-sm font-bold">{{ t('الشركة', 'Company') }}</span>
            <input v-model="form.company" autocomplete="organization" class="mt-1 w-full rounded-lg border border-line dark:border-gray-600 bg-white dark:bg-gray-900 px-4 py-3" />
          </label>
          <label class="block">
            <span class="text-sm font-bold">{{ t('الهاتف أو واتساب', 'Phone or WhatsApp') }} <span class="text-slate font-normal">{{ t('(مطلوب)', '(required)') }}</span></span>
            <input v-model="form.phone" required type="tel" dir="ltr" autocomplete="tel" class="mt-1 w-full rounded-lg border border-line dark:border-gray-600 bg-white dark:bg-gray-900 px-4 py-3 text-start" />
          </label>
          <label class="block">
            <span class="text-sm font-bold">{{ t('البريد الإلكتروني', 'Email') }}</span>
            <input v-model="form.email" type="email" dir="ltr" autocomplete="email" class="mt-1 w-full rounded-lg border border-line dark:border-gray-600 bg-white dark:bg-gray-900 px-4 py-3 text-start" />
          </label>
          <label class="block">
            <span class="text-sm font-bold">{{ t('نوع الطلب', 'Request type') }}</span>
            <select v-model="form.kind" class="mt-1 w-full rounded-lg border border-line dark:border-gray-600 bg-white dark:bg-gray-900 px-4 py-3">
              <option v-for="k in kindOptions" :key="k.id" :value="k.id">{{ t(k.ar, k.en) }}</option>
            </select>
          </label>
          <label class="block">
            <span class="text-sm font-bold">{{ t('الموعد المطلوب للتشغيل', 'Needed in operation by') }}</span>
            <input v-model="form.neededBy" :placeholder="t('مثال: مارس 2027', 'e.g. March 2027')" class="mt-1 w-full rounded-lg border border-line dark:border-gray-600 bg-white dark:bg-gray-900 px-4 py-3" />
          </label>
          <label class="block sm:col-span-2">
            <span class="text-sm font-bold">{{ t('صف الاحتياج', 'Describe the need') }} <span class="text-slate font-normal">{{ t('(مطلوب)', '(required)') }}</span></span>
            <textarea v-model="form.message" required rows="6" :placeholder="t('ماذا ستنتج أو تنقل أو تعالج، وبأي كمية، وأين يُركَّب.', 'What you will produce, move or process, at what rate, and where it will be installed.')" class="mt-1 w-full rounded-lg border border-line dark:border-gray-600 bg-white dark:bg-gray-900 px-4 py-3"></textarea>
          </label>
          <p class="sm:col-span-2 text-sm text-slate dark:text-gray-400">
            {{ t('عندك كراسة شروط، أو مواصفة استشاري، أو صورة الآلة الحالية ولوحة بياناتها؟ أرسلها على واتساب أو إلى info@bestolex.com بعد إرسال الطلب.', 'Have tender documents, a consultant specification, or a photo of the current machine and its nameplate? Send them on WhatsApp or to info@bestolex.com after submitting.') }}
          </p>
          <div class="sm:col-span-2 flex flex-wrap items-center gap-4">
            <button type="submit" :disabled="loading" class="bg-[#191919] text-white font-bold px-8 py-3.5 rounded-lg hover:bg-black disabled:opacity-60 transition">
              {{ loading ? t('جارٍ الإرسال…', 'Sending…') : t('أرسل الطلب', 'Send request') }}
            </button>
            <span class="text-xs text-slate dark:text-gray-400">{{ t('بياناتك تُستخدم للرد على طلبك فقط.', 'Your details are used only to answer your request.') }}</span>
          </div>
          <p v-if="status" role="status" class="sm:col-span-2 font-bold" :class="statusOk ? 'text-green-700 dark:text-green-400' : 'text-red-700 dark:text-red-400'">{{ status }}</p>
        </form>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useI18n } from 'vue-i18n'
import { whatsappLink } from '~/utils/leads'
import { trackLead } from '~/utils/track'

const { locale } = useI18n()
const localePath = useLocalePath()
const isAr = computed(() => locale.value === 'ar')
const t = (ar, en) => (isAr.value ? ar : en)

const waLink = computed(() => whatsappLink(t('مرحباً بيستوليكس، أحتاج توريد: ', 'Hello Bestolex, I need to source: ')))
const trackWa = () => trackLead({ formName: 'sourcing_whatsapp', requestType: 'sourcing' })

const chips = [
  { a: 'وكيل ساب تك الحصري في قطر', ae: 'Exclusive SAB TECH agent in Qatar', b: 'لخطوطها الأربعة', be: 'for its four product lines' },
  { a: 'من الدراسة إلى الصيانة', ae: 'From study to maintenance', b: 'ثماني مراحل، جهة واحدة', be: 'eight stages, one company' },
  { a: 'قطع غيار لآلاتك القائمة', ae: 'Spare parts for your existing machines', b: 'ولو لم تشترها منا', be: "even if you didn't buy them from us" }
]

const kinds = [
  { id: 'single', ar: 'آلية أو معدة واحدة', en: 'A single machine', dar: 'حفار، رافعة، ضاغط، مولد، مكبس… وحدة واحدة بمواصفة محددة، أو عدة وحدات من الموديل نفسه.', den: 'An excavator, crane, compressor, generator, press… one unit to a set specification, or several of the same model.' },
  { id: 'line', ar: 'خط إنتاج', en: 'A production line', dar: 'عدة آلات تعمل معاً: تكسير وغربلة، تعبئة وتغليف، فرز نفايات، معالجة مياه. نوفّرها متوافقة مع بعضها لا كقطع متفرقة.', den: 'Several machines working together: crushing and screening, filling and packing, waste sorting, water treatment. Supplied to work together, not as separate pieces.' },
  { id: 'plant', ar: 'مصنع كامل', en: 'A complete plant', dar: 'من دراسة الاحتياج إلى التشغيل: المخطط، والآلات، والتركيب، وتدريب المشغّلين.', den: 'From the requirements study to start-up: layout, machines, installation and operator training.' },
  { id: 'lab', ar: 'أجهزة ومختبرات', en: 'Instruments and laboratories', dar: 'أجهزة قياس وفحص وتحليل ومعايرة، ومستلزمات المختبر.', den: 'Measuring, testing, analysis and calibration instruments, and laboratory supplies.' },
  { id: 'parts', ar: 'قطع غيار ومستهلكات', en: 'Spare parts and consumables', dar: 'قطع تآكل وفلاتر وسيور ومحامل لآلات قائمة عندك، حتى لو لم تشترها منا.', den: "Wear parts, filters, belts and bearings for machines you already run, even if you didn't buy them from us." }
]
const kindOptions = [...kinds, { id: 'other', ar: 'غير ذلك', en: 'Something else' }]

const stages = [
  { ar: 'دراسة المتطلبات والمعاينة الميدانية', en: 'Requirements study and site survey', dar: 'نسمع منك، ونزور الموقع عند اللزوم، ونحدد المواصفة التي تحتاجها فعلاً.', den: 'We listen, visit the site when needed, and pin down the specification you actually need.' },
  { ar: 'اختيار الحل والعرض الفني والتجاري', en: 'Solution selection and technical and commercial proposal', dar: 'نقارن الخيارات المتاحة ونرسل جدولاً يبيّن الفروق بينها: القدرة والاستهلاك وقطع التآكل والسعر.', den: 'We compare the options and send a table of the differences: capacity, consumption, wear parts and price.' },
  { ar: 'التوريد والخدمات اللوجستية', en: 'Supply and logistics', dar: 'نشتري من المصنع، ونتابع التصنيع والفحص قبل الشحن، ونشحن إلى موقعك.', den: 'We buy from the factory, follow manufacturing and pre-shipment inspection, and ship to your site.' },
  { ar: 'التركيب أو الإشراف الفني', en: 'Installation or technical supervision', dar: 'نركّب الآلة في موقعك أو نشرف على تركيبها وتوصيلها.', den: 'We install the machine on your site or supervise its installation and connection.' },
  { ar: 'الاختبار والتشغيل والتسليم', en: 'Testing, commissioning and handover', dar: 'تشغيل تجريبي تحت الحمل، ثم التسليم جاهزاً للعمل.', den: 'A trial run under load, then handover ready to work.' },
  { ar: 'تدريب المشغلين', en: 'Operator training', dar: 'ندرّب مشغّليك على التشغيل والسلامة والصيانة اليومية.', den: 'We train your operators on operation, safety and daily maintenance.' },
  { ar: 'الصيانة الوقائية والتصحيحية', en: 'Preventive and corrective maintenance', dar: 'برنامج صيانة دوري واستجابة للأعطال، حتى لا تتوقف الآلة في وقت حرج.', den: 'Scheduled maintenance and fault response, so the machine does not stop at a critical time.' },
  { ar: 'قطع الغيار وخدمة ما بعد البيع', en: 'Spare parts and after-sales service', dar: 'نوفّر قطع الغيار ونتابع الآلة بعد التسليم.', den: 'We supply spare parts and support the machine after handover.' }
]

const whyUs = [
  { ar: 'مقارنة محايدة', en: 'A neutral comparison', dar: 'لا نرشّح آلة لأنها متوفرة عندنا، بل لأنها تناسب تشغيلك. ونقول لك صراحة متى تكفيك آلة أصغر مما طلبت.', den: "We don't recommend a machine because we stock it, but because it suits your operation. And we tell you plainly when a smaller machine than you asked for will do." },
  { ar: 'تحقق من المصنع', en: 'Factory checks', dar: 'نراجع المصنع ومواصفاته وشهاداته قبل الشراء، ونطلب تقرير فحص قبل الشحن.', den: 'We review the factory, its specifications and certificates before buying, and ask for a pre-shipment inspection report.' },
  { ar: 'مواصفة مكتوبة', en: 'A written specification', dar: 'تستلم المواصفة الفنية والشهادات مع العرض، فتعرف ما تشتريه بالضبط قبل أن تدفع.', den: 'You receive the technical specification and certificates with the offer, so you know exactly what you are buying before you pay.' },
  { ar: 'جهة واحدة بعد التسليم', en: 'One company after handover', dar: 'التركيب والتدريب والصيانة وقطع الغيار من جهة واحدة، فلا تطارد المصنع في بلد آخر.', den: 'Installation, training, maintenance and spare parts from one company, so you never chase a factory in another country.' }
]

const needs = [
  { ar: 'ماذا ستنتج أو تنقل أو تعالج، وبأي كمية في الساعة أو في اليوم.', en: 'What you will produce, move or process, and how much per hour or per day.' },
  { ar: 'المساحة المتاحة في الموقع، والكهرباء المتوفرة (الجهد والتردد)، أو هل تحتاج مولداً معها.', en: 'The space available on site and the power supply (voltage and frequency), or whether you need a generator with it.' },
  { ar: 'أقصى موعد تحتاج فيه تشغيل الآلة.', en: 'The latest date you need the machine running.' },
  { ar: 'أي مواصفة ملزمة من استشاري أو كراسة شروط مناقصة، أرسلها كما هي.', en: 'Any binding specification from a consultant or tender documents, sent as they are.' },
  { ar: 'صور أو فيديو للآلة الحالية، إن كنت تستبدلها أو تطلب لها قطع غيار.', en: 'Photos or video of the current machine, if you are replacing it or need parts for it.' }
]

const examples = [
  { img: '/sourcing/heavy-equipment.webp', ar: 'المعدات الثقيلة', en: 'Heavy equipment', altAr: 'شاحنة تعدين ورافعة على شاحنة', altEn: 'Mining truck and truck-mounted crane' },
  { img: '/sourcing/pumps.webp', ar: 'المضخات ونقل اللب', en: 'Pumps and slurry handling', altAr: 'مضخة لب عمودية ومضخة غاطسة ومضخة نزح على زلاجة', altEn: 'Vertical slurry pump, submersible pump and skid-mounted dewatering pump' },
  { img: '/sourcing/generators.webp', ar: 'المولدات والطاقة', en: 'Generators and power', altAr: 'مجموعة توليد صامتة على مقطورة', altEn: 'Silent generating set on a trailer' },
  { img: '/sourcing/laboratory.webp', ar: 'المختبرات والأجهزة', en: 'Laboratories and instruments', altAr: 'أجهزة تحضير العينات وموازين المختبر', altEn: 'Sample preparation equipment and laboratory balances' },
  { img: '/sourcing/fleet-support.webp', ar: 'دعم الأسطول', en: 'Fleet support', altAr: 'إطار لودر وبرج إنارة متنقل', altEn: 'Loader tyre and mobile light tower' },
  { img: '/sourcing/safety.webp', ar: 'السلامة ومرافق الموقع', en: 'Safety and site facilities', altAr: 'قفازات حماية ومعدات سلامة', altEn: 'Protective gloves and safety equipment' }
]

const faq = [
  { q: { ar: 'هل تورّدون قطعة واحدة، أم كميات فقط؟', en: 'Do you supply single units, or only quantities?' }, a: { ar: 'قطعة واحدة أو كمية. كثير من طلباتنا وحدة واحدة بمواصفة دقيقة.', en: 'Either. Many of our requests are a single unit to a precise specification.' } },
  { q: { ar: 'كم يستغرق التوريد؟', en: 'How long does supply take?' }, a: { ar: 'يعتمد على الآلة وجاهزيتها في المصنع. نحدد المدة في العرض الفني بعد تأكيدها من المصنع، ولا نعد بمدة قبل ذلك.', en: "It depends on the machine and its availability at the factory. We state the lead time in the technical offer once the factory confirms it, and don't promise one before that." } },
  { q: { ar: 'هل توفّرون قطع غيار لآلات لم نشترها منكم؟', en: "Do you supply parts for machines we didn't buy from you?" }, a: { ar: 'نعم. أرسل لنا لوحة بيانات الآلة ورقم الموديل وصورة القطعة، ونبحث عن المطابق لها أو البديل المتوافق.', en: 'Yes. Send us the nameplate, model number and a photo of the part, and we find the matching part or a compatible alternative.' } },
  { q: { ar: 'هل نستطيع تحديد المصنع الذي نريد الشراء منه؟', en: 'Can we name the factory we want to buy from?' }, a: { ar: 'نعم. إن كان لديك مصنع مفضل أو مواصفة ملزمة، نشتري منه ونتولى الباقي.', en: 'Yes. If you have a preferred factory or a binding specification, we buy from it and handle the rest.' } },
  { q: { ar: 'هل الخدمة داخل قطر فقط؟', en: 'Is the service only in Qatar?' }, a: { ar: 'السوق الأساسي قطر، بالتركيب والتدريب والصيانة. ونورّد معدات التعدين والطاقة إلى الشرق الأوسط وأفريقيا، فنحن وكلاء وموزّعون لكثير من المصانع العالمية في المنطقة.', en: 'Our main market is Qatar, with installation, training and maintenance. We also supply mining and energy equipment to the Middle East and Africa, as agents and distributors for many international factories in the region.' } }
]

// Form: goes to /api/contact like the other forms, stored and mailed as a request
const emptyForm = () => ({ name: '', company: '', phone: '', email: '', kind: 'single', neededBy: '', message: '' })
const form = ref(emptyForm())
const loading = ref(false)
const status = ref('')
const statusOk = ref(false)

const submit = async () => {
  loading.value = true
  status.value = ''
  const kind = kindOptions.find(k => k.id === form.value.kind) || kindOptions[0]
  const lines = [
    form.value.message,
    '',
    `نوع التوريد: ${kind.ar}`,
    form.value.neededBy && `الموعد المطلوب للتشغيل: ${form.value.neededBy}`
  ].filter(v => v !== false && v !== undefined)
  try {
    await $fetch('/api/contact', {
      method: 'POST',
      body: {
        name: form.value.name,
        company: form.value.company,
        phone: form.value.phone,
        email: form.value.email,
        requestType: 'sourcing',
        productName: `توريد حسب الطلب: ${kind.ar}`,
        productUrl: typeof window !== 'undefined' ? window.location.href : '',
        message: lines.join('\n'),
        isQuoteRequest: true
      }
    })
    trackLead({ formName: 'sourcing_request', requestType: 'sourcing' })
    statusOk.value = true
    status.value = t('وصل طلبك. سنتواصل معك قريباً، وإن كانت لديك مرفقات فأرسلها على واتساب +974 5150 5014.', 'Your request has arrived. We will contact you soon; if you have attachments, send them on WhatsApp +974 5150 5014.')
    form.value = emptyForm()
  } catch (e) {
    statusOk.value = false
    status.value = t('تعذّر الإرسال. حاول مرة أخرى أو راسلنا على واتساب +974 5150 5014.', 'Sending failed. Please try again or message us on WhatsApp +974 5150 5014.')
  } finally {
    loading.value = false
  }
}

const pageTitle = computed(() => t('التوريد حسب الطلب: آلات ومعدات من مصانع حول العالم | بيستوليكس', 'Equipment Sourcing on Request in Qatar | Bestolex'))
const pageDesc = computed(() => t(
  'صف الآلة أو خط الإنتاج أو قطع الغيار التي تحتاجها، ونقارن لك الخيارات في مصانع حول العالم، ثم نورّد ونركّب وندرّب ونصون في قطر. اطلب عرضاً.',
  'Describe the machine, production line or spare parts you need. We compare options from factories worldwide, then supply, install, train and maintain in Qatar.'
))

useSeoMeta({
  title: pageTitle,
  description: pageDesc,
  ogTitle: pageTitle,
  ogDescription: pageDesc,
  ogImage: `${SITE_URL}/sourcing/heavy-equipment.webp`
})

useHead(() => ({
  script: [
    {
      type: 'application/ld+json',
      key: 'ld-sourcing',
      innerHTML: JSON.stringify({
        '@context': 'https://schema.org',
        '@graph': [
          {
            '@type': 'Service',
            name: t('التوريد حسب الطلب', 'Sourcing on request'),
            description: pageDesc.value,
            url: `${SITE_URL}${localePath('/sourcing')}`,
            provider: { '@id': ORG_ID },
            areaServed: [{ '@type': 'Country', name: 'Qatar' }, { '@type': 'Place', name: 'Middle East' }, { '@type': 'Place', name: 'Africa' }]
          },
          {
            '@type': 'FAQPage',
            mainEntity: faq.map(f => ({ '@type': 'Question', name: t(f.q.ar, f.q.en), acceptedAnswer: { '@type': 'Answer', text: t(f.a.ar, f.a.en) } }))
          },
          {
            '@type': 'BreadcrumbList',
            itemListElement: [
              { '@type': 'ListItem', position: 1, name: t('الرئيسية', 'Home'), item: `${SITE_URL}${localePath('/')}` },
              { '@type': 'ListItem', position: 2, name: t('التوريد حسب الطلب', 'Sourcing on request'), item: `${SITE_URL}${localePath('/sourcing')}` }
            ]
          }
        ]
      })
    }
  ]
}))
</script>
