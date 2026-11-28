"""BXC-04 Ed6 (Crushing, grinding & screening) model tables, part 2: grinding & classifying, feeding, screening &
conveying, and wear & spare parts (catalogue pages 21–54). "Additional sizes / models / series / types" pages are
merged into their families, as the crusher pages 19–20 were. Clean tables come from the page drawing
(bxc04b_pages.json: header cells are the dark-grey cells, rows end at the thin rules); tables with mixed or
bilingual cells are typed here from the page image (the JSON keeps only the tables read automatically). Every BX code is one product line in the supplier list under
BXC-04; where the catalogue prints one code over a group (BX-0302-01-007 · 008 · 009 · 015) each line gets its own
row, and where it prints the same product twice under two supplier catalogues (GS, ZSM, TSS, GP) the first code is
used. Maker names in the replacement-parts tables are left out: the models stay, matched to the original part."""
import json, os, re
from lib import table, family

CAT = 'BXC-04 Ed6'
HERE = os.path.dirname(__file__)
PAGES = json.load(open(os.path.join(HERE, 'bxc04b_pages.json')))
F = {}

U = [('(mm)', '(مم)'), ('(t/h)', '(طن/ساعة)'), ('(kW)', '(كيلوواط)'), ('(r/min)', '(دورة/دقيقة)'), ('(rpm)', '(دورة/دقيقة)'),
     ('(t)', '(طن)'), ('(m³)', '(م³)'), ('(m/s)', '(م/ث)'), ('(m³/h)', '(م³/ساعة)'), ('(µm)', '(ميكرون)'), ('(MPa)', '(ميجاباسكال)'),
     ('(t/d)', '(طن/يوم)'), ('(kg)', '(كغ)'), ('(V)', '(فولت)'), ('(/min)', '(في الدقيقة)'), ('(m²)', '(م²)'), ('(m)', '(م)'), ('(°)', '(°)')]
H = {  # column names EN → AR, without the unit (added from U)
    'Amplitude': 'السعة', 'Aperture': 'الفتحة', 'Ball load': 'حمولة الكرات', 'Belt width': 'عرض السير', 'Blower': 'المنفاخ',
    'Bucket pitch': 'خطوة الدلاء', 'Bucket width': 'عرض الدلو', 'Capacity': 'الطاقة', 'Capacity coarse': 'الطاقة – خشن',
    'Capacity fine': 'الطاقة – ناعم', 'Classifier': 'المصنّف', 'Cone': 'زاوية المخروط', 'Cut size': 'حجم الفصل', 'Cyl. Ø': 'قطر الأسطوانة',
    'Deck area': 'مساحة السطح', 'Decks': 'الطوابق', 'Diameter': 'القطر', 'Discharge': 'المخرج', 'Discharge size': 'حجم التفريغ',
    'Double amplitude': 'السعة المزدوجة', 'Drive': 'محرك الدوران', 'Drum length': 'طول الأسطوانة', 'Drum Ø': 'قطر الأسطوانة',
    'Effective volume': 'الحجم الفعّال', 'Fan': 'المروحة', 'Feed size': 'حجم التغذية', 'Frequency': 'التردد', 'Grinding media': 'وسط الطحن',
    'Inclination': 'الميل', 'Lifting': 'محرك الرفع', 'L×W×H': 'ط×ع×ا', 'Main mill': 'الطاحونة الرئيسية', 'Max feed': 'أقصى تغذية',
    'Max. feed': 'أقصى تغذية', 'Max. feed size': 'أقصى حجم تغذية', 'Max. length': 'أقصى طول', 'Max. lump size': 'أقصى حجم كتلة',
    'Motor': 'المحرك', 'Outlet W × H': 'المخرج عرض × ارتفاع', 'Overall dimensions': 'الأبعاد الكلية', 'Overall height': 'الارتفاع الكلي',
    'Overflow': 'الفيض', 'Output size': 'حجم الناتج', 'Product (µm)': 'المنتج', 'Capacity (t/h)': 'الطاقة', 'Plate width × length': 'عرض الألواح × الطول', 'Power': 'القدرة', 'Pressure': 'الضغط', 'Product': 'المنتج',
    'Product size': 'حجم المنتج', 'Ring Ø × height': 'قطر الحلقة × الارتفاع', 'Rod load': 'حمولة القضبان', 'Rollers': 'الأسطوانات',
    'Sand return': 'إرجاع الرمل', 'Screen area': 'مساحة الغربلة', 'Screen deck': 'سطح الغربال', 'Screen size': 'مقاس الغربال',
    'Shell length': 'طول الأسطوانة', 'Shell Ø': 'قطر الأسطوانة', 'Shell Ø × L': 'قطر الأسطوانة × الطول', 'Specification': 'المواصفة',
    'Speed': 'السرعة', 'Spiral speed': 'سرعة الحلزون', 'Spiral Ø': 'قطر الحلزون', 'Stroke': 'الشوط', 'Strokes': 'عدد الأشواط',
    'Swing': 'التأرجح', 'Tank length': 'طول الحوض', 'Trough size': 'مقاس الحوض', 'Tube Ø': 'قطر الأنبوب', 'Underflow': 'السفلي',
    'Vibrations': 'الاهتزازات', 'Vibrator': 'الهزّاز', 'Voltage': 'الجهد', 'W × L': 'العرض × الطول', 'Weight': 'الوزن',
    'Working angle': 'زاوية العمل', 'Models': 'الموديلات', 'Key data': 'أهم البيانات', 'Type': 'النوع', 'Grade / model': 'الدرجة / الموديل',
    'Size': 'المقاس', 'Material': 'الخامة', 'Application': 'الاستخدام', 'Items': 'القطع', 'Supply': 'التوريد', 'Construction': 'الصنع',
    'Short conveyor: length / power': 'سير قصير: الطول / القدرة', 'Medium conveyor: length / power': 'سير متوسط: الطول / القدرة',
    'Long conveyor: length / power': 'سير طويل: الطول / القدرة', 'Notes': 'ملاحظات', 'Sizes / models': 'المقاسات / الموديلات',
}


def ar_head(h):
    m = re.match(r'^(.*?)\s*(\([^)]*\))?$', h)
    name, unit = m.group(1), m.group(2)
    a = H[name]
    if unit:
        a += ' ' + dict(U).get(unit, unit)
    return a


def key(h):
    s = h.lower().replace('ø', 'dia').replace('³', '3').replace('²', '2').replace('µ', 'u').replace('°', 'deg').replace('×', 'x')
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')


def cols(headers):
    return [(key(h), h, ar_head(h)) for h in headers]


def kr(*headers):
    return [key(h) for h in headers]


def num(v):
    return [float(x.replace(',', '')) for x in re.findall(r'\d[\d,]*\.?\d*', v)]


def span(rows, i):
    """min–max over a column of numbers and ranges."""
    ns = [n for r in rows for n in num(r[i])]
    lo, hi = min(ns), max(ns)
    f = lambda n: f'{n:,.0f}' if n == int(n) and n >= 10000 else (f'{n:g}')
    return f'{f(lo)}–{f(hi)}'


TYPES = {'ar': ['نوع واحد', 'نوعان', 'أنواع'], 'en': ['type', 'types']}
PRODUCTS = {'ar': ['منتج واحد', 'منتجان', 'منتجات'], 'en': ['product', 'products']}
SERIES_U = {'ar': ['سلسلة واحدة', 'سلسلتان', 'سلاسل'], 'en': ['series', 'series']}


def auto(page, n, tid, label, key_txt, key_rows=None, intro=None, code=None, head=None, names=None, unit=None):
    t = PAGES[str(page)]['tables'][n]
    head = head or t['header']
    code = code or (t['codes'][0] if len(t['codes']) == 1 else None)
    assert code and re.fullmatch(r'BX-\d{4}-\d{2}-\d{3}', code), (page, n, t['codes'])
    for r in t['rows']:
        assert len(r) == len(head) and r[0], (page, n, r)
    nm = names or (lambda s: s)
    rows = [(None, nm(r[0]), None, *r[1:]) for r in t['rows']]
    names_ = [r[1] for r in rows]
    assert len(set(names_)) == len(names_), (page, n, 'model names repeat')
    return table(tid, label, key_txt, cols(head[1:]), rows, intro=intro, key_rows=key_rows, code=code, unit=unit)


def rows_of(page, n):
    return PAGES[str(page)]['tables'][n]['rows']


def tph(page, n, i):
    s = span(rows_of(page, n), i)
    return (f'{s} t/h', f'{s} طن/ساعة')


# =============================================================== GRINDING & CLASSIFYING (pages 21–32) ==========

# p21 wet pan mills ----------------------------------------------------------------------------------------------
F['wet-pan-mills'] = family('wet-pan-mills', CAT, [
    auto(21, 0, 'wet-pan', ('Wet pan mills', 'الطواحين الرطبة (الطاحونة الدائرية)'), ('5.5–30 kW', '5.5–30 كيلوواط'),
         kr('Specification (mm)', 'Power (kW)', 'Weight (t)')),
], type_label=('Model', 'الموديل'))

# p22 + p30 + p32 ball mills, small to medium ---------------------------------------------------------------------
F['ball-mills-small-medium'] = family('ball-mills-small-medium', CAT, [
    auto(22, 0, 'wet', ('Wet overflow ball mills', 'طواحين كروية رطبة بتفريغ الفيضان'), tph(22, 0, 2),
         kr('Capacity (t/h)', 'Discharge size (mm)', 'Power (kW)'),
         intro=('Model = shell Ø × length (m).', 'الموديل = قطر الأسطوانة × الطول (م).')),
    auto(30, 0, 'gzm', ('GZM cone ball mills', 'طواحين كروية مخروطية GZM'), tph(30, 0, 5),
         kr('Capacity (t/h)', 'Discharge size (mm)', 'Power (kW)'),
         intro=('Conical discharge end; the small sizes suit pilot plants and small gold circuits.',
                'طرف تفريغ مخروطي؛ المقاسات الصغيرة تناسب المصانع التجريبية ودوائر الذهب الصغيرة.')),
    table('wet-dry-additional', ('Ball mills, wet or dry – additional sizes', 'طواحين كروية رطبة أو جافة – مقاسات إضافية'), ('', ''),
          [('models', 'Models', 'الموديلات'), ('data', 'Key data', 'أهم البيانات')],
          [('BX-0018-05-001', 'Ball mill, wet or dry', 'طاحونة كروية رطبة أو جافة', ('2200 × 5500 and 2400 × 3000 mm', '2200 × 5500 و2400 × 3000 مم'),
            ('Series range: feed ≤ 20–25 mm; product 0.074–0.89 mm; 0.65–90 t/h; 18.5–800 kW; 18–42 r/min',
             'نطاق السلسلة: تغذية ≤ 20–25 مم؛ منتج 0.074–0.89 مم؛ 0.65–90 طن/ساعة؛ 18.5–800 كيلوواط؛ 18–42 دورة/دقيقة'))],
          unit={'ar': ['بند واحد', 'بندان', 'بنود'], 'en': ['line', 'lines']}),
], type_label=('Series', 'السلسلة'))

# p23 + p30 ball mills, large -------------------------------------------------------------------------------------
F['ball-mills-large'] = family('ball-mills-large', CAT, [
    auto(23, 0, 'mqs', ('MQS wet grate-discharge ball mills', 'طواحين كروية رطبة بتفريغ شبكي MQS'), ('60–5800 kW', '60–5800 كيلوواط'),
         kr('Shell Ø (mm)', 'Effective volume (m³)', 'Power (kW)')),
    auto(23, 1, 'mqy', ('MQY overflow ball mills', 'طواحين كروية بتفريغ الفيضان MQY'), ('55–6000 kW', '55–6000 كيلوواط'),
         kr('Shell Ø (mm)', 'Effective volume (m³)', 'Power (kW)')),
    auto(30, 1, 'mqg', ('MQG grate-discharge ball mills – additional sizes', 'طواحين كروية بتفريغ شبكي MQG – مقاسات إضافية'), tph(30, 1, 5),
         kr('Capacity (t/h)', 'Discharge size (mm)', 'Power (kW)')),
], type_label=('Series', 'السلسلة'))

# p24 + p31 rod mills ---------------------------------------------------------------------------------------------
F['rod-mills'] = family('rod-mills', CAT, [
    auto(24, 0, 'mb', ('MB wet overflow rod mills', 'طواحين قضبان رطبة بتفريغ الفيضان MB'), tph(24, 0, 4),
         kr('Output size (mm)', 'Capacity (t/h)', 'Power (kW)'),
         intro=('Rod mills give an even product with little over-grinding, often as the first grinding stage.',
                'تعطي طواحين القضبان منتجاً متجانساً بقليل من الطحن الزائد، وكثيراً ما تكون مرحلة الطحن الأولى.')),
    auto(31, 0, 'mb-additional', ('MB rod mills – additional sizes', 'طواحين قضبان MB – مقاسات إضافية'), ('22–245 kW', '22–245 كيلوواط'),
         kr('Shell Ø × L (mm)', 'Rod load (t)', 'Power (kW)')),
], type_label=('Series', 'السلسلة'))

# p25 + p31 spiral classifiers ------------------------------------------------------------------------------------
FG = ['Model', 'Spiral Ø (mm)', 'Tank length (mm)', 'Spiral speed (r/min)', 'Sand return (t/d)', 'Overflow (t/d)', 'Drive (kW)', 'Lifting (kW)', 'Weight (t)']
F['spiral-classifiers'] = family('spiral-classifiers', CAT, [
    auto(25, 0, 'fg-fc', ('FG / FC spiral classifiers (single and double spiral)', 'مصنّفات حلزونية FG / FC (حلزون مفرد ومزدوج)'),
         ('Sand return 340–23,300 t/d', 'إرجاع الرمل 340–23,300 طن/يوم'), kr('Spiral Ø (mm)', 'Sand return (t/d)', 'Drive (kW)'), head=FG,
         intro=('FG = high weir, FC = submerged spiral; the 2 prefix means a double spiral.',
                'FG بفائض مرتفع وFC بحلزون مغمور؛ والرقم 2 في أول الموديل يعني حلزوناً مزدوجاً.')),
    table('flg', ('FLG-5 high-weir spiral classifier – additional size', 'مصنّف حلزوني بفائض مرتفع FLG-5 – مقاس إضافي'), ('1.1 kW', '1.1 كيلوواط'),
          cols(FG[1:]), [(None, 'FLG-5', None, '500', '4500', '8.5–15.5', '143–261', None, '1.1', None, '1.6')],
          intro=('Tank 4500 × 555 mm.', 'الحوض 4500 × 555 مم.'), code='BX-0033-01-015'),
], type_label=('Series', 'السلسلة'))

# p26 powder grinding mills ---------------------------------------------------------------------------------------
F['powder-grinding-mills'] = family('powder-grinding-mills', CAT, [
    auto(26, 0, 'ygm', ('YGM high-pressure grinding mills', 'طواحين طحن عالية الضغط YGM'), ('1–36 t/h', '1–36 طن/ساعة'),
         kr('Capacity (t/h)', 'Main mill (kW)', 'Blower (kW)'),
         intro=('Capacity at 200 mesh fineness.', 'الطاقة عند نعومة 200 مش.')),
    auto(26, 1, 'mtw', ('MTW trapezium grinding mills', 'طواحين شبه منحرفة MTW'), ('3–50 t/h', '3–50 طن/ساعة'),
         kr('Product size (mm)', 'Capacity (t/h)', 'Main mill (kW)')),
    auto(26, 2, 'hgm', ('HGM micro-powder mills (three-ring)', 'طواحين المساحيق الدقيقة HGM (ثلاثية الحلقات)'), ('0.5–20.5 t/h', '0.5–20.5 طن/ساعة'),
         kr('Product (µm)', 'Capacity (t/h)', 'Main mill (kW)'),
         intro=('Product fineness 150–3000 mesh (HGM1250: 150–2500 mesh).', 'نعومة المنتج 150–3000 مش (HGM1250: ‏150–2500 مش).')),
], type_label=('Series', 'السلسلة'))

# p27 SAG and AG mills (no model table in the catalogue: types and liners, one code) -------------------------------
F['sag-autogenous-mills'] = family('sag-autogenous-mills', CAT, [
    table('types', ('Mill types and liners', 'أنواع الطواحين والبطانات'), ('Sized to the plant duty', 'حسب طاقة المصنع'),
          [('use', 'Use', 'الاستخدام'), ('supply', 'Supply', 'التوريد')],
          [(None, 'SAG mill (semi-autogenous)', 'طاحونة شبه ذاتية (SAG)',
            ('Primary grinding of run-of-mine or crushed ore in one stage, with a small ball charge', 'طحن أولي لخام المنجم أو الخام المكسّر في مرحلة واحدة، مع شحنة كرات صغيرة'),
            ('Mill size, drive and liners selected to the ore and plant tonnage', 'مقاس الطاحونة ونظام الدفع والبطانات حسب الخام وطاقة المصنع')),
           (None, 'AG mill (autogenous)', 'طاحونة ذاتية (AG)',
            ('Primary grinding with the ore as its own grinding media', 'طحن أولي يكون فيه الخام نفسه وسط الطحن'),
            ('Mill size, drive and liners selected to the ore and plant tonnage', 'مقاس الطاحونة ونظام الدفع والبطانات حسب الخام وطاقة المصنع')),
           (None, 'Mill liners', 'بطانات الطاحونة',
            ('Shell, end and grid (discharge) liners', 'بطانات الجسم والنهاية والشبكة (التفريغ)'),
            ('With the mill and as spares; shells, heads and trunnions fabricated', 'مع الطاحونة وكقطع غيار؛ وتصنيع الأسطوانات والرؤوس والمحاور'))],
          intro=('Mill sizes and capacities are quoted per project: send the ore data and plant tonnage with the enquiry.',
                 'تُسعَّر مقاسات الطواحين وطاقاتها لكل مشروع: أرسل بيانات الخام وطاقة المصنع مع الطلب.'),
          code='BX-0034-01-004', unit={'ar': ['بند واحد', 'بندان', 'بنود'], 'en': ['line', 'lines']}),
], type_label=('Type', 'النوع'))

# p28 + p31 hydrocyclones -----------------------------------------------------------------------------------------
FX = ['Model', 'Cyl. Ø (mm)', 'Cone (°)', 'Overflow (mm)', 'Underflow (mm)', 'Max feed (mm)', 'Pressure (MPa)', 'Capacity (m³/h)', 'Cut size (µm)', 'L×W×H (mm)', 'Weight (kg)']
F['hydrocyclones'] = family('hydrocyclones', CAT, [
    table('fx', ('FX hydrocyclones', 'هيدروسيكلونات FX'), ('11–350 m³/h', '11–350 م³/ساعة'), cols(FX[1:]),
          [(None, f'{r[0]} · {r[2]}°', None, *r[1:]) for r in rows_of(28, 0)],
          intro=('The same cylinder is offered with different cone angles: a smaller angle gives a finer cut.',
                 'تُورَّد الأسطوانة نفسها بزوايا مخروط مختلفة: الزاوية الأصغر تعطي فصلاً أنعم.'),
          code='BX-0028-01-020', key_rows=kr('Capacity (m³/h)', 'Cut size (µm)', 'Pressure (MPa)')),
    table('fx-small', ('FX small hydrocyclones – additional sizes', 'هيدروسيكلونات FX صغيرة – مقاسات إضافية'), ('5–15 m³/h', '5–15 م³/ساعة'),
          cols(['Cyl. Ø (mm)', 'Pressure (MPa)', 'Capacity (m³/h)', 'Cut size (µm)']),
          [(None, 'FX-125', None, '125', '0.05–0.4', '8–15', '20–100'), (None, 'FX-100', None, '100', '0.05–0.4', '5–12', '10–100')],
          code='BX-0033-01-016'),
], type_label=('Series', 'السلسلة'))
assert len(set(m['code'] for m in F['hydrocyclones']['types'][0]['models'])) == 20

# p29 + p32 ceramic grinding media --------------------------------------------------------------------------------
MEDIA = [('grade', 'Grade / model', 'الدرجة / الموديل'), ('size', 'Size (mm)', 'المقاس (مم)'), ('data', 'Key data', 'أهم البيانات')]
F['ceramic-grinding-media'] = family('ceramic-grinding-media', CAT, [
    table('media', ('Ceramic grinding media', 'كرات الطحن الخزفية'), ('0.5–80 mm', '0.5–80 مم'), MEDIA,
          [('BX-0174-01-001', 'Alumina grinding balls', 'كرات طحن ألومينا', ('60, 75, 92 or 99 % Al2O3', 'ألومينا 60 أو 75 أو 92 أو 99%'),
            ('0.5–30 (92 % to 70)', '0.5–30 (92% حتى 70)'), ('Density ≥ 2.8–3.8 g/cm³; hardness ≥ 7–14 GPa', 'الكثافة ≥ 2.8–3.8 غ/سم³؛ الصلادة ≥ 7–14 جيجاباسكال')),
           ('BX-0174-01-002', 'ZTA grinding media', 'وسط طحن ZTA', ('Zirconia-toughened alumina', 'ألومينا مقوّاة بالزركونيا'), '1–30',
            ('Density ≥ 3.7–5.0 g/cm³', 'الكثافة ≥ 3.7–5.0 غ/سم³')),
           ('BX-0174-01-005', 'Balls for horizontal stirred mills', 'كرات للطواحين الأفقية ذات التقليب', 'HCTA370A · HCTA450', '3 · 3.5 · 5',
            ('Density 3.75 / 4.45 g/cm³', 'الكثافة 3.75 / 4.45 غ/سم³')),
           ('BX-0174-01-006', 'Balls for tower (vertical) mills', 'كرات للطواحين البرجية (الرأسية)', 'HCTA370 · HCTA450', '5–20',
            ('Self-wear ≤ 0.03 g/kg·h', 'التآكل الذاتي ≤ 0.03 غ/كغ·ساعة')),
           ('BX-0174-01-007', 'Balls for ball mills (regrind)', 'كرات للطواحين الكروية (إعادة الطحن)', 'HCGA360 · HCTA450', '20 · 25 · 30 · 35',
            ('Density 3.7 / 4.5 g/cm³; self-wear ≤ 0.025–0.03 g/kg·h', 'الكثافة 3.7 / 4.5 غ/سم³؛ التآكل الذاتي ≤ 0.025–0.03 غ/كغ·ساعة')),
           ('BX-0629-01-001', '92 % alumina balls – larger sizes', 'كرات ألومينا 92% – مقاسات أكبر', ('92 % Al2O3', 'ألومينا 92%'), '30–80',
            ('High-alumina ceramic', 'خزف عالي الألومينا'))],
          intro=('Iron-free media for fine grinding and regrinding; size and grade are selected to the mill and the target grind.',
                 'وسط طحن خالٍ من الحديد للطحن الناعم وإعادة الطحن؛ يُختار المقاس والدرجة حسب الطاحونة ونعومة الطحن المطلوبة.'),
          key_rows=['grade', 'size', 'data'], unit=TYPES),
], type_label=('Media type', 'نوع الوسط'))

# ================================================== FEEDING, SCREENING & CONVEYING (pages 33–48) ================

# p33 + p36 + p44 vibrating feeders ------------------------------------------------------------------------------------
F['vibrating-feeders'] = family('vibrating-feeders', CAT, [
    auto(33, 0, 'mvf', ('MVF vibrating grizzly feeders', 'مغذيات اهتزازية بقضبان MVF'), ('450–1800 t/h', '450–1800 طن/ساعة'),
         kr('Capacity (t/h)', 'Max. feed size (mm)', 'Power (kW)')),
    auto(33, 1, 'gzd-zsw', ('GZD / ZSW vibrating feeders', 'مغذيات اهتزازية GZD / ZSW'), tph(33, 1, 4),
         kr('Capacity (t/h)', 'Max. feed size (mm)', 'Motor (kW)')),
    table('gzd-large', ('GZD vibrating feeders – larger sizes', 'مغذيات اهتزازية GZD – مقاسات أكبر'), ('20–1400 t/h', '20–1400 طن/ساعة'),
          [('models', 'Models', 'الموديلات'), ('capacity-t-h', 'Capacity (t/h)', 'الطاقة (طن/ساعة)'), ('max-feed-size-mm', 'Max. feed size (mm)', 'أقصى حجم تغذية (مم)'),
           ('power-kw', 'Power (kW)', 'القدرة (كيلوواط)')],
          [('BX-0018-03-017', 'GZD vibrating feeder', 'مغذٍّ اهتزازي GZD', ('GZD-900×2000 to GZD-1600×6000 (10 sizes)', 'من GZD-900×2000 إلى GZD-1600×6000 (10 مقاسات)'),
            '20–1400', '300–900', '5.5–37')],
          intro=('For primary crushing stations.', 'لمحطات التكسير الأولي.'), unit=SERIES_U),
    auto(44, 1, 'gzt', ('GZT grizzly vibrating feeders', 'مغذيات اهتزازية بقضبان GZT'), ('30–600 t/h', '30–600 طن/ساعة'),
         kr('Capacity (t/h)', 'Max. feed size (mm)', 'Power (kW)')),
    auto(33, 2, 'gz', ('GZ electromagnetic vibrating feeders', 'مغذيات اهتزازية كهرومغناطيسية GZ'), ('5–100 t/h', '5–100 طن/ساعة'),
         kr('Capacity (t/h)', 'Max. feed size (mm)', 'Power (kW)'),
         intro=('For a steady, adjustable mill feed.', 'لتغذية ثابتة وقابلة للضبط إلى الطاحونة.')),
], type_label=('Series', 'السلسلة'))

# p34 + p44 apron, box and pendulum feeders --------------------------------------------------------------------------
F['apron-reciprocating-feeders'] = family('apron-reciprocating-feeders', CAT, [
    auto(34, 0, 'gbz', ('GBZ heavy-duty apron feeders', 'مغذيات صفائحية ثقيلة GBZ'), ('16.6–1900 m³/h', '16.6–1900 م³/ساعة'),
         kr('Plate width × length (mm)', 'Capacity (m³/h)', 'Motor (kW)'),
         intro=('For sticky or large run-of-mine ore under the primary hopper.', 'لخام المنجم اللزج أو الكبير تحت قادوس التكسير الأولي.')),
    auto(34, 1, 'box', ('Box-type (reciprocating) feeders', 'مغذيات صندوقية (ترددية)'), ('2.5–50 t/h', '2.5–50 طن/ساعة'),
         kr('Feed size (mm)', 'Capacity (t/h)', 'Motor (kW)')),
    auto(44, 0, 'pendulum', ('Pendulum feeders for small mills', 'مغذيات بندولية للطواحين الصغيرة'), ('4.5–25 t/h', '4.5–25 طن/ساعة'),
         kr('Feed size (mm)', 'Capacity (t/h)', 'Power (kW)'),
         intro=('Meter crushed ore into small ball mills.', 'تُدخل الخام المكسّر بمعدل منتظم إلى الطواحين الكروية الصغيرة.')),
], type_label=('Series', 'السلسلة'))

# p35 + p36 + p43 circular-motion vibrating screens -----------------------------------------------------------------------
F['inclined-vibrating-screens'] = family('inclined-vibrating-screens', CAT, [
    auto(35, 0, 'mya', ('MYA inclined vibrating screens (1–4 decks)', 'غرابيل اهتزازية مائلة MYA (1–4 طوابق)'), ('120–1360 t/h', '120–1360 طن/ساعة'),
         kr('Deck area (mm)', 'Capacity (t/h)', 'Power (kW)'),
         intro=('(2/3/4) before the model = number of decks.', 'الرقم (2/3/4) قبل الموديل = عدد الطوابق.')),
    auto(35, 1, 'yk', ('YK circular vibrating screens', 'غرابيل دائرية اهتزازية YK'), ('30–720 t/h', '30–720 طن/ساعة'),
         kr('Screen size (mm)', 'Capacity (t/h)', 'Power (kW)')),
    auto(43, 1, 'yk-additional', ('YK circular vibrating screens – additional sizes', 'غرابيل دائرية اهتزازية YK – مقاسات إضافية'), ('1–4 decks', '1–4 طوابق'),
         kr('Decks', 'Screen area (m²)', 'Power (kW)'), code='BX-0033-01-028', unit=SERIES_U,
         intro=('Max. feed 200–400 mm.', 'أقصى تغذية 200–400 مم.')),
    table('yzs', ('YZS circular vibrating screens', 'غرابيل دائرية اهتزازية YZS'), ('25–2250 t/h', '25–2250 طن/ساعة'),
          [('models', 'Models', 'الموديلات'), ('capacity-t-h', 'Capacity (t/h)', 'الطاقة (طن/ساعة)'), ('max-feed-size-mm', 'Max. feed size (mm)', 'أقصى حجم تغذية (مم)'),
           ('power-kw', 'Power (kW)', 'القدرة (كيلوواط)'), ('decks', 'Decks', 'الطوابق')],
          [('BX-0018-03-014', 'YZS circular vibrating screen', 'غربال دائري اهتزازي YZS', ('2YZS, 3YZS and 4YZS, 1237 to 3680 (22 models)', '2YZS و3YZS و4YZS، من 1237 إلى 3680 (22 موديلاً)'),
            '25–2250', '300–400', ('11 to 2 × 37', 'من 11 إلى 2 × 37'), '2–4')], unit=SERIES_U),
    auto(43, 0, 'szz', ('SZZ self-centering vibrating screens (single or double deck)', 'غرابيل اهتزازية ذاتية التمركز SZZ (طابق أو طابقان)'), ('20–245 t/h', '20–245 طن/ساعة'),
         kr('Screen area (m²)', 'Capacity (t/h)', 'Power (kW)'),
         intro=('SZZ(2) and SZZ2… = double deck; hanging or seat mounting.', 'SZZ(2) وSZZ2… = طابقان؛ تركيب معلّق أو على قاعدة.')),
], type_label=('Series', 'السلسلة'))

# p37 horizontal and linear screens --------------------------------------------------------------------------------
F['horizontal-linear-screens'] = family('horizontal-linear-screens', CAT, [
    auto(37, 0, 'mfs', ('MFS horizontal screens', 'غرابيل أفقية MFS'), ('300–800 t/h', '300–800 طن/ساعة'),
         kr('W × L (mm)', 'Capacity (t/h)', 'Power (kW)'),
         intro=('Low-profile screens for mobile and modular plants; -2 / -3 = two or three decks.', 'غرابيل منخفضة الارتفاع للمحطات المتنقلة والمعيارية؛ ‎-2 / ‎-3 = طابقان أو ثلاثة.')),
    auto(37, 1, 'szf', ('SZF linear vibrating screens', 'غرابيل اهتزازية خطية SZF'), ('1–35 t/h', '1–35 طن/ساعة'),
         kr('Screen size (mm)', 'Capacity (t/h)', 'Power (kW)'),
         intro=('Light screens for fine sizing, 1 to 6 decks.', 'غرابيل خفيفة للتصنيف الناعم، من طابق إلى 6 طوابق.')),
], type_label=('Series', 'السلسلة'))

# p38 + p43 trommels and ZSD dewatering screens ------------------------------------------------------------------------
F['trommel-dewatering-screens'] = family('trommel-dewatering-screens', CAT, [
    auto(38, 0, 'gt', ('GT trommel screens', 'غرابيل أسطوانية GT'), ('10–600 t/h', '10–600 طن/ساعة'),
         kr('Drum Ø (mm)', 'Capacity (t/h)', 'Power (kW)'),
         intro=('Drum length can be made to order.', 'يمكن تصنيع طول الأسطوانة حسب الطلب.')),
    auto(38, 2, 'gs', ('GS trommel screens', 'غرابيل أسطوانية GS'), ('8–230 t/h', '8–230 طن/ساعة'),
         kr('Capacity coarse (t/h)', 'Capacity fine (t/h)', 'Power (kW)'), code='BX-0021-01-020'),
    auto(38, 1, 'zsd', ('ZSD dewatering screens', 'غرابيل نزع الماء ZSD'), ('30–250 t/h', '30–250 طن/ساعة'),
         kr('Capacity (t/h)', 'Screen area (m²)', 'Power (kW)')),
    auto(43, 2, 'zsd-additional', ('ZSD dewatering screens – additional sizes (polyurethane deck)', 'غرابيل نزع الماء ZSD – مقاسات إضافية (سطح بولي يوريثان)'),
         ('30–180 t/h', '30–180 طن/ساعة'), kr('Capacity (t/h)', 'Screen area (m²)', 'Power (kW)')),
], type_label=('Series', 'السلسلة'))

# p39 linear and high-frequency dewatering screens ----------------------------------------------------------------------
F['linear-high-frequency-dewatering-screens'] = family('linear-high-frequency-dewatering-screens', CAT, [
    auto(39, 0, 'zsm', ('ZSM linear dewatering screens', 'غرابيل نزع ماء خطية ZSM'), ('7.2–420 t/h', '7.2–420 طن/ساعة'),
         kr('Screen area (m²)', 'Capacity (t/h)', 'Power (kW)'), code='BX-0021-01-022',
         intro=('The 2 prefix means a double deck.', 'الرقم 2 في أول الموديل يعني طابقين.')),
    auto(39, 1, 'tss', ('TSS high-frequency dewatering screens', 'غرابيل نزع ماء عالية التردد TSS'), ('15–100 t/h', '15–100 طن/ساعة'),
         kr('Aperture (mm)', 'Capacity (t/h)', 'Power (kW)'), code='BX-0021-01-023',
         intro=('For fine material ≤ 10 mm; /2 = two decks.', 'للمواد الناعمة ≤ 10 مم؛ ‎/2 = طابقان.')),
    auto(39, 2, 'gp', ('GP tailings dewatering screens', 'غرابيل نزع ماء المخلفات GP'), ('15–100 t/h', '15–100 طن/ساعة'),
         kr('Aperture (mm)', 'Capacity (t/h)', 'Power (kW)'), code='BX-0021-01-024',
         intro=('Supplied with a slurry pump and hydrocyclones.', 'تُورَّد مع مضخة لب وهيدروسيكلونات.')),
], type_label=('Series', 'السلسلة'))

# p40 conveyors and elevators --------------------------------------------------------------------------------------------
BELT = ['Belt width', 'Short conveyor: length / power', 'Medium conveyor: length / power', 'Long conveyor: length / power', 'Speed (m/s)', 'Capacity (t/h)']
F['conveyors-elevators'] = family('conveyors-elevators', CAT, [
    auto(40, 0, 'belt', ('B belt conveyors', 'سيور ناقلة B'), ('40–500 t/h', '40–500 طن/ساعة'),
         kr('Capacity (t/h)', 'Speed (m/s)', 'Short conveyor: length / power'), head=BELT,
         intro=('Length in metres / motor power in kW for each conveyor length; B = belt width in mm.',
                'الطول بالمتر / قدرة المحرك بالكيلوواط لكل طول سير؛ B = عرض السير بالملّيمتر.')),
    auto(40, 1, 'th', ('TH bucket elevators', 'روافع دلوية TH'), ('15–118 m³/h', '15–118 م³/ساعة'),
         kr('Bucket width (mm)', 'Max. lump size (mm)', 'Capacity (m³/h)'),
         intro=('H = lifting height.', 'H = ارتفاع الرفع.')),
    auto(40, 2, 'lsy', ('LSY screw conveyors', 'ناقلات حلزونية LSY'), ('3–100 m³/h', '3–100 م³/ساعة'),
         kr('Tube Ø (mm)', 'Capacity (m³/h)', 'Motor (kW)')),
], type_label=('Series', 'السلسلة'))

# p41 + p47 screen mesh --------------------------------------------------------------------------------------------------
MESH = [('material', 'Material', 'الخامة'), ('data', 'Key data', 'أهم البيانات')]
F['screen-mesh'] = family('screen-mesh', CAT, [
    table('woven', ('Woven and crimped screen mesh', 'شبك الغربلة المنسوج والمجعّد'), ('Aperture 1–150 mm', 'فتحة 1–150 مم'), MESH,
          [('BX-0233-02-001', 'Heavy-duty crimped wire mesh', 'شبك سلكي مجعّد ثقيل', ('High-tensile, 45# or 65Mn steel', 'فولاذ عالي الشد 45# أو 65Mn'),
            ('Wire 1.5–12.8 mm (to 22 mm); aperture 2–110 mm (to 150 mm); width 0.5–4 m, length to 30 m; plain, raw, hooked or plate-hooked edges',
             'سلك 1.5–12.8 مم (حتى 22 مم)؛ فتحة 2–110 مم (حتى 150 مم)؛ عرض 0.5–4 م وطول حتى 30 م؛ حواف عادية أو خام أو بخطاف أو بخطاف ولوح')),
           ('BX-0233-02-002', 'Crimped vibrating-screen mesh', 'شبك مجعّد للغرابيل الاهتزازية', ('65Mn, single- or double-wire crimp', '65Mn، تجعيد بسلك مفرد أو مزدوج'),
            ('Wire 0.5–12.7 mm; aperture 1–120 mm; panels to size; double-chute slotted screen in high-tensile, wear-resistant steel',
             'سلك 0.5–12.7 مم؛ فتحة 1–120 مم؛ ألواح حسب المقاس؛ وغربال مشقوق بمجريين من فولاذ عالي الشد مقاوم للتآكل')),
           ('BX-0233-02-003', 'Woven manganese-steel mesh', 'شبك منسوج من فولاذ المنغنيز', '65Mn',
            ('For vibrating screens, trommels, crushers and quarries', 'للغرابيل الاهتزازية والأسطوانية والكسارات والمحاجر'))],
          intro=('Square or rectangular openings; double, intermediate, flat-top or lock crimp; made to the screen deck size.',
                 'فتحات مربعة أو مستطيلة؛ تجعيد مزدوج أو متوسط أو مسطح السطح أو مقفل؛ حسب مقاس سطح الغربال.'),
          key_rows=['material', 'data'], unit=PRODUCTS),
    table('additional', ('Plate, wedge-wire and fine mesh – additional types', 'ألواح مثقبة وشبك وتدي وشبك ناعم – أنواع إضافية'), ('2–635 mesh', '2–635 مش'),
          [('sizes', 'Sizes / models', 'المقاسات / الموديلات'), ('data', 'Key data', 'أهم البيانات')],
          [('BX-0309-01-010', 'Heavy perforated plate', 'ألواح مثقبة ثقيلة',
            ('Round holes 0.4–120 mm, rectangular 1×20–30×65 mm, square 3×3–150×150 mm, hexagonal 8–65 mm', 'ثقوب دائرية 0.4–120 مم، ومستطيلة 1×20–30×65 مم، ومربعة 3×3–150×150 مم، وسداسية 8–65 مم'),
            ('0.5–15 mm thick; mild, manganese or stainless steel, non-ferrous or plastic; sized to the machine', 'سماكة 0.5–15 مم؛ فولاذ طري أو منغنيز أو ستانلس أو معادن غير حديدية أو بلاستيك؛ حسب مقاس الآلة')),
           ('BX-0309-01-005', 'Polyurethane cross-band and poly woven-wire modular panels', 'ألواح بولي يوريثان معيارية بأشرطة عرضية وبسلك منسوج مغلّف',
            ("1'×1', 1'×2', 2'×2'; ripple, harp, wavy and piano patterns", "‏1'×1' و1'×2' و2'×2'؛ أنماط متموجة وقيثارية ومتعرجة وبيانو"),
            ('80 Shore polyurethane; up to 100 % more open area than PU or rubber panels; self-cleaning', 'بولي يوريثان بصلادة 80 شور؛ مساحة مفتوحة أكبر حتى 100% من ألواح البولي يوريثان أو المطاط؛ ذاتية التنظيف')),
           ('BX-0309-01-006', 'Polyurethane screen panels', 'ألواح غربلة بولي يوريثان', ('Square and rectangular tapered openings', 'فتحات مربعة ومستطيلة مستدقة'),
            ('45–90 Shore A; tensile 31–56 MPa; density 1.20–1.22', 'صلادة 45–90 شور A؛ مقاومة شد 31–56 ميجاباسكال؛ كثافة 1.20–1.22')),
           ('BX-0689-01-007', 'Wedge-wire sieving screen', 'غربال من السلك الوتدي', ('Slots 0.1–20 mm; square openings 6×6–30×30 mm', 'شقوق 0.1–20 مم؛ فتحات مربعة 6×6–30×30 مم'),
            ('Wedge wire 1.6–3.5 mm on 4 mm support rods; made to size', 'سلك وتدي 1.6–3.5 مم على قضبان دعم 4 مم؛ حسب المقاس')),
           ('BX-0309-01-012', 'Wedge-wire screen tubes and panels', 'أنابيب وألواح غربلة من السلك الوتدي', ('Slot from 0.02 mm; Ø 100–630 mm; up to 6000 mm long', 'شق من 0.02 مم؛ قطر 100–630 مم؛ طول حتى 6000 مم'),
            ('AISI 304 / 316 and other grades; for screening and dewatering', 'ستانلس AISI 304 / 316 ودرجات أخرى؛ للغربلة ونزع الماء')),
           ('BX-0689-01-009', 'Stainless steel wire mesh, fine', 'شبك ستانلس ناعم', ('2–635 mesh; wire 1.8–0.0203 mm; opening 10.9–0.0203 mm', '2–635 مش؛ سلك 1.8–0.0203 مم؛ فتحة 10.9–0.0203 مم'),
            ('SS 201 / 202 / 304 / 316 / 316L; plain, twill and Dutch weave', 'ستانلس 201 / 202 / 304 / 316 / 316L؛ نسج سادة ومبرد وهولندي')),
           ('BX-0701-01-003', 'Stainless steel wire mesh', 'شبك ستانلس', ('2–100 mesh; SUS 302 / 304 / 316 / 304L / 316L; heavy 14 gauge with 3/4 in opening', '2–100 مش؛ ستانلس 302 / 304 / 316 / 304L / 316L؛ ثقيل بمقاس 14 وفتحة 3/4 بوصة'),
            ('Plain, twill and Dutch weave for sizing and filtering', 'نسج سادة ومبرد وهولندي للتصنيف والترشيح')),
           ('BX-0309-01-011', 'Stainless steel woven mesh, heavy wire', 'شبك ستانلس منسوج بسلك ثقيل', ('304 and 316; plain, twill and Dutch', '304 و316؛ سادة ومبرد وهولندي'),
            ('Wire Ø 0.63–9.5 mm; supplied in rolls', 'قطر السلك 0.63–9.5 مم؛ يُورَّد في لفات'))],
          key_rows=['sizes', 'data'], unit=PRODUCTS),
], type_label=('Product', 'المنتج'))

# p42 + p46 conveyor rollers, belts and cleaners ---------------------------------------------------------------------------
TYP = [('types', 'Types / models', 'الأنواع / الموديلات'), ('data', 'Key data', 'أهم البيانات')]
F['conveyor-rollers-belts-cleaners'] = family('conveyor-rollers-belts-cleaners', CAT, [
    table('rollers-belts', ('Conveyor rollers and belts', 'رولات السيور والسيور الناقلة'), ('Belts 300–2200 mm', 'سيور 300–2200 مم'), TYP,
          [('BX-0062-01-004', 'UHMW-PE rollers', 'رولات UHMW-PE', ('Standard, low-noise, impact, disc, spiral, self-aligning, tapered, crowned, guide', 'قياسية، ومنخفضة الضجيج، وللصدمات، وقرصية، وحلزونية، وذاتية الاستقامة، ومخروطية، ومحدّبة، وتوجيه'),
            ('Ø 63.5–219 mm or to order', 'قطر 63.5–219 مم أو حسب الطلب')),
           ('BX-0062-01-002', 'Mining roller', 'رول للمناجم', ('Fire-resistant, anti-static', 'مقاوم للحريق ومانع للكهرباء الساكنة'),
            ('Sealed against water and dust; TIR ≤ 0.2 mm; axial load > 15 kN; noise ≤ 45 dB', 'محكم ضد الماء والغبار؛ انحراف دوراني ≤ 0.2 مم؛ حمل محوري > 15 كيلونيوتن؛ ضجيج ≤ 45 ديسيبل')),
           ('BX-0062-02-001', 'Fabric conveyor belt', 'سير ناقل بقلب نسيجي', 'EP100–EP600 · NN100–NN600 · CC56',
            ('2–8 plies (CC 3–12); width 300–2200 mm; covers 1.5–30 / 0–20 mm; DIN 22102, AS 1332', '2–8 طبقات (CC من 3 إلى 12)؛ عرض 300–2200 مم؛ غطاء 1.5–30 / 0–20 مم؛ DIN 22102 وAS 1332')),
           ('BX-0062-02-002', 'Chevron belt', 'سير شيفرون', ('Open-V, closed-V and other patterns', 'نقش V مفتوح وV مغلق وأنماط أخرى'),
            ('Inclines up to 40°; width up to 1200 mm', 'ميل حتى 40°؛ عرض حتى 1200 مم'))],
          key_rows=['types', 'data'], unit=PRODUCTS),
    table('cleaners', ('Belt cleaners and loading-zone parts', 'منظفات السيور وقطع منطقة التحميل'), ('Belts 650–2200 mm', 'سيور 650–2200 مم'), TYP,
          [('BX-0062-03-001', 'Primary cleaner, PU blade', 'منظف أولي بشفرة بولي يوريثان', 'H · HR · HN', ('Belt 650–2200 mm', 'سير 650–2200 مم')),
           ('BX-0062-03-002', 'Secondary cleaner, PU blade', 'منظف ثانوي بشفرة بولي يوريثان', 'P · PR · PN', ('Belt 650–2200 mm', 'سير 650–2200 مم')),
           ('BX-0062-03-003', 'Primary cleaner, carbide tip', 'منظف أولي برأس كربيد', 'H-TD · HN-TD', ('Alloy-steel blade with tungsten-carbide tip', 'شفرة فولاذ سبائكي برأس كربيد التنغستن')),
           ('BX-0062-03-004', 'Secondary cleaner, carbide tip', 'منظف ثانوي برأس كربيد', 'P-TD · PN-TD · N-TD · PM', ('Belt 650–2200 mm', 'سير 650–2200 مم')),
           ('BX-0062-03-005', 'Heavy-duty primary cleaner', 'منظف أولي للخدمة الشاقة', 'HZ', ('PU blade 600–2100 mm', 'شفرة بولي يوريثان 600–2100 مم')),
           ('BX-0062-03-006', 'Return-belt V-plough', 'محراث V للسير الراجع', 'V', ('PU blade, alloy-steel frame', 'شفرة بولي يوريثان وإطار فولاذ سبائكي')),
           ('BX-0062-03-010', 'Impact bed and impact bars', 'سرير وقضبان امتصاص الصدمات', 'C · C-T',
            ('Rubber + UHMW-PE bars on a steel cradle; bars 100 mm wide, 50 / 65 / 75 mm high', 'قضبان مطاط وUHMW-PE على مهد فولاذي؛ عرض القضبان 100 مم وارتفاعها 50 / 65 / 75 مم')),
           ('BX-0062-03-012', 'Skirting', 'جوانب منع التسرب', 'B', ('Rubber or polyurethane, sizes to order', 'مطاط أو بولي يوريثان، المقاسات حسب الطلب'))],
          key_rows=['types', 'data'], unit=PRODUCTS),
    table('belts-additional', ('Conveyor belts – additional series', 'السيور الناقلة – سلاسل إضافية'), ('Up to ST7500', 'حتى ST7500'), TYP,
          [('BX-0271-02-001', 'Steel-cord belt ST and flame-retardant wire-rope belt GX', 'سير بقلب حبال فولاذية ST وسير GX مقاوم للهب', 'ST630–ST5400 · GX630–GX4000',
            ('Widths 800–2000 mm', 'عروض 800–2000 مم')),
           ('BX-0717-01-001', 'Steel-cord belt (GB/T 9770, DIN 22131)', 'سير بقلب حبال فولاذية (GB/T 9770 وDIN 22131)', 'ST630–ST7500 (16 grades)',
            ('630–7500 N/mm; cord Ø 3.0–15.0 mm; covers 5–10 mm; width 800–2200 mm; standard, fire-, heat-, abrasion-, oil- and cold-resistant covers',
             '630–7500 نيوتن/مم؛ قطر الحبل 3.0–15.0 مم؛ غطاء 5–10 مم؛ عرض 800–2200 مم؛ أغطية قياسية ومقاومة للحريق والحرارة والتآكل والزيت والبرد')),
           ('BX-0684-01-001', 'Multi-ply EP belt, high strength', 'سير EP متعدد الطبقات عالي المتانة', 'EP400/3 … EP1250/5, EP1200/6',
            ('Width 500–2500 mm; covers 3+1.5 to 5+1.5 mm (DIN X/Y/W, RMA-1/2, N17/M24); lengths 10–500 m', 'عرض 500–2500 مم؛ غطاء من 3+1.5 إلى 5+1.5 مم (DIN X/Y/W وRMA-1/2 وN17/M24)؛ أطوال 10–500 م')),
           ('BX-0684-01-002', 'Flame-retardant belt', 'سير مقاوم للهب', ('EP with fire-resistant (EN/ISO 340) and anti-static (EN/ISO 20284) covers', 'EP بأغطية مقاومة للحريق (EN/ISO 340) ومانعة للكهرباء الساكنة (EN/ISO 20284)'),
            ('No flame in the drum test up to 325 °C; self-extinguishes within 10 s', 'لا لهب في اختبار الأسطوانة حتى 325°م؛ ينطفئ ذاتياً خلال 10 ثوانٍ')),
           ('BX-0717-01-007', 'Flame-retardant (self-extinguishing) belt', 'سير مقاوم للهب (ذاتي الانطفاء)', ('NN or EP carcass', 'قلب NN أو EP'),
            ('For underground mines, power plants and ports', 'للمناجم تحت الأرض ومحطات الكهرباء والموانئ')),
           ('BX-0684-01-006', 'Abrasion-resistant belt', 'سير مقاوم للتآكل', ('Abrasion-resistant cover (DIN test)', 'غطاء مقاوم للتآكل (اختبار DIN)'), ('For quarries and mines', 'للمحاجر والمناجم')),
           ('BX-0684-01-007', 'Impact- and cut-resistant belt', 'سير مقاوم للصدم والقطع', ('Impact- and cut-resistant cover', 'غطاء مقاوم للصدم والقطع'),
            ('For crusher discharge and coarse rock (15 kg hammer dropped from 400 mm test)', 'لمخرج الكسارات والصخر الخشن (اختبار مطرقة 15 كغ من ارتفاع 400 مم)')),
           ('BX-0271-02-005', 'Chevron belt', 'سير شيفرون', ('Width 300–2200 mm; cleat height 5–30 mm', 'عرض 300–2200 مم؛ ارتفاع النقش 5–30 مم'), ('Inclined conveying up to about 45°', 'نقل مائل حتى نحو 45°')),
           ('BX-0717-01-003', 'Chevron (patterned) belt', 'سير شيفرون منقوش', ('EP / NN; open and closed V, U and multi-V patterns; pattern height 5–32 mm', 'EP / NN؛ أنماط V مفتوحة ومغلقة وU وV متعددة؛ ارتفاع النقش 5–32 مم'),
            ('Width 300–1800 mm; full-thickness strength 160–3150 N/mm; elongation ≤ 4 %', 'عرض 300–1800 مم؛ متانة بكامل السماكة 160–3150 نيوتن/مم؛ استطالة ≤ 4%')),
           ('BX-0684-01-008', 'Chevron belt, moulded cleats', 'سير شيفرون بنقوش مقولبة', ('Chevron height 2.4–32 mm; belt width 330–1500 mm', 'ارتفاع النقش 2.4–32 مم؛ عرض السير 330–1500 مم'),
            ('Inclines to about 30° for gravel and 40° for wet sand', 'ميل حتى نحو 30° للحصى و40° للرمل الرطب')),
           ('BX-0271-02-007', 'Corrugated sidewall belt', 'سير بجوانب مموجة', ('Sidewalls 60–400 mm; base width 300–1400 mm', 'جوانب 60–400 مم؛ عرض القاعدة 300–1400 مم'), ('Steep-incline conveying', 'نقل شديد الميل')),
           ('BX-0717-01-013', 'Corrugated sidewall belt, heavy duty', 'سير بجوانب مموجة للخدمة الشاقة',
            ('Bases XE, XE+2, XE-SC+2 and XST-SC; sidewalls 40–630 mm; C, T and TC cleats 35–600 mm', 'قواعد XE وXE+2 وXE-SC+2 وXST-SC؛ جوانب 40–630 مم؛ فواصل C وT وTC بارتفاع 35–600 مم'),
            ('Inclines up to 90°; base width 300–2400 mm; 250–7500 N/mm; up to 6000 m³/h', 'ميل حتى 90°؛ عرض القاعدة 300–2400 مم؛ 250–7500 نيوتن/مم؛ حتى 6000 م³/ساعة')),
           ('BX-0684-01-009', 'Sidewall belt', 'سير بجوانب', ('Base width 300–1400 mm; sidewalls 40–300 mm; cleats 35–260 mm', 'عرض القاعدة 300–1400 مم؛ جوانب 40–300 مم؛ فواصل 35–260 مم'),
            ('Hot-vulcanised sidewalls and cleats', 'جوانب وفواصل مفلكنة على الساخن')),
           ('BX-0717-01-009', 'Bucket elevator belt', 'سير للروافع الدلوية', ('Bucket width 250–1600 mm', 'عرض الدلو 250–1600 مم'), ('Low-elongation belt for vertical lifting', 'سير منخفض الاستطالة للرفع الرأسي'))],
          key_rows=['types', 'data'], unit=PRODUCTS),
], type_label=('Product', 'المنتج'))

# p45 polyurethane and rubber screen panels ------------------------------------------------------------------------------
F['polyurethane-rubber-screen-panels'] = family('polyurethane-rubber-screen-panels', CAT, [
    table('panels', ('Polyurethane and rubber screen media', 'وسائط الغربلة من البولي يوريثان والمطاط'), ('Apertures 0.045–8 mm (fine panels)', 'فتحات 0.045–8 مم (الألواح الناعمة)'),
          [('data', 'Key data', 'أهم البيانات')],
          [('BX-0302-01-001', 'Fine urethane screen panels', 'ألواح غربلة يوريثان ناعمة',
            ('Apertures 0.045–8 mm; open area 32–43 %; popular size 1045 × 700 mm; for high-frequency multi-deck and other screens',
             'فتحات 0.045–8 مم؛ مساحة مفتوحة 32–43%؛ المقاس الشائع 1045 × 700 مم؛ للغرابيل عالية التردد متعددة الطوابق وغيرها')),
           ('BX-0302-01-005', 'Polyurethane screen panels', 'ألواح غربلة بولي يوريثان',
            ('PU or rubber with steel-wire-rope reinforcement; aperture from 3 mm; 80–95 Shore A; hook or screw fixing; any size',
             'بولي يوريثان أو مطاط مقوّى بحبال فولاذية؛ فتحة من 3 مم؛ صلادة 80–95 شور A؛ تثبيت بخطاف أو براغٍ؛ أي مقاس')),
           ('BX-0302-01-004', 'PU dewatering slot panels', 'ألواح بولي يوريثان مشقوقة لنزع الماء',
            ('Slots 0.1–2.5 × 4–16 mm; 30, 45 or 50 mm thick; 305 / 500 / 515 mm wide, 305–1220 mm long; bolt, pin, strip or rail fixing',
             'شقوق 0.1–2.5 × 4–16 مم؛ سماكة 30 أو 45 أو 50 مم؛ عرض 305 / 500 / 515 مم وطول 305–1220 مم؛ تثبيت ببراغٍ أو مسامير أو شرائط أو سكك')),
           ('BX-0302-01-002', 'PU-coated wire-rope screen', 'غربال حبال فولاذية مغلّفة بالبولي يوريثان',
            ('Light and flexible; 3–8 × the wear life of wire mesh; low noise and blinding', 'خفيف ومرن؛ عمر تآكل 3–8 أضعاف الشبك السلكي؛ ضجيج وانسداد أقل')),
           ('BX-0302-01-003', 'Self-cleaning PU-strip screen', 'غربال ذاتي التنظيف بشرائط بولي يوريثان',
            ('Steel or stainless grid with PU strips on the bars; aperture from 3 mm', 'شبكة فولاذ أو ستانلس بشرائط بولي يوريثان على القضبان؛ فتحة من 3 مم')),
           ('BX-0302-01-010', 'Self-cleaning wire screen', 'غربال سلكي ذاتي التنظيف', ('Hook-edge screen for sticky and wet feed', 'غربال بحواف خطافية للتغذية اللزجة والرطبة')),
           ('BX-0302-01-008', 'Flip-flop screen panels', 'ألواح غربلة مرنة متقلبة', ('Flexible perforated panels for wet, sticky ore', 'ألواح مثقبة مرنة للخام الرطب واللزج')),
           ('BX-0302-01-009', 'Rubber screen panels', 'ألواح غربلة مطاطية', ('Modular rubber panels', 'ألواح مطاطية معيارية')),
           ('BX-0302-01-007', 'PU composite screens', 'غرابيل مركّبة من البولي يوريثان', ('Polyurethane–steel composite screens made to the deck', 'غرابيل مركّبة من البولي يوريثان والفولاذ حسب سطح الغربال')),
           ('BX-0302-01-015', 'Triangular dewatering screen panels', 'ألواح نزع ماء بقضبان مثلثة', ('Triangular-bar panels for dewatering', 'ألواح بقضبان مثلثة المقطع لنزع الماء')),
           ('BX-0302-01-013', 'Pins and sleeves', 'مسامير وجلب التثبيت', ('Fixing for modular panels', 'لتثبيت الألواح المعيارية')),
           ('BX-0302-01-014', 'WS85 support profiles', 'مقاطع الدعم WS85', ('Support rails for modular panels', 'سكك دعم للألواح المعيارية')),
           ('BX-0302-01-016', 'Multi-deck high-frequency screen', 'غربال عالي التردد متعدد الطوابق',
            ('Wet fine screen with stacked decks and twin vibration motors', 'غربال رطب ناعم بطوابق متراكبة ومحركي اهتزاز')),
           ('BX-0302-01-019', 'Slurry divider', 'موزّع اللب', ('Splits the feed between the decks of the multi-deck screen', 'يوزّع التغذية على طوابق الغربال متعدد الطوابق')),
           ('BX-0302-01-018', 'Vibration motors', 'محركات اهتزاز', ('Replacement vibration motors for screens and feeders', 'محركات اهتزاز بديلة للغرابيل والمغذيات'))],
          intro=('Polyurethane and rubber panels last several times longer than wire mesh in wet screening. Price depends on the panel size and aperture: quote the screen model and deck size.',
                 'تدوم ألواح البولي يوريثان والمطاط أضعاف الشبك السلكي في الغربلة الرطبة. يعتمد السعر على مقاس اللوح والفتحة: اذكر موديل الغربال ومقاس السطح.'),
          key_rows=['data'], unit=PRODUCTS),
], type_label=('Product', 'المنتج'))

# p48 tramp-iron separators and belt metal detectors ---------------------------------------------------------------------------
SEP = [('models', 'Models / sizes', 'الموديلات / المقاسات'), ('data', 'Key data', 'أهم البيانات')]
F['tramp-iron-separators-metal-detectors'] = family('tramp-iron-separators-metal-detectors', CAT, [
    table('separators', ('Belt metal detectors and magnetic iron separators', 'كواشف المعادن للسيور وفواصل الحديد المغناطيسية'), ('Belts 400–2000 mm', 'سيور 400–2000 مم'), SEP,
          [('BX-0386-01-001', 'Belt metal detector JYG-B', 'كاشف معادن للسيور JYG-B', 'JYG-B-500 … JYG-B-1800 (9 sizes)',
            ('Detects tramp metal on belts 500–1800 mm wide to protect crushers', 'يكشف المعادن الشاردة على سيور بعرض 500–1800 مم لحماية الكسارات')),
           ('BX-0386-02-001', 'Suspended permanent-magnet separator RCYB', 'فاصل مغناطيس دائم معلّق RCYB', 'RCYB-4 … RCYB-16 (13 sizes)',
            ('Belts 400–1600 mm; suspension height 75–450 mm; NdFeB magnets; no power needed', 'سيور 400–1600 مم؛ ارتفاع التعليق 75–450 مم؛ مغانط نيوديميوم؛ بلا كهرباء')),
           ('BX-0386-02-002', 'Self-cleaning permanent-magnet separator RCYD(C)', 'فاصل مغناطيس دائم ذاتي التنظيف RCYD(C)', 'RCYD(C)-5 … -20 (10 sizes)',
            ('Belts 500–2000 mm; self-cleaning discharge belt', 'سيور 500–2000 مم؛ سير تفريغ ذاتي التنظيف')),
           ('BX-0386-02-003', 'Permanent-magnet iron separator RCYP', 'فاصل حديد بمغناطيس دائم RCYP', 'RCYP-4 … -14 (8 sizes)', ('Suspended permanent-magnet type', 'نوع معلّق بمغناطيس دائم')),
           ('BX-0386-02-004', 'Self-cleaning permanent-magnet separator RCYP II', 'فاصل مغناطيس دائم ذاتي التنظيف RCYP II', 'RCYPII-5 … -18 (9 sizes)', ('Self-cleaning permanent-magnet type', 'نوع ذاتي التنظيف بمغناطيس دائم')),
           ('BX-0386-02-005', 'Light-duty permanent-magnet separator RCY-Q', 'فاصل مغناطيس دائم خفيف RCY-Q', 'RCY-Q40 … Q120 (6 sizes)', ('Light-duty permanent-magnet type', 'نوع خفيف بمغناطيس دائم')),
           ('BX-0386-02-006', 'Armoured permanent-magnet separator RCYK', 'فاصل مغناطيس دائم مدرّع RCYK', 'RCYK-5 … -14 (6 sizes)', ('Armoured permanent-magnet type', 'نوع مدرّع بمغناطيس دائم')),
           ('BX-0386-02-007', 'Dry electromagnetic separator RCDB', 'فاصل كهرومغناطيسي جاف RCDB', 'RCDB-4 … -18 (10 sizes)', ('Air-cooled electromagnet', 'مغناطيس كهربائي مبرّد بالهواء')),
           ('BX-0386-02-008', 'Self-cleaning electromagnetic separator RCDD', 'فاصل كهرومغناطيسي ذاتي التنظيف RCDD', 'RCDD-6 … -18 (8 sizes)', ('Self-cleaning electromagnet', 'مغناطيس كهربائي ذاتي التنظيف')),
           ('BX-0386-02-009', 'Oil-cooled electromagnetic separator RCDEJ', 'فاصل كهرومغناطيسي مبرّد بالزيت RCDEJ', 'RCDEJ-12 … -24 (7 sizes)', ('Forced oil circulation; heavy duty', 'دوران زيت قسري؛ للخدمة الشاقة')),
           ('BX-0386-02-010', 'Oil-cooled self-cleaning separator RCDFJ', 'فاصل مبرّد بالزيت ذاتي التنظيف RCDFJ', 'RCDFJ-12 … -24 (7 sizes)', ('Oil-cooled, self-cleaning', 'مبرّد بالزيت وذاتي التنظيف'))],
          intro=('Tramp-iron protection for conveyors feeding crushers and mills.', 'حماية من الحديد الشارد للسيور التي تغذي الكسارات والطواحين.'),
          key_rows=['models', 'data'], unit=TYPES),
], type_label=('Product', 'المنتج'))

# ================================================================== WEAR & SPARE PARTS (pages 49–54) ============

PARTS = [('items', 'Items / models', 'القطع / الموديلات'), ('data', 'Material / key data', 'الخامة / أهم البيانات')]
MN = ('High-manganese steel Mn13Cr2, Mn18Cr2 or Mn22Cr2', 'فولاذ عالي المنغنيز Mn13Cr2 أو Mn18Cr2 أو Mn22Cr2')
F['crusher-wear-spare-parts'] = family('crusher-wear-spare-parts', CAT, [
    table('groups', ('Part groups', 'مجموعات القطع'), ('Jaw, cone and impact crushers', 'الكسارات الفكية والمخروطية والصدمية'), PARTS,
          [('BX-0152-01-001', 'Jaw crusher wear parts', 'قطع تآكل الكسارات الفكية', ('Fixed and movable jaw plates, cheek plates', 'ألواح الفك الثابتة والمتحركة والألواح الجانبية'),
            ('High-manganese, alloy or carbon steel', 'فولاذ عالي المنغنيز أو سبائكي أو كربوني')),
           ('BX-0152-01-002', 'TiC-insert jaw plates', 'ألواح فك بإدخالات كربيد التيتانيوم', ('Jaw plates with titanium-carbide inserts', 'ألواح فك بإدخالات كربيد التيتانيوم'), ('Longer wear life', 'عمر تآكل أطول')),
           ('BX-0152-01-003', 'Jaw crusher spares', 'قطع غيار الكسارات الفكية', ('Frames, pitmans, eccentric shafts, flywheels, toggle seats', 'الإطارات وأذرع التوصيل والأعمدة اللامركزية والحدافات ومقاعد الذراع'), None),
           ('BX-0152-01-005', 'Cone crusher wear parts', 'قطع تآكل الكسارات المخروطية', ('Mantles and bowl liners (concaves)', 'البطانات الداخلية والخارجية'), ('High-manganese steel', 'فولاذ عالي المنغنيز')),
           ('BX-0152-01-006', 'TiC-insert cone liners', 'بطانات مخروطية بإدخالات كربيد التيتانيوم', ('Mantles and concaves with TiC inserts', 'بطانات داخلية وخارجية بإدخالات كربيد التيتانيوم'), ('Longer wear life', 'عمر تآكل أطول')),
           ('BX-0152-01-007', 'Cone crusher spares', 'قطع غيار الكسارات المخروطية', ('Main shafts, bronze bushings, frames, eccentrics, gears', 'الأعمدة الرئيسية والجلب البرونزية والإطارات والأجزاء اللامركزية والتروس'), None),
           ('BX-0152-01-009', 'Impact crusher parts', 'قطع الكسارات الصدمية', ('Blow bars and impact plates', 'قضبان الضرب وألواح الصدم'), ('Martensitic steel; ceramic composite option', 'فولاذ مارتنسيتي؛ وخيار مركّب بالسيراميك'))],
          intro=('Quote the crusher model and the part drawing or part number to receive a price.', 'اذكر موديل الكسارة ورسم القطعة أو رقمها لتصلك التسعيرة.'),
          key_rows=['items', 'data'], unit={'ar': ['مجموعة واحدة', 'مجموعتان', 'مجموعات'], 'en': ['group', 'groups']}),
    table('jaw-vsi-replacement', ('Jaw and VSI crusher parts – replacement series', 'قطع الكسارات الفكية وVSI – سلاسل بديلة'), ('Matched to the original part', 'مطابقة للقطعة الأصلية'), PARTS,
          [('BX-0628-01-001', 'Cheek plates – C-series jaw crushers', 'ألواح جانبية – كسارات فكية من السلسلة C',
            ('C63–C200 and C3054 (16 sizes)', 'C63–C200 وC3054 (16 مقاساً)'), MN),
           ('BX-0628-01-002', 'Cheek plates – CJ-series jaw crushers', 'ألواح جانبية – كسارات فكية من السلسلة CJ', 'CJ409, CJ411, CJ412, CJ612, CJ613', MN),
           ('BX-0628-01-003', 'Cheek plates – JW-series jaw crushers', 'ألواح جانبية – كسارات فكية من السلسلة JW', 'JW40, JW42, JW55', MN),
           ('BX-0226-01-003', 'Jaw crusher wear and spare parts', 'قطع التآكل والغيار للكسارات الفكية',
            ('C-, CJ- and JM-series jaw crushers', 'كسارات فكية من السلاسل C وCJ وJM'),
            ('Fixed and movable jaw plates, cheek plates, pitman, shafts, bearings, wedges and springs', 'ألواح الفك الثابتة والمتحركة والألواح الجانبية وذراع التوصيل والأعمدة والمحامل والأسافين والنوابض')),
           ('BX-0226-01-005', 'VSI crusher wear parts', 'قطع تآكل كسارات VSI', ('B-series and CV-series VSI crushers', 'كسارات VSI من السلسلتين B وCV'),
            ('Wear parts for vertical-shaft impact (sand-making) crushers', 'قطع تآكل الكسارات الصدمية رأسية العمود (صناعة الرمل)'))],
          intro=('Replacement parts cast to match the original part; send the crusher model and the original part number.',
                 'قطع بديلة مصبوبة مطابقة للقطعة الأصلية؛ أرسل موديل الكسارة ورقم القطعة الأصلية.'),
          key_rows=['items', 'data'], unit=PRODUCTS),
    table('cone-gyratory-replacement', ('Cone and gyratory crusher parts – replacement series', 'قطع الكسارات المخروطية والدوّارة – سلاسل بديلة'), ('Mn13–Mn22 steel', 'فولاذ Mn13–Mn22'), PARTS,
          [('BX-0628-01-004', 'Mantles and bowl liners – HP, MP and GP cone crushers', 'بطانات داخلية وخارجية – كسارات مخروطية HP وMP وGP',
            ('HP100–HP800, HP3–HP6; MP800–MP1250; GP100–GP550, GP100S–GP500S, GP11 (24 sizes)', 'HP100–HP800 وHP3–HP6؛ MP800–MP1250؛ GP100–GP550 وGP100S–GP500S وGP11 (24 مقاساً)'), MN),
           ('BX-0628-01-005', 'Mantles and bowl liners – gyratory crushers', 'بطانات داخلية وخارجية – كسارات دوّارة', '5065, 4265, MKIII54-75134, MKIII60-89119, MKIII60-110, S6275102', MN),
           ('BX-0628-01-006', 'Mantles and bowl liners – CH and CS cone crushers', 'بطانات داخلية وخارجية – كسارات مخروطية CH وCS', ('CH430–CH895, CS440, CS660 (8 sizes)', 'CH430–CH895 وCS440 وCS660 (8 مقاسات)'), MN),
           ('BX-0628-01-007', 'Mantles and bowl liners – TC cone crushers', 'بطانات داخلية وخارجية – كسارات مخروطية TC', 'TC66, TC84, TC84X, TC5A', MN),
           ('BX-0628-01-008', 'Mantles and bowl liners – XL cone crushers', 'بطانات داخلية وخارجية – كسارات مخروطية XL', 'XL200, XL300, XL400', MN),
           ('BX-0628-01-009', 'Mantles and bowl liners – T, TC and MVP cone crushers', 'بطانات داخلية وخارجية – كسارات مخروطية T وTC وMVP', 'T1000, TC1300, MVP550', MN),
           ('BX-0226-01-004', 'Cone crusher wear and spare parts', 'قطع التآكل والغيار للكسارات المخروطية',
            ('GP, HP, CH, CS, H and S series cone crushers', 'كسارات مخروطية من السلاسل GP وHP وCH وCS وH وS'),
            ('Mantles and concaves, head, bowl and frame, main and counter shafts, eccentric bushing and socket, gears, adjusting ring, springs, dampers, filters, seals, valves, tramp-release cylinders and accumulators',
             'البطانات الداخلية والخارجية، والرأس والوعاء والإطار، والعمود الرئيسي والأفقي، والجلبة اللامركزية والمقبس، والتروس، وحلقة الضبط، والنوابض والمخمّدات والفلاتر والأختام والصمامات، وأسطوانات تحرير الشوائب والمراكم'))],
          key_rows=['items', 'data'], unit=PRODUCTS),
], type_label=('Part group', 'مجموعة القطع'))

# p50 ceramic and polymer wear protection --------------------------------------------------------------------------------------------
F['ceramic-wear-protection'] = family('ceramic-wear-protection', CAT, [
    table('wear', ('Ceramic and polymer wear protection', 'الحماية من التآكل بالسيراميك والبوليمر'), ('Alumina 92–99 %', 'ألومينا 92–99%'),
          [('material', 'Material / models', 'الخامة / الموديلات'), ('use', 'Application', 'الاستخدام')],
          [('BX-0174-01-008', 'Ceramic-rubber composite panels', 'ألواح مركّبة من السيراميك والمطاط',
            ('Alumina 92 / 95 / 99 %, ZTA or SiC tiles vulcanised in rubber on a steel backing', 'بلاطات ألومينا 92 / 95 / 99% أو ZTA أو كربيد السيليكون مفلكنة في المطاط على قاعدة فولاذية'),
            ('Chutes, transfer points, cyclones and launders', 'المزالق ونقاط النقل والسيكلونات والمجاري')),
           ('BX-0174-01-011', 'Ceramic wear tiles', 'بلاطات سيراميك مقاومة للتآكل', 'HC90 · HC92 · HC95 · HCT95 · HC99 · HCZTA',
            ('Lining plates in many shapes for bins, chutes and pipes', 'ألواح تبطين بأشكال متعددة للصوامع والمزالق والأنابيب')),
           ('BX-0174-01-010', 'Ceramic-lined hydrocyclones and liners', 'هيدروسيكلونات مبطّنة بالسيراميك وبطاناتها',
            ('Ø 350–1400 mm; alumina, SiC or polyurethane', 'قطر 350–1400 مم؛ ألومينا أو كربيد السيليكون أو بولي يوريثان'),
            ('Cylinder and cone liners, inlets, apexes and vortex finders', 'بطانات الأسطوانة والمخروط والمداخل والفتحات السفلية وأنابيب الفيض')),
           ('BX-0174-01-013', 'Ceramic wearing compound', 'معجون سيراميك مقاوم للتآكل',
            ('Alumina 92 % or ZTA beads 0.5–2 mm in epoxy; 86 Shore D; −60 to 120 °C', 'حبيبات ألومينا 92% أو ZTA بمقاس 0.5–2 مم في إيبوكسي؛ صلادة 86 شور D؛ من −60 إلى 120°م'),
            ('Repairs where tiling is not possible', 'للإصلاح حيث يتعذر التبليط')),
           ('BX-0062-01-007', 'UHMW-PE liners', 'بطانات UHMW-PE', ('Self-lubricating, impact- and wear-resistant sheet', 'ألواح ذاتية التزييت مقاومة للصدم والتآكل'),
            ('Chutes and hoppers; stops material hang-up', 'المزالق والقواديس؛ تمنع التصاق المادة'))],
          intro=('Supplied to drawing or measured on site.', 'تُورَّد حسب الرسم أو بالقياس في الموقع.'),
          key_rows=['material', 'use'], unit=PRODUCTS),
], type_label=('Product', 'المنتج'))

# p51 mill gears and heavy castings ---------------------------------------------------------------------------------------------------
F['mill-gears-heavy-castings'] = family('mill-gears-heavy-castings', CAT, [
    table('castings', ('Mill gears and heavy steel castings', 'تروس الطواحين والمسبوكات الفولاذية الثقيلة'), ('From about 5 t', 'من نحو 5 أطنان'),
          [('build', 'Construction', 'الصنع'), ('supply', 'Supply', 'التوريد')],
          [('BX-0156-02-003', 'Mill girth gears', 'تروس الطواحين المحيطية', ('Cast and machined; for ball mills and rotary kilns', 'مصبوبة ومشغّلة آلياً؛ للطواحين الكروية والأفران الدوارة'), ('To drawing and size', 'حسب الرسم والمقاس')),
           ('BX-0156-02-004', 'Mill trunnions and end covers', 'محاور الطواحين وأغطية النهاية', ('Cast mill heads', 'رؤوس طواحين مصبوبة'), ('To drawing and size', 'حسب الرسم والمقاس')),
           ('BX-0156-01-015', 'Trunnion, girth gear and pinion sets', 'أطقم المحور والترس المحيطي والترس الصغير', ('For large ball mills', 'للطواحين الكروية الكبيرة'), ('To drawing', 'حسب الرسم')),
           ('BX-0156-02-002', 'Cone-crusher shells and adjusting rings', 'أغلفة الكسارات المخروطية وحلقات الضبط', ('Cast and machined shells, fixed cones and adjusting rings', 'أغلفة ومخاريط ثابتة وحلقات ضبط مصبوبة ومشغّلة آلياً'), ('To drawing', 'حسب الرسم'))],
          intro=('Heavy steel castings from about 5 t: send the drawing or the old part dimensions for a quotation.', 'مسبوكات فولاذية ثقيلة من نحو 5 أطنان: أرسل الرسم أو أبعاد القطعة القديمة لعرض السعر.'),
          key_rows=['build', 'supply'], unit=PRODUCTS),
], type_label=('Part', 'القطعة'))

# p52 drive V-belts and industrial rubber ------------------------------------------------------------------------------------------------
F['drive-v-belts-industrial-rubber'] = family('drive-v-belts-industrial-rubber', CAT, [
    table('vbelts', ('Drive V-belts', 'سيور V لنقل الحركة'), ('Top width 8–50 mm', 'العرض العلوي 8–50 مم'),
          [('sections', 'Sections / grades', 'المقاطع / الدرجات'), ('data', 'Key data', 'أهم البيانات')],
          [('BX-0684-03-001', 'Classical wrapped V-belt', 'سير V كلاسيكي ملفوف', 'K, Z, A, AB, B, BC, C, CD, D, CE, CL, E, F',
            ('Top width 8–50 mm; 40°; lengths about 356–21,000 mm; high strength, low stretch', 'العرض العلوي 8–50 مم؛ 40°؛ أطوال نحو 356–21,000 مم؛ متانة عالية واستطالة قليلة')),
           ('BX-0684-03-002', 'Wrapped narrow (wedge) V-belt', 'سير V ضيق (إسفيني) ملفوف', '3V (9N), 5V (15N), 8V (25N), SPZ, SPA, SPB, SPC',
            ('Top width 9.5–25.5 mm; lengths 508–20,955 mm; up to 40 m/s; efficiency above 95 %', 'العرض العلوي 9.5–25.5 مم؛ أطوال 508–20,955 مم؛ حتى 40 م/ث؛ كفاءة أعلى من 95%')),
           ('BX-0684-03-004', 'Banded classical V-belt', 'سير V كلاسيكي مجمّع', 'AJ, BJ, CJ, DJ',
            ('Top width 13.6–32.8 mm; lengths 1549–15,748 mm; stops belt whip and turn-over', 'العرض العلوي 13.6–32.8 مم؛ أطوال 1549–15,748 مم؛ يمنع اهتزاز السير وانقلابه')),
           ('BX-0684-03-005', 'Banded wedge V-belt', 'سير V إسفيني مجمّع', '3V (9J), 5V (15J), 8V (25J), SPZ, SPA, SPB, SPC', ('For heavy and shock loads', 'للأحمال الثقيلة والصدمات')),
           ('BX-0684-04-007', 'Raw-edge cogged V-belt', 'سير V مسنّن بحافة خام', 'AVX, ZX, AX, BX, CX, DX, XPZ, XPA, XPB, XPC, 3VX, 5VX, 8VX, RECMF',
            ('Top width 9.5–32 mm; for small pulleys and high speeds; heat-, oil- and wear-resistant', 'العرض العلوي 9.5–32 مم؛ للبكرات الصغيرة والسرعات العالية؛ مقاوم للحرارة والزيت والتآكل')),
           ('BX-0684-03-009', 'Aramid-cord V-belt', 'سير V بحبال أراميد', ('Made to section and length', 'حسب المقطع والطول'),
            ('High tensile strength, very low stretch; no re-tensioning; for severe shock loads', 'مقاومة شد عالية واستطالة قليلة جداً؛ لا يحتاج إعادة شد؛ للصدمات الشديدة'))],
          key_rows=['sections', 'data'], unit=TYPES),
    table('rubber', ('Industrial rubber for conveyors and wear lining', 'المطاط الصناعي للسيور وتبطين التآكل'), ('1–50 mm thick', 'سماكة 1–50 مم'),
          [('sizes', 'Sizes / grades', 'المقاسات / الدرجات'), ('data', 'Key data', 'أهم البيانات')],
          [('BX-0717-01-016', 'High tear-resistant rubber sheet NR40', 'لوح مطاط عالي مقاومة التمزق NR40', ('1–30 mm thick; up to 2 m wide', 'سماكة 1–30 مم؛ عرض حتى 2 م'),
            ('Shore A 40 ± 5; tensile ≥ 22 MPa; elongation ≥ 700 %; tear ≥ 60 N/mm; −40 to 80 °C', 'صلادة 40 ± 5 شور A؛ شد ≥ 22 ميجاباسكال؛ استطالة ≥ 700%؛ تمزق ≥ 60 نيوتن/مم؛ من −40 إلى 80°م')),
           ('BX-0717-01-017', 'Abrasion-resistant rubber sheet for mines', 'لوح مطاط مقاوم للتآكل للمناجم',
            ('Grades 6, 8, 10, 12, 15 MPa; 1–30 mm thick; ≤ 2 m wide; ≤ 10 m long', 'درجات 6 و8 و10 و12 و15 ميجاباسكال؛ سماكة 1–30 مم؛ عرض ≤ 2 م؛ طول ≤ 10 م'),
            ('Shore A 65 ± 5 (or 60 ± 5); abrasion ≤ 90–350 mm³ by grade', 'صلادة 65 ± 5 شور A (أو 60 ± 5)؛ تآكل ≤ 90–350 مم³ حسب الدرجة')),
           ('BX-0717-01-018', 'Rubber pulley lagging', 'تكسية البكرات بالمطاط', ('10, 12, 15 mm thick; 0.6–2 m wide; 1–20 m long', 'سماكة 10 و12 و15 مم؛ عرض 0.6–2 م؛ طول 1–20 م'),
            ('Shore A 60 ± 5; tensile ≥ 10 MPa; abrasion ≤ 150 mm³; CN bonding layer available', 'صلادة 60 ± 5 شور A؛ شد ≥ 10 ميجاباسكال؛ تآكل ≤ 150 مم³؛ طبقة لصق CN متوفرة')),
           ('BX-0717-01-019', 'Sandwich rubber for belt cleaners', 'مطاط متعدد الطبقات لمنظفات السيور', ('Shore A 55, 60, 65', 'صلادة 55 و60 و65 شور A'),
            ('Tensile 4–15 MPa; scraper blades for dust and wet slurry', 'شد 4–15 ميجاباسكال؛ شفرات كشط للغبار واللب الرطب')),
           ('BX-0717-01-020', 'Rubber skirt board', 'ألواح مطاط جانبية للسيور', ('6–50 mm thick; 0.6–2 m wide; 1–20 m long', 'سماكة 6–50 مم؛ عرض 0.6–2 م؛ طول 1–20 م'),
            ('NR / SBR, Shore A 40–60; −40 to +100 °C; seals belt edges against spillage and dust', 'NR / SBR بصلادة 40–60 شور A؛ من −40 إلى +100°م؛ تحكم حواف السير ضد الانسكاب والغبار'))],
          key_rows=['sizes', 'data'], unit=PRODUCTS),
], type_label=('Product', 'المنتج'))

# p53 bearings and housed bearing units ------------------------------------------------------------------------------------------------
BRG = [('sizes', 'Sizes / models', 'المقاسات / الموديلات'), ('data', 'Key data', 'أهم البيانات')]
F['bearings-housed-bearing-units'] = family('bearings-housed-bearing-units', CAT, [
    table('bearings', ('Rolling bearings', 'محامل الدحرجة'), ('Bore 4–170 mm', 'قطر داخلي 4–170 مم'), BRG,
          [('BX-0716-01-003', 'Deep-groove ball bearings', 'محامل كروية أخدودية', '6000–6020, 6200–6220, 6300–6320, 6400–6420', ('Open, 2Z and 2RS', 'مفتوحة و2Z و2RS')),
           ('BX-0684-05-001', 'Deep-groove ball bearings, 60 series', 'محامل كروية أخدودية، سلسلة 60', '604–609, 6000–6026', ('Bore 4–130 mm; Z, ZZ, RZ, 2RZ, RS, 2RS, RW seals', 'قطر داخلي 4–130 مم؛ أغطية Z وZZ وRZ و2RZ وRS و2RS وRW')),
           ('BX-0684-05-002', 'Deep-groove ball bearings, 62 series', 'محامل كروية أخدودية، سلسلة 62', '624–629, 6200–6222', ('Bore 4–110 mm', 'قطر داخلي 4–110 مم')),
           ('BX-0684-05-003', 'Deep-groove ball bearings, 63 series', 'محامل كروية أخدودية، سلسلة 63', '635–639, 6300–6320', ('Bore 5–100 mm; heavier loads', 'قطر داخلي 5–100 مم؛ لأحمال أثقل')),
           ('BX-0716-01-004', 'Cylindrical roller bearings', 'محامل أسطوانية', 'NU1005…NU430, NJ1021…NJ428, NUP, N', ('Single row', 'صف واحد')),
           ('BX-0716-01-005', 'Tapered roller bearings', 'محامل مخروطية', ('30203…32960 (302, 303, 313, 320, 322, 323, 329, 330, 331, 332 series)', '30203…32960 (السلاسل 302 و303 و313 و320 و322 و323 و329 و330 و331 و332)'),
            ('Single row', 'صف واحد')),
           ('BX-0684-05-009', 'Tapered roller bearings, 30200 series', 'محامل مخروطية، سلسلة 30200', '30203–30228', ('Bore 17–140 mm', 'قطر داخلي 17–140 مم')),
           ('BX-0684-05-010', 'Tapered roller bearings, 30300 series', 'محامل مخروطية، سلسلة 30300', '30302–30324', ('Bore 15–120 mm; heavier loads', 'قطر داخلي 15–120 مم؛ لأحمال أثقل')),
           ('BX-0684-05-011', 'Tapered roller bearings, 32000 series', 'محامل مخروطية، سلسلة 32000', '32004–32034', ('Bore 20–170 mm; thin section', 'قطر داخلي 20–170 مم؛ مقطع رفيع')),
           ('BX-0684-05-012', 'Tapered roller bearings, 32200 series', 'محامل مخروطية، سلسلة 32200', '32203–32228', ('Bore 17–140 mm; wide', 'قطر داخلي 17–140 مم؛ عريضة')),
           ('BX-0684-05-013', 'Tapered roller bearings, 32300 series', 'محامل مخروطية، سلسلة 32300', '32304–32324', ('Bore 20–120 mm; wide, heavy duty', 'قطر داخلي 20–120 مم؛ عريضة للخدمة الشاقة')),
           ('BX-0716-01-006', 'Spherical roller bearings', 'محامل كروية الدحاريج', ('22205…22264, 22308…22356, 230, 231 and 232 series to 23248', '22205…22264 و22308…22356 والسلاسل 230 و231 و232 حتى 23248'),
            ('Double row; cylindrical or tapered bore', 'صفان؛ ثقب أسطواني أو مخروطي'))],
          key_rows=['sizes', 'data'], unit=SERIES_U),
    table('housed', ('UC insert bearings and housed units', 'محامل UC ووحدات الكراسي'), ('UC201–UC328', 'UC201–UC328'), BRG,
          [('BX-0716-01-009', 'UC insert bearings', 'محامل إدخال UC', 'UC201…UC328', ('Set-screw inserts for housed units', 'محامل بمسمار تثبيت لوحدات الكراسي')),
           ('BX-0716-01-013', 'UCP pillow-block units', 'وحدات كراسي قائمة UCP', 'UCP201…UCP328', ('Cast-iron housings', 'كراسٍ من حديد الزهر')),
           ('BX-0716-01-014', 'UCF square-flange units', 'وحدات بفلنجة مربعة UCF', 'UCF201…UCF328', ('Four-bolt flange', 'فلنجة بأربعة براغٍ')),
           ('BX-0716-01-015', 'UCFL two-bolt flange units', 'وحدات بفلنجة ببرغيين UCFL', 'UCFL201…UCFL326', ('Oval flange', 'فلنجة بيضاوية')),
           ('BX-0716-01-016', 'UCT take-up units', 'وحدات شد UCT', 'UCT201…UCT218', ('Sliding take-up housing', 'كرسي شد منزلق'))],
          key_rows=['sizes', 'data'], unit=SERIES_U),
], type_label=('Series', 'السلسلة'))
