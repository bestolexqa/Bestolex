"""BXC-04 Ed6 (Crushing, grinding & screening) model tables, part 1: crushers (catalogue pages 4–20).
Clean tables come from the catalogue page text (bxc04_pages.json, made by parse_tables.py); tables whose cells
wrap in the PDF are typed here from the page image. Every BX code is checked against the supplier list
(list_index.json) when the tables are built."""
import json, os, re
from lib import table, family

CAT = 'BXC-04 Ed6'
HERE = os.path.dirname(__file__)
PAGES = json.load(open(os.path.join(HERE, 'bxc04_pages.json')))
F = {}

H = {  # column headers EN → AR
    'Capacity (t/h)': 'الطاقة (طن/ساعة)', 'Capacity – clinker (t/h)': 'الطاقة – كلنكر (طن/ساعة)',
    'Capacity – limestone (t/h)': 'الطاقة – حجر جيري (طن/ساعة)', 'Cone Ø (mm)': 'قطر المخروط (مم)',
    'Discharge (mm)': 'المخرج (مم)', 'Discharge opening (mm)': 'فتحة التفريغ (مم)',
    'Discharge setting (mm)': 'ضبط التفريغ (مم)', 'Feed opening (mm)': 'فتحة التغذية (مم)',
    'Feed size (mm)': 'حجم التغذية (مم)', 'Max. capacity (t/h)': 'أقصى طاقة (طن/ساعة)', 'Max. feed (mm)': 'أقصى تغذية (مم)',
    'Max. feed size (mm)': 'أقصى حجم تغذية (مم)', 'Max. installed power (kW)': 'أقصى قدرة مركّبة (كيلوواط)',
    'Max. speed (rpm)': 'أقصى سرعة (دورة/دقيقة)', 'Output size (mm)': 'حجم الناتج (مم)',
    'Overall dimensions (mm)': 'الأبعاد الكلية (مم)', 'Power (kW)': 'القدرة (كيلوواط)', 'Product size (mm)': 'حجم المنتج (مم)',
    'Roller length (mm)': 'طول الأسطوانة (مم)', 'Roller Ø (mm)': 'قطر الأسطوانة (مم)', 'Rotor (mm)': 'الدوّار (مم)',
    'Rotor Ø × L (mm)': 'قطر الدوّار × الطول (مم)', 'Rotor Ø × length (mm)': 'قطر الدوّار × الطول (مم)', 'Weight (t)': 'الوزن (طن)',
    'Rotor speed (m/s)': 'سرعة الدوّار (م/ث)', 'Discharge size (mm)': 'حجم التفريغ (مم)', 'Roll Ø × L (mm)': 'قطر الأسطوانة × الطول (مم)',
    'Models': 'الموديلات', 'Key data': 'أهم البيانات',
}


def key(h):
    return re.sub(r'[^a-z0-9]+', '-', h.lower().split('(')[0].strip()).strip('-')


def cols(headers):
    return [(key(h), h, H[h]) for h in headers]


def auto(page, n, tid, label, key_txt, key_rows=None, intro=None, unit=None):
    t = PAGES[str(page)]['tables'][n]
    head = t['header']
    assert head[0] == 'Model' and len(t['codes']) == 1, (page, n, head, t['codes'])
    for r in t['rows']:
        assert len(r) == len(head), (page, n, r)
    rows = [(None, r[0], None, *r[1:]) for r in t['rows']]
    return table(tid, label, key_txt, cols(head[1:]), rows, intro=intro, key_rows=key_rows, code=t['codes'][0], unit=unit)


SERIES = [('models', 'Models', 'الموديلات'), ('data', 'Key data', 'أهم البيانات')]

# p4 + p19 jaw crushers ------------------------------------------------------------------------------------
F['jaw-crushers'] = family('jaw-crushers', CAT, [
    auto(4, 0, 'small', ('Small jaw crushers (electric or diesel drive)', 'كسارات فكية صغيرة (محرك كهربائي أو ديزل)'), ('1–10 t/h', '1–10 طن/ساعة'), ['capacity', 'output-size', 'power']),
    auto(4, 1, 'pe-pex', ('PE / PEX jaw crushers', 'كسارات فكية PE / PEX'), ('5–380 t/h', '5–380 طن/ساعة'), ['capacity', 'output-size', 'power']),
    auto(4, 2, 'mc', ('MC heavy jaw crushers', 'كسارات فكية ثقيلة MC'), ('65–1460 t/h', '65–1460 طن/ساعة'), ['capacity', 'discharge-opening', 'power']),
    table('pef-pex-additional', ('PEF / PEX jaw crushers – additional sizes', 'كسارات فكية PEF / PEX – مقاسات إضافية'), ('0.4–500 t/h', '0.4–500 طن/ساعة'),
          cols(['Max. feed size (mm)', 'Discharge size (mm)', 'Capacity (t/h)', 'Power (kW)', 'Weight (t)']),
          [(None, 'PEF-100×150', None, '90', '5–20', '0.4–1.8', '2.2', '0.4'), (None, 'PEF-900×1200', None, '750', '100–220', '150–330', '160', '48'),
           (None, 'PEF-1000×1200', None, '780', '195–270', '190–280', '160', '54.7'), (None, 'PEF-1200×1500', None, '1020', '150–300', '270–500', '200', '96.8'),
           (None, 'PEX-100×500', None, '80', '7–20', '3–15', '7.5', '1.5'), (None, 'PEX-150×750', None, '120', '10–40', '8–35', '15', '3.7'),
           (None, 'PEX-200×1000', None, '210', '13–50', '15–50', '30', '6.3'), (None, 'PEX-300×1300', None, '250', '20–90', '20–130', '75', '12.6')],
          intro=('PEF for coarse (primary) crushing, PEX for fine (secondary) crushing.', 'PEF للتكسير الخشن (الأولي)، وPEX للتكسير الناعم (الثانوي).'),
          code='BX-0033-01-001', key_rows=['capacity', 'discharge-size', 'power']),
], type_label=('Series', 'السلسلة'))

# p5 + p20 gyratory & impact -------------------------------------------------------------------------------
F['gyratory-impact-crushers'] = family('gyratory-impact-crushers', CAT, [
    auto(5, 0, 'mg', ('MG gyratory crushers', 'كسارات دوّارة MG'), ('Up to 17,000 t/h', 'حتى 17,000 طن/ساعة'), ['max-capacity', 'max-feed-size', 'power']),
    auto(5, 1, 'mim', ('MIM horizontal-shaft impact crushers', 'كسارات صدمية أفقية العمود MIM'), ('220–1000 kW', '220–1000 كيلوواط'), ['max-feed-size', 'max-installed-power', 'weight']),
    auto(5, 2, 'pf-pfw', ('PF / PFW impact crushers', 'كسارات صدمية PF / PFW'), ('15–800 t/h', '15–800 طن/ساعة'), ['capacity', 'max-feed', 'power']),
    table('pf-mfd-additional', ('PF and MFD impact crushers – additional sizes', 'كسارات صدمية PF وMFD – مقاسات إضافية'), ('4–220 t/h', '4–220 طن/ساعة'),
          cols(['Rotor Ø × L (mm)', 'Feed opening (mm)', 'Max. feed size (mm)', 'Discharge size (mm)', 'Capacity (t/h)', 'Power (kW)', 'Weight (t)']),
          [(None, 'PF-0504', None, '500 × 400', '320×500', '100', '< 20', '4–8', '7.5', '1.6'), (None, 'PF-0807', None, '800 × 700', '400×730', '100', '< 40', '15–30', '22', '3.5'),
           (None, 'PF-1108', None, '1100 × 850', '400×1080', '300', '< 50', '60–100', '110', '13.5'), (None, 'PF-1310', None, '1300 × 1050', '490×1170', '400', '< 20', '120–220', '160', '24.3'),
           (None, 'MFD-20', None, '750 × 500', None, '200', '< 15', '8–20', '30', '1.9')],
          intro=('For medium-hard, non-abrasive ores.', 'للخامات متوسطة الصلابة غير الكاشطة.'), code='BX-0033-01-005', key_rows=['capacity', 'discharge-size', 'power']),
], type_label=('Series', 'السلسلة'))

# p6 C-series ------------------------------------------------------------------------------------------------
F['c-series-jaw-gyratory-impact-crushers'] = family('c-series-jaw-gyratory-impact-crushers', CAT, [
    table('c-jaw', ('C-series jaw crushers', 'كسارات فكية من السلسلة C'), ('80–1510 t/h', '80–1510 طن/ساعة'),
          cols(['Feed opening (mm)', 'Max. feed size (mm)', 'Discharge opening (mm)', 'Capacity (t/h)', 'Power (kW)']),
          [(None, m, None, *v) for m, *v in [
              ('C80', '520 × 800', '420', '60–150', '80–290', '75'), ('C100', '760 × 1000', '650', '70–200', '140–400', '110'),
              ('C106', '700 × 1060', '600', '70–200', '140–420', '110'), ('C110', '850 × 1100', '720', '80–200', '160–550', '160'),
              ('C120', '870 × 1200', '740', '100–200', '200–650', '160'), ('C125', '950 × 1250', '800', '100–250', '230–760', '160'),
              ('C145', '1100 × 1450', '920', '125–275', '320–950', '200'), ('C160', '1200 × 1600', '1020', '150–300', '410–1150', '250'),
              ('C200', '1500 × 2000', '1200', '175–300', '610–1510', '400'), ('CJ6310', '630 × 1000', '580', '80–180', '100–195', '75'),
              ('CJ8711', '870 × 1100', '720', '85–220', '130–360', '110'), ('CJ1113', '1100 × 1300', '940', '120–260', '360–780', '160'),
              ('CJ1216', '1200 × 1600', '1050', '165–320', '450–1100', '220')]],
          code='BX-0018-03-001', key_rows=['capacity', 'feed-opening', 'power']),
    table('gyratory-impact', ('Gyratory and impact crushers', 'الكسارات الدوّارة والصدمية'), ('15–1720 t/h', '15–1720 طن/ساعة'),
          [('models', 'Models', 'الموديلات'), ('capacity', 'Capacity (t/h)', 'الطاقة (طن/ساعة)'), ('max-feed-size', 'Max. feed size (mm)', 'أقصى حجم تغذية (مم)'), ('power', 'Power (kW)', 'القدرة (كيلوواط)')],
          [('BX-0018-03-008', 'PXZ gyratory crusher', 'كسارة دوّارة PXZ', 'PXZ0710, PXZ0909, PXZ0913, PXZ0917, PXZ1216, PXZ1221', '310–1720', '580–1000', '132–355'),
           ('BX-0018-03-006', 'P6S hydraulic impact crusher', 'كسارة صدمية هيدروليكية P6S', 'P6S1010, P6S1210, P6S1214, P6S1315, P6S1317, P6S1420, P6S1520, P6S1620', '100–700', '400–1200', '90–500'),
           ('BX-0018-03-007', 'PF impact crusher', 'كسارة صدمية PF', 'PF-1007, PF-1010, PF-1210, PF-1214, PF-1315, PF-1318, PF-1320, PF-1520, PF-1620, PF-1820', '15–800', '250–700', '37–710')],
          unit={'ar': ['سلسلة واحدة', 'سلسلتان', 'سلاسل'], 'en': ['series', 'series']}),
], type_label=('Series', 'السلسلة'))

# p7 hydraulic cone -------------------------------------------------------------------------------------------
F['hydraulic-cone-crushers'] = family('hydraulic-cone-crushers', CAT, [
    auto(7, 0, 'mhp', ('MHP multi-cylinder hydraulic cone crushers', 'كسارات مخروطية هيدروليكية متعددة الأسطوانات MHP'), ('50–1220 t/h', '50–1220 طن/ساعة')),
    auto(7, 1, 'mgp', ('MGP single-cylinder hydraulic cone crushers', 'كسارات مخروطية هيدروليكية أحادية الأسطوانة MGP'), ('40–1060 t/h', '40–1060 طن/ساعة')),
], type_label=('Series', 'السلسلة'))

# p8 single-cylinder cone -------------------------------------------------------------------------------------
F['single-cylinder-cone-crushers'] = family('single-cylinder-cone-crushers', CAT, [
    auto(8, 0, 'mcs-mch', ('MCS (secondary) and MCH (fine) cone crushers', 'كسارات مخروطية MCS (ثانوي) وMCH (ناعم)'), ('27–2181 t/h', '27–2181 طن/ساعة')),
], type_label=('Series', 'السلسلة'))

# p9 Symons & spring cone ------------------------------------------------------------------------------------
F['symons-spring-cone-crushers'] = family('symons-spring-cone-crushers', CAT, [
    auto(9, 0, 'cs', ('CS cone crushers (coarse, medium or fine cavity)', 'كسارات مخروطية CS (تجويف خشن أو متوسط أو ناعم)'), ('27–1814 t/h', '27–1814 طن/ساعة')),
    auto(9, 1, 'py', ('PY spring cone crushers (B coarse, Z medium, D fine)', 'كسارات مخروطية نابضية PY (B خشن، Z متوسط، D ناعم)'), ('5–1000 t/h', '5–1000 طن/ساعة')),
    # p32 (additional sizes)
    table('cs-additional', ('CS cone crushers – additional sizes', 'كسارات مخروطية CS – مقاسات إضافية'), ('', ''), SERIES,
          [('BX-0018-03-005', 'CS cone crusher (coarse, medium or fine cavity)', 'كسارة مخروطية CS (تجويف خشن أو متوسط أو ناعم)', 'CS130, CS200, CS240',
            ('Series range 27–725 t/h; max. feed 41–267 mm; 75–250 kW', 'نطاق السلسلة 27–725 طن/ساعة؛ أقصى تغذية 41–267 مم؛ 75–250 كيلوواط'))],
          unit={'ar': ['بند واحد', 'بندان', 'بنود'], 'en': ['line', 'lines']}),
], type_label=('Series', 'السلسلة'))

# p10 GP & HPS ------------------------------------------------------------------------------------------------
F['gp-hps-hydraulic-cone-crushers'] = family('gp-hps-hydraulic-cone-crushers', CAT, [
    table('gp-s', ('GP single-cylinder cone crushers – extra-coarse (S) cavity', 'كسارات مخروطية أحادية الأسطوانة GP – تجويف خشن جداً (S)'), ('80–1200 t/h', '80–1200 طن/ساعة'),
          cols(['Max. feed size (mm)', 'Discharge setting (mm)', 'Capacity (t/h)', 'Power (kW)']),
          [(None, m, None, *v) for m, *v in [('GP100S', '200', '25–50', '80–190', '90'), ('GP200S', '250', '30–70', '160–280', '160'),
                                             ('GP300S', '300', '35–75', '260–500', '250'), ('GP400S', '400', '50–95', '380–650', '315'),
                                             ('GP500S', '480', '60–115', '500–900', '355'), ('GP650S', '500', '70–120', '600–1050', '450'),
                                             ('GP800S', '560', '80–130', '710–1200', '630')]],
          code='BX-0018-03-003', key_rows=['capacity', 'discharge-setting', 'power']),
    table('standard', ('GP and HPS cone crushers – standard cavities', 'كسارات مخروطية GP وHPS – التجاويف القياسية'), ('Up to 1200 t/h', 'حتى 1200 طن/ساعة'),
          [('models', 'Models', 'الموديلات'), ('capacity', 'Capacity (t/h)', 'الطاقة (طن/ساعة)'), ('max-feed-size', 'Max. feed size (mm)', 'أقصى حجم تغذية (مم)'), ('power', 'Power (kW)', 'القدرة (كيلوواط)')],
          [('BX-0018-03-003', 'GP single-cylinder (coarse, medium, fine)', 'GP أحادية الأسطوانة (خشن، متوسط، ناعم)', 'GP100, GP200, GP300, GP400, GP500, GP650, GP800', ('up to 1200', 'حتى 1200'), '60–560', '90–630'),
           ('BX-0018-03-004', 'HPS multi-cylinder', 'HPS متعددة الأسطوانات', 'HPS200, HPS300, HPS400, HPS500, HPS800', '90–1200', None, '132–630')],
          unit={'ar': ['سلسلة واحدة', 'سلسلتان', 'سلاسل'], 'en': ['series', 'series']}),
], type_label=('Series', 'السلسلة'))

# p11 VSI -----------------------------------------------------------------------------------------------------
F['vertical-shaft-impact-crushers'] = family('vertical-shaft-impact-crushers', CAT, [
    auto(11, 0, 'mvs', ('MVS vertical shaft impact crushers', 'كسارات صدمية رأسية العمود MVS'), ('165–600 t/h', '165–600 طن/ساعة')),
    table('vsi', ('VSI5X and VSI sand-making crushers', 'كسارات صنع الرمل VSI5X وVSI'), ('Dual motors', 'محركان'),
          [('cap-cascade', 'Capacity – cascade & centre feed (t/h)', 'الطاقة – تغذية شلالية ومركزية (طن/ساعة)'), ('cap-centre', 'Capacity – full centre feed (t/h)', 'الطاقة – تغذية مركزية كاملة (طن/ساعة)'),
           ('feed', 'Feed size soft / hard (mm)', 'حجم التغذية لين / صلب (مم)'), ('rpm', 'Rotor speed (r/min)', 'سرعة الدوّار (دورة/دقيقة)'), ('motors', 'Motors (kW)', 'المحركات (كيلوواط)')],
          [('BX-0016-03-011', m, None, *v) if m.startswith('VSI5X') else ('BX-0016-03-012', m, None, *v) for m, *v in [
              ('VSI5X7615', '150–280', '70–140', '< 40 / < 35', '1700–1900', '2 × 75'), ('VSI5X8522', '240–380', '120–200', '< 45 / < 40', '1500–1700', '2 × 110'),
              ('VSI5X9532', '350–450', '180–290', '< 50 / < 45', '1330–1510', '2 × 160'), ('VSI5X1150', '413–644', '344–368', '< 55 / < 45', '1000–1300', '2 × 250'),
              ('VSI5X1263', '545–849', '454–498', '< 60 / < 50', '900–1200', '2 × 315'), ('VSI7611', '120–180', '60–90', '< 35 / < 30', '1700–1890', '2 × 55'),
              ('VSI8518', '200–260', '100–130', '< 40 / < 35', '1520–1690', '2 × 90'), ('VSI9526', '300–360', '150–190', '< 45 / < 40', '1360–1510', '2 × 132'),
              ('VSI1140', '450–520', '225–260', '< 50 / < 45', '1180–1310', '2 × 200'), ('VSI1145', '500–600', '250–360', '< 50 / < 45', '1180–1280', '2 × 220')]],
          intro=('Dual-pump hydraulic lubrication station with vibration monitoring (0.1–20 mm/s).', 'محطة تزييت هيدروليكية بمضختين مع مراقبة الاهتزاز (0.1–20 مم/ث).'),
          key_rows=['cap-cascade', 'feed', 'motors']),
], type_label=('Series', 'السلسلة'))

# p12 sand makers ---------------------------------------------------------------------------------------------
F['sand-makers-fine-crushers'] = family('sand-makers-fine-crushers', CAT, [
    table('sand-makers', ('Sand makers and roller crushers', 'صانعات الرمل والكسارات الأسطوانية'), ('10–800 t/h', '10–800 طن/ساعة'),
          [('models', 'Models', 'الموديلات'), ('capacity', 'Capacity (t/h)', 'الطاقة (طن/ساعة)'), ('feed', 'Feed size (mm)', 'حجم التغذية (مم)'),
           ('product', 'Product', 'المنتج'), ('power', 'Power (kW)', 'القدرة (كيلوواط)')],
          [('BX-0018-03-010', 'V6S sand making machine', 'صانعة رمل V6S', 'V6S-9832, V6S-1250, V6S-1263, V6S-1371', '236–800', ('< 45 hard, < 50 soft', '< 45 صلب، < 50 لين'), ('Sand', 'رمل'), ('2 × 160 to 2 × 355', 'من 2 × 160 إلى 2 × 355')),
           ('BX-0018-03-012', 'PFL vertical compound crusher', 'كسارة مركّبة رأسية PFL', 'PFL800, PFL1000, PFL1250, PFL1500, PFL1750, PFL2000', '10–180', '< 80–190', ('< 5 mm (80–95%)', '< 5 مم (80–95%)'), '30–250'),
           ('BX-0018-03-013', 'Hydraulic-opening sand making machine', 'صانعة رمل بفتح هيدروليكي', '800×400, 800×800, 1000×1000, 1200×1200, 1400×1400, 1600×1600, 1800×1800', '20–300', '< 120–190', ('< 5 mm', '< 5 مم'), '30–315'),
           ('BX-0018-03-009', '2PGY hydraulic roller crusher', 'كسارة أسطوانية هيدروليكية 2PGY', ('2PGY800×800 to 2PGY2000×1200', 'من 2PGY800×800 إلى 2PGY2000×1200'), '40–400', '≤ 40–120', ('Setting 1–20 mm', 'ضبط 1–20 مم'), ('2 × 30 to 2 × 315', 'من 2 × 30 إلى 2 × 315'))],
          unit={'ar': ['سلسلة واحدة', 'سلسلتان', 'سلاسل'], 'en': ['series', 'series']}),
], type_label=('Series', 'السلسلة'))

# p13 + p20 hammer --------------------------------------------------------------------------------------------
F['hammer-crushers'] = family('hammer-crushers', CAT, [
    auto(13, 0, 'pc', ('PC hammer crushers', 'كسارات مطرقية PC'), ('5–85 t/h', '5–85 طن/ساعة'), ['capacity', 'output-size', 'power']),
    auto(13, 1, 'pcz', ('PCZ heavy hammer crushers', 'كسارات مطرقية ثقيلة PCZ'), ('50–800 t/h', '50–800 طن/ساعة'), ['capacity', 'max-feed', 'power']),
    table('pc-additional', ('PC hammer crushers – additional sizes', 'كسارات مطرقية PC – مقاسات إضافية'), ('12–290 t/h', '12–290 طن/ساعة'),
          cols(['Max. feed size (mm)', 'Discharge size (mm)', 'Capacity (t/h)', 'Power (kW)', 'Weight (t)']),
          [(None, m, None, *v) for m, *v in [('PC600×600', '≤ 100', '≤ 15', '12–16', '37', '3.1'), ('PC600×1200', '≤ 350', '≤ 25', '15–20', '37', '3.8'),
                                             ('PC1200×1000', '≤ 200', '≤ 25', '75–150', '160', '12.5'), ('PC1200×1200', '≤ 200', '≤ 20', '80–160', '185', '14'),
                                             ('PC1250×1250', '≤ 200', '≤ 20', '80–160', '180', '14.5'), ('PC1400×1400', '≤ 250', '≤ 20', '120–170', '280', '17.2'),
                                             ('PC1600×1600', '≤ 350', '≤ 20', '220–290', '500', '32.5')]],
          code='BX-0033-01-003', key_rows=['capacity', 'discharge-size', 'power']),
], type_label=('Series', 'السلسلة'))

# p14 fine & double-rotor ---------------------------------------------------------------------------------------
F['fine-double-rotor-crushers'] = family('fine-double-rotor-crushers', CAT, [
    auto(14, 0, 'pcx', ('PCX high-efficiency fine crushers', 'كسارات ناعمة عالية الكفاءة PCX'), ('Output ≤ 3–5 mm (85%)', 'ناتج ≤ 3–5 مم (85%)')),
    auto(14, 1, 'pck', ('PCK reversible hammer crushers', 'كسارات مطرقية عكوسة PCK'), ('Product ≤ 15 mm', 'منتج ≤ 15 مم')),
    auto(14, 2, '2pc', ('2PC double-rotor hammer crushers', 'كسارات مطرقية مزدوجة الدوّار 2PC'), ('15–250 t/h · discharge ≤ 3 mm', '15–250 طن/ساعة · تفريغ ≤ 3 مم'),
         intro=('Discharge ≤ 3 mm, of which 0.5–0.075 mm 50%, 0.6–2 mm 35%, 2–3 mm 15%.', 'ناتج ≤ 3 مم، منه 50% بين 0.5 و0.075 مم، و35% بين 0.6 و2 مم، و15% بين 2 و3 مم.')),
], type_label=('Series', 'السلسلة'))

# p15 impact fine -------------------------------------------------------------------------------------------------
F['impact-fine-crushers'] = family('impact-fine-crushers', CAT, [
    auto(15, 0, 'pxj', ('PXJ high-efficiency impact fine crushers', 'كسارات صدمية ناعمة عالية الكفاءة PXJ'), ('Output 5–20 mm', 'ناتج 5–20 مم')),
], type_label=('Series', 'السلسلة'))

# p16 + p19 roller --------------------------------------------------------------------------------------------------
F['roller-crushers'] = family('roller-crushers', CAT, [
    auto(16, 0, '2pg', ('2PG / 2PGY double-roller crushers', 'كسارات مزدوجة الأسطوانة 2PG / 2PGY'), ('2–250 t/h', '2–250 طن/ساعة')),
    auto(16, 1, '4pg', ('4PG four-roll crushers', 'كسارات رباعية الأسطوانات 4PG'), ('Output 0.2–10 mm', 'ناتج 0.2–10 مم')),
    table('2pg-2pgc-additional', ('Double-roll crushers – smooth (2PG) and toothed (2PGC)', 'كسارات مزدوجة الأسطوانة – ملساء (2PG) ومسنّنة (2PGC)'), ('7–180 t/h', '7–180 طن/ساعة'),
          cols(['Roll Ø × L (mm)', 'Max. feed size (mm)', 'Discharge size (mm)', 'Capacity (t/h)', 'Power (kW)', 'Weight (t)']),
          [(None, m, None, *v) for m, *v in [('2PG400×500', '400 × 500', '25', '2–8', '7–11', '7.5 × 2', '1.7'), ('2PG610×500', '610 × 500', '75', '10–20', '15–50', '15 × 2', '3.5'),
                                             ('2PGC450', '450 × 500', '200', '0–100', '20–55', '11', '3.8'), ('2PGC600', '600 × 750', '600', '0–125', '60–125', '22', '6.7'),
                                             ('2PGC900', '900 × 900', '800', '0–125', '125–180', '30', '13.3')]],
          intro=('2PGC toothed rolls for coarse and medium crushing of brittle and soft ores.', 'أسطوانات 2PGC المسنّنة للتكسير الخشن والمتوسط للخامات الهشة واللينة.'),
          code='BX-0033-01-002', key_rows=['capacity', 'discharge-size', 'power']),
], type_label=('Series', 'السلسلة'))

# p17 mobile plants --------------------------------------------------------------------------------------------------
F['mobile-crushing-plants'] = family('mobile-crushing-plants', CAT, [
    table('crawler', ('Crawler mobile crushing plants (jaw, impact, cone)', 'محطات تكسير متنقلة على جنزير (فكية، صدمية، مخروطية)'), ('80–520 t/h', '80–520 طن/ساعة'),
          [('crusher', 'Crusher', 'الكسارة'), ('cpower', 'Crusher power (kW)', 'قدرة الكسارة (كيلوواط)'), ('screen', 'On-board screen', 'الغربال المدمج'),
           ('engine', 'Main engine (kW)', 'المحرك الرئيسي (كيلوواط)'), ('capacity', 'Capacity (t/h)', 'الطاقة (طن/ساعة)'), ('dims', 'Transport L×W×H (mm)', 'أبعاد النقل ط×ع×ا (مم)')],
          [(None, m, None, (c, {'Jaw': 'فكية', 'Impact': 'صدمية', 'Cone': 'مخروطية'}[c.split()[0]] + ' ' + c.split()[1]), *v) for m, c, *v in [
              ('YMC80', 'Jaw C80', '55', None, '163', '80–125', '12500×2850×3550'), ('YMC96', 'Jaw C96', '90', None, '225', '100–250', '14500×2950×3550'),
              ('YMC106', 'Jaw C106', '110', None, '310', '160–360', '15000×3000×3600'), ('YMC116', 'Jaw C116', '132', None, '310', '200–450', '15000×3200×3600'),
              ('YMC120', 'Jaw C120', '160', None, '403', '300–520', '15500×3200×3700'), ('YMCI10S', 'Impact CI1110', '160', '2YK1436', '330', '100–200', '16500×3400×3700'),
              ('YMCI12S', 'Impact CI1213', '200', '2YK1436', '440', '150–300', '17500×3580×3850'), ('YMCI12', 'Impact CI1213', '200', None, '440', '150–300', '14500×3350×3850'),
              ('YMCI13S', 'Impact CI1313', '250', '2YK1436', '440', '220–500', '18500×3650×3900'), ('YMCI13', 'Impact CI1313', '250', None, '440', '220–500', '17500×3450×3900'),
              ('YMH20S', 'Cone HP200', '160', '2YK1436', '310', '100–225', '17000×3300×3700'), ('YMH20', 'Cone HP200', '160', None, '310', '100–225', '16400×2950×3600'),
              ('YMH30S', 'Cone HP300', '250', '2YK1436', '448', '150–380', '17800×3500×3750'), ('YMH30', 'Cone HP300', '250', None, '448', '150–380', '17400×3300×3800'),
              ('YMH40S', 'Cone HP400', '280', '2YK1545', '574', '200–450', '22000×3750×4100'), ('YMH40', 'Cone HP400', '280', None, '574', '200–450', '20000×3500×3800')]],
          intro=('Hydraulic crawler chassis, diesel–electric dual drive, integrated feeder, crusher and discharge belts.', 'هيكل جنزير هيدروليكي، وإدارة مزدوجة ديزل وكهرباء، مع مغذٍّ وكسارة وسيور تفريغ مدمجة.'),
          code='BX-0016-03-001', key_rows=['crusher', 'capacity', 'engine']),
    table('wheel', ('Wheel-mounted mobile jaw crushing plants', 'محطات تكسير فكية متنقلة على عجلات'), ('40–400 t/h', '40–400 طن/ساعة'),
          [('feeder', 'Vibrating feeder', 'المغذي الهزاز'), ('jaw', 'Jaw crusher', 'الكسارة الفكية'), ('feed', 'Max. feed size (mm)', 'أقصى حجم تغذية (مم)'),
           ('belt', 'Belt conveyor', 'السير الناقل'), ('motors', 'Motors (kW)', 'المحركات (كيلوواط)'), ('capacity', 'Capacity (t/h)', 'الطاقة (طن/ساعة)'), ('dims', 'Overall dimensions (mm)', 'الأبعاد الكلية (مم)')],
          [(None, m, None, *v) for m, *v in [
              ('YDPZ57-8530', 'ZSW8530', 'PE500×750', '≤ 425', 'B650', '7.5 + 45 + 4', '40–130', '10000×2300×4020'),
              ('YDPZ80-8530', 'ZSW8530', 'C80', '≤ 400', 'B650', '7.5 + 55 + 4', '50–160', '10000×2300×4020'),
              ('YDPZ69-9638', 'ZSW9638', 'PE600×900', '≤ 500', 'B800', '11 + 55 + 4', '90–180', '11500×2300×4120'),
              ('YDPZ96-9638', 'ZSW9638', 'C96', '≤ 480', 'B800', '11 + 90 + 4', '60–160', '11600×2250×3710'),
              ('YDPZ75-1142', 'ZSW1142', 'PE750×1060', '≤ 630', 'B1000', '15 + 110 + 4', '110–380', '12500×2550×4570'),
              ('YDPZ106-1142', 'ZSW1142', 'CJ106', '≤ 580', 'B1000', '15 + 110 + 4', '150–300', '12850×2280×3950'),
              ('YDPZ116-1242', 'ZSW1142', 'CJ116', '≤ 680', 'B1000', '15 + 132 + 4', '200–400', '13000×2550×4150')]],
          code='BX-0016-04-001', key_rows=['jaw', 'capacity', 'motors']),
], type_label=('Series', 'السلسلة'))

# p18 tyre & crawler plants ---------------------------------------------------------------------------------------------
F['tyre-crawler-mounted-crushing-plants'] = family('tyre-crawler-mounted-crushing-plants', CAT, [
    table('plants', ('Mobile crushing and screening plants', 'محطات التكسير والغربلة المتنقلة'), ('50–650 t/h', '50–650 طن/ساعة'),
          [('models', 'Models', 'الموديلات'), ('capacity', 'Capacity (t/h)', 'الطاقة (طن/ساعة)'), ('feed', 'Max. feed size (mm)', 'أقصى حجم تغذية (مم)'),
           ('power', 'Power (kW)', 'القدرة (كيلوواط)'), ('w', 'Weight (t)', 'الوزن (طن)')],
          [('BX-0018-02-001', 'Jaw plant on tyres', 'محطة فكية على عجلات', 'MJ-E69, MJ-E75, MJ-E912, MJ-C106, MJ-C116', '90–650', '480–750', ('Genset 160–300 (option)', 'مولد 160–300 (اختياري)'), '36–83'),
           ('BX-0018-02-002', 'Impact plant on tyres', 'محطة صدمية على عجلات', 'MJ-F1210, MJ-F1214, MJ-F1315', '80–300', None, None, '39–52'),
           ('BX-0018-02-003', 'Cone plant on tyres', 'محطة مخروطية على عجلات', 'MJ-CS75, MJ-CS160, MJ-H200, MJ-H300, MJ-8010', '50–320', None, None, '34.5–50'),
           ('BX-0018-02-004', 'Combined plant on tyres', 'محطة مركّبة على عجلات', ('3 or 4 units working together', '3 أو 4 وحدات تعمل معاً'), None, None, None, None),
           ('BX-0018-02-005', 'Jaw plant on crawlers', 'محطة فكية على جنزير', 'MC-C106, MC-C116', '140–600', '650–680', '200–250', '45–58'),
           ('BX-0018-02-006', 'Impact plant on crawlers', 'محطة صدمية على جنزير', 'MC-F250S, MC-F350S', '150–400', '500–600', '400–500', '60–65'),
           ('BX-0018-02-007', 'Cone plant on crawlers', 'محطة مخروطية على جنزير', 'MC-H300S, MC-H400S', '100–450', '180–210', '350–500', '58–65'),
           ('BX-0018-02-008', 'Screening plant on crawlers', 'محطة غربلة على جنزير', 'MC-S6018, MC-S7020', '85–350', None, '50–65', '33–45')],
          unit={'ar': ['محطة واحدة', 'محطتان', 'محطات'], 'en': ['plant type', 'plant types']}),
], type_label=('Series', 'السلسلة'))
