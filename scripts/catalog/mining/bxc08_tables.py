"""BXC-08 Ed7 (Smelting & refining) model tables, catalogue pages 3–8. Typed from the page text and checked
against the page images where cells wrap. Every BX code is checked against the supplier list (list_index.json)."""
from lib import table, family
from bxc02_tables import U_LINES, U_GRADE

CAT = 'BXC-08 Ed7'
F = {}
U_PRODUCT = {'ar': ['منتج واحد', 'منتجان', 'منتجات'], 'en': ['product', 'products']}
U_SIZES = {'ar': ['مقاس واحد', 'مقاسان', 'مقاسات'], 'en': ['size', 'sizes']}
SERIES = [('models', 'Models / sizes', 'الموديلات والمقاسات'), ('data', 'Key data', 'أهم البيانات')]

# p3 induction gold smelting furnaces ----------------------------------------------------------------------
F['induction-gold-smelting-furnaces'] = family('induction-gold-smelting-furnaces', CAT, [
    table('portable', ('Portable high/medium-frequency melting furnaces', 'أفران صهر محمولة عالية ومتوسطة التردد'), ('1–100 kg per melt', '1–100 كجم للصهرة'),
          [('power', 'Power (kW)', 'القدرة (كيلوواط)'), ('voltage', 'Voltage (V)', 'الجهد (فولت)'), ('hf', 'High frequency (kHz)', 'التردد العالي (كيلوهرتز)'),
           ('mf', 'Medium frequency (kHz)', 'التردد المتوسط (كيلوهرتز)'), ('weight', 'Weight (kg)', 'الوزن (كجم)'), ('melt', 'Melting capacity (kg)', 'سعة الصهر (كجم)'),
           ('time', 'Melting time (min)', 'زمن الصهر (دقيقة)')],
          [(None, '15A', None, '2', '220', '30–50', '1–15', '15', '1–2', '≤ 5'),
           (None, '25A', None, '5', '380', '30–50', '1–15', '25', '1–4', '≤ 5'),
           (None, '35AB', None, '10', '380', '30–50', '1–15', '35', '1–8', '≤ 10'),
           (None, '45AB', None, '15', '380', '30–50', '1–15', '70', '1–15', '≤ 15'),
           (None, '60AB', None, '20', '380', '30–50', '1–15', '70', '1–25', '≤ 20'),
           (None, '80AB', None, '30', '380', '30–50', '1–15', '90', '1–40', '≤ 30'),
           (None, '100AB', None, '45', '380', '30–50', '1–15', '120', '1–50', '≤ 40'),
           (None, '120AB', None, '70', '380', '30–50', '1–15', '150', '1–100', '≤ 40')],
          code='BX-0029-01-006', key_rows=['power', 'melt', 'time']),
    table('wgr', ('WGR high-frequency induction furnaces', 'أفران حث عالية التردد WGR'), ('1–4 kg gold per melt', '1–4 كجم ذهب للصهرة'),
          [('supply', 'Supply', 'التغذية'), ('input', 'Input (V)', 'جهد الدخل (فولت)'), ('gold', 'Gold per melt (kg)', 'الذهب في الصهرة (كجم)'),
           ('current', 'Output current (A)', 'تيار الخرج (أمبير)'), ('freq', 'Frequency (kHz)', 'التردد (كيلوهرتز)'),
           ('water', 'Cooling water (MPa)', 'ماء التبريد (ميجاباسكال)'), ('time_min', 'Melting time (min)', 'زمن الصهر (دقيقة)')],
          [(None, 'WGR-1-5', None, ('3-phase 380 V', '3 أطوار 380 فولت'), '360–410', '1', '180–700', '30–100', '0.1–0.3', '< 5'),
           (None, 'WGR-1-10', None, ('3-phase 380 V', '3 أطوار 380 فولت'), '360–410', '3–4', '180–1200', '30–100', '0.1–0.3', '< 8')],
          code='BX-0028-01-037', key_rows=['gold', 'freq', 'time_min']),
    table('gwj', ('GWJ medium-frequency coreless induction furnaces', 'أفران حث بلا قلب متوسطة التردد GWJ'), ('150–500 kg', '150–500 كجم'),
          [('rated_power', 'Rated power (kW)', 'القدرة المقننة (كيلوواط)'), ('supply_vhz', 'Supply voltage / frequency (V / Hz)', 'جهد وتردد التغذية (فولت / هرتز)'),
           ('phases', 'Phases', 'الأطوار'), ('consumption', 'Power consumption (kW/h)', 'استهلاك الطاقة (كيلوواط/ساعة)'),
           ('water_th', 'Water consumption (t/h)', 'استهلاك الماء (طن/ساعة)'), ('inverter', 'Inverter output (V/A)', 'خرج العاكس (فولت/أمبير)'),
           ('furnace_va', 'Furnace voltage / current (V/A)', 'جهد وتيار الفرن (فولت/أمبير)'), ('furnace_hz', 'Furnace frequency (Hz)', 'تردد الفرن (هرتز)'),
           ('capacity_kg', 'Rated capacity (kg)', 'السعة المقننة (كجم)'), ('temp', 'Rated temperature (°C)', 'الحرارة المقننة (°م)'),
           ('weight_kg', 'Weight excl. lining (kg)', 'الوزن دون البطانة (كجم)')],
          [(None, 'GWJ-0.15-100/1', None, '110', '380 / 50', '3', '850', '5', '750 / 250', '100 / 650', '1000', '150', '1600', '540'),
           (None, 'GWJ-0.25-160/1', None, '170', '380 / 50', '3', '800', '5', '750 / 350', '160 / 750', '1000', '250', '1600', '600'),
           (None, 'GWJ-0.5-250/1', None, '275', '380 / 50', '3', '750', '10', '750 / 550', '100 / 1300', '1000', '500', '1600', '1000')],
          intro=('Power consumption unit as stated by the manufacturer.', 'وحدة استهلاك الطاقة كما ذكرها المصنّع.'),
          code='BX-0028-01-037', key_rows=['capacity_kg', 'rated_power', 'temp']),
])

# p4 gold melting furnaces – additional models --------------------------------------------------------------
F['gold-melting-furnaces'] = family('gold-melting-furnaces', CAT, [
    table('series', ('Gold melting furnaces – additional models', 'أفران صهر الذهب – موديلات إضافية'), ('1–250 kg', '1–250 كجم'), SERIES,
          [('BX-0436-01-001', '1 kg precious-metal melting furnace', 'فرن صهر معادن ثمينة 1 كجم', 'JL-MF-1',
            ('Up to 1 kg; 1500 W; 220 V or 110 V; max. 1150 °C; ±0.5% FS; 310 × 360 × 370 mm; 15 kg',
             'حتى 1 كجم؛ 1500 واط؛ 220 أو 110 فولت؛ حتى 1150 °م؛ دقة ±0.5% FS؛ 310 × 360 × 370 مم؛ 15 كجم')),
           ('BX-0436-01-002', 'High-frequency induction melting furnaces', 'أفران صهر بالحث عالية التردد', 'JL-15KW, JL-25KW',
            ('JL-15: 1–2 kg gold or silver, 220 V, 15 kW; JL-25: 3–5 kg, 380 V, 25 kW; 30–100 kHz; 3–5 min per melt',
             'JL-15: ‏1–2 كجم ذهب أو فضة، 220 فولت، 15 كيلوواط؛ JL-25: ‏3–5 كجم، 380 فولت، 25 كيلوواط؛ 30–100 كيلوهرتز؛ 3–5 دقائق للصهرة')),
           ('BX-0436-01-003', 'Cabinet induction melting furnaces', 'أفران صهر بالحث بخزانة',
            ('JL-MFG, 1 to 8 kg (1, 2, 3, 4, 5, 5.5, 6, 8 kg)', 'JL-MFG، من 1 إلى 8 كجم (1، 2، 3، 4، 5، 5.5، 6، 8 كجم)'),
            ('IGBT; gold, silver, copper; 3–5 min per melt; 24 h full-load duty; voltage, current and water-loss protection',
             'IGBT؛ ذهب وفضة ونحاس؛ 3–5 دقائق للصهرة؛ تشغيل 24 ساعة بالحمل الكامل؛ حماية من الجهد والتيار وانقطاع الماء')),
           ('BX-0436-02-001', 'Medium-frequency induction melting furnaces', 'أفران صهر بالحث متوسطة التردد',
            ('JLZ-15, 25, 35, 45, 70, 90, 110, 160 kW; fixed, tilting or push-out', 'JLZ-15، 25، 35، 45، 70، 90، 110، 160 كيلوواط؛ ثابتة أو قلّابة أو بالدفع'),
            ('Copper and precious metals 5–10 kg (15 kW) to 150–250 kg (160 kW); steel 3–130 kg; aluminium 30–350 kg; under 1 m²',
             'النحاس والمعادن الثمينة من 5–10 كجم (15 كيلوواط) إلى 150–250 كجم (160 كيلوواط)؛ الفولاذ 3–130 كجم؛ الألومنيوم 30–350 كجم؛ أقل من 1 م²'))],
          unit=U_LINES),
], type_label=('Series', 'السلسلة'))

# p5 firebricks, electrodes & induction units ---------------------------------------------------------------
F['firebricks-electrodes-induction-units'] = family('firebricks-electrodes-induction-units', CAT, [
    table('bricks', ('Firebricks, mortars & electrodes', 'الطوب الحراري والملاط والأقطاب'), ('1200–1760 °C', '1200–1760 °م'), SERIES,
          [('BX-0453-01-019', 'Insulating firebrick', 'طوب حراري عازل', ('9 grades, 1200–1730 °C', '9 درجات، 1200–1730 °م'),
            ('Al2O3 35–75%; density 480–1200 kg/m³; crushing strength 1.1–4.0 MPa', 'أكسيد الألومنيوم 35–75%؛ الكثافة 480–1200 كجم/م³؛ مقاومة السحق 1.1–4.0 ميجاباسكال')),
           ('BX-0453-01-022', 'Refractory mortars & binders', 'ملاط ومواد ربط حرارية', 'HJM2600, HJM2800, HJM3300',
            ('Classification 1430, 1650 and 1760 °C; laying firebrick and furnace repair', 'تصنيف 1430 و1650 و1760 °م؛ لرصّ الطوب الحراري وإصلاح الأفران')),
           ('BX-0453-01-023', 'Fire clay brick', 'طوب طيني حراري', 'SK30, SK32, SK34', ('Al2O3 40–50%', 'أكسيد الألومنيوم 40–50%')),
           ('BX-0453-01-024', 'High-alumina brick', 'طوب عالي الألومينا', 'SK36, SK38, SK40', ('Al2O3 55–80%', 'أكسيد الألومنيوم 55–80%')),
           ('BX-0453-01-027', 'Graphite electrodes', 'أقطاب جرافيت', ('RP, HP and UHP grades', 'درجات RP وHP وUHP'),
            ('To YB/T 4089; diameters to order; for electric-arc furnaces', 'وفق YB/T 4089؛ الأقطار حسب الطلب؛ لأفران القوس الكهربائي'))],
          unit=U_LINES),
    table('induction', ('Induction heating & melting units, chillers', 'وحدات التسخين والصهر بالحث والمبرّدات'), ('15–500 kW', '15–500 كيلوواط'), SERIES,
          [('BX-0438-01-001', 'High-frequency induction heater (single unit)', 'جهاز تسخين حثي عالي التردد (وحدة واحدة)',
            'GHF-15, GHF-15A, GHF-15B, GHF-15AB, GHF-25, GHF-25A, GHF-25B, GHF-25AB',
            ('8–15 kW; 30–100 kHz; GHF-15 single-phase 220 V, GHF-25 three-phase 380/415/440 V; 80% duty; water cooled; small-batch gold, silver and copper melting with crucible and coil',
             '8–15 كيلوواط؛ 30–100 كيلوهرتز؛ GHF-15 أحادي الطور 220 فولت، وGHF-25 ثلاثي الأطوار 380/415/440 فولت؛ دورة تشغيل 80%؛ تبريد مائي؛ لصهر كميات صغيرة من الذهب والفضة والنحاس ببوتقة وملف')),
           ('BX-0438-01-002', 'High-frequency induction heaters (split type)', 'أجهزة تسخين حثي عالية التردد (منفصلة)',
            'GHF-25BD/25ABD, GHF-30B/30AB, GHF-40B/40AB, GHF-45B/45AB, GHF-50BD, GHF-70B/70AB, GHF-70BD, GHF-100B/100AB',
            ('20–100 kW; 30–80 kHz; three-phase 380/415/440 V; 100% duty; water cooling 0.2 MPa',
             '20–100 كيلوواط؛ 30–80 كيلوهرتز؛ ثلاثي الأطوار 380/415/440 فولت؛ دورة تشغيل 100%؛ تبريد مائي 0.2 ميجاباسكال')),
           ('BX-0438-01-009', 'Medium-frequency induction melting units', 'وحدات صهر حثي متوسطة التردد',
            'GMF-15, -25, -35, -45, -70, -90, -110, -160, -200, -300, -500',
            ('15–500 kW; 1–20 kHz; three-phase 380/415/440 V, 50/60 Hz; 100% duty (24 h); water 0.2 MPa, 10–30 L/min; top-open, tilting or vacuum furnaces',
             '15–500 كيلوواط؛ 1–20 كيلوهرتز؛ ثلاثي الأطوار 380/415/440 فولت، 50/60 هرتز؛ دورة تشغيل 100% (24 ساعة)؛ ماء 0.2 ميجاباسكال و10–30 لتر/دقيقة؛ أفران مفتوحة من الأعلى أو قلّابة أو مفرّغة')),
           ('BX-0438-01-015', 'Air-cooled industrial chillers', 'مبرّدات صناعية بالهواء',
            'CA-0.5, CA-1, CA-2, CA-3, CA-4, CA-5, CA-6, CA-8(D), CA-10(D)',
            ('Cooling capacity about 1.5–26 kW (50 Hz); hermetic compressor; R22 (R134a / R407C); tank and pump; for induction heating and melting',
             'سعة تبريد نحو 1.5–26 كيلوواط (50 هرتز)؛ ضاغط محكم؛ R22 ‏(R134a / R407C)؛ خزان ومضخة؛ لأجهزة التسخين والصهر بالحث'))],
          unit=U_LINES),
], type_label=('Series', 'السلسلة'))

# p6 fused-quartz & silicon-carbide crucibles -----------------------------------------------------------------
F['fused-quartz-silicon-carbide-crucibles'] = family('fused-quartz-silicon-carbide-crucibles', CAT, [
    table('quartz', ('Fused-quartz (silica) crucibles for induction gold melting – sizes available now', 'بوتقات كوارتز منصهر (سيليكا) لصهر الذهب بالحث – مقاسات متوفرة'),
          ('Ø100–365 mm', 'قطر 100–365 مم'),
          [('dia', 'Diameter (mm)', 'القطر (مم)'), ('height', 'Height (mm)', 'الارتفاع (مم)')],
          [(None, 'Ø100 × 130', None, '100', '130'), (None, 'Ø160 × 130', None, '160', '130'), (None, 'Ø210 × 150', None, '210', '150'),
           (None, 'Ø285 × 260', None, '285', '260'), (None, 'Ø295 × 250', None, '295', '250'), (None, 'Ø325 × 285', None, '325', '285'),
           (None, 'Ø365 × 345', None, '365', '345')],
          intro=('For 1, 2, 3, 5, 10 and 20 kg gold melts. Other sizes made to order.', 'لصهرات ذهب 1 و2 و3 و5 و10 و20 كجم. المقاسات الأخرى تُصنع حسب الطلب.'),
          code='BX-0046-02-001', unit=U_SIZES),
    table('sic', ('Silicon-carbide crucibles for gas and diesel melting furnaces', 'بوتقات كربيد السيليكون لأفران الصهر بالغاز والديزل'), ('', ''),
          [('supply', 'Supply', 'التوريد'), ('quote', 'Data needed for a quotation', 'البيانات المطلوبة لعرض السعر')],
          [(None, 'Silicon-carbide crucibles', 'بوتقات كربيد السيليكون', ('Made to order', 'تُصنع حسب الطلب'),
            ('Outer Ø, height, metal capacity and furnace type', 'القطر الخارجي والارتفاع وسعة المعدن ونوع الفرن'))],
          code='BX-0046-02-002', unit=U_LINES),
])

# p7 refractories, quartz glass & ceramics ------------------------------------------------------------------
F['refractories-quartz-glass-ceramics'] = family('refractories-quartz-glass-ceramics', CAT, [
    table('refractories', ('Refractories and insulation for furnaces', 'الحراريات والعوازل للأفران'), ('900–1400 °C', '900–1400 °م'),
          [('grade', 'Grade / models', 'الدرجة / الموديلات'), ('temp', 'Max. service temp. (°C)', 'أقصى حرارة تشغيل (°م)'), ('density', 'Bulk density (g/cm³)', 'الكثافة الظاهرية (جم/سم³)')],
          [('BX-0045-01-005', 'Low-cement castable', 'خرسانة حرارية منخفضة الأسمنت', ('Al2O3 ≥ 40% and ≥ 65%', 'أكسيد الألومنيوم ≥ 40% و≥ 65%'), '1300–1400', '2.30–2.55'),
           ('BX-0045-01-007', 'High-alumina plastic refractory', 'حراريات لدنة عالية الألومينا', ('RS-PA70, Al2O3 ≥ 70%, phosphate bonded', 'RS-PA70، أكسيد الألومنيوم ≥ 70%، رابط فوسفاتي'), '1400', '2.7'),
           ('BX-0045-01-011', 'Lightweight insulating castable', 'خرسانة عازلة خفيفة', ('RS-LW1.2, RS-LW1.0, RS-LW0.8; Al2O3 ≥ 30%', 'RS-LW1.2 وRS-LW1.0 وRS-LW0.8؛ أكسيد الألومنيوم ≥ 30%'), '900–1100', '0.8–1.2'),
           ('BX-0045-01-009', 'Aluminium silicate fibre board', 'لوح ألياف سيليكات الألومنيوم', ('PXB-1000; Al2O3 ≥ 45%', 'PXB-1000؛ أكسيد الألومنيوم ≥ 45%'), '1000', '0.28–0.80'),
           ('BX-0045-01-015', 'High-alumina, phosphate-bonded and fire-clay bricks', 'طوب عالي الألومينا وفوسفاتي وطين حراري',
            ('Al2O3 48–75% (high-alumina), 71–80% (phosphate-bonded)', 'أكسيد الألومنيوم 48–75% (عالي الألومينا)، و71–80% (فوسفاتي)'),
            ('Refractoriness 1720–1790', 'مقاومة حرارية 1720–1790'), None),
           ('BX-0045-03-026', 'Alumina hollow-sphere insulating castable', 'خرسانة عازلة بكرات ألومينا مجوفة', None, None, None),
           ('BX-0045-03-027', 'Mullite insulating brick', 'طوب موليت عازل', None, None, None),
           ('BX-0045-03-028', 'High-alumina insulating brick', 'طوب عازل عالي الألومينا', None, None, None),
           ('BX-0045-03-029', 'Alumina hollow-ball insulating brick', 'طوب عازل بكرات ألومينا مجوفة', None, None, None),
           ('BX-0045-03-030', 'Insulation boards', 'ألواح العزل', ('Calcium silicate, aluminium silicate fibre, rock wool, composite silicate', 'سيليكات الكالسيوم، وألياف سيليكات الألومنيوم، والصوف الصخري، والسيليكات المركّبة'), None, None)],
          intro=('Bricks: refractoriness under load 1250–1500 °C. Fibre board thermal conductivity ≤ 0.14 W/(m·K) at 680 °C.',
                 'الطوب: مقاومة حرارية تحت الحمل 1250–1500 °م. الموصلية الحرارية للوح الألياف ≤ 0.14 واط/(م·كلفن) عند 680 °م.'),
          unit=U_PRODUCT),
    table('quartz-ceramics', ('Quartz glass and industrial ceramics', 'زجاج الكوارتز والسيراميك الصناعي'), ('', ''),
          [('desc', 'Description', 'الوصف')],
          [('BX-0046-01-003', 'Quartz glass', 'زجاج الكوارتز',
            ('Opaque quartz crucibles with lids, tubes, plates, discs, rods and trays; high heat and thermal-shock resistance, acid and alkali resistant, high purity; made to order',
             'بوتقات كوارتز معتمة بأغطية، وأنابيب وألواح وأقراص وقضبان وصوانٍ؛ تتحمل الحرارة العالية والصدمة الحرارية، ومقاومة للأحماض والقلويات، وعالية النقاء؛ تُصنع حسب الطلب')),
           ('BX-0046-01-002', 'Industrial ceramics', 'السيراميك الصناعي',
            ('Wear blocks and tiles, tubes, seal rings, trays and square crucibles, made to drawing for wear linings and process equipment',
             'كتل وبلاطات مقاومة للتآكل، وأنابيب وحلقات إحكام وصوانٍ وبوتقات مربعة، تُصنع حسب الرسم لبطانات التآكل ومعدات المعالجة'))],
          unit=U_PRODUCT),
], type_label=('Product', 'المنتج'), unit=U_PRODUCT)

# p8 ceramic fibre & furnace insulation ---------------------------------------------------------------------
F['ceramic-fibre-furnace-insulation'] = family('ceramic-fibre-furnace-insulation', CAT, [
    table('fibre', ('Ceramic fibre & insulation products', 'منتجات الألياف الخزفية والعزل'), ('950–1430 °C', '950–1430 °م'), SERIES,
          [('BX-0453-01-002', 'Ceramic fibre blanket', 'بطانية ألياف خزفية', ('1260 STD, 1260 HP, 1430 HZ; density 80, 96, 128, 160 kg/m³', '1260 STD و1260 HP و1430 HZ؛ الكثافة 80 و96 و128 و160 كجم/م³'),
            ('Classification 1260 and 1430 °C; Al2O3 34–45%', 'تصنيف 1260 و1430 °م؛ أكسيد الألومنيوم 34–45%')),
           ('BX-0453-01-003', 'Ceramic fibre board', 'لوح ألياف خزفية', 'LNTX-1050B, LNTX-1260B, LNTX-1260HPB, LNTX-1430B',
            ('Density 250–320 kg/m³; shrinkage ≤ 4% at 950–1350 °C; conductivity ≤ 0.165 W/m·K', 'الكثافة 250–320 كجم/م³؛ الانكماش ≤ 4% عند 950–1350 °م؛ الموصلية الحرارية ≤ 0.165 واط/م·كلفن')),
           ('BX-0453-01-004', 'Ceramic fibre paper', 'ورق ألياف خزفية', 'STD, HA, HZ',
            ('Al2O3 34–52%; ZrO2 ≥ 15% (HZ); tensile strength ≥ 0.3 MPa', 'أكسيد الألومنيوم 34–52%؛ أكسيد الزركونيوم ≥ 15% (HZ)؛ مقاومة الشد ≥ 0.3 ميجاباسكال')),
           ('BX-0453-01-006', 'Vacuum-formed ceramic fibre shapes', 'أشكال ألياف خزفية مشكّلة بالتفريغ', ('LNTX-1050VF to LNTX-1430VF (6 grades)', 'من LNTX-1050VF إلى LNTX-1430VF (6 درجات)'),
            ('Density 180–250 kg/m³; 950–1350 °C; shapes made to order (covers, holders)', 'الكثافة 180–250 كجم/م³؛ 950–1350 °م؛ أشكال حسب الطلب (أغطية وحوامل)')),
           ('BX-0453-01-008', 'Ceramic fibre cloth', 'قماش ألياف خزفية', ('FG cloth, SS cloth', 'قماش FG وقماش SS'),
            ('Al2O3 45–46%; glass-filament or stainless-wire reinforced', 'أكسيد الألومنيوم 45–46%؛ مقوّى بخيوط زجاجية أو أسلاك ستانلس')),
           ('BX-0453-01-009', 'Ceramic fibre tape', 'شريط ألياف خزفية', ('FG tape, SS tape', 'شريط FG وشريط SS'),
            ('Up to 1000 °C; furnace doors and joints', 'حتى 1000 °م؛ لأبواب الأفران والوصلات')),
           ('BX-0453-01-010', 'Ceramic fibre rope', 'حبل ألياف خزفية', ('FG / SS round, square and twisted rope', 'حبال FG / SS مستديرة ومربعة ومجدولة'),
            ('Density 500–650 kg/m³; 500–600 °C (FG), 1000 °C (SS); furnace-door seals', 'الكثافة 500–650 كجم/م³؛ 500–600 °م (FG) و1000 °م (SS)؛ حشوات أبواب الأفران')),
           ('BX-0453-01-012', 'Bio-soluble fibre blanket', 'بطانية ألياف قابلة للذوبان حيوياً', ('GBSF-1260T; density 80, 96, 128 kg/m³', 'GBSF-1260T؛ الكثافة 80 و96 و128 كجم/م³'),
            ('SiO2 55–65%, CaO 23–35%, MgO 5–10%; 1260 °C', 'سيليكا 55–65%، وأكسيد الكالسيوم 23–35%، وأكسيد المغنيسيوم 5–10%؛ 1260 °م')),
           ('BX-0453-01-013', 'Bio-soluble fibre board', 'لوح ألياف قابلة للذوبان حيوياً', ('GBSF-1260B; density 280–380 kg/m³', 'GBSF-1260B؛ الكثافة 280–380 كجم/م³'),
            ('Solubility ≥ 200 mg/l; tensile strength ≥ 0.1 MPa', 'الذوبانية ≥ 200 ملغ/لتر؛ مقاومة الشد ≥ 0.1 ميجاباسكال')),
           ('BX-0453-01-017', 'Microporous insulation board & felt', 'ألواح ولبّاد عزل ميكروبوري',
            ('950 TT Eco / Classic board, 950 TT Flex felt, TT 1050 Classic, TT 1050 Flex felt, special shapes', 'ألواح 950 TT Eco / Classic، ولبّاد 950 TT Flex، وTT 1050 Classic، ولبّاد TT 1050 Flex، وأشكال خاصة'),
            ('Classification 950 and 1050 °C; density 250–350 kg/m³; for melting furnaces', 'تصنيف 950 و1050 °م؛ الكثافة 250–350 كجم/م³؛ لأفران الصهر'))],
          unit=U_PRODUCT),
], type_label=('Product', 'المنتج'), unit=U_PRODUCT)
