<template>
  <div>
    <!-- Hero Section -->
    <section class="relative h-[80vh] flex items-center justify-center bg-gray-900 overflow-hidden">
      <!-- Video Background -->
      <div class="absolute inset-0 z-0">
        <!-- Interim cover image: the previous background video belonged to another project (dental clinic).
             Replace with a compressed Bestolex video + this image as its poster when the footage is ready. -->
        <img
          src="https://cdn.bestolex.com/bestolex/about/showroom-v2.jpg"
          alt=""
          aria-hidden="true"
          fetchpriority="high"
          loading="eager"
          decoding="async"
          class="w-full h-full object-cover opacity-60 dark:opacity-40"
        />
        <!-- Optional overlay gradient for better text readability -->
        <div class="absolute inset-0 bg-gradient-to-t from-gray-900 via-transparent to-transparent opacity-80"></div>
      </div>
      <div class="relative z-10 text-center px-4" data-aos="fade-up">
        <div class="flex justify-center mb-8">
          <NuxtImg src="/logo-dark-transparent.png" alt="Bestolex Logo" class="h-20 md:h-32 object-contain drop-shadow-2xl" format="webp" loading="eager" />
        </div>
        <h1 class="text-xl md:text-3xl font-medium mb-3 text-gray-100 drop-shadow-md">
          {{ locale === 'ar' ? 'معدات التحميل والنفايات والحماية المحيطية والأبواب الصناعية في قطر' : 'Loading, Waste, Perimeter Security and Industrial Door Solutions in Qatar' }}
        </h1>
        <p class="text-base md:text-xl mb-8 text-gray-200 drop-shadow-md">
          {{ locale === 'ar' ? 'بيستوليكس – الوكيل الحصري لمنتجات ساب تك في قطر' : 'Bestolex – the exclusive SABTECH agent in Qatar' }}
        </p>
        <NuxtLink :to="localePath('/products')" class="inline-block bg-primary text-white px-8 py-4 rounded-lg font-bold text-lg hover:bg-orange-600 transition shadow-lg shadow-primary/30 hover:scale-105">
          {{ locale === 'ar' ? 'اكتشف منتجاتنا' : 'Explore Our Products' }}
        </NuxtLink>
      </div>
    </section>

    <!-- Featured Products Section -->
    <section class="py-20 bg-white dark:bg-secondary">
      <div class="container mx-auto px-4">
        <h2 class="text-3xl font-bold text-center mb-12" data-aos="fade-up">
          {{ locale === 'ar' ? 'أبرز أنظمة المعدات والحلول الصناعية' : 'Our Core Industrial & Engineering Solutions' }}
        </h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div v-for="(category, index) in products" :key="category.id" class="bg-gray-50 dark:bg-gray-800 rounded-xl overflow-hidden shadow hover:shadow-xl transition group flex flex-col justify-between" :data-aos="'fade-up'" :data-aos-delay="index * 100">
            <div>
              <NuxtLink :to="localePath(`/products/category/${category.id}`)" class="block h-52 overflow-hidden relative">
                <NuxtImg :src="category.image" :alt="category.title[locale]" class="w-full h-full object-cover group-hover:scale-110 transition duration-500" format="webp" loading="lazy" />
                <div class="absolute inset-0 bg-black/20 group-hover:bg-transparent transition"></div>
              </NuxtLink>
              <div class="p-6 pb-2">
                <h3 class="font-bold text-xl mb-2 text-primary">
                  <NuxtLink :to="localePath(`/products/category/${category.id}`)" class="hover:underline">
                    {{ category.title[locale] }}
                  </NuxtLink>
                </h3>
                <p class="text-gray-600 dark:text-gray-400 mb-4">{{ category.description[locale] }}</p>
              </div>
            </div>
            <div class="p-6 pt-0">
              <NuxtLink :to="localePath(`/products/category/${category.id}`)" class="text-primary font-bold hover:text-orange-600 transition inline-flex items-center gap-2">
                {{ locale === 'ar' ? 'عرض منتجات القسم' : 'View Category Products' }} &rarr;
              </NuxtLink>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Articles / Blog Section -->
    <section class="py-24 bg-gray-50 dark:bg-gray-900">
      <div class="container mx-auto px-4 md:px-8">
        <div class="text-center max-w-3xl mx-auto mb-16" data-aos="fade-up">
          <div class="inline-block bg-primary/10 text-primary font-extrabold px-4 py-1.5 rounded-lg text-sm mb-4">
            {{ locale === 'ar' ? 'المدونة الهندسية المتخصصة في المعدات الثقيلة' : 'Heavy Machinery Engineering Blog' }}
          </div>
          <h2 class="text-3xl md:text-5xl font-black text-gray-900 dark:text-white mb-6">
            {{ locale === 'ar' ? 'المقالات' : 'Articles' }}
          </h2>
          <p class="text-lg md:text-xl text-gray-600 dark:text-gray-400 leading-relaxed">
            {{ locale === 'ar' 
              ? 'اكتشف أحدث الرؤى الفنية، وأدلة الصيانة المتكاملة، والحلول الهندسية المبتكرة في مجالات المعدات الثقيلة، النظم الهيدروليكية، والأنظمة اللوجستية الحديثة.' 
              : 'Discover the latest technical insights, comprehensive maintenance guides, and innovative engineering solutions for heavy machinery and advanced hydraulic systems.' 
            }}
          </p>
        </div>

        <!-- 6 Articles Grid (2 Rows of 3) -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-12">
          <article 
            v-for="(article, idx) in articles" 
            :key="article.id" 
            class="bg-white dark:bg-gray-800 rounded-3xl overflow-hidden shadow-lg border border-gray-100 dark:border-gray-700 hover:-translate-y-2 hover:shadow-2xl transition-all duration-300 flex flex-col group"
            data-aos="fade-up"
            :data-aos-delay="(idx % 3) * 100"
          >
            <!-- Article Image -->
            <div class="relative h-52 overflow-hidden bg-gray-100 dark:bg-gray-700">
              <NuxtImg 
                :src="article.image" 
                :alt="article.title[locale]" 
                class="w-full h-full object-cover group-hover:scale-110 transition duration-700" 
                format="webp" 
                loading="lazy" 
              />
              <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent"></div>
              
              <!-- Category Tag -->
              <span class="absolute top-4 rtl:right-4 ltr:left-4 bg-[#191919]/90 backdrop-blur-md text-[#E99E05] font-black text-xs px-3.5 py-1.5 rounded-full border border-[#E99E05]/30">
                {{ article.category[locale] }}
              </span>
            </div>

            <!-- Article Content -->
            <div class="p-6 flex-1 flex flex-col justify-between">
              <div>
                <!-- Date & Read Time -->
                <div class="flex items-center gap-3 text-xs font-bold text-gray-400 mb-3">
                  <span>📅 {{ article.date }}</span>
                  <span>•</span>
                  <span>⏱️ {{ article.readTime[locale] }}</span>
                </div>

                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-3 group-hover:text-primary transition-colors leading-tight line-clamp-2">
                  <NuxtLink :to="localePath(`/blog/${article.id}`)">
                    {{ article.title[locale] }}
                  </NuxtLink>
                </h3>

                <p class="text-gray-600 dark:text-gray-400 text-sm leading-relaxed mb-6 line-clamp-3">
                  {{ article.desc[locale] }}
                </p>
              </div>

              <!-- Read Article Link -->
              <div class="pt-4 border-t border-gray-100 dark:border-gray-700/60 mt-auto">
                <NuxtLink 
                  :to="localePath(`/blog/${article.id}`)" 
                  class="inline-flex items-center gap-2 text-primary hover:text-orange-600 font-black text-sm group-hover:underline transition"
                >
                  <span>{{ locale === 'ar' ? 'قراءة المقال' : 'Read Article' }}</span>
                  <span class="rtl:rotate-180 text-base">&rarr;</span>
                </NuxtLink>
              </div>
            </div>
          </article>
        </div>

        <!-- View More Button -->
        <div class="text-center" data-aos="fade-up">
          <NuxtLink 
            :to="localePath('/blog')" 
            class="inline-flex items-center gap-3 bg-gradient-to-r from-primary to-orange-500 hover:from-orange-500 hover:to-orange-600 text-white font-bold px-8 py-4 rounded-xl transition shadow-lg shadow-primary/30 hover:shadow-primary/50 hover:-translate-y-1 text-lg"
          >
            <span>{{ locale === 'ar' ? 'عرض المزيد من المقالات' : 'Explore All Articles' }}</span>
            <span class="rtl:rotate-180 text-xl">&rarr;</span>
          </NuxtLink>
        </div>
      </div>
    </section>

    <!-- Services Section -->
    <section class="py-24 bg-gray-50 dark:bg-[#0b0f17]">
      <div class="container mx-auto px-4 md:px-8">
        <div class="text-center max-w-3xl mx-auto mb-16" data-aos="fade-up">
          <div class="inline-block bg-primary/10 text-primary font-extrabold px-4 py-1.5 rounded-lg text-sm mb-4">
            {{ locale === 'ar' ? 'خدماتنا الهندسية والصناعية المتكاملة' : 'Comprehensive Engineering & Industrial Services' }}
          </div>
          <h2 class="text-3xl md:text-5xl font-black text-gray-900 dark:text-white mb-6">
            {{ locale === 'ar' ? 'مراحل خدمتنا الثماني' : 'Our Eight Service Stages' }}
          </h2>
          <p class="text-lg md:text-xl text-gray-600 dark:text-gray-400 leading-relaxed">
            {{ locale === 'ar'
              ? 'من دراسة المتطلبات والمعاينة الميدانية حتى قطع الغيار وخدمة ما بعد البيع، تتولى بيستوليكس مشروعك في قطر عبر ثماني مراحل.'
              : 'From the requirements study and site survey to spare parts and after-sales service, Bestolex runs your project in Qatar in eight stages.'
            }}
          </p>
        </div>

        <!-- The eight service stages -->
        <ol class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5 md:gap-6 mb-12">
          <li
            v-for="(service, idx) in homeServices"
            :key="idx"
            class="bg-white dark:bg-gray-800 rounded-2xl shadow border border-gray-100 dark:border-gray-700 p-6 flex flex-col gap-3 hover:-translate-y-1 hover:shadow-xl transition"
            data-aos="fade-up"
            :data-aos-delay="(idx % 4) * 80"
          >
            <div class="flex items-center gap-3">
              <span class="w-10 h-10 shrink-0 rounded-full bg-[#191919] text-[#E99E05] font-black flex items-center justify-center">{{ idx + 1 }}</span>
              <h3 class="text-lg font-bold text-gray-900 dark:text-white leading-snug">{{ service.title[locale] }}</h3>
            </div>
            <p class="text-gray-600 dark:text-gray-400 text-sm leading-relaxed">{{ service.desc[locale] }}</p>
          </li>
        </ol>

        <!-- View More Services Button -->
        <div class="text-center" data-aos="fade-up">
          <NuxtLink 
            :to="localePath('/services')" 
            class="inline-flex items-center gap-3 bg-gradient-to-r from-primary to-orange-500 hover:from-orange-500 hover:to-orange-600 text-white font-bold px-8 py-4 rounded-xl transition shadow-lg shadow-primary/30 hover:shadow-primary/50 hover:-translate-y-1 text-lg"
          >
            <span>{{ locale === 'ar' ? 'عرض المزيد من الخدمات' : 'Explore All Services' }}</span>
            <span class="rtl:rotate-180 text-xl">&rarr;</span>
          </NuxtLink>
        </div>
      </div>
    </section>

    <!-- Why Choose Us Section -->
    <WhyChooseUs />

    <!-- Articles / Blog Section -->
    <section class="py-24 bg-gray-50 dark:bg-gray-900 border-t border-gray-100 dark:border-gray-800 transition-colors">
      <div class="container mx-auto px-4 md:px-8">
        <div class="text-center max-w-3xl mx-auto mb-16" data-aos="fade-up">
          <div class="inline-block bg-primary/10 text-primary font-extrabold px-4 py-1.5 rounded-lg text-sm mb-4">
            {{ locale === 'ar' ? 'المدونة الهندسية' : 'Engineering Blog' }}
          </div>
          <h2 class="text-3xl md:text-5xl font-black text-gray-900 dark:text-white mb-6">
            {{ locale === 'ar' ? 'أحدث المقالات الهندسية' : 'Latest Engineering Articles' }}
          </h2>
          <p class="text-lg md:text-xl text-gray-600 dark:text-gray-400 leading-relaxed">
            {{ locale === 'ar' 
              ? 'أحدث الرؤى الفنية، وأدلة الصيانة، والحلول الهندسية في مجال المعدات الثقيلة والأنظمة اللوجستية في قطر.' 
              : 'Latest technical insights, maintenance guides, and industrial equipment solutions in Qatar.' 
            }}
          </p>
        </div>

        <!-- 6 Articles Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-12">
          <article 
            v-for="(article, idx) in articles" 
            :key="article.id" 
            class="bg-white dark:bg-gray-800 rounded-3xl overflow-hidden shadow-lg border border-gray-100 dark:border-gray-700 hover:-translate-y-2 hover:shadow-2xl transition-all duration-300 flex flex-col group"
            data-aos="fade-up"
            :data-aos-delay="(idx % 3) * 100"
          >
            <!-- Article Image -->
            <div class="relative h-52 overflow-hidden bg-gray-100 dark:bg-gray-700">
              <NuxtImg 
                :src="article.image" 
                :alt="article.title?.[locale] || article.title_ar" 
                class="w-full h-full object-cover group-hover:scale-110 transition duration-700" 
                format="webp" 
                loading="lazy" 
              />
              <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent"></div>
              
              <!-- Category Tag -->
              <span class="absolute top-4 rtl:right-4 ltr:left-4 bg-[#191919]/90 backdrop-blur-md text-[#E99E05] font-black text-xs px-3.5 py-1.5 rounded-full border border-[#E99E05]/30">
                {{ article.category?.[locale] || article.category_ar || 'عام' }}
              </span>
            </div>

            <!-- Article Content -->
            <div class="p-6 flex-1 flex flex-col justify-between">
              <div>
                <!-- Date & Read Time -->
                <div class="flex items-center gap-3 text-xs font-bold text-gray-400 mb-3">
                  <span>📅 {{ article.date }}</span>
                  <span>•</span>
                  <span>⏱️ {{ article.readTime?.[locale] || article.read_time_ar || '5 دقائق' }}</span>
                </div>

                <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-3 group-hover:text-primary transition-colors leading-tight line-clamp-2">
                  <NuxtLink :to="localePath(`/blog/${article.id}`)">
                    {{ article.title?.[locale] || article.title_ar }}
                  </NuxtLink>
                </h3>

                <p class="text-gray-600 dark:text-gray-400 text-sm leading-relaxed mb-6 line-clamp-3">
                  {{ article.desc?.[locale] || article.excerpt_ar }}
                </p>
              </div>

              <!-- Read Article Link -->
              <div class="pt-4 border-t border-gray-100 dark:border-gray-700/60 mt-auto">
                <NuxtLink 
                  :to="localePath(`/blog/${article.id}`)" 
                  class="inline-flex items-center gap-2 text-primary hover:text-orange-600 font-black text-sm group-hover:underline transition"
                >
                  <span>{{ locale === 'ar' ? 'قراءة المقال' : 'Read Article' }}</span>
                  <span class="rtl:rotate-180 text-base">&rarr;</span>
                </NuxtLink>
              </div>
            </div>
          </article>
        </div>

        <!-- View More Button -->
        <div class="text-center" data-aos="fade-up">
          <NuxtLink 
            :to="localePath('/blog')" 
            class="inline-flex items-center gap-3 bg-gradient-to-r from-primary to-orange-500 hover:from-orange-500 hover:to-orange-600 text-white font-bold px-8 py-4 rounded-xl transition shadow-lg shadow-primary/30 hover:shadow-primary/50 hover:-translate-y-1 text-base sm:text-lg"
          >
            <span>{{ locale === 'ar' ? 'عرض كافة المقالات' : 'Explore All Articles' }}</span>
            <span class="rtl:rotate-180 text-xl">&rarr;</span>
          </NuxtLink>
        </div>
      </div>
    </section>

  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import mockProducts from '@/data/products.json'
import mockArticles from '@/data/articles.json'

const { locale } = useI18n()
const localePath = useLocalePath()
const products = ref(mockProducts)

const isAr = computed(() => locale.value === 'ar')

useSeoMeta({
  title: () => isAr.value
    ? 'أنظمة التحميل والنفايات والحماية المحيطية في قطر | بيستوليكس'
    : 'Loading, Waste & Security Equipment in Qatar | Bestolex',
  description: () => isAr.value
    ? 'بيستوليكس تورّد أرصفة التحميل والرافعات المقصية ومكابس النفايات ومصدات الطرق ومفجرات الإطارات والأبواب الصناعية في قطر. الوكيل الحصري لساب تك. اطلب عرض سعر.'
    : 'Bestolex supplies dock levelers, scissor lifts, balers, road blockers, bollards and industrial doors in Qatar. Exclusive SABTECH agent. Request a quote.',
  ogTitle: () => isAr.value ? 'بيستوليكس | معدات التحميل والنفايات والحماية والأبواب الصناعية في قطر' : 'Bestolex | Loading, Waste, Security and Industrial Door Solutions in Qatar',
  ogDescription: () => isAr.value
    ? 'الوكيل الحصري لمنتجات ساب تك في قطر: توريد وتركيب وصيانة معدات المنشآت.'
    : 'Exclusive SABTECH agent in Qatar: supply, installation and maintenance of facility equipment.',
  ogImage: BUSINESS.image
})

useHead(() => ({
  script: [
    {
      type: 'application/ld+json',
      key: 'ld-business',
      innerHTML: JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'LocalBusiness',
        '@id': `${SITE_URL}/#business`,
        'name': isAr.value ? BUSINESS.legalNameAr : BUSINESS.legalNameEn,
        'legalName': BUSINESS.legalNameEn,
        'alternateName': [BUSINESS.legalNameAr, 'Bestolex', 'بيستوليكس'],
        'description': isAr.value ? BUSINESS.descriptionAr : BUSINESS.descriptionEn,
        'sameAs': BUSINESS.sameAs,
        'url': SITE_URL,
        'logo': BUSINESS.logo,
        'image': BUSINESS.image,
        'telephone': BUSINESS.phonePrimary,
        'email': BUSINESS.email,
        'address': BUSINESS.address,
        'openingHoursSpecification': BUSINESS.openingHours,
        'areaServed': { '@type': 'Country', 'name': 'Qatar' },
        'parentOrganization': { '@id': ORG_ID },
        'taxID': '5009022658',
        'identifier': 'CR: 248416'
      })
    }
  ]
}))

// Fetch live articles and display the 6 pinned articles
const { data: blogData } = await useFetch('/api/blog', { query: { view: 'list' } })
const articles = computed(() => {
  const all = (blogData.value && Array.isArray(blogData.value) && blogData.value.length > 0) ? blogData.value : mockArticles
  const featured = all.filter((a) => a.is_featured || a.isFeatured)
  
  if (featured.length >= 6) {
    return featured.slice(0, 6)
  }
  
  // Fill remaining slots from the latest articles if fewer than 6 are pinned
  const nonFeatured = all.filter((a) => !(a.is_featured || a.isFeatured))
  return [...featured, ...nonFeatured].slice(0, 6)
})

// The eight service stages, numbered 1-8 as in the company profile
const homeServices = [
  { title: { ar: 'دراسة المتطلبات والمعاينة الميدانية', en: 'Requirements Study & Site Survey' }, desc: { ar: 'نعاين الموقع ونفهم ظروف التشغيل والمتطلبات الفنية قبل أي عرض.', en: 'We survey the site and understand operating conditions and technical requirements before any offer.' } },
  { title: { ar: 'اختيار الحل والعرض الفني والتجاري', en: 'Solution Selection & Technical and Commercial Proposal' }, desc: { ar: 'نختار الحل المناسب للموقع ونقدّم عرضاً فنياً وتجارياً واضحاً.', en: 'We select the right solution for the site and submit a clear technical and commercial offer.' } },
  { title: { ar: 'التوريد والخدمات اللوجستية', en: 'Supply & Logistics' }, desc: { ar: 'ننسّق التوريد والشحن والتخليص الجمركي حتى وصول المعدات إلى الموقع.', en: 'We coordinate supply, shipping and customs clearance until the equipment reaches the site.' } },
  { title: { ar: 'التركيب أو الإشراف الفني', en: 'Installation or Technical Supervision' }, desc: { ar: 'نركّب المعدات بفريقنا الفني أو نشرف على تركيبها وفق إجراءات السلامة.', en: 'Our technical team installs the equipment or supervises its installation following safety procedures.' } },
  { title: { ar: 'الاختبار والتشغيل والتسليم', en: 'Testing, Commissioning & Handover' }, desc: { ar: 'نختبر النظام ونشغّله ونسلّمه جاهزاً للعمل.', en: 'We test, commission and hand over a working system.' } },
  { title: { ar: 'تدريب المشغلين', en: 'Operator Training' }, desc: { ar: 'ندرّب فريقك على التشغيل الصحيح والاستخدام الآمن وإجراءات الطوارئ.', en: 'We train your team on correct operation, safe use and emergency procedures.' } },
  { title: { ar: 'الصيانة الوقائية والتصحيحية', en: 'Preventive & Corrective Maintenance' }, desc: { ar: 'صيانة دورية واستجابة للأعطال للحفاظ على استمرارية التشغيل.', en: 'Scheduled maintenance and fault response to keep operations running.' } },
  { title: { ar: 'قطع الغيار وخدمة ما بعد البيع', en: 'Spare Parts & After-Sales Service' }, desc: { ar: 'نوفّر قطع الغيار ونتابع المعدات بعد التسليم.', en: 'We supply spare parts and support the equipment after handover.' } }
]

const features = [
  { icon: '🔬', title: 'البحث والتطوير' },
  { icon: '⚙️', title: 'التصنيع والصيانة' },
  { icon: '👷', title: 'مهندسين' },
  { icon: '🤝', title: 'خدمات مابعد البيع' },
  { icon: '🛠️', title: 'التركيب' },
  { icon: '📦', title: 'منتجات حسب الطلب' }
]

const testimonials = [
  { id: 1, name: 'أحمد محمود', company: 'مدير المشتريات', text: 'معدات ذات كفاءة عالية وخدمة ما بعد البيع ممتازة. أنصح بالتعامل معهم. سرعة في التوريد واحترافية في التركيب فاق توقعاتنا.' },
  { id: 2, name: 'مؤسسة السيف للمقاولات', company: 'إدارة المشاريع', text: 'سرعة في التوريد واحترافية في التركيب. أداء المكابس فاق توقعاتنا بكثير وتتحمل العمل الشاق بشكل ممتاز.' },
  { id: 3, name: 'خالد عبد الرحمن', company: 'مصنع البلاستيك الوطني', text: 'أبواب الرول الصناعية لديهم تتحمل ضغط العمل الشاق ومصممة بعناية فائقة. فريق الصيانة متجاوب دائماً.' }
]

const activeTestimonial = ref(0)
let testimonialInterval = null

onMounted(() => {
  testimonialInterval = setInterval(() => {
    activeTestimonial.value = (activeTestimonial.value + 1) % testimonials.length
  }, 4000)
})

onUnmounted(() => {
  if (testimonialInterval) clearInterval(testimonialInterval)
})
</script>

<style scoped>
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 0.5s ease;
}
.fade-slide-enter-from {
  opacity: 0;
  transform: translateY(20px) scale(0.95);
}
.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(-20px) scale(0.95);
}

.animate-marquee {
  animation: marquee 20s linear infinite;
}

@keyframes marquee {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
</style>
