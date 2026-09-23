<template>
  <section class="py-16 md:py-20 relative bg-[#0b1320] text-white overflow-hidden border-t border-b border-gray-800/80">
    <!-- Subtle Ambient Glow -->
    <div class="absolute -top-40 -left-40 w-96 h-96 bg-[#E99E15]/10 rounded-full blur-3xl pointer-events-none"></div>
    <div class="absolute -bottom-40 -right-40 w-96 h-96 bg-[#E99E15]/10 rounded-full blur-3xl pointer-events-none"></div>

    <div class="container mx-auto px-4 md:px-8 relative z-10">
      
      <!-- Section Header -->
      <div class="text-center max-w-4xl mx-auto mb-12 md:mb-14" data-aos="fade-up">
        <!-- Subtitle as regular paragraph -->
        <p class="inline-block bg-[#E99E15]/15 text-[#E99E15] border border-[#E99E15]/30 font-bold px-4 py-1.5 rounded-full text-xs md:text-sm mb-4 tracking-wide shadow-sm">
          {{ isAr ? 'شريك محلي لحلول صناعية متكاملة' : 'Your Local Partner for Integrated Industrial Solutions' }}
        </p>

        <!-- Main Heading H2 -->
        <h2 class="text-2xl sm:text-3xl md:text-4xl lg:text-5xl font-black text-white leading-tight mb-5">
          {{ isAr ? 'لماذا تختار بيستوليكس للحلول والمعدات الصناعية في قطر؟' : 'Why Choose Bestolex for Industrial Solutions and Equipment in Qatar?' }}
        </h2>

        <!-- Intro Paragraph -->
        <p class="text-gray-300 text-sm sm:text-base md:text-lg leading-relaxed max-w-3xl mx-auto">
          {{ isAr 
            ? 'بيستوليكس لتجارة الآلات والمعدات الثقيلة (ذ.م.م) شركة قطرية توفر حلولًا ومعدات صناعية للمشاريع والمنشآت في الدوحة ومختلف أنحاء قطر. تشمل محفظتنا معدات إدارة النفايات وإعادة التدوير، وأنظمة ومعدات أرصفة التحميل، وأنظمة حماية المحيط والتحكم في الدخول، والأبواب الصناعية، والمعدات الثقيلة.' 
            : 'Bestolex Trading of Heavy Equipment and Machinery W.L.L is a Qatari company providing industrial solutions and equipment for projects and facilities in Doha and across Qatar. Our portfolio includes waste management and recycling equipment, loading dock systems and equipment, perimeter protection and access control systems, industrial doors, and heavy equipment.' 
          }}
        </p>
      </div>

      <!-- Features Cards Grid (1 col mobile, 2 col tablet, 3 col desktop) -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-12 max-w-7xl mx-auto">
        <div 
          v-for="(card, idx) in cards" 
          :key="idx"
          class="bg-gray-900/80 backdrop-blur-sm rounded-2xl p-6 sm:p-7 border border-gray-800 hover:border-[#E99E15]/60 hover:shadow-xl hover:shadow-[#E99E15]/10 hover:-translate-y-1 transition-all duration-300 flex flex-col justify-between group"
          data-aos="fade-up"
          :data-aos-delay="(idx % 3) * 100"
        >
          <div>
            <!-- Unified Linear Gold SVG Icon -->
            <div class="w-14 h-14 rounded-xl bg-[#E99E15]/10 border border-[#E99E15]/30 flex items-center justify-center text-[#E99E15] mb-5 group-hover:scale-110 group-hover:bg-[#E99E15] group-hover:text-gray-950 transition-all duration-300 shadow-md">
              <component :is="card.iconComponent" class="w-7 h-7 stroke-[2]" />
            </div>

            <!-- Card Title H3 -->
            <h3 class="text-lg sm:text-xl font-bold text-white mb-3 group-hover:text-[#E99E15] transition-colors leading-snug">
              {{ isAr ? card.titleAr : card.titleEn }}
            </h3>

            <!-- Card Description -->
            <p class="text-gray-400 text-sm leading-relaxed">
              {{ isAr ? card.descAr : card.descEn }}
            </p>
          </div>
        </div>
      </div>

      <!-- Action Button & WhatsApp Option -->
      <div class="text-center mb-8" data-aos="fade-up">
        <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
          <!-- Site Survey Request Button -->
          <button 
            type="button"
            @click="isModalOpen = true"
            class="w-full sm:w-auto inline-flex items-center justify-center gap-3 bg-gradient-to-r from-[#E99E15] to-orange-500 hover:from-orange-500 hover:to-orange-600 text-white font-extrabold px-8 py-4 rounded-xl transition duration-300 shadow-lg shadow-[#E99E15]/30 hover:shadow-[#E99E15]/50 hover:scale-105 text-base sm:text-lg cursor-pointer"
          >
            <!-- Calendar/Survey Icon -->
            <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 stroke-[2.5]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
              <rect width="18" height="18" x="3" y="4" rx="2" ry="2"/>
              <line x1="16" x2="16" y1="2" y2="6"/>
              <line x1="8" x2="8" y1="2" y2="6"/>
              <line x1="3" x2="21" y1="10" y2="10"/>
              <path d="m9 16 2 2 4-4"/>
            </svg>
            <span>{{ isAr ? 'اطلب معاينة ميدانية' : 'Request a Site Survey' }}</span>
          </button>

          <!-- Direct WhatsApp Button -->
          <a 
            :href="whatsappUrl"
            target="_blank"
            rel="noopener noreferrer"
            class="w-full sm:w-auto inline-flex items-center justify-center gap-3 bg-white/10 hover:bg-white/20 text-white border border-white/20 font-bold px-6 py-4 rounded-xl transition duration-300 hover:scale-105 text-base cursor-pointer"
          >
            <svg class="w-5 h-5 fill-current text-green-400" viewBox="0 0 24 24">
              <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/>
            </svg>
            <span>{{ isAr ? 'تواصل عبر واتساب' : 'Chat on WhatsApp' }}</span>
          </a>
        </div>
      </div>

      <!-- Tagline & Clearance Space (100px bottom clearance for floating buttons) -->
      <div class="text-center pt-6 pb-24 md:pb-28 border-t border-gray-800/60 max-w-xl mx-auto" data-aos="fade-up">
        <p class="text-base sm:text-lg md:text-xl font-bold tracking-wide text-[#E99E15] drop-shadow-sm">
          {{ isAr ? 'قوة تدفع أعمالكم… ثقة تدوم' : 'Power That Drives Your Business. Trust That Lasts.' }}
        </p>
      </div>

    </div>

    <!-- Booking / Site Survey Appointment Modal -->
    <BookAppointmentModal :is-open="isModalOpen" @close="isModalOpen = false" />
  </section>
</template>

<script setup>
import { ref, computed, h } from 'vue'

const { locale } = useI18n()
const isAr = computed(() => locale.value === 'ar')

const isModalOpen = ref(false)

const whatsappUrl = computed(() => {
  const text = isAr.value 
    ? 'مرحباً بيستوليكس، أود طلب معاينة ميدانية لمشروعنا.' 
    : 'Hello Bestolex, I would like to request a site survey for our project.'
  return `https://wa.me/97450708833?text=${encodeURIComponent(text)}`
})

// Lucide Linear Icons as inline render functions (Gold stroke)
const BadgeCheckIcon = () => h('svg', {
  viewBox: '0 0 24 24',
  fill: 'none',
  stroke: 'currentColor',
  'stroke-linecap': 'round',
  'stroke-linejoin': 'round'
}, [
  h('path', { d: 'M3.85 8.62a4 4 0 0 1 4.78-4.77 4 4 0 0 1 6.74 0 4 4 0 0 1 4.78 4.78 4 4 0 0 1 0 6.74 4 4 0 0 1-4.77 4.78 4 4 0 0 1-6.75 0 4 4 0 0 1-4.78-4.77 4 4 0 0 1 0-6.76Z' }),
  h('path', { d: 'm9 12 2 2 4-4' })
])

const ClipboardCheckIcon = () => h('svg', {
  viewBox: '0 0 24 24',
  fill: 'none',
  stroke: 'currentColor',
  'stroke-linecap': 'round',
  'stroke-linejoin': 'round'
}, [
  h('rect', { width: '8', height: '4', x: '8', y: '2', rx: '1', ry: '1' }),
  h('path', { d: 'M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2' }),
  h('path', { d: 'm9 14 2 2 4-4' })
])

const TruckIcon = () => h('svg', {
  viewBox: '0 0 24 24',
  fill: 'none',
  stroke: 'currentColor',
  'stroke-linecap': 'round',
  'stroke-linejoin': 'round'
}, [
  h('path', { d: 'M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2' }),
  h('path', { d: 'M15 18H9' }),
  h('path', { d: 'M19 18h2a1 1 0 0 0 1-1v-3.65a1 1 0 0 0-.22-.624l-3.48-4.35A1 1 0 0 0 17.52 8H14' }),
  h('circle', { cx: '17', cy: '18', r: '2' }),
  h('circle', { cx: '7', cy: '18', r: '2' })
])

const GraduationCapIcon = () => h('svg', {
  viewBox: '0 0 24 24',
  fill: 'none',
  stroke: 'currentColor',
  'stroke-linecap': 'round',
  'stroke-linejoin': 'round'
}, [
  h('path', { d: 'M21.42 10.922a1 1 0 0 0-.019-1.838L12.83 5.18a2 2 0 0 0-1.66 0L2.6 9.08a1 1 0 0 0 0 1.832l8.57 3.908a2 2 0 0 0 1.66 0z' }),
  h('path', { d: 'M22 10v6' }),
  h('path', { d: 'M6 12.5V16a6 3 0 0 0 12 0v-3.5' })
])

const WrenchIcon = () => h('svg', {
  viewBox: '0 0 24 24',
  fill: 'none',
  stroke: 'currentColor',
  'stroke-linecap': 'round',
  'stroke-linejoin': 'round'
}, [
  h('path', { d: 'M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z' })
])

const Building2Icon = () => h('svg', {
  viewBox: '0 0 24 24',
  fill: 'none',
  stroke: 'currentColor',
  'stroke-linecap': 'round',
  'stroke-linejoin': 'round'
}, [
  h('path', { d: 'M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18Z' }),
  h('path', { d: 'M6 12H4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h2' }),
  h('path', { d: 'M18 9h2a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-2' }),
  h('path', { d: 'M10 6h4' }),
  h('path', { d: 'M10 10h4' }),
  h('path', { d: 'M10 14h4' }),
  h('path', { d: 'M10 18h4' })
])

const cards = [
  {
    iconComponent: BadgeCheckIcon,
    titleAr: '1. وكيل حصري لـ SABTECH في قطر',
    titleEn: '1. Exclusive SABTECH Agent in Qatar',
    descAr: 'نوفر منتجات وحلول SABTECH الأصلية من المصنّع مباشرة، مع الدعم الفني وضمان لمدة سنة ضد عيوب التصنيع وفق شروط الضمان المعتمدة.',
    descEn: 'We supply genuine SABTECH products and solutions directly from the manufacturer, with technical support and a one-year warranty against manufacturing defects, subject to the approved warranty terms.'
  },
  {
    iconComponent: ClipboardCheckIcon,
    titleAr: '2. المعاينة الميدانية والدعم الهندسي',
    titleEn: '2. Site Survey and Engineering Support',
    descAr: 'نزور موقع المشروع في قطر، وندرس المتطلبات الفنية والتشغيلية وظروف الموقع، ثم نساعد في اختيار المعدات والمواصفات الأنسب للتطبيق المطلوب.',
    descEn: 'We visit your project site in Qatar, study its technical, operational and site conditions, then help you select the most suitable equipment and specifications for the application.'
  },
  {
    iconComponent: TruckIcon,
    titleAr: '3. التوريد والتركيب والتشغيل',
    titleEn: '3. Supply, Installation and Commissioning',
    descAr: 'نتولى توريد المعدات والأنظمة، وتنفيذ أعمال التركيب أو الإشراف الفني، ثم الاختبار والتشغيل والتسليم.',
    descEn: 'We handle the supply of equipment and systems, installation or technical supervision, followed by testing, commissioning and handover.'
  },
  {
    iconComponent: GraduationCapIcon,
    titleAr: '4. تدريب فريق التشغيل',
    titleEn: '4. Operator Training',
    descAr: 'نوفّر تدريبًا عمليًا لفريق التشغيل على الاستخدام الآمن والصحيح للمعدات والأنظمة وإجراءات تشغيلها الأساسية.',
    descEn: 'We provide hands-on training for your operating team on the safe and correct use of equipment and systems and their basic operating procedures.'
  },
  {
    iconComponent: WrenchIcon,
    titleAr: '5. الصيانة وقطع الغيار',
    titleEn: '5. Maintenance and Spare Parts',
    descAr: 'صيانة وقائية وتصحيحية ودعم فني، مع قطع غيار أصلية أو معتمدة وفق نوع المعدات ومتطلبات المصنّع.',
    descEn: 'Preventive and corrective maintenance and technical support, with genuine or approved spare parts according to equipment type and manufacturer requirements.'
  },
  {
    iconComponent: Building2Icon,
    titleAr: '6. حلول لقطاعات متعددة',
    titleEn: '6. Solutions for Multiple Sectors',
    descAr: 'نوفر معدات وأنظمة لقطاعات المقاولات والمستودعات والمصانع والموانئ والمراكز اللوجستية والمنشآت الحكومية والحيوية والمجمعات التجارية والفنادق في قطر.',
    descEn: 'We supply equipment and systems for contracting, warehousing, manufacturing, ports, logistics centers, government and critical facilities, commercial complexes and hotels in Qatar.'
  }
]
</script>
