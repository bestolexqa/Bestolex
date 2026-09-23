<template>
  <div class="terms-page bg-gray-50 dark:bg-gray-950 min-h-screen transition-colors duration-300 py-16 md:py-24">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8 max-w-5xl">
      
      <!-- Main Card -->
      <article class="bg-white dark:bg-gray-900 rounded-3xl p-6 sm:p-10 md:p-14 shadow-xl border border-gray-100 dark:border-gray-800 transition-colors">
        
        <!-- Header -->
        <header class="text-center border-b border-gray-200 dark:border-gray-800 pb-10 mb-12">
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-amber-500/10 text-amber-600 dark:text-amber-400 text-xs sm:text-sm font-semibold mb-4">
            <span class="w-2 h-2 rounded-full bg-amber-500 animate-pulse"></span>
            {{ locale === 'ar' ? 'آخر تحديث: 17 سبتمبر 2026' : 'Last Updated: 17 September 2026' }}
          </div>
          <h1 class="text-3xl sm:text-4xl md:text-5xl font-black text-gray-900 dark:text-white tracking-tight mb-4">
            {{ locale === 'ar' ? 'شروط الاستخدام' : 'Terms of Use' }}
          </h1>
          <p class="text-lg sm:text-xl font-bold text-gray-700 dark:text-gray-300">
            {{ locale === 'ar' ? 'بيستوليكس لتجارة الآلات والمعدات الثقيلة (ذ.م.م)' : 'Bestolex Trading of Heavy Equipment and Machinery W.L.L' }}
          </p>
        </header>

        <!-- ARABIC CONTENT -->
        <div v-if="locale === 'ar'" class="space-y-12 text-gray-700 dark:text-gray-300 leading-relaxed text-base sm:text-lg">
          
          <!-- 1. مقدمة وقبول الشروط -->
          <section id="ar-sec-1" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              1. مقدمة وقبول الشروط
            </h2>
            <p>
              مرحباً بكم في الموقع الإلكتروني لشركة بيستوليكس لتجارة الآلات والمعدات الثقيلة (ذ.م.م)، المشار إليها في هذه الشروط بـ"بيستوليكس" أو "الشركة" أو "نحن".
            </p>
            <p>
              تحكم هذه الشروط وصولك إلى الموقع الإلكتروني 
              <a href="https://www.bestolex.com" target="_blank" rel="noopener noreferrer" class="text-amber-600 dark:text-amber-400 font-semibold hover:underline">www.bestolex.com</a> ("الموقع")، واستخدامك للمحتوى والمعلومات والنماذج والوظائف والخدمات الإلكترونية المتاحة من خلاله.
            </p>
            <p>
              باستخدامك للموقع، فإنك تقرّ بأنك قرأت هذه الشروط وفهمتها ووافقت على الالتزام بها. وإذا كنت لا توافق عليها، يُرجى عدم استخدام الموقع.
            </p>
            <p>
              إذا كنت تستخدم الموقع نيابةً عن شركة أو مؤسسة أو جهة أخرى، فإنك تقرّ بأن لديك الصلاحية المناسبة للتواصل والتصرف نيابةً عنها في حدود الاستخدام أو الطلب المعني.
            </p>
            <p>
              وتخضع معالجة البيانات الشخصية عبر الموقع لـ<NuxtLink :to="localePath('/privacy')" class="text-amber-600 dark:text-amber-400 font-semibold hover:underline">سياسة الخصوصية</NuxtLink>.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 2. الغرض من الموقع -->
          <section id="ar-sec-2" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              2. الغرض من الموقع
            </h2>
            <p>
              يهدف الموقع إلى التعريف ببيستوليكس وأنشطتها ومنتجاتها وخدماتها وحلولها التجارية والفنية والقطاعات التي تخدمها، وتمكين العملاء والموردين والشركاء من إرسال الاستفسارات، وطلب عروض الأسعار والمعلومات الفنية، وحجز المواعيد والمعاينات، والتسجيل في البرامج التدريبية عند توفرها، والتواصل مع الشركة عبر قنواتها الرسمية.
            </p>
            <div class="p-4 rounded-2xl bg-gray-100 dark:bg-gray-800/60 border border-gray-200 dark:border-gray-700/60 text-sm sm:text-base font-medium">
              الموقع موجه بصورة أساسية إلى الشركات والمؤسسات والجهات الحكومية والمهنيين والعملاء التجاريين.
            </div>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 3. طبيعة المحتوى ودقة المعلومات -->
          <section id="ar-sec-3" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              3. طبيعة المحتوى ودقة المعلومات
            </h2>
            <p>
              ما لم تذكر بيستوليكس صراحةً خلاف ذلك، فإن المعلومات المنشورة على الموقع، بما فيها أوصاف المنتجات والمواصفات والصور والرسومات والكتالوجات والبيانات الفنية والتطبيقات المقترحة ومعلومات الخدمات، تُقدَّم <strong class="text-gray-900 dark:text-white">لأغراض التعريف والمعلومات العامة فقط</strong>. ولا تشكل بمفردها عرض بيع، أو التزاماً تعاقدياً، أو استشارة هندسية أو فنية خاصة بمشروعك، أو ضماناً لملاءمة منتج أو نظام لاستخدام محدد دون دراسة متطلبات المشروع.
            </p>
            <p>نبذل جهوداً معقولة للمحافظة على دقة المعلومات وحداثتها، إلا أن:</p>
            <ul class="list-disc list-inside space-y-3 ps-2 sm:ps-4">
              <li>
                <strong class="text-gray-900 dark:text-white">المصنّعين والموردين:</strong> قد يغيّرون التصميم أو المواصفات أو الأبعاد أو المواد والمكونات أو السعات أو الطرازات أو أنظمة التحكم أو الملحقات أو التشطيبات أو بلد المنشأ أو التوافر، دون إشعار مسبق وقبل تحديث المعلومات على الموقع.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">الصور والرسومات ومقاطع الفيديو:</strong> توضيحية، وقد يختلف المنتج الفعلي في اللون أو الحجم أو التجهيزات أو الشكل الخارجي أو الطراز أو التكوين النهائي. ولا يُعتمد عليها وحدها لتحديد المواصفات أو نطاق التوريد.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">عرض المنتج على الموقع:</strong> لا يعني بالضرورة توفره في المخزون بصورة فورية.
              </li>
            </ul>
            <p class="p-4 rounded-2xl bg-amber-500/5 dark:bg-amber-500/10 border border-amber-500/20 text-sm sm:text-base">
              إذا كانت أي معلومة عنصراً جوهرياً في قرار الشراء، مثل السعر أو السعة أو الأبعاد أو قدرة التحميل أو بلد المنشأ أو الاعتمادات أو مدة التوريد أو التوافق مع متطلبات مشروع معين، فيجب تأكيدها من خلال العرض الفني أو التجاري المعتمد أو مستندات المصنّع الخاصة بالمعاملة قبل الشراء أو التعاقد.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 4. المعدات المستعملة -->
          <section id="ar-sec-4" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              4. المعدات المستعملة
            </h2>
            <p>
              عند عرض معدات أو آليات مستعملة على الموقع، تستند المعلومات المتعلقة بحالتها أو سنة صنعها أو ساعات تشغيلها أو مواصفاتها أو تجهيزاتها إلى المعلومات والسجلات المتاحة لدينا وقت النشر، ما لم يُذكر خلاف ذلك.
            </p>
            <p>
              تُحدَّد الحالة الفعلية ونطاق الفحص وأي ضمانات أو استثناءات وشروط البيع في عرض السعر أو تقرير الفحص أو العقد الخاص بالمعاملة.
            </p>
            <p>
              ويحق للعميل طلب المعاينة أو الفحص المستقل قبل إتمام الشراء، متى كان ذلك متاحاً ومناسباً.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 5. الاستفسارات وتكوين العقود وأولوية المستندات -->
          <section id="ar-sec-5" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              5. الاستفسارات وتكوين العقود وأولوية المستندات
            </h2>
            <p>
              لا يُنشئ تصفح الموقع، أو إرسال استفسار، أو تعبئة نموذج، أو طلب معلومات أو عرض سعر، بمفرده، أي التزام تعاقدي على بيستوليكس بقبول الطلب أو توريد منتج أو تنفيذ خدمة. ويجوز للشركة طلب معلومات أو مستندات أو مواصفات إضافية قبل إعداد عرض السعر أو المقترح الفني.
            </p>
            <p>
              تخضع عروض الأسعار للمدة والشروط والمواصفات والاستثناءات الواردة فيها. ولا تُعدّ المنتجات أو الخدمات محجوزة أو مؤكدة ما لم تؤكد بيستوليكس ذلك وفق الإجراءات التجارية المتفق عليها.
            </p>
            <p>
              قد ينشأ الالتزام التعاقدي بموجب عرض سعر مقبول، أو عقد، أو أمر شراء، أو موافقات ومراسلات إلكترونية معتمدة، أو أي وسيلة أخرى تستوفي المتطلبات القانونية والتجارية المعمول بها. وتعتمد طبيعة الالتزام على مضمون المستندات والمراسلات الخاصة بكل معاملة.
            </p>
            <p class="p-4 rounded-2xl bg-amber-500/10 border border-amber-500/20 text-gray-900 dark:text-white font-medium">
              تنظّم هذه الشروط استخدام الموقع فقط، ولا تحل محل الشروط الخاصة بكل صفقة أو مشروع. وإذا صدر عرض سعر أو عرض فني أو أمر شراء أو عقد توريد أو أمر عمل أو شروط ضمان أو اتفاقية صيانة أو أي مستند تعاقدي معتمد، <strong>فإن أحكامه تسود</strong> بالنسبة لتلك المعاملة، ومنها شروط التوريد والدفع والتسليم والتركيب والتشغيل والضمان والصيانة، عند تعارضها مع هذه الشروط أو مع المعلومات المنشورة على الموقع.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 6. الأسعار والتوافر ومواعيد التسليم -->
          <section id="ar-sec-6" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              6. الأسعار والتوافر ومواعيد التسليم
            </h2>
            <p>
              ما لم يُذكر صراحةً خلاف ذلك، لا يمثل الموقع قائمة أسعار ملزمة. وتتأثر الأسعار والتوافر بعوامل منها: مواصفات المنتج وخياراته وملحقاته وبلد المنشأ، وأسعار المصنّع أو المورد وأسعار الصرف، وتكاليف النقل والشحن والتأمين والرسوم الجمركية والضرائب عند انطباقها، ومتطلبات التركيب والتشغيل والمشروع، وحالة المخزون وظروف السوق.
            </p>
            <p>
              <strong class="text-gray-900 dark:text-white">السعر الملزم</strong> لأي معاملة هو السعر الوارد في عرض السعر أو الاتفاق الخاص بها، وفقاً لشروطه ومدة صلاحيته.
            </p>
            <p>
              أي مدد توريد أو تسليم منشورة بصورة عامة على الموقع <strong class="text-gray-900 dark:text-white">تقديرية</strong>، ما لم تُؤكَّد في مستند تجاري أو تعاقدي خاص بالمعاملة. وقد تتأثر المواعيد بعوامل مثل الإنتاج لدى المصنّع، وتوفر المنتجات، والشحن الدولي، والتخليص الجمركي، وإجراءات الجهات المختصة، وتأخير الموردين أو شركات النقل، والظروف الخارجة عن السيطرة المعقولة للشركة.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 7. المعلومات الفنية والمعاينات -->
          <section id="ar-sec-7" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              7. المعلومات الفنية والمعاينات
            </h2>
            <p>
              المعلومات الفنية والهندسية والتطبيقات المقترحة المنشورة على الموقع ذات طبيعة عامة، ما لم تُعَدّ صراحةً لمشروع محدد بناءً على بياناته الفنية.
            </p>
            <p>
              ولا تغني هذه المعلومات، عندما تقتضي طبيعة المشروع ذلك، عن المعاينة الميدانية، أو دراسة الاحتياجات، أو المخططات المعتمدة، أو الحسابات الهندسية وبيانات الأحمال، أو تقييم ظروف التشغيل والمتطلبات الكهربائية والميكانيكية، أو اشتراطات السلامة ومتطلبات الجهات المختصة.
            </p>
            <p>
              يتحمل العميل مسؤولية تزويد بيستوليكس بمعلومات صحيحة وكافية عن المشروع عند طلب توصية فنية أو عرض مخصص.
            </p>
            <div class="p-4 rounded-2xl bg-gray-50 dark:bg-gray-800/80 border border-gray-200 dark:border-gray-700/80 space-y-2">
              <h3 class="font-bold text-gray-900 dark:text-white">حجز المواعيد والمعاينات:</h3>
              <p class="text-sm sm:text-base text-gray-600 dark:text-gray-300">
                لا تُعدّ الطلبات المقدمة عبر الموقع مؤكدة إلا بعد تأكيدها من فريق بيستوليكس. ويلتزم مقدم الطلب بتقديم معلومات صحيحة وكاملة، وبأن يكون مخوّلاً بطلب الزيارة، وبتوفير دخول آمن ومشروع إلى الموقع، وبإبلاغنا مسبقاً بأي اشتراطات أمن أو سلامة أو تصاريح لازمة للدخول. ويجوز إعادة جدولة الموعد عندما تتطلب الظروف التشغيلية أو متطلبات الموقع ذلك.
              </p>
            </div>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 8. التركيب والتشغيل والسلامة -->
          <section id="ar-sec-8" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              8. التركيب والتشغيل والسلامة
            </h2>
            <p>
              لا يعني عرض منتج على الموقع أن التركيب أو التشغيل أو التدريب أو الصيانة مشمولة تلقائياً في سعره. ويُحدَّد نطاق هذه الخدمات، عند انطباقها، في عرض السعر أو العقد الخاص بالمعاملة.
            </p>
            <p>
              المعلومات المنشورة على الموقع لا تُغني عن أدلة التشغيل والصيانة الصادرة عن المصنّع، ولا عن التدريب المعتمد، ولا عن اشتراطات السلامة المعمول بها في دولة قطر.
            </p>
            <p>
              ويجب تركيب المعدات وتشغيلها وصيانتها وفقاً لتعليمات المصنّع وأدلة التشغيل والتعليمات الفنية المعتمدة ومتطلبات السلامة والقوانين واللوائح المعمول بها، وأن يتولى ذلك أشخاص مؤهلون ومدرَّبون متى استلزمت طبيعة المعدات ذلك.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 9. الضمان -->
          <section id="ar-sec-9" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              9. الضمان
            </h2>
            <p>
              تخضع الضمانات، عند توفرها، للشروط الواردة في عرض السعر أو العقد أو شهادة الضمان أو شروط المصنّع أو المورد أو المستندات التجارية الخاصة بالمعاملة. وتختلف مدة الضمان ونطاقه وشروطه واستثناءاته باختلاف المنتج والمصنّع وطبيعة المشروع.
            </p>
            <p>
              لا يشكل أي وصف عام منشور على الموقع ضماناً إضافياً يتجاوز الضمان المكتوب والمعتمد الخاص بالمعاملة. ولا يؤثر هذا البند على أي حقوق إلزامية لا يجوز قانوناً استبعادها أو تقييدها.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 10. التدريب والشهادات التدريبية -->
          <section id="ar-sec-10" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              10. التدريب والشهادات التدريبية
            </h2>
            <p>
              تخضع كل دورة أو برنامج تدريبي تقدمه بيستوليكس، منفردة أو بالتعاون مع شركائها، للشروط الخاصة به، ومنها عند الاقتضاء: المحتوى والمواعيد والمكان والرسوم وشروط التسجيل ومتطلبات الحضور والإلغاء أو إعادة الجدولة وشروط إصدار الشهادات.
            </p>
            <p>
              لا يُعدّ إدراج برنامج تدريبي على الموقع ضماناً لاستمرار توفره أو انعقاده في موعد معين، ما لم يُؤكَّد التسجيل أو الموعد رسمياً. وتُحدَّد الجهة المُصدِرة لأي شهادة تدريبية في مستندات البرنامج نفسه.
            </p>
            <p class="text-sm sm:text-base text-gray-600 dark:text-gray-400 italic">
              لا يجوز تسجيل المواد التدريبية أو نسخها أو إعادة نشرها أو استخدامها تجارياً دون إذن كتابي من صاحب الحق فيها.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 11. شهادات واعتمادات المنتجات والمصنّعين -->
          <section id="ar-sec-11" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              11. شهادات واعتمادات المنتجات والمصنّعين
            </h2>
            <p>
              قد يشير الموقع إلى شهادات أو معايير أو اعتمادات مرتبطة بمنتج أو مصنّع أو نظام معين. وتعود هذه الشهادات إلى الجهة أو المنتج المحدد في مستندها الرسمي، <strong class="text-gray-900 dark:text-white">ولا تُنسب إلى بيستوليكس</strong> إلا إذا كانت صادرة باسم الشركة مباشرة.
            </p>
            <p>
              ويجب الرجوع إلى الوثائق الرسمية للمنتج أو المصنّع للتأكد من نطاق أي شهادة أو اعتماد ومدى انطباقها على المنتج المحدد.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 12. المواد والمعلومات التي ترسلها إلينا -->
          <section id="ar-sec-12" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              12. المواد والمعلومات التي ترسلها إلينا
            </h2>
            <p>
              عند إرسال صور أو مخططات أو مواصفات أو مستندات أو معلومات خاصة بمشروعك، فإنك تقرّ، في حدود علمك وصلاحياتك، بأن لديك الحق أو الصلاحية اللازمة لمشاركتها معنا للغرض المطلوب.
            </p>
            <p>
              وتأذن لبيستوليكس باستخدام هذه المواد بالقدر الضروري لدراسة طلبك وتقييم متطلباته، وإعداد العروض الفنية والتجارية، ومشاركة المعلومات اللازمة مع المصنّع أو المورد أو الشريك الفني عند الحاجة، وتنفيذ المنتجات أو الخدمات المتفق عليها.
            </p>
            <p class="font-medium text-gray-900 dark:text-gray-100">
              لا تنتقل ملكية المواد التي ترسلها إلى بيستوليكس لمجرد إرسالها. وتُعالَج أي بيانات شخصية تتضمنها وفقاً لـ<NuxtLink :to="localePath('/privacy')" class="text-amber-600 dark:text-amber-400 font-semibold hover:underline">سياسة الخصوصية</NuxtLink>.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 13. الملكية الفكرية والعلامات التجارية -->
          <section id="ar-sec-13" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              13. الملكية الفكرية والعلامات التجارية
            </h2>
            <p>
              المحتوى الأصلي المملوك لبيستوليكس، ومنه النصوص والتصاميم والعناصر الرسومية والمواد التسويقية والصور التي تملك الشركة حقوق استخدامها وترتيب محتوى الموقع وعرضه، محمي بموجب قوانين الملكية الفكرية وحقوق المؤلف والعلامات التجارية المعمول بها في دولة قطر.
            </p>
            <p>
              اسم <strong class="text-gray-900 dark:text-white">بيستوليكس / Bestolex</strong> وشعار الشركة من العناصر الخاصة بها، ولا يجوز استخدامهما دون إذن، أو على نحو يوحي بوجود علاقة أو اعتماد أو تمثيل غير موجود.
            </p>
            <p>
              ويحتوي الموقع أيضاً على أسماء تجارية وعلامات وشعارات وصور منتجات وكتالوجات ومخططات ومواصفات فنية تعود إلى المصنّعين والموردين والشركاء، ومنهم SAB TECH. ظهور هذه العلامات على الموقع <strong class="text-gray-900 dark:text-white">لا يعني أن بيستوليكس تملكها</strong>، وتظل حقوقها لأصحابها، وتُستخدم لتحديد المنتجات في إطار العلاقات التجارية المشروعة.
            </p>
            <p class="text-sm sm:text-base text-gray-600 dark:text-gray-400">
              يُسمح بعرض صفحات الموقع وطباعتها للاستخدام الشخصي أو الداخلي المشروع، مع الإبقاء على إشارات الملكية. ولا يجوز نسخ المحتوى المحمي أو إعادة نشره أو توزيعه أو تعديله أو استغلاله تجارياً دون إذن صاحب الحق، باستثناء ما يسمح به القانون.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 14. الاستخدام المقبول وأمن الموقع -->
          <section id="ar-sec-14" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              14. الاستخدام المقبول وأمن الموقع
            </h2>
            <p>يجب استخدام الموقع لأغراض مشروعة فقط. ويُحظر على المستخدم، من بين أمور أخرى:</p>
            <ul class="list-disc list-inside space-y-2 ps-2 sm:ps-4">
              <li>مخالفة القوانين أو الأنظمة أو النظام العام والآداب العامة في دولة قطر.</li>
              <li>تقديم معلومات كاذبة أو مضللة عمداً، أو انتحال شخصية فرد أو جهة أخرى.</li>
              <li>محاولة الوصول غير المصرح به إلى الموقع أو أنظمته أو خوادمه، أو اختبار تدابيره الأمنية أو تجاوزها دون إذن صريح.</li>
              <li>تعطيل الموقع أو التأثير على تشغيله، أو إرسال برمجيات ضارة أو أكواد خبيثة.</li>
              <li>استخدام أدوات آلية لجمع محتوى الموقع أو بياناته، أو بطريقة تسبب عبئاً غير معقول على بنيته التحتية.</li>
              <li>جمع البيانات الشخصية من الموقع بوسائل غير مشروعة.</li>
              <li>إرسال رسائل دعائية أو مزعجة عبر نماذج الموقع أو قنوات التواصل.</li>
              <li>استخدام محتوى الموقع لأغراض تجارية منافسة، أو بطريقة تنتهك حقوق بيستوليكس أو حقوق الغير.</li>
            </ul>
            <p class="p-4 rounded-2xl bg-amber-500/10 border border-amber-500/20 text-gray-900 dark:text-white font-medium">
              <strong>يحق لبيستوليكس تقييد وصول أي مستخدم يخالف هذه الشروط أو منعه</strong>، واتخاذ الإجراءات الفنية والقانونية المناسبة عند اكتشاف استخدام غير مشروع أو يهدد أمن الموقع أو أنظمته أو بياناته أو مستخدميه.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 15. الروابط وخدمات الأطراف الأخرى -->
          <section id="ar-sec-15" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              15. الروابط وخدمات الأطراف الأخرى
            </h2>
            <p>
              يحتوي الموقع على روابط إلى مواقع ومنصات تديرها أطراف أخرى، مثل واتساب وإنستغرام وفيسبوك، ومواقع المصنّعين والموردين والشركاء. وتُوفَّر هذه الروابط للتسهيل والتواصل.
            </p>
            <p>
              كما يعتمد الموقع على خدمات يقدمها أطراف ثالثة لوظائف مثل الاستضافة والتحليلات وإدارة الوسوم والبريد الإلكتروني والحماية التقنية.
            </p>
            <p class="text-sm sm:text-base text-gray-600 dark:text-gray-400">
              لا تتحكم بيستوليكس في المواقع والخدمات الخارجية، ولا تتحمل المسؤولية عن محتواها أو أمنها أو سياساتها. ويخضع استخدامك لها لشروط مقدميها وسياسات الخصوصية الخاصة بهم.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 16. الخصوصية وملفات تعريف الارتباط -->
          <section id="ar-sec-16" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              16. الخصوصية وملفات تعريف الارتباط
            </h2>
            <p>
              توضح <NuxtLink :to="localePath('/privacy')" class="text-amber-600 dark:text-amber-400 font-semibold hover:underline">سياسة الخصوصية</NuxtLink> كيفية جمع البيانات الشخصية واستخدامها وحمايتها ومشاركتها، واستخدام ملفات تعريف الارتباط والتقنيات المشابهة.
            </p>
            <div class="p-5 rounded-2xl bg-gradient-to-r from-amber-500/10 via-orange-500/10 to-amber-500/10 border border-amber-500/30 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
              <div>
                <p class="text-sm sm:text-base text-gray-700 dark:text-gray-200">
                  ويمكنك مراجعة اختياراتك بشأن ملفات تعريف الارتباط أو تعديلها في أي وقت عبر زر <strong>«إعدادات ملفات تعريف الارتباط»</strong> المتاح على الموقع.
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
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 17. توفر الموقع وتعديله -->
          <section id="ar-sec-17" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              17. توفر الموقع وتعديله
            </h2>
            <p>
              يُقدَّم الموقع ومحتواه "كما هو" و"حسب التوفر"، في حدود ما يسمح به القانون. ونسعى إلى تشغيله بصورة مناسبة وآمنة، لكننا لا نضمن أن يكون متاحاً بشكل مستمر دون انقطاع، أو خالياً تماماً من الأخطاء التقنية، أو متوافقاً مع جميع الأجهزة والبرامج في كل الأوقات.
            </p>
            <p>يجوز لبيستوليكس في أي وقت، وفي حدود القانون:</p>
            <ul class="list-disc list-inside space-y-2 ps-2 sm:ps-4">
              <li>تعليق الموقع أو بعض وظائفه مؤقتاً لأغراض الصيانة أو التطوير أو التحديث أو الأمن، أو بسبب أعطال فنية أو ظروف خارجة عن سيطرتها المعقولة.</li>
              <li>تحديث المحتوى والمواصفات، أو إضافة منتجات وخدمات أو إيقافها، أو تعديل التصميم، أو تغيير وظائف الموقع أو إزالتها.</li>
            </ul>
            <p class="text-sm sm:text-base text-gray-600 dark:text-gray-400">
              ولا يعني عرض منتج أو خدمة على الموقع سابقاً استمرار توفره بصورة دائمة.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 18. حدود المسؤولية -->
          <section id="ar-sec-18" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              18. حدود المسؤولية
            </h2>
            <p>في حدود ما يسمح به القانون المعمول به في دولة قطر، لا تتحمل بيستوليكس المسؤولية عن:</p>
            <ul class="list-disc list-inside space-y-2 ps-2 sm:ps-4">
              <li>أي خسارة أو ضرر ينشأ عن الاعتماد على معلومات عامة منشورة على الموقع دون الحصول على تأكيد فني أو تجاري معتمد.</li>
              <li>أي خسارة تنشأ عن استخدام مواقع أو خدمات خارجية يتم الوصول إليها من خلال روابط على الموقع.</li>
              <li>أي انقطاع أو تعذّر في استخدام الموقع لأسباب خارجة عن سيطرتها المعقولة.</li>
              <li>أي خسارة تنشأ عن استخدام الموقع بالمخالفة لهذه الشروط.</li>
              <li>أي أضرار غير مباشرة أو تبعية، أو خسارة أرباح أو بيانات أو فرص تجارية، تنشأ عن استخدام الموقع أو تعذّر استخدامه.</li>
            </ul>
            <p class="pt-2">ولا يهدف أي حكم في هذه الشروط إلى استبعاد أو الحد من:</p>
            <ul class="list-disc list-inside space-y-2 ps-2 sm:ps-4">
              <li>المسؤولية عن الغش أو الخطأ الجسيم.</li>
              <li>أي مسؤولية لا يجوز قانوناً استبعادها أو تقييدها.</li>
              <li>الحقوق والالتزامات المنصوص عليها في العقود المبرمة مع العملاء.</li>
            </ul>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 19. المسؤولية عن إساءة استخدام الموقع -->
          <section id="ar-sec-19" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              19. المسؤولية عن إساءة استخدام الموقع
            </h2>
            <p>
              في حدود ما يسمح به القانون، يكون المستخدم مسؤولاً عن الخسائر والمطالبات والمصاريف المعقولة التي تتحملها بيستوليكس كنتيجة مباشرة لاستخدامه غير المشروع للموقع، أو انتهاكه المتعمد لهذه الشروط، أو تعديه على حقوق بيستوليكس أو حقوق الغير.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 20. حقوق المستهلك -->
          <section id="ar-sec-20" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              20. حقوق المستهلك
            </h2>
            <p>
              تعمل بيستوليكس بصورة أساسية في مجال التعاملات بين الشركات والمؤسسات (B2B). ومع ذلك، عندما يكون قانون حماية المستهلك أو أي أحكام إلزامية أخرى منطبقة على معاملة محددة، لا تُفسَّر هذه الشروط على أنها تستبعد أو تقلل من أي حق لا يجوز قانوناً الاتفاق على استبعاده أو الانتقاص منه.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 21. تعديل الشروط وأحكام عامة -->
          <section id="ar-sec-21" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              21. تعديل الشروط وأحكام عامة
            </h2>
            <div class="space-y-3">
              <p>
                <strong class="text-gray-900 dark:text-white">تعديل الشروط:</strong> 
                قد نحدّث هذه الشروط من وقت لآخر لتعكس التغيرات في الموقع أو الخدمات أو نشاط الشركة أو التطورات التقنية أو المتطلبات القانونية والتنظيمية. تُنشر النسخة المحدثة على هذه الصفحة مع تعديل تاريخ "آخر تحديث"، وتسري من تاريخ نشرها أو من التاريخ المحدد فيها.
              </p>
              <p>
                <strong class="text-gray-900 dark:text-white">قابلية الفصل:</strong> 
                إذا اعتُبر أي حكم من هذه الشروط باطلاً أو غير قابل للتنفيذ، فلا يؤثر ذلك على باقي الأحكام، ويُفسَّر الحكم المتأثر، بالقدر الممكن قانوناً، بما يحقق غرضه المشروع.
              </p>
              <p>
                <strong class="text-gray-900 dark:text-white">عدم التنازل:</strong> 
                عدم ممارسة بيستوليكس لأي حق أو تأخرها في ممارسته لا يُعدّ تنازلاً عنه.
              </p>
              <p>
                <strong class="text-gray-900 dark:text-white">اللغة:</strong> 
                تتوفر هذه الشروط باللغتين العربية والإنجليزية. وفي حال وجود أي اختلاف أو تعارض في التفسير بين النسختين، يُعتد بالنص العربي ما لم يقتض القانون خلاف ذلك.
              </p>
            </div>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 22. القانون الواجب التطبيق والاختصاص القضائي -->
          <section id="ar-sec-22" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              22. القانون الواجب التطبيق والاختصاص القضائي
            </h2>
            <p>
              تخضع هذه الشروط للقوانين واللوائح المعمول بها في دولة قطر وتُفسَّر وفقاً لها.
            </p>
            <p>
              ويخضع أي نزاع ينشأ عن استخدام الموقع ولا تتم تسويته ودياً لاختصاص المحاكم المختصة في دولة قطر، مع مراعاة أي أحكام قانونية إلزامية واجبة التطبيق.
            </p>
            <p class="text-sm sm:text-base text-gray-600 dark:text-gray-400">
              ولا يؤثر هذا البند على أي اتفاق مكتوب لتسوية النزاعات أو تحديد الاختصاص وارد في عقد أو اتفاق منفصل يتعلق بمعاملة تجارية محددة.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 23. معلومات الشركة والتواصل -->
          <section id="ar-sec-23" class="space-y-6">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              23. معلومات الشركة والتواصل
            </h2>
            <p>لأي استفسار يتعلق بالموقع أو بهذه الشروط:</p>
            
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
          
          <!-- 1. Introduction and Acceptance -->
          <section id="en-sec-1" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              1. Introduction and Acceptance
            </h2>
            <p>
              Welcome to the website of Bestolex Trading of Heavy Equipment and Machinery W.L.L, referred to in these Terms as "Bestolex", "the Company" or "we".
            </p>
            <p>
              These Terms govern your access to the website 
              <a href="https://www.bestolex.com" target="_blank" rel="noopener noreferrer" class="text-amber-600 dark:text-amber-400 font-semibold hover:underline">www.bestolex.com</a> ("the Website") and your use of the content, information, forms, functions and electronic services available through it.
            </p>
            <p>
              By using the Website, you acknowledge that you have read, understood and agreed to be bound by these Terms. If you do not agree, please do not use the Website.
            </p>
            <p>
              If you use the Website on behalf of a company, institution or other organisation, you confirm that you have appropriate authority to communicate and act on its behalf within the scope of the relevant use or request.
            </p>
            <p>
              Processing of personal data through the Website is governed by our 
              <NuxtLink :to="localePath('/privacy')" class="text-amber-600 dark:text-amber-400 font-semibold hover:underline">Privacy Policy</NuxtLink>.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 2. Purpose of the Website -->
          <section id="en-sec-2" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              2. Purpose of the Website
            </h2>
            <p>
              The Website introduces Bestolex, its activities, products, services, commercial and technical solutions and the sectors it serves. It enables customers, suppliers and partners to submit enquiries, request quotations and technical information, book appointments and site surveys, register for training programmes where available, and contact the Company through its official channels.
            </p>
            <div class="p-4 rounded-2xl bg-gray-100 dark:bg-gray-800/60 border border-gray-200 dark:border-gray-700/60 text-sm sm:text-base font-medium">
              The Website is intended primarily for companies, institutions, government entities, professionals and business customers.
            </div>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 3. Nature of Content and Accuracy of Information -->
          <section id="en-sec-3" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              3. Nature of Content and Accuracy of Information
            </h2>
            <p>
              Unless Bestolex expressly states otherwise, information published on the Website, including product descriptions, specifications, images, drawings, catalogues, technical data, suggested applications and service information, is provided <strong class="text-gray-900 dark:text-white">for introductory and general information purposes only</strong>. It does not by itself constitute an offer to sell, a contractual commitment, engineering or technical advice specific to your project, or a guarantee that a product or system is suitable for a particular use without assessing the project's requirements.
            </p>
            <p>We make reasonable efforts to keep information accurate and up to date. However:</p>
            <ul class="list-disc list-inside space-y-3 ps-2 sm:ps-4">
              <li>
                <strong class="text-gray-900 dark:text-white">Manufacturers and suppliers:</strong> may change the design, specifications, dimensions, materials and components, capacities, models, control systems, accessories, finishes, country of origin or availability without prior notice and before the Website is updated.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">Images, drawings and videos:</strong> are illustrative; the actual product may differ in colour, size, equipment, external appearance, model or final configuration. They should not be relied on alone to determine specifications or scope of supply.
              </li>
              <li>
                <strong class="text-gray-900 dark:text-white">Displaying a product on the Website:</strong> does not necessarily mean it is immediately available in stock.
              </li>
            </ul>
            <p class="p-4 rounded-2xl bg-amber-500/5 dark:bg-amber-500/10 border border-amber-500/20 text-sm sm:text-base">
              If any information is essential to a purchasing decision, such as price, capacity, dimensions, load capacity, country of origin, certifications, lead time or compatibility with specific project requirements, it must be confirmed in the approved technical or commercial offer or the manufacturer's documents for the transaction before purchase or contracting.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 4. Used Equipment -->
          <section id="en-sec-4" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              4. Used Equipment
            </h2>
            <p>
              Where used equipment or machinery is listed on the Website, information about its condition, year of manufacture, operating hours, specifications or equipment is based on the information and records available to us at the time of publication, unless stated otherwise.
            </p>
            <p>
              The actual condition, scope of inspection, any warranties or exclusions, and terms of sale are set out in the quotation, inspection report or contract for the transaction.
            </p>
            <p>
              The customer may request a viewing or independent inspection before completing the purchase, where available and appropriate.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 5. Enquiries, Contract Formation and Precedence of Documents -->
          <section id="en-sec-5" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              5. Enquiries, Contract Formation and Precedence of Documents
            </h2>
            <p>
              Browsing the Website, submitting an enquiry, completing a form, or requesting information or a quotation does not, by itself, create any contractual obligation on Bestolex to accept the request, supply a product or perform a service. The Company may request additional information, documents or specifications before preparing a quotation or technical proposal.
            </p>
            <p>
              Quotations are subject to the validity period, terms, specifications and exclusions stated in them. Products or services are not reserved or confirmed unless Bestolex confirms this in accordance with agreed commercial procedures.
            </p>
            <p>
              A contractual obligation may arise under an accepted quotation, a contract, a purchase order, approved electronic approvals and correspondence, or any other means meeting applicable legal and commercial requirements. The nature of the obligation depends on the content of the documents and correspondence for each transaction.
            </p>
            <p class="p-4 rounded-2xl bg-amber-500/10 border border-amber-500/20 text-gray-900 dark:text-white font-medium">
              These Terms govern use of the Website only and do not replace the terms of each transaction or project. Where a quotation, technical offer, purchase order, supply contract, work order, warranty terms, maintenance agreement or any approved contractual document is issued, <strong>its provisions prevail</strong> for that transaction, including terms of supply, payment, delivery, installation, commissioning, warranty and maintenance, in the event of conflict with these Terms or with information published on the Website.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 6. Prices, Availability and Delivery Times -->
          <section id="en-sec-6" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              6. Prices, Availability and Delivery Times
            </h2>
            <p>
              Unless expressly stated otherwise, the Website is not a binding price list. Prices and availability depend on factors including product specifications, options, accessories and country of origin; manufacturer or supplier prices and exchange rates; transport, shipping, insurance, customs duties and taxes where applicable; installation, commissioning and project requirements; and stock status and market conditions.
            </p>
            <p>
              The <strong class="text-gray-900 dark:text-white">binding price</strong> for any transaction is the price stated in its quotation or agreement, subject to its terms and validity period.
            </p>
            <p>
              Any supply or delivery times published generally on the Website are <strong class="text-gray-900 dark:text-white">estimates</strong> unless confirmed in a commercial or contractual document for the transaction. Delivery times may be affected by factors such as manufacturer production, product availability, international shipping, customs clearance, procedures of competent authorities, delays by suppliers or carriers, and circumstances beyond the Company's reasonable control.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 7. Technical Information and Site Surveys -->
          <section id="en-sec-7" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              7. Technical Information and Site Surveys
            </h2>
            <p>
              Technical and engineering information and suggested applications published on the Website are general in nature, unless expressly prepared for a specific project based on its technical data.
            </p>
            <p>
              Where the nature of the project requires, this information does not replace a site survey, needs assessment, approved drawings, engineering calculations and load data, assessment of operating conditions and electrical and mechanical requirements, or safety and regulatory requirements.
            </p>
            <p>
              The customer is responsible for providing Bestolex with accurate and sufficient project information when requesting a technical recommendation or customised offer.
            </p>
            <div class="p-4 rounded-2xl bg-gray-50 dark:bg-gray-800/80 border border-gray-200 dark:border-gray-700/80 space-y-2">
              <h3 class="font-bold text-gray-900 dark:text-white">Appointments and site surveys:</h3>
              <p class="text-sm sm:text-base text-gray-600 dark:text-gray-300">
                Requests submitted through the Website are not confirmed until the Bestolex team confirms them. The requester must provide accurate and complete information, be authorised to request the visit, provide safe and lawful access to the site, and inform us in advance of any security or safety requirements or permits needed for entry. Appointments may be rescheduled where operational circumstances or site requirements so require.
              </p>
            </div>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 8. Installation, Operation and Safety -->
          <section id="en-sec-8" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              8. Installation, Operation and Safety
            </h2>
            <p>
              Displaying a product on the Website does not mean that installation, commissioning, training or maintenance is automatically included in its price. The scope of these services, where applicable, is defined in the quotation or contract for the transaction.
            </p>
            <p>
              Information published on the Website does not replace the manufacturer's operation and maintenance manuals, certified training, or the safety requirements applicable in the State of Qatar.
            </p>
            <p>
              Equipment must be installed, operated and maintained in accordance with the manufacturer's instructions, operating manuals, approved technical instructions, safety requirements and applicable laws and regulations, by qualified and trained persons where the nature of the equipment so requires.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 9. Warranty -->
          <section id="en-sec-9" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              9. Warranty
            </h2>
            <p>
              Warranties, where available, are subject to the terms set out in the quotation, contract, warranty certificate, manufacturer's or supplier's terms, or commercial documents for the transaction. Warranty period, scope, conditions and exclusions vary by product, manufacturer and nature of the project.
            </p>
            <p>
              No general description published on the Website constitutes an additional warranty beyond the written and approved warranty for the transaction. This clause does not affect any mandatory rights that cannot lawfully be excluded or restricted.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 10. Training and Training Certificates -->
          <section id="en-sec-10" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              10. Training and Training Certificates
            </h2>
            <p>
              Each course or training programme offered by Bestolex, alone or in cooperation with its partners, is subject to its own terms, including where applicable: content, schedule, venue, fees, registration conditions, attendance requirements, cancellation or rescheduling, and certificate issuance conditions.
            </p>
            <p>
              Listing a training programme on the Website does not guarantee its continued availability or that it will be held on a particular date, unless the registration or date has been formally confirmed. The issuing body of any training certificate is identified in the programme's own documents.
            </p>
            <p class="text-sm sm:text-base text-gray-600 dark:text-gray-400 italic">
              Training materials may not be recorded, copied, republished or used commercially without written permission from the rights holder.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 11. Product and Manufacturer Certifications -->
          <section id="en-sec-11" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              11. Product and Manufacturer Certifications
            </h2>
            <p>
              The Website may refer to certificates, standards or approvals associated with a particular product, manufacturer or system. Such certifications belong to the entity or product specified in their official documents and <strong class="text-gray-900 dark:text-white">are not attributed to Bestolex</strong> unless issued directly in the Company's name.
            </p>
            <p>
              Refer to the official product or manufacturer documents to confirm the scope of any certificate or approval and its applicability to the specific product.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 12. Materials and Information You Send Us -->
          <section id="en-sec-12" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              12. Materials and Information You Send Us
            </h2>
            <p>
              When you send photos, drawings, specifications, documents or project information, you confirm, to the best of your knowledge and authority, that you have the right or authority to share them with us for the requested purpose.
            </p>
            <p>
              You permit Bestolex to use these materials to the extent necessary to assess your request and its requirements, prepare technical and commercial offers, share necessary information with the manufacturer, supplier or technical partner where needed, and deliver the agreed products or services.
            </p>
            <p class="font-medium text-gray-900 dark:text-gray-100">
              Ownership of materials you send does not transfer to Bestolex merely by sending them. Any personal data they contain is processed in accordance with our 
              <NuxtLink :to="localePath('/privacy')" class="text-amber-600 dark:text-amber-400 font-semibold hover:underline">Privacy Policy</NuxtLink>.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 13. Intellectual Property and Trademarks -->
          <section id="en-sec-13" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              13. Intellectual Property and Trademarks
            </h2>
            <p>
              Original content owned by Bestolex, including text, designs, graphic elements, marketing materials, images the Company has the right to use, and the arrangement and presentation of Website content, is protected under the intellectual property, copyright and trademark laws applicable in the State of Qatar.
            </p>
            <p>
              The name <strong class="text-gray-900 dark:text-white">Bestolex / بيستوليكس</strong> and the Company logo belong to the Company and may not be used without permission, or in a way that suggests a relationship, endorsement or representation that does not exist.
            </p>
            <p>
              The Website also contains trade names, trademarks, logos, product images, catalogues, drawings and technical specifications belonging to manufacturers, suppliers and partners, including SAB TECH. The appearance of such marks on the Website <strong class="text-gray-900 dark:text-white">does not mean Bestolex owns them</strong>; their rights remain with their respective owners, and they are used to identify products within legitimate business relationships.
            </p>
            <p class="text-sm sm:text-base text-gray-600 dark:text-gray-400">
              You may view and print Website pages for legitimate personal or internal use, provided ownership notices are retained. Protected content may not be copied, republished, distributed, modified or commercially exploited without the rights holder's permission, except as permitted by law.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 14. Acceptable Use and Website Security -->
          <section id="en-sec-14" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              14. Acceptable Use and Website Security
            </h2>
            <p>The Website must be used for lawful purposes only. Users are prohibited from, among other things:</p>
            <ul class="list-disc list-inside space-y-2 ps-2 sm:ps-4">
              <li>Violating the laws, regulations, public order or public morals of the State of Qatar.</li>
              <li>Knowingly providing false or misleading information, or impersonating another individual or entity.</li>
              <li>Attempting unauthorised access to the Website, its systems or servers, or testing or bypassing its security measures without express permission.</li>
              <li>Disrupting or affecting the Website's operation, or sending malware or malicious code.</li>
              <li>Using automated tools to extract Website content or data, or in a way that places an unreasonable load on its infrastructure.</li>
              <li>Collecting personal data from the Website by unlawful means.</li>
              <li>Sending promotional or unsolicited messages through Website forms or contact channels.</li>
              <li>Using Website content for competing commercial purposes, or in a way that infringes the rights of Bestolex or third parties.</li>
            </ul>
            <p class="p-4 rounded-2xl bg-amber-500/10 border border-amber-500/20 text-gray-900 dark:text-white font-medium">
              <strong>Bestolex may restrict or block access for any user who breaches these Terms</strong>, and take appropriate technical and legal action upon detecting unlawful use or activity that threatens the security of the Website, its systems, data or users.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 15. Links and Third-Party Services -->
          <section id="en-sec-15" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              15. Links and Third-Party Services
            </h2>
            <p>
              The Website contains links to websites and platforms operated by third parties, such as WhatsApp, Instagram and Facebook, and the websites of manufacturers, suppliers and partners. These links are provided for convenience and communication.
            </p>
            <p>
              The Website also relies on services provided by third parties for functions such as hosting, analytics, tag management, email and technical protection.
            </p>
            <p class="text-sm sm:text-base text-gray-600 dark:text-gray-400">
              Bestolex does not control external websites and services and is not responsible for their content, security or policies. Your use of them is subject to their providers' terms and privacy policies.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 16. Privacy and Cookies -->
          <section id="en-sec-16" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              16. Privacy and Cookies
            </h2>
            <p>
              Our <NuxtLink :to="localePath('/privacy')" class="text-amber-600 dark:text-amber-400 font-semibold hover:underline">Privacy Policy</NuxtLink> explains how personal data is collected, used, protected and shared, and how cookies and similar technologies are used.
            </p>
            <div class="p-5 rounded-2xl bg-gradient-to-r from-amber-500/10 via-orange-500/10 to-amber-500/10 border border-amber-500/30 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
              <div>
                <p class="text-sm sm:text-base text-gray-700 dark:text-gray-200">
                  You can review or change your cookie choices at any time using the <strong>"Cookie Settings"</strong> button available on the Website.
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
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 17. Website Availability and Changes -->
          <section id="en-sec-17" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              17. Website Availability and Changes
            </h2>
            <p>
              The Website and its content are provided "as is" and "as available", to the extent permitted by law. We aim to operate it appropriately and securely, but we do not guarantee that it will be continuously available without interruption, entirely free of technical errors, or compatible with all devices and software at all times.
            </p>
            <p>Bestolex may at any time, within the limits of the law:</p>
            <ul class="list-disc list-inside space-y-2 ps-2 sm:ps-4">
              <li>Temporarily suspend the Website or some of its functions for maintenance, development, updates or security, or due to technical faults or circumstances beyond its reasonable control.</li>
              <li>Update content and specifications, add or discontinue products and services, modify the design, or change or remove Website functions.</li>
            </ul>
            <p class="text-sm sm:text-base text-gray-600 dark:text-gray-400">
              The past display of a product or service on the Website does not mean it will remain permanently available.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 18. Limitation of Liability -->
          <section id="en-sec-18" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              18. Limitation of Liability
            </h2>
            <p>To the extent permitted by the laws applicable in the State of Qatar, Bestolex is not liable for:</p>
            <ul class="list-disc list-inside space-y-2 ps-2 sm:ps-4">
              <li>Any loss or damage arising from reliance on general information published on the Website without obtaining approved technical or commercial confirmation.</li>
              <li>Any loss arising from use of external websites or services accessed through links on the Website.</li>
              <li>Any interruption or unavailability of the Website for reasons beyond its reasonable control.</li>
              <li>Any loss arising from use of the Website in breach of these Terms.</li>
              <li>Any indirect or consequential damages, or loss of profits, data or business opportunities, arising from use of or inability to use the Website.</li>
            </ul>
            <p class="pt-2">Nothing in these Terms is intended to exclude or limit:</p>
            <ul class="list-disc list-inside space-y-2 ps-2 sm:ps-4">
              <li>Liability for fraud or gross negligence.</li>
              <li>Any liability that cannot lawfully be excluded or restricted.</li>
              <li>Rights and obligations set out in contracts with customers.</li>
            </ul>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 19. Liability for Misuse of the Website -->
          <section id="en-sec-19" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              19. Liability for Misuse of the Website
            </h2>
            <p>
              To the extent permitted by law, the user is responsible for losses, claims and reasonable expenses incurred by Bestolex as a direct result of the user's unlawful use of the Website, intentional breach of these Terms, or infringement of the rights of Bestolex or third parties.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 20. Consumer Rights -->
          <section id="en-sec-20" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              20. Consumer Rights
            </h2>
            <p>
              Bestolex operates primarily in business-to-business (B2B) transactions. However, where consumer protection law or other mandatory provisions apply to a specific transaction, these Terms shall not be interpreted as excluding or reducing any right that cannot lawfully be excluded or diminished by agreement.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 21. Changes to These Terms and General Provisions -->
          <section id="en-sec-21" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              21. Changes to These Terms and General Provisions
            </h2>
            <div class="space-y-3">
              <p>
                <strong class="text-gray-900 dark:text-white">Changes to these Terms:</strong> 
                We may update these Terms from time to time to reflect changes in the Website, services, the Company's activities, technological developments, or legal and regulatory requirements. The updated version will be published on this page with a revised "Last Updated" date and takes effect from its publication date or the date stated in it.
              </p>
              <p>
                <strong class="text-gray-900 dark:text-white">Severability:</strong> 
                If any provision of these Terms is found invalid or unenforceable, the remaining provisions are unaffected, and the affected provision shall be interpreted, to the extent legally possible, to achieve its legitimate purpose.
              </p>
              <p>
                <strong class="text-gray-900 dark:text-white">No waiver:</strong> 
                Bestolex's failure or delay in exercising any right does not constitute a waiver of that right.
              </p>
              <p>
                <strong class="text-gray-900 dark:text-white">Language:</strong> 
                These Terms are available in Arabic and English. In the event of any difference or conflict in interpretation between the two versions, the Arabic text prevails unless the law requires otherwise.
              </p>
            </div>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 22. Governing Law and Jurisdiction -->
          <section id="en-sec-22" class="space-y-4">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              22. Governing Law and Jurisdiction
            </h2>
            <p>
              These Terms are governed by and construed in accordance with the laws and regulations applicable in the State of Qatar.
            </p>
            <p>
              Any dispute arising from use of the Website that is not resolved amicably shall be subject to the jurisdiction of the competent courts of the State of Qatar, subject to any applicable mandatory legal provisions.
            </p>
            <p class="text-sm sm:text-base text-gray-600 dark:text-gray-400">
              This clause does not affect any written dispute resolution or jurisdiction agreement contained in a separate contract or agreement relating to a specific commercial transaction.
            </p>
          </section>

          <hr class="border-gray-200 dark:border-gray-800" />

          <!-- 23. Company Information and Contact -->
          <section id="en-sec-23" class="space-y-6">
            <h2 class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
              <span class="w-2 h-7 bg-amber-500 rounded-full inline-block"></span>
              23. Company Information and Contact
            </h2>
            <p>For any enquiry about the Website or these Terms:</p>
            
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
  title: isAr.value ? 'شروط الاستخدام | بيستوليكس' : 'Terms of Use | Bestolex',
  description: isAr.value 
    ? 'شروط وأحكام استخدام موقع وخدمات شركة بيستوليكس لتجارة الآلات والمعدات الثقيلة في دولة قطر.'
    : 'Terms of Use for Bestolex Trading of Heavy Equipment and Machinery website and services in Qatar.',
  robots: 'index, follow'
})
</script>
