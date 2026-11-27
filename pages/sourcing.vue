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
            <p class="text-primary font-bold tracking-wide mb-3">{{ t('التوريد حسب الطلب · شراء وتوريد للغير', 'Sourcing on request · Procurement on your behalf') }}</p>
            <h1 class="font-display text-4xl md:text-5xl font-extrabold leading-[1.2] mb-6">
              {{ t('توريد المعدات والآلات حسب الطلب، لأي نشاط في قطر', 'Equipment and machinery sourcing for any industry in Qatar') }}
            </h1>
            <p class="text-lg text-gray-300 leading-relaxed max-w-[62ch] mb-8">
              {{ t('مقاول يحتاج سقالات وخلاطات خرسانة، أو مصنع يريد خط إنتاج، أو مستشفى يحتاج أجهزة طبية، أو ورشة حدادة أو نجارة تحتاج مكائن جديدة؟ صف لنا ما تحتاجه، ونحن نبحث عنه في مصانع حول العالم ونقارن العروض ونشتريه نيابة عنك، ثم نشحنه ونخلّصه جمركياً ونركّبه في موقعك.',
                   'A contractor who needs scaffolding and concrete mixers, a factory that wants a production line, a hospital that needs medical equipment, or a metal or carpentry workshop that needs new machines? Tell us what you need. We look for it in factories around the world, compare the offers and buy it on your behalf, then ship it, clear customs and install it on your site.') }}
            </p>
            <div class="flex flex-wrap gap-3">
              <a href="#request" class="inline-flex items-center gap-2 bg-primary text-[#191919] font-bold px-7 py-3.5 rounded-lg hover:bg-[#f2b02a] transition">
                {{ t('صف ما تحتاجه', 'Describe what you need') }}
              </a>
              <a :href="waLink" target="_blank" rel="noopener" class="inline-flex items-center gap-2 border border-gray-500 text-white font-bold px-7 py-3.5 rounded-lg hover:border-primary hover:text-primary transition" @click="trackWa">
                {{ t('واتساب', 'WhatsApp') }} <span dir="ltr" class="font-normal">+974 5150 5014</span>
              </a>
            </div>
          </div>
          <aside class="lg:col-span-5 bg-white/[0.04] border border-white/10 rounded-2xl p-6 md:p-7">
            <p class="text-sm text-gray-400 mb-4">{{ t('أمثلة لما يمكنك طلبه', 'Examples of what you can ask for') }}</p>
            <ul class="space-y-3">
              <li v-for="e in heroExamples" :key="e.ar" class="flex items-center gap-4 bg-white/[0.04] rounded-xl px-4 py-3">
                <span class="w-10 h-10 shrink-0 rounded-lg bg-primary/15 text-primary flex items-center justify-center">
                  <SourcingIcon :name="e.icon" class="w-5 h-5" />
                </span>
                <span class="font-bold leading-snug">{{ t(e.ar, e.en) }}</span>
              </li>
            </ul>
          </aside>
        </div>
        <ul class="grid sm:grid-cols-3 gap-4 mt-12">
          <li v-for="c in chips" :key="c.a" class="border border-white/15 rounded-xl px-5 py-4">
            <p class="font-display font-bold text-lg text-white">{{ t(c.a, c.ae) }}</p>
            <p class="text-sm text-gray-400 mt-1">{{ t(c.b, c.be) }}</p>
          </li>
        </ul>
      </div>
    </section>

    <!-- In short (a direct answer for readers and AI assistants) -->
    <section id="summary" class="py-14 md:py-16">
      <div class="container mx-auto px-4 md:px-8 grid lg:grid-cols-12 gap-8">
        <div class="lg:col-span-7 border-s-4 border-primary ps-6">
          <h2 class="font-display text-2xl md:text-3xl font-bold mb-4">{{ t('باختصار: ما هو التوريد حسب الطلب؟', 'In short: what is sourcing on request?') }}</h2>
          <p class="text-lg leading-relaxed text-slate dark:text-gray-300">
            {{ t('التوريد حسب الطلب خدمة شراء وتوريد للغير تقدّمها بيستوليكس لتجارة الآلات والمعدات الثقيلة، الشركة القطرية في الدوحة. نشتري للعميل أي آلة أو معدة أو جهاز أو خط إنتاج أو قطع غيار غير موجودة في أقسام منتجاتنا، من مصانع حول العالم، ونتولى المقارنة والفحص والشحن والتخليص الجمركي والتركيب والتدريب والصيانة. نخدم المقاولين والمصانع والورش والمطاعم والمقاهي والفنادق والمستشفيات والمزارع والمختبرات والجهات الحكومية في قطر.',
                 'Sourcing on request is a procurement service from Bestolex Trading of Heavy Equipment and Machinery, a Qatari company based in Doha. We buy, on the customer\'s behalf, any machine, equipment, device, production line or spare part that is not in our own product sections, from factories around the world, and handle the comparison, inspection, shipping, customs clearance, installation, training and maintenance. We serve contractors, factories, workshops, restaurants, cafés and hotels, hospitals, farms, laboratories and government entities in Qatar.') }}
          </p>
        </div>
        <dl class="lg:col-span-5 grid grid-cols-2 gap-px bg-line dark:bg-gray-700 border border-line dark:border-gray-700 rounded-2xl overflow-hidden text-sm">
          <div v-for="f in facts" :key="f.lar" class="bg-surface dark:bg-gray-800 p-4">
            <dt class="text-slate dark:text-gray-400">{{ t(f.lar, f.len) }}</dt>
            <dd class="font-bold mt-1 leading-snug">{{ t(f.ar, f.en) }}</dd>
          </div>
        </dl>
      </div>
    </section>

    <!-- What this page is not for -->
    <section class="pb-14">
      <div class="container mx-auto px-4 md:px-8">
        <div class="bg-surface dark:bg-gray-800/60 border border-line dark:border-gray-700 rounded-2xl p-6 md:p-8 flex flex-col lg:flex-row lg:items-center gap-6">
          <div class="flex-1">
            <h2 class="font-display text-xl font-bold mb-2">{{ t('هذه الخدمة لما ليس في أقسامنا', "This service is for what isn't in our sections") }}</h2>
            <p class="text-slate dark:text-gray-400 leading-relaxed">{{ t('أرصفة التحميل، ومكابس النفايات، ومصدات الطريق، والأبواب الصناعية، وأنظمة الطاقة الشمسية لها أقسامها الخاصة في الموقع. والتوريد حسب الطلب لكل ما عداها.', 'Dock levelers, waste balers, road blockers, industrial doors and solar energy systems have their own sections on the site. Sourcing on request covers everything else.') }}</p>
          </div>
          <ul class="flex flex-wrap gap-2">
            <li v-for="c in ownSections" :key="c.id">
              <NuxtLink :to="localePath(`/products/category/${c.id}`)" class="inline-block bg-white dark:bg-gray-900 border border-line dark:border-gray-600 rounded-full px-4 py-2 text-sm font-bold hover:border-primary hover:text-primary transition">{{ t(c.ar, c.en) }}</NuxtLink>
            </li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Sectors -->
    <section id="sectors" class="py-16 md:py-20 bg-surface dark:bg-[#0f1216]">
      <div class="container mx-auto px-4 md:px-8">
        <h2 class="font-display text-3xl md:text-4xl font-bold mb-3">{{ t('نورّد المعدات لكل نشاط', 'Equipment for every activity') }}</h2>
        <p class="text-slate dark:text-gray-400 text-lg mb-10 max-w-[70ch]">{{ t('أمثلة من القطاعات التي نورّد لها. القائمة لا تحصر ما نستطيع توريده: إن كانت الآلة تُصنع في مكان ما، نبحث عنها لك.', 'Examples of the sectors we supply. The list is not exhaustive: if the machine is made somewhere, we will look for it.') }}</p>
        <div class="grid sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
          <article v-for="s in SOURCING_SECTORS" :id="s.id" :key="s.id" class="bg-white dark:bg-gray-800 border border-line dark:border-gray-700 rounded-2xl p-6 scroll-mt-24 flex flex-col">
            <div class="flex items-center gap-3 mb-4">
              <span class="w-11 h-11 shrink-0 rounded-xl bg-[#191919] text-primary flex items-center justify-center">
                <SourcingIcon :name="s.icon" class="w-6 h-6" />
              </span>
              <h3 class="font-display text-lg font-bold leading-snug">{{ t(s.ar, s.en) }}</h3>
            </div>
            <ul class="space-y-1.5 text-sm text-slate dark:text-gray-300 flex-1">
              <li v-for="(it, i) in (isAr ? s.itemsAr : s.itemsEn)" :key="i" class="flex gap-2"><span class="text-primary" aria-hidden="true">•</span>{{ it }}</li>
            </ul>
            <p v-if="s.noteAr" class="mt-4 text-xs text-slate dark:text-gray-400 leading-relaxed border-t border-line dark:border-gray-700 pt-3">{{ t(s.noteAr, s.noteEn) }}</p>
          </article>
          <a href="#request" class="rounded-2xl p-6 bg-[#191919] text-white flex flex-col justify-between hover:ring-2 hover:ring-primary transition">
            <span class="w-11 h-11 rounded-xl bg-primary text-[#191919] flex items-center justify-center mb-4">
              <SourcingIcon name="plus" class="w-6 h-6" />
            </span>
            <span>
              <span class="block font-display text-lg font-bold mb-2">{{ t('نشاطك ليس في القائمة؟', 'Your activity is not listed?') }}</span>
              <span class="block text-sm text-gray-300 leading-relaxed">{{ t('أرسل طلبك على أي حال، ونخبرك بسرعة إن كنا نستطيع توريده.', "Send your request anyway and we'll quickly tell you whether we can supply it.") }}</span>
            </span>
          </a>
        </div>
      </div>
    </section>

    <!-- Request size -->
    <section class="py-16 md:py-20">
      <div class="container mx-auto px-4 md:px-8">
        <h2 class="font-display text-3xl font-bold mb-3">{{ t('من آلة واحدة إلى مصنع كامل', 'From one machine to a complete plant') }}</h2>
        <p class="text-slate dark:text-gray-400 mb-10 max-w-[70ch]">{{ t('لا حد أدنى للطلب. هذه الأنواع الخمسة تغطي معظم ما يصلنا.', 'There is no minimum order. These five kinds cover most requests.') }}</p>
        <div class="grid sm:grid-cols-2 lg:grid-cols-5 gap-5">
          <article v-for="(k, i) in kinds" :key="k.id" class="border border-line dark:border-gray-700 rounded-2xl p-6">
            <span class="font-display text-primary font-bold text-sm">0{{ i + 1 }}</span>
            <h3 class="font-display text-lg font-bold mt-2 mb-2">{{ t(k.ar, k.en) }}</h3>
            <p class="text-sm text-slate dark:text-gray-400 leading-relaxed">{{ t(k.dar, k.den) }}</p>
          </article>
        </div>
      </div>
    </section>

    <!-- How it works: the eight service stages -->
    <section id="how" class="py-16 md:py-20 bg-surface dark:bg-[#0f1216]">
      <div class="container mx-auto px-4 md:px-8">
        <h2 class="font-display text-3xl font-bold mb-3">{{ t('كيف يعمل التوريد حسب الطلب', 'How sourcing on request works') }}</h2>
        <p class="text-slate dark:text-gray-400 mb-10 max-w-[70ch]">{{ t('ثماني مراحل من فهم الاحتياج إلى قطع الغيار، وأنت تتعامل مع جهة واحدة في الدوحة طوال الوقت.', 'Eight stages from understanding the need to spare parts, with one company in Doha to deal with throughout.') }}</p>
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

    <!-- Import it yourself or through Bestolex -->
    <section class="py-16 md:py-20">
      <div class="container mx-auto px-4 md:px-8">
        <h2 class="font-display text-3xl font-bold mb-3">{{ t('تستورد بنفسك أم عبر بيستوليكس؟', 'Import it yourself, or through Bestolex?') }}</h2>
        <p class="text-slate dark:text-gray-400 mb-8 max-w-[70ch]">{{ t('الآلة نفسها، لكن الطريق إليها مختلف.', 'The same machine, a different road to it.') }}</p>
        <div class="overflow-x-auto border border-line dark:border-gray-700 rounded-2xl">
          <table class="w-full min-w-[640px] text-sm">
            <thead class="bg-[#191919] text-white">
              <tr>
                <th scope="col" class="text-start font-bold p-4 w-1/4">{{ t('المرحلة', 'Step') }}</th>
                <th scope="col" class="text-start font-bold p-4">{{ t('حين تستورد بنفسك', 'When you import yourself') }}</th>
                <th scope="col" class="text-start font-bold p-4 text-primary">{{ t('مع بيستوليكس', 'With Bestolex') }}</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-line dark:divide-gray-700">
              <tr v-for="r in compare" :key="r.ar" class="odd:bg-surface dark:odd:bg-gray-800/40">
                <th scope="row" class="text-start font-bold p-4 align-top">{{ t(r.ar, r.en) }}</th>
                <td class="p-4 text-slate dark:text-gray-400 align-top leading-relaxed">{{ t(r.selfAr, r.selfEn) }}</td>
                <td class="p-4 font-bold align-top leading-relaxed">{{ t(r.bxAr, r.bxEn) }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- Where from + what we need -->
    <section class="py-16 md:py-20 bg-surface dark:bg-[#0f1216]">
      <div class="container mx-auto px-4 md:px-8 grid lg:grid-cols-2 gap-10">
        <div>
          <h2 class="font-display text-3xl font-bold mb-4">{{ t('من أين نورّد', 'Where we source from') }}</h2>
          <p class="text-slate dark:text-gray-300 leading-relaxed mb-4">
            {{ t('نبحث في مصانع حول العالم، ونرشّح ما يطابق مواصفتك ويتوفر له دعم فني وقطع غيار على المدى الطويل، لا الأرخص فقط.', 'We search factories around the world and recommend what matches your specification and has long-term technical support and spare parts, not just the cheapest.') }}
          </p>
          <p class="text-slate dark:text-gray-300 leading-relaxed">
            {{ t('وإن كان لديك مصنع أو علامة تجارية محددة، أو مواصفة ملزمة من استشاري، نشتري وفقها ونتولى الباقي.', 'If you have a specific factory or brand in mind, or a binding consultant specification, we buy accordingly and handle the rest.') }}
          </p>
        </div>
        <div>
          <h2 class="font-display text-3xl font-bold mb-4">{{ t('ما نحتاجه منك لنبدأ', 'What we need from you to start') }}</h2>
          <ul class="space-y-3">
            <li v-for="n in needs" :key="n.ar" class="flex gap-3 bg-white dark:bg-gray-800 border border-line dark:border-gray-700 rounded-xl p-4">
              <span class="text-primary font-bold" aria-hidden="true">✓</span>
              <span class="leading-relaxed">{{ t(n.ar, n.en) }}</span>
            </li>
          </ul>
          <p class="text-sm text-slate dark:text-gray-400 mt-4">{{ t('لا تعرف المواصفة الفنية؟ لا بأس. صف العمل الذي تريد إنجازه، ونحن نستخرج المواصفة معك.', "Don't know the technical specification? That's fine. Describe the job and we'll work out the specification with you.") }}</p>
        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section id="faq" class="py-16 md:py-20">
      <div class="container mx-auto px-4 md:px-8 max-w-4xl">
        <h2 class="font-display text-3xl font-bold mb-8">{{ t('أسئلة شائعة عن التوريد حسب الطلب', 'Sourcing on request: frequently asked questions') }}</h2>
        <div class="divide-y divide-line dark:divide-gray-700 border-y border-line dark:border-gray-700">
          <details v-for="(f, i) in faq" :key="f.q.ar" class="group py-5" :open="i === 0">
            <summary class="flex justify-between items-center gap-4 cursor-pointer font-bold text-lg list-none">
              <h3 class="font-bold text-lg">{{ t(f.q.ar, f.q.en) }}</h3>
              <span class="text-primary text-2xl leading-none group-open:rotate-45 transition" aria-hidden="true">+</span>
            </summary>
            <p class="mt-3 text-slate dark:text-gray-400 leading-relaxed">{{ t(f.a.ar, f.a.en) }}</p>
          </details>
        </div>
      </div>
    </section>

    <!-- Request form -->
    <section id="request" class="py-16 md:py-20 bg-surface dark:bg-[#0f1216] scroll-mt-24">
      <div class="container mx-auto px-4 md:px-8 grid lg:grid-cols-12 gap-10">
        <div class="lg:col-span-4">
          <h2 class="font-display text-3xl font-bold mb-4">{{ t('صف ما تحتاجه', 'Describe what you need') }}</h2>
          <p class="text-slate dark:text-gray-400 mb-8 leading-relaxed">{{ t('املأ النموذج، أو أرسل لنا رسالة واتساب بوصف مختصر. نرد عليك بأسئلة فنية قصيرة إن لزم، ثم بالعرض.', 'Fill in the form, or send us a short WhatsApp message. We reply with a few technical questions if needed, then with the offer.') }}</p>
          <dl class="space-y-4 text-sm">
            <div><dt class="text-slate dark:text-gray-400">{{ t('واتساب', 'WhatsApp') }}</dt><dd><a :href="waLink" target="_blank" rel="noopener" class="font-bold hover:text-primary" dir="ltr" @click="trackWa">+974 5150 5014</a></dd></div>
            <div><dt class="text-slate dark:text-gray-400">{{ t('هاتف', 'Phone') }}</dt><dd class="space-y-1"><a href="tel:+97451505014" class="block font-bold hover:text-primary" dir="ltr">+974 5150 5014</a><a href="tel:+97450708833" class="block font-bold hover:text-primary" dir="ltr">+974 5070 8833</a></dd></div>
            <div><dt class="text-slate dark:text-gray-400">{{ t('البريد', 'Email') }}</dt><dd><a href="mailto:info@bestolex.com" class="font-bold hover:text-primary">info@bestolex.com</a></dd></div>
            <div><dt class="text-slate dark:text-gray-400">{{ t('ساعات العمل', 'Working hours') }}</dt><dd class="font-bold"><span dir="ltr">7:00–18:00</span>{{ t('، الأحد إلى الخميس والسبت', ', Sunday to Thursday and Saturday') }}</dd></div>
            <div><dt class="text-slate dark:text-gray-400">{{ t('المقر', 'Office') }}</dt><dd class="font-bold leading-relaxed">{{ t('المنتزه، المنطقة 24، شارع 830، مبنى 16، الطابق 7، مكتب 714، الدوحة', 'Al Muntazah, Zone 24, Street 830, Building 16, Floor 7, Office 714, Doha') }}</dd></div>
          </dl>
        </div>
        <form class="lg:col-span-8 bg-white dark:bg-gray-800/50 border border-line dark:border-gray-700 rounded-2xl p-6 md:p-8 grid sm:grid-cols-2 gap-5" @submit.prevent="submit">
          <label class="block">
            <span class="text-sm font-bold">{{ t('الاسم', 'Name') }} <span class="text-slate font-normal">{{ t('(مطلوب)', '(required)') }}</span></span>
            <input v-model="form.name" required autocomplete="name" class="mt-1 w-full rounded-lg border border-line dark:border-gray-600 bg-white dark:bg-gray-900 px-4 py-3" />
          </label>
          <label class="block">
            <span class="text-sm font-bold">{{ t('الجهة أو الشركة', 'Organisation or company') }}</span>
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
            <span class="text-sm font-bold">{{ t('نشاطك أو قطاعك', 'Your activity or sector') }}</span>
            <select v-model="form.sector" class="mt-1 w-full rounded-lg border border-line dark:border-gray-600 bg-white dark:bg-gray-900 px-4 py-3">
              <option v-for="s in sectorOptions" :key="s.id" :value="s.id">{{ t(s.ar, s.en) }}</option>
            </select>
          </label>
          <label class="block">
            <span class="text-sm font-bold">{{ t('حجم الطلب', 'Request size') }}</span>
            <select v-model="form.kind" class="mt-1 w-full rounded-lg border border-line dark:border-gray-600 bg-white dark:bg-gray-900 px-4 py-3">
              <option v-for="k in kindOptions" :key="k.id" :value="k.id">{{ t(k.ar, k.en) }}</option>
            </select>
          </label>
          <label class="block sm:col-span-2">
            <span class="text-sm font-bold">{{ t('الموعد المطلوب للتشغيل', 'Needed in operation by') }}</span>
            <input v-model="form.neededBy" :placeholder="t('مثال: مارس 2027', 'e.g. March 2027')" class="mt-1 w-full rounded-lg border border-line dark:border-gray-600 bg-white dark:bg-gray-900 px-4 py-3" />
          </label>
          <label class="block sm:col-span-2">
            <span class="text-sm font-bold">{{ t('ما الذي تحتاجه؟', 'What do you need?') }} <span class="text-slate font-normal">{{ t('(مطلوب)', '(required)') }}</span></span>
            <textarea v-model="form.message" required rows="6" :placeholder="t('مثال: ماكينة CNC للخشب بطاولة 1300×2500 مم لورشة نجارة في الصناعية، أو: جهاز تعقيم لعيادة أسنان. اذكر الكمية والمكان إن أمكن.', 'Example: a wood CNC router with a 1300×2500 mm table for a carpentry workshop, or: a steriliser for a dental clinic. Mention quantity and location if you can.')" class="mt-1 w-full rounded-lg border border-line dark:border-gray-600 bg-white dark:bg-gray-900 px-4 py-3"></textarea>
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
import { SOURCING_SECTORS } from '~/utils/sourcing'

const { locale } = useI18n()
const localePath = useLocalePath()
const isAr = computed(() => locale.value === 'ar')
const t = (ar, en) => (isAr.value ? ar : en)

const waLink = computed(() => whatsappLink(t('مرحباً بيستوليكس، أحتاج توريد: ', 'Hello Bestolex, I need to source: ')))
const trackWa = () => trackLead({ formName: 'sourcing_whatsapp', requestType: 'sourcing' })

const heroExamples = [
  { icon: 'construction', ar: 'سقالات وخلاطات خرسانة لمشروع بناء', en: 'Scaffolding and concrete mixers for a building project' },
  { icon: 'parts', ar: 'قطع غيار لآلة توقّف وكيلها', en: 'Spare parts for a machine whose agent has closed' },
  { icon: 'gauge', ar: 'مضخات غاطسة وضاغط هواء صناعي', en: 'Submersible pumps and an industrial air compressor' },
  { icon: 'metal', ar: 'ماكينة لحام ومخرطة لورشة حدادة', en: 'A welding machine and lathe for a metal workshop' },
  { icon: 'kitchen', ar: 'مكائن قهوة وعصير لمقهى جديد', en: 'Coffee and juice machines for a new café' },
  { icon: 'medical', ar: 'جهاز تعقيم لعيادة أسنان', en: 'A steriliser for a dental clinic' }
]

const chips = [
  { a: 'أي نشاط، أي آلة', ae: 'Any activity, any machine', b: 'بناء، صناعة، ورش، ضيافة، طب، زراعة', be: 'construction, industry, workshops, hospitality, medical, farming' },
  { a: 'من مصانع حول العالم', ae: 'From factories worldwide', b: 'أو من مصنع تحدده أنت', be: 'or from a factory you name' },
  { a: 'من الطلب إلى التشغيل', ae: 'From request to start-up', b: 'شحن وتخليص وتركيب وتدريب وصيانة', be: 'shipping, clearance, installation, training, maintenance' }
]

const facts = [
  { lar: 'الخدمة', len: 'Service', ar: 'شراء وتوريد للغير', en: 'Procurement on your behalf' },
  { lar: 'الكمية', len: 'Quantity', ar: 'قطعة واحدة إلى مصنع كامل', en: 'One unit to a complete plant' },
  { lar: 'المصدر', len: 'Source', ar: 'مصانع حول العالم، أو مصنع تحدده', en: 'Factories worldwide, or one you name' },
  { lar: 'التسليم', len: 'Delivery', ar: 'في موقعك بقطر، مركّباً وجاهزاً', en: 'On your site in Qatar, installed and ready' },
  { lar: 'السعر', len: 'Price', ar: 'بعرض سعر بعد تحديد المواصفة', en: 'Quoted once the specification is set' },
  { lar: 'البداية', len: 'To start', ar: 'النموذج أو واتساب 51505014', en: 'The form or WhatsApp 51505014' }
]

const ownSections = [
  { id: 'docking-systems', ar: 'أنظمة التحميل', en: 'Loading systems' },
  { id: 'waste-management', ar: 'النفايات وإعادة التدوير', en: 'Waste and recycling' },
  { id: 'perimeter-protection', ar: 'الحماية المحيطية', en: 'Perimeter protection' },
  { id: 'industrial-doors', ar: 'الأبواب الصناعية', en: 'Industrial doors' },
  { id: 'energy-solutions', ar: 'حلول الطاقة', en: 'Energy solutions' }
]

const kinds = [
  { id: 'single', ar: 'آلة أو جهاز واحد', en: 'A single machine or device', dar: 'ماكينة لحام، ضاغط هواء، مضخة، جهاز تعقيم، ماكينة CNC… وحدة واحدة بمواصفة محددة، أو عدة وحدات من الموديل نفسه.', den: 'A welding machine, air compressor, steriliser, CNC machine… one unit to a set specification, or several of the same model.' },
  { id: 'line', ar: 'خط إنتاج متكامل', en: 'A complete production line', dar: 'عدة آلات تعمل معاً: تعبئة وتغليف، تصنيع أغذية، حقن بلاستيك، بلوك وخرسانة. نوفّرها متوافقة مع بعضها لا كقطع متفرقة.', den: 'Several machines working together: filling and packing, food processing, plastic injection, blocks and concrete. Supplied to work together, not as separate pieces.' },
  { id: 'setup', ar: 'تجهيز منشأة من الصفر', en: 'Equipping a facility from scratch', dar: 'مصنع أو ورشة أو مطبخ مركزي أو مختبر أو عيادة: قائمة المعدات كاملة، والمخطط، والتركيب، وتدريب الفريق.', den: 'A factory, workshop, central kitchen, lab or clinic: the full equipment list, layout, installation and team training.' },
  { id: 'tender', ar: 'معدات لمناقصة أو مشروع', en: 'Equipment for a tender or project', dar: 'وفق كراسة الشروط ومواصفة الاستشاري، مع العرض الفني والتجاري ووثائق المطابقة.', den: 'To the tender documents and consultant specification, with the technical and commercial offer and compliance documents.' },
  { id: 'parts', ar: 'قطع غيار ومستهلكات', en: 'Spare parts and consumables', dar: 'قطع تآكل وفلاتر وسيور ومحامل ومحركات لآلات قائمة عندك، حتى لو لم تشترها منا.', den: "Wear parts, filters, belts, bearings and motors for machines you already run, even if you didn't buy them from us." }
]
const kindOptions = [...kinds, { id: 'other', ar: 'غير ذلك', en: 'Something else' }]
const sectorOptions = [{ id: '', ar: 'اختر نشاطك', en: 'Choose your activity' }, ...SOURCING_SECTORS.map(s => ({ id: s.id, ar: s.ar, en: s.en })), { id: 'government', ar: 'جهة حكومية أو شبه حكومية', en: 'Government or semi-government entity' }, { id: 'other', ar: 'نشاط آخر', en: 'Another activity' }]

const stages = [
  { ar: 'دراسة المتطلبات والمعاينة الميدانية', en: 'Requirements study and site survey', dar: 'نفهم العمل الذي تريد إنجازه، ونعاين الموقع عند اللزوم، ونكتب المواصفة الفنية معك.', den: 'We understand the job, survey the site when needed, and write the technical specification with you.' },
  { ar: 'اختيار الحل والعرض الفني والتجاري', en: 'Solution selection and technical and commercial proposal', dar: 'نطلب عروضاً من أكثر من مصنع، ونرسل لك مقارنة واضحة بالمواصفات والضمان والمدة والسعر، مع توصيتنا.', den: 'We request offers from more than one factory and send you a clear comparison of specifications, warranty, lead time and price, with our recommendation.' },
  { ar: 'التوريد والخدمات اللوجستية', en: 'Supply and logistics', dar: 'نتولى الشراء من المصنع، ونتابع التصنيع والفحص قبل الشحن، ثم الشحن والتخليص الجمركي حتى موقعك.', den: 'We handle the purchase from the factory, follow manufacturing and pre-shipment inspection, then shipping and customs clearance to your site.' },
  { ar: 'التركيب أو الإشراف الفني', en: 'Installation or technical supervision', dar: 'نركّب الآلة في موقعك، أو نشرف على تركيبها وتوصيلها مع فني المصنع.', den: "We install the machine on your site, or supervise its installation and connection with the factory's technician." },
  { ar: 'الاختبار والتشغيل والتسليم', en: 'Testing, commissioning and handover', dar: 'تشغيل تجريبي يثبت أن الآلة تؤدي ما طلبته، ثم التسليم جاهزة للعمل.', den: 'A trial run that shows the machine does what you asked, then handover ready to work.' },
  { ar: 'تدريب المشغلين', en: 'Operator training', dar: 'ندرّب فريقك على التشغيل والسلامة والصيانة اليومية.', den: 'We train your team on operation, safety and daily maintenance.' },
  { ar: 'الصيانة الوقائية والتصحيحية', en: 'Preventive and corrective maintenance', dar: 'برنامج صيانة دوري واستجابة للأعطال، حتى لا تتوقف الآلة في وقت حرج.', den: 'Scheduled maintenance and fault response, so the machine does not stop at a critical time.' },
  { ar: 'قطع الغيار وخدمة ما بعد البيع', en: 'Spare parts and after-sales service', dar: 'نوفّر قطع الغيار من المصنع أو بديلها المتوافق، ونتابع الآلة بعد التسليم.', den: 'We supply spare parts from the factory or a compatible equivalent, and support the machine after handover.' }
]

const compare = [
  { ar: 'إيجاد المصنع', en: 'Finding the factory', selfAr: 'تبحث وتراسل مصانع لا تعرفها، وكثير منها وسطاء.', selfEn: "You search and write to factories you don't know, many of them middlemen.", bxAr: 'نطلب العروض من أكثر من مصنع ونقارنها لك.', bxEn: 'We request offers from more than one factory and compare them for you.' },
  { ar: 'التحقق من الجودة', en: 'Checking quality', selfAr: 'تعتمد على كلام البائع وصور الكتالوج.', selfEn: "You rely on the seller's word and catalogue photos.", bxAr: 'نراجع المواصفة والشهادات، ونطلب فحصاً قبل الشحن.', bxEn: 'We review the specification and certificates, and ask for a pre-shipment inspection.' },
  { ar: 'التفاوض والتعاقد', en: 'Negotiating and contracting', selfAr: 'بلغة أخرى، ومع جهة خارج قطر.', selfEn: 'In another language, with a party outside Qatar.', bxAr: 'تتعامل مع شركة قطرية واحدة في الدوحة.', bxEn: 'You deal with one Qatari company in Doha.' },
  { ar: 'الشحن والتخليص', en: 'Shipping and clearance', selfAr: 'تنسّق بنفسك مع شركة شحن ومخلّص جمركي.', selfEn: 'You coordinate a forwarder and a customs broker yourself.', bxAr: 'نتولاهما حتى وصول الآلة إلى موقعك.', bxEn: 'We handle both until the machine reaches your site.' },
  { ar: 'التركيب والتشغيل', en: 'Installation and start-up', selfAr: 'تبحث عن فني يعرف الآلة.', selfEn: 'You look for a technician who knows the machine.', bxAr: 'نركّب أو نشرف، ونشغّل وندرّب فريقك.', bxEn: 'We install or supervise, commission and train your team.' },
  { ar: 'الضمان وقطع الغيار', en: 'Warranty and spare parts', selfAr: 'تطارد المصنع في بلد آخر.', selfEn: 'You chase the factory in another country.', bxAr: 'جهة واحدة في الدوحة تتابع الضمان وتوفّر القطع.', bxEn: 'One company in Doha follows the warranty and supplies the parts.' }
]

const needs = [
  { ar: 'نشاطك، وما الذي ستنتجه أو تعالجه أو تقدّمه بالآلة، وبأي كمية في الساعة أو في اليوم.', en: 'Your activity, what the machine will produce, process or serve, and how much per hour or per day.' },
  { ar: 'مكان التركيب، والمساحة المتاحة، والكهرباء المتوفرة (الجهد والتردد).', en: 'Where it will be installed, the space available and the power supply (voltage and frequency).' },
  { ar: 'أقصى موعد تحتاج فيه تشغيل الآلة.', en: 'The latest date you need the machine running.' },
  { ar: 'أي مواصفة ملزمة من استشاري أو كراسة شروط، كما هي.', en: 'Any binding specification from a consultant or tender documents, as they are.' },
  { ar: 'صور الآلة الحالية ولوحة بياناتها، إن كنت تستبدلها أو تطلب لها قطع غيار.', en: 'Photos of the current machine and its nameplate, if you are replacing it or need parts for it.' }
]

const faq = [
  { q: { ar: 'ما هي خدمة التوريد حسب الطلب؟', en: 'What is the sourcing on request service?' }, a: { ar: 'خدمة شراء وتوريد للغير من بيستوليكس في الدوحة: نشتري لك أي آلة أو معدة أو جهاز أو قطع غيار لا تجدها في السوق المحلي، من مصانع حول العالم، ونتولى الفحص والشحن والتخليص الجمركي والتركيب والتدريب والصيانة في قطر.', en: "A procurement service from Bestolex in Doha: we buy, on your behalf, any machine, equipment, device or spare part you can't find locally, from factories around the world, and handle inspection, shipping, customs clearance, installation, training and maintenance in Qatar." } },
  { q: { ar: 'ما الفرق بينها وبين منتجات بيستوليكس؟', en: "How is it different from Bestolex's own products?" }, a: { ar: 'منتجاتنا في الأقسام الخمسة (أنظمة التحميل، والنفايات وإعادة التدوير، والحماية المحيطية، والأبواب الصناعية، وحلول الطاقة) نوردها بصفتنا وكلاء وموزّعين. والتوريد حسب الطلب لكل ما عدا ذلك، في أي نشاط.', en: 'Our products in the five sections (loading systems, waste and recycling, perimeter protection, industrial doors and energy solutions) we supply as agents and distributors. Sourcing on request covers everything else, for any activity.' } },
  { q: { ar: 'هل تورّدون السقالات وخلاطات الخرسانة ومعدات المقاولين؟', en: 'Do you supply scaffolding, concrete mixers and contractor equipment?' }, a: { ar: 'نعم: السقالات، وخلاطات الخرسانة وهزازاتها، ومحطات الخلط، ومكائن البلوك، وروافع المواد، ومعدات الطرق، والمعدات الثقيلة عند الطلب.', en: 'Yes: scaffolding, concrete mixers and vibrators, batching plants, block making machines, material hoists, road equipment, and heavy equipment on request.' } },
  { q: { ar: 'هل توفّرون قطع غيار لآلات لم نشترها منكم؟', en: "Do you supply parts for machines we didn't buy from you?" }, a: { ar: 'نعم. أرسل لوحة بيانات الآلة ورقم الموديل وصورة القطعة، ونبحث عن القطعة الأصلية أو البديل المتوافق.', en: 'Yes. Send the nameplate, model number and a photo of the part, and we find the original part or a compatible alternative.' } },
  { q: { ar: 'هل تورّدون معدات طبية للمستشفيات والعيادات؟', en: 'Do you supply medical equipment to hospitals and clinics?' }, a: { ar: 'نعم: أجهزة ومعدات طبية، وأسرّة، وأجهزة تعقيم، ومعدات عيادات الأسنان والعلاج الطبيعي، وأثاث طبي. ونتحقق قبل الشراء من متطلبات استيراد كل جهاز لدى وزارة الصحة العامة. الأدوية خارج نطاق الخدمة.', en: 'Yes: medical devices and equipment, beds, sterilisers, dental and physiotherapy equipment, and medical furniture. Before buying, we check each device\'s import requirements with the Ministry of Public Health. Medicines are outside the scope.' } },
  { q: { ar: 'هل تورّدون خطوط إنتاج كاملة لمصنع جديد؟', en: 'Do you supply complete production lines for a new factory?' }, a: { ar: 'نعم. نحدد معك الطاقة الإنتاجية والمساحة والكهرباء، ونورّد آلات الخط متوافقة مع بعضها، ثم نركّبها ونشغّلها وندرّب الفريق.', en: 'Yes. We agree the capacity, space and power with you, supply the line\'s machines to work together, then install, commission and train the team.' } },
  { q: { ar: 'هل تورّدون مكائن للورش: الحدادة واللحام والنجارة والخياطة؟', en: 'Do you supply machines for workshops: metalwork, welding, carpentry and tailoring?' }, a: { ar: 'نعم، آلة واحدة أو تجهيز الورشة كاملة: مكائن لحام ومخارط ومكابس ثني ومقصات وقطع بالليزر والبلازما، ومناشير ومكائن CNC للخشب، ومكائن خياطة وتطريز صناعية، وضواغط هواء.', en: 'Yes, a single machine or a full workshop: welding machines, lathes, press brakes, shears, laser and plasma cutting, saws and CNC routers for wood, industrial sewing and embroidery machines, and air compressors.' } },
  { q: { ar: 'هل تورّدون قطعة واحدة، أم كميات فقط؟', en: 'Do you supply single units, or only quantities?' }, a: { ar: 'قطعة واحدة أو كمية. لا حد أدنى للطلب.', en: 'Either. There is no minimum order.' } },
  { q: { ar: 'هل نستطيع تحديد المصنع أو العلامة التجارية؟', en: 'Can we name the factory or brand?' }, a: { ar: 'نعم. إن كان لديك مصنع مفضل أو مواصفة ملزمة، نشتري وفقها ونتولى الباقي.', en: 'Yes. If you have a preferred factory or a binding specification, we buy accordingly and handle the rest.' } },
  { q: { ar: 'هل تورّدون لمناقصات ومشاريع الجهات الحكومية؟', en: 'Do you supply for government tenders and projects?' }, a: { ar: 'أرسل كراسة الشروط ومواصفة الاستشاري، ونجهّز عرض المعدات الفني والتجاري المطابق لها مع وثائق المطابقة.', en: 'Send the tender documents and consultant specification, and we prepare a matching technical and commercial equipment offer with compliance documents.' } },
  { q: { ar: 'كم يستغرق التوريد؟', en: 'How long does supply take?' }, a: { ar: 'يعتمد على الآلة وجاهزيتها في المصنع. نحدد المدة في العرض بعد تأكيدها من المصنع، ولا نعد بمدة قبل ذلك.', en: "It depends on the machine and its availability at the factory. We state the lead time in the offer once the factory confirms it, and don't promise one before that." } },
  { q: { ar: 'كم تكلفة الخدمة؟', en: 'What does the service cost?' }, a: { ar: 'يصلك عرض سعر بعد تحديد المواصفة. لا ننشر أسعاراً ثابتة لأن كل طلب مختلف.', en: 'You receive a quote once the specification is set. We do not publish fixed prices because every request is different.' } },
  { q: { ar: 'هل الخدمة داخل قطر فقط؟', en: 'Is the service only in Qatar?' }, a: { ar: 'السوق الأساسي قطر، بالتركيب والتدريب والصيانة. ونورّد معدات التعدين والطاقة إلى الشرق الأوسط وأفريقيا، فنحن موزّعون معتمدون للعديد من المصانع والشركات العالمية.', en: 'Our main market is Qatar, with installation, training and maintenance. We also supply mining and energy equipment to the Middle East and Africa, as authorised distributors for many international manufacturers and companies.' } }
]

// Form: goes to /api/contact like the other forms, stored and mailed as a request
const emptyForm = () => ({ name: '', company: '', phone: '', email: '', sector: '', kind: 'single', neededBy: '', message: '' })
const form = ref(emptyForm())
const loading = ref(false)
const status = ref('')
const statusOk = ref(false)

const submit = async () => {
  loading.value = true
  status.value = ''
  const kind = kindOptions.find(k => k.id === form.value.kind) || kindOptions[0]
  const sector = (form.value.sector && sectorOptions.find(s => s.id === form.value.sector)) || { ar: 'غير محدد', en: 'Not specified' }
  const lines = [
    form.value.message,
    '',
    `النشاط: ${sector.ar}`,
    `حجم الطلب: ${kind.ar}`,
    form.value.neededBy ? `الموعد المطلوب للتشغيل: ${form.value.neededBy}` : ''
  ].filter(Boolean)
  try {
    await $fetch('/api/contact', {
      method: 'POST',
      body: {
        name: form.value.name,
        company: form.value.company,
        phone: form.value.phone,
        email: form.value.email,
        requestType: 'sourcing',
        productName: `توريد حسب الطلب: ${sector.ar}`,
        categoryTitle: kind.ar,
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

const pageTitle = computed(() => t('توريد المعدات والآلات حسب الطلب في قطر لأي نشاط | بيستوليكس', 'Equipment Suppliers in Qatar for Any Industry | Bestolex'))
const pageDesc = computed(() => t(
  'نورّد أي آلة غير متوفرة محلياً لأي نشاط: سقالات ومعدات بناء، قطع غيار، مضخات وضواغط، مكائن لحام، معدات مطابخ وطبية، من مصانع حول العالم إلى قطر.',
  "Any machine you can't find locally, for any industry: scaffolding, spare parts, pumps, compressors, welding, kitchen and medical equipment, in Qatar."
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
      key: 'ld-sourcing',
      innerHTML: JSON.stringify({
        '@context': 'https://schema.org',
        '@graph': [
          {
            '@type': 'Service',
            '@id': `${SITE_URL}/sourcing#service`,
            name: t('التوريد حسب الطلب', 'Sourcing on request'),
            alternateName: isAr.value ? ['شراء وتوريد للغير', 'توريد المعدات والآلات'] : ['Equipment procurement', 'Machinery sourcing'],
            serviceType: t('توريد وشراء المعدات والآلات للغير', 'Equipment and machinery sourcing and procurement'),
            description: pageDesc.value,
            url: `${SITE_URL}${localePath('/sourcing')}`,
            provider: { '@id': ORG_ID },
            areaServed: [{ '@type': 'Country', name: 'Qatar' }, { '@type': 'Place', name: 'Middle East' }, { '@type': 'Place', name: 'Africa' }],
            audience: { '@type': 'BusinessAudience', audienceType: t('المقاولون والمصانع والورش والمطاعم والمقاهي والفنادق والمستشفيات والمزارع والمختبرات والجهات الحكومية', 'Contractors, factories, workshops, restaurants, cafés and hotels, hospitals, farms, laboratories and government entities') },
            hasOfferCatalog: {
              '@type': 'OfferCatalog',
              name: t('القطاعات التي نورّد لها', 'Sectors we supply'),
              itemListElement: SOURCING_SECTORS.map(s => ({
                '@type': 'OfferCatalog',
                name: t(s.ar, s.en),
                itemListElement: (isAr.value ? s.itemsAr : s.itemsEn).map(it => ({ '@type': 'Offer', itemOffered: { '@type': 'Product', name: it } }))
              }))
            }
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
