"""BXS-02 Ed1 (Site supplies & facilities) model tables, catalogue pages 3–4. Every code is in the supplier list
under BXS-02."""
from lib import table, family

CAT = 'BXS-02 Ed1'
F = {}
U_PRODUCT = {'ar': ['منتج واحد', 'منتجان', 'منتجات'], 'en': ['product', 'products']}
U_TYPE = {'ar': ['نوع واحد', 'نوعان', 'أنواع'], 'en': ['type', 'types']}
SERIES = [('models', 'Sizes / models', 'المقاسات والموديلات'), ('data', 'Key data', 'أهم البيانات')]
MTO = ('Made to order', 'حسب الطلب')

# p3 container houses & prefab buildings ---------------------------------------------------------------------
F['container-houses-prefab-buildings'] = family('container-houses-prefab-buildings', CAT, [
    table('houses', ('Container houses & prefab buildings', 'البيوت الجاهزة من الحاويات والمباني مسبقة الصنع'), ('20–40 ft', '20–40 قدماً'), SERIES,
          [('BX-0337-01-001', 'Flat-pack container house, 20 ft', 'بيت حاوية مفكك 20 قدماً', ('Layouts FC-01 to FC-16', 'مخططات FC-01 إلى FC-16'),
            ('Steel frame, sandwich-panel walls; layouts for 1-, 2- and multi-room units, men\'s and women\'s toilets, kitchen and dining, hostel, clinic, classroom and two-storey blocks',
             'هيكل فولاذي وجدران ألواح ساندويتش؛ مخططات لوحدات بغرفة وغرفتين وأكثر، ودورات مياه للرجال والنساء، ومطبخ وطعام، وسكن، وعيادة، وفصل، وكتل بطابقين')),
           ('BX-0337-01-002', 'Detachable container house', 'بيت حاوية قابل للفك', ('20 ft units; multi-storey', 'وحدات 20 قدماً؛ متعددة الطوابق'), ('Worker camps, dormitories, offices and hostels', 'مخيمات العمال والمهاجع والمكاتب والسكن')),
           ('BX-0337-01-003', 'Expandable container house', 'بيت حاوية قابل للتمديد', ('20 ft, 30 ft, 40 ft', '20 و30 و40 قدماً'), ('Folds out to a larger living space', 'ينفتح إلى مساحة معيشة أكبر')),
           ('BX-0337-01-004', 'Folding container house, first generation', 'بيت حاوية قابل للطي – الجيل الأول', ('Folding unit', 'وحدة قابلة للطي'), ('Installed in 4 steps in about 10 minutes', 'يُركّب في 4 خطوات خلال نحو 10 دقائق')),
           ('BX-0337-01-005', 'Folding container house, second generation', 'بيت حاوية قابل للطي – الجيل الثاني', 'L5,900 × W2,500 × H2,470 mm',
            ('10 sets per 40HQ container; saves about 80% of installation time', '10 وحدات في حاوية 40HQ؛ يوفر نحو 80% من وقت التركيب')),
           ('BX-0337-01-007', 'Prefabricated K-type house', 'مبنى جاهز طراز K', ('K-type; 1–2 storeys', 'طراز K؛ طابق أو طابقان'), ('Sandwich-panel camp buildings', 'مباني مخيمات من ألواح الساندويتش')),
           ('BX-0337-01-008', 'Prefabricated T-type house', 'مبنى جاهز طراز T', ('T-type', 'طراز T'), ('Camp and site buildings', 'مباني المخيمات والمواقع')),
           ('BX-0337-01-012', 'Sentry boxes & kiosks', 'أكشاك الحراسة والأكشاك', ('Post series', 'سلسلة Post'), ('Guard booths for site gates', 'أكشاك حراسة لبوابات المواقع'))],
          intro=('Units ship flat or folded to cut freight and installation time.', 'تُشحن الوحدات مفككة أو مطوية لتقليل الشحن ووقت التركيب.'),
          unit=U_TYPE),
], type_label=('Product', 'المنتج'), unit=U_TYPE)

# p4 toilets, fencing, mesh & grating ------------------------------------------------------------------------
F['portable-toilets-fencing-mesh-grating'] = family('portable-toilets-fencing-mesh-grating', CAT, [
    table('sanitation', ('Portable sanitation', 'المرافق الصحية المتنقلة'), ('HDPE', 'HDPE'), SERIES,
          [('BX-0337-01-006', 'Portable toilets & showers, HDPE', 'دورات مياه ودشات متنقلة HDPE', 'PT100, PT200, PS-100, PT400',
            ('For construction sites, mine sites and labour camps; a luxury portable toilet is also available', 'لمواقع البناء والمناجم ومخيمات العمال؛ ويتوفر أيضاً حمام متنقل فاخر'))],
          unit=U_PRODUCT),
    table('fencing', ('Fencing & perimeter security', 'الأسوار وتأمين المحيط'), ('4 fence types', '4 أنواع أسوار'), SERIES,
          [('BX-0313-01-012', 'Anti-climb high-security fence (358)', 'سور أمني عالي الحماية ضد التسلق (358)', MTO, ('High-security perimeter fence', 'سور محيطي عالي الأمان')),
           ('BX-0313-01-011', 'Chain-link fence', 'سور شبك مجدول', MTO, ('Perimeter fencing', 'تسوير المحيط')),
           ('BX-0313-01-008', 'Barbed wire & razor wire', 'الأسلاك الشائكة والشفرات', MTO, ('Perimeter security wire', 'أسلاك لتأمين المحيط')),
           ('BX-0313-01-016', 'Temporary fence & crowd-control barriers', 'أسوار مؤقتة وحواجز تنظيم الحشود', MTO, ('Movable fencing for sites and camps', 'أسوار متنقلة للمواقع والمخيمات'))],
          unit=U_PRODUCT),
    table('mesh', ('Expanded mesh & steel grating', 'الشبك الممدد والشبكات الفولاذية'), ('', ''), SERIES,
          [('BX-0313-01-001', 'Expanded metal mesh', 'شبك معدني ممدد', ('Steel; aluminium for facades; made to order', 'فولاذ؛ وألمنيوم للواجهات؛ حسب الطلب'), ('Stair treads, walkways, safety barriers, filters and mining stations', 'درجات السلالم والممرات وحواجز الأمان والمرشحات ومحطات التعدين')),
           ('BX-0313-01-002', 'Steel grating', 'شبكات فولاذية (جريتنغ)', ('Compound grating, trench drain grates, stair treads', 'شبكات مركّبة، وأغطية قنوات التصريف، ودرجات السلالم'), ('Platforms, walkways and stairs', 'المنصات والممرات والسلالم'))],
          unit=U_PRODUCT),
])
