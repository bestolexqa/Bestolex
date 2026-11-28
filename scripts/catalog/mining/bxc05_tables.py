"""BXC-05 Ed4 (Washing & gold concentration) model tables, catalogue pages 3–18. Typed from the page text and
checked against the page images where cells wrap (pages 5, 11, 13, 15). A table that carries two codes in the
catalogue (the same line in two supplier catalogues) gives each row the code whose model list covers it; every
code is in the supplier list under BXC-05."""
from lib import table, family
from bxc02_tables import U_LINES, U_TYPE

CAT = 'BXC-05 Ed4'
F = {}
U_DECK = {'ar': ['سطح واحد', 'سطحان', 'أسطح'], 'en': ['deck', 'decks']}
U_PLANT = {'ar': ['محطة واحدة', 'محطتان', 'محطات'], 'en': ['plant type', 'plant types']}
U_PRODUCT = {'ar': ['منتج واحد', 'منتجان', 'منتجات'], 'en': ['product', 'products']}
SERIES = [('models', 'Models', 'الموديلات'), ('data', 'Key data', 'أهم البيانات')]
C = lambda k, en, ar: (k, en, ar)
CAP = C('capacity', 'Capacity (t/h)', 'الطاقة (طن/ساعة)')
PWR = C('power', 'Power (kW)', 'القدرة (كيلوواط)')
FEED = C('feed', 'Feed size (mm)', 'حجم التغذية (مم)')
MAXFEED = C('max-feed', 'Max. feed size (mm)', 'أقصى حجم تغذية (مم)')
JIG = [C('chambers', 'Chambers', 'الحجرات'), FEED, C('stroke', 'Stroke (mm)', 'الشوط (مم)'), C('strokes', 'Strokes (r/min)', 'الأشواط (دورة/دقيقة)'), CAP, PWR]

# p3 trommel scrubbers & log washers ------------------------------------------------------------------------
F['trommel-scrubbers-log-washers'] = family('trommel-scrubbers-log-washers', CAT, [
    table('trommel', ('Trommel scrubbers (washing drum with screen section)', 'غسالات أسطوانية (أسطوانة غسيل بقسم غربلة)'), ('20–200 t/h', '20–200 طن/ساعة'),
          [C('drum', 'Drum Ø × length (mm)', 'قطر الأسطوانة × الطول (مم)'), C('aperture', 'Screen aperture (mm)', 'فتحة الغربال (مم)'),
           C('speed', 'Speed (r/min)', 'السرعة (دورة/دقيقة)'), FEED, CAP, PWR],
          [(None, 'YTXK1030', None, '1000 × 3000', '≤ 20', '27.9', '≤ 80', '20–30', '15'),
           (None, 'YTXK1230', None, '1200 × 3000', '≤ 25', '27.6', '≤ 100', '30–50', '22'),
           (None, 'YTXK1430', None, '1400 × 3000', '≤ 25', '27.6', '≤ 100', '50–80', '22'),
           (None, 'YTXK1545', None, '1500 × 4500', '≤ 25', '21', '≤ 160', '80–100', '30'),
           (None, 'YTXK1836', None, '1800 × 3600', '≤ 40', '20.6', '≤ 180', '100–120', '37'),
           (None, 'YTXK2265', None, '2200 × 6500', '≤ 50', '19', '≤ 230', '130–150', '45'),
           (None, 'YTXK2480', None, '2400 × 8000', '≤ 80', '18', '≤ 250', '150–200', '60')],
          intro=('Wear liners and drive arrangement chosen to suit the material.', 'تُختار بطانات التآكل وترتيب الإدارة حسب المادة.'),
          code='BX-0021-01-027', key_rows=['capacity', 'drum', 'power']),
    table('log', ('Log washers (twin-shaft paddle washers)', 'غسالات الطين (غسالات بمجاديف على عمودين)'), ('10–100 t/h', '10–100 طن/ساعة'),
          [C('tank', 'Tank L × W (mm)', 'الحوض الطول × العرض (مم)'), FEED, C('speed', 'Speed (r/min)', 'السرعة (دورة/دقيقة)'),
           C('incl', 'Inclination (°)', 'الميل (°)'), CAP, PWR],
          [(None, 'XK1156', None, '5600 × 1100', '50', '14', '20 / 24 / 27', '10–30', '11'),
           (None, 'XK1572', None, '7200 × 1500', '70', '11–14', '20 / 24 / 27', '20–60', '22'),
           (None, 'XK1876', None, '7600 × 1800', '70', '12', '24', '30–70', '30'),
           (None, 'XK2080', None, '8000 × 2000', '70', '12', '22', '40–80', '37'),
           (None, 'XK2284', None, '8400 × 2200', '70', '14', '17', '50–100', '55')],
          intro=('Breaks up clay and cemented gravel, including clay-rich alluvial gold ore.', 'يفكك الطين والحصى المتماسك، ومنه خام الذهب الغريني الغني بالطين.'),
          code='BX-0021-01-025', key_rows=['capacity', 'tank', 'power']),
])

# p4 spiral washers & attrition scrubbers ------------------------------------------------------------------
F['spiral-washers-attrition-scrubbers'] = family('spiral-washers-attrition-scrubbers', CAT, [
    table('spiral', ('Spiral washers', 'غسالات حلزونية'), ('Ø500–1500 mm', 'قطر 500–1500 مم'),
          [C('spiral-d', 'Spiral Ø (mm)', 'قطر الحلزون (مم)'), C('spirals', 'Spirals', 'عدد الحلزونات'), C('trough', 'Trough length (mm)', 'طول الحوض (مم)'), MAXFEED, PWR],
          [(None, 'SW500', None, '500', '1', '4500', '8', '5.5'), (None, 'SW750', None, '750', '1', '5500', '8', '7.5'),
           (None, 'SW750-2', None, '750', '2', '5500', '8', '7.5 × 2'), (None, 'SW1000', None, '1000', '1', '6500', '10', '15'),
           (None, 'SW1000-2', None, '1000', '2', '8500', '10', '15 × 2'), (None, 'SW1200', None, '1200', '1', '8500', '10', '18.5'),
           (None, 'SW1200-2', None, '1200', '2', '8500', '10', '18.5 × 2'), (None, 'SW1500', None, '1500', '1', '8500', '10', '30'),
           (None, 'SW1500-2', None, '1500', '2', '8500', '10', '30 × 2')],
          code='BX-0021-01-026', key_rows=['spiral-d', 'spirals', 'power']),
    table('attrition', ('Attrition scrubbers', 'خلايا الغسيل بالاحتكاك'), ('10–80 t/h', '10–80 طن/ساعة'),
          [C('cells', 'Cells', 'الخلايا'), MAXFEED, CAP, C('volume', 'Cell volume (m³)', 'حجم الخلية (م³)'), C('impeller', 'Impeller Ø (mm)', 'قطر الدافع (مم)'), PWR],
          [(None, 'CX1-1', None, '1', '10', '10–30', '1', '480', '15'), (None, 'CX1-2', None, '2', '10', '10–30', '1 × 2', '480 × 2', '15 × 2'),
           (None, 'CX2-1', None, '1', '10', '20–50', '2', '520', '30'), (None, 'CX2-2', None, '2', '10', '20–50', '2 × 2', '520 × 2', '30 × 2'),
           (None, 'CX4-1', None, '1', '10', '40–80', '4', '770', '55'), (None, 'CX4-2', None, '2', '10', '40–80', '4 × 2', '770 × 2', '55 × 2')],
          intro=('Rubber-lined cells for intensive surface cleaning of fine sand.', 'خلايا مبطنة بالمطاط لتنظيف أسطح الرمل الناعم تنظيفاً مكثفاً.'),
          code='BX-0021-02-013', key_rows=['capacity', 'cells', 'power']),
])

# p5 trommels & scrubbers – additional models ---------------------------------------------------------------
F['trommels-scrubbers-additional-models'] = family('trommels-scrubbers-additional-models', CAT, [
    table('series', ('Trommel screens, washing plants and scrubbers – additional models', 'غرابيل أسطوانية ومحطات غسيل وغسالات – موديلات إضافية'), ('5–800 t/h', '5–800 طن/ساعة'), SERIES,
          [('BX-0029-01-011', 'Stationary trommel screens (TW)', 'غرابيل أسطوانية ثابتة (TW)', 'TW1015, TW1020, TW1225, TW1530, TW1545, TW1848, TW2055, TW2265',
            ('50–800 t/h; feed ≤ 300–400 mm; product 0–100 mm; 3–30 kW; 2.2–12.8 t', '50–800 طن/ساعة؛ تغذية ≤ 300–400 مم؛ المنتج 0–100 مم؛ 3–30 كيلوواط؛ 2.2–12.8 طن')),
           ('BX-0029-01-012', 'Mobile trommel washing plants (GL)', 'محطات غسيل أسطوانية متنقلة (GL)', 'GL510, GL615, GL715, GL815, GL1020, GL1225, GL1530, GL1545, GL1848, GL2055',
            ('5–600 t/h; on 4–6 wheels; built-in water pump; diesel or electric drive; apertures < 3–20 mm; 0.8–8 t',
             '5–600 طن/ساعة؛ على 4–6 عجلات؛ مضخة ماء مدمجة؛ إدارة بالديزل أو الكهرباء؛ فتحات < 3–20 مم؛ 0.8–8 طن')),
           ('BX-0029-01-013', 'Rotary scrubbers (G)', 'غسالات دوّارة (G)', 'G1030, G1136, G1230, G1430, G1545, G1560, G1845, G1860, G2060, G2265',
            ('Drum Ø 1.0 × 3.0 to Ø 2.2 × 6.5 m; feed ≤ 100–230 mm; 30–180 t/h; 15–55 kW; 4.8–16.5 t; gear or tyre drive',
             'أسطوانة من 1.0 × 3.0 إلى 2.2 × 6.5 م؛ تغذية ≤ 100–230 مم؛ 30–180 طن/ساعة؛ 15–55 كيلوواط؛ 4.8–16.5 طن؛ إدارة بالتروس أو بالإطارات')),
           ('BX-0028-01-034', 'Agitation scrubbers (GJC)', 'غسالات بالخلط (GJC)', 'GJC×1.5, GJC×2.8, GJC×4.4',
            ('Effective volume 1.5 / 2.8 / 4.4 m³; 30 / 55 / 75 kW; 1459–6200 kg; ore up to 6 mm',
             'حجم فعال 1.5 / 2.8 / 4.4 م³؛ 30 / 55 / 75 كيلوواط؛ 1459–6200 كجم؛ خام حتى 6 مم'))],
          unit=U_LINES),
], type_label=('Series', 'السلسلة'))

# p6 jigs for alluvial gold ---------------------------------------------------------------------------------
F['alluvial-gold-jigs'] = family('alluvial-gold-jigs', CAT, [
    table('trapezoid', ('Trapezoid jigs – two rows, eight chambers', 'أجهزة جيج شبه منحرفة – صفّان وثماني حجرات'), ('3–40 t/h', '3–40 طن/ساعة'), JIG,
          [(None, '2LTC-6109/8T', None, '8', '0–10', '0–50', '0–300', '25–40', '2.2 × 4'),
           (None, '2LTC-366/8T', None, '8', '0–5', '0–50', '0–300', '3–6', '1.1 × 2')],
          intro=('2LTC-6109/8T jigging area 5.76 m². Stroke and stroke rate set separately for each chamber.',
                 'مساحة الجيج في 2LTC-6109/8T ‏5.76 م². يُضبط الشوط وعدد الأشواط لكل حجرة على حدة.'),
          code='BX-0021-01-001'),
    table('lta', ('LTA down-moving jigs', 'أجهزة جيج LTA بالحركة السفلية'), ('3–60 t/h', '3–60 طن/ساعة'), JIG,
          [(None, 'LTA55/2', None, '2', '0–5', '0–25', '0–350', '3–5', '1.5'), (None, 'LTA55/3', None, '3', '0–5', '0–25', '0–350', '3–5', '2.2'),
           (None, 'LTA1010/2', None, '2', '0–8', '0–25', '0–350', '8–10', '3'), (None, 'LTA1010/3', None, '3', '0–8', '0–25', '0–350', '8–10', '5.5'),
           (None, 'LTA1010/6', None, '6', '0–8', '0–25', '0–350', '10–20', '7.5'), (None, 'LTA1515/2', None, '2', '0–10', '0–50', '0–300', '20–25', '5.5'),
           (None, 'LTA1515/3', None, '3', '0–10', '0–50', '0–300', '20–30', '11'), (None, 'LTA1515/6', None, '6', '0–10', '0–50', '0–300', '40–60', '18.5')],
          code='BX-0021-01-002'),
    table('jt-ltp', ('JT saw-tooth-wave and LTP side-moving jigs', 'أجهزة جيج JT بموجة سن المنشار وLTP بالحركة الجانبية'), ('1–40 t/h', '1–40 طن/ساعة'), JIG,
          [('BX-0021-01-003', 'JT1070/2', None, '2', '0–5', '0–12', '0–170', '6–8', '3'),
           ('BX-0021-01-003', 'JT1515/2', None, '2', '0–8', '0–25', '0–150', '16–24', '4 × 2'),
           ('BX-0021-02-016', 'JT2020/2', None, '2', '0–10', None, None, '25–40', '5.5 × 2'),
           ('BX-0021-01-004', 'LTP34/2', None, '2', '0–12', '0–27', '0–340', '1–2', '1.1')],
          intro=('JT jigs suit flaky and fine gold. LTP34/2 is light and easy to move to remote sites.',
                 'أجهزة JT تناسب الذهب الرقائقي والناعم. وجهاز LTP34/2 خفيف وسهل النقل إلى المواقع البعيدة.')),
])

# p7 heavy-duty & laboratory jigs --------------------------------------------------------------------------
F['heavy-duty-laboratory-jigs'] = family('heavy-duty-laboratory-jigs', CAT, [
    table('coarse', ('Jigs for coarse ore', 'أجهزة جيج للخام الخشن'), ('10–100 t/h', '10–100 طن/ساعة'), JIG,
          [('BX-0021-01-005', 'AM30', None, '4', '10–30', '0–50', '0–160', '10–15', '3'),
           ('BX-0021-01-006', '2LTC912/4', None, '4', '10–25', '0–50', '0–280', '30–40', '11'),
           ('BX-0021-01-006', '2LTC912/4A', None, '4', '30–50', '0–100', '0–160', '30–40', '11'),
           ('BX-0021-01-007', 'FRT16-2', None, '2', '0–50', '0–90', '0–200', '40–60', '18.5'),
           ('BX-0021-02-018', 'FFD4-2', None, '2', '0–50', None, None, '40–60', '22'),
           ('BX-0021-02-018', 'FFD8-2', None, '2', '10–50', None, None, '80–100', '30')],
          intro=('Jigging area: FRT16-2 5.12 m², FFD4-2 4 m², FFD8-2 8 m². FFD jigs separate coarse and fine particles (0–50 mm) at the same time.',
                 'مساحة الجيج: FRT16-2 ‏5.12 م²، وFFD4-2 ‏4 م²، وFFD8-2 ‏8 م². أجهزة FFD تفصل الحبيبات الخشنة والناعمة (0–50 مم) في الوقت نفسه.')),
    table('lab', ('Laboratory jig', 'جهاز جيج مخبري'), ('100 kg/h', '100 كجم/ساعة'),
          [C('chambers', 'Chambers', 'الحجرات'), FEED, C('capacity-kg', 'Capacity (kg/h)', 'الطاقة (كجم/ساعة)'), PWR],
          [(None, 'LTP120', None, '1', '0–5', '100', '0.75')],
          intro=('For ore testing, pilot plants and training.', 'لاختبار الخام والمحطات التجريبية والتدريب.'),
          code='BX-0021-02-020'),
])

# p8 centrifugal concentrators -----------------------------------------------------------------------------
F['centrifugal-concentrators'] = family('centrifugal-concentrators', CAT, [
    table('bc', ('BC gold centrifugal concentrators', 'مركّزات الذهب الطاردة المركزية BC'), ('0.25–120 t/h', '0.25–120 طن/ساعة'),
          [CAP, FEED, C('density', 'Feed density (%)', 'كثافة التغذية (%)'), C('fluid', 'Fluidising water (t/h)', 'ماء التمييع (طن/ساعة)'),
           C('conc', 'Concentrate (kg/cycle)', 'المركّز (كجم/دورة)'), PWR, C('speed', 'Speed (r/min)', 'السرعة (دورة/دقيقة)'),
           C('water-p', 'Water pressure (MPa)', 'ضغط الماء (ميجاباسكال)'), C('weight', 'Weight (kg)', 'الوزن (كجم)')],
          [(None, 'BC19', None, '0.25–0.3', '0–3', '0–50', '1.5–2', '2–3', '0.75', '800', '0.04', '145'),
           (None, 'BC30', None, '2–3', '0–4', '0–50', '4–6', '10–20', '1.5', '600', '0.12', '400'),
           (None, 'BC60', None, '10–15', '0–6', '0–50', '10–15', '30–40', '4', '460', '0.25', '1300'),
           (None, 'BC80', None, '35–40', '0–6', '0–50', '45–55', '60–70', '11', '400', '0.35', '1500'),
           (None, 'BC100', None, '70–85', '0–6', '0–50', '60–70', '70–80', '18.5', '360', '0.4', '2000'),
           (None, 'BC120', None, '100–120', '0–6', '0–50', '70–80', '110–120', '22', '360', '0.5', '3000')],
          code='BX-0016-01-015', key_rows=['capacity', 'conc', 'power']),
    table('gxd', ('GXD centrifugal concentrators', 'مركّزات GXD الطاردة المركزية'), ('3–180 t/h', '3–180 طن/ساعة'),
          [CAP, MAXFEED, C('rec-feed', 'Recommended feed (mm)', 'التغذية الموصى بها (مم)'), C('density', 'Feed density (%)', 'كثافة التغذية (%)'),
           C('air', 'Air pressure (MPa)', 'ضغط الهواء (ميجاباسكال)'), C('motor', 'Motor (kW)', 'المحرك (كيلوواط)'),
           C('water', 'Water use (m³/t)', 'استهلاك الماء (م³/طن)'), C('batch', 'Concentrate per batch (kg)', 'المركّز في الدفعة (كجم)')],
          [(None, 'GXD30', None, '3–10', '6', '−2', '< 70', '0.5–0.7', '2.2', '4–6', '2–5'),
           (None, 'GXD50', None, '10–50', '6', '−2', '< 70', '0.5–0.7', '5.5', '10–15', '8–15'),
           (None, 'GXD80', None, '30–70', '6', '−2', '< 70', '0.5–0.7', '11', '16–25', '20–30'),
           (None, 'GXD100', None, '50–120', '6', '−2', '< 70', '0.5–0.7', '22', '25–45', '25–60'),
           (None, 'GXD120', None, '70–180', '6', '−2', '< 70', '0.5–0.7', '30', '40–65', '45–70')],
          intro=('60G, 90G and 120G versions; polyurethane inner cone; automatic control.', 'إصدارات 60G و90G و120G؛ مخروط داخلي من البولي يوريثان؛ تحكم آلي.'),
          code='BX-0021-02-023', key_rows=['capacity', 'batch', 'motor']),
])

# p9 spiral concentrators ----------------------------------------------------------------------------------
F['spiral-concentrators'] = family('spiral-concentrators', CAT, [
    table('5ll', ('5LL spiral chutes', 'مجاري حلزونية 5LL'), ('0.15–16 t/h', '0.15–16 طن/ساعة'),
          [C('outer', 'Outer Ø (mm)', 'القطر الخارجي (مم)'), C('pitch', 'Pitch (mm)', 'الخطوة (مم)'), C('starts', 'Starts per unit', 'المداخل في الوحدة'),
           FEED, C('density', 'Feed density (%)', 'كثافة التغذية (%)'), CAP, C('dims', 'Dimensions (mm)', 'الأبعاد (مم)')],
          [(None, '5LL-1500', None, '1500', '540/720', '2–4', '0.3–0.02', '25–55', '8–16', '1560×1560×5230'),
           (None, '5LL-1200', None, '1200', '900/720/540', '2–4', '0.3–0.03', '25–55', '4–6', '1360×1360×5230'),
           (None, '5LL-900', None, '900', '675/540/405', '2–4', '0.3–0.03', '25–55', '2–3', '1060×1060×4000'),
           (None, '5LL-600', None, '600', '450/360/270', '3', '0.2–0.02', '25–55', '0.8–1.2', '700×700×2600'),
           (None, '5LL-400', None, '400', '240/180', '2', '0.2–0.02', '25–55', '0.15–0.2', '460×460×1500')],
          code='BX-0016-01-014', key_rows=['capacity', 'outer', 'feed']),
    table('ql', ('QL spiral concentrators (polyurethane on fibreglass)', 'مركّزات حلزونية QL (بولي يوريثان على ألياف زجاجية)'), ('0.4–20 t/h per start', '0.4–20 طن/ساعة لكل مدخل'),
          [FEED, C('density', 'Feed density (%)', 'كثافة التغذية (%)'), C('pulp', 'Pulp per start (m³/h)', 'اللب لكل مدخل (م³/ساعة)'),
           C('cap-start', 'Capacity per start (t/h)', 'الطاقة لكل مدخل (طن/ساعة)')],
          [(None, 'QL20', None, '4–0.04', '20–45', '20–40', '7.5–20'), (None, 'QL16', None, '2–0.04', '20–45', '7–10', '2.5–4.5'),
           (None, 'QL15', None, '2–0.03', '20–45', '5–8', '2–4'), (None, 'QL12', None, '1–0.03', '20–45', '2.5–4.0', '1.2–2.0'),
           (None, 'QL11', None, '1–0.03', '20–45', '2.5–3.5', '1.2–1.6'), (None, 'QL10', None, '0.3–0.03', '20–45', '2–2.5', '1–1.2'),
           (None, 'QL9', None, '0.3–0.03', '20–40', '1.8–2', '0.9–1.2'), (None, 'QL7', None, '0.3–0.02', '20–40', '1.5–2', '0.7–0.9'),
           (None, 'QL6', None, '0.2–0.02', '20–40', '1–1.5', '0.6–0.8'), (None, 'QL4', None, '0.2–0.02', '20–40', '0.2–0.4', '0.4–0.5')],
          intro=('No power and no chemicals. Used for metallic ores and beach placer sands.', 'بلا كهرباء وبلا كيماويات. تُستخدم للخامات المعدنية ورمال الشواطئ الرسوبية.'),
          code='BX-0021-02-022', key_rows=['cap-start', 'feed', 'pulp']),
])

# p10 shaking tables ---------------------------------------------------------------------------------------
DECKS = [('Coarse sand deck', 'سطح الرمل الخشن'), ('Fine sand deck', 'سطح الرمل الناعم'), ('Slime deck', 'سطح الطين')]
F['shaking-tables'] = family('shaking-tables', CAT, [
    table('standard', ('Shaking table (coarse sand / fine sand / slime deck)', 'طاولة هزّازة (سطح رمل خشن / رمل ناعم / طين)'), ('10–60 t/d', '10–60 طن/يوم'),
          [C('deck', 'Deck L × W (mm)', 'السطح الطول × العرض (مم)'), MAXFEED, C('cap-d', 'Capacity (t/d)', 'الطاقة (طن/يوم)'),
           C('density', 'Feed density (%)', 'كثافة التغذية (%)'), C('stroke', 'Stroke (mm)', 'الشوط (مم)'), C('spm', 'Strokes per minute', 'الأشواط في الدقيقة'),
           C('slope', 'Cross slope (°)', 'الميل العرضي (°)'), C('area', 'Dressing area (m²)', 'مساحة الفرز (م²)'), C('riffle', 'Riffle profile', 'شكل الحواجز'),
           C('motor', 'Motor (kW)', 'المحرك (كيلوواط)')],
          [(None, DECKS[0][0], DECKS[0][1], '4450 × 1855 / 1546', '2', '30–60', '25–30', '24–29', '210–220', '3.5–5.0', '7.6', ('Rectangular', 'مستطيل'), '1.1'),
           (None, DECKS[1][0], DECKS[1][1], '4450 × 1855 / 1546', '0.5', '10–20', '20–25', '14–18', '270–280', '1.5–3.5', '7.6', ('Indented', 'مسنّن'), '1.1'),
           (None, DECKS[2][0], DECKS[2][1], '4450 × 1855 / 1546', '0.15', '15–25', '15–25', '12–16', '280–300', '1–2', '7.6', ('Triangular', 'مثلث'), '1.1')],
          intro=('Deck width: 1855 mm at drive end, 1546 mm at concentrate end. Eccentric-link drive.', 'عرض السطح 1855 مم عند طرف الإدارة و1546 مم عند طرف المركّز. إدارة بوصلة لامركزية.'),
          code='BX-0016-01-016', key_rows=['max-feed', 'cap-d', 'motor'], unit=U_DECK),
    table('6s', ('6S shaking table (composite deck)', 'طاولة هزّازة 6S (سطح مركّب)'), ('0.3–1.5 t/h', '0.3–1.5 طن/ساعة'),
          [C('area', 'Deck area (m²)', 'مساحة السطح (م²)'), C('deck', 'Deck L × W (mm)', 'السطح الطول × العرض (مم)'), MAXFEED, CAP,
           C('density', 'Feed density (%)', 'كثافة التغذية (%)'), C('stroke', 'Stroke (mm)', 'الشوط (مم)'), C('spm', 'Strokes per minute', 'الأشواط في الدقيقة'),
           C('water', 'Water (t/h)', 'الماء (طن/ساعة)'), C('slope', 'Cross slope (°)', 'الميل العرضي (°)'), C('motor', 'Motor (kW)', 'المحرك (كيلوواط)')],
          [(None, DECKS[0][0], DECKS[0][1], '7.6', '4500 × 1850 / 1520', '2', '1–1.5', '20–30', '16–22', '220', '0.7–1', '2.3–4.3', '1.1'),
           (None, DECKS[1][0], DECKS[1][1], '7.6', '4500 × 1850 / 1520', '0.5', '0.5–1', '18–25', '11–16', '250', '0.4–0.7', '1.3–3.3', '1.1'),
           (None, DECKS[2][0], DECKS[2][1], '7.6', '4500 × 1850 / 1520', '0.15', '0.3–0.5', '15–20', '8–16', '280', '0.4–0.7', '1–2', '1.1')],
          code='BX-0021-02-021', key_rows=['max-feed', 'capacity', 'motor'], unit=U_DECK),
    table('grease', ('Vibrating grease table for diamond recovery', 'طاولة شحم هزّازة لاستخلاص الألماس'), ('0.5–0.8 t/h', '0.5–0.8 طن/ساعة'),
          [C('speed', 'Speed (r/min)', 'السرعة (دورة/دقيقة)'), C('amp', 'Amplitude (mm)', 'السعة (مم)'), FEED, CAP, PWR],
          [(None, 'YGXK1020', None, '1100', '10', '0–6', '0.5–0.8', '3')],
          code='BX-0021-01-012'),
], type_label=('Model / deck', 'الموديل / السطح'))

# p11 gravity concentrators – additional models -------------------------------------------------------------
F['gravity-concentrators-additional-models'] = family('gravity-concentrators-additional-models', CAT, [
    table('series', ('Jigs, shaking tables, centrifuges and spirals – additional models', 'أجهزة جيج وطاولات هزّازة ومركّزات طاردة ومجارٍ حلزونية – موديلات إضافية'), ('', ''), SERIES,
          [('BX-0029-01-008', 'Sawtooth-wave jigs (JT)', 'أجهزة جيج بموجة سن المنشار (JT)',
            'JT0.57-1, JT1-1, JT1.5-2, JT2-2, JT3-1, JT4-2, JT5-2, JT1.5-2S, JT2-2S, JT3-2S, JT4-2S, JT5-2S, JT5-3, JT6-3S, JT8-3',
            ('Jigging area 0.57–8 m²; feed 6–40 mm; 1–30 t/h; 1.5 to 7.5 × 3 kW; 610–6300 kg; uses one-third to two-thirds of the water of a conventional jig',
             'مساحة الجيج 0.57–8 م²؛ تغذية 6–40 مم؛ 1–30 طن/ساعة؛ من 1.5 إلى 7.5 × 3 كيلوواط؛ 610–6300 كجم؛ يستهلك من ثلث إلى ثلثي ماء الجيج التقليدي')),
           ('BX-0029-01-009', '6-S shaking tables (smaller decks)', 'طاولات هزّازة 6-S (أسطح أصغر)', ('6-S 4.08, 6-S 1.95, 6-S 0.5 (laboratory)', '6-S 4.08 و6-S 1.95 و6-S 0.5 (مخبرية)'),
            ('Deck 0.5–4.08 m²; feed up to 2 mm; 1.1 kW (laboratory table 0.55 kW); decks with 46, 60, 88 or 110 riffles',
             'سطح 0.5–4.08 م²؛ تغذية حتى 2 مم؛ 1.1 كيلوواط (الطاولة المخبرية 0.55 كيلوواط)؛ أسطح بـ 46 أو 60 أو 88 أو 110 حواجز')),
           ('BX-0029-01-010', 'STLB centrifugal concentrators', 'مركّزات طاردة STLB', ('STLB-70 (additional size); automatic-discharge versions', 'STLB-70 (مقاس إضافي)؛ ونسخ بتفريغ آلي'),
            ('Series 0.25–120 t/h; feed 0–6 mm; back-flush water 1.5–80 t/h; 2–120 kg concentrate per batch; 0.75–22 kW; 145–3000 kg',
             'السلسلة 0.25–120 طن/ساعة؛ تغذية 0–6 مم؛ ماء عكسي 1.5–80 طن/ساعة؛ مركّز 2–120 كجم لكل دفعة؛ 0.75–22 كيلوواط؛ 145–3000 كجم')),
           ('BX-0028-01-027', 'Large spiral chute', 'مجرى حلزوني كبير', 'DL2000',
            ('Ø 2000 mm; feed 0.02–0.4 mm; no electric power', 'قطر 2000 مم؛ تغذية 0.02–0.4 مم؛ بلا طاقة كهربائية'))],
          unit=U_LINES),
], type_label=('Series', 'السلسلة'))

# p12 drum magnetic separators -----------------------------------------------------------------------------
DRUM = [C('drum', 'Drum Ø × length (mm)', 'قطر الأسطوانة × الطول (مم)'), CAP, C('field', 'Field (Gs)', 'شدة المجال (جاوس)'), PWR]
F['drum-magnetic-separators'] = family('drum-magnetic-separators', CAT, [
    table('wet', ('Wet drum magnetic separators (permanent magnet)', 'فواصل مغناطيسية أسطوانية رطبة (مغناطيس دائم)'), ('15–220 t/h', '15–220 طن/ساعة'), DRUM,
          [(None, 'CT618', None, '600 × 1800', '15–30', '800–6500', '2.2'), (None, 'CT918', None, '900 × 1800', '25–55', '800–6500', '4'),
           (None, 'CT924', None, '900 × 2400', '35–70', '800–6500', '4'), (None, 'CT1021', None, '1050 × 2100', '45–88', '800–6500', '5.5'),
           (None, 'CT1024', None, '1050 × 2400', '52–100', '800–6500', '5.5'), (None, 'CT1230', None, '1200 × 3000', '80–150', '800–6500', '7.5'),
           (None, 'CT1530', None, '1500 × 3000', '90–170', '800–6500', '11'), (None, 'CT1540', None, '1500 × 4000', '115–220', '800–6500', '15')],
          code='BX-0021-01-009'),
    table('dry', ('Dry drum magnetic separators', 'فواصل مغناطيسية أسطوانية جافة'), ('10–250 t/h', '10–250 طن/ساعة'), DRUM,
          [(None, 'GCT918', None, '900 × 1800', '10–30', '800–6500', '5.5'), (None, 'GCT924', None, '900 × 2400', '20–45', '800–6500', '5.5'),
           (None, 'GCT1021', None, '1050 × 2100', '50–60', '800–6500', '7.5'), (None, 'GCT1024', None, '1050 × 2400', '60–80', '800–6500', '7.5'),
           (None, 'GCT1230', None, '1200 × 3000', '80–100', '800–6500', '11'), (None, 'GCT1530', None, '1500 × 3000', '150–200', '800–6500', '18.5'),
           (None, 'GCT1540', None, '1500 × 4000', '200–250', '800–6500', '18.5')],
          code='BX-0021-01-008'),
])

# p13 high-intensity magnetic separators -------------------------------------------------------------------
F['high-intensity-magnetic-separators'] = family('high-intensity-magnetic-separators', CAT, [
    table('roller-disc', ('High-intensity dry separators (roller and disc)', 'فواصل جافة عالية الشدة (أسطوانية وقرصية)'), ('0.1–35 t/h', '0.1–35 طن/ساعة'),
          [C('size', 'Roller / disc size (mm)', 'مقاس الأسطوانة / القرص (مم)'), C('field', 'Field', 'شدة المجال'), FEED, CAP, PWR],
          [('BX-0021-01-010', 'CTG160×800', None, '160 × 800', '1.2–1.5 T', '< 5', '3–5', '1.1 × 2'),
           ('BX-0021-01-010', 'CTG160×1200', None, '160 × 1200', '1.2–1.5 T', '< 5', '6–8', '1.5 × 2'),
           ('BX-0021-01-010', 'CTG160×1500', None, '160 × 1500', '1.2–1.5 T', '< 5', '8–10', '2.2 × 2'),
           ('BX-0021-01-010', 'CTG160×1800', None, '160 × 1800', '1.2–1.5 T', '< 5', '10–13', '3 × 2'),
           ('BX-0021-01-010', 'CTG400×800', None, '400 × 800', '1.2–1.5 T', '< 5', '15–20', '3 × 2'),
           ('BX-0021-01-010', 'CTG400×1200', None, '400 × 1200', '1.2–1.5 T', '< 5', '25–30', '5.5 × 2'),
           ('BX-0021-01-010', 'CTG400×1500', None, '400 × 1500', '1.2–1.5 T', '< 5', '30–35', '5.5 × 2'),
           ('BX-0021-02-024', '3PC-500 disc', 'قرصي 3PC-500', ('3 discs Ø500', '3 أقراص قطر 500'), '1000–16000 Gs', '2', '0.1–0.5', '1.1'),
           ('BX-0021-02-024', '3PC-600 disc', 'قرصي 3PC-600', ('3 discs Ø600', '3 أقراص قطر 600'), '1000–18000 Gs', '2', '0.12–0.8', '1.5')],
          intro=('For weakly magnetic minerals and iron removal, e.g. ilmenite, monazite, zircon, rutile and garnet in heavy-mineral concentrates.',
                 'للمعادن ضعيفة المغناطيسية وإزالة الحديد، مثل الإلمنيت والمونازيت والزركون والروتيل والعقيق في مركّزات المعادن الثقيلة.'),
          key_rows=['capacity', 'field', 'power']),
])

# p14 magnetic reclaimers & pulleys ------------------------------------------------------------------------
F['magnetic-reclaimers-pulleys'] = family('magnetic-reclaimers-pulleys', CAT, [
    table('series', ('Reclaimers & magnetic pulleys', 'مستردّات المعادن المغناطيسية والبكرات المغناطيسية'), ('50–2400 t/h', '50–2400 طن/ساعة'), SERIES,
          [('BX-0386-02-015', 'Pulse-discharge magnetic reclaimer YCMW', 'مستردّ مغناطيسي بالتفريغ النبضي YCMW',
            'YCMW-80-4, -80-6, -10-4, -10-6, -12-8, -12-10, -15-12, -15-14, -20-12, -20-14',
            ('Drum Ø800–2000 mm; 50–2400 t/h; NdFeB ring magnet; recovers magnetic minerals', 'أسطوانة قطر 800–2000 مم؛ 50–2400 طن/ساعة؛ مغناطيس حلقي NdFeB؛ يسترد المعادن المغناطيسية')),
           ('BX-0386-02-016', 'Permanent magnetic pulley & dry drum separator CTZ / CTDG', 'بكرة مغناطيسية دائمة وفاصل أسطواني جاف CTZ / CTDG',
            ('CTZ-32, -40, -50, -63, -80, -100, -125; CTDG series', 'CTZ-32 و-40 و-50 و-63 و-80 و-100 و-125؛ سلسلة CTDG'),
            ('Permanent-magnet head pulley and dry drum separator', 'بكرة رأس بمغناطيس دائم وفاصل أسطواني جاف'))],
          intro=('Magnetic pulleys replace the head pulley of a conveyor to pull out iron and magnetic minerals as the belt discharges.',
                 'تحل البكرة المغناطيسية محل بكرة رأس السير لسحب الحديد والمعادن المغناطيسية عند تفريغ السير.'),
          unit=U_LINES),
], type_label=('Series', 'السلسلة'))

# p15 mobile gold washing plants ---------------------------------------------------------------------------
F['mobile-gold-washing-plants'] = family('mobile-gold-washing-plants', CAT, [
    table('plants', ('Mobile gold washing plants', 'محطات غسيل الذهب المتنقلة'), ('5–100 t/h', '5–100 طن/ساعة'),
          [CAP, C('screen', 'Screening', 'الغربلة'), C('recovery', 'Recovery', 'الاستخلاص'), C('pump', 'Water pump', 'مضخة الماء'), C('data', 'Other data', 'بيانات أخرى')],
          [('BX-0029-01-001', 'Trommel & jig washing plant', 'محطة غربال أسطواني وجيج', '5–60',
            ('Trommel Ø500 / 600 / 800 / 1000 mm × 1000 / 1500 / 2000 mm; apertures 2, 3, 5, 6, 8, 10, 20 mm; single or double layer; motor 1.5–4 kW',
             'غربال أسطواني قطر 500 / 600 / 800 / 1000 مم × 1000 / 1500 / 2000 مم؛ فتحات 2 و3 و5 و6 و8 و10 و20 مم؛ طبقة أو طبقتان؛ محرك 1.5–4 كيلوواط'),
            ('Rectangular or ladder jig 0.57–4.86 m², motor 1.5–4 kW; sluice 1000 mm × 5000/6000 mm', 'جيج مستطيل أو سلّمي 0.57–4.86 م² بمحرك 1.5–4 كيلوواط؛ مجرى غسيل 1000 مم × 5000/6000 مم'),
            ('5–18.5 kW', '5–18.5 كيلوواط'),
            ('Feed hopper, grizzly bars optional; jig 3225×1550×2050 mm (varies by model)', 'قادوس تغذية مع قضبان اختيارية؛ الجيج 3225×1550×2050 مم (يختلف حسب الموديل)')),
           ('BX-0029-01-002', 'Vibrating-screen washing plant', 'محطة غربال اهتزازي', '15–20',
            ('Two-tier 1800×900 mm screen, diesel drive; top / bottom mesh 25 mm / 8 mm', 'غربال بطبقتين 1800×900 مم بإدارة ديزل؛ شبك علوي / سفلي 25 مم / 8 مم'),
            ('Sluice with gold carpet', 'مجرى غسيل بسجادة ذهب'),
            ('Diesel, 50 m lay-flat hose', 'ديزل، خرطوم مسطح 50 م'),
            ('Hopper 2–3 m³ with 140 mm grizzly; manual jacks at each wheel; 2300 kg; 2800×1200×3000 mm', 'قادوس 2–3 م³ بقضبان 140 مم؛ رافعات يدوية عند كل عجلة؛ 2300 كجم؛ 2800×1200×3000 مم')),
           ('BX-0029-01-014', 'Integrated ore washing machine', 'وحدة غسيل الخام المتكاملة', ('30, 50 and 100', '30 و50 و100'),
            ('Rotary scrubber and vibrating screen', 'غسالة دوّارة وغربال اهتزازي'), None,
            ('Built in', 'مدمجة'),
            ('Feed hopper, scrubber, screen and pump in one unit for clayey alluvial gold and river-sand deposits', 'قادوس وغسالة وغربال ومضخة في وحدة واحدة لرواسب الذهب الغريني الطينية ورمال الأنهار'))],
          key_rows=['capacity', 'screen', 'recovery'], unit=U_PLANT),
])

# p16 sluice boxes, gold carpets & pans --------------------------------------------------------------------
F['sluice-boxes-gold-carpets-pans'] = family('sluice-boxes-gold-carpets-pans', CAT, [
    table('sluice', ('Sluice boxes and gold carpets', 'مجاري الغسيل وسجاد الذهب'), ('0.5×3–1×10 m', '0.5×3–1×10 م'),
          [C('sizes', 'Standard sizes (width × length, m)', 'المقاسات القياسية (العرض × الطول، م)'), C('notes', 'Notes', 'ملاحظات')],
          [('BX-0029-01-004', 'Sluice box', 'مجرى غسيل', '0.5×3 · 1×5 · 1×6 · 1×8 · 1×10',
            ('Steel trough with riffle frames; often three sets per plant', 'مجرى فولاذي بإطارات حواجز؛ غالباً ثلاث مجموعات لكل محطة')),
           ('BX-0029-01-003', 'Gold carpet (sluice mat)', 'سجادة ذهب (حصيرة المجرى)', '0.5×3 · 1×5 · 1×6 · 1×8 · 1×10',
            ('Eight-leaf artificial turf; traps fine gold', 'عشب صناعي بثماني ورقات؛ يحجز الذهب الناعم'))],
          unit=U_PRODUCT),
    table('pans', ('Gold pans', 'أطباق غسل الذهب'), ('1 kg/h', '1 كجم/ساعة'),
          [C('material', 'Material', 'المادة'), C('height', 'Height (cm)', 'الارتفاع (سم)'), C('top', 'Top Ø (cm)', 'القطر العلوي (سم)'),
           C('base', 'Base Ø (cm)', 'قطر القاعدة (سم)'), C('weight', 'Net weight (g)', 'الوزن الصافي (جم)'), C('cap-kg', 'Capacity (kg/h)', 'الطاقة (كجم/ساعة)')],
          [(None, 'Black', 'أسود', 'PP', '8', '38.5', '17.2', '340', '1'),
           (None, 'Light blue', 'أزرق فاتح', 'PP', '8', '36.5', '20', '275', '1'),
           (None, 'Dark blue', 'أزرق داكن', 'PP', '8', '36.5', '20', '275', '1')],
          intro=('Polypropylene pans with concentric riffles 0.25 mm deep, for sampling and hand panning; pair with a small shovel.',
                 'أطباق من البولي بروبلين بحواجز دائرية بعمق 0.25 مم، لأخذ العينات والغسل اليدوي؛ تُستخدم مع مجرفة صغيرة.'),
          code='BX-0029-01-005', unit={'ar': ['لون واحد', 'لونان', 'ألوان'], 'en': ['colour', 'colours']}),
], type_label=('Product', 'المنتج'))

# p17 dredgers ---------------------------------------------------------------------------------------------
F['dredgers'] = family('dredgers', CAT, [
    table('types', ('Dredger types', 'أنواع الكراكات'), ('200–7000 m³/h', '200–7000 م³/ساعة'),
          [C('models', 'Models', 'الموديلات'), C('capacity', 'Capacity', 'الطاقة'), C('depth', 'Depth', 'العمق'), C('data', 'Key data', 'أهم البيانات')],
          [('BX-0183-01-001', 'Cutter suction', 'كراكة قطع وشفط', ('JLCSD-200 … JLCSD-700 (7)', 'JLCSD-200 … JLCSD-700 ‏(7)'), ('500–7000 m³/h', '500–7000 م³/ساعة'), ('1–20 m', '1–20 م'),
            ('Pipe Ø200–750 mm; 160–3500 kW; modular, dismountable', 'أنبوب قطر 200–750 مم؛ 160–3500 كيلوواط؛ وحدات قابلة للفك')),
           ('BX-0183-01-002', 'Bucket wheel', 'كراكة بعجلة دلاء', None, None, None,
            ('Wheel cuts hard soil, clay and compacted sand; cutter-suction platform', 'العجلة تقطع التربة الصلبة والطين والرمل المضغوط؛ على منصة قطع وشفط')),
           ('BX-0183-01-003', 'Bucket chain', 'كراكة بسلسلة دلاء', None, ('200 m³/h', '200 م³/ساعة'), ('6–7 m', '6–7 م'),
            ('Hull 19.6×6.2×1.5 m; diesel, generator or electric; sand, gravel and alluvial gold', 'بدن 19.6×6.2×1.5 م؛ ديزل أو مولد أو كهرباء؛ للرمل والحصى والذهب الغريني')),
           ('BX-0183-01-005', 'Mining & screening', 'كراكة تعدين وغربلة', None, ('500–3000 m³/day', '500–3000 م³/يوم'), None,
            ('Dredging and screening in one unit', 'تجريف وغربلة في وحدة واحدة')),
           ('BX-0183-01-006', 'Auger head suction', 'كراكة شفط برأس حلزوني', None, ('200–2000 m³/h', '200–2000 م³/ساعة'), None,
            ('Small, easy to transport, remote operation; ponds and channels', 'صغيرة وسهلة النقل وتُشغّل عن بعد؛ للبرك والقنوات'))],
          intro=('Specifications are for guidance; each dredger is configured to the project.', 'المواصفات للاسترشاد؛ تُهيّأ كل كراكة حسب المشروع.'),
          key_rows=['capacity', 'depth', 'data'], unit=U_TYPE),
], type_label=('Type', 'النوع'), unit=U_TYPE)

# p18 amphibious dredgers & excavators ---------------------------------------------------------------------
F['amphibious-dredgers-excavators'] = family('amphibious-dredgers-excavators', CAT, [
    table('multifunction', ('Amphibious multifunction dredgers', 'كراكات برمائية متعددة المهام'), ('5–6 m', '5–6 م'),
          [C('under', 'Undercarriage', 'الهيكل السفلي'), C('size', 'Overall size (m)', 'الأبعاد الكلية (م)'), C('engine', 'Engine / power', 'المحرك / القدرة'),
           C('weight', 'Weight', 'الوزن'), C('depth', 'Dredging depth', 'عمق التجريف'), C('arm', 'Arm length', 'طول الذراع'),
           C('pump', 'Pump flow', 'تدفق المضخة'), C('discharge', 'Discharge distance', 'مسافة الضخ'), C('fuel', 'Fuel tank', 'خزان الوقود')],
          [('BX-0183-02-001', 'JL-AMD220', None, ('Pontoon hull, 4 spuds, own propulsion', 'بدن عائم، 4 أوتاد تثبيت، دفع ذاتي'), ('14.7×3.4×3.3 (transport)', '14.7×3.4×3.3 (للنقل)'),
            ('Diesel', 'ديزل'), ('26 t', '26 طن'), ('6 m', '6 م'), None, ('500 m³/h', '500 م³/ساعة'), ('Up to 1.2 km', 'حتى 1.2 كم'), ('1000 L', '1000 لتر')),
           ('BX-0183-02-002', 'JL-AME450', None, ('Multi-pontoon with crawler', 'عوامات متعددة بجنزير'), '13.5×3.5×3.8', ('269 kW', '269 كيلوواط'), None, ('6 m', '6 م'), ('8 m', '8 م'), None, None, None),
           ('BX-0183-02-002', 'JL-AME200', None, ('Multi-pontoon with crawler', 'عوامات متعددة بجنزير'), '12.5×4.4×3.6', ('179 kW', '179 كيلوواط'), None, ('5 m', '5 م'), ('6 m', '6 م'), None, None, None)],
          intro=('Change tools on site: bucket, cutter-suction pump, rake, piling, clamshell or weed cutter.', 'تُبدّل الأدوات في الموقع: دلو، أو مضخة قطع وشفط، أو مشط، أو دق خوازيق، أو ملقط، أو قاطع أعشاب.'),
          key_rows=['depth', 'engine', 'pump']),
    table('excavators', ('Amphibious excavators', 'حفارات برمائية'), ('6.1–76.2 t', '6.1–76.2 طن'),
          [C('weight-kg', 'Weight (kg)', 'الوزن (كجم)'), C('bucket', 'Std. bucket (m³)', 'الدلو القياسي (م³)'),
           C('dig', 'Max digging depth (mm)', 'أقصى عمق حفر (مم)'), C('reach', 'Max reach (mm)', 'أقصى مدى (مم)')],
          [(None, 'AME-4T', None, '6100', '0.22', '3220', '5955'),
           (None, 'AME-15T', None, '22800 / 24400', '0.65', '4630 / 9760', '8850 / 11700'),
           (None, 'AME-20T', None, '30700 / 32800', '1.0', '5970 / 11270', '9860 / 16150'),
           (None, 'AME-30T', None, '45400 / 47800', '1.8', '6500 / 14200', '10950 / 18600'),
           (None, 'AME-50T', None, '70900 / 76200', '2.61', '6380 / 19000', '11440 / 23500')],
          intro=('Two values: standard / long-reach work equipment. Weight without side pontoons or spuds.',
                 'قيمتان: معدات العمل القياسية / بعيدة المدى. الوزن دون العوامات الجانبية أو أوتاد التثبيت.'),
          code='BX-0183-02-004', key_rows=['weight-kg', 'bucket', 'dig']),
])
