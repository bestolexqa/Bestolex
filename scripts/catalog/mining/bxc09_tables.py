"""BXC-09 Ed6 (Laboratory & assay) model tables, catalogue pages 3–18. Typed from the page text and checked
against the page images where cells wrap (pages 5, 9, 10, 11, 13, 14, 18). Rows under a header code range
(BX-0047-01-007 … 009, BX-0048-04-001 … 006, BX-0048-04-012 … 017) take their own codes from the supplier list;
every code is in the supplier list under BXC-09."""
from lib import table, family
from bxc02_tables import U_LINES

CAT = 'BXC-09 Ed6'
F = {}
U_PRODUCT = {'ar': ['منتج واحد', 'منتجان', 'منتجات'], 'en': ['product', 'products']}
U_INSTR = {'ar': ['جهاز واحد', 'جهازان', 'أجهزة'], 'en': ['instrument', 'instruments']}
U_SIZE = {'ar': ['مقاس واحد', 'مقاسان', 'مقاسات'], 'en': ['size', 'sizes']}
SERIES = [('models', 'Sizes / models', 'المقاسات والموديلات'), ('data', 'Key data', 'أهم البيانات')]
DATA = [('data', 'Key data', 'أهم البيانات')]
C = lambda k, en, ar: (k, en, ar)
PWR = C('power', 'Power (kW)', 'القدرة (كيلوواط)')


def series(tid, label, key, rows, intro=None, unit=U_LINES):
    """rows: (code, name_en, name_ar, models, data); models/data: str or (en, ar)."""
    return table(tid, label, key, SERIES, [(c, ne, na, m, d) for c, ne, na, m, d in rows], intro=intro, unit=unit)


# p3 sample crushing & pulverizing ------------------------------------------------------------------------
F['sample-crushing-pulverizing'] = family('sample-crushing-pulverizing', CAT, [
    table('jaw', ('Sealed laboratory jaw crushers (negative-pressure, dust-free)', 'كسارات فكية مختبرية محكمة (ضغط سالب، بلا غبار)'), ('230–1800 kg/h', '230–1800 كجم/ساعة'),
          [C('inlet', 'Inlet (mm)', 'المدخل (مم)'), C('max-feed', 'Max. feed (mm)', 'أقصى تغذية (مم)'), C('output', 'Output (mm)', 'الناتج (مم)'),
           C('cap-kg', 'Capacity (kg/h)', 'الطاقة (كجم/ساعة)'), C('speed', 'Speed (r/min)', 'السرعة (دورة/دقيقة)'), PWR],
          [(None, '100×60', None, '100×60', '≤ 50', '6–10', '230–400', '650', '1.5'),
           (None, '100×100', None, '100×100', '≤ 100', '5–25', '400–1800', '390', '3'),
           (None, '100×125', None, '100×125', '≤ 100', '3–25', '400–1800', '390', '3'),
           (None, '100×150', None, '100×150', '≤ 90', '5–25', '400–1800', '390', '3')],
          code='BX-0047-01-001', key_rows=['cap-kg', 'output', 'power']),
    table('mills', ('Sealed pulverizer and jar mill', 'ساحقة محكمة وطاحونة جرار'), ('', ''), DATA,
          [('BX-0047-01-003', 'GJ100-1A sealed pulverizer', 'ساحقة محكمة GJ100-1A',
            ('High-manganese steel bowl; 1 × 100 g per run; feed < 13 mm; < 3 min; output 120–200 mesh; 1.1 kW, 380 V; 510×580×820 mm; noise < 60 dB',
             'وعاء من فولاذ عالي المنغنيز؛ عينة واحدة 100 جم في الدورة؛ تغذية < 13 مم؛ < 3 دقائق؛ ناتج 120–200 ميش؛ 1.1 كيلوواط، 380 فولت؛ 510×580×820 مم؛ ضجيج < 60 ديسيبل')),
           ('BX-0047-01-002', 'GQM-2-5 jar (roller) ball mill', 'طاحونة جرار كروية GQM-2-5',
            ('2 jars of 0.5–5 L; feed ≤ 10 mm; output 200–2000 mesh; 0.75 kW, 220 V, VFD; rollers 50–410 r/min; timer 0–6500 min; up to 35 kg per jar; 950×660×710 mm, 72 kg',
             'جرّتان سعة 0.5–5 لتر؛ تغذية ≤ 10 مم؛ ناتج 200–2000 ميش؛ 0.75 كيلوواط، 220 فولت، محوّل تردد؛ البكرات 50–410 دورة/دقيقة؛ مؤقت 0–6500 دقيقة؛ حتى 35 كجم للجرة؛ 950×660×710 مم، 72 كجم'))],
          intro=('Jars in stainless steel, nylon, polyurethane, PTFE, corundum or zirconia.', 'الجرار من الستانلس أو النايلون أو البولي يوريثان أو PTFE أو الكوراندوم أو الزركونيا.'),
          unit=U_INSTR),
])

# p4 sample division, sieving, drying & digestion -----------------------------------------------------------
F['sample-division-sieving-drying-digestion'] = family('sample-division-sieving-drying-digestion', CAT, [
    table('division', ('Sieve shaker, riffle splitter and test sieves', 'هزاز المناخل ومقسّم العينات ومناخل الاختبار'), ('', ''), DATA,
          [('BX-0047-01-013', 'NB-RT88 sieve shaker (Ro-tap type)', 'هزاز مناخل NB-RT88 (نوع Ro-tap)',
            ('1–8 sieve layers; 310 ± 6 rotations/min; 170 ± 3 taps/min; tap height 38 ± 6 mm; stroke 16 mm; 0.55 kW, 220 V 50 Hz; digital timer and counters',
             '1–8 طبقات مناخل؛ 310 ± 6 دورة/دقيقة؛ 170 ± 3 طرقة/دقيقة؛ ارتفاع الطرق 38 ± 6 مم؛ شوط 16 مم؛ 0.55 كيلوواط، 220 فولت 50 هرتز؛ مؤقت وعدادات رقمية')),
           ('BX-0047-01-011', 'NBG-II riffle splitter', 'مقسّم عينات NBG-II', ('12 chutes of 25.4 mm; load 300–2000 g', '12 مجرى بعرض 25.4 مم؛ حمولة 300–2000 جم')),
           ('BX-0047-01-014', 'Test sieve set (10 sieves)', 'طقم مناخل اختبار (10 مناخل)',
            ('Apertures 16000 · 8000 · 4000 · 2000 · 1000 · 500 · 250 · 150 · 75 · 53 µm', 'الفتحات 16000 · 8000 · 4000 · 2000 · 1000 · 500 · 250 · 150 · 75 · 53 ميكرون'))],
          unit=U_PRODUCT),
    table('hot-plates', ('DRB constant-temperature hot plates (cast aluminium alloy)', 'سخانات مسطحة بحرارة ثابتة DRB (سبيكة ألومنيوم مصبوبة)'), ('RT–400 °C', 'حرارة الغرفة–400 °م'),
          [C('plate', 'Plate (mm)', 'السطح (مم)'), C('temp', 'Temperature', 'الحرارة'), C('acc', 'Accuracy', 'الدقة'), C('watts', 'Power (W)', 'القدرة (واط)'),
           C('supply', 'Supply', 'التغذية'), C('dims', 'Dimensions (mm)', 'الأبعاد (مم)')],
          [(None, 'DRB-300B', None, '300×200', ('RT–400 °C', 'حرارة الغرفة–400 °م'), '± 1 °C', '2000', 'AC 220 V 50 Hz', '480×260×160'),
           (None, 'DRB-400B', None, '400×300', ('RT–400 °C', 'حرارة الغرفة–400 °م'), '± 1 °C', '3000', 'AC 220 V 50 Hz', '680×360×160'),
           (None, 'DRB-600B', None, '600×400', ('RT–400 °C', 'حرارة الغرفة–400 °م'), '± 1 °C', '4000', 'AC 220 V 50 Hz', '880×460×160')],
          intro=('LCD controller with fuzzy PID, timed alarm and shut-off. For sample heating, drying, digestion and acid treatment.',
                 'وحدة تحكم LCD بنظام PID، مع إنذار وإيقاف مؤقت. لتسخين العينات وتجفيفها وهضمها ومعالجتها بالأحماض.'),
          code='BX-0047-01-004', key_rows=['plate', 'temp', 'watts']),
    table('vacuum-ovens', ('DZF vacuum drying ovens', 'أفران تجفيف بالتفريغ DZF'), ('', ''),
          [C('watts', 'Power (W)', 'القدرة (واط)'), C('chamber', 'Chamber (mm)', 'الحجرة (مم)'), C('overall', 'Overall (mm)', 'الأبعاد الكلية (مم)'), C('shelves', 'Shelves', 'الرفوف')],
          [(None, 'DZF-6020 / 6021', None, '450', '300×300×275', '605×490×450', '1'),
           (None, 'DZF-6050 / 6051 / 6053', None, '1450', '415×370×345', '730×560×550', ('2 (6053: 3)', '2 (‏6053: ‏3)')),
           (None, 'DZF-6090', None, '1400', '450×450×450', '610×660×1400', '2'),
           (None, 'DZF-6210', None, '2200', '560×600×640', '720×805×1680', '3'),
           (None, 'DZF-6500', None, '3600', '630×810×845', '790×1030×1855', '4')],
          intro=('Vacuum < 133 Pa; +10 to 200 / 250 °C by model; resolution 0.1 °C; ±1 °C; timer 1–9999 min. D and LC versions with programmable or vacuum-display controllers.',
                 'تفريغ < 133 باسكال؛ من +10 إلى 200 / 250 °م حسب الموديل؛ دقة العرض 0.1 °م؛ ±1 °م؛ مؤقت 1–9999 دقيقة. نسخ D وLC بوحدات تحكم قابلة للبرمجة أو بعرض التفريغ.'),
          code='BX-0047-01-010', key_rows=['chamber', 'watts', 'shelves']),
])

# p5 sample preparation – additional range -------------------------------------------------------------------
F['sample-preparation-additional-range'] = family('sample-preparation-additional-range', CAT, [
    series('series', ('Sample preparation equipment – additional range', 'معدات تحضير العينات – مجموعة إضافية'), ('', ''), [
        ('BX-0421-01-002', 'Laboratory jaw crushers (heavy-duty, mega-reduction, double-acting, ultra-fine)', 'كسارات فكية مختبرية (ثقيلة، وتخفيض كبير، ومزدوجة الحركة، وناعمة جداً)',
         'YX-JC250×400, JC150×250, HJ125×150, HJ100×60, YX-JCT100, YX-JCT50, YX-HJ60×100P / 125×150P / 150×250P, YX-HP200, YX-HJTX30/100',
         ('Feed to 210 mm; product 0.5–60 mm adjustable; 2.2–15 kW, 380 V 50 Hz; JCT100 gives 85% below 2 mm in one pass',
          'تغذية حتى 210 مم؛ ناتج 0.5–60 مم قابل للضبط؛ 2.2–15 كيلوواط، 380 فولت 50 هرتز؛ JCT100 يعطي 85% أقل من 2 مم في مرور واحد')),
        ('BX-0421-01-003', 'Jaw crusher over rotary sample divider', 'كسارة فكية فوق مقسّم عينات دوّار', ('YX-HJD125×150, YX-HJD125×150R (with reject discharge)', 'YX-HJD125×150 وYX-HJD125×150R (بتفريغ المرفوض)'),
         ('Crushes and splits in one step; product 3–20 mm; 8 × 20 L buckets; 4 kW', 'يكسّر ويقسّم في خطوة واحدة؛ ناتج 3–20 مم؛ 8 دلاء × 20 لتر؛ 4 كيلوواط')),
        ('BX-0421-01-004', 'Laboratory hammer and roll crushers', 'كسارات مطرقية وأسطوانية مختبرية', 'YX-HC250×360, YX-HC180×150; YX-RC250×75 / 125 / 150',
         ('Hammer: feed ≤ 150 mm, product below 13 / 6 / 3 mm; roll: feed ≤ 13 mm, product 1–3 mm', 'المطرقية: تغذية ≤ 150 مم، ناتج أقل من 13 / 6 / 3 مم؛ الأسطوانية: تغذية ≤ 13 مم، ناتج 1–3 مم')),
        ('BX-0421-01-007', 'Vibration pulverisers, bowls and continuous ring mill', 'ساحقات اهتزازية وأوعية وطاحونة حلقية مستمرة', ('YX-M2000, YX-M5000; bowls B300–B5000; YX-ZM100', 'YX-M2000 وYX-M5000؛ أوعية B300–B5000؛ YX-ZM100'),
         ('Product ≤ 75 µm; M2000 up to 1.8 kg and M5000 up to 3.5 kg per batch; steel, chrome and tungsten-carbide bowls',
          'ناتج ≤ 75 ميكرون؛ M2000 حتى 1.8 كجم وM5000 حتى 3.5 كجم في الدفعة؛ أوعية من الفولاذ والكروم وكربيد التنغستن')),
        ('BX-0421-01-008', 'Multi-pot grinders', 'مطاحن متعددة الأوعية', 'YX-M100 to M100-7, YX-M200 to M200-4, YX-M400, M800, M1000',
         ('1–7 pots of 50–1000 g; product 80–200 mesh; 1.1–2.2 kW', '1–7 أوعية سعة 50–1000 جم؛ ناتج 80–200 ميش؛ 1.1–2.2 كيلوواط')),
        ('BX-0421-01-009', 'Disc mills', 'طواحين قرصية', 'YX-DM175, YX-DM200', ('Feed ≤ 6–8 mm; product 80–200 mesh; 10–35 kg/h', 'تغذية ≤ 6–8 مم؛ ناتج 80–200 ميش؛ 10–35 كجم/ساعة')),
        ('BX-0421-01-005', 'Rotary sample dividers', 'مقسّمات عينات دوّارة', ('YX-RSD02, 05, 05P, 20, 30, 40, 60, 90; YX-RSD30R / 60R with reject', 'YX-RSD02 و05 و05P و20 و30 و40 و60 و90؛ YX-RSD30R / 60R بالمرفوض'),
         ('Buckets 2–90 L; 4–10 splits; 220 V', 'دلاء 2–90 لتر؛ 4–10 أقسام؛ 220 فولت')),
        ('BX-0421-01-006', 'Drying ovens, trolley ovens and multi-cavity oven', 'أفران تجفيف وأفران بعربات وفرن متعدد الحجرات',
         ('YH-9023A to 9960A (25–960 L); YD-2000T / 4000T / 10000T; YD-MC100', 'YH-9023A إلى 9960A (25–960 لتر)؛ YD-2000T / 4000T / 10000T؛ YD-MC100'),
         ('Up to 250 °C; trolley ovens 120 °C, 2.1–10.3 m³', 'حتى 250 °م؛ أفران العربات 120 °م، 2.1–10.3 م³')),
        ('BX-0421-01-014', 'Sieve shakers', 'هزازات مناخل', 'YX-ZS200, YX-CT200', ('200 / 300 mm sieves; up to 7 sieves; 0.37 kW', 'مناخل 200 / 300 مم؛ حتى 7 مناخل؛ 0.37 كيلوواط')),
        ('BX-0421-01-013', 'Automatic XRF pellet press', 'مكبس أقراص XRF آلي', 'YX-YP40T, YX-YP60T',
         ('40 / 60 t; PLC with touch screen; steel-ring and boric-acid dies', '40 / 60 طن؛ تحكم PLC بشاشة لمس؛ قوالب بحلقة فولاذية أو حمض البوريك')),
    ]),
], type_label=('Series', 'السلسلة'))

# p6 fire-assay furnaces & cupels ----------------------------------------------------------------------------
F['fire-assay-furnaces-cupels'] = family('fire-assay-furnaces-cupels', CAT, [
    table('muffle', ('Muffle furnaces for cupellation and ashing', 'أفران كتمية للتكويب وتعيين الرماد'), ('1000–1200 °C', '1000–1200 °م'),
          [C('temp', 'Max. temp. (°C)', 'أقصى حرارة (°م)'), C('chamber', 'Chamber (cm)', 'الحجرة (سم)'), PWR, C('outer', 'Outer size (cm)', 'المقاس الخارجي (سم)')],
          [('BX-0047-01-006', '2.5-10', None, '1000', '8×12×20', '2.5', '52×39×52'), ('BX-0047-01-006', '2.5-12', None, '1200', '8×12×20', '2.5', '52×39×52'),
           ('BX-0047-01-006', '4-10', None, '1000', '12×20×30', '4', '63×48×57'), ('BX-0047-01-006', '5-12', None, '1200', '12×20×30', '5', '63×48×57'),
           ('BX-0047-01-006', '8-10', None, '1000', '16×25×40', '8', '73×56×65'), ('BX-0047-01-006', '10-12', None, '1200', '16×25×40', '10', '73×56×65'),
           ('BX-0047-01-006', '12-12', None, '1200', '20×30×50', '12', '83×63×69'),
           ('BX-0047-01-005', 'NB.M8/12 (8 L)', None, '1200', ('8 L', '8 لتر'), None, None)],
          intro=('Fluctuation ±2 °C; display 1 °C; heating ≤ 15 °C/min; 220 V or 380 V by model. PID control, K-type thermocouple, high-alumina firebrick chamber and a 24 mm exhaust port.',
                 'تذبذب ±2 °م؛ عرض 1 °م؛ تسخين ≤ 15 °م/دقيقة؛ 220 أو 380 فولت حسب الموديل. تحكم PID، ومزدوج حراري نوع K، وحجرة من الطوب الحراري عالي الألومينا، وفتحة عادم 24 مم.'),
          key_rows=['temp', 'chamber', 'power']),
    table('cupels', ('Magnesia cupels', 'أكواب التكويب المغنيسية'), ('16 sizes', '16 مقاساً'),
          [C('top-od', 'Top OD (mm)', 'القطر الخارجي العلوي (مم)'), C('base', 'Base Ø (mm)', 'قطر القاعدة (مم)'), C('top-id', 'Top ID (mm)', 'القطر الداخلي العلوي (مم)'),
           C('height', 'Height (mm)', 'الارتفاع (مم)'), C('rim', 'Rim (mm)', 'الحافة (مم)'), C('dish', 'Dish depth (mm)', 'عمق التجويف (مم)'),
           C('wt', 'Net wt. (g)', 'الوزن الصافي (جم)'), C('pcs', 'Pcs/carton', 'قطعة/كرتون'), C('carton', 'Carton (cm)', 'الكرتون (سم)')],
          [(None, '2x', None, '24', '19', '18', '17', '4.5', '8', '13', '1040', '34×22×22'), (None, '3', None, '26', '20', '23', '20', '8', '5.5', '17', '864', '34×22×22'),
           (None, '4', None, '29', '23', '24', '22', '8', '6', '20', '486', '30×30×15'), (None, '5', None, '35', '26', '27', '26', '6.5', '8', '35', '378', '34×22×22'),
           (None, '6A', None, '40', '30', '30', '26', '6', '12', '62', '200', '34×22×22'), (None, '7A', None, '40', '30', '30', '32', '10', '12', '72', '200', '34×22×22'),
           (None, '7AS', None, '40', '30', '32', '32', '10', '15', '62', '200', '34×22×22'), (None, '8A', None, '45', '37', '38', '35', '13', '13', '103', '200', '38×24×21'),
           (None, '8AM', None, '45', '37', '33', '35', '15', '12', '110', '200', '38×24×21'), (None, '9', None, '51', '43', '40', '30', '5', '11', '120', '120', '34×22×22'),
           (None, '9A', None, '51', '39', '40', '34', '14', '15', '123', '120', '34×22×22'), (None, '11', None, '56', '46', '46', '37', '11', '14', '166', '100', '34×22×22'),
           (None, '12', None, '80.2', '62.5', '57.5', '47', '11', '16.5', '450', '12', '34×22×22'), (None, '14', None, '110', '88', '80', '70', '14', '24', '1180', '44', '34×22×22'),
           (None, 'Z27', None, '27', '27', '23', '23', None, '10', '29', '500', '30×30×15'), (None, 'Y40', None, '40', '40', '32', '30', None, '15', '73', '200', '34×22×22')],
          intro=('Magnesia cupels absorb lead oxide during cupellation and leave the gold-silver prill.', 'تمتص أكواب المغنيسيا أكسيد الرصاص أثناء التكويب وتترك حبة الذهب والفضة.'),
          code='BX-0046-02-003', key_rows=['top-od', 'height', 'wt'], unit=U_SIZE),
])

# p7 fire assay furnaces, fluxing & laboratory utilities -----------------------------------------------------
F['fire-assay-fluxing-lab-utilities'] = family('fire-assay-fluxing-lab-utilities', CAT, [
    series('series', ('Fire assay furnaces, fluxing, consumables and lab utilities', 'أفران التحليل بالنار والمصهرات والمستهلكات ومرافق المختبر'), ('', ''), [
        ('BX-0421-01-017', 'Fire assay fusion furnaces', 'أفران الصهر للتحليل بالنار', 'YX-FF12, YX-FF25, YX-FF42P',
         ('1200 °C; 12–42 crucibles; silicon-carbide elements; pneumatic door; 18–40 kW three-phase', '1200 °م؛ 12–42 بوتقة؛ عناصر تسخين من كربيد السيليكون؛ باب هوائي؛ 18–40 كيلوواط ثلاثي الأطوار')),
        ('BX-0421-01-018', 'Cupellation furnaces', 'أفران التكويب', 'YX-CF50, YX-CF100', ('1200 °C; 50 / 100 cupels; 18 / 35 kW', '1200 °م؛ 50 / 100 كوب تكويب؛ 18 / 35 كيلوواط')),
        ('BX-0421-01-019', 'Roasting (pre-firing) furnace and muffle furnaces', 'فرن التحميص (الحرق المسبق) والأفران الكتمية',
         ('Roasting furnace 10.5 kW; MFLC-2/12 to 36/12 (D and P)', 'فرن تحميص 10.5 كيلوواط؛ MFLC-2/12 إلى 36/12 (D وP)'),
         ('Up to 1000–1200 °C; chamber 2–36 L', 'حتى 1000–1200 °م؛ حجرة 2–36 لتر')),
        ('BX-0421-01-020', 'Flux mixers, automatic flux dosing and crucible mixers', 'خلاطات المصهر والجرعات الآلية وخلاطات البوتقات',
         ('YH-5L to YH-1200L (3D); YX-CM25, YX-CM50', 'YH-5L إلى YH-1200L ‏(3D)؛ YX-CM25 وYX-CM50'),
         ('Mix flux and sample; 25 / 50 crucibles per batch', 'خلط المصهر والعينة؛ 25 / 50 بوتقة في الدفعة')),
        ('BX-0421-01-021', 'Fire assay clay crucibles', 'بوتقات طينية للتحليل بالنار', ('YAC0245 to YAC0750A (30 g to 75 g+ charges)', 'YAC0245 إلى YAC0750A (شحنات من 30 جم إلى 75 جم فأكثر)'),
         ('Volume 245–760 mL', 'السعة 245–760 مل')),
        ('BX-0421-01-011', 'Bottle roller / rod mill', 'دوّار القوارير / طاحونة القضبان',
         ('YXRM-3A-300 to YXRM-5D-1500 (1–4 tiers, 2–20 rollers, 300–1800 mm)', 'YXRM-3A-300 إلى YXRM-5D-1500 ‏(1–4 طبقات، 2–20 بكرة، 300–1800 مم)'),
         ('Variable speed; for bottle-roll leach tests, mixing and rod grinding', 'سرعة متغيرة؛ لاختبارات الإذابة بالقوارير والخلط والطحن بالقضبان')),
        ('BX-0421-01-027', 'Hot plates (ceramic, graphite, stainless)', 'سخانات مسطحة (سيراميك، جرافيت، ستانلس)',
         'YHP-300EX / 400EX / 500EX; YHP-DB-XS to 3S, XSGW to 3SGW; YHP-DB-2A to 6A',
         ('300–500 °C; 1–5 kW; for sample digestion', '300–500 °م؛ 1–5 كيلوواط؛ لهضم العينات')),
        ('BX-0421-01-028', 'Magnetic stirrers', 'خلاطات مغناطيسية', ('YXMS-901D, 1 to 10 positions', 'YXMS-901D، من 1 إلى 10 مواضع'),
         ('3 L per position; 0–2500 r/min', '3 لتر لكل موضع؛ 0–2500 دورة/دقيقة')),
        ('BX-0421-01-026', 'Mobile containerised laboratories', 'مختبرات متنقلة في حاويات', ('20 ft and 40 ft HQ containers', 'حاويات 20 قدماً و40 قدماً HQ'),
         ('Insulated units for sample preparation, fire assay, wet assay or two-level labs; for remote sites',
          'وحدات معزولة لتحضير العينات أو التحليل بالنار أو التحليل الرطب أو مختبرات بطابقين؛ للمواقع البعيدة')),
    ]),
], type_label=('Series', 'السلسلة'))

# p8 laboratory balances & micropipettes ---------------------------------------------------------------------
F['laboratory-balances-micropipettes'] = family('laboratory-balances-micropipettes', CAT, [
    table('balances', ('Balances', 'الموازين'), ('200 g–3 kg', '200 جم–3 كجم'),
          [C('cap', 'Capacity', 'السعة'), C('read', 'Readability', 'دقة القراءة'), C('pan', 'Pan', 'الكفة'), C('display', 'Display / interface', 'الشاشة / الواجهة'), C('details', 'Details', 'التفاصيل')],
          [('BX-0047-01-007', 'NA2204', None, ('220 g', '220 جم'), ('0.1 mg', '0.1 ملغ'), ('Ø80 mm stainless', 'قطر 80 مم ستانلس'), 'LCD, RS232',
            ('Linearity ±0.2 mg; repeatability 0.2 mg; stable < 0.5 s; AC/DC rechargeable; 350×210×360 mm',
             'الخطية ±0.2 ملغ؛ التكرارية 0.2 ملغ؛ الاستقرار < 0.5 ثانية؛ تيار متردد/مستمر قابل للشحن؛ 350×210×360 مم')),
           ('BX-0047-01-008', 'NB30002K', None, ('3000 g', '3000 جم'), ('0.01 g', '0.01 جم'), ('Ø130 mm', 'قطر 130 مم'), ('LED, backlit', 'LED بإضاءة خلفية'),
            ('Counting; multi-point or single-point calibration; 25×18×14 cm; 2 kg', 'العدّ؛ معايرة متعددة النقاط أو بنقطة واحدة؛ 25×18×14 سم؛ 2 كجم')),
           ('BX-0047-01-009', 'Pocket balance', 'ميزان جيب', ('200 g', '200 جم'), ('0.01 g', '0.01 جم'), None, 'LCD',
            ('Battery-operated, for gold buying in the field', 'يعمل بالبطارية، لشراء الذهب في الموقع'))],
          key_rows=['cap', 'read', 'display']),
    table('pipettes', ('Adjustable single-channel micropipettes', 'ماصات دقيقة أحادية القناة قابلة للضبط'), ('2–1000 µL', '2–1000 ميكرولتر'),
          [C('inc', 'Increment', 'الخطوة'), C('test', 'Test volume (µL)', 'حجم الاختبار (ميكرولتر)'), C('acc', 'Accuracy error', 'خطأ الدقة'), C('prec', 'Precision error', 'خطأ الضبط')],
          [(None, '2–20 µL (metal nozzle)', '2–20 ميكرولتر (فوهة معدنية)', '0.5 µL', '20', '0.90% · 0.18 µL', '0.40% · 0.08 µL'),
           (None, '2–20 µL (metal nozzle)', '2–20 ميكرولتر (فوهة معدنية)', '0.5 µL', '10', '1.20% · 0.12 µL', '1.00% · 0.10 µL'),
           (None, '2–20 µL (metal nozzle)', '2–20 ميكرولتر (فوهة معدنية)', '0.5 µL', '2', '3.00% · 0.06 µL', '2.00% · 0.04 µL'),
           (None, '100–1000 µL', '100–1000 ميكرولتر', '5 µL', '1000', '0.60% · 6 µL', '0.20% · 2 µL'),
           (None, '100–1000 µL', '100–1000 ميكرولتر', '5 µL', '500', '0.70% · 3.5 µL', '0.25% · 1.25 µL'),
           (None, '100–1000 µL', '100–1000 ميكرولتر', '5 µL', '100', '2.00% · 2 µL', '0.70% · 0.7 µL')],
          intro=('Fully autoclavable; each pipette with an individual ISO 8655 calibration certificate. Other ranges from 0.1 µL to 10 mL.',
                 'قابلة للتعقيم بالكامل؛ لكل ماصة شهادة معايرة فردية وفق ISO 8655. مدايات أخرى من 0.1 ميكرولتر إلى 10 مل.'),
          code='BX-0047-01-012', key_rows=['test', 'acc', 'prec'], unit={'ar': ['اختبار واحد', 'اختباران', 'اختبارات'], 'en': ['test point', 'test points']}),
])

# p9 laboratory balances & industrial scales -----------------------------------------------------------------
F['laboratory-balances-industrial-scales'] = family('laboratory-balances-industrial-scales', CAT, [
    series('series', ('Laboratory balances and industrial scales', 'موازين المختبر والموازين الصناعية'), ('31 g–3 t', '31 جم–3 طن'), [
        ('BX-0456-01-001', 'Analytical and precision balances, WT-G series', 'موازين تحليلية ودقيقة، سلسلة WT-G',
         'FA604–FA3004, WT2003GH–WT20003GH, WT1003G–WT5003G, WT2002G–WT100002G, WT60001GF–WT15000GF',
         ('60 g to 15 kg; 0.1 mg to 1 g; electromagnetic (FA) or load cell; internal or external calibration; RS232',
          '60 جم إلى 15 كجم؛ 0.1 ملغ إلى 1 جم؛ كهرومغناطيسي (FA) أو خلية حمل؛ معايرة داخلية أو خارجية؛ RS232')),
        ('BX-0456-01-002', '0.01 mg semi-micro balances', 'موازين شبه دقيقة 0.01 ملغ', 'ES1035B(A), ES1055B(A), ES1085B(A), ES2035B(A), ES2055B(A), ES2085B(A)',
         ('120/31 g to 210/82 g; 0.1 / 0.01 mg; internal (A) or external (B) calibration; Ø90 mm pan', '120/31 جم إلى 210/82 جم؛ 0.1 / 0.01 ملغ؛ معايرة داخلية (A) أو خارجية (B)؛ كفة قطر 90 مم')),
        ('BX-0456-01-003', 'Auto internal-calibration balances', 'موازين بمعايرة داخلية آلية', 'JA6003N, JA10003N, FA1204N, FA2204N, FA3204N',
         ('120–320 g at 0.1 mg; 600–1000 g at 1 mg', '120–320 جم بدقة 0.1 ملغ؛ 600–1000 جم بدقة 1 ملغ')),
        ('BX-0456-01-004', 'Precision balances, WT-CH', 'موازين دقيقة، WT-CH', ('WT603CH to WT5003CH', 'WT603CH إلى WT5003CH'),
         ('60–500 g at 1 mg; glass draft shield; RS232 / 485 / USB', '60–500 جم بدقة 1 ملغ؛ واقٍ زجاجي من التيار الهوائي؛ RS232 / 485 / USB')),
        ('BX-0456-01-005', 'Large-capacity precision balances, WT-CF', 'موازين دقيقة كبيرة السعة، WT-CF', ('WT10002CF to WT50002CF', 'WT10002CF إلى WT50002CF'),
         ('1–5 kg at 0.01 g; Ø160 mm stainless pan; counting, % and dynamic weighing', '1–5 كجم بدقة 0.01 جم؛ كفة ستانلس قطر 160 مم؛ العدّ والنسبة المئوية والوزن الديناميكي')),
        ('BX-0456-01-006', 'Classic electronic balances, WT-N', 'موازين إلكترونية كلاسيكية، WT-N', 'WT603N–WT5003N, WT1002N–WT10002N, WT3001N–WT10001N, WT20001NF–WT50001NF',
         ('60 g to 5 kg; 1 mg, 0.01 g or 0.1 g; below-hook weighing for density', '60 جم إلى 5 كجم؛ 1 ملغ أو 0.01 جم أو 0.1 جم؛ وزن بخطاف سفلي لقياس الكثافة')),
        ('BX-0456-01-007', 'Economy electronic balances, WT(B)-K', 'موازين إلكترونية اقتصادية، WT(B)-K', 'WT(B)603K–5003K, 1002K–20002K, 3001K–10001K, 20001KF–10001KF, 1000KF',
         ('60 g to 10 kg; 1 mg to 1 g; LCD (WT) or LED (WTB)', '60 جم إلى 10 كجم؛ 1 ملغ إلى 1 جم؛ شاشة LCD ‏(WT) أو LED ‏(WTB)')),
        ('BX-0456-01-008', 'Double-display balances, WT-A', 'موازين بشاشتين، WT-A', 'WT1002A–WT10002A, WT3001AF–WT20001AF',
         ('100 g to 2 kg; 0.01 or 0.1 g; front and rear displays', '100 جم إلى 2 كجم؛ 0.01 أو 0.1 جم؛ شاشتان أمامية وخلفية')),
        ('BX-0456-01-009', 'Bench counting balances, WT-X', 'موازين عدّ منضدية، WT-X', 'WT64X–WT304X, WT63X–WT303X',
         ('6–30 kg; 0.1 or 1 g; stainless 25×19 cm pan', '6–30 كجم؛ 0.1 أو 1 جم؛ كفة ستانلس 25×19 سم')),
        ('BX-0456-01-017', 'Large-pan bench balances, WT-Y(C)', 'موازين منضدية بكفة كبيرة، WT-Y(C)', 'WT203Y(C)–WT404Y(C)',
         ('20–40 kg; 1 or 0.1 g; 25×36 cm stainless pan', '20–40 كجم؛ 1 أو 0.1 جم؛ كفة ستانلس 25×36 سم')),
        ('BX-0456-01-018', 'Waterproof bench scales', 'موازين منضدية مقاومة للماء', 'WT31WP, WT62WP, WT155WP',
         ('3–15 kg; stainless 304; IP68; 17.5×21 cm pan', '3–15 كجم؛ ستانلس 304؛ IP68؛ كفة 17.5×21 سم')),
        ('BX-0456-01-010', 'Split bench scales, WT-B and WT-LB', 'موازين منضدية بمؤشر منفصل، WT-B وWT-LB', 'WT64B–WT304B, WT63B–WT303B, WT104LB–WT304LB, WT603LB–WT1503LB',
         ('6–150 kg; separate indicator', '6–150 كجم؛ مؤشر منفصل')),
        ('BX-0456-01-011', 'Platform scales, WT-L', 'موازين منصة، WT-L', 'WT603L–WT1503L, WT602L–WT3002L',
         ('60–300 kg; 1 or 10 g; 50×40 cm platform; column indicator; battery; optional wheels', '60–300 كجم؛ 1 أو 10 جم؛ منصة 50×40 سم؛ مؤشر على عمود؛ بطارية؛ عجلات اختيارية')),
        ('BX-0456-01-012', 'Electronic floor scales, WT-D', 'موازين أرضية إلكترونية، WT-D', 'WT10002D, WT20001D, WT30001D',
         ('1–3 t; 100×100 cm platform', '1–3 طن؛ منصة 100×100 سم')),
    ]),
], type_label=('Series', 'السلسلة'))

# p10 XRF analyzers – benchtop & handheld -------------------------------------------------------------------
F['xrf-analyzers-benchtop-handheld'] = family('xrf-analyzers-benchtop-handheld', CAT, [
    table('edx680', ('EDX 680 benchtop gold tester', 'جهاز فحص الذهب المكتبي EDX 680'), ('K–U', 'K–U'),
          [C('elements', 'Elements', 'العناصر'), C('samples', 'Samples', 'العينات'), C('time', 'Measuring time', 'زمن القياس'), C('detector', 'Detector', 'الكاشف'),
           C('tube', 'Tube voltage', 'جهد الأنبوب'), C('view', 'Sample view', 'رؤية العينة'), C('chamber', 'Chamber', 'الحجرة'), C('weight', 'Weight / supply', 'الوزن / التغذية')],
          [(None, 'EDX 680', None, 'K–U', ('Solid, liquid, powder', 'صلبة وسائلة ومسحوق'), ('60–200 s', '60–200 ثانية'), 'Si-PIN', ('5–50 kV', '5–50 كيلوفولت'),
            ('Built-in camera', 'كاميرا مدمجة'), ('292×269×85 mm', '292×269×85 مم'), ('26 kg / 110–220 V', '26 كجم / 110–220 فولت'))],
          code='BX-0047-02-001', key_rows=['elements', 'time', 'detector']),
    table('handheld', ('Handheld XRF analyzers', 'محللات XRF محمولة'), ('Mg–U', 'Mg–U'),
          [C('use', 'Use', 'الاستخدام'), C('detector', 'Detector', 'الكاشف'), C('tube', 'X-ray tube', 'أنبوب الأشعة'), C('elements', 'Elements / reading', 'العناصر / القراءة'),
           C('weight', 'Weight', 'الوزن'), C('notes', 'Notes', 'ملاحظات')],
          [('BX-0048-04-001', 'DW-EX7000', None, ('Ore & minerals', 'الخامات والمعادن'), ('SDD, 128 eV (Fast-SDD opt.)', 'SDD، ‏128 إلكترون فولت (Fast-SDD اختياري)'), ('Ag target, 200 µA', 'هدف فضة، 200 ميكروأمبير'),
            ('Mg–U, up to 40 at once incl. Au, Ag, Pt, Pd, Cu, Pb, Zn; ppm to 99.99%', 'Mg–U، حتى 40 عنصراً معاً منها Au وAg وPt وPd وCu وPb وZn؛ من ppm إلى 99.99%'),
            ('1.7 kg', '1.7 كجم'), ('5" touch screen, camera, GPS; up to 12 h battery', 'شاشة لمس 5 بوصات، كاميرا، GPS؛ بطارية حتى 12 ساعة')),
           ('BX-0048-04-002', 'TrueX 960', None, ('Ore & minerals', 'الخامات والمعادن'), 'SDD', ('Ag target, ≤ 50 kV / 200 µA', 'هدف فضة، ≤ 50 كيلوفولت / 200 ميكروأمبير'),
            ('Mg–U incl. Au, As, Hg; 15 s', 'Mg–U منها Au وAs وHg؛ 15 ثانية'), ('1.6 kg', '1.6 كجم'), ('4.3" screen; ~8 h; −20 to 50 °C', 'شاشة 4.3 بوصة؛ نحو 8 ساعات؛ من −20 إلى 50 °م')),
           ('BX-0048-04-003', 'TrueX 900', None, ('Ore & minerals', 'الخامات والمعادن'), ('Si-PIN, 139 eV', 'Si-PIN، ‏139 إلكترون فولت'), ('Ag target', 'هدف فضة'),
            ('29 elements (standard mode) incl. Au, Ag, Cu, Pb, Zn, As, Hg; 15 s', '29 عنصراً (الوضع القياسي) منها Au وAg وCu وPb وZn وAs وHg؛ 15 ثانية'), ('1.6 kg', '1.6 كجم'),
            ('32 GB; USB, Bluetooth, Wi-Fi, GPS', '32 جيجابايت؛ USB وبلوتوث وWi-Fi وGPS')),
           ('BX-0048-04-004', 'DW-600 / 600S', None, ('Ore & minerals', 'الخامات والمعادن'), 'Si-PIN / SDD', ('W target, 50 kV, ≤ 100 µA; 8 filters', 'هدف تنغستن، 50 كيلوفولت، ≤ 100 ميكروأمبير؛ 8 مرشحات'),
            ('> 30 elements incl. Au, Ag, Cu, Pb, Zn, Mo; 600S adds Mg, Al, Si, P, S', '> 30 عنصراً منها Au وAg وCu وPb وZn وMo؛ ويضيف 600S عناصر Mg وAl وSi وP وS'),
            None, ('Two batteries', 'بطاريتان')),
           ('BX-0048-04-005', 'TrueX G5 / G7', None, ('Gold & precious metals', 'الذهب والمعادن الثمينة'), 'Si-PIN / SDD', ('Ag target, ≤ 50 kV / 200 µA', 'هدف فضة، ≤ 50 كيلوفولت / 200 ميكروأمبير'),
            ('Au, Ag, Pt, Pd, Rh, Ir, Ru, Cu, Zn, Ni; karat 9–24 K and %', 'Au وAg وPt وPd وRh وIr وRu وCu وZn وNi؛ العيار 9–24 قيراطاً والنسبة المئوية'),
            ('1.5 kg', '1.5 كجم'), ('~8 h battery', 'بطارية نحو 8 ساعات')),
           ('BX-0048-04-006', 'DW-8000', None, ('Gold & precious metals', 'الذهب والمعادن الثمينة'), ('Si-PIN, Peltier-cooled', 'Si-PIN مبرّد بتأثير بلتييه'),
            ('35–50 kV, switchable targets', '35–50 كيلوفولت، أهداف قابلة للتبديل'), ('Au, Pt, Ag, Pd, Rh, Ir and base metals', 'Au وPt وAg وPd وRh وIr والمعادن الأساسية'),
            ('1.65 kg', '1.65 كجم'), ('X-rays stop within 2 s without a sample', 'تتوقف الأشعة خلال ثانيتين دون عينة'))],
          key_rows=['use', 'elements', 'weight'], unit=U_INSTR),
], type_label=('Model', 'الموديل'))

# p11 atomic absorption & fluorescence ------------------------------------------------------------------------
F['atomic-absorption-fluorescence-spectrometers'] = family('atomic-absorption-fluorescence-spectrometers', CAT, [
    table('aas', ('AAS models', 'موديلات الامتصاص الذري'), ('190–900 nm', '190–900 نانومتر'),
          [C('atom', 'Atomization', 'التذرية'), C('lamps', 'Lamps', 'المصابيح'), C('slit', 'Slit (nm)', 'الشق (نانومتر)'), C('bg', 'Background correction', 'تصحيح الخلفية'), C('data', 'Key data', 'أهم البيانات')],
          [('BX-0047-03-001', 'AA320N', None, ('Air-acetylene and nitrous oxide-acetylene flame; graphite furnace and hydride generator available', 'لهب هواء-أسيتيلين وأكسيد النيتروز-أسيتيلين؛ فرن جرافيت ومولد هيدريد متاحان'),
            None, '0.2–5.0', ('Deuterium', 'ديوتيريوم'), ('Double beam; ±0.5 nm; Cu DL 0.008 µg/mL; Ti burner 5 cm; 1220×770×730 mm, 160 kg', 'شعاع مزدوج؛ ±0.5 نانومتر؛ حد كشف النحاس 0.008 ميكروجرام/مل؛ موقد تيتانيوم 5 سم؛ 1220×770×730 مم، 160 كجم')),
           ('BX-0048-04-013', 'DW-AA4530F', None, ('Flame (100 mm Ti burner); graphite furnace optional, ≤ 3000 °C', 'لهب (موقد تيتانيوم 100 مم)؛ فرن جرافيت اختياري، ≤ 3000 °م'),
            ('8-turret', 'برج 8 مصابيح'), '0.1–2.0', ('Deuterium, self-absorption', 'ديوتيريوم، امتصاص ذاتي'), ('±0.15 nm; 1800 l/mm grating; Cu DL 0.004 µg/mL', '±0.15 نانومتر؛ محزز 1800 خط/مم؛ حد كشف النحاس 0.004 ميكروجرام/مل')),
           ('BX-0048-04-014', 'DW-AA4730FG', None, ('Flame and graphite furnace integrated, PC switching', 'لهب وفرن جرافيت متكاملان، تبديل بالحاسوب'), None, None,
            ('Deuterium, self-absorption', 'ديوتيريوم، امتصاص ذاتي'), ('Czerny-Turner, 1800 l/mm; auto gas cut-off; ppb level', 'Czerny-Turner، ‏1800 خط/مم؛ قطع آلي للغاز؛ مستوى ppb')),
           ('BX-0048-04-015', 'DW-220A', None, ('Flame + graphite furnace, ≤ 3000 °C, > 2500 °C/s', 'لهب + فرن جرافيت، ≤ 3000 °م، > 2500 °م/ثانية'), ('8, auto', '8، آلي'), '0.1 / 0.2 / 0.4 / 0.8 / 1.6',
            ('Deuterium, Smith-Hieftje', 'ديوتيريوم، Smith-Hieftje'), ('Auto burner height/position; 1020×530×500 mm, 90 kg', 'ضبط آلي لارتفاع الموقد وموضعه؛ 1020×530×500 مم، 90 كجم')),
           ('BX-0048-04-016', 'DW-220B', None, ('Flame, auto ignition', 'لهب، إشعال آلي'), ('8, auto', '8، آلي'), '0.1 / 0.2 / 0.4 / 1.2',
            ('Deuterium, Smith-Hieftje', 'ديوتيريوم، Smith-Hieftje'), ('ppm-level gold in mine labs; 1020×530×500 mm, 85 kg', 'الذهب بمستوى ppm في مختبرات المناجم؛ 1020×530×500 مم، 85 كجم')),
           ('BX-0048-04-017', 'DW-180B', None, ('Automatic flame, single beam', 'لهب آلي، شعاع واحد'), '8', None, None,
            ('71-position autosampler optional; 20 mm cast-aluminium optical bench', 'مُلقّم عينات آلي 71 موضعاً اختياري؛ منصة بصرية من الألومنيوم المصبوب 20 مم'))],
          intro=('All models 190–900 nm. AA320N is supplied with air compressor and Cu lamp; Au lamp on request.', 'جميع الموديلات 190–900 نانومتر. يُورَّد AA320N مع ضاغط هواء ومصباح نحاس؛ مصباح الذهب عند الطلب.'),
          key_rows=['atom', 'bg', 'data'], unit=U_INSTR),
    table('afs', ('Atomic fluorescence & hollow-cathode lamps', 'الفلورة الذرية ومصابيح الكاثود المجوف'), ('', ''), [C('desc', 'Description', 'الوصف')],
          [('BX-0048-04-018', 'DW-AFS310', None, ('Atomic fluorescence spectrometer with hydride generation and two lamp positions for trace Hg, As and Se',
                                                    'مطياف فلورة ذرية بمولد هيدريد وموضعين للمصابيح لقياس الزئبق والزرنيخ والسيلينيوم بتراكيز ضئيلة')),
           ('BX-0048-04-019', 'KY-I to KY-IV lamps', 'مصابيح KY-I إلى KY-IV', ('Hollow-cathode lamps for Au, Ag, Cu, Pb, Zn, Hg, Cd and other elements, with nebulizers and burners',
                                                                           'مصابيح كاثود مجوف للذهب والفضة والنحاس والرصاص والزنك والزئبق والكادميوم وعناصر أخرى، مع البخاخات والمواقد'))],
          unit=U_PRODUCT),
], type_label=('Model', 'الموديل'))

# p12 ICP-OES ------------------------------------------------------------------------------------------------
F['icp-oes-spectrometer'] = family('icp-oes-spectrometer', CAT, [
    table('icp', ('ICP-OES spectrometer', 'مطياف ICP-OES'), ('190–800 nm', '190–800 نانومتر'),
          [C('type', 'Type', 'النوع'), C('optics', 'Optics', 'البصريات'), C('rf', 'RF generator', 'مولد التردد الراديوي'), C('torch', 'Torch', 'الشعلة'),
           C('software', 'Software', 'البرمجيات'), C('use', 'Use', 'الاستخدام')],
          [(None, 'ICP2060T', None, ('Sequential scanning ICP-OES', 'ICP-OES بمسح تتابعي'), ('Holographic grating; 190–500 or 190–800 nm by grating', 'محزز هولوغرافي؛ 190–500 أو 190–800 نانومتر حسب المحزز'),
            ('Self-excited 27.12 MHz with automatic matching', 'ذاتي الإثارة 27.12 ميجاهرتز بمواءمة آلية'), ('Computer-controlled plasma platform', 'منصة بلازما يتحكم فيها الحاسوب'),
            ('Background and spectral-interference correction; instrument diagnostics', 'تصحيح الخلفية والتداخل الطيفي؛ تشخيص الجهاز'),
            ('Multi-element analysis of digested ore, concentrate and process solutions', 'تحليل متعدد العناصر للخام المهضوم والمركّز ومحاليل المعالجة'))],
          intro=('Full specifications (power, dimensions, weight) on request.', 'المواصفات الكاملة (القدرة والأبعاد والوزن) عند الطلب.'),
          code='BX-0050-05-001', key_rows=['type', 'optics', 'rf']),
])

# p13 benchtop XRF, flame AAS & assay crucibles --------------------------------------------------------------
F['benchtop-xrf-flame-aas-crucibles'] = family('benchtop-xrf-flame-aas-crucibles', CAT, [
    table('models', ('Benchtop XRF, flame AAS and fire-assay crucibles – additional models', 'XRF مكتبي ومطياف امتصاص ذري باللهب وبوتقات التحليل بالنار – موديلات إضافية'), ('', ''),
          [C('type', 'Type', 'النوع'), C('optics', 'Detector / optics', 'الكاشف / البصريات'), C('range', 'Range', 'المدى'), C('data', 'Key data', 'أهم البيانات')],
          [('BX-0050-03-001', 'EDX3600H', None, ('Benchtop EDXRF mineral analyzer (vacuum)', 'محلل خامات EDXRF مكتبي (تفريغ)'), ('SDD; thin-window tube 5–50 kV, 50–1000 µA', 'SDD؛ أنبوب بنافذة رقيقة 5–50 كيلوفولت، 50–1000 ميكروأمبير'),
            ('Na–U; ppm–99.99%', 'Na–U؛ ‏ppm–99.99%'), ('Ore grade checks; vacuum pump for light elements; auto collimators and filters; camera; 60–200 s; chamber 320 × 100 mm',
                                                     'فحص رتبة الخام؛ مضخة تفريغ للعناصر الخفيفة؛ مسدّدات ومرشحات آلية؛ كاميرا؛ 60–200 ثانية؛ حجرة 320 × 100 مم')),
           ('BX-0050-04-001', 'EDX6000C', None, ('Benchtop EDXRF spectrometer', 'مطياف EDXRF مكتبي'), ('SDD ≤ 129 eV; tube 5–50 kV, 0–1000 µA', 'SDD ≤ 129 إلكترون فولت؛ أنبوب 5–50 كيلوفولت، 0–1000 ميكروأمبير'),
            ('F–U; ppm–99.99%', 'F–U؛ ‏ppm–99.99%'), ('Single chamber or 9 / 12 / 20-sample changer; vacuum for powders, helium for liquids; detection limit to 0.2 ppm; 646 × 578 × 388 mm, 85 kg',
                                                    'حجرة واحدة أو مبدّل 9 / 12 / 20 عينة؛ تفريغ للمساحيق وهيليوم للسوائل؛ حد كشف حتى 0.2 ppm؛ 646 × 578 × 388 مم، 85 كجم')),
           ('BX-0050-01-001', 'AAS6000', None, ('Flame atomic absorption spectrometer', 'مطياف امتصاص ذري باللهب'), ('350 mm monochromator, 1800 l/mm grating', 'مقياس أحادي اللون 350 مم، محزز 1800 خط/مم'),
            ('190–900 nm', '190–900 نانومتر'), ('8-lamp turret; air-acetylene and nitrous oxide-acetylene flame; D2 and self-reversal background correction; slit 0.1–1.4 nm; 68 elements',
                                                'برج 8 مصابيح؛ لهب هواء-أسيتيلين وأكسيد النيتروز-أسيتيلين؛ تصحيح الخلفية بالديوتيريوم والانعكاس الذاتي؛ شق 0.1–1.4 نانومتر؛ 68 عنصراً')),
           ('BX-0046-04-001', 'Fire-clay crucibles', 'بوتقات طينية', ('Fire-assay crucibles', 'بوتقات التحليل بالنار'), ('Fire clay', 'طين حراري'), ('30 g, 40 g', '30 و40 جم'),
            ('For fusion in fire assay', 'للصهر في التحليل بالنار'))],
          key_rows=['type', 'range', 'data'], unit=U_PRODUCT),
], type_label=('Model', 'الموديل'))

# p14 atomic absorption – additional models ------------------------------------------------------------------
F['atomic-absorption-additional-models'] = family('atomic-absorption-additional-models', CAT, [
    table('models', ('Atomic absorption spectrophotometers – additional models', 'مطيافات الامتصاص الذري – موديلات إضافية'), ('190–900 nm', '190–900 نانومتر'),
          [C('atom', 'Atomization', 'التذرية'), C('lamps', 'Lamps', 'المصابيح'), C('bg', 'Background correction', 'تصحيح الخلفية'), C('data', 'Key data', 'أهم البيانات')],
          [('BX-0048-03-003', 'DW-320', None, ('Flame (economy model)', 'لهب (موديل اقتصادي)'), ('2 powered (1 pre-heating)', 'مصباحان يعملان (واحد للتسخين المسبق)'), ('Deuterium, > 30× at 1 A', 'ديوتيريوم، > 30 ضعفاً عند 1 A'),
            ('Manual wavelength and slit (0.1 / 0.2 / 0.4 / 1.2 nm); 277 mm Czerny-Turner, 1800 l/mm; ±0.5 nm; baseline 0.005 A/30 min; R928 photomultiplier; 10 cm Ti burner; fuel-leak alarm; Cu detection limit ≤ 0.006 mg/L; 1020 × 490 × 540 mm, 80 kg',
             'ضبط يدوي للطول الموجي والشق (0.1 / 0.2 / 0.4 / 1.2 نانومتر)؛ Czerny-Turner ‏277 مم، 1800 خط/مم؛ ±0.5 نانومتر؛ خط الأساس 0.005 A/30 دقيقة؛ مضاعف ضوئي R928؛ موقد تيتانيوم 10 سم؛ إنذار تسرب الوقود؛ حد كشف النحاس ≤ 0.006 ملغ/لتر؛ 1020 × 490 × 540 مم، 80 كجم')),
           ('BX-0048-03-006', 'DW-200', None, ('Flame and graphite furnace, automatic changeover; flame emission for K and Na', 'لهب وفرن جرافيت بتبديل آلي؛ انبعاث لهبي للبوتاسيوم والصوديوم'),
            ('6, motorized turret', '6، برج آلي'), ('Deuterium and S-H, > 30×', 'ديوتيريوم وS-H، > 30 ضعفاً'),
            ('Auto slit 0.1 / 0.2 / 0.4 / 1.2 nm; 277 mm Czerny-Turner; ±0.25 nm; baseline 0.004 A/30 min; furnace to 3000 °C at 2000 °C/s; precision Cd, Cu ≤ 3%; autosampler 55 + 5 vessels, from 1 µl; main unit 140 kg, furnace 65 kg',
             'شق آلي 0.1 / 0.2 / 0.4 / 1.2 نانومتر؛ Czerny-Turner ‏277 مم؛ ±0.25 نانومتر؛ خط الأساس 0.004 A/30 دقيقة؛ فرن حتى 3000 °م بمعدل 2000 °م/ثانية؛ دقة Cd وCu ≤ 3%؛ ملقّم عينات 55 + 5 أوعية من 1 ميكرولتر؛ الجهاز 140 كجم والفرن 65 كجم')),
           ('BX-0048-03-005', 'DW-220C Pro / 220C / 220C Es', None, ('Graphite furnace only', 'فرن جرافيت فقط'), ('8, automatic', '8، آلي'), ('Deuterium; self-absorption (not on Es)', 'ديوتيريوم؛ امتصاص ذاتي (عدا Es)'),
            ('Cd detection limit ≤ 0.5 pg, precision ≤ 2.8%; 190–900 nm; Pro adds a furnace camera; Es with CR131 photomultiplier and 4 slits',
             'حد كشف الكادميوم ≤ 0.5 بيكوجرام، دقة ≤ 2.8%؛ 190–900 نانومتر؛ يضيف Pro كاميرا للفرن؛ Es بمضاعف ضوئي CR131 و4 شقوق')),
           ('BX-0048-03-005', 'AAS accessories', 'ملحقات الامتصاص الذري', None, None, None,
            ('CQ-320 air compressor; HG-C hydride generator; WF-30 flame autosampler (70 vessels); WF-20 furnace autosampler (60 + 6 or 150 + 5 vessels); WF-2A furnace power unit (upgrades 220B to 220A); H50 water chiller; coated graphite tubes',
             'ضاغط هواء CQ-320؛ مولد هيدريد HG-C؛ ملقّم عينات للهب WF-30 ‏(70 وعاء)؛ ملقّم عينات للفرن WF-20 ‏(60 + 6 أو 150 + 5 أوعية)؛ وحدة طاقة للفرن WF-2A ‏(ترقّي 220B إلى 220A)؛ مبرّد ماء H50؛ أنابيب جرافيت مطلية'))],
          intro=('Gold by flame (DW-220 data): Au 242.8 nm, detection limit 0.0032 µg/mL, recommended range 0.2–7.5 µg/mL.',
                 'الذهب باللهب (بيانات DW-220): ‏Au ‏242.8 نانومتر، حد الكشف 0.0032 ميكروجرام/مل، المدى الموصى به 0.2–7.5 ميكروجرام/مل.'),
          key_rows=['atom', 'lamps', 'data'], unit=U_PRODUCT),
], type_label=('Model', 'الموديل'))

# p15 XRF & carbon-sulfur analyzers – additional ------------------------------------------------------------
F['xrf-carbon-sulfur-analyzers'] = family('xrf-carbon-sulfur-analyzers', CAT, [
    series('series', ('XRF and carbon-sulfur analyzers – additional models', 'محللات XRF والكربون والكبريت – موديلات إضافية'), ('', ''), [
        ('BX-0050-06-001', 'Handheld XRF ore analyzer', 'محلل خامات XRF محمول', 'EXPLORER 7000',
         ('Fast-SDD; miniature Rh tube 50 kV / 200 µA; Mg–U; GPS, Bluetooth, HD camera; 1.7 kg; battery up to 12 h', 'Fast-SDD؛ أنبوب روديوم مصغر 50 كيلوفولت / 200 ميكروأمبير؛ Mg–U؛ GPS وبلوتوث وكاميرا عالية الدقة؛ 1.7 كجم؛ بطارية حتى 12 ساعة')),
        ('BX-0208-03-001', 'Handheld XRF analyzers', 'محللات XRF محمولة', 'Expert JX5 (Si-PIN), Expert JX6 (Fast-SDD)',
         ('50 kV, 200 µA, 4 W tube; JX5 Si-PIN 148 eV, Ca–U; JX6 Fast-SDD 123 eV, Mg–U incl. Au; 1–90 s; 1.5 kg; IP54',
          'أنبوب 50 كيلوفولت، 200 ميكروأمبير، 4 واط؛ JX5 ‏Si-PIN ‏148 إلكترون فولت، Ca–U؛ JX6 ‏Fast-SDD ‏123 إلكترون فولت، Mg–U منها الذهب؛ 1–90 ثانية؛ 1.5 كجم؛ IP54')),
        ('BX-0208-01-010', 'Benchtop EDXRF, precious metals and coatings', 'EDXRF مكتبي للمعادن الثمينة والطلاءات', 'TY-9800',
         ('Na–U; 1 ppm–99.99%; SDD 1–50 keV, 130 eV; std. dev. ≤ 0.05%; gold purity, RoHS and coating thickness', 'Na–U؛ ‏1 ppm–99.99%؛ SDD ‏1–50 كيلو إلكترون فولت، 130 إلكترون فولت؛ انحراف معياري ≤ 0.05%؛ نقاء الذهب وRoHS وسماكة الطلاء')),
        ('BX-0208-01-011', 'Benchtop EDXRF for mining and minerals', 'EDXRF مكتبي للتعدين والمعادن', 'P9800',
         ('F–U; 1 ppm–99.99%; Fast SDD 1–50 keV, 127 eV; std. dev. ≤ 0.05%; for pressed powder pellets', 'F–U؛ ‏1 ppm–99.99%؛ Fast SDD ‏1–50 كيلو إلكترون فولت، 127 إلكترون فولت؛ انحراف معياري ≤ 0.05%؛ لأقراص المسحوق المضغوط')),
        ('BX-0208-02-003', 'Benchtop EDXRF with 10-sample turntable', 'EDXRF مكتبي بقرص دوّار لعشر عينات', 'JXT-6800',
         ('F–U; Fast SDD, 127 eV; automatic setting of measuring conditions', 'F–U؛ ‏Fast SDD، ‏127 إلكترون فولت؛ ضبط آلي لظروف القياس')),
        ('BX-0208-02-004', 'Benchtop EDXRF with 31-sample robot arm', 'EDXRF مكتبي بذراع آلية لـ 31 عينة', 'JXT6',
         ('F–U; Fast SDD, 127 eV; 31 sample positions; for high-throughput mine labs', 'F–U؛ ‏Fast SDD، ‏127 إلكترون فولت؛ 31 موضع عينة؛ لمختبرات المناجم عالية الإنتاج')),
        ('BX-0208-01-008', 'Carbon-sulfur analyzer, wide range', 'محلل كربون وكبريت، مدى واسع', 'CS8800S',
         ('High-frequency furnace, infrared detection; C and S 0.000001–99.999999%; RSD C ≤ 0.5%, S ≤ 1.0%; ISO 9556 and ISO 4935',
          'فرن عالي التردد، كشف بالأشعة تحت الحمراء؛ الكربون والكبريت 0.000001–99.999999%؛ الانحراف النسبي للكربون ≤ 0.5% وللكبريت ≤ 1.0%؛ ISO 9556 وISO 4935')),
        ('BX-0208-04-002', 'Carbon-sulfur analyzer, high range', 'محلل كربون وكبريت، مدى مرتفع', 'CS8820T',
         ('C 5–95%, S 1–50%; sensitivity 0.1 ppm; 25–60 s per test; ISO 9556 and ISO 4935; for graphite, coke, coal and pyrite samples',
          'الكربون 5–95% والكبريت 1–50%؛ حساسية 0.1 ppm؛ 25–60 ثانية للاختبار؛ ISO 9556 وISO 4935؛ لعينات الجرافيت وفحم الكوك والفحم والبيريت')),
    ]),
], type_label=('Series', 'السلسلة'))

# p16 spark OES, carbon-sulphur & XRF ------------------------------------------------------------------------
F['spark-oes-carbon-sulphur-xrf-analyzers'] = family('spark-oes-carbon-sulphur-xrf-analyzers', CAT, [
    series('series', ('Analyzers & XRF sample preparation', 'المحللات وتحضير عينات XRF'), ('', ''), [
        ('BX-0206-01-001', 'Spark optical emission spectrometer', 'مطياف انبعاث بصري بالشرارة', 'Exquis T4',
         ('Metals and alloys (Fe, Al, Cu, Zn matrices); Paschen-Runge optics; 160–580 nm; 33 kg', 'المعادن والسبائك (قواعد Fe وAl وCu وZn)؛ بصريات Paschen-Runge؛ 160–580 نانومتر؛ 33 كجم')),
        ('BX-0206-01-002', 'Spark optical emission spectrometer', 'مطياف انبعاث بصري بالشرارة', 'Innovate T5', ('Metals and alloys', 'المعادن والسبائك')),
        ('BX-0206-01-003', 'Spark optical emission spectrometer', 'مطياف انبعاث بصري بالشرارة', 'Noble T7', ('Metals and alloys', 'المعادن والسبائك')),
        ('BX-0206-01-004', 'Mobile spark spectrometer', 'مطياف شرارة متنقل', 'Surpass F1', ('On a trolley for on-site alloy analysis', 'على عربة لتحليل السبائك في الموقع')),
        ('BX-0206-01-005', 'High-frequency infrared carbon & sulphur analyzer', 'محلل كربون وكبريت بالأشعة تحت الحمراء عالي التردد', 'CS2020',
         ('Carbon and sulphur in metals, ores and minerals', 'الكربون والكبريت في المعادن والخامات')),
        ('BX-0206-01-006', 'High-frequency infrared carbon & sulphur analyzers', 'محللات كربون وكبريت بالأشعة تحت الحمراء عالية التردد', 'CS995, CS996',
         ('Carbon and sulphur analysis', 'تحليل الكربون والكبريت')),
        ('BX-0468-01-001', 'Multi-element XRF analyzer', 'محلل XRF متعدد العناصر', 'KL6800', ('Energy-dispersive multi-element analysis', 'تحليل متعدد العناصر بتشتت الطاقة')),
        ('BX-0468-02-001', 'XRF spectrometer', 'مطياف XRF', 'RL-RAY6000T', ('Metals and alloys', 'المعادن والسبائك')),
        ('BX-0468-03-001', 'Vibratory sample mill', 'طاحونة عينات اهتزازية', 'ZHM-PLUS', ('Sample preparation for XRF', 'تحضير العينات لتحليل XRF')),
        ('BX-0468-04-001', 'Automatic pellet press', 'مكبس أقراص آلي', 'ZHY-40PRO, ZHY-60PRO', ('Pressed-pellet preparation for XRF', 'تحضير الأقراص المضغوطة لتحليل XRF')),
    ], unit=U_PRODUCT),
], type_label=('Product', 'المنتج'))

# p17 gold purity, density & lab testing ----------------------------------------------------------------------
F['gold-purity-density-lab-testing'] = family('gold-purity-density-lab-testing', CAT, [
    series('series', ('Gold purity, density and lab testing instruments', 'أجهزة نقاء الذهب والكثافة والاختبارات المخبرية'), ('', ''), [
        ('BX-0456-01-020', 'Gold and silver purity meters', 'أجهزة قياس نقاء الذهب والفضة', 'MDJ-300K, MDJ-1200K',
         ("300 g and 1200 g at 0.01 g; reads gold karat 9–24 K, density and purity % by Archimedes' principle", '300 جم و1200 جم بدقة 0.01 جم؛ يقرأ عيار الذهب 9–24 قيراطاً والكثافة ونسبة النقاء بمبدأ أرخميدس')),
        ('BX-0456-01-014', 'Hydrostatic density balances, WT-S', 'موازين كثافة هيدروستاتيكية، WT-S', 'WT20001SF, WT50001SF, WT104XS, WT303XS, WT1003GHS, WT5003GHS',
         ('100 g to 30 kg; density software; solid and liquid kits', '100 جم إلى 30 كجم؛ برنامج للكثافة؛ أطقم للمواد الصلبة والسوائل')),
        ('BX-0456-01-016', 'Moisture analyzers, MB(T)', 'محللات الرطوبة، MB(T)', 'MB1203(T), MB1203-5(T), MB1202(T)',
         ('120 g; 1, 5 or 10 mg; halogen heating to 180 °C', '120 جم؛ 1 أو 5 أو 10 ملغ؛ تسخين بالهالوجين حتى 180 °م')),
        ('BX-0456-01-023', 'Laboratory pH meters', 'أجهزة قياس pH مخبرية', 'PH-25, PH-3C, PHS-3CB, PHS-3CU',
         ('pH 0–14 or -2.00 to 19.99; 0.01 resolution; manual or automatic temperature compensation', 'pH من 0 إلى 14 أو من -2.00 إلى 19.99؛ دقة 0.01؛ تعويض حراري يدوي أو آلي')),
        ('BX-0456-01-024', 'Rotational viscometers', 'مقاييس لزوجة دورانية', 'NDJ-5S, NDJ-8S, DV-1, RVDV-1',
         ('1 to 2,000,000 mPa·s; RVDV-1 to 13,000,000 mPa·s', 'من 1 إلى 2,000,000 ملي باسكال·ثانية؛ RVDV-1 حتى 13,000,000 ملي باسكال·ثانية')),
        ('BX-0456-01-022', 'Calibration weights', 'أوزان المعايرة', ('Classes E1, E2, F1, F2, M1', 'فئات E1 وE2 وF1 وF2 وM1'), ('Weight sets with cases and tweezers', 'أطقم أوزان بعلب وملاقط')),
        ('BX-0456-01-021', 'Balance data printers', 'طابعات بيانات الموازين', 'TX-100, TX-110, TX-120',
         ('Print weight, date and statistics; GLP / GMP formats', 'طباعة الوزن والتاريخ والإحصاءات؛ بصيغ GLP / GMP')),
    ]),
], type_label=('Series', 'السلسلة'))

# p18 metallurgical test laboratory equipment ----------------------------------------------------------------
F['metallurgical-test-laboratory-equipment'] = family('metallurgical-test-laboratory-equipment', CAT, [
    series('series', ('Ore testing equipment', 'معدات اختبار الخام'), ('', ''), [
        ('BX-0188-01-001', 'Laboratory crushers', 'كسارات مختبرية', ('DG double-roll, XPF disc pulverizer, MPS, PC hammer crusher, DF-4', 'DG مزدوجة الأسطوانة، وساحقة قرصية XPF، وMPS، وكسارة مطرقية PC، وDF-4'),
         ('Sample preparation crushing', 'تكسير العينات للتحضير')),
        ('BX-0188-01-002', 'Laboratory jaw crushers', 'كسارات فكية مختبرية', ('PE, HPEF (suspended), EPS (sealed)', 'PE وHPEF (معلّقة) وEPS (محكمة)'), ('Sample preparation jaw crushing', 'تكسير العينات بالفكين')),
        ('BX-0188-01-004', 'Laboratory ball & rod mills', 'طواحين كرات وقضبان مختبرية', ('XMB, XMQ, QM tube mill, XMGB work-index mill, MJQL, XMQL Ø420×450', 'XMB وXMQ وطاحونة أنبوبية QM وطاحونة مؤشر العمل XMGB وMJQL وXMQL ‏420×450'),
         ('Grinding tests and Bond work-index tests', 'اختبارات الطحن ومؤشر عمل بوند')),
        ('BX-0188-01-005', 'Laboratory grinders & wet pan mill', 'مطاحن مختبرية وطاحونة رطبة', 'XPM Ø120×3, XPWL, LQM-Ø600 / Ø300', ('Fine grinding and gravity tests', 'الطحن الناعم واختبارات الجاذبية')),
        ('BX-0188-01-006', 'Laboratory flotation machines', 'آلات تعويم مختبرية', 'XFD, XFG, XFD-12, XFLB, FX', ('Single-cell and multi-cell flotation tests', 'اختبارات التعويم بخلية واحدة أو بعدة خلايا')),
        ('BX-0188-01-007', 'Leaching agitator XJT', 'خلاط إذابة XJT', 'XJT', ('Bottle-roll leach and agitation tests', 'اختبارات الإذابة في القوارير الدوّارة والخلط')),
        ('BX-0188-01-008', 'Sample splitters & roasting kiln', 'مقسّمات العينات وفرن التحميص', ('XSHF2-3 wet splitter, NTL-WF, SHY-I', 'مقسّم رطب XSHF2-3 وNTL-WF وSHY-I'),
         ('Sample division and roasting tests', 'تقسيم العينات واختبارات التحميص')),
        ('BX-0188-01-009', 'Laboratory magnetic separators', 'فواصل مغناطيسية مختبرية', ('CRS Ø400×300 wet drum, XCGS Ø50, CSQ 50×70', 'أسطوانة رطبة CRS ‏400×300 وXCGS ‏50 وCSQ ‏50×70'),
         ('Magnetic separation tests', 'اختبارات الفصل المغناطيسي')),
        ('BX-0188-01-010', 'Sieve shakers & lab vibrating screens', 'هزازات مناخل وغرابيل اهتزازية مختبرية', 'XSZ-200, XSBP, XSZ-600×300', ('Particle-size analysis', 'تحليل حجم الحبيبات')),
        ('BX-0188-01-013', 'Laboratory gravity concentrators', 'مركّزات جاذبية مختبرية', ('LYN(S)-1100×500 shaking table, XCT, XDT', 'طاولة هزّازة LYN(S)-1100×500 وXCT وXDT'), ('Gravity separation tests', 'اختبارات الفصل بالجاذبية')),
        ('BX-0188-01-014', 'Laboratory desorption & electrowinning unit', 'وحدة نزع واستخلاص كهربائي مختبرية', ('Laboratory unit', 'وحدة مختبرية'),
         ('Carbon elution and gold electrowinning tests', 'اختبارات نزع الكربون واستخلاص الذهب كهربائياً')),
    ], unit=U_PRODUCT),
], type_label=('Product', 'المنتج'))
