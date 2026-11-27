// Sectors served by the sourcing-on-request service (/sourcing).
// The page covers equipment that is NOT in Bestolex's own product sections, for any activity.
// Shared by the sourcing page, the homepage band and the About page.
// Order = Qatar search demand per sector, highest first (Semrush, Qatar database, 27 Nov 2026,
// summed over each sector's AR/EN terms): construction ~2,160/month, spare parts ~1,890,
// pumps/compressors/water ~1,870, metalwork ~1,150, hospitality ~1,060, printing ~1,060,
// agriculture ~700, sewing ~690, woodworking ~300, production lines ~220,
// cleaning ~150, garages ~80, laboratories ~60.
// Medical equipment (~480) is left out until the commercial registration covers it (owner, 27 Nov 2026).

export interface SourcingSector {
  id: string
  icon: string
  ar: string
  en: string
  itemsAr: string[]
  itemsEn: string[]
  noteAr?: string
  noteEn?: string
}

export const SOURCING_SECTORS: SourcingSector[] = [
  {
    id: 'construction',
    icon: 'construction',
    ar: 'المقاولات والبناء',
    en: 'Contracting and construction',
    itemsAr: ['السقالات', 'خلاطات الخرسانة وهزازاتها', 'محطات خلط الخرسانة', 'مكائن البلوك', 'روافع المواد', 'معدات الطرق، والمعدات الثقيلة عند الطلب'],
    itemsEn: ['Scaffolding', 'Concrete mixers and vibrators', 'Concrete batching plants', 'Block making machines', 'Material hoists', 'Road equipment, and heavy equipment on request']
  },
  {
    id: 'spare-parts',
    icon: 'parts',
    ar: 'قطع الغيار والمستهلكات',
    en: 'Spare parts and consumables',
    itemsAr: ['قطع غيار أصلية أو بديلة متوافقة', 'قطع التآكل', 'الفلاتر والسيور والمحامل', 'المحركات ولوحات التحكم', 'لآلات قائمة عندك، ولو لم تشترها منا'],
    itemsEn: ['Original or compatible spare parts', 'Wear parts', 'Filters, belts and bearings', 'Motors and control panels', "For machines you already run, even if you didn't buy them from us"]
  },
  {
    id: 'pumps-compressors',
    icon: 'gauge',
    ar: 'المضخات والضواغط ومعالجة المياه',
    en: 'Pumps, compressors and water treatment',
    itemsAr: ['مضخات المياه والمضخات الغاطسة', 'ضواغط الهواء الصناعية (الكمبروسر)', 'محطات معالجة المياه وتحليتها', 'الصمامات والعدادات', 'المبادلات الحرارية'],
    itemsEn: ['Water pumps and submersible pumps', 'Industrial air compressors', 'Water treatment and desalination plants', 'Valves and meters', 'Heat exchangers']
  },
  {
    id: 'metalworking',
    icon: 'metal',
    ar: 'ورش الحدادة واللحام والتشغيل المعدني',
    en: 'Metalwork, welding and machining workshops',
    itemsAr: ['مكائن اللحام', 'المخارط ومكائن التفريز', 'مكائن CNC', 'المكابس الهيدروليكية ومكابس الثني', 'مقصات الصاج', 'القطع بالليزر والبلازما'],
    itemsEn: ['Welding machines', 'Lathes and milling machines', 'CNC machines', 'Hydraulic presses and press brakes', 'Sheet metal shears', 'Laser and plasma cutting']
  },
  {
    id: 'hospitality',
    icon: 'kitchen',
    ar: 'المطاعم والمقاهي والفنادق والمطابخ المركزية',
    en: 'Restaurants, cafés, hotels and central kitchens',
    itemsAr: ['معدات المطابخ التجارية', 'مكائن القهوة والعصائر والثلج', 'غرف التبريد والتجميد', 'معدات المخابز والحلويات', 'المغاسل الصناعية'],
    itemsEn: ['Commercial kitchen equipment', 'Coffee, juice and ice machines', 'Cold and freezer rooms', 'Bakery and pastry equipment', 'Industrial laundry equipment']
  },
  {
    id: 'printing',
    icon: 'print',
    ar: 'المطابع والإعلان',
    en: 'Printing and signage',
    itemsAr: ['مكائن الطباعة الأوفست والرقمية', 'طابعات اللوحات الكبيرة', 'مكائن القص والحفر بالليزر', 'مكائن CNC للافتات', 'الطابعات ثلاثية الأبعاد'],
    itemsEn: ['Offset and digital printing presses', 'Large-format printers', 'Laser cutting and engraving machines', 'CNC routers for signage', '3D printers']
  },
  {
    id: 'agriculture',
    icon: 'agri',
    ar: 'الزراعة والأمن الغذائي',
    en: 'Agriculture and food security',
    itemsAr: ['الجرارات والمعدات الزراعية', 'البيوت المحمية', 'أنظمة الري بالتنقيط', 'معدات فرز وتعبئة الخضار والتمور', 'معدات مزارع الدواجن والألبان'],
    itemsEn: ['Tractors and farm machinery', 'Greenhouses', 'Drip irrigation systems', 'Vegetable and date sorting and packing', 'Poultry and dairy farm equipment']
  },
  {
    id: 'tailoring',
    icon: 'sewing',
    ar: 'مشاغل الخياطة والتطريز والنسيج',
    en: 'Tailoring, embroidery and textiles',
    itemsAr: ['مكائن الخياطة الصناعية', 'مكائن التطريز', 'مكائن القص والكي', 'معدات مصانع الملابس والمفروشات'],
    itemsEn: ['Industrial sewing machines', 'Embroidery machines', 'Cutting and pressing machines', 'Garment and soft-furnishing factory equipment']
  },
  {
    id: 'woodworking',
    icon: 'wood',
    ar: 'ورش النجارة والأثاث',
    en: 'Carpentry and furniture workshops',
    itemsAr: ['مناشير الطاولة والمناشير الشريطية', 'مكائن CNC للخشب', 'مكائن الرندة والتسوية', 'مكائن لصق الحواف', 'مكابس القشرة', 'أنظمة شفط النشارة'],
    itemsEn: ['Table and band saws', 'CNC routers for wood', 'Planers and thicknessers', 'Edge banding machines', 'Veneer presses', 'Dust extraction systems']
  },
  {
    id: 'factories',
    icon: 'factory',
    ar: 'المصانع وخطوط الإنتاج',
    en: 'Factories and production lines',
    itemsAr: ['خطوط التعبئة والتغليف', 'خطوط تعبئة المياه والعصائر', 'معدات تصنيع الأغذية', 'مكائن حقن البلاستيك', 'معدات مصانع مواد البناء'],
    itemsEn: ['Filling and packaging lines', 'Water and juice bottling lines', 'Food processing equipment', 'Plastic injection machines', 'Building materials plant equipment']
  },
  {
    id: 'facilities',
    icon: 'cleaning',
    ar: 'النظافة وإدارة المرافق',
    en: 'Cleaning and facility management',
    itemsAr: ['مكائن الغسيل بالضغط', 'آلات تنظيف الأرضيات', 'المكانس الصناعية', 'معدات صيانة المباني'],
    itemsEn: ['Pressure washers', 'Floor scrubbers', 'Industrial vacuum cleaners', 'Building maintenance equipment']
  },
  {
    id: 'automotive',
    icon: 'car',
    ar: 'ورش السيارات ومراكز الصيانة',
    en: 'Garages and service centres',
    itemsAr: ['روافع السيارات', 'معدات غسيل السيارات', 'أجهزة الفحص والتشخيص', 'مكائن تغيير الإطارات وموازنتها'],
    itemsEn: ['Car lifts', 'Car wash equipment', 'Diagnostic equipment', 'Tyre changers and wheel balancers']
  },
  {
    id: 'labs',
    icon: 'lab',
    ar: 'المختبرات والجامعات والمدارس',
    en: 'Laboratories, universities and schools',
    itemsAr: ['أجهزة القياس والتحليل', 'أجهزة المعايرة', 'معدات تحضير العينات', 'تجهيز المختبرات التعليمية', 'معدات التدريب المهني'],
    itemsEn: ['Measuring and analysis instruments', 'Calibration equipment', 'Sample preparation equipment', 'Teaching laboratory fit-out', 'Vocational training equipment']
  }
]
