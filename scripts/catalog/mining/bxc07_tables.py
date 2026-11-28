"""BXC-07 Ed5 (Pumps & slurry handling) model tables, catalogue pages 3–19. Clean tables from the page text; tables
whose cells wrap typed from the page images. Rows that carry several codes in the catalogue (hose groups, page 14)
are split by code using the supplier list names; where two suppliers' codes share one row (none here) the first is
used. Every code is in the supplier list under BXC-07."""
from lib import table, family
from bxc02_tables import U_LINES

CAT = 'BXC-07 Ed5'
F = {}
U_PRODUCT = {'ar': ['منتج واحد', 'منتجان', 'منتجات'], 'en': ['product', 'products']}
U_HOSE = {'ar': ['خرطوم واحد', 'خرطومان', 'خراطيم'], 'en': ['hose type', 'hose types']}
SERIES = [('models', 'Sizes / models', 'المقاسات والموديلات'), ('data', 'Key data', 'أهم البيانات')]
C = lambda k, en, ar: (k, en, ar)
CAP = C('capacity', 'Capacity (m³/h)', 'الطاقة (م³/ساعة)')
HEAD = C('head', 'Head (m)', 'الرفع (م)')
SPEED = C('speed', 'Speed (r/min)', 'السرعة (دورة/دقيقة)')
EFF = C('eff', 'Max. efficiency (%)', 'أقصى كفاءة (%)')
IMP = C('impeller', 'Impeller Ø (mm)', 'قطر الدفّاعة (مم)')
PWR = C('power', 'Max. power (kW)', 'أقصى قدرة (كيلوواط)')


def series(tid, label, key, rows, intro=None, unit=U_LINES, cols=SERIES):
    return table(tid, label, key, cols, rows, intro=intro, unit=unit)


# p3 horizontal slurry pumps ---------------------------------------------------------------------------------
F['horizontal-slurry-pumps'] = family('horizontal-slurry-pumps', CAT, [
    table('dhr', ('Heavy-duty slurry pumps DH(R)', 'مضخات لب ثقيلة DH(R)'), ('10.8–5400 m³/h', '10.8–5400 م³/ساعة'),
          [C('sizes', 'Sizes', 'المقاسات'), CAP, HEAD, SPEED, PWR, IMP],
          [(None, 'DH (metal) / DHR (rubber-lined)', 'DH معدنية / DHR مبطنة بالمطاط',
            '40X25DH(R)-B, 50X40DH(R)-B, 75X50DH(R)-C, 100X75DH(R)-C, 150X100DH(R)-D, 200X150DH(R)-R, 250X200DH(R)-ST, 300X250DH(R)-ST, 350X300DH(R)-ST, 400X350DH-TU, 500X450DH-TU',
            '10.8–5400', '5.5–68', '200–3800', '15–1200', '152–1370')],
          intro=('Wear-resistant alloy or rubber liners and impellers.', 'بطانات ودفّاعات من سبيكة مقاومة للتآكل أو من المطاط.'),
          code='BX-0038-01-001', key_rows=['capacity', 'head', 'power'], unit=U_LINES),
    table('dm', ('Slurry pumps DM(R)', 'مضخات لب DM(R)'), ('2.34–2800 m³/h', '2.34–2800 م³/ساعة'),
          [PWR, CAP, HEAD, SPEED, EFF, IMP],
          [(None, '25X20DM-A', None, '7.5', '2.34–10.8', '6–37', '1400–3000', '30', '152.4'),
           (None, '75X50DM-B', None, '15', '16.2–76', '9–44', '1400–2800', '55', '190'),
           (None, '100X75DM-C', None, '30', '18–151', '4–45', '900–2400', '57', '229'),
           (None, '150X100DM-D', None, '60', '50–252', '7–46', '800–1800', '60', '305'),
           (None, '200X150DM-E', None, '120', '115–486', '12–51.5', '800–1500', '65', '381'),
           (None, '250X200DM-E', None, '120', '234–910', '9.5–40', '600–1100', '64', '457'),
           (None, '300X250DM-S', None, '120', '396–1425', '8–30', '500–800', '77', '550'),
           (None, '350X300DM-S', None, '560', '468–2538', '8–60', '400–950', '79', '653'),
           (None, '400X350DM-S', None, '560', '650–2800', '10–59', '400–840', '81', '736')],
          intro=('Clear-water performance, metal (M) liner and impeller. Also: 450X400DM(R)-ST, 500X450DM(R)-ST and 650X550DM(R)-TU, with rubber-lined versions.',
                 'الأداء بالماء النقي ببطانة ودفّاعة معدنية (M). وتتوفر أيضاً 450X400DM(R)-ST و500X450DM(R)-ST و650X550DM(R)-TU، مع نسخ مبطنة بالمطاط.'),
          code='BX-0038-01-002', key_rows=['capacity', 'head', 'power']),
])

# p4 gravel & dredge pumps ----------------------------------------------------------------------------------
F['gravel-dredge-pumps'] = family('gravel-dredge-pumps', CAT, [
    table('dg', ('Gravel pumps DG / DGH', 'مضخات الحصى DG / DGH'), ('36–3816 m³/h', '36–3816 م³/ساعة'),
          [CAP, HEAD, SPEED, EFF, C('ports', 'Suction / discharge Ø (mm)', 'قطر السحب / الطرد (مم)'), C('particle', 'Max. particle (mm)', 'أكبر حبيبة (مم)'), C('weight', 'Weight (kg)', 'الوزن (كجم)')],
          [(None, 'DG150X100-D', None, '36–252', '3.5–51', '600–1400', '30–50', '150 / 100', '82', '460'),
           (None, 'DG200X150-E', None, '137–576', '10–48', '800–1400', '50–60', '200 / 150', '127', '1120'),
           (None, 'DG250X200-S', None, '216–979', '13–50', '500–1000', '45–65', '250 / 200', '178', '2285'),
           (None, 'DG300X250-G', None, '360–1512', '11–58', '400–850', '50–70', '300 / 250', '220', '4450'),
           (None, 'DG350X300-G', None, '504–3168', '6–66', '300–700', '60–68', '350 / 300', '240', '5400'),
           (None, 'DG450X400-T', None, '864–3816', '9–48', '250–500', '60–72', '450 / 400', '254', '10800'),
           (None, 'DG250X200H-S', None, '396–1296', '10–80', '500–950', '60–72', '250 / 200', '180', '3188'),
           (None, 'DG300X400H-T', None, '612–2232', '28–78', '350–700', '60–72', '300 / 250', '210', '4638'),
           (None, 'DG400X350H-TU', None, '720–3600', '20–72', '300–500', '60–72', '400 / 350', '230', '12250')],
          intro=('H = high-head models. Model names as listed by the manufacturer.', 'H = موديلات رفع عالٍ. أسماء الموديلات كما يذكرها المصنّع.'),
          code='BX-0038-01-003', key_rows=['capacity', 'head', 'particle']),
    table('tzw', ('Dredge pumps', 'مضخات الكراكات'), ('750–25000 m³/h', '750–25000 م³/ساعة'),
          [C('sizes', 'Sizes', 'المقاسات'), CAP, HEAD, C('outlet', 'Outlet (mm)', 'المخرج (مم)')],
          [(None, 'TZW dredge pump', 'مضخة كراكات TZW', '200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000', '750–25000', '20–85', '200–1000')],
          code='BX-0022-01-007', unit=U_LINES),
])

# p5 vertical sump pumps ------------------------------------------------------------------------------------
MET, RUB = ('Metal', 'معدنية'), ('Rubber', 'مطاطية')
F['vertical-sump-pumps'] = family('vertical-sump-pumps', CAT, [
    table('dv', ('Vertical sump pumps DV(R)', 'مضخات أحواض رأسية DV(R)'), ('18–1267 m³/h', '18–1267 م³/ساعة'),
          [C('liner', 'Liner', 'البطانة'), CAP, HEAD, SPEED, EFF, IMP],
          [(None, '40(L)DV', None, MET, '19–43', '4.5–28.5', '1000–2200', '40', '188'), (None, '40(L)DVR', None, RUB, '18–40', '4–26', '1000–2200', '40', '188'),
           (None, '65(L)DV', None, MET, '23–111', '5–29.5', '700–1500', '50', '280'), (None, '65(L)DVR', None, RUB, '23–105', '5.5–30.5', '500–1200', '51', '280'),
           (None, '100(L)DV', None, MET, '54–289', '5–35', '600–1200', '56', '370'), (None, '100(L)DVR', None, RUB, '65–285', '7.5–36', '600–1200', '62', '370'),
           (None, '150(L)DV', None, MET, '108–480', '8.5–40', '500–1000', '52', '450'), (None, '200(L)DV', None, MET, '189–891', '6.5–37', '400–850', '64', '520'),
           (None, '250(L)DV', None, MET, '261–1089', '7.5–33', '400–750', '60', '575'), (None, '300(L)DV', None, MET, '288–1267', '6.5–33', '350–700', '50', '610')],
          intro=('(L) = extended shaft for deep sumps. Cantilever design with no shaft seal.', '(L) = عمود ممدد للأحواض العميقة. تصميم معلّق بلا مانع تسرب للعمود.'),
          code='BX-0038-01-005', key_rows=['capacity', 'head', 'liner']),
    table('vsb', ('High-head vertical sump pumps', 'مضخات أحواض رأسية برفع عالٍ'), ('6–1057 m³/h', '6–1057 م³/ساعة'),
          [C('sizes', 'Sizes', 'المقاسات'), CAP, HEAD, C('outlet', 'Outlet (mm)', 'المخرج (مم)'), C('notes', 'Notes', 'ملاحظات')],
          [(None, 'VSB high-head sump pump', 'مضخة أحواض VSB برفع عالٍ', ('40VSB, 50VSB, 65VSB, 80VSB and larger, to 250 mm outlet', '40VSB و50VSB و65VSB و80VSB وأكبر، حتى مخرج 250 مم'),
            '6–1057', '2.4–80.5', '40–250',
            ('High-chrome parts; no shaft seal and no gland water; extended-shaft version for deep sumps', 'أجزاء عالية الكروم؛ بلا مانع تسرب للعمود وبلا ماء للحشوة؛ نسخة بعمود ممدد للأحواض العميقة'))],
          code='BX-0022-01-014', unit=U_LINES),
])

# p6 slurry, gravel & submersible – additional series --------------------------------------------------------
F['slurry-gravel-submersible-pumps-additional'] = family('slurry-gravel-submersible-pumps-additional', CAT, [
    series('series', ('Slurry, gravel, dredge and submersible pumps – additional series', 'مضخات لب وحصى وكراكات وغاطسة – سلاسل إضافية'), ('7–12000 m³/h', '7–12000 م³/ساعة'), [
        ('BX-0024-02-001', 'AM / AMH / MM horizontal slurry pumps', 'مضخات لب أفقية AM / AMH / MM', ('1.5/1B-AM to 20/18TU-AM (20 sizes)', 'من 1.5/1B-AM إلى 20/18TU-AM ‏(20 مقاساً)'),
         ('Cantilever; metal (M) or rubber (RU) liners and impellers; max. power 15–1200 kW; e.g. 3/2C-AM 39.6–86.4 m³/h, head 12–64 m; direct or belt drive',
          'معلّقة؛ بطانات ودفّاعات معدنية (M) أو مطاطية (RU)؛ أقصى قدرة 15–1200 كيلوواط؛ مثال 3/2C-AM ‏39.6–86.4 م³/ساعة ورفع 12–64 م؛ إدارة مباشرة أو بالسيور')),
        ('BX-0024-03-001', 'AMG / AMGH gravel and sand pumps', 'مضخات الحصى والرمل AMG / AMGH', ('6/4D-AMG to 16/14TU-AMGH (9 sizes)', 'من 6/4D-AMG إلى 16/14TU-AMGH ‏(9 مقاسات)'),
         ('Outlet 100–350 mm; 36–2800 m³/h; head 7–90 m; particles up to 82–241 mm; 60–1200 kW', 'مخرج 100–350 مم؛ 36–2800 م³/ساعة؛ رفع 7–90 م؛ حبيبات حتى 82–241 مم؛ 60–1200 كيلوواط')),
        ('BX-0024-03-002', 'AWN dredging pumps', 'مضخات كراكات AWN', ('200AWN to 1000AWN', 'من 200AWN إلى 1000AWN'),
         ('Outlet 200–1000 mm; 600–12000 m³/h; head 20–85 m; particles up to 144–354 mm', 'مخرج 200–1000 مم؛ 600–12000 م³/ساعة؛ رفع 20–85 م؛ حبيبات حتى 144–354 مم')),
        ('BX-0024-04-001', 'AZ double-casing horizontal slurry pumps', 'مضخات لب أفقية AZ بغلاف مزدوج', ('AZ40 to AZ300', 'من AZ40 إلى AZ300'),
         ('40–300 mm; vertically split double casing; outlet turns in 45° steps; media up to 80 °C (110 °C special)', '40–300 مم؛ غلاف مزدوج مشقوق رأسياً؛ المخرج يدور بخطوات 45°؛ حرارة الوسط حتى 80 °م (110 °م خاص)')),
        ('BX-0024-04-002', 'AZL vertical slurry pumps', 'مضخات لب رأسية AZL', 'AZL50, AZL65, AZL80, AZL100, AZL150', ('Sump pumps, outlet 50–150 mm', 'مضخات أحواض، مخرج 50–150 مم')),
        ('BX-0024-05-001', 'QSZ submersible slurry pumps', 'مضخات لب غاطسة QSZ', ('QSZ7-25-15 to QSZ2000-35-315', 'من QSZ7-25-15 إلى QSZ2000-35-315'),
         ('Pump and motor on one shaft; 7–2000 m³/h; head 15–60 m; 4–315 kW; 380 V 50 Hz; rubber hose outlet', 'المضخة والمحرك على عمود واحد؛ 7–2000 م³/ساعة؛ رفع 15–60 م؛ 4–315 كيلوواط؛ 380 فولت 50 هرتز؛ مخرج لخرطوم مطاطي')),
        ('BX-0024-02-002', 'Wet-end wear parts and shaft seals', 'قطع تآكل الجزء الرطب وموانع تسرب العمود', ('For the series above', 'للسلاسل أعلاه'),
         ('High-chrome or rubber liners and impellers; expeller, packing or mechanical seals', 'بطانات ودفّاعات عالية الكروم أو مطاطية؛ موانع تسرب طاردة أو بالحشوة أو ميكانيكية')),
    ]),
], type_label=('Series', 'السلسلة'))

# p7 slurry, froth & dredge pumps – additional series --------------------------------------------------------
F['slurry-froth-dredge-pumps-additional'] = family('slurry-froth-dredge-pumps-additional', CAT, [
    series('series', ('Slurry, froth and dredge pumps – additional series', 'مضخات لب ورغوة وكراكات – سلاسل إضافية'), ('1730–25,000 m³/h', '1730–25,000 م³/ساعة'), [
        ('BX-0020-01-001', 'Heavy-duty horizontal slurry pumps NPAH / NPHH / NPAHPP', 'مضخات لب أفقية ثقيلة NPAH / NPHH / NPAHPP', ('NPAH; NPHH high head; NPAHPP multistage for long distances', 'NPAH؛ وNPHH برفع عالٍ؛ وNPAHPP متعددة المراحل للمسافات الطويلة'),
         ('Up to 5400 m³/h; head to 100 m; outlet to 450 mm (18 in); pressure to 6900 kPa; max. particle 205 mm; metal or rubber liners; parts interchange with common AH / HH pumps',
          'حتى 5400 م³/ساعة؛ رفع حتى 100 م؛ مخرج حتى 450 مم (18 بوصة)؛ ضغط حتى 6900 كيلوباسكال؛ أكبر حبيبة 205 مم؛ بطانات معدنية أو مطاطية؛ أجزاؤها تتبادل مع مضخات AH / HH الشائعة')),
        ('BX-0020-01-002', 'Light-duty horizontal slurry pumps NPL', 'مضخات لب أفقية خفيفة NPL', ('Outlet 3/4–26 in', 'مخرج 3/4–26 بوصة'),
         ('Up to 12,200 m³/h; head to 55 m; outlet to 650 mm; pressure to 1725 kPa; max. particle 164 mm', 'حتى 12,200 م³/ساعة؛ رفع حتى 55 م؛ مخرج حتى 650 مم؛ ضغط حتى 1725 كيلوباسكال؛ أكبر حبيبة 164 مم')),
        ('BX-0020-01-003', 'Mill-circuit slurry pumps NPMC (R)', 'مضخات لب لدائرة الطاحونة NPMC (R)', ('Outlet 5–30 in', 'مخرج 5–30 بوصة'),
         ('Up to 21,500 m³/h; head to 55 m; outlet to 750 mm; pressure to 830 kPa; max. particle 254 mm; metal or rubber liners', 'حتى 21,500 م³/ساعة؛ رفع حتى 55 م؛ مخرج حتى 750 مم؛ ضغط حتى 830 كيلوباسكال؛ أكبر حبيبة 254 مم؛ بطانات معدنية أو مطاطية')),
        ('BX-0020-01-004', 'Gravel and sand pumps NPG / NPGH', 'مضخات الحصى والرمل NPG / NPGH', ('Outlet 4–36 in; NPGH high head', 'مخرج 4–36 بوصة؛ NPGH برفع عالٍ'),
         ('Up to 14,400 m³/h; head to 100 m; outlet to 900 mm; pressure to 2500 kPa; max. particle 500 mm', 'حتى 14,400 م³/ساعة؛ رفع حتى 100 م؛ مخرج حتى 900 مم؛ ضغط حتى 2500 كيلوباسكال؛ أكبر حبيبة 500 مم')),
        ('BX-0020-01-005', 'Heavy-duty dredge pumps NPD', 'مضخات كراكات ثقيلة NPD', ('Outlet to 1000 mm (39 in)', 'مخرج حتى 1000 مم (39 بوصة)'),
         ('Up to 25,000 m³/h; head to 85 m; NPSHr below 6 m; max. particle 350 mm; lighter than NPG', 'حتى 25,000 م³/ساعة؛ رفع حتى 85 م؛ NPSHr أقل من 6 م؛ أكبر حبيبة 350 مم؛ أخف من NPG')),
        ('BX-0020-01-006', 'Froth pumps NPAHF / NPAF', 'مضخات الرغوة NPAHF / NPAF', ('Outlet 2–22 in; NPAHF horizontal, NPAF vertical', 'مخرج 2–22 بوصة؛ NPAHF أفقية وNPAF رأسية'),
         ('Up to 12,000 m³/h; head to 85 m; pressure to 3400 kPa; max. particle 205 mm; open impeller with inducer', 'حتى 12,000 م³/ساعة؛ رفع حتى 85 م؛ ضغط حتى 3400 كيلوباسكال؛ أكبر حبيبة 205 مم؛ دفّاعة مفتوحة بمحرّض')),
        ('BX-0020-01-007', 'Vertical sump pumps NPSP (R)', 'مضخات أحواض رأسية NPSP (R)', ('Outlet 1.5–12 in; depth to 2.1 m with extension', 'مخرج 1.5–12 بوصة؛ عمق حتى 2.1 م بالتمديد'),
         ('Up to 1730 m³/h; head to 34 m; pressure to 800 kPa; max. particle 80 mm; cantilever shaft, no submerged bearings', 'حتى 1730 م³/ساعة؛ رفع حتى 34 م؛ ضغط حتى 800 كيلوباسكال؛ أكبر حبيبة 80 مم؛ عمود معلّق بلا محامل مغمورة')),
        ('BX-0020-01-008', 'Single-casing slurry pumps NPXU', 'مضخات لب بغلاف واحد NPXU', 'NPXU',
         ('Medium and low head; simple design, easy maintenance; for tailings and aggregate transfer', 'رفع متوسط ومنخفض؛ تصميم بسيط وصيانة سهلة؛ لنقل المخلفات والركام')),
        ('BX-0020-01-009', 'Vortex (recessed-impeller) pumps NPTC', 'مضخات دوامية (دفّاعة غائرة) NPTC', ('Horizontal and vertical', 'أفقية ورأسية'),
         ('Low-shear transfer of activated carbon and fragile solids without breakage; for CIP / CIL circuits', 'نقل الكربون المنشط والمواد الهشة دون تكسيرها؛ لدوائر CIP / CIL')),
        ('BX-0020-01-012', 'Interchangeable slurry pump wet-end parts', 'قطع الجزء الرطب القابلة للتبديل لمضخات اللب',
         ('Impellers, volute liners, throat bushes, frame-plate liners, rings', 'دفّاعات وبطانات الحلزون وجلب الحلق وبطانات لوح الإطار وحلقات'),
         ('High-chrome A05, A07, A49, A61, rubber and ceramic; fit common AH-type pumps', 'عالية الكروم A05 وA07 وA49 وA61، ومطاط وسيراميك؛ تناسب مضخات AH الشائعة')),
        ('BX-0020-01-013', 'Slurry pump sealing and rotating parts', 'قطع الإحكام والأجزاء الدوّارة لمضخات اللب',
         ('Expellers, packings, mechanical seals, shaft sleeves, bearing assemblies', 'طاردات وحشوات وموانع تسرب ميكانيكية وجلب أعمدة ومجموعات محامل'),
         ('Gland and drive-end parts', 'قطع الحشوة وطرف الإدارة')),
    ]),
], type_label=('Series', 'السلسلة'))

# p8 submersible & hydraulic slurry pumps -------------------------------------------------------------------
F['submersible-hydraulic-slurry-pumps'] = family('submersible-hydraulic-slurry-pumps', CAT, [
    table('pumps', ('Submersible and hydraulic slurry pumps', 'مضخات لب غاطسة وهيدروليكية'), ('15–4000 m³/h', '15–4000 م³/ساعة'),
          [C('sizes', 'Sizes', 'المقاسات'), CAP, HEAD, C('drive', 'Drive', 'الإدارة'), C('notes', 'Notes', 'ملاحظات')],
          [('BX-0022-01-018', 'Electric submersible slurry pump DZQ(J)', 'مضخة لب غاطسة كهربائية DZQ(J)', ('Outlet 80–400 mm', 'مخرج 80–400 مم'), '30–2400', '12–65', ('Electric', 'كهربائية'),
            ('Bottom agitator; up to 150 m submergence; overheating protection', 'محرّض سفلي؛ غمر حتى 150 م؛ حماية من السخونة الزائدة')),
           ('BX-0022-01-019', 'Hydraulic submersible slurry pump YZQ', 'مضخة لب غاطسة هيدروليكية YZQ', '50YZQ, 75YZQ, 100YZQ, 150YZQ, 200YZQ', ('max. 46–570', 'حتى 46–570'), ('max. 14–32', 'حتى 14–32'),
            ('Hydraulic', 'هيدروليكية'), ('Ø 50–200 mm', 'قطر 50–200 مم')),
           ('BX-0022-01-021', 'Hydraulic slurry pump with agitators YZQJ', 'مضخة لب هيدروليكية بمحرّضات YZQJ', ('YZQJ35 to YZQJ400 (A/B, HC versions)', 'من YZQJ35 إلى YZQJ400 (نسخ A/B وHC)'),
            '100–1200', '14–43', ('Hydraulic, 18–295 kW', 'هيدروليكية، 18–295 كيلوواط'), ('Two side agitators', 'محرّضان جانبيان')),
           ('BX-0036-01-021', 'Excavator-mounted hydraulic pump package', 'مجموعة مضخة هيدروليكية تُركّب على الحفار', ('65–600 mm', '65–600 مم'), '15–4000', '10–125',
            ('Excavator hydraulics', 'هيدروليك الحفار'), ('For 1–80 t excavators', 'لحفارات 1–80 طن'))],
          key_rows=['capacity', 'head', 'drive']),
])

# p9 dewatering, water & deep-well pumps --------------------------------------------------------------------
F['dewatering-water-deep-well-pumps'] = family('dewatering-water-deep-well-pumps', CAT, [
    table('pumps', ('Dewatering, water and deep-well pumps', 'مضخات النزح والمياه والآبار العميقة'), ('3.8–15000 m³/h', '3.8–15000 م³/ساعة'),
          [C('sizes', 'Sizes', 'المقاسات'), CAP, HEAD, C('notes', 'Notes', 'ملاحظات')],
          [('BX-0036-01-012', 'Self-priming trash pump TSP / TSPH', 'مضخة مخلفات ذاتية التحضير TSP / TSPH', ('2–12 in', '2–12 بوصة'), '10–1275', '3–75', ('Self-priming to 8 m', 'تحضير ذاتي حتى 8 م')),
           ('BX-0036-01-013', 'Self-priming dewatering pump TSPL / TSPM / TSPHH', 'مضخة نزح ذاتية التحضير TSPL / TSPM / TSPHH', ('4–42 in', '4–42 بوصة'), '25–15000', '10–245',
            ('Self-priming to 8.8 m; diesel skid version', 'تحضير ذاتي حتى 8.8 م؛ نسخة على هيكل بمحرك ديزل')),
           ('BX-0036-01-023', 'Submersible dewatering pump TRZ', 'مضخة نزح غاطسة TRZ', ('50–600 mm', '50–600 مم'), '10–6000', '3–125', ('Submersible dewatering', 'نزح غاطس')),
           ('BX-0036-01-024', 'Submersible drainage pump TBZ', 'مضخة تصريف غاطسة TBZ', ('50–200 mm', '50–200 مم'), '10–372', '5–50', ('Compact drainage pump', 'مضخة تصريف مدمجة')),
           ('BX-0036-01-026', 'Deep-well pump TQJ', 'مضخة آبار عميقة TQJ', ('Well Ø 150–550 mm', 'قطر البئر 150–550 مم'), '5–900', '10–450', ('Water supply', 'إمداد المياه')),
           ('BX-0024-01-013', 'End-suction water pump', 'مضخة مياه بسحب طرفي', ('1.5–12 in', '1.5–12 بوصة'), '3.8–1200', '4.6–133', ('Process water', 'مياه المعالجة'))],
          key_rows=['capacity', 'head', 'notes']),
])

# p10 submersible, drainage & borehole pumps – additional ---------------------------------------------------
F['submersible-drainage-borehole-pumps'] = family('submersible-drainage-borehole-pumps', CAT, [
    series('series', ('Submersible, drainage and borehole pumps – additional series', 'مضخات غاطسة وتصريف وآبار – سلاسل إضافية'), ('0.12–110 kW', '0.12–110 كيلوواط'), [
        ('BX-0020-01-010', 'Submersible slurry pumps NQ', 'مضخات لب غاطسة NQ', ('NQ with agitator', 'NQ بمحرّض'), ('Built-in motor, no priming; high-chrome wear parts; agitator stirs settled solids', 'محرك مدمج بلا تحضير؛ قطع تآكل عالية الكروم؛ المحرّض يقلّب المواد المترسبة')),
        ('BX-0407-01-002', 'KBS submersible slurry pumps', 'مضخات لب غاطسة KBS', ('KBS series, 4–37 kW', 'سلسلة KBS، ‏4–37 كيلوواط'), ('Up to 390 m³/h; head to 39 m; outlet 80–200 mm; 380 V; IP68; to 15 m depth', 'حتى 390 م³/ساعة؛ رفع حتى 39 م؛ مخرج 80–200 مم؛ 380 فولت؛ IP68؛ حتى عمق 15 م')),
        ('BX-0407-01-006', 'QNS submersible slurry pumps', 'مضخات لب غاطسة QNS', ('80QNS42.2 to 200QNS475 (19 models)', 'من 80QNS42.2 إلى 200QNS475 ‏(19 موديلاً)'),
         ('2.2–75 kW; up to 600 m³/h; head to 57 m; outlet 80–200 mm; slurry density to 1.3 g/cm³', '2.2–75 كيلوواط؛ حتى 600 م³/ساعة؛ رفع حتى 57 م؛ مخرج 80–200 مم؛ كثافة اللب حتى 1.3 جم/سم³')),
        ('BX-0407-01-004', 'GMS submersible sludge pumps (vortex)', 'مضخات حمأة غاطسة GMS (دوامية)', ('GMS series, 4–22 kW', 'سلسلة GMS، ‏4–22 كيلوواط'), ('Up to 235 m³/h; head to 58 m; density to 1.3 g/cm³; up to 60 °C; pH 6–10', 'حتى 235 م³/ساعة؛ رفع حتى 58 م؛ كثافة حتى 1.3 جم/سم³؛ حتى 60 °م؛ pH ‏6–10')),
        ('BX-0407-01-001', 'KBZ submersible drainage pumps', 'مضخات تصريف غاطسة KBZ', ('KBZ series, 1.5–15 kW', 'سلسلة KBZ، ‏1.5–15 كيلوواط'), ('Up to 160 m³/h; head to 57 m; 400 V 50 Hz; IP68; to 25 m depth', 'حتى 160 م³/ساعة؛ رفع حتى 57 م؛ 400 فولت 50 هرتز؛ IP68؛ حتى عمق 25 م')),
        ('BX-0407-01-003', 'SH high-head submersible drainage pumps', 'مضخات تصريف غاطسة برفع عالٍ SH', ('SH series, 22–110 kW', 'سلسلة SH، ‏22–110 كيلوواط'), ('Up to 408 m³/h; head to 140 m; 400 V; to 30 m depth; for deep mines and open pits', 'حتى 408 م³/ساعة؛ رفع حتى 140 م؛ 400 فولت؛ حتى عمق 30 م؛ للمناجم العميقة والحفر المفتوحة')),
        ('BX-0407-01-005', 'Small submersible drainage pumps', 'مضخات تصريف غاطسة صغيرة', 'FS(M)2.4(F), FS(M)2.75(F)', ('50 mm outlet; 220 V single or 380 V three phase; IP68; 13.5–16.5 kg', 'مخرج 50 مم؛ 220 فولت أحادي الطور أو 380 فولت ثلاثي الأطوار؛ IP68؛ 13.5–16.5 كجم')),
        ('BX-0407-01-007', 'QXN multistage submersible pumps', 'مضخات غاطسة متعددة المراحل QXN', ('QXN25-17/1-2.2 to QXN40-85/2-18.5 and larger', 'من QXN25-17/1-2.2 إلى QXN40-85/2-18.5 وأكبر'), ('25–40 m³/h; head to 85 m; 2.2–18.5 kW and above; 380 V', '25–40 م³/ساعة؛ رفع حتى 85 م؛ 2.2–18.5 كيلوواط فأكثر؛ 380 فولت')),
        ('BX-0026-01-009', 'Contractor dewatering pumps', 'مضخات نزح للمقاولين', ('HS, KBZ, KS, QXN, LBM; LBR residue pump', 'HS وKBZ وKS وQXN وLBM؛ ومضخة مخلفات LBR'), ('Submersible IP68 pumps for pit dewatering', 'مضخات غاطسة IP68 لنزح الحفر')),
        ('BX-0026-01-010', 'Submersible slurry pumps with agitator', 'مضخات لب غاطسة بمحرّض', 'HSD, KBS', ('Lift sand and mud from ponds and pits', 'ترفع الرمل والطين من البرك والحفر')),
        ('BX-0026-01-007', 'Submersible sewage and wastewater pumps', 'مضخات صرف صحي ومياه مستعملة غاطسة', 'VB, HVS, V, VP, QWK / QWKF, U, B, WQ / WQ(D), V-D, CUT, C, WF, WP(D), LF',
         ('IP68 with float switch; vortex, channel or cutter impellers; stainless QWK; WQ up to 90 kW and DN600 outlet', 'IP68 بمفتاح عوامة؛ دفّاعات دوامية أو بقنوات أو قاطعة؛ QWK من الستانلس؛ WQ حتى 90 كيلوواط ومخرج DN600')),
        ('BX-0026-01-011', 'Clear-water drainage pumps', 'مضخات تصريف المياه النقية', 'SPA multistage, SPT, SPSN stainless, QDX, QDXS', ('Submersible, float switch option; about 0.12–5.5 kW', 'غاطسة، بخيار مفتاح عوامة؛ نحو 0.12–5.5 كيلوواط')),
        ('BX-0026-01-012', 'Submersible borehole pumps', 'مضخات آبار غاطسة', ('3SKm / 4SKm, SD(M), SP(M), QGD screw pumps', '3SKm / 4SKm وSD(M) وSP(M) ومضخات لولبية QGD'), ('3 and 4 in wells; AISI 201 / 304 stainless casings; oil-cooled motors', 'لآبار 3 و4 بوصات؛ أغلفة ستانلس AISI 201 / 304؛ محركات مبرّدة بالزيت')),
        ('BX-0026-01-013', 'Solar pumping systems', 'أنظمة ضخ بالطاقة الشمسية', '3SQJ / 4SQJ, 3SSC / 4SSC (DC), SQG, SQY, SQD, SHFM, SMH, SJ, SQB', ('Solar borehole and surface pumps with controllers', 'مضخات آبار وسطحية تعمل بالطاقة الشمسية مع وحدات تحكم')),
    ], intro=('Includes small 50 mm drainage pumps for small sites.', 'تشمل مضخات تصريف صغيرة بمخرج 50 مم للمواقع الصغيرة.')),
], type_label=('Series', 'السلسلة'))

# p11 water, process & engine-driven pumps ------------------------------------------------------------------
F['water-process-engine-driven-pumps'] = family('water-process-engine-driven-pumps', CAT, [
    series('series', ('Water, process and engine-driven pumps', 'مضخات المياه والمعالجة والمضخات بمحرك'), ('0.75–90 kW', '0.75–90 كيلوواط'), [
        ('BX-0020-01-011', 'Horizontal split-case pumps NS', 'مضخات أفقية بغلاف مشقوق NS', 'NS', ('Double-suction clean-water pump; high flow, low vibration; for water supply and drainage', 'مضخة مياه نقية بسحب مزدوج؛ تدفق عالٍ واهتزاز منخفض؛ لإمداد المياه والتصريف')),
        ('BX-0026-01-004', 'End-suction centrifugal pumps', 'مضخات طاردة مركزية بسحب طرفي', 'FSE, FSBE, F (EN 733), FG / FGS / FGD, FS / FSD', ('Cast iron or CF8 / CF8M stainless; DIN flanges; up to DN350; IE2 / IE3 motors; FSBE speed controlled', 'حديد زهر أو ستانلس CF8 / CF8M؛ شفاه DIN؛ حتى DN350؛ محركات IE2 / IE3؛ FSBE بتحكم في السرعة')),
        ('BX-0026-01-003', 'Vertical and in-line multistage pumps', 'مضخات متعددة المراحل رأسية ومباشرة', 'CDL / CDLF, CRA / CRNA / CRLA, CRAE, CVA / CVFA / CVLA, CVM, WSF',
         ('304 / 316 stainless; IE3 / IE4 motors, IE5 variable-speed versions; permanent-magnet motors 0.75–90 kW', 'ستانلس 304 / 316؛ محركات IE3 / IE4، ونسخ IE5 متغيرة السرعة؛ محركات مغناطيس دائم 0.75–90 كيلوواط')),
        ('BX-0026-01-002', 'Stainless horizontal and booster pumps', 'مضخات أفقية ومضخات تعزيز من الستانلس', 'BK, MB, CM, SJZ, PLURI / PLURIJET, ASJZ, ACM, BP-CMA, BP-P',
         ('AISI 304 / 316 wet parts; self-priming and variable-frequency booster sets up to 4 kW', 'أجزاء رطبة من ستانلس AISI 304 / 316؛ مجموعات تعزيز ذاتية التحضير ومتغيرة التردد حتى 4 كيلوواط')),
        ('BX-0026-01-005', 'Self-priming sewage pumps', 'مضخات صرف ذاتية التحضير', 'EJ / EJZ / EJD, EJT', ('Cast or ductile iron casing; ductile iron, bronze or stainless impeller', 'غلاف من الحديد الزهر أو المطيلي؛ دفّاعة من الحديد المطيلي أو البرونز أو الستانلس')),
        ('BX-0026-01-014', 'Pump frequency converters and accessories', 'محوّلات تردد المضخات وملحقاتها', ('W191, W713B; pressure switches, pressure tanks, float switches', 'W191 وW713B؛ مفاتيح ضغط وخزانات ضغط ومفاتيح عوامة'), ('Speed and pressure control for pumps', 'التحكم في سرعة المضخات وضغطها')),
        ('BX-0529-01-004', 'Petrol water pumps', 'مضخات مياه بالبنزين', ('YL20, YL30, YL40 (7.5 hp), YL40 (13 hp)', 'YL20 وYL30 وYL40 ‏(7.5 حصان) وYL40 ‏(13 حصاناً)'), ('2, 3 and 4 in; 5.5–13 hp; head 26–30 m; suction 8 m; 36, 60 and 90 m³/h; 20–47 kg', '2 و3 و4 بوصات؛ 5.5–13 حصاناً؛ رفع 26–30 م؛ سحب 8 م؛ 36 و60 و90 م³/ساعة؛ 20–47 كجم')),
        ('BX-0481-01-010', 'Petrol water pumps (PGW)', 'مضخات مياه بالبنزين (PGW)', ('PGW-20 (2 in), PGW-30 (3 in), PGW-20H (2 in high head)', 'PGW-20 ‏(2 بوصة) وPGW-30 ‏(3 بوصات) وPGW-20H ‏(2 بوصة برفع عالٍ)'), ('30 / 60 / 30 m³/h; head 28 / 26 / 65 m; suction 7–8 m; 23–27 kg', '30 / 60 / 30 م³/ساعة؛ رفع 28 / 26 / 65 م؛ سحب 7–8 م؛ 23–27 كجم')),
        ('BX-0529-01-008', 'Diesel water pump', 'مضخة مياه بالديزل', 'YLD80', ('3 in; 40 m³/h; head 26 m; suction 8 m; self-priming 120 s at 4 m; 4 kW engine; 10 h continuous', '3 بوصات؛ 40 م³/ساعة؛ رفع 26 م؛ سحب 8 م؛ تحضير ذاتي 120 ثانية عند 4 م؛ محرك 4 كيلوواط؛ 10 ساعات متواصلة')),
        ('BX-0529-01-009', 'Electric water pumps', 'مضخات مياه كهربائية', 'YLWP20E, YLWP30E, YLWP40E', ('2, 3 and 4 in; 2.2 / 3 / 4 kW; 220 / 380 V; head 25–27 m; 30 / 55 / 60 m³/h', '2 و3 و4 بوصات؛ 2.2 / 3 / 4 كيلوواط؛ 220 / 380 فولت؛ رفع 25–27 م؛ 30 / 55 / 60 م³/ساعة')),
        ('BX-0492-01-004', 'Petrol, diesel, trash and fire pumps', 'مضخات بالبنزين والديزل ومضخات مخلفات وحريق', 'WL20XH, WB20XH, SEH-50X / 80X, YP40T, WHP15 / 20 / 30-E', ('Petrol 2–3 in; diesel 2–6 in, 9–15 hp; 4 in trash pump', 'بنزين 2–3 بوصات؛ ديزل 2–6 بوصات، 9–15 حصاناً؛ مضخة مخلفات 4 بوصات')),
        ('BX-0485-01-003', 'Diesel water pumps', 'مضخات مياه بالديزل', ('2 and 3 in high pressure; 4 and 6 in electric start', '2 و3 بوصات بضغط عالٍ؛ 4 و6 بوصات بتشغيل كهربائي'), ('Site water and dewatering pumps', 'مضخات مياه ونزح للموقع')),
    ]),
], type_label=('Series', 'السلسلة'))

# p12 pump wear parts & slurry hoses ------------------------------------------------------------------------
F['pump-wear-parts-slurry-hoses'] = family('pump-wear-parts-slurry-hoses', CAT, [
    table('parts', ('Wear parts and hoses', 'قطع التآكل والخراطيم'), ('', ''), [C('desc', 'Description', 'الوصف')],
          [('BX-0022-01-027', 'Slurry pump wear parts', 'قطع تآكل مضخات اللب',
            ('Impellers, liners, throat bushes, casings, shafts, bearings and seals (expeller, packing, mechanical, lip). Materials: high-chrome B05 (≥ 56 HRC), B07 (≥ 59 HRC), B49, B25, SiC ceramic, rubber, polyurethane',
             'دفّاعات وبطانات وجلب حلق وأغلفة وأعمدة ومحامل وموانع تسرب (طاردة وبالحشوة وميكانيكية وشفوية). المواد: عالية الكروم B05 ‏(≥ 56 HRC) وB07 ‏(≥ 59 HRC) وB49 وB25، وسيراميك كربيد السيليكون، ومطاط، وبولي يوريثان')),
           ('BX-0036-01-015', 'Metal slurry pump parts', 'قطع معدنية لمضخات اللب', ('Metal parts interchangeable with common international slurry pumps', 'قطع معدنية قابلة للتبادل مع مضخات اللب العالمية الشائعة')),
           ('BX-0036-01-016', 'Rubber slurry pump parts', 'قطع مطاطية لمضخات اللب', ('Impeller, cover plate liner, frame plate liner, throat bush, frame plate liner insert; natural or synthetic rubber', 'دفّاعة وبطانة لوح الغطاء وبطانة لوح الإطار وجلبة الحلق وحشوة بطانة لوح الإطار؛ مطاط طبيعي أو صناعي')),
           ('BX-0036-01-035', 'Submersible slurry pump parts', 'قطع المضخات الغاطسة', ('High-chrome 27–28%, hardness 650+ Brinell', 'كروم عالٍ 27–28%، صلادة 650+ برينل')),
           ('BX-0036-01-033', 'Slurry and dredge hose', 'خراطيم اللب والتجريف', ('Ø 50–1000 mm, 3–30 bar, 6 or 12 m lengths or to order; flange or clamp ends; rubber, PE, HDPE, PVC or steel', 'قطر 50–1000 مم، 3–30 بار، أطوال 6 أو 12 م أو حسب الطلب؛ أطراف بشفة أو مشبك؛ مطاط أو PE أو HDPE أو PVC أو فولاذ'))],
          unit=U_PRODUCT),
], type_label=('Product', 'المنتج'))

# p13 slurry pipes, packings & gaskets ----------------------------------------------------------------------
F['slurry-pipes-packings-gaskets'] = family('slurry-pipes-packings-gaskets', CAT, [
    table('pipes', ('Wear-resistant slurry pipes', 'أنابيب لب مقاومة للتآكل'), ('', ''), [C('range', 'Range', 'المدى'), C('use', 'Use', 'الاستخدام')],
          [('BX-0062-01-006', 'UHMW-PE pipe & fittings', 'أنابيب ووصلات UHMW-PE', ('Pipe, elbows, tees, Y-pieces, flanged joints', 'أنابيب وأكواع ووصلات T وY ووصلات بشفة'),
            ('Slurry, tailings, mine water and dredging lines; self-lubricating, high abrasion resistance', 'خطوط اللب والمخلفات ومياه المناجم والتجريف؛ ذاتية التزييت وعالية المقاومة للتآكل')),
           ('BX-0174-01-009', 'Ceramic-lined pipes & fittings', 'أنابيب ووصلات مبطّنة بالخزف', ('Pipes, bends and ducts lined with 92–99% alumina', 'أنابيب وأكواع ومجارٍ مبطّنة بألومينا 92–99%'),
            ('Highly abrasive slurry and bulk transport', 'نقل اللب والمواد شديدة الكشط'))],
          unit=U_PRODUCT),
    table('packings', ('Pump packings and gasket materials', 'حشوات المضخات ومواد الجوانات'), ('', ''), [C('spec', 'Specification', 'المواصفات')],
          [('BX-0043-02-016', 'PTFE braided packing', 'حشوة مجدولة من PTFE', ('With graphite or aramid fibre; 2–25 MPa; −240 to 288 °C; pH 0–14; 3.2–25.4 mm', 'مع الجرافيت أو ألياف الأراميد؛ 2–25 ميجاباسكال؛ من −240 إلى 288 °م؛ pH ‏0–14؛ 3.2–25.4 مم')),
           ('BX-0043-02-018', 'Flexible graphite braided packing', 'حشوة مجدولة من الجرافيت المرن', ('Plain or Inconel-wire reinforced', 'عادية أو مقوّاة بسلك إنكونيل')),
           ('BX-0043-02-021', 'Non-asbestos gasket sheet', 'ألواح جوانات خالية من الأسبستوس', ('0.4–6 mm; 200–450 °C; 15–40 kg/cm²', '0.4–6 مم؛ 200–450 °م؛ 15–40 كجم/سم²'))],
          unit=U_PRODUCT),
], type_label=('Product', 'المنتج'))

# p14 industrial rubber & hydraulic hoses (rows split by code) ---------------------------------------------
H = lambda code, en, ar, size, data: (code, en, ar, size, data)
AIR = (('3/16–4 in (4.8–101.6 mm)', '3/16–4 بوصة (4.8–101.6 مم)'), ('WP 20 bar (300 psi); −40 to 70 °C', 'ضغط تشغيل 20 بار (300 psi)؛ من −40 إلى 70 °م'))
FUEL = ('3/16–12 in', '3/16–12 بوصة')
CHEM = (('3/4–6 in', '3/4–6 بوصات'), ('WP 10–17 bar; for reagents and acids', 'ضغط تشغيل 10–17 بار؛ للكواشف والأحماض'))
GAS = (('3/16–1 in', '3/16–1 بوصة'), ('WP 20 bar', 'ضغط تشغيل 20 بار'))
BULK = (('1-1/4–12 in', '1-1/4–12 بوصة'), ('WP 10 bar; abrasion-resistant', 'ضغط تشغيل 10 بار؛ مقاومة للتآكل'))
DRED = (('150–1300 mm', '150–1300 مم'), ('WP 3–30 bar; lengths 1–3 m (floating 11.8 m)', 'ضغط تشغيل 3–30 بار؛ أطوال 1–3 م (العائم 11.8 م)'))
SPIR = (('1/4–2 in', '1/4–2 بوصة'), ('Four to six steel-wire spirals; WP up to 45 MPa', 'أربع إلى ست طبقات سلك فولاذي حلزوني؛ ضغط تشغيل حتى 45 ميجاباسكال'))
LAY = (('1–10 in', '1–10 بوصات'), ('For fire water and pump discharge lines', 'لمياه الإطفاء وخطوط تصريف المضخات'))
F['industrial-rubber-hydraulic-hoses'] = family('industrial-rubber-hydraulic-hoses', CAT, [
    table('hoses', ('Industrial rubber and hydraulic hoses', 'الخراطيم المطاطية الصناعية والهيدروليكية'), ('3/16 in–1.3 m', '3/16 بوصة–1.3 م'),
          [C('size', 'Size range', 'مدى المقاسات'), C('data', 'Pressure / data', 'الضغط / البيانات')],
          [H('BX-0258-01-001', 'Textile-reinforced air hose', 'خرطوم هواء مقوّى بالنسيج', *AIR),
           H('BX-0258-01-002', 'Jackhammer air hose', 'خرطوم هواء للمطارق', *AIR),
           H('BX-0258-01-003', 'Multi-purpose hose', 'خرطوم متعدد الأغراض', *AIR),
           H('BX-0258-01-004', 'Water discharge hose 150 PSI', 'خرطوم تصريف ماء 150 PSI', ('3/16–12 in', '3/16–12 بوصة'), ('WP 10 bar', 'ضغط تشغيل 10 بار')),
           H('BX-0258-01-006', 'Water discharge hose 300 PSI', 'خرطوم تصريف ماء 300 PSI', ('3/16–12 in', '3/16–12 بوصة'), ('WP 20 bar', 'ضغط تشغيل 20 بار')),
           H('BX-0258-01-005', 'Water suction hose 150 PSI', 'خرطوم شفط ماء 150 PSI', ('3/4–14 in', '3/4–14 بوصة'), ('WP 10 bar; vacuum 0.8 bar', 'ضغط تشغيل 10 بار؛ تفريغ 0.8 بار')),
           H('BX-0258-01-007', 'Water suction hose 300 PSI', 'خرطوم شفط ماء 300 PSI', ('3/4–14 in', '3/4–14 بوصة'), ('WP 20 bar; vacuum 0.8 bar', 'ضغط تشغيل 20 بار؛ تفريغ 0.8 بار')),
           H('BX-0258-01-009', 'Nitrile fuel transfer hose 300 PSI', 'خرطوم نقل وقود نتريل 300 PSI', FUEL, ('WP 20 bar', 'ضغط تشغيل 20 بار')),
           H('BX-0258-01-011', 'Nitrile fuel discharge hose 150 PSI', 'خرطوم تصريف وقود نتريل 150 PSI', FUEL, ('WP 10 bar', 'ضغط تشغيل 10 بار')),
           H('BX-0258-01-013', 'Nitrile fuel suction hose 150 PSI', 'خرطوم شفط وقود نتريل 150 PSI', FUEL, ('WP 10 bar', 'ضغط تشغيل 10 بار')),
           H('BX-0258-01-019', 'UHMWPE chemical discharge hose', 'خرطوم تصريف كيماويات UHMWPE', *CHEM),
           H('BX-0258-01-020', 'UHMWPE chemical suction hose', 'خرطوم شفط كيماويات UHMWPE', *CHEM),
           H('BX-0258-01-023', 'Oxygen hose', 'خرطوم أكسجين', *GAS),
           H('BX-0258-01-024', 'Acetylene hose', 'خرطوم أسيتيلين', *GAS),
           H('BX-0258-01-025', 'Twin welding hose', 'خرطوم لحام مزدوج', *GAS),
           H('BX-0258-01-026', 'LPG / propane gas hose', 'خرطوم غاز LPG / بروبان', *GAS),
           H('BX-0258-01-028', 'Bulk material suction hose', 'خرطوم شفط المواد السائبة', *BULK),
           H('BX-0258-01-029', 'Bulk material discharge hose', 'خرطوم تصريف المواد السائبة', *BULK),
           H('BX-0258-01-034', 'Suction dredging hose', 'خرطوم شفط للتجريف', *DRED),
           H('BX-0258-01-035', 'Discharge dredging hose', 'خرطوم تصريف للتجريف', *DRED),
           H('BX-0258-01-036', 'Floating dredging hose', 'خرطوم تجريف عائم', *DRED),
           H('BX-0258-01-037', 'Rubber expansion joints and floaters', 'وصلات تمدد مطاطية وعوامات', 'DN50–DN1500',
             ('Single, double-arch, reducer and restrained joints; hose and cable floaters', 'وصلات بقوس مفرد ومزدوج ومخفّضة ومقيّدة؛ عوامات للخراطيم والكابلات')),
           H('BX-0258-01-038', 'Hydraulic hose SAE100 R1AT / EN 853 1SN', 'خرطوم هيدروليك SAE100 R1AT / EN 853 1SN', ('3/16–2 in', '3/16–2 بوصة'), ('One steel-wire braid', 'طبقة واحدة من السلك الفولاذي المجدول')),
           H('BX-0258-01-039', 'Hydraulic hose SAE100 R2AT / EN 853 2SN', 'خرطوم هيدروليك SAE100 R2AT / EN 853 2SN', ('3/16–2 in', '3/16–2 بوصة'), ('Two steel-wire braids', 'طبقتان من السلك الفولاذي المجدول')),
           H('BX-0258-01-046', 'Spiral hydraulic hose R12', 'خرطوم هيدروليك حلزوني R12', *SPIR),
           H('BX-0258-01-047', 'Spiral hydraulic hose R13', 'خرطوم هيدروليك حلزوني R13', *SPIR),
           H('BX-0258-01-048', 'Spiral hydraulic hose R15', 'خرطوم هيدروليك حلزوني R15', *SPIR),
           H('BX-0258-01-050', 'Spiral hydraulic hose EN856 4SP', 'خرطوم هيدروليك حلزوني EN856 4SP', *SPIR),
           H('BX-0258-01-051', 'Spiral hydraulic hose EN856 4SH', 'خرطوم هيدروليك حلزوني EN856 4SH', *SPIR),
           H('BX-0258-01-053', 'Rubber-lined layflat fire hose', 'خرطوم حريق مسطح مبطن بالمطاط', *LAY),
           H('BX-0258-01-054', 'PVC-lined layflat fire hose', 'خرطوم حريق مسطح مبطن بـ PVC', *LAY),
           H('BX-0258-01-058', 'Rubber layflat discharge hose', 'خرطوم تصريف مسطح مطاطي', *LAY)],
          key_rows=['size', 'data'], unit=U_HOSE),
], type_label=('Hose type', 'نوع الخرطوم'), unit=U_HOSE)

# p15 knife gate, slurry & process valves -------------------------------------------------------------------
F['knife-gate-slurry-process-valves'] = family('knife-gate-slurry-process-valves', CAT, [
    series('series', ('Knife gate, slurry and process valves', 'صمامات سكينية ولب ومعالجة'), ('DN15–DN2500', 'DN15–DN2500'), [
        ('BX-0619-02-001', 'Bonneted knife gate valve, double flange', 'صمام سكيني بغطاء وشفتين', 'DN80–DN1200', ('For slurry and mud; 150 psi (MSS SP-81); CF8M body and bonnet, SS316 gate, EPDM seat (V-port or O-ring)', 'للب والطين؛ 150 psi ‏(MSS SP-81)؛ جسم وغطاء CF8M، بوابة SS316، مقعد EPDM ‏(فتحة V أو حلقة O)')),
        ('BX-0619-03-001', 'Flanged slurry knife gate valve, sleeved, bi-directional', 'صمام سكيني للب بشفة وجلبتين، ثنائي الاتجاه', ('3–60 in (DN80–DN1500)', '3–60 بوصة (DN80–DN1500)'), ('Two rubber sleeves; no metal in contact with slurry; tight shut-off; natural rubber to 180 °F, special rubber to 400 °F', 'جلبتان مطاطيتان؛ لا معدن يلامس اللب؛ إغلاق محكم؛ مطاط طبيعي حتى 180 °ف ومطاط خاص حتى 400 °ف')),
        ('BX-0619-05-001', 'Wafer slurry knife gate valve, sleeved, bi-directional', 'صمام سكيني رقاقي للب بجلبتين، ثنائي الاتجاه', ('2–24 in (DN50–DN600)', '2–24 بوصة (DN50–DN600)'), ('Two rubber sleeves; tight shut-off; no metal in contact with slurry', 'جلبتان مطاطيتان؛ إغلاق محكم؛ لا معدن يلامس اللب')),
        ('BX-0619-04-001', 'Through-conduit knife gate valve, bi-directional', 'صمام سكيني بممر كامل، ثنائي الاتجاه', ('DN50–DN600 (2–24 in)', 'DN50–DN600 ‏(2–24 بوصة)'), ('O-port gate for high-solids lines without clogging; seats on both sides; 10 bar to DN250, 7 bar DN300–450', 'بوابة بفتحة O لخطوط المواد الصلبة الكثيفة دون انسداد؛ مقاعد على الجانبين؛ 10 بار حتى DN250 و7 بار من DN300 إلى 450')),
        ('BX-0619-06-001', 'Wafer knife gate valve, unidirectional (VT series)', 'صمام سكيني رقاقي أحادي الاتجاه (سلسلة VT)', ('2–24 in (DN50–DN600)', '2–24 بوصة (DN50–DN600)'), ('Bevelled, polished, hard-chrome gate; replaceable seat; for particle-laden lines', 'بوابة مشطوفة مصقولة مطلية بالكروم الصلب؛ مقعد قابل للتبديل؛ للخطوط المحمّلة بالحبيبات')),
        ('BX-0669-01-001', 'Integrated knife gate valve, non-rising stem', 'صمام سكيني متكامل بساق غير صاعدة', 'DN50–DN300', ('Ductile iron body, SS304 knife, EPDM U-seat, PTFE packing, handwheel; EN 558 S20 and MSS SP-81', 'جسم من الحديد المطيلي، سكين SS304، مقعد U من EPDM، حشوة PTFE، عجلة يدوية؛ EN 558 S20 وMSS SP-81')),
        ('BX-0669-02-001', 'Integrated knife gate valve, rising stem', 'صمام سكيني متكامل بساق صاعدة', 'DN50–DN300', ('Same materials as the non-rising-stem version', 'المواد نفسها في نسخة الساق غير الصاعدة')),
        ('BX-0619-01-004', 'Axial-flow (nozzle) non-slam check valves', 'صمامات عدم رجوع محورية (بفوهة) بلا طرق', ('To API 6D, ASME B16.34, API 594', 'وفق API 6D وASME B16.34 وAPI 594'), ('Venturi port for low pressure loss; spring closing reduces water hammer; soft seal with metal back-up', 'فتحة فنتوري لفقد ضغط منخفض؛ إغلاق بنابض يقلل المطرقة المائية؛ إحكام لين بدعم معدني')),
        ('BX-0619-01-005', 'Tilted-disc check valves', 'صمامات عدم رجوع بقرص مائل', ('2–60 in; up to ASME Class 2500', '2–60 بوصة؛ حتى ASME Class 2500'), ('Large flow area, low pressure loss, compact', 'مساحة تدفق كبيرة وفقد ضغط منخفض وحجم مدمج')),
        ('BX-0619-01-007', 'Butterfly valves, concentric and eccentric', 'صمامات فراشة متمركزة ولا متمركزة', ('2–100 in (DN50–DN2500); CL150–900', '2–100 بوصة (DN50–DN2500)؛ CL150–900'), ('Metal or soft seated; cast iron, carbon steel, stainless, alloy or duplex', 'مقعد معدني أو لين؛ حديد زهر أو فولاذ كربوني أو ستانلس أو سبائك أو دوبلكس')),
        ('BX-0619-01-011', 'Fully lined valves for slurry and corrosive service', 'صمامات مبطنة بالكامل للب والخدمة المسببة للتآكل', ('1/2–24 in (DN15–DN600); CL125 / CL150', '1/2–24 بوصة (DN15–DN600)؛ CL125 / CL150'), ('Diaphragm, ball, plug, butterfly and check types, rubber or fluoropolymer lined; manual, electric, pneumatic or hydraulic', 'أنواع غشائية وكروية وسدادية وفراشة وعدم رجوع، مبطنة بالمطاط أو البوليمر الفلوري؛ يدوية أو كهربائية أو هوائية أو هيدروليكية')),
    ]),
], type_label=('Series', 'السلسلة'))

# p16 water-line valves – ductile iron & steel ---------------------------------------------------------------
F['water-line-valves-ductile-iron-steel'] = family('water-line-valves-ductile-iron-steel', CAT, [
    series('series', ('Water-line valves – ductile iron and steel', 'صمامات خطوط المياه – حديد مطيلي وفولاذ'), ('150–2500 LB', '150–2500 LB'), [
        ('BX-0648-02-001', 'Ductile iron gate valves, resilient and metal seated', 'صمامات بوابة من الحديد المطيلي بمقعد مرن أو معدني', 'AWWA C509 / C515, BS 5163, EN 1171, DIN 3352', ('Flanged or socket ends', 'أطراف بشفة أو بقابس')),
        ('BX-0648-02-002', 'Ductile iron check valves', 'صمامات عدم رجوع من الحديد المطيلي', ('Swing, ball, dual-plate, wafer and lift types', 'أنواع متأرجحة وكروية ومزدوجة الألواح ورقاقية ورافعة'), ('Flanged or wafer', 'بشفة أو رقاقية')),
        ('BX-0648-02-003', 'Ductile iron globe valves', 'صمامات كروية الشكل من الحديد المطيلي', ('Straight and angle patterns, flanged', 'نمطان مستقيم وزاوي، بشفة'), ('Cast and ductile iron', 'حديد زهر ومطيلي')),
        ('BX-0648-02-004', 'Butterfly valves', 'صمامات فراشة', ('Wafer, lug and double-flanged; lever or gearbox', 'رقاقية وبعروات وبشفتين؛ بذراع أو علبة تروس'), ('Ductile iron bodies', 'أجسام من الحديد المطيلي')),
        ('BX-0648-02-005', 'Flanged ball valves', 'صمامات كروية بشفة', ('Two- and three-piece', 'من قطعتين أو ثلاث'), ('Cast and ductile iron', 'حديد زهر ومطيلي')),
        ('BX-0648-02-006', 'Y-strainers, air release valves and foot valves', 'مصافٍ Y وصمامات تنفيس الهواء وصمامات القدم', ('Single and double air valves', 'صمامات هواء مفردة ومزدوجة'), ('For pump suction and delivery lines', 'لخطوط سحب المضخات وطردها')),
        ('BX-0648-02-008', 'Flange adaptors, saddles, couplings, expansion and dismantling joints', 'وصلات شفاه وسروج وقارنات ووصلات تمدد وفك', ('Rubber expansion joints and dismantling joints', 'وصلات تمدد مطاطية ووصلات فك'), ('For connecting pipes, pumps and valves', 'لوصل الأنابيب والمضخات والصمامات')),
        ('BX-0648-03-001', 'Steel ball valves', 'صمامات كروية فولاذية', ('1PC, 2PC, 3PC, wafer; forged 800 / 1500 LB; 6000 psi high pressure; flanged 2PC / 3PC; DBB', 'قطعة وقطعتان وثلاث ورقاقية؛ مطروقة 800 / 1500 LB؛ ضغط عالٍ 6000 psi؛ بشفة 2PC / 3PC؛ DBB'), ('Carbon and stainless steel', 'فولاذ كربوني وستانلس')),
        ('BX-0648-03-002', 'Steel check valves', 'صمامات عدم رجوع فولاذية', ('Wafer spring, dual-plate, forged 800 LB', 'رقاقية بنابض ومزدوجة الألواح ومطروقة 800 LB'), ('Steel', 'فولاذ')),
        ('BX-0648-03-003', 'Steel gate and globe valves and strainers', 'صمامات بوابة وكروية الشكل فولاذية ومصافٍ', ('Forged 800 LB (1/2–2 in); pressure-seal gate 1500 / 2500 LB; flanged gate 150–1500 LB', 'مطروقة 800 LB ‏(1/2–2 بوصة)؛ بوابة بإحكام ضغطي 1500 / 2500 LB؛ بوابة بشفة 150–1500 LB'), ('Forged and cast steel', 'فولاذ مطروق ومصبوب')),
    ]),
], type_label=('Series', 'السلسلة'))

# p17 ductile iron & steel pipes, fittings & mining hoses ----------------------------------------------------
F['ductile-iron-steel-pipes-fittings-hoses'] = family('ductile-iron-steel-pipes-fittings-hoses', CAT, [
    series('series', ('Ductile iron and steel pipes, fittings and mining hoses', 'أنابيب ووصلات من الحديد المطيلي والفولاذ وخراطيم التعدين'), ('', ''), [
        ('BX-0648-01-001', 'Ductile iron pipes (ISO 2531 / EN 545 / EN 598)', 'أنابيب حديد مطيلي (ISO 2531 / EN 545 / EN 598)', ('Push-on joint pipes', 'أنابيب بوصلات دفع'), ('Push-on and restrained joints; for water and process lines', 'وصلات دفع ووصلات مقيّدة؛ لخطوط المياه والمعالجة')),
        ('BX-0648-01-002', 'Ductile iron fittings (ISO 2531 / EN 545 / EN 598 / BS 4772)', 'وصلات حديد مطيلي (ISO 2531 / EN 545 / EN 598 / BS 4772)', ('Bends, tees, crosses, tapers, collars, flanged and socket pieces', 'أكواع ووصلات T وصلبان ومخفّضات وأطواق وقطع بشفة وبقابس'), ('Flanged or socket ends', 'أطراف بشفة أو بقابس')),
        ('BX-0648-01-003', 'Ductile iron fittings to ANSI / AWWA C110', 'وصلات حديد مطيلي وفق ANSI / AWWA C110', ('Bends, tees, reducers and flanges', 'أكواع ووصلات T ومخفّضات وشفاه'), ('US standard fittings', 'وصلات بالمعيار الأمريكي')),
        ('BX-0648-01-004', 'Compact ductile iron fittings to ANSI / AWWA C153', 'وصلات حديد مطيلي مدمجة وفق ANSI / AWWA C153', ('Compact fittings', 'وصلات مدمجة'), ('US standard compact fittings', 'وصلات مدمجة بالمعيار الأمريكي')),
        ('BX-0648-01-005', 'Flange adaptors, couplings and dismantling joints', 'وصلات شفاه وقارنات ووصلات فك', ('Wide-range and dedicated flange adaptors and couplings', 'وصلات شفاه وقارنات واسعة المدى ومخصصة'), ('For pipes, pumps and valves', 'للأنابيب والمضخات والصمامات')),
        ('BX-0648-04-001', 'Steel butt-weld pipe fittings (ASME B16.9)', 'وصلات أنابيب فولاذية باللحام التناكبي (ASME B16.9)', ('Elbows incl. large diameter, equal, reducing and high-pressure tees, crosses, reducers, caps, flanges', 'أكواع منها كبيرة القطر، ووصلات T متساوية ومخفّضة وعالية الضغط، وصلبان ومخفّضات وأغطية وشفاه'),
         ('Carbon and alloy steel, seamless and welded; ASME B16.9 and B36.10M / B36.19M', 'فولاذ كربوني وسبائكي، ملحوم وغير ملحوم؛ ASME B16.9 وB36.10M / B36.19M')),
        ('BX-0648-04-002', 'Special steel fittings', 'وصلات فولاذية خاصة', ('Headers, laterals, flanged fittings', 'مجمّعات وتفرعات ووصلات بشفة'), ('Made to order', 'حسب الطلب')),
        ('BX-0341-02-001', 'Sand suction hose (material handling)', 'خرطوم شفط الرمل (مناولة المواد)', ('ID 4–12 in (102–305 mm); 10 m lengths', 'قطر داخلي 4–12 بوصة (102–305 مم)؛ أطوال 10 م'),
         ('WP 20 bar (300 psi), burst 60 bar; abrasion-resistant natural rubber; clamp or flange ends; −30 to +80 °C', 'ضغط تشغيل 20 بار (300 psi)، انفجار 60 بار؛ مطاط طبيعي مقاوم للتآكل؛ أطراف بمشبك أو شفة؛ من −30 إلى +80 °م')),
        ('BX-0341-02-002', 'Mineral sampling hose', 'خرطوم أخذ عينات المعادن', ('ID 2, 3, 4 in (51 / 76 / 102 mm); 61 m lengths', 'قطر داخلي 2 و3 و4 بوصات (51 / 76 / 102 مم)؛ أطوال 61 م'),
         ('WP 35 bar (525 psi), burst 105 bar; conductive abrasion-resistant NR tube; textile cord and steel helix', 'ضغط تشغيل 35 بار (525 psi)، انفجار 105 بار؛ أنبوب مطاط طبيعي موصل ومقاوم للتآكل؛ حبال نسيجية ولولب فولاذي')),
    ], unit={'ar': ['مجموعة واحدة', 'مجموعتان', 'مجموعات'], 'en': ['product group', 'product groups']}),
], type_label=('Series', 'السلسلة'))

# p18 knife gate valves (split body) & diaphragm pumps -------------------------------------------------------
KG = [C('models', 'Models / sizes', 'الموديلات والمقاسات'), C('data', 'Key data', 'أهم البيانات')]
F['knife-gate-valves-diaphragm-pumps'] = family('knife-gate-valves-diaphragm-pumps', CAT, [
    series('split', ('Knife gate valves – split-body series', 'الصمامات السكينية – سلاسل الجسم المنقسم'), ('DN50–DN4000', 'DN50–DN4000'), [
        ('BX-0754-01-001', 'Knife gate valve DFQB – unidirectional sealing', 'صمام سكيني DFQB – إحكام أحادي الاتجاه', 'DN50–DN1200', ('Slurry, sewage, pulp, chemicals, ore powder and slag', 'اللب والصرف ولب الورق والكيماويات ومسحوق الخام والخبث')),
        ('BX-0754-01-009', 'Knife gate valve DFQPA – split body, bi-directional, wear-resistant, replaceable PU seat', 'صمام سكيني DFQPA – جسم منقسم، ثنائي الاتجاه، مقاوم للتآكل، مقعد بولي يوريثان قابل للتبديل', 'DN50–DN600',
         ('Abrasive and highly alkaline ore slurry (copper, iron, nickel); −40 to 100 °C', 'لب خام كاشط وعالي القلوية (نحاس وحديد ونيكل)؛ من −40 إلى 100 °م')),
        ('BX-0754-01-010', 'Knife gate valve DFQJ – split body, bi-directional, fully rubber-lined, low pressure', 'صمام سكيني DFQJ – جسم منقسم، ثنائي الاتجاه، مبطن بالمطاط بالكامل، ضغط منخفض', 'DN50–DN400',
         ('Alkaline ore slurry, dilute acids and alkalis, slurries with solids; PN10', 'لب خام قلوي وأحماض وقلويات مخففة ولب بمواد صلبة؛ PN10')),
        ('BX-0754-01-013', 'Knife gate valve DFQMD – split body, bi-directional, medium pressure', 'صمام سكيني DFQMD – جسم منقسم، ثنائي الاتجاه، ضغط متوسط', 'DN50–DN4000', ('Alkaline slurries; PN10/PN16/150LB; −40 to 250 °C', 'لب قلوي؛ PN10/PN16/150LB؛ من −40 إلى 250 °م')),
        ('BX-0754-01-014', 'Knife gate valve DFQMDY – split body, bi-directional, medium pressure, with cover', 'صمام سكيني DFQMDY – جسم منقسم، ثنائي الاتجاه، ضغط متوسط، بغطاء', 'DN100–DN2000', ('Alkaline slurries; −40 to 120 °C', 'لب قلوي؛ من −40 إلى 120 °م')),
        ('BX-0754-01-015', 'Knife gate valve DFQMB – split body, bi-directional, wear-resistant, medium pressure', 'صمام سكيني DFQMB – جسم منقسم، ثنائي الاتجاه، مقاوم للتآكل، ضغط متوسط', 'DN50–DN2000',
         ('Wear-resistant guide ring; ore slurry with bi-directional sealing at PN16 and above (to PN40)', 'حلقة توجيه مقاومة للتآكل؛ لب خام بإحكام ثنائي الاتجاه عند PN16 فأعلى (حتى PN40)')),
        ('BX-0754-01-016', 'Knife gate valve DFQMG – split body, bi-directional sealing', 'صمام سكيني DFQMG – جسم منقسم، إحكام ثنائي الاتجاه', 'DN50–DN400', ('Wastewater, sewage and stormwater; PN10', 'مياه الصرف والمجاري ومياه الأمطار؛ PN10')),
    ], cols=KG),
    series('diaphragm', ('Pneumatic diaphragm pumps', 'المضخات الغشائية الهوائية'), ('1.62–63.6 m³/h', '1.62–63.6 م³/ساعة'), [
        ('BX-0422-01-020', 'Pneumatic diaphragm pumps (PP, aluminium, stainless steel)', 'مضخات غشائية هوائية (بولي بروبلين، ألومنيوم، ستانلس)', 'MK06/10, MK15, MK25, MK40, MK50, MK80',
         ('Flow 1.62–63.6 m³/h; head 70–84 m; solids to 9.4 mm; ports 3/8–3 in; Santoprene, PTFE, EPDM or NBR diaphragms; for filter-press feed and slurry transfer',
          'تدفق 1.62–63.6 م³/ساعة؛ رفع 70–84 م؛ مواد صلبة حتى 9.4 مم؛ منافذ 3/8–3 بوصات؛ أغشية سانتوبرين أو PTFE أو EPDM أو NBR؛ لتغذية مكابس الترشيح ونقل اللب'))
    ], cols=KG),
], type_label=('Series', 'السلسلة'))

# p19 knife gate valves – through-gate & self-sealing -------------------------------------------------------
F['knife-gate-valves-through-gate-self-sealing'] = family('knife-gate-valves-through-gate-self-sealing', CAT, [
    series('series', ('Through-gate & self-sealing series', 'سلاسل البوابة النافذة والإحكام الذاتي'), ('DN50–DN2000', 'DN50–DN2000'), [
        ('BX-0754-01-017', 'Knife gate valve DFQCA – bi-directional, through-type gate, low pressure', 'صمام سكيني DFQCA – ثنائي الاتجاه، بوابة نافذة، ضغط منخفض', 'DN50–DN1000', ('Low-pressure granules, dust, slag and mud', 'الحبيبات والغبار والخبث والطين بضغط منخفض')),
        ('BX-0754-01-018', 'Knife gate valve DFQCB – bi-directional, through-type gate, medium pressure', 'صمام سكيني DFQCB – ثنائي الاتجاه، بوابة نافذة، ضغط متوسط', 'DN50–DN1000', ('Medium-pressure ore slurry', 'لب الخام بضغط متوسط')),
        ('BX-0754-01-019', 'Knife gate valve DFQCG – bi-directional, through-type gate, centre guide', 'صمام سكيني DFQCG – ثنائي الاتجاه، بوابة نافذة، توجيه مركزي', 'DN100–DN1200', ('Medium-pressure ore slurry (copper, iron, nickel)', 'لب الخام (النحاس والحديد والنيكل) بضغط متوسط')),
        ('BX-0754-01-020', 'Knife gate valve DFQW – integral body, self-sealing, low pressure, replaceable seat', 'صمام سكيني DFQW – جسم متكامل، إحكام ذاتي، ضغط منخفض، مقعد قابل للتبديل', 'DN50–DN1000', ('Hydrocyclone ore slurry (copper, iron, nickel)', 'لب الخام في الهيدروسيكلونات (النحاس والحديد والنيكل)')),
        ('BX-0754-01-021', 'Knife gate valve DFQWF – two-piece body, self-sealing, low pressure', 'صمام سكيني DFQWF – جسم من قطعتين، إحكام ذاتي، ضغط منخفض', 'DN50–DN1000',
         ('PN10/PN16/150LB; body Q235, 304, 316L, 2205 or 2507; NR seat; −40 to 120 °C; flushing holes; hydrocyclone slurry', 'PN10/PN16/150LB؛ جسم Q235 أو 304 أو 316L أو 2205 أو 2507؛ مقعد مطاط طبيعي؛ من −40 إلى 120 °م؛ فتحات غسيل؛ لب الهيدروسيكلونات')),
        ('BX-0754-01-022', 'Knife gate valve DFQWLF – two-piece body, self-sealing, medium pressure', 'صمام سكيني DFQWLF – جسم من قطعتين، إحكام ذاتي، ضغط متوسط', 'DN100–DN2000',
         ('PN10/PN16/150LB; body Q235, 304, 316L, 2205 or 2507; NR seat; −40 to 120 °C; hydrocyclone slurry', 'PN10/PN16/150LB؛ جسم Q235 أو 304 أو 316L أو 2205 أو 2507؛ مقعد مطاط طبيعي؛ من −40 إلى 120 °م؛ لب الهيدروسيكلونات')),
        ('BX-0754-01-023', 'Knife gate valve DFQWL – integral body, self-sealing, medium pressure', 'صمام سكيني DFQWL – جسم متكامل، إحكام ذاتي، ضغط متوسط', 'DN100–DN2000', ('PN10/PN16/150LB; WCB body; NR seat; −40 to 120 °C; hydrocyclone slurry', 'PN10/PN16/150LB؛ جسم WCB؛ مقعد مطاط طبيعي؛ من −40 إلى 120 °م؛ لب الهيدروسيكلونات')),
        ('BX-0754-01-024', 'Knife gate valve DFQWLY – integral body, replaceable rubber seat ring', 'صمام سكيني DFQWLY – جسم متكامل، حلقة مقعد مطاطية قابلة للتبديل', 'DN100–DN2000',
         ('PN16/150LB; WCB body; NR seat; for cutter-suction dredgers, slurry and slag', 'PN16/150LB؛ جسم WCB؛ مقعد مطاط طبيعي؛ لكراكات القطع والشفط واللب والخبث')),
    ], cols=KG),
], type_label=('Series', 'السلسلة'))
