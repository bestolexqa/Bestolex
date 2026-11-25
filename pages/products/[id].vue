<template>
  <div class="product-page bg-white dark:bg-gray-900 min-h-screen transition-colors duration-300">
    
    <!-- Loading State -->
    <div v-if="!product" class="min-h-screen flex items-center justify-center">
      <div class="text-center">
        <div class="w-16 h-16 border-4 border-gray-200 dark:border-gray-700 border-t-primary rounded-full animate-spin mx-auto mb-6"></div>
        <p class="text-gray-500 dark:text-gray-400 text-lg">{{ locale === 'ar' ? 'جاري التحميل...' : 'Loading...' }}</p>
      </div>
    </div>

    <div v-else>

      <!-- مسار الصفحة -->
      <div class="bg-white dark:bg-gray-900 border-b border-[#E1E3E3] dark:border-gray-700">
        <div class="container mx-auto px-4 md:px-8 lg:px-12 py-4">
          <nav :aria-label="locale === 'ar' ? 'مسار الصفحة' : 'Breadcrumb'">
            <ol class="flex items-center flex-wrap gap-2 text-sm md:text-base text-[#5E5F5F] dark:text-gray-400">
              <li><NuxtLink :to="localePath('/')" class="hover:text-[#191919] dark:hover:text-white transition">{{ locale === 'ar' ? 'الرئيسية' : 'Home' }}</NuxtLink></li>
              <li aria-hidden="true">/</li>
              <li><NuxtLink :to="localePath('/products')" class="hover:text-[#191919] dark:hover:text-white transition">{{ locale === 'ar' ? 'المنتجات' : 'Products' }}</NuxtLink></li>
              <li aria-hidden="true">/</li>
              <li v-if="categoryInfo"><NuxtLink :to="localePath(`/products/category/${categoryInfo.id}`)" class="hover:text-[#191919] dark:hover:text-white transition">{{ categoryInfo.title }}</NuxtLink></li>
              <li v-if="categoryInfo" aria-hidden="true">/</li>
              <li aria-current="page" class="font-bold text-[#191919] dark:text-white">{{ product.name[locale] }}</li>
            </ol>
          </nav>
        </div>
      </div>

      <!-- الواجهة: عمودان على أرضية فاتحة -->
      <section class="bg-white dark:bg-gray-900">
        <div class="container mx-auto px-4 md:px-8 lg:px-12 py-10 md:py-14">
          <div class="flex flex-col lg:flex-row gap-10 lg:gap-14 items-start">

            <!-- النص والأرقام -->
            <div class="w-full lg:w-1/2 flex flex-col gap-6">
              <div>
                <NuxtLink v-if="categoryInfo" :to="localePath(`/products/category/${categoryInfo.id}`)" class="inline-block text-sm font-bold text-[#191919] dark:text-[#E99E05] bg-[#FFF1D4] dark:bg-transparent dark:border dark:border-[#E99E05]/60 rounded-md px-3 py-1.5 hover:bg-[#E99E05] dark:hover:bg-[#E99E05] dark:hover:text-[#191919] transition">
                  {{ categoryInfo.title }}
                </NuxtLink>
              </div>

              <h1 class="font-display text-4xl md:text-5xl font-extrabold text-[#191919] dark:text-white leading-[1.15]">
                {{ product.name[locale] }}
              </h1>

              <p v-if="product.description && product.description[locale]" class="text-base md:text-lg text-[#333434] dark:text-gray-300 leading-relaxed whitespace-pre-line max-w-[54ch]">
                {{ product.description[locale] }}
              </p>

              <!-- كتل الأرقام: طبقة المخطط الفني -->
              <div v-if="heroFigures.length" class="bp grid grid-cols-1" :class="heroFigures.length > 2 ? 'sm:grid-cols-3' : (heroFigures.length > 1 ? 'sm:grid-cols-2' : '')">
                <div v-for="(fig, i) in heroFigures" :key="i" class="px-4 py-3 border-t sm:border-t-0 sm:border-s border-[#191919] dark:border-[#6F7070] first:border-t-0 sm:first:border-s-0">
                  <div class="text-xs text-[#5E5F5F] dark:text-gray-400">{{ fig.label }}</div>
                  <div class="bp-num font-display text-lg md:text-xl font-bold text-[#191919] dark:text-white mt-1">{{ fig.value }}</div>
                </div>
              </div>

              <!-- الأزرار -->
              <div class="flex flex-wrap gap-3">
                <button @click="scrollToQuote" class="inline-flex items-center justify-center gap-2 min-h-[52px] px-6 rounded-[10px] bg-[#E99E05] text-[#191919] font-extrabold text-base md:text-lg hover:bg-[#d08f04] transition">
                  {{ locale === 'ar' ? 'طلب عرض سعر' : 'Request a Quote' }}
                </button>
                <a :href="whatsappHref" target="_blank" rel="noopener noreferrer" @click="trackWhatsapp" class="inline-flex items-center justify-center gap-2 min-h-[52px] px-6 rounded-[10px] border border-[#191919] dark:border-gray-500 text-[#191919] dark:text-white font-bold text-base md:text-lg hover:bg-[#191919] hover:text-white dark:hover:bg-white dark:hover:text-[#191919] transition">
                  <svg class="h-5 w-5 fill-current" viewBox="0 0 24 24" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>
                  {{ locale === 'ar' ? 'اطلب عبر واتساب' : 'Ask on WhatsApp' }}
                </a>
                <button @click="requestDatasheet" class="inline-flex items-center justify-center gap-2 min-h-[52px] px-6 rounded-[10px] border border-[#A9AAAA] text-[#191919] dark:text-white font-bold text-base md:text-lg hover:border-[#191919] dark:hover:border-white transition">
                  {{ locale === 'ar' ? 'اطلب ورقة المواصفات' : 'Request the datasheet' }}
                </button>
              </div>

            </div>

            <!-- الصورة بخط الأبعاد -->
            <div class="w-full lg:w-1/2">
              <figure class="m-0 relative" :class="dimensionSpec ? 'pb-14 ps-16' : ''">
                <div class="bg-[#F4F5F5] dark:bg-gray-800 border border-[#E1E3E3] dark:border-gray-700 rounded-xl p-4 md:p-6">
                  <div class="aspect-[4/5] md:aspect-[4/4.4] flex items-center justify-center overflow-hidden relative">
                    <transition name="fade">
                      <NuxtImg
                        :key="currentDisplayImage"
                        :src="currentDisplayImage"
                        :alt="product.name[locale]"
                        class="absolute inset-0 w-full h-full object-contain p-2 md:p-4"
                        format="webp"
                        loading="eager"
                      />
                    </transition>
                  </div>
                </div>

                <!-- خط الأبعاد: يظهر فقط حين يحمل الكتالوج مقاساً لهذا المنتج -->
                <template v-if="dimensionSpec">
                  <div aria-hidden="true" class="absolute end-0 start-16 bottom-7 h-px bg-[#E99E05]"></div>
                  <div aria-hidden="true" class="absolute end-0 bottom-[18px] w-px h-[18px] bg-[#E99E05]"></div>
                  <div aria-hidden="true" class="absolute start-16 bottom-[18px] w-px h-[18px] bg-[#E99E05]"></div>
                  <div aria-hidden="true" class="absolute top-0 bottom-14 start-8 w-px bg-[#E99E05]"></div>
                  <div aria-hidden="true" class="absolute start-[18px] top-0 h-px w-[18px] bg-[#E99E05]"></div>
                  <div aria-hidden="true" class="absolute start-[18px] bottom-14 h-px w-[18px] bg-[#E99E05]"></div>
                </template>

                <figcaption v-if="dimensionSpec" class="absolute bottom-0 inset-x-0 text-center">
                  <span class="bp-num inline-block bg-white dark:bg-gray-900 px-3 text-sm text-[#191919] dark:text-gray-200">
                    {{ dimensionSpec.label }}: {{ dimensionSpec.value }}
                  </span>
                </figcaption>
              </figure>

              <!-- المصغّرات -->
              <div v-if="allImages.length > 1" class="flex flex-wrap gap-2.5 mt-4">
                <button
                  v-for="(img, idx) in allImages.slice(0, 6)"
                  :key="idx"
                  @click="setCurrentImage(idx)"
                  :aria-label="`${product.name?.[locale]} — ${idx + 1}`"
                  :aria-pressed="currentImageIndex === idx"
                  class="w-14 h-14 md:w-16 md:h-16 bg-white rounded-lg overflow-hidden border p-1 transition"
                  :class="currentImageIndex === idx ? 'border-[#191919]' : 'border-[#E1E3E3] opacity-70 hover:opacity-100'"
                >
                  <NuxtImg :src="img" :alt="`${product.name[locale]} — ${idx + 1}`" sizes="64px" class="w-full h-full object-contain" format="webp" loading="lazy" />
                </button>
              </div>
            </div>

          </div>
        </div>
      </section>

      <!-- باختصار -->
      <section v-if="product.summary && product.summary[locale]" class="bg-[#F4F5F5] dark:bg-gray-800 border-y border-[#E1E3E3] dark:border-gray-700">
        <div class="container mx-auto px-4 md:px-8 lg:px-12 py-8 md:py-10">
          <div class="bg-white dark:bg-gray-900 border border-[#E1E3E3] dark:border-gray-700 border-s-4 border-s-[#E99E05] rounded-xl px-6 py-5 md:px-7 md:py-6">
            <h2 class="font-display text-xl md:text-2xl font-bold text-[#191919] dark:text-white mb-2">{{ locale === 'ar' ? 'باختصار' : 'At a glance' }}</h2>
            <p class="text-base md:text-lg text-[#333434] dark:text-gray-300 leading-relaxed">{{ product.summary[locale] }}</p>
          </div>
        </div>
      </section>

      <!-- المواصفات + أهم المميزات جنباً إلى جنب -->
      <section v-if="(product.specs && product.specs[locale]) || (product.features && product.features[locale])" class="bg-white dark:bg-gray-900">
        <div class="container mx-auto px-4 md:px-8 lg:px-12 py-12 md:py-16">
          <div class="flex flex-col lg:flex-row gap-10 lg:gap-12 items-start">

            <div v-if="product.specs && product.specs[locale]" class="w-full" :class="(product.features && product.features[locale]) ? 'lg:w-1/2' : ''">
              <h2 class="font-display text-2xl md:text-3xl font-bold text-[#191919] dark:text-white mb-5">{{ locale === 'ar' ? 'المواصفات' : 'Specifications' }}</h2>
              <div class="bp">
                <table>
                  <!-- سطر المصدر يُضاف حين يحمل كل منتج حقل مصدره في data/products.json؛ لا يُكتب مصدر عام غير مؤكد. -->
                  <caption class="sr-only">{{ locale === 'ar' ? `المواصفات الفنية: ${product.name[locale]}` : `Technical specifications: ${product.name[locale]}` }}</caption>
                  <tbody>
                    <tr v-for="(spec, idx) in product.specs[locale]" :key="idx">
                      <th scope="row" class="font-bold text-[#191919] dark:text-white w-1/2">{{ spec.label }}</th>
                      <td class="bp-num text-[#333434] dark:text-gray-200"><bdi>{{ spec.value }}</bdi></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            <div v-if="product.features && product.features[locale]" class="w-full" :class="(product.specs && product.specs[locale]) ? 'lg:w-1/2' : ''">
              <h2 class="font-display text-2xl md:text-3xl font-bold text-[#191919] dark:text-white mb-5">{{ locale === 'ar' ? 'أهم المميزات' : 'Key Features' }}</h2>
              <ul class="flex flex-col gap-3">
                <li v-for="(feature, idx) in product.features[locale]" :key="idx" class="flex items-start gap-3 border border-[#E1E3E3] dark:border-gray-700 rounded-xl p-4 md:p-5 hover:border-[#191919] dark:hover:border-[#E99E05] transition">
                  <span aria-hidden="true" class="mt-0.5 flex-shrink-0 w-6 h-6 rounded-md bg-[#FFF1D4] text-[#191919] flex items-center justify-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" /></svg>
                  </span>
                  <span class="text-base md:text-lg text-[#333434] dark:text-gray-200 leading-relaxed">{{ feature }}</span>
                </li>
              </ul>
            </div>

          </div>
        </div>
      </section>

      <!-- الرسومات التقنية -->
      <section v-if="product.specDrawings && product.specDrawings.length" class="bg-[#F4F5F5] dark:bg-gray-800 border-y border-[#E1E3E3] dark:border-gray-700">
        <div class="container mx-auto px-4 md:px-8 lg:px-12 py-12 md:py-16">
          <h2 class="font-display text-2xl md:text-3xl font-bold text-[#191919] dark:text-white mb-6">{{ locale === 'ar' ? 'الرسومات التقنية' : 'Technical Drawings' }}</h2>
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
            <figure v-for="(drawing, idx) in product.specDrawings" :key="idx" class="m-0 bg-white dark:bg-gray-900 border border-[#E1E3E3] dark:border-gray-700 rounded-xl overflow-hidden">
              <div class="aspect-square bg-white p-4 flex items-center justify-center">
                <NuxtImg :src="drawing.image" :alt="drawing.label[locale]" class="w-full h-full object-contain" format="webp" loading="lazy" />
              </div>
              <figcaption class="px-4 py-3 border-t border-[#E1E3E3] dark:border-gray-700 text-sm md:text-base font-bold text-[#191919] dark:text-gray-200">{{ drawing.label[locale] }}</figcaption>
            </figure>
          </div>
        </div>
      </section>

      <!-- مكونات وتفاصيل: فهرس القطع -->
      <section v-if="partsList.length >= 3" class="bg-[#191919]" aria-labelledby="product-parts-title">
        <div class="container mx-auto px-4 md:px-8 lg:px-12 py-14 md:py-16">

          <div class="flex flex-wrap items-end justify-between gap-4 border-b border-[#343535] pb-5 mb-8">
            <div class="flex flex-col gap-2">
              <span class="text-sm font-bold text-[#E99E05]">{{ locale === 'ar' ? 'فهرس القطع' : 'Parts index' }}</span>
              <h2 id="product-parts-title" class="font-display text-3xl md:text-4xl font-extrabold text-white leading-tight">
                {{ locale === 'ar' ? 'مكونات وتفاصيل' : 'Components & Details' }}
              </h2>
            </div>
            <p class="m-0 text-base text-[#B9BABA] leading-relaxed max-w-[46ch]">
              {{ locale === 'ar' ? 'اختر قطعة لتراها عن قرب. الأسماء من كتالوج المصنّع.' : 'Pick a part to see it up close. Names come from the manufacturer catalogue.' }}
            </p>
          </div>

          <div class="flex flex-col-reverse lg:flex-row gap-8 lg:gap-10 items-stretch">

            <!-- الفهرس -->
            <nav class="w-full lg:w-[360px] lg:flex-shrink-0 flex flex-col" :aria-label="locale === 'ar' ? 'قطع المنتج' : 'Product parts'">
              <button
                v-for="(part, idx) in partsList"
                :key="idx"
                type="button"
                @click="activePart = idx"
                :aria-pressed="activePart === idx"
                class="parts-row text-start flex items-center gap-3.5 w-full border-0 border-b border-[#2E2E2E] bg-transparent cursor-pointer"
                :class="activePart === idx ? 'py-4 pe-4' : 'py-3 pe-3.5'"
              >
                <span aria-hidden="true" class="w-[3px] self-stretch" :class="activePart === idx ? 'bg-[#E99E05]' : 'bg-transparent'"></span>
                <span class="bp-num font-display font-bold text-[15px] w-6" dir="ltr" :class="activePart === idx ? 'text-[#E99E05]' : 'text-[#6F7070]'">{{ String(idx + 1).padStart(2, '0') }}</span>
                <span class="flex-1 text-base leading-relaxed" :class="activePart === idx ? 'text-white font-bold' : 'text-[#B9BABA]'">{{ part.label[locale] }}</span>
              </button>
            </nav>

            <!-- المنصة -->
            <figure class="m-0 flex-1 flex flex-col gap-4">
              <div class="relative border border-[#4A4B4B] bg-[#F4F5F5] overflow-hidden">
                <span aria-hidden="true" class="bp-num font-display absolute top-2 start-5 font-extrabold text-[92px] md:text-[132px] leading-none text-[#191919]/[0.07]" dir="ltr">{{ String(activePart + 1).padStart(2, '0') }}</span>
                <NuxtImg
                  v-for="(part, idx) in partsList"
                  v-show="activePart === idx"
                  :key="idx"
                  :src="part.image"
                  :alt="part.label[locale]"
                  :class="['relative block w-full aspect-[4/3] object-contain p-5 md:p-7', activePart === idx ? 'parts-stage' : '']"
                  sizes="(max-width: 1024px) 100vw, 640px"
                  format="webp"
                  loading="lazy"
                />
                <span aria-hidden="true" class="absolute bottom-0 start-0 h-[3px] bg-[#E99E05] transition-all duration-300" :style="{ width: Math.round(((activePart + 1) / partsList.length) * 100) + '%' }"></span>
              </div>
              <figcaption class="flex flex-wrap items-baseline gap-x-4 gap-y-2">
                <span aria-hidden="true" class="w-8 h-0.5 bg-[#E99E05] self-center"></span>
                <span class="font-display font-bold text-xl md:text-2xl text-white">{{ partsList[activePart].label[locale] }}</span>
                <span class="bp-num ms-auto text-[15px] text-[#8A8B8B]" dir="ltr">{{ activePart + 1 }} / {{ partsList.length }}</span>
              </figcaption>
            </figure>

          </div>
        </div>
      </section>

      <!-- مكونات وتفاصيل: قطعتان أو أقل، فالفهرس لا يخدمها -->
      <section v-else-if="partsList.length" class="bg-white dark:bg-gray-900">
        <div class="container mx-auto px-4 md:px-8 lg:px-12 py-12 md:py-16">
          <h2 class="font-display text-2xl md:text-3xl font-bold text-[#191919] dark:text-white mb-6">{{ locale === 'ar' ? 'مكونات وتفاصيل' : 'Components & Details' }}</h2>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <figure v-for="(featImg, idx) in partsList" :key="idx" class="m-0 bg-white dark:bg-gray-800 border border-[#E1E3E3] dark:border-gray-700 rounded-xl overflow-hidden">
              <div class="w-full aspect-[4/3] overflow-hidden bg-[#F4F5F5] dark:bg-gray-900 flex items-center justify-center p-4">
                <NuxtImg :src="featImg.image" :alt="featImg.label[locale]" class="w-full h-full object-contain" format="webp" loading="lazy" />
              </div>
              <figcaption class="px-5 py-4 border-t border-[#E1E3E3] dark:border-gray-700 text-base md:text-lg font-bold text-[#191919] dark:text-white">{{ featImg.label[locale] }}</figcaption>
            </figure>
          </div>
        </div>
      </section>

      <!-- مقارنة الموديلات -->
      <section v-if="comparison" class="bg-[#F4F5F5] dark:bg-gray-800 border-y border-[#E1E3E3] dark:border-gray-700" aria-labelledby="product-compare-title">
        <div class="container mx-auto px-4 md:px-8 lg:px-12 py-12 md:py-16">
          <h2 id="product-compare-title" class="font-display text-2xl md:text-3xl font-bold text-[#191919] dark:text-white mb-4">{{ comparison.title[locale] }}</h2>
          <p class="text-base md:text-lg text-[#444545] dark:text-gray-300 leading-relaxed mb-6 max-w-[70ch]">{{ comparison.intro[locale] }}</p>
          <div class="bp overflow-x-auto">
            <table class="min-w-[640px]">
              <thead>
                <tr>
                  <th><span class="sr-only">{{ locale === 'ar' ? 'المواصفة' : 'Specification' }}</span></th>
                  <th v-for="(col, ci) in comparison.columns" :key="col" :class="col === product.id ? 'bg-[#E99E05]/15 !text-[#191919] dark:!text-white' : ''">
                    <span v-if="col === product.id">{{ comparison.columnLabels[ci][locale] }} ({{ locale === 'ar' ? 'هذا الموديل' : 'this model' }})</span>
                    <NuxtLink v-else :to="localePath(`/products/${col}`)" class="text-[#191919] dark:text-gray-200 underline decoration-[#E99E05] decoration-2 underline-offset-4">{{ comparison.columnLabels[ci][locale] }}</NuxtLink>
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(row, ri) in comparison.rows" :key="ri">
                  <th scope="row" class="font-bold text-[#191919] dark:text-gray-200 whitespace-nowrap">{{ row.label[locale] }}</th>
                  <td v-for="(val, vi) in row.values" :key="vi" class="bp-num text-[#333434] dark:text-gray-300" :class="comparison.columns[vi] === product.id ? 'bg-[#E99E05]/10 font-bold' : ''"><bdi>{{ val[locale] }}</bdi></td>
                </tr>
              </tbody>
            </table>
          </div>
          <p v-if="comparison.note" class="text-sm text-[#5E5F5F] dark:text-gray-400 mt-3">{{ comparison.note[locale] }}</p>
        </div>
      </section>

      <!-- الأسئلة الشائعة -->
      <section v-if="faqItems.length" class="bg-white dark:bg-gray-900" aria-labelledby="product-faq-title">
        <div class="container mx-auto px-4 md:px-8 lg:px-12 py-12 md:py-16">
          <div class="max-w-3xl">
            <h2 id="product-faq-title" class="font-display text-2xl md:text-3xl font-bold text-[#191919] dark:text-white mb-5">{{ locale === 'ar' ? 'الأسئلة الشائعة' : 'Frequently Asked Questions' }}</h2>
            <div>
              <details v-for="(item, idx) in faqItems" :key="idx" class="group border-b border-[#E1E3E3] dark:border-gray-700 py-4">
                <summary class="faq-summary font-display text-lg md:text-xl font-bold text-[#191919] dark:text-white cursor-pointer flex items-start justify-between gap-4">
                  <span>{{ item.q }}</span>
                  <span aria-hidden="true" class="flex-shrink-0 mt-1 text-[#E99E05] transition-transform group-open:rotate-45 text-2xl leading-none">+</span>
                </summary>
                <p class="mt-3 text-base md:text-lg text-[#444545] dark:text-gray-300 leading-relaxed">{{ item.a }}</p>
              </details>
            </div>
          </div>
        </div>
      </section>


      <!-- منتجات ذات صلة -->
      <section v-if="relatedProducts.length" class="bg-white dark:bg-gray-900" aria-labelledby="product-related-title">
        <div class="container mx-auto px-4 md:px-8 lg:px-12 py-12 md:py-16">
          <h2 id="product-related-title" class="font-display text-2xl md:text-3xl font-bold text-[#191919] dark:text-white mb-6">
            {{ locale === 'ar' ? 'منتجات ذات صلة' : 'Related products' }}
          </h2>
          <div class="grid grid-cols-2 lg:grid-cols-4 gap-5">
            <NuxtLink
              v-for="rel in relatedProducts"
              :key="rel.id"
              :to="localePath(`/products/${rel.id}`)"
              class="group flex flex-col border border-[#E1E3E3] dark:border-gray-700 rounded-xl overflow-hidden hover:border-[#191919] dark:hover:border-[#E99E05] transition"
            >
              <div class="aspect-[4/3] bg-[#F4F5F5] dark:bg-gray-800 flex items-center justify-center p-3">
                <NuxtImg :src="rel.cardImage || rel.image" :alt="rel.name[locale]" class="w-full h-full object-contain" format="webp" loading="lazy" />
              </div>
              <span class="px-4 py-3 text-sm md:text-base font-bold leading-relaxed text-[#191919] dark:text-white">{{ rel.name[locale] }}</span>
            </NuxtLink>
          </div>
        </div>
      </section>

      <!-- اقرأ قبل أن تقرر -->
      <section v-if="relatedArticles.length" class="bg-[#F4F5F5] dark:bg-gray-800 border-y border-[#E1E3E3] dark:border-gray-700" aria-labelledby="product-reading-title">
        <div class="container mx-auto px-4 md:px-8 lg:px-12 py-12 md:py-16">
          <div class="flex flex-wrap items-baseline justify-between gap-3 mb-6">
            <h2 id="product-reading-title" class="font-display text-2xl md:text-3xl font-bold text-[#191919] dark:text-white">
              {{ locale === 'ar' ? 'اقرأ قبل أن تقرر' : 'Read before you decide' }}
            </h2>
            <NuxtLink :to="localePath('/blog')" class="text-base font-bold text-[#191919] dark:text-white underline decoration-[#E99E05] decoration-2 underline-offset-4">
              {{ locale === 'ar' ? 'كل المقالات' : 'All articles' }}
            </NuxtLink>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
            <NuxtLink
              v-for="art in relatedArticles"
              :key="art.id"
              :to="localePath(`/blog/${art.id}`)"
              class="flex flex-col gap-3 bg-white dark:bg-gray-900 border border-[#E1E3E3] dark:border-gray-700 rounded-xl p-5 hover:border-[#191919] dark:hover:border-[#E99E05] transition"
            >
              <span class="flex items-center gap-2 text-xs font-bold text-[#5E5F5F] dark:text-gray-400"><span aria-hidden="true" class="w-2 h-2 rounded-full bg-[#E99E05]"></span>{{ art.category?.[locale] || art.category?.ar }}</span>
              <span class="font-display text-lg font-bold leading-snug text-[#191919] dark:text-white">{{ art.title?.[locale] || art.title?.ar }}</span>
              <span class="text-sm text-[#5E5F5F] dark:text-gray-400 leading-relaxed">{{ art.desc?.[locale] || art.desc?.ar }}</span>
            </NuxtLink>
          </div>
        </div>
      </section>

      <div class="container mx-auto px-4 md:px-8 lg:px-12 pb-16 md:pb-24">
        <!-- Quote Form Section -->
        <div id="quote-form" class="mt-16 md:mt-24 bg-white dark:bg-gray-800 rounded-xl border border-[#E1E3E3] dark:border-gray-700 p-6 md:p-16 max-w-4xl mx-auto" data-aos="fade-up">
          <div class="mb-8 md:mb-10">
            <h2 class="font-display text-2xl md:text-4xl font-black text-gray-900 dark:text-white mb-3 md:mb-4">
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

            <button type="submit" :disabled="loading" class="w-full bg-primary text-[#191919] py-4 md:py-5 rounded-[10px] font-extrabold text-lg md:text-xl hover:bg-[#d08f04] transition disabled:opacity-50">
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
import { ref, computed, watch, onMounted, onUnmounted } from 'vue'
import { useRoute } from 'vue-router'
import { useI18n } from 'vue-i18n'
import mockProducts from '@/data/products.json'
import comparisons from '@/data/comparisons.json'
import { REQUEST_TYPES, whatsappLink } from '~/utils/leads'
import { trackLead } from '~/utils/track'

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

// لا تبديل تلقائي: كان يسرق اختيار الزائر بعد ثلاث ثوانٍ، ويترك سطر الأبعاد
// يصف صورة أخرى، ويجلب كل صور المنتج بعرض 1536 في أول نصف دقيقة.
const startCarousel = () => {}

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

// The datasheet is sent by us with the technical proposal, so the request stays
// on our form instead of sending the buyer to the manufacturer's 2019 brochure.
const requestDatasheet = () => {
  const n = product.value?.name?.[locale.value] || product.value?.name?.ar || ''
  const line = locale.value === 'ar'
    ? `أرجو إرسال ورقة المواصفات الفنية لـ${n}.`
    : `Please send the technical datasheet for the ${n}.`
  form.value.requestType = 'quote'
  form.value.message = form.value.message ? `${line}\n${form.value.message}` : line
  scrollToQuote()
  trackBrochureDownload()
}

const trackBrochureDownload = () => {
  try {
    $fetch('/api/analytics/track', {
      method: 'POST',
      body: {
        event_type: 'datasheet_request',
        target_name: `ورقة مواصفات ${product.value?.name?.ar || product.value?.name?.en || 'منتج'}`
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
    
    trackLead({ formName: 'product_quote', requestType: form.value.requestType, productId: product.value?.id })
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

// اسم القسم الذي ينتمي إليه المنتج، من بيانات المنتجات لا من نص ثابت
const categoryName = computed(() => {
  const cat = mockProducts.find(c => (c.products || []).some(pr => pr.id === product.value?.id))
  return cat?.title?.[locale.value] || ''
})

// أول مواصفة تحمل مقاس الآلة. خط الأبعاد على الصورة يظهر فقط حين توجد،
// فلا يُرسم خط بلا رقم من الكتالوج.
// كتل الأرقام تحت العنوان. النموذج يعتمد عليها، ولا تحمل إلا بيانات موجودة:
// حقل stats إن وُجد (8 منتجات)، وإلا أقصر ثلاث مواصفات تحمل رقماً من الكتالوج.
// التصنيف المقابل في المدونة لكل قسم منتجات (الأسماء الخمسة الثابتة في server/utils/blogCategories.ts)
const BLOG_CATEGORY_BY_PRODUCT_CATEGORY = {
  'waste-management': 'النفايات وإعادة التدوير',
  'docking-systems': 'أنظمة التحميل والمستودعات',
  'perimeter-protection': 'الحماية المحيطية',
  'industrial-doors': 'الأبواب الصناعية',
  'other-products': 'المعدات الثقيلة'
}

// بطاقات المقالات بلا نصوصها، وهي مخزّنة في الخادم خمس دقائق
const { data: blogCards } = await useFetch('/api/blog', {
  query: { view: 'list' },
  key: 'blog-cards-list',
  default: () => [],
  server: true
})

const relatedArticles = computed(() => {
  const list = Array.isArray(blogCards.value) ? blogCards.value : []
  if (!list.length) return []
  const want = BLOG_CATEGORY_BY_PRODUCT_CATEGORY[categoryInfo.value?.id]
  const same = want ? list.filter(a => (a.category?.ar || a.category) === want) : []
  const rest = list.filter(a => !same.includes(a))
  return [...same, ...rest].slice(0, 3)
})

// منتجات أخرى من القسم نفسه
const relatedProducts = computed(() => {
  const cat = mockProducts.find(c => (c.products || []).some(pr => pr.id === route.params.id))
  if (!cat) return []
  return (cat.products || []).filter(pr => pr.id !== route.params.id).slice(0, 4)
})

// فهرس القطع: القطعة المعروضة على المنصة
const partsList = computed(() => product.value?.featureImages || [])
const activePart = ref(0)
watch(() => product.value?.id, () => { activePart.value = 0 })

const heroFigures = computed(() => {
  const stats = product.value?.stats?.[locale.value]
  if (stats && stats.length) return stats.slice(0, 3).map(s => ({ value: s.value, label: s.label }))
  const specs = product.value?.specs?.[locale.value] || []
  // مرشّح الطول كان يُسقط أهم رقم في الصفحة (ارتفاع المصد 24 حرفاً) ويعطي
  // عدد كتل مختلفاً بين العربية والإنجليزية. الترتيب الآن بالأولوية لا بالطول.
  const PRIORITY = /حمولة|طاقة|قوة|سعة|ارتفاع|عرض|طول|سرعة|قدرة|capacity|load|height|width|speed|power/i
  const usable = specs.filter(s => /\d/.test(s.value || '') && (s.value || '').length <= 26)
  const ranked = [...usable].sort((a, b) => (PRIORITY.test(b.label || '') ? 1 : 0) - (PRIORITY.test(a.label || '') ? 1 : 0))
  return ranked.slice(0, 3).map(s => ({ value: s.value, label: s.label }))
})

const dimensionSpec = computed(() => {
  const specs = product.value?.specs?.[locale.value] || []
  const re = locale.value === 'ar'
    ? /أبعاد|مقاس|ارتفاع|عرض|طول|سماكة|قطر/
    : /dimension|size|height|width|length|thickness|diameter/i
  return specs.find(s => re.test(s.label || '')) || null
})

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
        'image': [...new Set([shareImage.value, ...(product.value?.images || []), ...((product.value?.featureImages || []).map(f => f.image))])].slice(0, 12),
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
/* فهرس القطع: الصورة تصعد وتظهر عند التبديل — حركة واحدة مقصودة */
.parts-stage {
  animation: part-rise 0.34s cubic-bezier(0.2, 0.7, 0.3, 1) both;
}
@keyframes part-rise {
  from { opacity: 0; transform: translateY(14px) scale(0.985); }
  to   { opacity: 1; transform: none; }
}
.parts-row {
  transition: background 0.18s ease, padding 0.18s ease;
}
.parts-row:hover {
  background: rgba(255, 255, 255, 0.05);
}
@media (prefers-reduced-motion: reduce) {
  .parts-stage { animation: none; }
  .parts-row { transition: none; }
}

/* الأسئلة الشائعة: سهم الهوية بدل المثلث الافتراضي للمتصفح */
.faq-summary {
  list-style: none;
}
.faq-summary::-webkit-details-marker {
  display: none;
}

.custom-scrollbar::-webkit-scrollbar {
  height: 6px;
}
.custom-scrollbar::-webkit-scrollbar-track {
  background: transparent;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background-color: #E99E05;
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
