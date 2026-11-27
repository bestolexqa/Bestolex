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
          <h1 class="font-display text-4xl md:text-6xl font-extrabold leading-[1.15] mb-5">
            {{ t('بيستوليكس لتجارة الآلات والمعدات الثقيلة', 'Bestolex Trading of Heavy Equipment and Machinery') }}
          </h1>
          <p class="font-display text-xl md:text-2xl text-primary font-bold mb-6">
            {{ t('قوة تدفع أعمالكم... ثقة تدوم', 'Power That Drives Your Business. Trust That Lasts') }}
          </p>
          <p class="text-lg md:text-xl text-gray-300 leading-relaxed max-w-[65ch] mb-8">
            {{ t('شركة قطرية في الدوحة، والوكيل الحصري لمنتجات ساب تك في قطر. نورّد ونركّب ونصون أنظمة التحميل والمستودعات، ومعدات النفايات وإعادة التدوير، والحماية المحيطية، والأبواب الصناعية، ونقدّم حلول الطاقة، ونورّد حسب الطلب أي آلة أو خط إنتاج من مصانع حول العالم.',
                 'A Qatari company based in Doha and the exclusive SABTECH agent in Qatar. We supply, install and maintain loading and warehouse systems, waste and recycling equipment, perimeter protection and industrial doors, provide energy solutions, and source any machine or production line on request from factories worldwide.') }}
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

    <!-- Who we are + company data -->
    <section class="py-16 md:py-24">
      <div class="container mx-auto px-4 md:px-8 grid lg:grid-cols-12 gap-12">
        <div class="lg:col-span-7 space-y-5 text-lg leading-relaxed text-slate dark:text-gray-300">
          <h2 class="font-display text-3xl md:text-4xl font-bold text-ink dark:text-white mb-2">{{ t('من نحن', 'Who we are') }}</h2>
          <p>
            {{ t('بيستوليكس لتجارة الآلات والمعدات الثقيلة (ذ.م.م) شركة قطرية تخدم المنشآت الصناعية واللوجستية والتجارية والحكومية. نحن الوكيل الحصري في قطر لشركة ساب تك، شريكنا الاستراتيجي والجهة المصنِّعة، في خطوطها الأربعة: أنظمة التحميل والمستودعات، والنفايات وإعادة التدوير، والحماية المحيطية، والأبواب الصناعية.',
                 'Bestolex Trading of Heavy Equipment and Machinery W.L.L. is a Qatari company serving industrial, logistics, commercial and government facilities. We are the exclusive agent in Qatar for SAB TECH, our strategic partner and manufacturer, across its four lines: loading and warehouse systems, waste and recycling, perimeter protection and industrial doors.') }}
          </p>
          <p>
            {{ t('وإلى جانب الوكالة، نقدّم حلول الطاقة الشمسية ومجموعات التوليد، ونورّد المعدات الثقيلة عند الطلب. وما لا يدخل في أقسامنا نورّده حسب الطلب لأي نشاط، من المقاولات والمصانع والورش إلى المستشفيات والمطاعم والمزارع: يصف العميل ما يحتاجه، ويقارن مهندسونا الخيارات ويرشّحون الأنسب، ثم نتولى الشراء والشحن والتركيب والتدريب والصيانة.',
                 'Beyond the agency, we provide solar energy systems and generating sets, and supply heavy equipment on request. Anything outside our sections we source on request for any activity, from contracting, factories and workshops to hospitals, restaurants and farms: the customer describes what they need, our engineers compare the options and recommend the best fit, then we handle purchasing, shipping, installation, training and maintenance.') }}
          </p>
          <p>
            {{ t('وخارج قطر، نورّد معدات تعدين الذهب والطاقة إلى مشاريع الشرق الأوسط وأفريقيا، فنحن وكلاء وموزّعون لكثير من المصانع العالمية في المنطقة.',
                 'Outside Qatar, we supply gold-mining and energy equipment to projects in the Middle East and Africa, as agents and distributors for many international factories in the region.') }}
          </p>
        </div>
        <aside class="lg:col-span-5">
          <div class="bg-surface dark:bg-gray-800/60 border border-line dark:border-gray-700 rounded-2xl p-6 md:p-8">
            <h2 class="font-display text-xl font-bold mb-5">{{ t('بيانات الشركة', 'Company details') }}</h2>
            <dl class="divide-y divide-line dark:divide-gray-700 text-sm">
              <div class="py-3 grid grid-cols-3 gap-3">
                <dt class="text-slate dark:text-gray-400">{{ t('الاسم الرسمي', 'Legal name') }}</dt>
                <dd class="col-span-2 font-bold leading-relaxed">
                  بيستوليكس لتجارة الآلات والمعدات الثقيلة (ذ.م.م)
                  <span class="block font-normal text-slate dark:text-gray-400" dir="ltr">Bestolex Trading of Heavy Equipment and Machinery W.L.L.</span>
                </dd>
              </div>
              <div class="py-3 grid grid-cols-3 gap-3">
                <dt class="text-slate dark:text-gray-400">{{ t('الشكل القانوني', 'Legal form') }}</dt>
                <dd class="col-span-2 font-bold">{{ t('شركة ذات مسؤولية محدودة، دولة قطر', 'Limited liability company, State of Qatar') }}</dd>
              </div>
              <div class="py-3 grid grid-cols-3 gap-3">
                <dt class="text-slate dark:text-gray-400">{{ t('السجل التجاري', 'Commercial registration') }}</dt>
                <dd class="col-span-2 font-bold font-mono">248416</dd>
              </div>
              <div class="py-3 grid grid-cols-3 gap-3">
                <dt class="text-slate dark:text-gray-400">{{ t('المقر', 'Office') }}</dt>
                <dd class="col-span-2 font-bold leading-relaxed">{{ t('المنتزه، المنطقة 24، شارع 830، مبنى 16، الطابق 7، مكتب 714، الدوحة', 'Al Muntazah, Zone 24, Street 830, Building 16, Floor 7, Office 714, Doha') }}</dd>
              </div>
              <div class="py-3 grid grid-cols-3 gap-3">
                <dt class="text-slate dark:text-gray-400">{{ t('ساعات العمل', 'Working hours') }}</dt>
                <dd class="col-span-2 font-bold"><span dir="ltr">7:00–18:00</span>{{ t('، الأحد إلى الخميس والسبت', ', Sunday to Thursday and Saturday') }}</dd>
              </div>
              <div class="py-3 grid grid-cols-3 gap-3">
                <dt class="text-slate dark:text-gray-400">{{ t('التواصل', 'Contact') }}</dt>
                <dd class="col-span-2 font-bold space-y-1">
                  <a href="tel:+97451505014" class="block hover:text-primary" dir="ltr">+974 5150 5014</a>
                  <a href="tel:+97450708833" class="block hover:text-primary" dir="ltr">+974 5070 8833</a>
                  <a href="mailto:info@bestolex.com" class="block hover:text-primary">info@bestolex.com</a>
                </dd>
              </div>
            </dl>
          </div>
        </aside>
      </div>
    </section>

    <!-- Vision, mission -->
    <section class="py-16 md:py-20 bg-surface dark:bg-[#0f1216]">
      <div class="container mx-auto px-4 md:px-8 grid md:grid-cols-2 gap-6">
        <div class="bg-white dark:bg-gray-800 border border-line dark:border-gray-700 rounded-2xl p-8 md:p-10">
          <p class="text-primary font-bold mb-2">{{ t('رؤيتنا', 'Our vision') }}</p>
          <p class="font-display text-xl md:text-2xl font-bold leading-relaxed">
            {{ t('أن تكون بيستوليكس الشريك الأول الذي تثق به المنشآت الصناعية واللوجستية في قطر لرفع كفاءتها التشغيلية وتعزيز سلامتها ودعم استدامتها.',
                 'For Bestolex to be the partner industrial and logistics facilities in Qatar turn to first, to raise their operating efficiency, strengthen their safety and support their sustainability.') }}
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
          {{ t('ساب تك في قطر: الوكالة الحصرية', 'SAB TECH in Qatar: exclusive agency') }}
        </h3>
        <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-5 mb-14">
          <NuxtLink v-for="a in agencyLines" :key="a.link" :to="localePath(a.link)" class="group border border-line dark:border-gray-700 rounded-2xl overflow-hidden bg-white dark:bg-gray-800 hover:border-primary transition flex flex-col">
            <NuxtImg :src="a.img" :alt="t(a.ar, a.en)" class="w-full aspect-[4/3] object-cover" width="600" height="450" format="webp" loading="lazy" />
            <div class="p-5 flex-1 flex flex-col">
              <h4 class="font-display text-lg font-bold mb-2 group-hover:text-primary transition">{{ t(a.ar, a.en) }}</h4>
              <p class="text-sm text-slate dark:text-gray-400 leading-relaxed flex-1">{{ t(a.dar, a.den) }}</p>
              <span class="text-primary font-bold text-sm mt-4">{{ t('منتجات القسم', 'Category products') }} <span class="rtl:rotate-180 inline-block" aria-hidden="true">&rarr;</span></span>
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
            <h4 class="font-display text-2xl font-bold mb-3">{{ t('معدات تعدين الذهب للشرق الأوسط وأفريقيا', 'Gold-mining equipment for the Middle East and Africa') }}</h4>
            <p class="text-gray-300 leading-relaxed mb-6">
              {{ t('نورّد معدات مواقع التعدين من التنقيب حتى الصبّ، بصفتنا وكلاء وموزّعين لكثير من المصانع العالمية في المنطقة، مع قطع الغيار والمستهلكات التي تُبقي الموقع يعمل.',
                   'We supply mining-site equipment from exploration to pouring, as agents and distributors for many international factories in the region, together with the spare parts and consumables that keep a site running.') }}
            </p>
            <ul class="grid sm:grid-cols-2 gap-x-6 gap-y-2 text-sm text-gray-200 mb-8">
              <li v-for="m in miningAreas" :key="m.ar" class="flex gap-2"><span class="text-primary" aria-hidden="true">•</span>{{ t(m.ar, m.en) }}</li>
            </ul>
            <NuxtLink :to="localePath('/contact')" class="inline-block bg-primary text-[#191919] font-bold px-6 py-3 rounded-lg hover:bg-[#f2b02a] transition">
              {{ t('اطلب عرضاً لمشروعك', 'Request an offer for your project') }}
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
            {{ t('بيستوليكس هي الوكيل الحصري في قطر لشركة أساس السعودية لأعمال التقنية المحدودة (ساب تك). تمتد خبرة ساب تك لأكثر من 25 عاماً في التصنيع والحلول الهندسية، وهي حاصلة على شهادة إدارة الجودة ISO 9001:2015، وتحمل منتجاتها المشمولة بوثائقها الفنية علامة CE، ولها حضور في جدة والرياض والدمام وخميس مشيط ودبي.',
                 'Bestolex is the exclusive agent in Qatar for Saudi Basis for Technical Works Ltd. (SAB TECH). SAB TECH brings more than 25 years of manufacturing and engineering experience, holds ISO 9001:2015 quality management certification, its products covered by its technical documentation carry CE marking, and it has a presence in Jeddah, Riyadh, Dammam, Khamis Mushait and Dubai.') }}
          </p>
          <ul class="flex flex-wrap gap-3 text-sm font-bold">
            <li class="bg-white dark:bg-gray-800 border border-line dark:border-gray-700 rounded-lg px-4 py-2">{{ t('ساب تك: خبرة 25+ سنة', 'SAB TECH: 25+ years') }}</li>
            <li class="bg-white dark:bg-gray-800 border border-line dark:border-gray-700 rounded-lg px-4 py-2">{{ t('ساب تك: ISO 9001:2015', 'SAB TECH: ISO 9001:2015') }}</li>
            <li class="bg-white dark:bg-gray-800 border border-line dark:border-gray-700 rounded-lg px-4 py-2">{{ t('علامة CE على منتجات ساب تك', 'CE marking on SAB TECH products') }}</li>
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
          <h2 class="font-display text-3xl md:text-4xl font-bold mb-4">{{ t('حدّثنا عن مشروعك', 'Tell us about your project') }}</h2>
          <p class="text-gray-300 text-lg leading-relaxed">{{ t('معاينة للموقع، أو عرض سعر لمنتج من منتجاتنا، أو آلة تبحث عنها ولا تجدها. نرد عليك خلال ساعات العمل.', "A site survey, a quote for one of our products, or a machine you are looking for and can't find. We reply during working hours.") }}</p>
        </div>
        <div class="lg:col-span-5 flex flex-wrap gap-3 lg:justify-end">
          <NuxtLink :to="localePath('/contact')" class="bg-primary text-[#191919] font-bold px-7 py-3.5 rounded-lg hover:bg-[#f2b02a] transition">{{ t('تواصل معنا', 'Contact us') }}</NuxtLink>
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
  { lar: 'مراحل الخدمة', len: 'Service stages', ar: '8 مراحل، من الدراسة إلى الصيانة', en: '8 stages, study to maintenance' },
  { lar: 'الأسواق', len: 'Markets', ar: 'قطر، والشرق الأوسط وأفريقيا', en: 'Qatar, the Middle East and Africa' },
  { lar: 'السجل التجاري', len: 'Commercial registration', ar: '248416', en: '248416' }
]

const agencyLines = [
  { link: '/products/category/docking-systems', img: catImage('docking-systems'), ar: 'أنظمة التحميل والمستودعات', en: 'Loading and warehouse systems', dar: 'أرصفة التحميل الثابتة والمتحركة، ومظلات الأرصفة، والرافعات المقصية، ومصاعد البضائع.', den: 'Fixed and mobile dock levelers, dock shelters, scissor lifts and goods lifts.' },
  { link: '/products/category/waste-management', img: catImage('waste-management'), ar: 'النفايات وإعادة التدوير', en: 'Waste and recycling', dar: 'مكابس الكرتون والبلاستيك والحديد والأقمشة، وضواغط النفايات، ومنها ضاغط يعمل بالطاقة الشمسية.', den: 'Cardboard, plastic, metal and textile balers, and waste compactors, including a solar-powered compactor.' },
  { link: '/products/category/perimeter-protection', img: catImage('perimeter-protection'), ar: 'الحماية المحيطية', en: 'Perimeter protection', dar: 'مصدات الطريق ومفجرات الإطارات والبولارد الهيدروليكي والبوابات الدوارة وأنظمة الكشف تحت المركبات.', den: 'Road blockers, tyre killers, hydraulic bollards, turnstiles and under-vehicle inspection systems.' },
  { link: '/products/category/industrial-doors', img: catImage('industrial-doors'), ar: 'الأبواب الصناعية', en: 'Industrial doors', dar: 'الأبواب المقطعية والسريعة والشتر الصناعي والأبواب الخاصة للمنشآت.', den: 'Sectional, high-speed, rolling shutter and special doors for facilities.' }
]

const otherLines = [
  { link: '/products/category/energy-solutions', img: catImage('energy-solutions'), ar: 'حلول الطاقة', en: 'Energy solutions', dar: 'الألواح الشمسية والانفرترات وبطاريات التخزين والإنارة الشمسية والأنظمة التجارية والصناعية، ومجموعات التوليد.', den: 'Solar panels, inverters, storage batteries, solar lighting, commercial and industrial systems, and generating sets.', car: 'منتجات الطاقة', cen: 'Energy products' },
  { link: '/contact', img: '/about/heavy-equipment.webp', ar: 'المعدات الثقيلة عند الطلب', en: 'Heavy equipment on request', dar: 'الحفارات واللوادر وشاحنات القلاب والرافعات ومعدات الأنفاق والمناجم، نورّدها حسب المواصفة المطلوبة.', den: 'Excavators, loaders, dump trucks, cranes and tunnelling and mining equipment, supplied to the required specification.', car: 'اطلب معدة', cen: 'Request equipment' },
  { link: '/sourcing', icons: SOURCING_SECTORS.slice(0, 8).map(x => x.icon), ar: 'التوريد حسب الطلب', en: 'Sourcing on request', dar: 'أي آلة أو معدة ليست في أقسامنا، لأي نشاط: معدات البناء والسقالات، وقطع الغيار، والمضخات والضواغط، ومكائن الورش، ومعدات المطاعم والمستشفيات والمزارع، من مصانع حول العالم.', den: 'Any machine or equipment outside our sections, for any activity: construction equipment and scaffolding, spare parts, pumps and compressors, workshop machines, and equipment for restaurants, hospitals and farms, from factories worldwide.', car: 'التوريد حسب الطلب', cen: 'Sourcing on request' },
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
  { ar: 'التركيب أو الإشراف الفني', en: 'Installation or technical supervision', dar: 'نركّب المعدات بفريقنا الفني أو نشرف على تركيبها وفق إجراءات السلامة.', den: 'Our technical team installs the equipment or supervises its installation following safety procedures.' },
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
  { ar: 'حضور محلي في الدوحة', en: 'Local presence in Doha', dar: 'فهم مباشر لمتطلبات السوق القطري والمنشآت والمشاريع، وفريق يصل إلى موقعك.', den: "A direct understanding of Qatar's market, facilities and projects, and a team that comes to your site." },
  { ar: 'وكالة حصرية وشراكة صناعية', en: 'Exclusive agency and industrial partnership', dar: 'وكالة حصرية وشراكة استراتيجية مع ساب تك في نطاق منتجاتها المعتمدة.', den: 'An exclusive agency and strategic partnership with SAB TECH within its approved product scope.' },
  { ar: 'جهة واحدة لاحتياجات متعددة', en: 'One company for many needs', dar: 'الخطوط الأربعة وحلول الطاقة والمعدات الثقيلة والتوريد حسب الطلب من جهة واحدة، بعرض واحد ومتابعة واحدة.', den: 'The four lines, energy solutions, heavy equipment and sourcing on request from one company, with one offer and one point of follow-up.' },
  { ar: 'ترشيح محايد', en: 'Neutral recommendations', dar: 'نرشّح ما يناسب تشغيلك وميزانيتك، ونقول لك صراحة متى يكفيك حل أصغر.', den: 'We recommend what suits your operation and budget, and tell you plainly when a smaller solution will do.' },
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
  { ar: 'بناء دعم فني وخدمات ما بعد بيع عالية الكفاءة.', en: 'Building efficient technical support and after-sales services.' }
]

const pageTitle = computed(() => t('من نحن | بيستوليكس لتجارة الآلات والمعدات الثقيلة', 'About Bestolex | Exclusive SABTECH Agent in Qatar'))
const pageDesc = computed(() => t(
  'بيستوليكس شركة قطرية والوكيل الحصري لساب تك في قطر: أنظمة التحميل والنفايات والحماية المحيطية والأبواب الصناعية، وحلول الطاقة، والتوريد حسب الطلب.',
  'Qatari company and exclusive SABTECH agent in Qatar: loading, waste, perimeter security, industrial doors, energy solutions and sourcing on request.'
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
            name: pageTitle.value,
            description: pageDesc.value,
            url: `${SITE_URL}${localePath('/about')}`,
            isPartOf: { '@id': WEBSITE_ID },
            about: { '@id': ORG_ID }
          },
          {
            '@type': 'BreadcrumbList',
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
