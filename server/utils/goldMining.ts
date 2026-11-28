// Gold-mining section (/gold-mining): the production line, the support sections, the catalogues and the family
// cards, built from data/products.json (category "gold-mining") and the family tables in
// server/assets/catalog/mining. Layout follows the approved design board "1 · صفحة قسم تعدين الذهب" and its
// stage and family pages. Family and model counts in the line come from the catalogue covers; the search box
// counts what is published on the site.
import { catalog } from './catalog'

type L = { ar: string, en: string }
const L = (ar: string, en: string): L => ({ ar, en })

export type Stage = {
  id: string
  n: number                 // position in the production line (support sections: 0)
  kind: 'line' | 'support'
  code: string              // catalogue code(s)
  edition: string
  sub?: string              // products.json subcategory with the family pages
  title: L
  short: L                  // one line for the hub
  lead: L                   // stage page header
  families: number          // from the catalogue cover
  models: number
  image: string             // hub image
  cover: string             // stage page header image (catalogue cover)
  licensed?: boolean        // BXC-11: a card only, no products or download (owner, 28 Nov 2026)
  cta: { title: L, text: L }
  groups?: { id: string, title: L, note?: L }[]
  types?: { id: string, chip: L, badge: L }[]
  how?: { title: L, text: L }[]
}

const CTA_DEFAULT = {
  title: L('لا تعرف أي موديل يناسب موقعك؟', 'Not sure which model fits your site?'),
  text: L('أرسل وصف موقعك والطاقة المطلوبة، ونقترح عليك الموديل.', 'Send us a short description of your site and the capacity you need, and we suggest the model.')
}

export const STAGES: Stage[] = [
  {
    id: 'exploration-drilling', n: 1, kind: 'line', code: 'BXC-02', edition: '4', sub: 'exploration-drilling',
    title: L('التنقيب والحفر واستخراج الخام', 'Exploration, Drilling & Ore Extraction'),
    short: L('أجهزة المسح وكشف المعادن، وحفارات الاستكشاف واللب، والمثاقب الصخرية والفلق.', 'Survey instruments and metal detectors, exploration and core rigs, rock drills and rock splitting.'),
    lead: L('أجهزة المسح والكشف، وحفارات الاستكشاف اللبّية والدوران العكسي وDTH، والمثاقب الصخرية والضواغط، وأدوات الفلق والقطع والتهوية، من البحث عن الخام إلى استخراجه.',
      'Survey instruments and detectors, core, RC and DTH exploration rigs, rock drills and compressors, and splitting, cutting and ventilation equipment, from finding the ore to extracting it.'),
    families: 15, models: 163,
    image: '/products/metal-detectors-water-well-drill-rigs/metal-detectors-water-well-drill-rigs.webp', cover: '/gold-mining/covers/bxc-02.webp',
    cta: { title: L('لا تعرف أي حفارة تناسب موقعك؟', 'Not sure which rig fits your site?'),
      text: L('أرسل العمق المطلوب، وقطر الثقب، ونوع الصخر، ومصدر الطاقة في الموقع، ونقترح عليك الموديل.', 'Send us the depth and hole diameter you need, the rock type and the power available on site, and we suggest the model.') },
    types: [
      { id: 'survey', chip: L('مسح وكشف', 'Survey & detection'), badge: L('مسح وكشف', 'Survey & detection') },
      { id: 'rigs', chip: L('حفارات', 'Drill rigs'), badge: L('حفارات', 'Drill rigs') },
      { id: 'drills', chip: L('مثاقب وضواغط', 'Rock drills & air'), badge: L('مثاقب وضواغط', 'Rock drills & air') },
      { id: 'splitting', chip: L('فلق وقطع', 'Splitting & cutting'), badge: L('فلق وقطع', 'Splitting & cutting') },
      { id: 'underground', chip: L('تهوية وتدعيم', 'Ventilation & support'), badge: L('تهوية وتدعيم', 'Ventilation & support') }
    ],
    how: [
      { title: L('الغرض', 'The job'), text: L('مسح وكشف، أو حفر استكشافي وأخذ عينات، أو إنتاج وتكسير الصخر في الموقع.', 'Survey and detection, exploration drilling and sampling, or production and breaking rock on site.') },
      { title: L('العمق وقطر الثقب', 'Depth and hole size'), text: L('قارنهما بعمودي العمق والقطر في جدول الحفارة.', 'Compare them with the depth and diameter columns in the rig table.') },
      { title: L('صلابة الصخر', 'Rock hardness'), text: L('الصخر الصلب يحتاج مطرقة DTH أو مثقاباً صخرياً، والتربة والصخر الطري يكفيهما الحفر الدوراني.', 'Hard rock needs a DTH hammer or a rock drill; soil and soft rock can be drilled rotary.') },
      { title: L('مصدر الطاقة في الموقع', 'Power on site'), text: L('ديزل أو كهرباء أو هواء مضغوط. المثاقب الهوائية تحتاج ضاغطاً بالتدفق والضغط المناسبين.', 'Diesel, electric or compressed air. Air drills need a compressor with the right flow and pressure.') }
    ]
  },
  {
    id: 'drilling-consumables', n: 2, kind: 'line', code: 'BXC-03', edition: '4', sub: 'drilling-consumables',
    title: L('مستهلكات الحفر', 'Drilling Consumables'),
    short: L('مطارق ولقم DTH، وأدوات الدوران العكسي، ولقم ثلاثية الأقماع وPDC.', 'DTH hammers and bits, reverse-circulation tools, tricone and PDC bits.'),
    lead: L('مطارق ولقم DTH للضغط العالي والمنخفض، وأدوات الدوران العكسي، وأنظمة التغليف، ولقم ثلاثية المخاريط وPDC، وأدوات المطرقة العلوية وماكينات التجليخ.',
      'High- and low-pressure DTH hammers and bits, reverse-circulation tools, casing systems, tricone and PDC bits, top-hammer tools and bit grinders.'),
    families: 13, models: 270,
    image: '/products/high-pressure-dth-bits/high-pressure-dth-bits.webp', cover: '/gold-mining/covers/bxc-03.webp',
    cta: { title: L('لا تعرف أي لقمة أو مطرقة تناسب حفارتك؟', 'Not sure which bit or hammer fits your rig?'),
      text: L('أرسل موديل الحفارة أو المطرقة، وقطر الثقب، وضغط الضاغط، ونقترح عليك الأدوات.', 'Send us the rig or hammer model, the hole diameter and the compressor pressure, and we suggest the tools.') },
    types: [
      { id: 'dth', chip: L('DTH', 'DTH'), badge: L('DTH', 'DTH') },
      { id: 'rc', chip: L('RC والتغليف', 'RC & casing'), badge: L('RC والتغليف', 'RC & casing') },
      { id: 'rotary', chip: L('دوراني ولبّي', 'Rotary & core'), badge: L('دوراني ولبّي', 'Rotary & core') },
      { id: 'top', chip: L('المطرقة العلوية', 'Top hammer'), badge: L('المطرقة العلوية', 'Top hammer') },
      { id: 'workshop', chip: L('الورشة والقطع', 'Workshop & picks'), badge: L('الورشة والقطع', 'Workshop & picks') }
    ],
    how: [
      { title: L('طريقة الحفر', 'Drilling method'), text: L('DTH أو دوران عكسي أو مطرقة علوية أو حفر دوراني، ولكل طريقة أدواتها.', 'DTH, reverse circulation, top hammer or rotary: each method has its own tools.') },
      { title: L('قطر الثقب', 'Hole diameter'), text: L('يحدد قطر اللقمة والمطرقة المناسبين.', 'It sets the bit and hammer size.') },
      { title: L('الساق ونوع السن', 'Shank and thread'), text: L('يجب أن تطابق مطرقتك أو مثقابك، مثل DHD وQL وSD، أو R32 وT38.', 'They must match your hammer or drill, such as DHD, QL and SD, or R32 and T38.') },
      { title: L('ضغط الضاغط وتدفقه', 'Compressor pressure and flow'), text: L('قارنهما بضغط التشغيل واستهلاك الهواء في جدول المطرقة.', 'Compare them with the working pressure and air use in the hammer table.') }
    ]
  },
  {
    id: 'crushing-grinding-screening', n: 3, kind: 'line', code: 'BXC-04', edition: '6', sub: 'crushing-grinding-screening',
    title: L('التكسير والطحن والغربلة', 'Crushing, Grinding & Screening'),
    short: L('الكسارات والطواحين والمصنّفات والمغذيات والغرابيل والسيور وقطع التآكل.', 'Crushers, mills, classifiers, feeders, screens, conveyors and wear parts.'),
    lead: L('الكسارات والطواحين والمصنّفات والمغذيات والغرابيل والسيور، وفواصل الحديد الشارد وقطع التآكل، لتحويل الخام إلى لب جاهز للتركيز أو المعالجة.',
      'Crushers, mills, classifiers, feeders, screens and conveyors, tramp-iron separators and wear parts, to turn ore into a slurry ready for concentration or processing.'),
    families: 51, models: 1128,
    image: '/products/jaw-crushers/jaw-crushers.webp', cover: '/gold-mining/covers/bxc-04.webp',
    cta: { title: L('لا تعرف أي كسارة تناسب موقعك؟', 'Not sure which crusher fits your site?'),
      text: L('أرسل نوع الخام، والطاقة المطلوبة بالطن في الساعة، وأكبر حجم للحجر، ونقترح عليك الموديل.', 'Send us the ore type, the capacity you need in tonnes per hour and the largest rock size, and we suggest the model.') },
    groups: [
      { id: 'crushers', title: L('الكسارات', 'Crushers'), note: L('المقاسات الإضافية في الكتالوج مدمجة في عائلاتها.', 'Additional sizes in the catalogue are merged into their families.') },
      { id: 'grinding', title: L('الطحن والتصنيف', 'Grinding & Classifying') },
      { id: 'feeding', title: L('التغذية والغربلة والنقل', 'Feeding, Screening & Conveying') },
      { id: 'wear', title: L('قطع التآكل والغيار', 'Wear & Spare Parts') }
    ],
    types: [
      { id: 'primary', chip: L('أولي', 'Primary'), badge: L('تكسير أولي', 'Primary crushing') },
      { id: 'secondary', chip: L('ثانوي', 'Secondary'), badge: L('تكسير ثانوي', 'Secondary crushing') },
      { id: 'fine', chip: L('ناعم', 'Fine'), badge: L('تكسير ناعم', 'Fine crushing') },
      { id: 'single', chip: L('مرحلة واحدة', 'Single stage'), badge: L('مرحلة واحدة', 'Single stage') },
      { id: 'mobile', chip: L('متنقل', 'Mobile'), badge: L('محطة متنقلة', 'Mobile plant') }
    ],
    how: [
      { title: L('الطاقة المطلوبة', 'Capacity'), text: L('بالطن في الساعة، وهي تحدد السلسلة: الصغيرة للمواقع الصغيرة، والثقيلة للعمليات الكبيرة.', 'In tonnes per hour. It sets the series: compact models for small sites, heavy series for large operations.') },
      { title: L('حجم الحجر الداخل', 'Feed size'), text: L('يجب أن يكون أصغر من «أقصى حجم تغذية» في الجدول.', 'It must be smaller than the “max. feed size” in the table.') },
      { title: L('حجم الناتج', 'Product size'), text: L('الحجم المطلوب قبل المرحلة التالية: كسارة ثانوية أو طاحونة.', 'The size the next stage needs: a secondary crusher or a mill.') },
      { title: L('مصدر الطاقة في الموقع', 'Power on site'), text: L('الكسارات الفكية الصغيرة متوفرة بمحرك ديزل، ومحطات الجنزير بإدارة مزدوجة ديزل وكهرباء.', 'Small jaw crushers come with a diesel engine option, and crawler plants have diesel–electric dual drive.') }
    ]
  },
  {
    id: 'washing-gold-concentration', n: 4, kind: 'line', code: 'BXC-05', edition: '4', sub: 'washing-gold-concentration',
    title: L('الغسيل وتركيز الذهب', 'Washing & Gold Concentration'),
    short: L('غسالات الخام وأجهزة الجيج والمركّزات الطاردة المركزية والمجاري الحلزونية والطاولات الهزّازة والكراكات.', 'Ore washers, jigs, centrifugal concentrators, spirals, shaking tables and dredgers.'),
    lead: L('غسالات الخام وأجهزة الجيج والمركّزات الطاردة المركزية والمجاري الحلزونية والطاولات الهزّازة والكراكات، لفصل الذهب الحر وتركيزه.',
      'Ore washers, jigs, centrifugal concentrators, spirals, shaking tables and dredgers, to recover and concentrate free gold.'),
    families: 16, models: 200,
    image: '/gold-mining/stages/washing-gold-concentration.webp', cover: '/gold-mining/covers/bxc-05.webp',
    cta: { title: L('لا تعرف أي معدة تناسب خامك؟', 'Not sure which equipment fits your ore?'),
      text: L('أرسل نوع الرواسب (غريني أو طيني أو خام مطحون)، وحجم الذهب، والطاقة المطلوبة، ومصدر الماء في الموقع، ونقترح عليك خط الغسيل والتركيز.', 'Send us the deposit type (alluvial, clay-bound or ground ore), the gold particle size, the capacity you need and the water on site, and we suggest the washing and concentration line.') },
    types: [
      { id: 'washing', chip: L('الغسيل', 'Washing'), badge: L('غسيل الخام', 'Ore washing') },
      { id: 'jigs', chip: L('الجيج', 'Jigs'), badge: L('أجهزة الجيج', 'Jigs') },
      { id: 'concentration', chip: L('التركيز', 'Concentration'), badge: L('تركيز الذهب', 'Gold concentration') },
      { id: 'magnetic', chip: L('الفصل المغناطيسي', 'Magnetic'), badge: L('فصل مغناطيسي', 'Magnetic separation') },
      { id: 'placer', chip: L('الرواسب الغرينية', 'Placer & dredging'), badge: L('رواسب غرينية', 'Placer & dredging') }
    ],
    how: [
      { title: L('نوع الرواسب', 'Deposit type'), text: L('الرواسب الطينية تحتاج غسالة أسطوانية أو غسالة طين أولاً، والرمل النظيف يذهب مباشرة إلى الغربلة والتركيز.', 'Clay-bound deposits need a scrubber or log washer first; clean sand goes straight to screening and concentration.') },
      { title: L('حجم الذهب', 'Gold particle size'), text: L('الذهب الخشن والرقائقي للجيج ومجاري الغسيل، والناعم للمركّزات الطاردة والطاولات الهزّازة.', 'Coarse and flaky gold suits jigs and sluices; fine gold suits centrifugal concentrators and shaking tables.') },
      { title: L('الطاقة المطلوبة', 'Capacity'), text: L('قارنها بعمود الطاقة في الجدول، واختر كل معدة في الخط بالطاقة نفسها.', 'Compare it with the capacity column, and size every machine in the line to the same throughput.') },
      { title: L('الماء في الموقع', 'Water on site'), text: L('حيث الماء قليل اختر أجهزة جيج JT الموفرة والمركّزات الحلزونية التي لا تحتاج كهرباء.', 'Where water is scarce, choose water-saving JT jigs and spirals that need no power.') }
    ]
  },
  {
    id: 'ore-processing-plants', n: 5, kind: 'line', code: 'BXC-06', edition: '7',
    title: L('معالجة الخام والمصانع', 'Ore Processing & Plants'),
    short: L('مصانع معالجة متكاملة، والتعويم، وأحواض الترشيح، واسترجاع الذهب، والمكثفات والمكابس.', 'Complete processing plants, flotation, leaching tanks, gold recovery, thickeners and filter presses.'),
    lead: L('مصانع معالجة متكاملة، والتعويم، وأحواض الترشيح، واسترجاع الذهب، والمكثفات والمكابس.', 'Complete processing plants, flotation, leaching tanks, gold recovery, thickeners and filter presses.'),
    families: 12, models: 325,
    image: '/gold-mining/stages/ore-processing-plants.webp', cover: '/gold-mining/covers/bxc-06.webp', cta: CTA_DEFAULT
  },
  {
    id: 'process-chemicals', n: 6, kind: 'line', code: 'BXC-11', edition: '1', licensed: true,
    title: L('كيماويات المعالجة', 'Process Chemicals'),
    short: L('مواد التلبيد والتخثير، وكواشف المعالجة، والكربون المنشط.', 'Flocculants and coagulants, processing reagents and activated carbon.'),
    lead: L('مواد التلبيد والتخثير، وكواشف المعالجة، والكربون المنشط.', 'Flocculants and coagulants, processing reagents and activated carbon.'),
    families: 2, models: 80,
    image: '/gold-mining/stages/process-chemicals.webp', cover: '', cta: CTA_DEFAULT
  },
  {
    id: 'smelting-refining', n: 7, kind: 'line', code: 'BXC-08', edition: '7', sub: 'smelting-refining',
    title: L('الصهر والتنقية', 'Smelting & Refining'),
    short: L('أفران صهر الذهب بالحث، والبوتقات، والطوب الحراري، والعوازل.', 'Induction gold-melting furnaces, crucibles, refractory bricks and insulation.'),
    lead: L('أفران صهر الذهب بالحث من 1 إلى 500 كجم، وبوتقات الكوارتز وكربيد السيليكون، والطوب والخرسانات الحرارية، والألياف الخزفية لعزل الأفران، من الصهرة الأولى إلى السبيكة.',
      'Induction gold-melting furnaces from 1 to 500 kg, quartz and silicon-carbide crucibles, firebricks and castables, and ceramic fibre to insulate the furnace, from the first melt to the bar.'),
    families: 6, models: 144,
    image: '/gold-mining/stages/smelting-refining.webp', cover: '/gold-mining/covers/bxc-08.webp',
    cta: { title: L('لا تعرف أي فرن يناسب إنتاجك؟', 'Not sure which furnace fits your output?'),
      text: L('أرسل كمية الذهب في كل صهرة، وعدد الصهرات في اليوم، ومصدر الكهرباء في الموقع، ونقترح عليك الفرن والبوتقة.', 'Send us the gold per melt, the melts per day and the power on site, and we suggest the furnace and crucible.') },
    types: [
      { id: 'furnaces', chip: L('أفران الصهر', 'Furnaces'), badge: L('أفران الصهر', 'Melting furnaces') },
      { id: 'crucibles', chip: L('البوتقات', 'Crucibles'), badge: L('البوتقات', 'Crucibles') },
      { id: 'refractories', chip: L('الحراريات والعزل', 'Refractories & insulation'), badge: L('الحراريات والعزل', 'Refractories & insulation') }
    ],
    how: [
      { title: L('الكمية في كل صهرة', 'Gold per melt'), text: L('قارنها بعمود سعة الصهر في جدول الفرن، واترك هامشاً للبوتقة.', 'Compare it with the melting capacity column in the furnace table, with a margin for the crucible.') },
      { title: L('الكهرباء في الموقع', 'Power on site'), text: L('الوحدات الصغيرة تعمل على 220 فولت، والأكبر تحتاج 380 فولت ثلاثية الأطوار أو مولداً بالقدرة نفسها.', 'Small units run on 220 V; larger ones need 380 V three-phase or a generator of the same rating.') },
      { title: L('التبريد', 'Cooling'), text: L('أفران الحث مبرّدة بالماء: جهّز ماءً بالضغط المذكور أو مبرّداً هوائياً.', 'Induction furnaces are water cooled: plan water at the stated pressure, or an air-cooled chiller.') },
      { title: L('البوتقة والبطانة', 'Crucible and lining'), text: L('اختر البوتقة بقطر الفرن وكمية الصهرة، والطوب أو الخرسانة الحرارية بحرارة التشغيل.', 'Choose the crucible by furnace diameter and melt size, and the bricks or castable by service temperature.') }
    ]
  },
  {
    id: 'pumps-slurry-handling', n: 0, kind: 'support', code: 'BXC-07', edition: '5',
    title: L('المضخات ونقل اللب', 'Pumps & Slurry Handling'),
    short: L('مضخات اللب والحصى والنزح، والصمامات والأنابيب والخراطيم.', 'Slurry, gravel and dewatering pumps, valves, pipes and hoses.'),
    lead: L('مضخات اللب والحصى والنزح، والصمامات والأنابيب والخراطيم.', 'Slurry, gravel and dewatering pumps, valves, pipes and hoses.'),
    families: 17, models: 174,
    image: '/gold-mining/support/pumps-slurry-handling.webp', cover: '/gold-mining/covers/bxc-07.webp', cta: CTA_DEFAULT
  },
  {
    id: 'laboratory-assay', n: 0, kind: 'support', code: 'BXC-09', edition: '6',
    title: L('المختبر والتحليل', 'Laboratory & Assay'),
    short: L('تحضير العينات، والتحليل بالنار، والموازين، وأجهزة XRF وAAS.', 'Sample preparation, fire assay, balances, and XRF and AAS instruments.'),
    lead: L('تحضير العينات، والتحليل بالنار، والموازين، وأجهزة XRF وAAS.', 'Sample preparation, fire assay, balances, and XRF and AAS instruments.'),
    families: 16, models: 294,
    image: '/gold-mining/support/laboratory-assay.webp', cover: '/gold-mining/covers/bxc-09.webp', cta: CTA_DEFAULT
  },
  {
    id: 'fleet-support', n: 0, kind: 'support', code: 'BXC-10', edition: '4',
    title: L('دعم الأسطول', 'Fleet Support'),
    short: L('إطارات الشاحنات واللوادر، والورشة، والموازين الجسرية، وأبراج الإنارة.', 'Truck and loader tyres, workshop equipment, weighbridges and lighting towers.'),
    lead: L('إطارات الشاحنات واللوادر، والورشة، والموازين الجسرية، وأبراج الإنارة.', 'Truck and loader tyres, workshop equipment, weighbridges and lighting towers.'),
    families: 12, models: 201,
    image: '/gold-mining/support/fleet-support.webp', cover: '/gold-mining/covers/bxc-10.webp', cta: CTA_DEFAULT
  },
  {
    id: 'safety-site-facilities', n: 0, kind: 'support', code: 'BXS-01 · BXS-02', edition: '2 · 1',
    title: L('السلامة ومرافق الموقع', 'Safety & Site Facilities'),
    short: L('معدات الوقاية، وكشف الغاز، والحريق، والكرفانات والأسوار.', 'Protective equipment, gas detection, fire safety, cabins and fencing.'),
    lead: L('معدات الوقاية، وكشف الغاز، والحريق، والكرفانات والأسوار.', 'Protective equipment, gas detection, fire safety, cabins and fencing.'),
    families: 17, models: 227,
    image: '/gold-mining/support/safety-site-facilities.webp', cover: '/gold-mining/covers/bxs-01.webp', cta: CTA_DEFAULT
  }
]

// Family pages: their place in the stage (group tab) and their chip.
const FAMILY_META: Record<string, { group?: string, type?: string }> = {
  'trommel-scrubbers-log-washers': { type: 'washing' },
  'spiral-washers-attrition-scrubbers': { type: 'washing' },
  'trommels-scrubbers-additional-models': { type: 'washing' },
  'alluvial-gold-jigs': { type: 'jigs' },
  'heavy-duty-laboratory-jigs': { type: 'jigs' },
  'centrifugal-concentrators': { type: 'concentration' },
  'spiral-concentrators': { type: 'concentration' },
  'shaking-tables': { type: 'concentration' },
  'gravity-concentrators-additional-models': { type: 'concentration' },
  'drum-magnetic-separators': { type: 'magnetic' },
  'high-intensity-magnetic-separators': { type: 'magnetic' },
  'magnetic-reclaimers-pulleys': { type: 'magnetic' },
  'mobile-gold-washing-plants': { type: 'placer' },
  'sluice-boxes-gold-carpets-pans': { type: 'placer' },
  'dredgers': { type: 'placer' },
  'amphibious-dredgers-excavators': { type: 'placer' },
  'induction-gold-smelting-furnaces': { type: 'furnaces' },
  'gold-melting-furnaces': { type: 'furnaces' },
  'firebricks-electrodes-induction-units': { type: 'refractories' },
  'fused-quartz-silicon-carbide-crucibles': { type: 'crucibles' },
  'refractories-quartz-glass-ceramics': { type: 'refractories' },
  'ceramic-fibre-furnace-insulation': { type: 'refractories' },
  'geophysical-survey-instruments': { type: 'survey' },
  'metal-detectors-water-well-drill-rigs': { type: 'survey' },
  'core-rc-exploration-drill-rigs': { type: 'rigs' },
  'dth-water-well-drill-rigs': { type: 'rigs' },
  'line-drilling-machines-compact-dth-drillers': { type: 'rigs' },
  'air-leg-rock-drills': { type: 'drills' },
  'hand-held-gasoline-rock-drills': { type: 'drills' },
  'diesel-air-compressors': { type: 'drills' },
  'pneumatic-picks-wedges-cracking-mortar': { type: 'drills' },
  'paving-breakers-electric-hammers-hydraulic-power-packs': { type: 'drills' },
  'hydraulic-rock-splitters': { type: 'splitting' },
  'diamond-wire-saws': { type: 'splitting' },
  'block-pushing-handling': { type: 'splitting' },
  'mine-ventilation-fans-ground-support-mesh': { type: 'underground' },
  'dth-hammers-bits': { type: 'dth' },
  'high-pressure-dth-bits': { type: 'dth' },
  'low-medium-pressure-dth-tools': { type: 'dth' },
  'dth-pipes-back-hammers-breakout-benches': { type: 'dth' },
  'reverse-circulation-rc-tools': { type: 'rc' },
  'overburden-casing-systems': { type: 'rc' },
  'tricone-pdc-core-drilling-tools': { type: 'rotary' },
  'tapered-threaded-drilling-tools': { type: 'top' },
  'button-bit-grinders': { type: 'workshop' },
  'cutter-picks-additional-cir-hammers': { type: 'workshop' },
  'jaw-crushers': { group: 'crushers', type: 'primary' },
  'gyratory-impact-crushers': { group: 'crushers', type: 'primary' },
  'c-series-jaw-gyratory-impact-crushers': { group: 'crushers', type: 'primary' },
  'hydraulic-cone-crushers': { group: 'crushers', type: 'secondary' },
  'single-cylinder-cone-crushers': { group: 'crushers', type: 'secondary' },
  'symons-spring-cone-crushers': { group: 'crushers', type: 'secondary' },
  'gp-hps-hydraulic-cone-crushers': { group: 'crushers', type: 'secondary' },
  'roller-crushers': { group: 'crushers', type: 'secondary' },
  'vertical-shaft-impact-crushers': { group: 'crushers', type: 'fine' },
  'sand-makers-fine-crushers': { group: 'crushers', type: 'fine' },
  'fine-double-rotor-crushers': { group: 'crushers', type: 'fine' },
  'impact-fine-crushers': { group: 'crushers', type: 'fine' },
  'hammer-crushers': { group: 'crushers', type: 'single' },
  'mobile-crushing-plants': { group: 'crushers', type: 'mobile' },
  'tyre-crawler-mounted-crushing-plants': { group: 'crushers', type: 'mobile' }
}

// Catalogue downloads. Published after a check of each file (28 Nov 2026): no maker names, no Sudan, no
// "artisanal", no banned photo. The others wait for a corrected edition and are sent on request; BXC-11 is
// licensed-only and BXS-02 waits for the owner (fences and forklifts, SAB TECH contract).
const CAT_DIR = '/catalogues/gold-mining'
export const CATALOGUES: { code: string, edition: string, title: L, file?: string }[] = [
  { code: 'BXC-02', edition: '4', title: L('التنقيب والحفر واستخراج الخام', 'Exploration, Drilling & Ore Extraction') },
  { code: 'BXC-03', edition: '4', title: L('مستهلكات الحفر', 'Drilling Consumables') },
  { code: 'BXC-04', edition: '6', title: L('التكسير والطحن والغربلة', 'Crushing, Grinding & Screening') },
  { code: 'BXC-05', edition: '4', title: L('الغسيل وتركيز الذهب', 'Washing & Gold Concentration'), file: `${CAT_DIR}/Bestolex_BXC-05_Washing_Gold_Concentration_Ed4.pdf` },
  { code: 'BXC-06', edition: '7', title: L('معالجة الخام والمصانع', 'Ore Processing & Plants') },
  { code: 'BXC-07', edition: '5', title: L('المضخات ونقل اللب', 'Pumps & Slurry Handling') },
  { code: 'BXC-08', edition: '7', title: L('الصهر والتنقية', 'Smelting & Refining'), file: `${CAT_DIR}/Bestolex_BXC-08_Smelting_Refining_Ed7.pdf` },
  { code: 'BXC-09', edition: '6', title: L('المختبر والتحليل', 'Laboratory & Assay'), file: `${CAT_DIR}/Bestolex_BXC-09_Laboratory_Assay_Ed6.pdf` },
  { code: 'BXC-10', edition: '4', title: L('دعم الأسطول', 'Fleet Support') },
  { code: 'BXS-01', edition: '2', title: L('السلامة ومعدات الوقاية', 'Safety & PPE'), file: `${CAT_DIR}/Bestolex_BXS-01_Safety_PPE_Ed2.pdf` },
  { code: 'BXS-02', edition: '1', title: L('مستلزمات الموقع والمرافق', 'Site Supplies & Facilities') }
]

const goldCategory = () => catalog.find((c: any) => c.id === 'gold-mining')
const subProducts = (sub?: string): any[] =>
  sub ? ((goldCategory()?.subcategories || []).find((s: any) => s.id === sub)?.products || []) : []

const plain = (s?: string) => (s || '').replace(/[⁦-⁩⁠]/g, '')
const statOf = (p: any, i: number) => (p.stats?.ar?.[i] ? {
  value: { ar: p.stats.ar[i].value, en: p.stats.en?.[i]?.value || plain(p.stats.ar[i].value) },
  label: { ar: p.stats.ar[i].label, en: p.stats.en?.[i]?.label || '' }
} : null)

const typeOf = (stage: Stage, id: string) => {
  const t = FAMILY_META[id]?.type
  return t ? stage.types?.find(x => x.id === t) : undefined
}

export const familyCard = (stage: Stage, p: any) => ({
  id: p.id,
  name: p.name,
  image: p.cardImage || p.image || p.coverImage,
  type: FAMILY_META[p.id]?.type || null,
  group: FAMILY_META[p.id]?.group || stage.groups?.[0]?.id || null,
  badge: typeOf(stage, p.id)?.badge || null,
  stats: [0, 1, 2].map(i => statOf(p, i)).filter(Boolean)
})

const catalogueOf = (stage: Stage) => CATALOGUES.find(c => c.code === stage.code)

const stageSummary = (s: Stage) => {
  const fams = subProducts(s.sub)
  return {
    id: s.id, n: s.n, kind: s.kind, code: s.code, edition: s.edition, title: s.title, short: s.short,
    families: s.families, models: s.models, image: s.image, licensed: !!s.licensed,
    pages: fams.length,
    catalogue: s.licensed ? null : (catalogueOf(s)?.file || null)
  }
}

export const stageById = (id: string) => STAGES.find(s => s.id === id)
export const stageOfProduct = (productId: string) =>
  STAGES.find(s => subProducts(s.sub).some((p: any) => p.id === productId))

export const hubView = (published: { families: number, models: number }) => ({
  line: STAGES.filter(s => s.kind === 'line').map(stageSummary),
  support: STAGES.filter(s => s.kind === 'support').map(stageSummary),
  catalogues: CATALOGUES,
  published
})

export const stageView = (id: string) => {
  const s = stageById(id)
  if (!s || s.licensed) return null
  const cards = subProducts(s.sub).map(p => familyCard(s, p))
  const line = STAGES.filter(x => x.kind === 'line' && !x.licensed)
  const i = line.findIndex(x => x.id === s.id)
  const next = (i >= 0 ? line.slice(i + 1, i + 4) : line.slice(0, 3)).map(stageSummary)
  const { types, groups, how, cta, ...rest } = s
  const placed = cards.map(c => ({ ...c, group: groups ? c.group : 'all' }))
  return {
    ...rest,
    lineTotal: STAGES.filter(x => x.kind === 'line').length,
    catalogue: catalogueOf(s)?.file || null,
    groups: (groups || [{ id: 'all', title: s.title }]).map(g => ({ ...g, count: placed.filter(c => c.group === g.id).length })),
    types: (types || []).filter(t => cards.some(c => c.type === t.id)),
    cards: placed,
    cta,
    next
  }
}

// Family tables of the published gold-mining pages, for the search box and its counts.
let tables: Map<string, any> | null = null
export const miningTables = async () => {
  if (tables) return tables
  const out = new Map<string, any>()
  const store = useStorage('assets:server')
  for (const s of STAGES) {
    for (const p of subProducts(s.sub)) {
      let item: any = await store.getItem(`catalog/mining/${p.id}.json`)
      if (typeof item === 'string') { try { item = JSON.parse(item) } catch { item = null } }
      if (item?.types) out.set(p.id, item)
    }
  }
  tables = out
  return out
}

export const publishedCounts = async () => {
  const t = await miningTables()
  let models = 0
  for (const f of t.values()) for (const tp of f.types) models += (tp.models || []).length
  return { families: t.size, models }
}

// Search: family names, model names and BX codes. Arabic letters are folded (أ/إ/آ → ا, ة → ه, ى → ي) and
// spaces, ×/x and dashes ignored, so "PE 400x600" finds "PE400×600".
const fold = (s: string) => plain(s).toLowerCase()
  .replace(/[أإآ]/g, 'ا').replace(/ة/g, 'ه').replace(/ى/g, 'ي').replace(/[ً-ْ]/g, '')
  .replace(/[×x*]/g, 'x').replace(/[\s\-–_/·.,()]+/g, '')
const words = (q: string) => plain(q).trim().split(/\s+/).map(fold).filter(Boolean)

export const searchMining = async (q: string) => {
  const ws = words(q)
  if (!ws.length) return []
  const t = await miningTables()
  const hits: any[] = []
  const seenFam = new Set<string>()
  for (const s of STAGES) {
    for (const p of subProducts(s.sub)) {
      const famText = fold(`${p.name?.ar} ${p.name?.en} ${p.id}`)
      const famStage = { id: s.id, title: s.title }
      if (ws.every(w => famText.includes(w))) {
        hits.push({ kind: 'family', id: p.id, name: p.name, stage: famStage, image: p.cardImage || p.image })
        seenFam.add(p.id)
      }
      const f = t.get(p.id)
      for (const tp of f?.types || []) {
        for (const m of tp.models || []) {
          const own = fold(`${m.code} ${m.name?.en} ${m.name?.ar}`)
          const text = own + fold(`${tp.label?.en} ${tp.label?.ar}`)
          // A model shows when the query names it (its model or code), not for a family word alone.
          if (ws.some(w => own.includes(w)) && ws.every(w => text.includes(w) || famText.includes(w))) {
            hits.push({ kind: 'model', id: p.id, family: p.name, model: m.name, code: String(m.code).split(' / ')[0], stage: famStage })
          }
          if (hits.length >= 60) break
        }
      }
    }
  }
  // Families first, then models; at most 20.
  return [...hits.filter(h => h.kind === 'family'), ...hits.filter(h => h.kind === 'model')].slice(0, 20)
}

// Family page context: stage, chip, "how to choose", related families and the catalogue.
export const familyContext = (productId: string) => {
  const s = stageOfProduct(productId)
  if (!s) return null
  const all = subProducts(s.sub)
  const me = all.find((p: any) => p.id === productId)
  const meta = FAMILY_META[productId] || {}
  const sameType = all.filter((p: any) => p.id !== productId && FAMILY_META[p.id]?.type === meta.type)
  const others = all.filter((p: any) => p.id !== productId && !sameType.includes(p))
  return {
    stage: { id: s.id, n: s.n, kind: s.kind, title: s.title, code: s.code, edition: s.edition, catalogue: catalogueOf(s)?.file || null, cta: s.cta },
    group: s.groups?.find(g => g.id === (meta.group || s.groups?.[0]?.id)) || null,
    badge: typeOf(s, productId)?.badge || null,
    how: s.how || null,
    stats: me ? [0, 1, 2].map(i => statOf(me, i)).filter(Boolean) : [],
    related: [...sameType, ...others].slice(0, 4).map(p => familyCard(s, p))
  }
}
