<template>
  <div class="privacy-page bg-gray-50 dark:bg-gray-950 min-h-screen transition-colors duration-300 py-16 md:py-24">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8 max-w-5xl">
      
      <!-- Main Content Card -->
      <article class="bg-white dark:bg-gray-900 rounded-3xl p-6 sm:p-10 md:p-14 shadow-xl border border-gray-100 dark:border-gray-800 transition-colors">
        
        <!-- Header -->
        <header class="text-center border-b border-gray-200 dark:border-gray-800 pb-10 mb-12">
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-amber-500/10 text-amber-600 dark:text-amber-400 text-xs sm:text-sm font-semibold mb-4">
            <span class="w-2 h-2 rounded-full bg-amber-500 animate-pulse"></span>
            {{ locale === 'ar' ? 'آخر تحديث: 16 سبتمبر 2026' : 'Last Updated: 16 September 2026' }}
          </div>
          <h1 class="text-3xl sm:text-4xl md:text-5xl font-black text-gray-900 dark:text-white tracking-tight mb-4">
            {{ locale === 'ar' ? 'سياسة الخصوصية' : 'Privacy Policy' }}
          </h1>
          <p class="text-lg sm:text-xl font-bold text-gray-700 dark:text-gray-300">
            {{ locale === 'ar' ? 'بيستوليكس لتجارة الآلات والمعدات الثقيلة (ذ.م.م)' : 'Bestolex Trading of Heavy Equipment and Machinery W.L.L' }}
          </p>
        </header>

        <!-- ARABIC CONTENT -->
        <div v-if="locale === 'ar'" class="space-y-12 text-gray-700 dark:text-gray-300 leading-relaxed text-base sm:text-lg">
          
          <!-- 1. مقدمة -->
          <section id="ar-intro" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              1. مقدمة
            </h2>
            <p>
              تحترم شركة بيستوليكس لتجارة الآلات والمعدات الثقيلة (ذ.م.م)، المشار إليها في هذه السياسة بـ"الشركة" أو "نحن"، خصوصية زوار موقعها الإلكتروني وعملائها والمتعاملين معها. وتلتزم بالتعامل مع بياناتهم الشخصية وحمايتها وفقاً لأحكام القانون رقم (13) لسنة 2016 بشأن حماية خصوصية البيانات الشخصية في دولة قطر، والتشريعات واللوائح ذات الصلة.
            </p>
            <p>
              توضح هذه السياسة البيانات الشخصية التي نجمعها، وكيفية جمعها، والأغراض التي نستخدمها من أجلها، والجهات التي نشاركها معها، وكيفية حمايتها والاحتفاظ بها، والحقوق المتاحة لك فيما يتعلق بها.
            </p>
            <p>
              تُطبَّق هذه السياسة على الموقع الإلكتروني 
              <a href="https://www.bestolex.com" target="_blank" rel="noopener noreferrer" class="text-amber-600 dark:text-amber-400 font-semibold hover:underline">www.bestolex.com</a>، 
              وعلى تواصلك معنا عبر البريد الإلكتروني والهاتف وواتساب ونماذج التواصل وقنواتنا التجارية الأخرى. ويخضع استخدام الموقع كذلك لـ<NuxtLink :to="localePath('/terms')" class="text-amber-600 dark:text-amber-400 font-semibold hover:underline">شروط الاستخدام</NuxtLink>.
            </p>
            <p class="font-medium text-gray-900 dark:text-gray-100">
              وتُعد الشركة الجهة المسؤولة عن مراقبة ومعالجة البيانات الشخصية المشمولة بهذه السياسة.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 2. البيانات التي نجمعها -->
          <section id="ar-data" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              2. البيانات التي نجمعها
            </h2>
            <p>
              بحسب طبيعة تفاعلك معنا، نجمع الفئات التالية من البيانات:
            </p>
            <ul class="list-disc list-inside space-y-3 ps-2 sm:ps-4">
              <li>
                <strong class="text-gray-900 dark:text-white">بيانات الهوية والاتصال:</strong> 
                الاسم، والمسمى الوظيفي، واسم الشركة أو الجهة التي تمثلها، والبريد الإلكتروني، وأرقام الهاتف، وعنوان المنشأة أو موقع المشروع عند الحاجة.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">بيانات الطلبات والمراسلات:</strong> 
                تفاصيل الاستفسارات وطلبات عروض الأسعار، والمتطلبات الفنية والتجارية للمشروع، ومواعيد المعاينات والزيارات، والصور والمستندات التي ترسلها لنا، وسجلات المراسلات المتعلقة بطلبك.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">بيانات التعاقد والفوترة:</strong> 
                أوامر الشراء والعقود والفواتير، وبيانات التوريد والضمان والصيانة وقطع الغيار، والمعلومات المتعلقة بتنفيذ الالتزامات التجارية والتعاقدية.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">بيانات التدريب:</strong> 
                عند التسجيل في البرامج التدريبية، تشمل بيانات المتدرب وجهة عمله، ومعلومات التسجيل، وسجلات الحضور، وبيانات الشهادات.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">البيانات التقنية وبيانات استخدام الموقع:</strong> 
                عنوان بروتوكول الإنترنت (IP)، ونوع الجهاز والمتصفح ونظام التشغيل، والصفحات التي تمت زيارتها، ومدة الزيارة ومصدرها، وبيانات التفاعل مع الموقع.
              </li>
            </ul>
            <div class="p-4 rounded-2xl bg-gray-100 dark:bg-gray-800/60 border border-gray-200 dark:border-gray-700/60 text-sm sm:text-base">
              تُجمع البيانات التقنية غير الضرورية وفقاً لاختياراتك في إعدادات ملفات تعريف الارتباط والموافقة.
            </div>
            <p class="text-sm sm:text-base text-gray-600 dark:text-gray-400 italic">
              لا نطلب ولا نجمع عمداً بيانات شخصية ذات طبيعة خاصة، مثل البيانات الصحية أو الدينية، ونرجو عدم إرسالها إلينا ما لم تكن ضرورية ومطلوبة بصورة مشروعة لغرض محدد.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 3. كيف نجمع البيانات -->
          <section id="ar-collection" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              3. كيف نجمع البيانات
            </h2>
            <p>نجمع بياناتك بالطرق التالية:</p>
            <ul class="list-disc list-inside space-y-3 ps-2 sm:ps-4">
              <li>
                <strong class="text-gray-900 dark:text-white">مباشرةً منك:</strong> 
                عند تعبئة نماذج التواصل، أو طلب عرض سعر، أو حجز موعد أو معاينة، أو التسجيل في برنامج تدريبي، أو مراسلتنا عبر البريد الإلكتروني أو الهاتف أو واتساب.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">خلال التعامل التجاري أو التعاقدي معنا.</strong>
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">تلقائياً عند استخدام الموقع:</strong> 
                من خلال ملفات تعريف الارتباط الضرورية، ومن خلال أدوات التحليل والتسويق غير الضرورية بعد الحصول على موافقتك.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">من أطراف أخرى:</strong> 
                من جهة عملك أو ممثليها عند مشاركتك في مشروع أو معاملة معنا، أو من الموردين أو المصنعين أو الشركاء عندما يكون ذلك ضرورياً لتنفيذ طلب أو خدمة مرتبطة بك.
              </li>
            </ul>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 4. أغراض استخدام البيانات ومبرر المعالجة -->
          <section id="ar-purposes" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              4. أغراض استخدام البيانات ومبرر المعالجة
            </h2>
            
            <div class="overflow-x-auto rounded-2xl border border-gray-200 dark:border-gray-700 shadow-sm mt-4">
              <table class="w-full text-right border-collapse">
                <thead>
                  <tr class="bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-white border-b border-gray-200 dark:border-gray-700">
                    <th class="p-4 sm:p-5 font-bold text-base sm:text-lg w-1/2">الغرض</th>
                    <th class="p-4 sm:p-5 font-bold text-base sm:text-lg w-1/2">مبرر المعالجة</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-gray-200 dark:divide-gray-800 text-sm sm:text-base">
                  <tr class="hover:bg-gray-50/50 dark:hover:bg-gray-800/40 transition">
                    <td class="p-4 sm:p-5 align-top">الرد على الاستفسارات وإعداد عروض الأسعار والمقترحات الفنية والتجارية</td>
                    <td class="p-4 sm:p-5 align-top text-gray-600 dark:text-gray-400">غرض مشروع مرتبط بالرد على طلبك واتخاذ الإجراءات اللازمة بشأنه</td>
                  </tr>
                  <tr class="hover:bg-gray-50/50 dark:hover:bg-gray-800/40 transition">
                    <td class="p-4 sm:p-5 align-top">تنفيذ العقود وعمليات التوريد والتركيب والتشغيل والتدريب والضمان والصيانة وقطع الغيار</td>
                    <td class="p-4 sm:p-5 align-top text-gray-600 dark:text-gray-400">غرض مشروع وضروري لتنفيذ العلاقة التعاقدية</td>
                  </tr>
                  <tr class="hover:bg-gray-50/50 dark:hover:bg-gray-800/40 transition">
                    <td class="p-4 sm:p-5 align-top">إصدار الفواتير وحفظ السجلات والوفاء بالمتطلبات التجارية والضريبية والتنظيمية</td>
                    <td class="p-4 sm:p-5 align-top text-gray-600 dark:text-gray-400">الوفاء بالالتزامات القانونية والتنظيمية</td>
                  </tr>
                  <tr class="hover:bg-gray-50/50 dark:hover:bg-gray-800/40 transition">
                    <td class="p-4 sm:p-5 align-top">تشغيل الموقع وحمايته من الاستخدام غير المشروع والمخاطر الأمنية</td>
                    <td class="p-4 sm:p-5 align-top text-gray-600 dark:text-gray-400">غرض مشروع يتعلق بأمن الموقع وتشغيله</td>
                  </tr>
                  <tr class="hover:bg-gray-50/50 dark:hover:bg-gray-800/40 transition">
                    <td class="p-4 sm:p-5 align-top">تحليل أداء الموقع وتحسين المحتوى وتجربة المستخدم</td>
                    <td class="p-4 sm:p-5 align-top text-gray-600 dark:text-gray-400">موافقتك على ملفات الارتباط والتقنيات غير الضرورية</td>
                  </tr>
                  <tr class="hover:bg-gray-50/50 dark:hover:bg-gray-800/40 transition">
                    <td class="p-4 sm:p-5 align-top">إرسال العروض والأخبار والاتصالات التسويقية</td>
                    <td class="p-4 sm:p-5 align-top text-gray-600 dark:text-gray-400">موافقتك المسبقة</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <p class="pt-2">
              لن نستخدم بياناتك لغرض يختلف جوهرياً عن الأغراض التي جُمعت من أجلها دون إبلاغك واتخاذ الإجراءات المطلوبة، بما في ذلك الحصول على موافقتك عندما يكون ذلك لازماً.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 5. التسويق المباشر -->
          <section id="ar-marketing" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              5. التسويق المباشر
            </h2>
            <p>
              لا نرسل اتصالات تسويقية إلكترونية عبر البريد الإلكتروني أو الرسائل النصية أو واتساب إلا بعد الحصول على موافقتك المسبقة، ووفقاً للمتطلبات القانونية.
            </p>
            <p>
              تتضمن كل رسالة تسويقية وسيلة واضحة لإلغاء الاشتراك. ويمكنك إلغاء الاشتراك أو سحب موافقتك في أي وقت عبر وسيلة الإلغاء الواردة في الرسالة، أو بالرد عليها بطلب الإلغاء، أو بمراسلتنا على 
              <a href="mailto:info@bestolex.com" class="text-amber-600 dark:text-amber-400 font-semibold hover:underline">info@bestolex.com</a>.
            </p>
            <p class="text-sm sm:text-base text-gray-600 dark:text-gray-400">
              لا يؤثر إلغاء الاشتراك على المراسلات الضرورية المتعلقة بطلبات قائمة أو عروض أسعار أو عقود أو خدمات أو التزامات قانونية.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 6. مشاركة البيانات -->
          <section id="ar-sharing" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              6. مشاركة البيانات
            </h2>
            <div class="p-4 rounded-2xl bg-amber-500/10 border border-amber-500/20 text-gray-900 dark:text-white font-bold text-lg">
              لا تبيع بيستوليكس بياناتك الشخصية ولا تؤجرها.
            </div>
            <p>
              نشارك بياناتك بالقدر اللازم فقط لتحقيق الغرض المشروع، مع الجهات التالية:
            </p>
            <ul class="list-disc list-inside space-y-3 ps-2 sm:ps-4">
              <li>
                <strong class="text-gray-900 dark:text-white">المصنعون والموردون المعتمدون:</strong> 
                ومنهم شركة أساس السعودية لأعمال التقنية المحدودة (SAB TECH) في المملكة العربية السعودية، وذلك لتحديد المواصفات الفنية، أو إعداد العروض، أو التوريد، أو الدعم الفني، أو الضمان والصيانة وقطع الغيار.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">الشركاء الفنيون والمقاولون الفرعيون:</strong> 
                عندما تكون مشاركتهم ضرورية للمعاينة أو التركيب أو التشغيل أو الصيانة أو الخدمات الفنية ذات الصلة.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">مقدمو الخدمات التقنية:</strong> 
                مثل استضافة الموقع، والبريد الإلكتروني، والبنية التحتية الرقمية، وخدمات التحليل من Google، وخدمات المراسلة مثل واتساب.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">شركات الشحن والتخليص والخدمات اللوجستية:</strong> 
                عندما يكون ذلك ضرورياً لتوريد المعدات أو تنفيذ الطلب.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">الجهات الحكومية والتنظيمية والقضائية:</strong> 
                عندما يكون الإفصاح مطلوباً بموجب القانون أو بقرار من جهة مختصة، أو ضرورياً لحماية الحقوق القانونية للشركة.
              </li>
            </ul>
            <p>
              عندما يعالج مقدم خدمة البيانات الشخصية نيابةً عنا، نتخذ التدابير المناسبة، ومنها الالتزامات التعاقدية حيثما ينطبق ذلك، لضمان سرية البيانات وحمايتها واستخدامها للأغراض المحددة فقط.
            </p>
            <p class="text-sm sm:text-base text-gray-600 dark:text-gray-400">
              وقد تعالج بعض الجهات، مثل Google وواتساب، البيانات بصفتها جهات مستقلة وفق سياسات الخصوصية والالتزامات القانونية الخاصة بها.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 7. نقل البيانات خارج دولة قطر -->
          <section id="ar-transfers" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              7. نقل البيانات خارج دولة قطر
            </h2>
            <p>
              تُنقل بعض البيانات الشخصية أو تُعالَج أو تُخزَّن خارج دولة قطر، وذلك عند التعامل مع:
            </p>
            <ul class="list-disc list-inside space-y-2 ps-2 sm:ps-4">
              <li>الموردين والمصنعين في المملكة العربية السعودية، ومنهم SAB TECH، أو في دول أخرى.</li>
              <li>مقدمي الخدمات التقنية الدوليين، ومنها خدمات الاستضافة والحوسبة السحابية وخدمات Google ومنصات المراسلة.</li>
            </ul>
            <p>
              عند نقل البيانات أو معالجتها خارج دولة قطر، نتخذ الإجراءات المعقولة والمناسبة لضمان أن تتم المعالجة بما يتوافق مع المتطلبات القانونية المطبقة، وألا يُخل النقل بحقوق أصحاب البيانات أو بمستوى الحماية المقرر لهم.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 8. مدة الاحتفاظ بالبيانات -->
          <section id="ar-retention" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              8. مدة الاحتفاظ بالبيانات
            </h2>
            <p>
              نحتفظ بالبيانات الشخصية فقط للمدة اللازمة لتحقيق الغرض الذي جُمعت من أجله، أو للوفاء بالمتطلبات القانونية أو التعاقدية أو المحاسبية أو التنظيمية:
            </p>

            <div class="overflow-x-auto rounded-2xl border border-gray-200 dark:border-gray-700 shadow-sm mt-4">
              <table class="w-full text-right border-collapse">
                <thead>
                  <tr class="bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-white border-b border-gray-200 dark:border-gray-700">
                    <th class="p-4 sm:p-5 font-bold text-base sm:text-lg w-1/2">نوع البيانات</th>
                    <th class="p-4 sm:p-5 font-bold text-base sm:text-lg w-1/2">مدة الاحتفاظ</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-gray-200 dark:divide-gray-800 text-sm sm:text-base">
                  <tr class="hover:bg-gray-50/50 dark:hover:bg-gray-800/40 transition">
                    <td class="p-4 sm:p-5 align-top">الاستفسارات وعروض الأسعار التي لم تتحول إلى تعاقد</td>
                    <td class="p-4 sm:p-5 align-top text-gray-600 dark:text-gray-400">حتى سنتين من تاريخ آخر تواصل، ما لم يوجد سبب مشروع يستدعي مدة أطول</td>
                  </tr>
                  <tr class="hover:bg-gray-50/50 dark:hover:bg-gray-800/40 transition">
                    <td class="p-4 sm:p-5 align-top">بيانات العقود والفواتير والضمان والمعاملات التجارية</td>
                    <td class="p-4 sm:p-5 align-top text-gray-600 dark:text-gray-400">طوال مدة العلاقة التعاقدية، ثم للمدة التي تفرضها القوانين التجارية والضريبية والمحاسبية والتنظيمية في دولة قطر</td>
                  </tr>
                  <tr class="hover:bg-gray-50/50 dark:hover:bg-gray-800/40 transition">
                    <td class="p-4 sm:p-5 align-top">بيانات التدريب وسجلات الحضور والشهادات</td>
                    <td class="p-4 sm:p-5 align-top text-gray-600 dark:text-gray-400">حتى خمس سنوات من تاريخ انتهاء البرنامج التدريبي، لأغراض التحقق من الشهادات</td>
                  </tr>
                  <tr class="hover:bg-gray-50/50 dark:hover:bg-gray-800/40 transition">
                    <td class="p-4 sm:p-5 align-top">بيانات التحليلات (Google Analytics 4)</td>
                    <td class="p-4 sm:p-5 align-top text-gray-600 dark:text-gray-400">حتى 14 شهراً للبيانات الخاضعة لإعداد الاحتفاظ</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <p class="text-sm sm:text-base text-gray-600 dark:text-gray-400 pt-2">
              قد تبقى بعض التقارير الإحصائية المجمعة التي لا تُعرّف الشخص بصورة مباشرة، وفق طبيعة خدمة التحليلات المستخدمة.
            </p>
            <p>
              بعد انتهاء مدة الاحتفاظ، نحذف البيانات أو نتلفها أو نجعلها مجهولة الهوية بصورة آمنة، بحسب مقتضى الحال.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 9. أمن البيانات -->
          <section id="ar-security" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              9. أمن البيانات
            </h2>
            <p>
              نطبّق تدابير إدارية وتقنية ومادية مناسبة لحماية بياناتك الشخصية من الفقدان، أو الوصول أو الاستخدام أو التعديل أو الإفصاح غير المصرح به، أو التلف والإتلاف غير المشروع.
            </p>
            <p>
              وتشمل هذه التدابير، بحسب طبيعة النظام والخدمة: تشفير الاتصال بالموقع باستخدام HTTPS، وقصر الوصول إلى البيانات على الأشخاص المخولين، واستخدام وسائل أمن مناسبة لحماية الأنظمة والحسابات، وتطبيق إجراءات إدارية لتنظيم الوصول إلى المعلومات.
            </p>
            <p>
              في حال وقوع خرق للبيانات الشخصية من شأنه أن يُلحق ضرراً جسيماً بالبيانات أو بخصوصية الأفراد، سنتخذ الإجراءات المطلوبة، ومنها إخطار الجهة المختصة والأفراد المتأثرين، وفقاً لما يقتضيه القانون.
            </p>
            <p class="text-sm sm:text-base text-gray-500 dark:text-gray-400 italic">
              ومع ذلك، لا يمكن ضمان أن تكون أي وسيلة لنقل البيانات أو تخزينها إلكترونياً آمنة بصورة مطلقة.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 10. حقوقك -->
          <section id="ar-rights" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              10. حقوقك
            </h2>
            <p>
              وفقاً للقوانين المعمول بها في دولة قطر، يحق لك ما يلي فيما يتعلق ببياناتك الشخصية:
            </p>
            <ul class="list-disc list-inside space-y-3 ps-2 sm:ps-4">
              <li>
                <strong class="text-gray-900 dark:text-white">الحق في الاطلاع:</strong> معرفة ما إذا كنا نعالج بياناتك، والأغراض المتعلقة بهذه المعالجة.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">الحق في الحصول على نسخة:</strong> طلب نسخة من البيانات الشخصية التي نحتفظ بها عنك، وفقاً للضوابط القانونية المطبقة.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">الحق في التصحيح:</strong> طلب تصحيح البيانات غير الدقيقة أو استكمال البيانات غير المكتملة.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">الحق في الحذف:</strong> طلب حذف بياناتك متى لم تكن هناك حاجة مشروعة أو التزام قانوني يستوجب الاحتفاظ بها.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">الحق في سحب الموافقة:</strong> سحب موافقتك في أي وقت متى كانت المعالجة قائمة عليها، دون أن يؤثر ذلك على مشروعية المعالجة التي تمت قبل السحب.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">الحق في الاعتراض:</strong> الاعتراض على معالجة بياناتك إذا كانت غير ضرورية للأغراض التي جُمعت من أجلها، أو زائدة على متطلباتها، أو تمييزية، أو مجحفة، أو مخالفة للقانون. ويحق لك الاعتراض في أي وقت على معالجة بياناتك لأغراض التسويق المباشر.
              </li>
            </ul>

            <div class="mt-6 p-5 rounded-2xl bg-gray-50 dark:bg-gray-800/80 border border-gray-200 dark:border-gray-700 space-y-3">
              <p>
                <strong class="text-gray-900 dark:text-white">كيفية تقديم الطلب:</strong> 
                راسلنا على <a href="mailto:info@bestolex.com" class="text-amber-600 dark:text-amber-400 font-semibold hover:underline">info@bestolex.com</a>. قد نطلب معلومات مناسبة للتحقق من هويتك قبل تنفيذ الطلب، حمايةً للبيانات ومنعاً للإفصاح عنها لأي شخص غير مخول.
              </p>
              <p class="text-sm sm:text-base text-gray-600 dark:text-gray-300">
                سنرد على طلبك خلال 30 يوماً تقويمياً من تاريخ استلامه. وإذا استلزمت طبيعة الطلب أو المتطلبات القانونية وقتاً إضافياً، فسنبلغك بذلك.
              </p>
              <p class="text-sm sm:text-base text-gray-600 dark:text-gray-300">
                <strong class="text-gray-900 dark:text-white">حق الشكوى:</strong> 
                إذا لم تكن راضياً عن طريقة تعاملنا مع طلبك، يحق لك تقديم شكوى إلى الوكالة الوطنية للأمن السيبراني في دولة قطر، بصفتها الجهة المختصة بالإشراف على حماية خصوصية البيانات الشخصية، وفقاً للإجراءات المعتمدة لديها.
              </p>
            </div>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 11. ملفات تعريف الارتباط -->
          <section id="ar-cookies" class="space-y-5">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              11. ملفات تعريف الارتباط (Cookies)
            </h2>
            <p>
              يستخدم موقعنا ملفات تعريف الارتباط والتقنيات المشابهة لتشغيل الموقع، وتحسين أدائه، وفهم كيفية استخدامه، وقياس فعالية الحملات.
            </p>
            <p>
              ونستخدم <strong>Google Consent Mode v2</strong> من خلال <strong>Google Tag Manager</strong> لإدارة الموافقة المتعلقة بخدمات Google وملفات تعريف الارتباط.
            </p>

            <div class="space-y-4">
              <div class="p-4 rounded-xl bg-gray-50 dark:bg-gray-800/60 border border-gray-200 dark:border-gray-700">
                <h3 class="font-bold text-lg text-gray-900 dark:text-white mb-2">أ. ملفات تعريف الارتباط الضرورية</h3>
                <p class="text-sm sm:text-base text-gray-600 dark:text-gray-300">
                  تضمن التشغيل الأساسي للموقع، وتحفظ تفضيلات اللغة واختيارات الخصوصية وإعدادات الموافقة. وهي ضرورية لتقديم الوظائف الأساسية للموقع، ولا يمكن تعطيلها.
                </p>
              </div>

              <div class="p-4 rounded-xl bg-gray-50 dark:bg-gray-800/60 border border-gray-200 dark:border-gray-700">
                <h3 class="font-bold text-lg text-gray-900 dark:text-white mb-2">ب. ملفات تعريف الارتباط التحليلية</h3>
                <p class="text-sm sm:text-base text-gray-600 dark:text-gray-300">
                  نستخدمها عبر <strong>Google Analytics 4</strong> لفهم كيفية استخدام الزوار للموقع، ومصادر الزيارات، والصفحات الأكثر استخداماً، والأداء والتفاعل مع المحتوى. ولا تُفعَّل إلا وفقاً لاختيارات الموافقة التي تحددها.
                </p>
              </div>

              <div class="p-4 rounded-xl bg-gray-50 dark:bg-gray-800/60 border border-gray-200 dark:border-gray-700">
                <h3 class="font-bold text-lg text-gray-900 dark:text-white mb-2">ج. ملفات تعريف الارتباط التسويقية</h3>
                <p class="text-sm sm:text-base text-gray-600 dark:text-gray-300">
                  تُستخدم عند تفعيل خدمات التسويق والإعلانات، لقياس أداء الحملات والتحويلات، وتحسين ملاءمة الإعلانات، وتقييم فعاليتها على المنصات المختلفة. ولا تُفعَّل إلا وفقاً لاختيارات الموافقة التي تحددها.
                </p>
              </div>
            </div>

            <div class="p-4 rounded-xl bg-amber-500/5 dark:bg-amber-500/10 border border-amber-500/20">
              <h3 class="font-bold text-lg text-gray-900 dark:text-white mb-2">إشارات القياس عند عدم منح الموافقة</h3>
              <p class="text-sm sm:text-base text-gray-600 dark:text-gray-300">
                بحسب إعدادات Google Consent Mode المستخدمة، قد تُرسَل إلى Google إشارات قياس محدودة لا تستخدم ملفات تعريف الارتباط عندما لا تُمنح الموافقة، وذلك لأغراض القياس المجمع والنمذجة وتحسين دقة التقارير، وفق إعدادات الخدمة وسياسات Google.
              </p>
            </div>

            <div class="p-5 rounded-2xl bg-gradient-to-r from-amber-500/10 via-orange-500/10 to-amber-500/10 border border-amber-500/30 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
              <div>
                <h3 class="font-bold text-lg text-gray-900 dark:text-white mb-1">إدارة اختياراتك</h3>
                <p class="text-sm text-gray-600 dark:text-gray-300">
                  يمكنك مراجعة اختياراتك أو تغييرها في أي وقت عبر زر <strong>«إعدادات ملفات تعريف الارتباط»</strong> المتاح أسفل صفحات الموقع، أو من خلال إعدادات متصفحك.
                </p>
              </div>
              <button
                @click="openCookieSettings"
                type="button"
                class="shrink-0 inline-flex items-center justify-center gap-2 bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-gray-950 font-bold px-6 py-3 rounded-xl shadow-md transition transform active:scale-95"
              >
                <span>🍪</span>
                <span>إعدادات ملفات تعريف الارتباط</span>
              </button>
            </div>

            <p class="text-sm text-gray-500 dark:text-gray-400">
              لمعرفة كيفية استخدام Google للبيانات التي تجمعها المواقع التي تستخدم خدماتها: 
              <a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener noreferrer" class="text-amber-600 dark:text-amber-400 underline break-all">
                https://policies.google.com/technologies/partner-sites
              </a>
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 12. خصوصية القُصَّر -->
          <section id="ar-minors" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              12. خصوصية القُصَّر
            </h2>
            <p>
              موقعنا ومنتجاتنا وخدماتنا موجهة إلى الشركات والمؤسسات والجهات المهنية، ولا تستهدف الأشخاص الذين تقل أعمارهم عن 18 عاماً.
            </p>
            <p>
              لا نجمع عمداً بيانات شخصية عن القُصَّر. وإذا علمنا بأنه تم تزويدنا بمثل هذه البيانات، فسنحذفها أو نتعامل معها وفقاً للمتطلبات القانونية المطبقة.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 13. الروابط الخارجية -->
          <section id="ar-links" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              13. الروابط الخارجية
            </h2>
            <p>
              يحتوي الموقع على روابط إلى مواقع ومنصات تديرها جهات أخرى، مثل واتساب وإنستغرام وفيسبوك، ومواقع الشركات المصنعة والموردين والشركاء.
            </p>
            <p>
              لا تخضع تلك المواقع والخدمات لهذه السياسة، ولا نتحكم في ممارسات الخصوصية الخاصة بها. لذلك نوصي بمراجعة سياسة الخصوصية لكل موقع أو خدمة خارجية قبل تقديم بيانات شخصية إليها.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 14. تحديث سياسة الخصوصية -->
          <section id="ar-updates" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              14. تحديث سياسة الخصوصية
            </h2>
            <p>
              قد نحدّث هذه السياسة من وقت لآخر لتعكس التغيرات في أنشطة الشركة أو الموقع، أو الخدمات والتقنيات الجديدة، أو المتطلبات القانونية والتنظيمية.
            </p>
            <p>
              تُنشر النسخة المحدثة على هذه الصفحة مع تعديل تاريخ "آخر تحديث". وعند إجراء تغييرات جوهرية تؤثر بصورة مهمة على كيفية استخدام بياناتك، سنبلغك بالوسائل المناسبة.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 15. اللغة -->
          <section id="ar-language" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              15. اللغة
            </h2>
            <p>
              تتوفر هذه السياسة باللغتين العربية والإنجليزية. وفي حال وجود أي اختلاف أو تعارض في التفسير بين النسختين، يُعتد بالنص العربي ما لم يقتض القانون خلاف ذلك.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 16. معلومات الشركة والتواصل -->
          <section id="ar-contact" class="space-y-6">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              16. معلومات الشركة والتواصل
            </h2>
            
            <div class="p-6 sm:p-8 rounded-3xl bg-gray-50 dark:bg-gray-800/70 border border-gray-200 dark:border-gray-700/70 space-y-4">
              <div class="mb-4">
                <h3 class="text-xl sm:text-2xl font-black text-gray-900 dark:text-white">
                  بيستوليكس لتجارة الآلات والمعدات الثقيلة (ذ.م.م)
                </h3>
                <p class="text-gray-500 dark:text-gray-400 font-medium">
                  Bestolex Trading of Heavy Equipment and Machinery W.L.L
                </p>
              </div>

              <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm sm:text-base">
                <div class="p-3 bg-white dark:bg-gray-900/60 rounded-xl border border-gray-100 dark:border-gray-800">
                  <span class="text-gray-500 dark:text-gray-400 block text-xs">السجل التجاري</span>
                  <span class="font-bold text-gray-900 dark:text-white font-mono">248416</span>
                </div>
                <div class="p-3 bg-white dark:bg-gray-900/60 rounded-xl border border-gray-100 dark:border-gray-800">
                  <span class="text-gray-500 dark:text-gray-400 block text-xs">الرخصة التجارية</span>
                  <span class="font-bold text-gray-900 dark:text-white font-mono">337386</span>
                </div>
                <div class="p-3 bg-white dark:bg-gray-900/60 rounded-xl border border-gray-100 dark:border-gray-800">
                  <span class="text-gray-500 dark:text-gray-400 block text-xs">الرقم الضريبي</span>
                  <span class="font-bold text-gray-900 dark:text-white font-mono">5009022658</span>
                </div>
                <div class="p-3 bg-white dark:bg-gray-900/60 rounded-xl border border-gray-100 dark:border-gray-800">
                  <span class="text-gray-500 dark:text-gray-400 block text-xs">صندوق البريد</span>
                  <span class="font-bold text-gray-900 dark:text-white">ص.ب: 37439، الدوحة، دولة قطر</span>
                </div>
              </div>

              <div class="pt-2 space-y-2 text-sm sm:text-base border-t border-gray-200 dark:border-gray-700/60">
                <p>
                  <strong class="text-gray-900 dark:text-white">العنوان:</strong> 
                  الدوحة، المنتزه، منطقة 24، شارع 830، مبنى 16، الطابق 7، مكتب 714، دولة قطر
                </p>
                <p>
                  <strong class="text-gray-900 dark:text-white">البريد الإلكتروني:</strong> 
                  <a href="mailto:info@bestolex.com" class="text-amber-600 dark:text-amber-400 font-semibold hover:underline">info@bestolex.com</a>
                </p>
                <p>
                  <strong class="text-gray-900 dark:text-white">الهاتف:</strong> 
                  <span dir="ltr" class="font-mono text-gray-900 dark:text-white font-semibold">
                    <a href="tel:+97450708833" class="hover:text-amber-600 dark:hover:text-amber-400">+974 5070 8833</a> / 
                    <a href="tel:+97451505014" class="hover:text-amber-600 dark:hover:text-amber-400">+974 5150 5014</a>
                  </span>
                </p>
                <p>
                  <strong class="text-gray-900 dark:text-white">الموقع الإلكتروني:</strong> 
                  <a href="https://www.bestolex.com" target="_blank" rel="noopener noreferrer" class="text-amber-600 dark:text-amber-400 font-semibold hover:underline">www.bestolex.com</a>
                </p>
              </div>
            </div>
          </section>

        </div>


        <!-- ENGLISH CONTENT -->
        <div v-else class="space-y-12 text-gray-700 dark:text-gray-300 leading-relaxed text-base sm:text-lg">
          
          <!-- 1. Introduction -->
          <section id="en-intro" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              1. Introduction
            </h2>
            <p>
              Bestolex Trading of Heavy Equipment and Machinery W.L.L ("the Company", "we" or "us") respects the privacy of visitors to its website, its customers and those who deal with it. We are committed to handling and protecting their personal data in accordance with Qatar Law No. (13) of 2016 on Personal Data Privacy Protection and related legislation and regulations.
            </p>
            <p>
              This Policy explains what personal data we collect, how we collect it, the purposes for which we use it, the parties with whom we share it, how we protect and retain it, and the rights available to you in relation to it.
            </p>
            <p>
              This Policy applies to the website 
              <a href="https://www.bestolex.com" target="_blank" rel="noopener noreferrer" class="text-amber-600 dark:text-amber-400 font-semibold hover:underline">www.bestolex.com</a> 
              and to your communications with us by email, telephone, WhatsApp, contact forms and our other business channels. Use of the website is also governed by our 
              <NuxtLink :to="localePath('/terms')" class="text-amber-600 dark:text-amber-400 font-semibold hover:underline">Terms of Use</NuxtLink>.
            </p>
            <p class="font-medium text-gray-900 dark:text-gray-100">
              The Company is the controller responsible for the personal data covered by this Policy.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 2. Data We Collect -->
          <section id="en-data" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              2. Data We Collect
            </h2>
            <p>
              Depending on how you interact with us, we collect the following categories of data:
            </p>
            <ul class="list-disc list-inside space-y-3 ps-2 sm:ps-4">
              <li>
                <strong class="text-gray-900 dark:text-white">Identity and contact data:</strong> 
                name, job title, name of the company or organisation you represent, email address, phone numbers, and facility or project site address where relevant.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">Enquiry and correspondence data:</strong> 
                details of enquiries and quotation requests, technical and commercial project requirements, site survey and visit appointments, photos and documents you send us, and records of correspondence relating to your request.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">Contract and billing data:</strong> 
                purchase orders, contracts and invoices; supply, warranty, maintenance and spare parts data; and information relating to the performance of commercial and contractual obligations.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">Training data:</strong> 
                when you register for a training programme, this includes trainee details and employer, registration information, attendance records and certificate data.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">Technical and website usage data:</strong> 
                IP address, device, browser and operating system type, pages visited, visit duration and source, and website interaction data.
              </li>
            </ul>
            <div class="p-4 rounded-2xl bg-gray-100 dark:bg-gray-800/60 border border-gray-200 dark:border-gray-700/60 text-sm sm:text-base">
              Non-essential technical data is collected according to your cookie and consent preferences.
            </div>
            <p class="text-sm sm:text-base text-gray-600 dark:text-gray-400 italic">
              We do not request or knowingly collect personal data of a special nature, such as health or religious data. Please do not send such data to us unless it is necessary and lawfully required for a specific purpose.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 3. How We Collect Data -->
          <section id="en-collection" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              3. How We Collect Data
            </h2>
            <p>We collect your data in the following ways:</p>
            <ul class="list-disc list-inside space-y-3 ps-2 sm:ps-4">
              <li>
                <strong class="text-gray-900 dark:text-white">Directly from you:</strong> 
                when you complete contact forms, request a quotation, book an appointment or site survey, register for a training programme, or contact us by email, telephone or WhatsApp.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">During commercial or contractual dealings with us.</strong>
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">Automatically when you use the website:</strong> 
                through strictly necessary cookies, and through non-essential analytics and marketing tools after obtaining your consent.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">From other parties:</strong> 
                from your employer or its representatives when you are involved in a project or transaction with us, or from suppliers, manufacturers or partners where necessary to fulfil a request or service relating to you.
              </li>
            </ul>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 4. Purposes and Justification for Processing -->
          <section id="en-purposes" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              4. Purposes and Justification for Processing
            </h2>
            
            <div class="overflow-x-auto rounded-2xl border border-gray-200 dark:border-gray-700 shadow-sm mt-4">
              <table class="w-full text-left border-collapse">
                <thead>
                  <tr class="bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-white border-b border-gray-200 dark:border-gray-700">
                    <th class="p-4 sm:p-5 font-bold text-base sm:text-lg w-1/2">Purpose</th>
                    <th class="p-4 sm:p-5 font-bold text-base sm:text-lg w-1/2">Justification</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-gray-200 dark:divide-gray-800 text-sm sm:text-base">
                  <tr class="hover:bg-gray-50/50 dark:hover:bg-gray-800/40 transition">
                    <td class="p-4 sm:p-5 align-top">Responding to enquiries and preparing quotations and technical and commercial proposals</td>
                    <td class="p-4 sm:p-5 align-top text-gray-600 dark:text-gray-400">Legitimate purpose linked to responding to your request and taking the necessary steps</td>
                  </tr>
                  <tr class="hover:bg-gray-50/50 dark:hover:bg-gray-800/40 transition">
                    <td class="p-4 sm:p-5 align-top">Performing contracts and supply, installation, commissioning, training, warranty, maintenance and spare parts operations</td>
                    <td class="p-4 sm:p-5 align-top text-gray-600 dark:text-gray-400">Legitimate purpose necessary to perform the contractual relationship</td>
                  </tr>
                  <tr class="hover:bg-gray-50/50 dark:hover:bg-gray-800/40 transition">
                    <td class="p-4 sm:p-5 align-top">Issuing invoices, keeping records and meeting commercial, tax and regulatory requirements</td>
                    <td class="p-4 sm:p-5 align-top text-gray-600 dark:text-gray-400">Compliance with legal and regulatory obligations</td>
                  </tr>
                  <tr class="hover:bg-gray-50/50 dark:hover:bg-gray-800/40 transition">
                    <td class="p-4 sm:p-5 align-top">Operating the website and protecting it against misuse and security risks</td>
                    <td class="p-4 sm:p-5 align-top text-gray-600 dark:text-gray-400">Legitimate purpose relating to website security and operation</td>
                  </tr>
                  <tr class="hover:bg-gray-50/50 dark:hover:bg-gray-800/40 transition">
                    <td class="p-4 sm:p-5 align-top">Analysing website performance and improving content and user experience</td>
                    <td class="p-4 sm:p-5 align-top text-gray-600 dark:text-gray-400">Your consent to non-essential cookies and technologies</td>
                  </tr>
                  <tr class="hover:bg-gray-50/50 dark:hover:bg-gray-800/40 transition">
                    <td class="p-4 sm:p-5 align-top">Sending offers, news and marketing communications</td>
                    <td class="p-4 sm:p-5 align-top text-gray-600 dark:text-gray-400">Your prior consent</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <p class="pt-2">
              We will not use your data for a purpose materially different from those for which it was collected without informing you and taking the required steps, including obtaining your consent where necessary.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 5. Direct Marketing -->
          <section id="en-marketing" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              5. Direct Marketing
            </h2>
            <p>
              We send electronic marketing communications by email, SMS or WhatsApp only after obtaining your prior consent, and in accordance with legal requirements.
            </p>
            <p>
              Every marketing message includes a clear means to unsubscribe. You may unsubscribe or withdraw your consent at any time using the unsubscribe option in the message, by replying with an unsubscribe request, or by emailing 
              <a href="mailto:info@bestolex.com" class="text-amber-600 dark:text-amber-400 font-semibold hover:underline">info@bestolex.com</a>.
            </p>
            <p class="text-sm sm:text-base text-gray-600 dark:text-gray-400">
              Unsubscribing does not affect necessary communications relating to existing requests, quotations, contracts, services or legal obligations.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 6. Sharing Your Data -->
          <section id="en-sharing" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              6. Sharing Your Data
            </h2>
            <div class="p-4 rounded-2xl bg-amber-500/10 border border-amber-500/20 text-gray-900 dark:text-white font-bold text-lg">
              Bestolex does not sell or rent your personal data.
            </div>
            <p>
              We share your data only to the extent necessary to achieve the legitimate purpose, with the following parties:
            </p>
            <ul class="list-disc list-inside space-y-3 ps-2 sm:ps-4">
              <li>
                <strong class="text-gray-900 dark:text-white">Manufacturers and authorised suppliers:</strong> 
                including Saudi Asas Technology Works Co. Ltd. (SAB TECH) in the Kingdom of Saudi Arabia, to confirm technical specifications, prepare quotations, supply products, or provide technical support, warranty, maintenance and spare parts.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">Technical partners and subcontractors:</strong> 
                where their involvement is necessary for site surveys, installation, commissioning, maintenance or related technical services.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">Technology service providers:</strong> 
                such as website hosting, email, digital infrastructure, Google analytics services, and messaging services such as WhatsApp.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">Shipping, clearance and logistics companies:</strong> 
                where necessary to supply equipment or fulfil an order.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">Government, regulatory and judicial authorities:</strong> 
                where disclosure is required by law or by a decision of a competent authority, or is necessary to protect the Company's legal rights.
              </li>
            </ul>
            <p>
              When a service provider processes personal data on our behalf, we take appropriate measures, including contractual obligations where applicable, to ensure the data is kept confidential, protected and used only for the specified purposes.
            </p>
            <p class="text-sm sm:text-base text-gray-600 dark:text-gray-400">
              Some parties, such as Google and WhatsApp, may process data as independent entities under their own privacy policies and legal obligations.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 7. Transfers Outside Qatar -->
          <section id="en-transfers" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              7. Transfers Outside Qatar
            </h2>
            <p>
              Some personal data is transferred, processed or stored outside the State of Qatar when dealing with:
            </p>
            <ul class="list-disc list-inside space-y-2 ps-2 sm:ps-4">
              <li>Suppliers and manufacturers in the Kingdom of Saudi Arabia, including SAB TECH, or in other countries.</li>
              <li>International technology service providers, including hosting and cloud computing services, Google services and messaging platforms.</li>
            </ul>
            <p>
              When data is transferred or processed outside Qatar, we take reasonable and appropriate measures to ensure that processing complies with applicable legal requirements, and that the transfer does not prejudice the rights of data subjects or the level of protection afforded to them.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 8. Data Retention -->
          <section id="en-retention" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              8. Data Retention
            </h2>
            <p>
              We retain personal data only for as long as necessary to fulfil the purpose for which it was collected, or to meet legal, contractual, accounting or regulatory requirements:
            </p>

            <div class="overflow-x-auto rounded-2xl border border-gray-200 dark:border-gray-700 shadow-sm mt-4">
              <table class="w-full text-left border-collapse">
                <thead>
                  <tr class="bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-white border-b border-gray-200 dark:border-gray-700">
                    <th class="p-4 sm:p-5 font-bold text-base sm:text-lg w-1/2">Type of data</th>
                    <th class="p-4 sm:p-5 font-bold text-base sm:text-lg w-1/2">Retention period</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-gray-200 dark:divide-gray-800 text-sm sm:text-base">
                  <tr class="hover:bg-gray-50/50 dark:hover:bg-gray-800/40 transition">
                    <td class="p-4 sm:p-5 align-top">Enquiries and quotations that do not lead to a contract</td>
                    <td class="p-4 sm:p-5 align-top text-gray-600 dark:text-gray-400">Up to two years from the date of last contact, unless a legitimate reason requires a longer period</td>
                  </tr>
                  <tr class="hover:bg-gray-50/50 dark:hover:bg-gray-800/40 transition">
                    <td class="p-4 sm:p-5 align-top">Contract, invoice, warranty and commercial transaction data</td>
                    <td class="p-4 sm:p-5 align-top text-gray-600 dark:text-gray-400">For the duration of the contractual relationship, then for the period required by commercial, tax, accounting and regulatory laws in Qatar</td>
                  </tr>
                  <tr class="hover:bg-gray-50/50 dark:hover:bg-gray-800/40 transition">
                    <td class="p-4 sm:p-5 align-top">Training data, attendance records and certificates</td>
                    <td class="p-4 sm:p-5 align-top text-gray-600 dark:text-gray-400">Up to five years after the training programme ends, for certificate verification purposes</td>
                  </tr>
                  <tr class="hover:bg-gray-50/50 dark:hover:bg-gray-800/40 transition">
                    <td class="p-4 sm:p-5 align-top">Analytics data (Google Analytics 4)</td>
                    <td class="p-4 sm:p-5 align-top text-gray-600 dark:text-gray-400">Up to 14 months for data subject to the retention setting</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <p class="text-sm sm:text-base text-gray-600 dark:text-gray-400 pt-2">
              Some aggregated statistical reports that do not directly identify individuals may remain, depending on the nature of the analytics service used.
            </p>
            <p>
              At the end of the retention period, we securely delete, destroy or anonymise the data, as appropriate.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 9. Data Security -->
          <section id="en-security" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              9. Data Security
            </h2>
            <p>
              We apply appropriate administrative, technical and physical measures to protect your personal data against loss; unauthorised access, use, alteration or disclosure; and unlawful damage or destruction.
            </p>
            <p>
              Depending on the nature of the system and service, these measures include encrypting website connections using HTTPS, restricting data access to authorised persons, using appropriate security tools to protect systems and accounts, and applying administrative procedures to control access to information.
            </p>
            <p>
              If a personal data breach occurs that may cause serious damage to the data or to individuals' privacy, we will take the required actions, including notifying the competent authority and affected individuals, as required by law.
            </p>
            <p class="text-sm sm:text-base text-gray-500 dark:text-gray-400 italic">
              However, no method of electronic transmission or storage can be guaranteed to be completely secure.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 10. Your Rights -->
          <section id="en-rights" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              10. Your Rights
            </h2>
            <p>
              Under the applicable laws of the State of Qatar, you have the following rights in relation to your personal data:
            </p>
            <ul class="list-disc list-inside space-y-3 ps-2 sm:ps-4">
              <li>
                <strong class="text-gray-900 dark:text-white">Right to be informed:</strong> to know whether we process your data and the purposes of that processing.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">Right to obtain a copy:</strong> to request a copy of the personal data we hold about you, subject to applicable legal controls.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">Right to correction:</strong> to request correction of inaccurate data or completion of incomplete data.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">Right to deletion:</strong> to request deletion of your data where there is no legitimate need or legal obligation to retain it.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">Right to withdraw consent:</strong> to withdraw your consent at any time where processing is based on it, without affecting the lawfulness of processing carried out before withdrawal.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">Right to object:</strong> to object to the processing of your data if it is unnecessary for the purposes for which it was collected, excessive in relation to those purposes, discriminatory, unfair or unlawful. You also have the right to object at any time to processing of your data for direct marketing.
              </li>
            </ul>

            <div class="mt-6 p-5 rounded-2xl bg-gray-50 dark:bg-gray-800/80 border border-gray-200 dark:border-gray-700 space-y-3">
              <p>
                <strong class="text-gray-900 dark:text-white">How to submit a request:</strong> 
                Email <a href="mailto:info@bestolex.com" class="text-amber-600 dark:text-amber-400 font-semibold hover:underline">info@bestolex.com</a>. We may request appropriate information to verify your identity before acting on the request, in order to protect the data and prevent disclosure to unauthorised persons.
              </p>
              <p class="text-sm sm:text-base text-gray-600 dark:text-gray-300">
                We will respond to your request within 30 calendar days of receipt. If the nature of the request or legal requirements require additional time, we will inform you.
              </p>
              <p class="text-sm sm:text-base text-gray-600 dark:text-gray-300">
                <strong class="text-gray-900 dark:text-white">Right to complain:</strong> 
                If you are not satisfied with how we handled your request, you may lodge a complaint with the National Cyber Security Agency of the State of Qatar, as the competent authority overseeing personal data privacy protection, in accordance with its procedures.
              </p>
            </div>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 11. Cookies -->
          <section id="en-cookies" class="space-y-5">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              11. Cookies
            </h2>
            <p>
              Our website uses cookies and similar technologies to operate the website, improve its performance, understand how it is used and measure campaign effectiveness.
            </p>
            <p>
              We use <strong>Google Consent Mode v2</strong> through <strong>Google Tag Manager</strong> to manage consent for Google services and cookies.
            </p>

            <div class="space-y-4">
              <div class="p-4 rounded-xl bg-gray-50 dark:bg-gray-800/60 border border-gray-200 dark:border-gray-700">
                <h3 class="font-bold text-lg text-gray-900 dark:text-white mb-2">a. Strictly necessary cookies</h3>
                <p class="text-sm sm:text-base text-gray-600 dark:text-gray-300">
                  These ensure the basic operation of the website and store language preferences, privacy choices and consent settings. They are necessary to provide the website's core functions and cannot be disabled.
                </p>
              </div>

              <div class="p-4 rounded-xl bg-gray-50 dark:bg-gray-800/60 border border-gray-200 dark:border-gray-700">
                <h3 class="font-bold text-lg text-gray-900 dark:text-white mb-2">b. Analytics cookies</h3>
                <p class="text-sm sm:text-base text-gray-600 dark:text-gray-300">
                  We use these through <strong>Google Analytics 4</strong> to understand how visitors use the website, traffic sources, the most visited pages, and performance and content engagement. They are activated only according to the consent choices you make.
                </p>
              </div>

              <div class="p-4 rounded-xl bg-gray-50 dark:bg-gray-800/60 border border-gray-200 dark:border-gray-700">
                <h3 class="font-bold text-lg text-gray-900 dark:text-white mb-2">c. Marketing cookies</h3>
                <p class="text-sm sm:text-base text-gray-600 dark:text-gray-300">
                  These are used when marketing and advertising services are enabled, to measure campaign performance and conversions, improve ad relevance and evaluate advertising effectiveness across platforms. They are activated only according to the consent choices you make.
                </p>
              </div>
            </div>

            <div class="p-4 rounded-xl bg-amber-500/5 dark:bg-amber-500/10 border border-amber-500/20">
              <h3 class="font-bold text-lg text-gray-900 dark:text-white mb-2">Measurement signals without consent</h3>
              <p class="text-sm sm:text-base text-gray-600 dark:text-gray-300">
                Depending on the Google Consent Mode settings in use, limited cookieless measurement signals may be sent to Google when consent is not given, for aggregated measurement, modelling and improving report accuracy, in accordance with the service settings and Google's policies.
              </p>
            </div>

            <div class="p-5 rounded-2xl bg-gradient-to-r from-amber-500/10 via-orange-500/10 to-amber-500/10 border border-amber-500/30 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
              <div>
                <h3 class="font-bold text-lg text-gray-900 dark:text-white mb-1">Managing your choices</h3>
                <p class="text-sm text-gray-600 dark:text-gray-300">
                  You can review or change your choices at any time using the <strong>"Cookie Settings"</strong> button at the bottom of the website pages, or through your browser settings.
                </p>
              </div>
              <button
                @click="openCookieSettings"
                type="button"
                class="shrink-0 inline-flex items-center justify-center gap-2 bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-gray-950 font-bold px-6 py-3 rounded-xl shadow-md transition transform active:scale-95"
              >
                <span>🍪</span>
                <span>Cookie Settings</span>
              </button>
            </div>

            <p class="text-sm text-gray-500 dark:text-gray-400">
              To learn how Google uses data from sites that use its services: 
              <a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener noreferrer" class="text-amber-600 dark:text-amber-400 underline break-all">
                https://policies.google.com/technologies/partner-sites
              </a>
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 12. Children's Privacy -->
          <section id="en-minors" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              12. Children's Privacy
            </h2>
            <p>
              Our website, products and services are intended for companies, institutions and professional organisations, and are not directed at persons under 18 years of age.
            </p>
            <p>
              We do not knowingly collect personal data about minors. If we become aware that such data has been provided to us, we will delete it or handle it in accordance with applicable legal requirements.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 13. External Links -->
          <section id="en-links" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              13. External Links
            </h2>
            <p>
              The website contains links to websites and platforms operated by other parties, such as WhatsApp, Instagram and Facebook, and the websites of manufacturers, suppliers and partners.
            </p>
            <p>
              Those websites and services are not covered by this Policy, and we do not control their privacy practices. We therefore recommend reviewing the privacy policy of each external website or service before providing personal data to it.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 14. Updates to This Privacy Policy -->
          <section id="en-updates" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              14. Updates to This Privacy Policy
            </h2>
            <p>
              We may update this Policy from time to time to reflect changes in the Company's activities or website, new services and technologies, or legal and regulatory requirements.
            </p>
            <p>
              The updated version will be published on this page with a revised "Last Updated" date. Where material changes significantly affect how your data is used, we will notify you by appropriate means.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 15. Language -->
          <section id="en-language" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              15. Language
            </h2>
            <p>
              This Policy is available in Arabic and English. In the event of any difference or conflict in interpretation between the two versions, the Arabic text prevails unless the law requires otherwise.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 16. Company Information and Contact -->
          <section id="en-contact" class="space-y-6">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              16. Company Information and Contact
            </h2>
            
            <div class="p-6 sm:p-8 rounded-3xl bg-gray-50 dark:bg-gray-800/70 border border-gray-200 dark:border-gray-700/70 space-y-4">
              <div class="mb-4">
                <h3 class="text-xl sm:text-2xl font-black text-gray-900 dark:text-white">
                  Bestolex Trading of Heavy Equipment and Machinery W.L.L
                </h3>
                <p class="text-gray-500 dark:text-gray-400 font-medium">
                  بيستوليكس لتجارة الآلات والمعدات الثقيلة (ذ.م.م)
                </p>
              </div>

              <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm sm:text-base">
                <div class="p-3 bg-white dark:bg-gray-900/60 rounded-xl border border-gray-100 dark:border-gray-800">
                  <span class="text-gray-500 dark:text-gray-400 block text-xs">Commercial Registration</span>
                  <span class="font-bold text-gray-900 dark:text-white font-mono">248416</span>
                </div>
                <div class="p-3 bg-white dark:bg-gray-900/60 rounded-xl border border-gray-100 dark:border-gray-800">
                  <span class="text-gray-500 dark:text-gray-400 block text-xs">Commercial License</span>
                  <span class="font-bold text-gray-900 dark:text-white font-mono">337386</span>
                </div>
                <div class="p-3 bg-white dark:bg-gray-900/60 rounded-xl border border-gray-100 dark:border-gray-800">
                  <span class="text-gray-500 dark:text-gray-400 block text-xs">Tax Number</span>
                  <span class="font-bold text-gray-900 dark:text-white font-mono">5009022658</span>
                </div>
                <div class="p-3 bg-white dark:bg-gray-900/60 rounded-xl border border-gray-100 dark:border-gray-800">
                  <span class="text-gray-500 dark:text-gray-400 block text-xs">P.O. Box</span>
                  <span class="font-bold text-gray-900 dark:text-white">P.O. Box: 37439, Doha, State of Qatar</span>
                </div>
              </div>

              <div class="pt-2 space-y-2 text-sm sm:text-base border-t border-gray-200 dark:border-gray-700/60">
                <p>
                  <strong class="text-gray-900 dark:text-white">Address:</strong> 
                  Office 714, Floor 7, Building 16, Street 830, Zone 24, Al Muntazah, Doha, State of Qatar
                </p>
                <p>
                  <strong class="text-gray-900 dark:text-white">Email:</strong> 
                  <a href="mailto:info@bestolex.com" class="text-amber-600 dark:text-amber-400 font-semibold hover:underline">info@bestolex.com</a>
                </p>
                <p>
                  <strong class="text-gray-900 dark:text-white">Phone:</strong> 
                  <span class="font-mono text-gray-900 dark:text-white font-semibold">
                    <a href="tel:+97450708833" class="hover:text-amber-600 dark:hover:text-amber-400">+974 5070 8833</a> / 
                    <a href="tel:+97451505014" class="hover:text-amber-600 dark:hover:text-amber-400">+974 5150 5014</a>
                  </span>
                </p>
                <p>
                  <strong class="text-gray-900 dark:text-white">Website:</strong> 
                  <a href="https://www.bestolex.com" target="_blank" rel="noopener noreferrer" class="text-amber-600 dark:text-amber-400 font-semibold hover:underline">www.bestolex.com</a>
                </p>
              </div>
            </div>
          </section>

        </div>

      </article>

    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'

const { locale } = useI18n()
const localePath = useLocalePath()

const isAr = computed(() => locale.value === 'ar')

const openCookieSettings = () => {
  if (typeof window !== 'undefined') {
    window.dispatchEvent(new CustomEvent('open-cookie-settings'))
  }
}

useSeoMeta({
  title: isAr.value ? 'سياسة الخصوصية | بيستوليكس' : 'Privacy Policy | Bestolex',
  description: isAr.value 
    ? 'سياسة الخصوصية وحماية البيانات الشخصية لشركة بيستوليكس لتجارة الآلات والمعدات الثقيلة في دولة قطر وفقاً للقانون رقم (13) لسنة 2016.'
    : 'Privacy policy and personal data protection of Bestolex Trading of Heavy Equipment and Machinery in Qatar pursuant to Law No. (13) of 2016.',
  robots: 'index, follow'
})
</script>
