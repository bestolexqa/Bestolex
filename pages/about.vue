<template>
  <div class="bg-white dark:bg-secondary text-ink dark:text-gray-100">

    <!-- Hero -->
    <section class="relative bg-[#191919] text-white overflow-hidden">
      <NuxtImg
        src="https://cdn.bestolex.com/bestolex/about/showroom-v2.jpg"
        alt=""
        aria-hidden="true"
        class="absolute inset-0 w-full h-full object-cover opacity-50"
        format="webp"
        loading="eager"
      />
      <div class="absolute inset-0 bg-gradient-to-r rtl:bg-gradient-to-l from-[#191919] via-[#191919]/85 to-[#191919]/40"></div>
      <div class="container mx-auto px-4 md:px-8 py-14 md:py-20 relative">
        <nav class="text-sm text-gray-400 mb-8" :aria-label="t('مسار التنقل', 'Breadcrumb')">
          <NuxtLink :to="localePath('/')" class="hover:text-primary">{{ t('الرئيسية', 'Home') }}</NuxtLink>
          <span class="mx-2">/</span>
          <span class="text-gray-200">{{ t('من نحن', 'About us') }}</span>
        </nav>
        <div class="max-w-4xl">
          <p class="text-gray-300 font-bold mb-4">{{ t('بيستوليكس لتجارة الآلات والمعدات الثقيلة (ذ.م.م)', 'Bestolex Trading of Heavy Equipment and Machinery W.L.L.') }}</p>
          <h1 class="font-display text-3xl md:text-5xl font-extrabold leading-[1.3] md:leading-[1.3] mb-5">
            {{ t('الوكيل الحصري لساب تك في قطر: توريد وتركيب وصيانة معدات المنشآت الصناعية واللوجستية', 'The exclusive SAB TECH agent in Qatar: supply, installation and maintenance of equipment for industrial and logistics facilities') }}
          </h1>
          <p class="font-display text-xl md:text-2xl text-primary font-bold mb-6">
            {{ t('قوة تدفع أعمالكم... ثقة تدوم', 'Power that drives your business. Trust that lasts.') }}
          </p>
          <p class="text-lg md:text-xl text-gray-200 leading-relaxed max-w-[65ch] mb-8">
            {{ t('شركة قطرية مقرّها الدوحة، وموزّعون معتمدون للعديد من المصانع والشركات العالمية. نورّد ونركّب ونصون أنظمة التحميل والمستودعات، ومعدات النفايات وإعادة التدوير، والحماية المحيطية، والأبواب الصناعية. ونقدّم حلول الطاقة، ونوفّر حسب الطلب أي آلة أو خط إنتاج من مصانع حول العالم.',
                 'A Qatari company based in Doha and an authorised distributor for many international manufacturers and companies. We supply, install and maintain loading and warehouse systems, waste and recycling equipment, perimeter protection systems and industrial doors. We also provide energy solutions and source any machine or production line from manufacturers worldwide.') }}
          </p>
          <div class="flex flex-wrap gap-3">
            <NuxtLink :to="localePath('/contact')" class="w-full sm:w-auto text-center bg-primary text-[#191919] font-bold px-7 py-3.5 rounded-lg hover:bg-[#f2b02a] transition">
              {{ t('اطلب عرض سعر', 'Request a quote') }}
            </NuxtLink>
            <NuxtLink :to="localePath('/sourcing')" class="w-full sm:w-auto text-center border border-gray-400 text-white font-bold px-7 py-3.5 rounded-lg hover:border-primary hover:text-primary transition">
              {{ t('التوريد حسب الطلب', 'Sourcing on request') }}
            </NuxtLink>
          </div>
        </div>
        <dl class="grid grid-cols-2 lg:grid-cols-4 gap-4 mt-12">
          <div v-for="f in heroFacts" :key="f.ar" class="border-t-2 border-primary pt-4">
            <dt class="text-sm text-gray-400">{{ t(f.lar, f.len) }}</dt>
            <dd class="font-display text-base md:text-xl font-bold mt-1">{{ t(f.ar, f.en) }}</dd>
          </div>
        </dl>
      </div>
    </section>

    <!-- At a glance: who we are, vision, mission -->
    <section class="py-16 md:py-20">
      <div class="container mx-auto px-4 md:px-8">
        <h2 class="font-display text-3xl md:text-4xl font-bold mb-10">{{ t('بيستوليكس في سطور', 'Bestolex at a glance') }}</h2>
        <div class="grid lg:grid-cols-3 gap-8 lg:gap-10">
          <div v-for="w in whoWeAre" :key="w.lar" class="border-t-2 border-primary pt-5">
            <h3 class="font-bold mb-3">{{ t(w.lar, w.len) }}</h3>
            <p class="text-[17px] leading-relaxed text-slate dark:text-gray-300">{{ t(w.ar, w.en) }}</p>
          </div>
        </div>
        <div class="grid md:grid-cols-2 gap-5 mt-12">
          <div class="bg-surface dark:bg-gray-800/60 rounded-2xl p-6 md:p-8">
            <h3 class="font-bold text-slate dark:text-gray-400 mb-2">{{ t('رؤيتنا', 'Our vision') }}</h3>
            <p class="font-display text-lg md:text-xl font-bold leading-relaxed">
              {{ t('أن تكون بيستوليكس الشريك الموثوق الذي تعتمد عليه المنشآت الصناعية واللوجستية في قطر لرفع كفاءتها التشغيلية وتعزيز سلامتها واستدامتها.',
                   'For Bestolex to be the trusted partner that industrial and logistics facilities in Qatar rely on to raise their operating efficiency, safety and sustainability.') }}
            </p>
          </div>
          <div class="bg-surface dark:bg-gray-800/60 rounded-2xl p-6 md:p-8">
            <h3 class="font-bold text-slate dark:text-gray-400 mb-2">{{ t('رسالتنا', 'Our mission') }}</h3>
            <p class="font-display text-lg md:text-xl font-bold leading-relaxed">
              {{ t('تقديم حلول هندسية وتجارية تلائم المتطلبات الفعلية لكل مشروع، من الاستشارة الفنية واختيار المعدات إلى التوريد والتركيب والتشغيل والصيانة، بجودة وسلامة وخدمة يُعتمد عليها، دعماً للتنمية الصناعية في قطر وفق رؤية قطر الوطنية 2030.',
                   'To deliver engineering and commercial solutions that fit the real requirements of each project, from technical advice and equipment selection to supply, installation, commissioning and maintenance, with dependable quality, safety and service, supporting Qatar\'s industrial development in line with Qatar National Vision 2030.') }}
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Business areas -->
    <section class="py-16 md:py-20 bg-surface dark:bg-[#0f1216]">
      <div class="container mx-auto px-4 md:px-8">
        <div class="max-w-3xl mb-10">
          <h2 class="font-display text-3xl md:text-4xl font-bold mb-3">{{ t('مجالات عملنا', 'What we do') }}</h2>
          <p class="text-slate dark:text-gray-400 text-lg">{{ t('في قطر: أربعة خطوط بوكالة حصرية، وحلول الطاقة، والمعدات الثقيلة، والتوريد حسب الطلب. وخارجها: معدات تعدين الذهب والطاقة لمشاريع الشرق الأوسط وأفريقيا.', 'In Qatar: four exclusive lines, energy solutions, heavy equipment and sourcing on request. Beyond Qatar: gold-mining and energy equipment for projects in the Middle East and Africa.') }}</p>
        </div>

        <h3 class="font-display text-xl font-bold mb-5 flex items-center gap-3">
          <span class="w-2 h-6 bg-primary rounded-full" aria-hidden="true"></span>
          {{ t('الخطوط الأربعة عبر وكالة ساب تك الحصرية', 'The four lines, through the exclusive SAB TECH agency') }}
        </h3>
        <div class="grid grid-cols-2 lg:grid-cols-4 gap-3 md:gap-5 mb-12">
          <NuxtLink v-for="a in agencyLines" :key="a.link" :to="localePath(a.link)" class="group border border-line dark:border-gray-700 rounded-2xl overflow-hidden bg-white dark:bg-gray-800 hover:border-primary transition flex flex-col">
            <NuxtImg :src="a.img" alt="" class="w-full aspect-[4/3] object-cover" width="600" height="450" format="webp" loading="lazy" />
            <div class="p-4 md:p-5 flex-1 flex flex-col">
              <h4 class="font-display text-base md:text-lg font-bold mb-2 group-hover:underline">{{ t(a.ar, a.en) }}</h4>
              <p class="hidden sm:block text-[15px] text-slate dark:text-gray-400 leading-relaxed flex-1">{{ t(a.dar, a.den) }}</p>
              <span class="font-bold text-sm mt-3">{{ t('عرض المنتجات', 'View products') }} <span class="text-primary rtl:rotate-180 inline-block" aria-hidden="true">&rarr;</span></span>
            </div>
          </NuxtLink>
        </div>

        <h3 class="font-display text-xl font-bold mb-5 flex items-center gap-3">
          <span class="w-2 h-6 bg-primary rounded-full" aria-hidden="true"></span>
          {{ t('مجالات أخرى في قطر', 'Other business areas in Qatar') }}
        </h3>
        <div class="grid md:grid-cols-3 gap-5 mb-12">
          <NuxtLink v-for="a in otherLines" :key="a.ar" :to="localePath(a.link)" class="group border border-line dark:border-gray-700 rounded-2xl overflow-hidden bg-white dark:bg-gray-800 hover:border-primary transition flex flex-col">
            <div v-if="a.icons" class="w-full aspect-[16/9] bg-[#191919] grid grid-cols-4 place-items-center p-5 gap-3" aria-hidden="true">
              <span v-for="ic in a.icons" :key="ic" class="w-11 h-11 rounded-xl bg-primary/15 text-primary flex items-center justify-center"><SourcingIcon :name="ic" class="w-6 h-6" /></span>
            </div>
            <NuxtImg v-else :src="a.img" alt="" class="w-full aspect-[16/9] object-cover" width="800" height="450" format="webp" loading="lazy" />
            <div class="p-5 flex-1 flex flex-col">
              <h4 class="font-display text-lg font-bold mb-2 group-hover:underline">{{ t(a.ar, a.en) }}</h4>
              <p class="text-[15px] text-slate dark:text-gray-400 leading-relaxed flex-1">{{ t(a.dar, a.den) }}</p>
              <span class="font-bold text-sm mt-4">{{ t(a.car, a.cen) }} <span class="text-primary rtl:rotate-180 inline-block" aria-hidden="true">&rarr;</span></span>
            </div>
          </NuxtLink>
        </div>

        <h3 class="font-display text-xl font-bold mb-5 flex items-center gap-3">
          <span class="w-2 h-6 bg-primary rounded-full" aria-hidden="true"></span>
          {{ t('خارج قطر: الشرق الأوسط وأفريقيا', 'Beyond Qatar: the Middle East and Africa') }}
        </h3>
        <div class="grid md:grid-cols-12 border border-line dark:border-gray-700 rounded-2xl overflow-hidden bg-white dark:bg-gray-800">
          <NuxtImg src="/about/gold-mining.webp" :alt="t('مجاري حلزونية وجهاز جيج ومركّز طارد مركزي وغربال أسطواني لغسيل الذهب وتركيزه', 'Spiral chutes, a jig, a centrifugal concentrator and a trommel for gold washing and concentration')" class="md:col-span-4 w-full h-full min-h-[200px] max-h-[320px] object-cover" width="1200" height="967" format="webp" loading="lazy" />
          <div class="md:col-span-8 p-6 md:p-8">
            <h4 class="font-display text-xl md:text-2xl font-bold mb-3">{{ t('تعدين الذهب: السلسلة كاملة من مورّد واحد', 'Gold mining: the whole chain from one supplier') }}</h4>
            <p class="text-[15px] md:text-base text-slate dark:text-gray-300 leading-relaxed mb-5">
              {{ t('موقع تعدين الذهب يحتاج عادةً عدة مورّدين: للحفر، والتكسير، والغسيل، والمعالجة، والصهر، والمختبر. نحن نجمعها في مورّد واحد، من التنقيب حتى صبّ السبائك، مع قطع الغيار والمستهلكات، بصفتنا موزّعين معتمدين للعديد من المصانع والشركات العالمية.',
                   'A gold-mining site usually needs several suppliers: for drilling, crushing, washing, processing, smelting and the lab. We bring them together in one supplier, from exploration to the final gold pour, with spare parts and consumables, as authorised distributors for many international manufacturers and companies.') }}
            </p>
            <dl class="grid grid-cols-3 gap-3 mb-6 max-w-xl">
              <div v-for="g in goldStats" :key="g.ar" class="bg-[#191919] text-white rounded-xl px-3 py-3 text-center">
                <dt class="sr-only">{{ t(g.lar, g.len) }}</dt>
                <dd><span class="block font-display text-2xl font-extrabold text-primary" dir="ltr">{{ g.n }}</span><span class="block text-xs text-gray-300 mt-1">{{ t(g.ar, g.en) }}</span></dd>
              </div>
            </dl>
            <NuxtLink :to="localePath('/contact')" class="inline-block w-full sm:w-auto text-center bg-[#191919] text-white font-bold px-6 py-3 rounded-lg hover:bg-black transition">
              {{ t('اطلب عرض سعر لمشروعك', 'Request a quote for your project') }}
            </NuxtLink>
          </div>
        </div>

        <!-- Mid-page call to action -->
        <div class="mt-12 flex flex-col md:flex-row md:items-center justify-between gap-5 bg-[#191919] text-white rounded-2xl p-6 md:p-8">
          <p class="font-display text-xl font-bold">{{ t('تحتاج حلاً لمنشأتك في قطر؟ اطلب عرض سعر أو معاينة لموقعك.', 'Need a solution for your facility in Qatar? Request a quote or a site survey.') }}</p>
          <div class="flex flex-wrap gap-3">
            <NuxtLink :to="localePath('/contact')" class="bg-primary text-[#191919] font-bold px-6 py-3 rounded-lg hover:bg-[#f2b02a] transition w-full sm:w-auto text-center">{{ t('اطلب عرض سعر', 'Request a quote') }}</NuxtLink>
            <NuxtLink :to="localePath('/contact') + '?type=site-survey'" class="border border-gray-400 font-bold px-6 py-3 rounded-lg hover:border-primary hover:text-primary transition w-full sm:w-auto text-center">{{ t('اطلب معاينة ميدانية', 'Request a site survey') }}</NuxtLink>
          </div>
        </div>
      </div>
    </section>

    <!-- SAB TECH partnership -->
    <section class="py-16 md:py-20">
      <div class="container mx-auto px-4 md:px-8 grid lg:grid-cols-12 gap-10 items-center">
        <div class="lg:col-span-8">
          <h2 class="font-display text-3xl md:text-4xl font-bold mb-5">{{ t('ساب تك: شريكنا الاستراتيجي المصنِّع', 'SAB TECH: our strategic manufacturing partner') }}</h2>
          <p class="text-lg text-slate dark:text-gray-300 leading-relaxed mb-6">
            {{ t('بيستوليكس هي الوكيل الحصري في قطر لشركة أساس السعودية لأعمال التقنية المحدودة (ساب تك). لساب تك خبرة تتجاوز 25 عاماً في التصنيع والحلول الهندسية، وهي حاصلة على شهادة إدارة الجودة ISO 9001:2015. وتحمل علامةَ CE منتجاتُها المشمولة بوثائقها الفنية.',
                 'Bestolex is the exclusive agent in Qatar for Saudi Basis for Technical Works Ltd. (SAB TECH). SAB TECH brings more than 25 years of manufacturing and engineering experience and holds ISO 9001:2015 quality management certification. Products covered by its technical documentation carry CE marking.') }}
          </p>
          <ul class="flex flex-wrap gap-3 text-sm font-bold">
            <li class="bg-surface dark:bg-gray-800 border border-line dark:border-gray-700 rounded-lg px-4 py-2">{{ t('ساب تك: أكثر من 25 عاماً', 'SAB TECH: 25+ years') }}</li>
            <li class="bg-surface dark:bg-gray-800 border border-line dark:border-gray-700 rounded-lg px-4 py-2"><bdi>{{ t('ساب تك: ISO 9001:2015', 'SAB TECH: ISO 9001:2015') }}</bdi></li>
            <li class="bg-surface dark:bg-gray-800 border border-line dark:border-gray-700 rounded-lg px-4 py-2">{{ t('علامة CE على منتجات ساب تك المشمولة', 'CE marking on covered SAB TECH products') }}</li>
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

    <!-- Why Bestolex + values -->
    <section class="py-16 md:py-20 bg-surface dark:bg-[#0f1216]">
      <div class="container mx-auto px-4 md:px-8 grid lg:grid-cols-2 gap-12">
        <div>
          <h2 class="font-display text-3xl font-bold mb-8">{{ t('لماذا بيستوليكس؟', 'Why Bestolex?') }}</h2>
          <ol class="space-y-5">
            <li v-for="(w, i) in whyUs" :key="w.ar" class="flex gap-4">
              <span class="w-9 h-9 shrink-0 rounded-lg bg-[#191919] text-primary font-display font-bold flex items-center justify-center">{{ i + 1 }}</span>
              <div>
                <h3 class="font-display text-lg font-bold">{{ t(w.ar, w.en) }}</h3>
                <p class="text-slate dark:text-gray-400 leading-relaxed mt-1">{{ t(w.dar, w.den) }}</p>
              </div>
            </li>
          </ol>
        </div>
        <div>
          <h2 class="font-display text-3xl font-bold mb-8">{{ t('قيمنا', 'Our values') }}</h2>
          <dl class="space-y-5">
            <div v-for="v in values" :key="v.ar" class="border-s-4 border-primary ps-5">
              <dt class="font-display text-lg font-bold">{{ t(v.ar, v.en) }}</dt>
              <dd class="text-slate dark:text-gray-400 leading-relaxed mt-1">{{ t(v.dar, v.den) }}</dd>
            </div>
          </dl>
        </div>
      </div>
    </section>

    <!-- How we work + sectors -->
    <section class="py-16 md:py-20">
      <div class="container mx-auto px-4 md:px-8">
        <h2 class="font-display text-3xl md:text-4xl font-bold mb-3">{{ t('كيف نعمل', 'How we work') }}</h2>
        <p class="text-slate dark:text-gray-400 text-lg mb-8 max-w-[70ch]">{{ t('ثماني مراحل، من دراسة المتطلبات إلى خدمة ما بعد البيع، تتابعها جهة واحدة من البداية إلى النهاية.', 'Eight stages, from the requirements study to after-sales service, followed by one company from start to finish.') }}</p>
        <ol class="grid sm:grid-cols-2 lg:grid-cols-4 gap-3 md:gap-5">
          <li v-for="(s, i) in stages" :key="i" class="border border-line dark:border-gray-700 rounded-2xl p-4 md:p-6 bg-white dark:bg-gray-800">
            <div class="flex items-center gap-3 sm:mb-3">
              <span class="w-9 h-9 shrink-0 rounded-full bg-[#191919] text-primary font-display font-bold flex items-center justify-center">{{ i + 1 }}</span>
              <h3 class="font-bold leading-snug">{{ t(s.ar, s.en) }}</h3>
            </div>
            <p class="hidden sm:block text-[15px] text-slate dark:text-gray-400 leading-relaxed">{{ t(s.dar, s.den) }}</p>
          </li>
        </ol>
        <div class="mt-6 flex flex-wrap items-center gap-x-6 gap-y-2 text-sm">
          <NuxtLink :to="localePath('/services')" class="font-bold underline underline-offset-4 decoration-primary hover:text-primary">{{ t('تفاصيل خدماتنا', 'Our services in detail') }}</NuxtLink>
          <NuxtLink :to="localePath('/training')" class="font-bold underline underline-offset-4 decoration-primary hover:text-primary">{{ t('برامج تدريب المشغلين', 'Operator training programmes') }}</NuxtLink>
          <span class="text-slate dark:text-gray-400">{{ t('الخدمات الهيدروليكية متاحة عند الطلب عبر شريك فني.', 'Hydraulic services are available on request through a technical partner.') }}</span>
        </div>

        <h3 class="font-display text-xl font-bold mt-14 mb-5">{{ t('القطاعات التي نخدمها', 'Sectors we serve') }}</h3>
        <ul class="flex flex-wrap gap-2">
          <li v-for="s in sectors" :key="s.ar" class="bg-surface dark:bg-gray-800 border border-line dark:border-gray-700 rounded-full px-4 py-2 font-bold text-sm">{{ t(s.ar, s.en) }}</li>
        </ul>
      </div>
    </section>

    <!-- FAQ -->
    <section class="py-16 md:py-20 bg-surface dark:bg-[#0f1216]">
      <div class="container mx-auto px-4 md:px-8 max-w-4xl">
        <h2 class="font-display text-3xl font-bold mb-8">{{ t('أسئلة عن بيستوليكس', 'Questions about Bestolex') }}</h2>
        <div class="divide-y divide-line dark:divide-gray-700 border-y border-line dark:border-gray-700">
          <details v-for="(f, i) in faq" :key="f.q.ar" class="group py-5" :open="i === 0">
            <summary class="flex justify-between items-center gap-4 cursor-pointer list-none">
              <h3 class="font-bold text-lg">{{ t(f.q.ar, f.q.en) }}</h3>
              <span class="text-primary text-2xl leading-none group-open:rotate-45 transition" aria-hidden="true">+</span>
            </summary>
            <p class="mt-3 text-slate dark:text-gray-400 leading-relaxed">{{ t(f.a.ar, f.a.en) }}</p>
          </details>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="py-16 md:py-20 bg-[#191919] text-white">
      <div class="container mx-auto px-4 md:px-8 grid lg:grid-cols-12 gap-8 items-center">
        <div class="lg:col-span-7">
          <h2 class="font-display text-3xl md:text-4xl font-bold mb-4">{{ t('اطلب عرض سعر أو معاينة لموقعك', 'Request a quote or a site survey') }}</h2>
          <p class="text-gray-300 text-lg leading-relaxed">{{ t('أرسل لنا نوع المعدّة والكمية ومقاسات الموقع أو المخططات والموعد المطلوب، ونعود إليك بعرض فني وتجاري. نردّ خلال ساعات العمل: 7:00–18:00، الأحد إلى الخميس والسبت.', 'Send us the equipment type, quantity, site dimensions or drawings and the date you need it, and we come back with a technical and commercial proposal. We reply during working hours: 7:00–18:00, Sunday to Thursday and Saturday.') }}</p>
        </div>
        <div class="lg:col-span-5 flex flex-wrap gap-3 lg:justify-end">
          <NuxtLink :to="localePath('/contact')" class="w-full sm:w-auto text-center bg-primary text-[#191919] font-bold px-7 py-3.5 rounded-lg hover:bg-[#f2b02a] transition">{{ t('اطلب عرض سعر', 'Request a quote') }}</NuxtLink>
          <NuxtLink :to="localePath('/contact') + '?type=site-survey'" class="w-full sm:w-auto text-center border border-gray-400 font-bold px-7 py-3.5 rounded-lg hover:border-primary hover:text-primary transition">{{ t('اطلب معاينة ميدانية', 'Request a site survey') }}</NuxtLink>
          <a :href="waLink" target="_blank" rel="noopener" class="w-full sm:w-auto text-center border border-gray-400 font-bold px-7 py-3.5 rounded-lg hover:border-primary hover:text-primary transition">
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
  { lar: 'في قطر: وكالة حصرية', len: 'In Qatar: an exclusive agency', ar: 'بيستوليكس لتجارة الآلات والمعدات الثقيلة (ذ.م.م) شركة قطرية تخدم المنشآت الصناعية واللوجستية والتجارية والحكومية. ونحن الوكيل الحصري في قطر لشركة ساب تك، شريكنا الاستراتيجي المصنِّع، في خطوطها الأربعة: أنظمة التحميل والمستودعات، والنفايات وإعادة التدوير، والحماية المحيطية، والأبواب الصناعية.', en: 'Bestolex Trading of Heavy Equipment and Machinery W.L.L. is a Qatari company serving industrial, logistics, commercial and government facilities. We are the exclusive agent in Qatar for SAB TECH, our strategic manufacturing partner, across its four lines: loading and warehouse systems, waste and recycling, perimeter protection and industrial doors.' },
  { lar: 'وما بعد الوكالة', len: 'Beyond the agency', ar: 'تقدّم بيستوليكس حلول الطاقة: الطاقة الشمسية، ومحركات الديزل والمولدات، والحلول الهجينة، وتورّد المعدات الثقيلة عند الطلب. وما لا تشمله أقسامنا نوفّره لأي نشاط، من المقاولات والمصانع والورش إلى المستشفيات والمطاعم والمزارع. تصف لنا ما تحتاجه، فندرس الخيارات مع الجهات المصنِّعة ونرشّح الأنسب، ثم نتولّى الشراء والشحن والتركيب والتدريب والصيانة.', en: 'Bestolex provides energy solutions: solar energy, diesel engines and generators, and hybrid systems, and supplies heavy equipment on request. Anything outside our sections we source for any activity, from contracting, factories and workshops to hospitals, restaurants and farms. You tell us what you need, we study the options with the manufacturers and recommend the best fit, then handle purchasing, shipping, installation, training and maintenance.' },
  { lar: 'خارج قطر', len: 'Beyond Qatar', ar: 'بيستوليكس موزّع معتمد للعديد من المصانع والشركات العالمية، ولها شراكات تجارية قوية مع شركات ومصانع عالمية كبرى في تعدين الذهب وحلول الطاقة: الطاقة الشمسية، ومحركات الديزل، والحلول الهجينة. وتورّد معدات تعدين الذهب والطاقة إلى مشاريع الشرق الأوسط وأفريقيا، وتغطي سلسلة تعدين الذهب كاملة من مورّد واحد، من التنقيب والحفر إلى الصهر والمختبر.', en: 'Bestolex is an authorised distributor for many international manufacturers and companies, with strong commercial partnerships with major international companies and manufacturers in gold mining and energy: solar, diesel engines and hybrid systems. It supplies gold-mining and energy equipment to projects in the Middle East and Africa, covering the whole gold-mining chain from one supplier, from exploration and drilling to smelting and the lab.' }
]

const agencyLines = [
  { link: '/products/category/docking-systems', img: catImage('docking-systems'), ar: 'أنظمة التحميل والمستودعات', en: 'Loading and warehouse systems', dar: 'أرصفة التحميل الثابتة والمتحركة، ومظلات الأرصفة، والرافعات المقصية، ومصاعد البضائع.', den: 'Fixed and mobile dock levellers, dock shelters, scissor lifts and goods lifts.' },
  { link: '/products/category/waste-management', img: catImage('waste-management'), ar: 'النفايات وإعادة التدوير', en: 'Waste and recycling', dar: 'مكابس الكرتون والبلاستيك والمعادن والأقمشة، وضواغط النفايات، ومنها ضاغط يعمل بالطاقة الشمسية.', den: 'Cardboard, plastic, metal and textile balers, and waste compactors, including a solar-powered compactor.' },
  { link: '/products/category/perimeter-protection', img: catImage('perimeter-protection'), ar: 'الحماية المحيطية', en: 'Perimeter protection', dar: 'مصدات الطريق ومفجرات الإطارات والأعمدة الهيدروليكية (البولارد) والبوابات الدوارة وأنظمة الكشف تحت المركبات.', den: 'Road blockers, tyre killers, hydraulic bollards, turnstiles and under-vehicle inspection systems.' },
  { link: '/products/category/industrial-doors', img: catImage('industrial-doors'), ar: 'الأبواب الصناعية', en: 'Industrial doors', dar: 'الأبواب المقطعية والسريعة والشتر الصناعي والأبواب الخاصة للمنشآت.', den: 'Sectional, high-speed, rolling shutter and special doors for facilities.' }
]

const otherLines = [
  { link: '/products/category/energy-solutions', img: '/products/solar-mounting-cables-protection/bxs-0020-01-003.webp', ar: 'حلول الطاقة', en: 'Energy solutions', dar: 'الطاقة الشمسية بأنظمتها كاملة، ومحركات الديزل والمولدات، والحلول الهجينة، عبر شراكات تجارية مع شركات ومصانع عالمية كبرى، للمنشآت في قطر والمشاريع في الشرق الأوسط وأفريقيا.', den: 'Complete solar energy systems, diesel engines and generators, and hybrid systems, through commercial partnerships with major international companies and manufacturers, for facilities in Qatar and projects in the Middle East and Africa.', car: 'منتجات الطاقة', cen: 'Energy products' },
  { link: '/contact', img: '/about/heavy-equipment-card.webp', ar: 'المعدات الثقيلة عند الطلب', en: 'Heavy equipment on request', dar: 'الحفارات واللوادر وشاحنات القلاب والرافعات ومعدات الأنفاق والمناجم، نورّدها حسب المواصفة المطلوبة.', den: 'Excavators, loaders, dump trucks, cranes and tunnelling and mining equipment, supplied to the required specification.', car: 'اطلب معدّة', cen: 'Request equipment' },
  { link: '/sourcing', icons: SOURCING_SECTORS.slice(0, 8).map(x => x.icon), ar: 'التوريد حسب الطلب', en: 'Sourcing on request', dar: 'أي آلة أو معدّة ليست في أقسامنا، لأي نشاط: معدات البناء والسقالات، وقطع الغيار، والمضخات والضواغط، ومكائن الورش، ومعدات المطاعم والمستشفيات والمزارع، من مصانع حول العالم.', den: 'Any machine or equipment outside our sections, for any activity: construction equipment and scaffolding, spare parts, pumps and compressors, workshop machines, and equipment for restaurants, hospitals and farms, from manufacturers worldwide.', car: 'التوريد حسب الطلب', cen: 'Sourcing on request' }
]

// From the approved families sheet (current catalogue editions, process chemicals excluded): 10 sections, 175 families, 1,955 model rows
const goldStats = [
  { n: '10', lar: 'أقسام', len: 'sections', ar: 'أقسام تغطي الموقع كاملاً', en: 'sections covering the whole site' },
  { n: '+170', lar: 'عائلات', len: 'families', ar: 'عائلة منتجات', en: 'product families' },
  { n: '~2,000', lar: 'موديلات', len: 'models', ar: 'موديل في كتالوجاتنا', en: 'models in our catalogues' }
]

const stages = [
  { ar: 'دراسة المتطلبات والمعاينة الميدانية', en: 'Requirements study and site survey', dar: 'نعاين الموقع ونفهم ظروف التشغيل والمتطلبات الفنية قبل أي عرض.', den: 'We survey the site and understand operating conditions and technical requirements before any proposal.' },
  { ar: 'اختيار الحل والعرض الفني والتجاري', en: 'Solution selection, technical and commercial proposal', dar: 'نختار الحل المناسب للموقع ونقدّم عرضاً فنياً وتجارياً واضحاً.', den: 'We select the right solution for the site and submit a clear technical and commercial proposal.' },
  { ar: 'التوريد والخدمات اللوجستية', en: 'Supply and logistics', dar: 'ننسّق التوريد والشحن والتخليص الجمركي حتى وصول المعدات إلى الموقع.', den: 'We coordinate supply, shipping and customs clearance until the equipment reaches the site.' },
  { ar: 'التركيب أو الإشراف الفني', en: 'Installation or technical supervision', dar: 'نركّب المعدات أو نشرف على تركيبها عبر فنيين مؤهلين وفق إجراءات السلامة.', den: 'We install the equipment, or supervise its installation, through qualified technicians following safety procedures.' },
  { ar: 'الاختبار والتشغيل والتسليم', en: 'Testing, commissioning and handover', dar: 'نختبر النظام ونشغّله ونسلّمه جاهزاً للعمل.', den: 'We test, commission and hand over a working system.' },
  { ar: 'تدريب المشغلين', en: 'Operator training', dar: 'ندرّب فريقك على التشغيل الصحيح والاستخدام الآمن وإجراءات الطوارئ.', den: 'We train your team on correct operation, safe use and emergency procedures.' },
  { ar: 'الصيانة الوقائية والتصحيحية', en: 'Preventive and corrective maintenance', dar: 'نجري صيانة دورية ونستجيب للأعطال حفاظاً على استمرارية التشغيل.', den: 'We carry out scheduled maintenance and respond to faults to keep operations running.' },
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

// Values and working principles merged into one list (expert review, 27 Nov 2026)
const values = [
  { ar: 'احتياج العميل أولاً', en: 'The customer\'s need first', dar: 'نبني كل قرار تجاري وهندسي على ما يحتاجه تشغيلك فعلاً.', den: 'We base every commercial and engineering decision on what your operation actually needs.' },
  { ar: 'الجودة', en: 'Quality', dar: 'نختار ونورّد حلولاً ومعدات تلبي المتطلبات الفنية ومعايير الجودة ذات الصلة.', den: 'We select and supply solutions and equipment that meet the relevant technical and quality requirements.' },
  { ar: 'النزاهة', en: 'Integrity', dar: 'نقدّم معلومات فنية وتجارية واضحة ودقيقة.', den: 'We give clear, accurate technical and commercial information.' },
  { ar: 'السلامة', en: 'Safety', dar: 'نراعي متطلبات السلامة في الحلول والمعدات والخدمات التي نقدّمها.', den: 'We build safety requirements into the solutions, equipment and services we provide.' },
  { ar: 'الالتزام', en: 'Commitment', dar: 'نحترم نطاق العمل والمتطلبات التعاقدية ومواعيد التوريد المتفق عليها.', den: 'We respect the agreed scope of work, contractual requirements and delivery dates.' },
  { ar: 'الشراكة طويلة الأمد', en: 'Long-term partnership', dar: 'نبني علاقات مستدامة مع العملاء والمصنِّعين والشركاء على أساس الثقة والقيمة المتبادلة.', den: 'We build lasting relationships with customers, manufacturers and partners based on trust and mutual value.' }
]

const whyUs = [
  { ar: 'حضور محلي في الدوحة', en: 'Local presence in Doha', dar: 'فهم مباشر لمتطلبات السوق القطري والمنشآت والمشاريع، ومعاينة في موقعك.', den: "A direct understanding of Qatar's market, facilities and projects, and site surveys at your premises." },
  { ar: 'وكالة حصرية وتوزيع معتمد', en: 'Exclusive agency and authorised distribution', dar: 'الوكيل الحصري لساب تك في قطر، وموزّعون معتمدون للعديد من المصانع والشركات العالمية.', den: 'The exclusive SAB TECH agent in Qatar, and authorised distributors for many international manufacturers and companies.' },
  { ar: 'جهة واحدة لاحتياجات متعددة', en: 'One company for many needs', dar: 'الخطوط الأربعة وحلول الطاقة والمعدات الثقيلة والتوريد حسب الطلب، في عرض واحد ومتابعة واحدة.', den: 'The four lines, energy solutions, heavy equipment and sourcing on request, in one proposal with one point of follow-up.' },
  { ar: 'ترشيح على قدر حاجتك', en: 'Recommendations sized to your need', dar: 'نرشّح ما يناسب تشغيلك وميزانيتك، ونقول لك صراحة متى يكفيك حل أصغر.', den: 'We recommend what suits your operation and budget, and tell you plainly when a smaller solution will do.' },
  { ar: 'دعم بعد التسليم', en: 'Support after handover', dar: 'تدريب وصيانة وقطع غيار وفق طبيعة المنتج ونطاق المشروع.', den: 'Training, maintenance and spare parts according to the product and project scope.' }
]

const faq = [
  { q: { ar: 'ما هي بيستوليكس؟', en: 'What is Bestolex?' }, a: { ar: 'بيستوليكس لتجارة الآلات والمعدات الثقيلة (ذ.م.م) شركة قطرية في الدوحة، وهي الوكيل الحصري لساب تك في قطر وموزّع معتمد للعديد من المصانع والشركات العالمية. تورّد وتركّب وتصون أنظمة التحميل والمستودعات والنفايات وإعادة التدوير والحماية المحيطية والأبواب الصناعية، وتقدّم حلول الطاقة والتوريد حسب الطلب.', en: 'Bestolex Trading of Heavy Equipment and Machinery W.L.L. is a Qatari company in Doha. It is the exclusive SAB TECH agent in Qatar and an authorised distributor for many international manufacturers and companies. It supplies, installs and maintains loading and warehouse systems, waste and recycling equipment, perimeter protection and industrial doors, and provides energy solutions and sourcing on request.' } },
  { q: { ar: 'ما علاقة بيستوليكس بساب تك؟', en: 'How is Bestolex related to SAB TECH?' }, a: { ar: 'ساب تك (شركة أساس السعودية لأعمال التقنية المحدودة) هي الشريك الاستراتيجي المصنِّع، وبيستوليكس وكيلها الحصري في قطر لخطوطها الأربعة. الخبرة التي تتجاوز 25 عاماً وشهادة ISO 9001:2015 وعلامة CE تخص ساب تك ومنتجاتها.', en: 'SAB TECH (Saudi Basis for Technical Works Ltd.) is the strategic manufacturing partner, and Bestolex is its exclusive agent in Qatar for its four lines. The 25+ years of experience, ISO 9001:2015 certification and CE marking belong to SAB TECH and its products.' } },
  { q: { ar: 'هل تورّد بيستوليكس معدات غير موجودة في موقعها؟', en: 'Does Bestolex supply equipment that is not on its website?' }, a: { ar: 'نعم. خدمة التوريد حسب الطلب تغطي أي آلة أو معدّة لأي نشاط، من مصانع حول العالم، مع الشحن والتخليص الجمركي والتركيب والتدريب والصيانة.', en: 'Yes. The sourcing on request service covers any machine or equipment for any activity, from manufacturers worldwide, with shipping, customs clearance, installation, training and maintenance.' } },
  { q: { ar: 'هل تعمل بيستوليكس خارج قطر؟', en: 'Does Bestolex work outside Qatar?' }, a: { ar: 'السوق الأساسي قطر. وتورّد بيستوليكس معدات تعدين الذهب والطاقة إلى مشاريع الشرق الأوسط وأفريقيا، وتغطي سلسلة تعدين الذهب كاملة من مورّد واحد، من التنقيب والحفر إلى الصهر والمختبر.', en: 'Qatar is the main market. Bestolex also supplies gold-mining and energy equipment to projects in the Middle East and Africa, covering the whole gold-mining chain from one supplier, from exploration and drilling to smelting and the lab.' } }
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
            description: t('الشريك الاستراتيجي المصنِّع، وبيستوليكس وكيلها الحصري في قطر.', 'Strategic manufacturing partner; Bestolex is its exclusive agent in Qatar.')
          },
          {
            '@type': 'FAQPage',
            '@id': `${SITE_URL}${localePath('/about')}#faq`,
            mainEntity: faq.map(f => ({ '@type': 'Question', name: t(f.q.ar, f.q.en), acceptedAnswer: { '@type': 'Answer', text: t(f.a.ar, f.a.en) } }))
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
