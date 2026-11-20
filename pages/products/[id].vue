<template>
  <div class="product-page bg-gray-50 dark:bg-gray-900 min-h-screen transition-colors duration-300">
    
    <!-- Loading State -->
    <div v-if="!product" class="min-h-screen flex items-center justify-center">
      <div class="text-center">
        <div class="w-16 h-16 border-4 border-gray-200 dark:border-gray-700 border-t-primary rounded-full animate-spin mx-auto mb-6"></div>
        <p class="text-gray-500 dark:text-gray-400 text-lg">{{ locale === 'ar' ? 'جاري التحميل...' : 'Loading...' }}</p>
      </div>
    </div>

    <div v-else>
      <!-- General Hero Banner -->
      <section class="relative w-full h-[35vh] sm:h-[45vh] md:h-[50vh] max-h-[550px] flex items-center justify-center overflow-hidden bg-black">
        <NuxtImg 
          :src="product.coverImage || product.images?.[0] || product.image" 
          alt="Banner" 
          class="absolute inset-0 w-full h-full object-cover object-center opacity-90 transition-all duration-700"
          format="webp"
          loading="eager"
        />
        <!-- Subtle dark gradient overlay for text readability -->
        <div class="absolute inset-0 bg-gradient-to-t from-[#121c2d] via-black/30 to-black/40"></div>
        
        <div class="relative z-10 text-center px-4" data-aos="fade-up">
          <p class="text-3xl md:text-5xl lg:text-6xl font-black text-white drop-shadow-[0_4px_12px_rgba(0,0,0,0.8)] tracking-tight">
            {{ product.name[locale] }}
          </p>
        </div>
      </section>

      <!-- Hero Product Section (Restored Original Layout but Full Width Carousel) -->
      <section class="bg-[#121c2d] py-12 md:py-20 relative overflow-hidden">
        <!-- Subtle Pattern Background -->
        <div class="absolute inset-0 opacity-10" style="background-image: radial-gradient(#ffffff 1px, transparent 1px); background-size: 24px 24px;"></div>
        
        <div class="container mx-auto px-4 md:px-8 relative z-10">
          <div class="flex flex-col gap-12 lg:gap-16 items-center">
            
            <!-- Product Info & Stats (Centered and Full Width) -->
            <div class="w-full lg:w-10/12 xl:w-8/12 flex flex-col items-center text-center" data-aos="fade-down">
              <!-- Breadcrumb -->
              <div class="flex items-center justify-center gap-2 text-gray-400 text-sm md:text-base mb-6 font-medium flex-wrap">
                <NuxtLink :to="localePath('/')" class="hover:text-white transition">{{ locale === 'ar' ? 'الرئيسية' : 'Home' }}</NuxtLink>
                <span>/</span>
                <NuxtLink :to="localePath('/products')" class="hover:text-white transition">{{ locale === 'ar' ? 'المنتجات' : 'Products' }}</NuxtLink>
                <span>/</span>
                <span class="text-[#E99E15]">{{ product.name[locale] }}</span>
              </div>
              
              <!-- Badge -->
              <div class="inline-block bg-gray-800/80 border border-gray-700 text-[#E99E15] rounded-full px-5 py-2 text-sm font-bold mb-6">
                <span class="w-2 h-2 rounded-full bg-[#E99E15] inline-block rtl:ml-2 ltr:mr-2"></span>
                {{ product.categoryTitle?.[locale] || (locale === 'ar' ? 'المخلفات وإعادة التدوير' : 'Waste & Recycling') }}
              </div>
              
              <!-- Title -->
              <h1 class="text-4xl md:text-5xl lg:text-6xl font-black text-white mb-6 leading-tight">
                {{ product.name[locale] }}
              </h1>
              
              <div class="w-20 h-1 bg-[#E99E15] mb-8"></div>

              <!-- At a glance: short answer-first summary (GEO) -->
              <div v-if="product.summary && product.summary[locale]" class="w-full max-w-3xl bg-white/5 border border-[#E99E15]/40 rounded-2xl px-6 py-5 mb-8 text-start">
                <p class="text-[#E99E15] text-sm font-black mb-2">{{ locale === 'ar' ? 'باختصار' : 'At a glance' }}</p>
                <p class="text-white text-base md:text-lg leading-relaxed">{{ product.summary[locale] }}</p>
              </div>
              
              <!-- Description -->
              <p class="text-lg md:text-xl text-gray-300 leading-relaxed mb-10 whitespace-pre-line text-center">
                {{ product.description ? product.description[locale] : '' }}
              </p>
              
              <!-- Stats Cards -->
              <div v-if="product.stats && product.stats[locale]" class="grid grid-cols-2 md:grid-cols-3 gap-4 mb-10 w-full">
                <div v-for="(stat, i) in product.stats[locale]" :key="i" class="bg-white/5 border border-white/10 rounded-2xl p-5 text-center backdrop-blur-sm hover:bg-white/10 transition">
                  <div class="text-[#E99E15] font-black text-2xl md:text-3xl mb-1">{{ stat.value }}</div>
                  <div class="text-gray-300 text-sm font-medium">{{ stat.label }}</div>
                </div>
              </div>
              
              <!-- Buttons -->
              <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <button @click="scrollToQuote" class="bg-[#E99E15] text-white px-8 py-4 rounded-xl font-bold text-lg hover:bg-orange-500 transition shadow-lg hover:shadow-[#E99E15]/40 flex items-center justify-center gap-3">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" /></svg>
                  {{ locale === 'ar' ? 'طلب عرض سعر' : 'Request a Quote' }}
                </button>
                <a :href="whatsappHref" target="_blank" rel="noopener noreferrer" @click="trackWhatsapp" class="bg-[#25D366] text-white px-8 py-4 rounded-xl font-bold text-lg hover:bg-[#1ebe5b] transition shadow-lg flex items-center justify-center gap-3">
                  <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>
                  {{ locale === 'ar' ? 'اطلب عبر واتساب' : 'Ask on WhatsApp' }}
                </a>
                <a v-if="product.pdf" :href="product.pdf" target="_blank" @click="trackBrochureDownload" class="bg-transparent border-2 border-gray-600 text-white px-8 py-4 rounded-xl font-bold text-lg hover:border-white transition flex items-center justify-center gap-3">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" /></svg>
                  {{ locale === 'ar' ? 'تحميل الكتيب' : 'Download Brochure' }}
                </a>
              </div>
            </div>

            <!-- Product Images / Carousel (Full Width Row) -->
            <div class="w-full" data-aos="fade-up">
              <div class="bg-white rounded-[2rem] p-4 md:p-8 shadow-2xl relative group product-3d-container">
                <div class="h-[400px] md:h-[600px] flex items-center justify-center overflow-hidden relative">
                  <transition name="fade">
                    <NuxtImg 
                      :key="currentDisplayImage"
                      :src="currentDisplayImage" 
                      :alt="product.name[locale]" 
                      class="absolute inset-0 w-full h-full object-contain p-4 md:p-8 floating-3d-image drop-shadow-2xl"
                      format="webp"
                      loading="eager"
                    />
                  </transition>
                </div>
              </div>
              
              <!-- Thumbnails -->
              <div v-if="allImages.length > 1" class="flex justify-center flex-wrap gap-4 mt-8">
                <button 
                  v-for="(img, idx) in allImages" 
                  :key="idx"
                  @click="setCurrentImage(idx)"
                  class="w-20 h-20 md:w-28 md:h-28 bg-white rounded-xl overflow-hidden border-2 transition-all p-2"
                  :class="currentImageIndex === idx ? 'border-[#E99E15] shadow-lg shadow-[#E99E15]/30 scale-110' : 'border-transparent opacity-60 hover:opacity-100 hover:scale-105'"
                >
                  <NuxtImg :src="img" :alt="`${product.name?.[locale] || 'Bestolex'} - ${idx + 1}`" class="w-full h-full object-contain" format="webp" loading="lazy" />
                </button>
              </div>
            </div>

          </div>
        </div>
      </section>

      <div class="container mx-auto px-3 md:px-8 lg:px-12 relative z-20 pb-16 md:pb-24">

        <!-- Features Section (2 cols on Desktop, 1 on Mobile) -->
        <div v-if="product.features && product.features[locale]" class="mt-16 md:mt-20" data-aos="fade-up">
          <div class="text-center mb-8 md:mb-12">
            <h2 class="text-2xl md:text-4xl font-bold text-gray-900 dark:text-white mb-3 md:mb-4">
              {{ locale === 'ar' ? 'أهم المميزات' : 'Key Features' }}
            </h2>
            <div class="h-1 w-20 md:w-24 bg-primary mx-auto rounded-full"></div>
          </div>
          
          <!-- Features Grid -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-5 md:gap-8">
            <div 
              v-for="(feature, idx) in product.features[locale]" 
              :key="idx"
              class="bg-white dark:bg-gray-800 p-5 md:p-8 rounded-2xl shadow border border-gray-100 dark:border-gray-700 flex items-start gap-3 md:gap-4 hover:shadow-xl transition"
              data-aos="fade-up"
              :data-aos-delay="idx * 100"
            >
              <div class="w-10 h-10 md:w-12 md:h-12 flex-shrink-0 bg-primary/10 rounded-xl flex items-center justify-center text-primary">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 md:h-6 md:w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
              </div>
              <div>
                <p class="text-base md:text-lg font-bold text-gray-800 dark:text-gray-200">{{ feature }}</p>
              </div>
            </div>
          </div>
        </div>



        <!-- Technical Specs & Drawings -->
        <div v-if="(product.specs && product.specs[locale]) || (product.specDrawings && product.specDrawings.length)" class="mt-16 md:mt-20" data-aos="fade-up">
          <div class="text-center mb-8 md:mb-12">
            <h2 class="text-2xl md:text-4xl font-bold text-gray-900 dark:text-white mb-3 md:mb-4">
              {{ locale === 'ar' ? 'المواصفات الفنية والرسومات التقنية' : 'Technical Specifications & Drawings' }}
            </h2>
            <div class="h-1 w-20 md:w-24 bg-primary mx-auto rounded-full"></div>
          </div>
          
          <div class="flex flex-col lg:flex-row gap-8 md:gap-12 items-start">
            <!-- Technical Specs Table -->
            <div v-if="product.specs && product.specs[locale]" class="w-full" :class="product.specDrawings?.length ? 'lg:w-1/2' : ''">
              <div class="bg-white dark:bg-gray-800 rounded-3xl shadow-xl border border-gray-100 dark:border-gray-700 overflow-hidden">
                <div class="bg-gradient-to-r from-primary to-orange-500 px-5 py-4 md:px-6 md:py-4">
                  <h3 class="text-white font-black text-lg md:text-xl">{{ locale === 'ar' ? 'الجدول التقني' : 'Technical Table' }}</h3>
                </div>
                <table class="w-full">
                  <caption class="sr-only">{{ locale === 'ar' ? `المواصفات الفنية: ${product.name[locale]}` : `Technical specifications: ${product.name[locale]}` }}</caption>
                  <tbody class="divide-y divide-gray-100 dark:divide-gray-700">
                    <tr 
                      v-for="(spec, idx) in product.specs[locale]" 
                      :key="idx"
                      class="flex flex-col sm:flex-row sm:items-center justify-between p-4 md:p-5 hover:bg-gray-50 dark:hover:bg-gray-750 transition"
                    >
                      <th scope="row" class="text-gray-500 dark:text-gray-400 font-bold mb-1 sm:mb-0 text-sm md:text-base text-start">{{ spec.label }}</th>
                      <td class="font-black text-gray-900 dark:text-white text-base md:text-lg sm:text-end">{{ spec.value }}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            <!-- Technical Drawings -->
            <div v-if="product.specDrawings && product.specDrawings.length" class="w-full lg:w-1/2">
              <h3 class="text-xl md:text-2xl font-black text-gray-900 dark:text-white mb-4 md:mb-6 text-center lg:text-start">
                {{ locale === 'ar' ? 'الرسومات التقنية' : 'Technical Drawings' }}
              </h3>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-5 md:gap-6">
                <div 
                  v-for="(drawing, idx) in product.specDrawings" 
                  :key="idx"
                  class="bg-white dark:bg-gray-800 rounded-2xl border border-gray-100 dark:border-gray-700 overflow-hidden shadow-lg hover:shadow-xl transition group"
                  data-aos="zoom-in"
                  :data-aos-delay="idx * 100"
                >
                  <div class="aspect-square bg-white p-3 md:p-4 flex items-center justify-center">
                    <NuxtImg :src="drawing.image" :alt="drawing.label[locale]" class="w-full h-full object-contain group-hover:scale-110 transition duration-500" format="webp" loading="lazy" />
                  </div>
                  <div class="p-3 md:p-4 text-center border-t border-gray-100 dark:border-gray-700">
                    <p class="font-bold text-gray-800 dark:text-gray-200 text-sm md:text-base">{{ drawing.label[locale] }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Feature Images Grid -->
        <div v-if="product.featureImages && product.featureImages.length" class="mt-16 md:mt-20" data-aos="fade-up">
          <div class="text-center mb-8 md:mb-12">
            <h2 class="text-2xl md:text-4xl font-bold text-gray-900 dark:text-white mb-3 md:mb-4">
              {{ locale === 'ar' ? 'مكونات وتفاصيل' : 'Components & Details' }}
            </h2>
            <div class="h-1 w-20 md:w-24 bg-primary mx-auto rounded-full"></div>
          </div>
          
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6 md:gap-10">
            <div 
              v-for="(featImg, idx) in product.featureImages" 
              :key="idx"
              class="bg-white dark:bg-gray-800 rounded-2xl shadow-lg border border-gray-100 dark:border-gray-700 overflow-hidden group"
              data-aos="fade-up"
              :data-aos-delay="idx * 100"
            >
              <div class="w-full aspect-[4/3] md:aspect-video overflow-hidden bg-gray-50 dark:bg-gray-900 flex items-center justify-center p-4">
                <NuxtImg :src="featImg.image" :alt="featImg.label[locale]" class="w-full h-full object-contain group-hover:scale-105 transition duration-500" format="webp" loading="lazy" />
              </div>
              <div class="p-4 md:p-6 text-center">
                <h3 class="text-lg md:text-xl font-bold text-gray-900 dark:text-white">{{ featImg.label[locale] }}</h3>
              </div>
            </div>
          </div>
        </div>

        <!-- Comparison across sibling products (data/comparisons.json), e.g. the four Garsite refuellers -->
        <section v-if="comparison" class="mt-16 md:mt-20" data-aos="fade-up" aria-labelledby="product-compare-title">
          <div class="text-center mb-8 md:mb-10">
            <h2 id="product-compare-title" class="text-2xl md:text-4xl font-bold text-gray-900 dark:text-white mb-3 md:mb-4">{{ comparison.title[locale] }}</h2>
            <div class="h-1 w-20 md:w-24 bg-primary mx-auto rounded-full"></div>
          </div>
          <p class="max-w-4xl mx-auto text-gray-600 dark:text-gray-300 leading-relaxed mb-6 text-center">{{ comparison.intro[locale] }}</p>
          <div class="overflow-x-auto bg-white dark:bg-gray-800 rounded-2xl shadow border border-gray-100 dark:border-gray-700">
            <table class="w-full min-w-[640px] text-sm md:text-base">
              <thead>
                <tr class="bg-gray-50 dark:bg-gray-900">
                  <th class="p-4 text-start font-bold text-gray-700 dark:text-gray-300"></th>
                  <th v-for="(col, ci) in comparison.columns" :key="col" class="p-4 text-start font-bold" :class="col === product.id ? 'bg-[#E99E15]/15 text-gray-900 dark:text-white' : 'text-gray-700 dark:text-gray-300'">
                    <span v-if="col === product.id">{{ comparison.columnLabels[ci][locale] }} ({{ locale === 'ar' ? 'هذه الشاحنة' : 'this truck' }})</span>
                    <NuxtLink v-else :to="localePath(`/products/${col}`)" class="text-primary hover:underline">{{ comparison.columnLabels[ci][locale] }}</NuxtLink>
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(row, ri) in comparison.rows" :key="ri" class="border-t border-gray-100 dark:border-gray-700">
                  <th scope="row" class="p-4 text-start font-bold text-gray-800 dark:text-gray-200 whitespace-nowrap">{{ row.label[locale] }}</th>
                  <td v-for="(val, vi) in row.values" :key="vi" class="p-4 text-gray-700 dark:text-gray-300" :class="comparison.columns[vi] === product.id ? 'bg-[#E99E15]/10 font-semibold' : ''">{{ val[locale] }}</td>
                </tr>
              </tbody>
            </table>
          </div>
          <p v-if="comparison.note" class="text-xs text-gray-500 dark:text-gray-400 mt-3 text-center">{{ comparison.note[locale] }}</p>
        </section>

        <!-- FAQ (GEO): visible questions and answers, mirrored in FAQPage structured data -->
        <section v-if="faqItems.length" class="mt-16 md:mt-20 max-w-4xl mx-auto" data-aos="fade-up" aria-labelledby="product-faq-title">
          <div class="text-center mb-8 md:mb-12">
            <h2 id="product-faq-title" class="text-2xl md:text-4xl font-bold text-gray-900 dark:text-white mb-3 md:mb-4">
              {{ locale === 'ar' ? 'الأسئلة الشائعة' : 'Frequently Asked Questions' }}
            </h2>
            <div class="h-1 w-20 md:w-24 bg-primary mx-auto rounded-full"></div>
          </div>
          <div class="space-y-4">
            <div v-for="(item, idx) in faqItems" :key="idx" class="bg-white dark:bg-gray-800 rounded-2xl shadow border border-gray-100 dark:border-gray-700 p-5 md:p-7">
              <h3 class="text-lg md:text-xl font-bold text-gray-900 dark:text-white mb-2">{{ item.q }}</h3>
              <p class="text-base md:text-lg text-gray-600 dark:text-gray-300 leading-relaxed">{{ item.a }}</p>
            </div>
          </div>
        </section>

        <!-- Quote Form Section -->
        <div id="quote-form" class="mt-16 md:mt-24 bg-white dark:bg-gray-800 rounded-3xl shadow-2xl border border-gray-100 dark:border-gray-700 p-6 md:p-16 max-w-4xl mx-auto" data-aos="fade-up">
          <div class="text-center mb-8 md:mb-10">
            <h2 class="text-2xl md:text-4xl font-black text-gray-900 dark:text-white mb-3 md:mb-4">
              {{ locale === 'ar' ? 'طلب عرض سعر للمنتج' : 'Request a Quote for this Product' }}
            </h2>
            <p class="text-base md:text-lg text-gray-500 dark:text-gray-400">
              {{ locale === 'ar' ? 'املأ النموذج التالي وسيقوم فريقنا بالتواصل معك في أقرب وقت.' : 'Fill out the form below and our team will contact you shortly.' }}
            </p>
          </div>
          
          <form @submit.prevent="submitQuote" class="space-y-4 md:space-y-6">
            <p class="text-sm font-bold text-gray-700 dark:text-gray-300 bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 rounded-xl px-4 py-3">
              {{ locale === 'ar' ? 'المنتج:' : 'Product:' }} <span class="text-primary">{{ productName }}</span>
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 md:gap-6">
              <div>
                <label for="q-name" class="block mb-2 text-sm font-bold text-gray-700 dark:text-gray-300">{{ locale === 'ar' ? 'الاسم*' : 'Name*' }}</label>
                <input id="q-name" v-model="form.name" type="text" required autocomplete="name" class="w-full px-4 py-3 md:px-5 md:py-4 bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 rounded-xl focus:ring-2 focus:ring-primary outline-none text-gray-900 dark:text-white transition">
              </div>
              <div>
                <label for="q-phone" class="block mb-2 text-sm font-bold text-gray-700 dark:text-gray-300">{{ locale === 'ar' ? 'رقم الهاتف أو واتساب*' : 'Phone or WhatsApp*' }}</label>
                <input id="q-phone" v-model="form.phone" type="tel" required dir="ltr" autocomplete="tel" placeholder="+974" class="w-full px-4 py-3 md:px-5 md:py-4 bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 rounded-xl focus:ring-2 focus:ring-primary outline-none text-gray-900 dark:text-white transition">
              </div>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 md:gap-6">
              <div>
                <label for="q-email" class="block mb-2 text-sm font-bold text-gray-700 dark:text-gray-300">{{ locale === 'ar' ? 'البريد الإلكتروني (اختياري)' : 'Email (optional)' }}</label>
                <input id="q-email" v-model="form.email" type="email" dir="ltr" autocomplete="email" class="w-full px-4 py-3 md:px-5 md:py-4 bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 rounded-xl focus:ring-2 focus:ring-primary outline-none text-gray-900 dark:text-white transition">
              </div>
              <div>
                <label for="q-company" class="block mb-2 text-sm font-bold text-gray-700 dark:text-gray-300">{{ locale === 'ar' ? 'اسم الشركة (اختياري)' : 'Company (optional)' }}</label>
                <input id="q-company" v-model="form.company" type="text" autocomplete="organization" class="w-full px-4 py-3 md:px-5 md:py-4 bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 rounded-xl focus:ring-2 focus:ring-primary outline-none text-gray-900 dark:text-white transition">
              </div>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 md:gap-6">
              <div>
                <label for="q-type" class="block mb-2 text-sm font-bold text-gray-700 dark:text-gray-300">{{ locale === 'ar' ? 'نوع الطلب' : 'Request type' }}</label>
                <select id="q-type" v-model="form.requestType" class="w-full px-4 py-3 md:px-5 md:py-4 bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 rounded-xl focus:ring-2 focus:ring-primary outline-none text-gray-900 dark:text-white transition">
                  <option v-for="t in REQUEST_TYPES" :key="t.id" :value="t.id">{{ locale === 'ar' ? t.ar : t.en }}</option>
                </select>
              </div>
              <div>
                <label for="q-location" class="block mb-2 text-sm font-bold text-gray-700 dark:text-gray-300">{{ locale === 'ar' ? 'موقع المشروع (اختياري)' : 'Project location (optional)' }}</label>
                <input id="q-location" v-model="form.location" type="text" :placeholder="locale === 'ar' ? 'مثال: الدوحة، مسيعيد، راس لفان' : 'e.g. Doha, Mesaieed, Ras Laffan'" class="w-full px-4 py-3 md:px-5 md:py-4 bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 rounded-xl focus:ring-2 focus:ring-primary outline-none text-gray-900 dark:text-white transition">
              </div>
            </div>
            <div>
              <label for="q-message" class="block mb-2 text-sm font-bold text-gray-700 dark:text-gray-300">{{ locale === 'ar' ? 'تفاصيل الطلب (اختياري)' : 'Details (optional)' }}</label>
              <textarea id="q-message" v-model="form.message" rows="4" :placeholder="locale === 'ar' ? 'الكمية، المقاسات، موعد التنفيذ...' : 'Quantity, sizes, timeline...'" class="w-full px-4 py-3 md:px-5 md:py-4 bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 rounded-xl focus:ring-2 focus:ring-primary outline-none text-gray-900 dark:text-white transition resize-none"></textarea>
            </div>

            <button type="submit" :disabled="loading" class="w-full bg-primary text-white py-4 md:py-5 rounded-xl font-bold text-lg md:text-xl hover:bg-orange-600 transition shadow-lg hover:shadow-primary/40 disabled:opacity-50">
              <span v-if="loading">{{ locale === 'ar' ? 'جاري الإرسال...' : 'Sending...' }}</span>
              <span v-else>{{ locale === 'ar' ? 'إرسال الطلب' : 'Submit Request' }}</span>
            </button>
            <p class="text-center text-sm text-gray-500 dark:text-gray-400">
              {{ locale === 'ar' ? 'أو تواصل معنا مباشرة على واتساب' : 'Or message us directly on WhatsApp' }}
              <a :href="whatsappHref" target="_blank" rel="noopener noreferrer" @click="trackWhatsapp" class="font-bold text-green-600 hover:underline" dir="ltr">+974 5150 5014</a>
            </p>

            <p v-if="statusMessage" :class="statusType === 'success' ? 'text-green-600' : 'text-red-600'" class="text-center font-bold mt-4 text-base md:text-lg" role="status">
              {{ statusMessage }}
            </p>
          </form>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRoute } from 'vue-router'
import { useI18n } from 'vue-i18n'
import mockProducts from '@/data/products.json'
import comparisons from '@/data/comparisons.json'
import { REQUEST_TYPES, whatsappLink } from '~/utils/leads'

const { locale } = useI18n()
const localePath = useLocalePath()
const route = useRoute()
const product = ref(null)

const initProduct = () => {
  const idStr = route.params.id
  let foundProduct = null
  let foundCatTitle = null

  for (const category of mockProducts) {
    if (category.products && Array.isArray(category.products)) {
      const prod = category.products.find(p => p.id === idStr)
      if (prod) { foundProduct = prod; foundCatTitle = category.title; break }
    }
    if (category.subcategories && Array.isArray(category.subcategories)) {
      for (const sub of category.subcategories) {
        if (sub.products && Array.isArray(sub.products)) {
          const prod = sub.products.find(p => p.id === idStr)
          if (prod) { foundProduct = prod; foundCatTitle = category.title; break }
        }
      }
      if (foundProduct) break
    }
  }

  if (foundProduct) {
    product.value = { ...foundProduct, categoryTitle: foundCatTitle }
  }
}

initProduct()

// Unknown product ids must return a real 404 (not a soft 200 page).
if (!product.value) {
  throw createError({ statusCode: 404, statusMessage: 'Product not found', fatal: true })
}

const shareImage = computed(() => {
  if (!product.value) return 'https://www.bestolex.com/logo.png'
  const raw = product.value.cardImage || product.value.image || product.value.images?.[0] || product.value.coverImage || ''
  if (!raw) return 'https://www.bestolex.com/logo.png'
  if (raw.startsWith('http://') || raw.startsWith('https://')) return raw
  return `https://www.bestolex.com${raw.startsWith('/') ? '' : '/'}${raw}`
})

const getEmbedYoutubeUrl = (url) => {
  if (!url) return ''
  const regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*/
  const match = url.match(regExp)
  return (match && match[2].length === 11)
    ? `https://www.youtube.com/embed/${match[2]}`
    : url
}

// For image gallery and autoplay
const currentImageIndex = ref(0)
let carouselInterval = null

const allImages = computed(() => {
  if (!product.value) return []
  if (product.value.images && product.value.images.length > 0) return product.value.images
  if (product.value.image) return [product.value.image]
  return []
})

const currentDisplayImage = computed(() => {
  return allImages.value[currentImageIndex.value] || ''
})

const setCurrentImage = (idx) => {
  currentImageIndex.value = idx
  resetCarousel()
}

const startCarousel = () => {
  if (allImages.value.length > 1) {
    carouselInterval = setInterval(() => {
      currentImageIndex.value = (currentImageIndex.value + 1) % allImages.value.length
    }, 3000)
  }
}

const resetCarousel = () => {
  if (carouselInterval) clearInterval(carouselInterval)
  startCarousel()
}

// Form State
const emptyForm = () => ({ name: '', company: '', email: '', phone: '', requestType: 'quote', location: '', message: '' })
const form = ref(emptyForm())
const loading = ref(false)
const statusMessage = ref('')
const statusType = ref('')

const scrollToQuote = () => {
  const el = document.getElementById('quote-form')
  if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' })
}

const trackBrochureDownload = () => {
  try {
    $fetch('/api/analytics/track', {
      method: 'POST',
      body: {
        event_type: 'brochure_download',
        target_name: `كتيب ${product.value?.name?.ar || product.value?.name?.en || 'منتج'}`
      }
    })
  } catch (e) {}
}

const submitQuote = async () => {
  loading.value = true
  statusMessage.value = ''
  
  const productNameAr = product.value?.name?.ar || ''
  const productNameEn = product.value?.name?.en || ''
  const catTitle = product.value?.categoryTitle?.[locale.value] || product.value?.categoryTitle?.ar || ''

  try {
    const response = await $fetch('/api/contact', {
      method: 'POST',
      body: {
        ...form.value,
        productId: product.value?.id,
        productName: `${productNameAr} - ${productNameEn}`,
        productNameAr,
        productNameEn,
        categoryTitle: catTitle,
        productUrl: typeof window !== 'undefined' ? window.location.href : '',
        isQuoteRequest: true
      }
    })
    
    statusType.value = 'success'
    statusMessage.value = locale.value === 'ar' ? 'تم إرسال طلب عرض السعر بنجاح! سنتواصل معك قريباً.' : 'Your quote request has been sent successfully! We will contact you soon.'
    form.value = emptyForm()
  } catch (error) {
    statusType.value = 'error'
    statusMessage.value = locale.value === 'ar' ? 'تعذّر الإرسال. حاول مرة أخرى أو راسلنا على واتساب +974 51505014.' : 'Sending failed. Please try again or message us on WhatsApp +974 51505014.'
    console.error(error)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  if (!product.value) initProduct()
  if (product.value) {
    startCarousel()
  }
})

const productName = computed(() => product.value?.name?.[locale.value] || product.value?.name?.ar || '')

// Page title and meta description: hand-written per product in data/products.json (seo.*),
// with a safe fallback that never cuts a word or adds "…".
const pageTitle = computed(() => {
  if (!product.value) return locale.value === 'ar' ? 'المنتجات | بيستوليكس قطر' : 'Products | Bestolex Qatar'
  const custom = product.value.seo?.title?.[locale.value]
  return seoTitle(custom || productName.value, locale.value)
})

const pageDesc = computed(() => {
  if (!product.value) return ''
  const custom = product.value.seo?.description?.[locale.value]
  return custom || seoDescription(product.value.description?.[locale.value] || product.value.description?.ar || '')
})

const pageUrl = computed(() => {
  return `${SITE_URL}${localePath(`/products/${route.params.id}`)}`
})

const faqItems = computed(() => product.value?.faq?.[locale.value] || [])

const comparison = computed(() => {
  const group = product.value?.comparisonGroup
  return group ? (comparisons[group] || null) : null
})

const whatsappHref = computed(() => {
  const url = `${SITE_URL}${localePath(`/products/${route.params.id}`)}`
  const text = locale.value === 'ar'
    ? `مرحباً بيستوليكس، أود طلب عرض سعر لـ: ${productName.value}\n${url}`
    : `Hello Bestolex, I would like a quote for: ${productName.value}\n${url}`
  return whatsappLink(text)
})

const trackWhatsapp = () => {
  try {
    $fetch('/api/analytics/track', { method: 'POST', body: { event_type: 'whatsapp_click', target_name: product.value?.name?.ar || product.value?.id } })
  } catch (e) {}
}

const categoryInfo = computed(() => {
  const cat = mockProducts.find(c => (c.products || []).some(p => p.id === route.params.id))
  return cat ? { id: cat.id, title: cat.title?.[locale.value] || cat.title?.ar } : null
})

useSeoMeta({
  title: pageTitle,
  description: pageDesc,
  // Open Graph for WhatsApp, Facebook, LinkedIn
  ogSiteName: 'Bestolex Qatar | بيستوليكس قطر',
  ogType: 'website',
  ogTitle: pageTitle,
  ogDescription: pageDesc,
  ogUrl: pageUrl,
  ogImage: shareImage,
  ogImageSecureUrl: shareImage,
  ogImageAlt: () => productName.value || 'Bestolex Product',
  ogImageType: () => (shareImage.value.endsWith('.png') ? 'image/png' : 'image/jpeg'),
  // Twitter Card
  twitterCard: 'summary_large_image',
  twitterTitle: pageTitle,
  twitterDescription: pageDesc,
  twitterImage: shareImage
})

useHead(() => ({
  // canonical + hreflang come from useLocaleHead in app.vue (self-referencing per language)
  script: [
    {
      type: 'application/ld+json',
      key: 'ld-product',
      innerHTML: JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'Product',
        '@id': `${pageUrl.value}#product`,
        'name': productName.value || 'Bestolex Equipment',
        'image': [...new Set([shareImage.value, ...(product.value?.images || [])])].slice(0, 6),
        'description': pageDesc.value,
        'url': pageUrl.value,
        'category': categoryInfo.value?.title || undefined,
        'brand': product.value?.brand ? { '@type': 'Brand', 'name': product.value.brand } : undefined,
        'additionalProperty': (product.value?.specs?.[locale.value] || []).map(s => ({
          '@type': 'PropertyValue', 'name': s.label, 'value': s.value
        }))
      })
    },
    ...(faqItems.value.length ? [{
      type: 'application/ld+json',
      key: 'ld-faq',
      innerHTML: JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'FAQPage',
        '@id': `${pageUrl.value}#faq`,
        'inLanguage': locale.value === 'ar' ? 'ar-QA' : 'en',
        'mainEntity': faqItems.value.map(item => ({
          '@type': 'Question',
          'name': item.q,
          'acceptedAnswer': { '@type': 'Answer', 'text': item.a }
        }))
      })
    }] : []),
    {
      type: 'application/ld+json',
      key: 'ld-breadcrumb',
      innerHTML: JSON.stringify(breadcrumbLd([
        [locale.value === 'ar' ? 'الرئيسية' : 'Home', `${SITE_URL}${localePath('/')}`.replace(/\/$/, '') || SITE_URL],
        [locale.value === 'ar' ? 'المنتجات' : 'Products', `${SITE_URL}${localePath('/products')}`],
        ...(categoryInfo.value ? [[categoryInfo.value.title, `${SITE_URL}${localePath(`/products/category/${categoryInfo.value.id}`)}`]] : []),
        [productName.value, pageUrl.value]
      ]))
    }
  ]
}))

onUnmounted(() => {
  if (carouselInterval) clearInterval(carouselInterval)
})
</script>

<style scoped>
.custom-scrollbar::-webkit-scrollbar {
  height: 6px;
}
.custom-scrollbar::-webkit-scrollbar-track {
  background: transparent;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background-color: #E99E15;
  border-radius: 10px;
}

/* Fade Animation */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}

/* 3D Floating Effect for Main Image */
.product-3d-container {
  perspective: 1000px;
}
.floating-3d-image {
  animation: float3d 5s ease-in-out infinite;
  transform-style: preserve-3d;
}
@keyframes float3d {
  0%, 100% {
    transform: translateY(0) rotateX(0deg) rotateY(0deg);
  }
  25% {
    transform: translateY(-8px) rotateX(3deg) rotateY(-2deg);
  }
  50% {
    transform: translateY(-4px) rotateX(-1deg) rotateY(3deg);
  }
  75% {
    transform: translateY(-12px) rotateX(2deg) rotateY(-1deg);
  }
}
</style>
