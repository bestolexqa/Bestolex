"""BXC-06 Ed7 (Ore processing & plants) model tables, catalogue pages 3–14. Typed from the page text and checked
against the page images where cells wrap. Every code is in the supplier list under BXC-06. The flotation plant row
carries two codes in the catalogue (plant and flotation separation plant); it takes the gold flotation plant code."""
from lib import table, family
from bxc02_tables import U_LINES

CAT = 'BXC-06 Ed7'
F = {}
U_PRODUCT = {'ar': ['منتج واحد', 'منتجان', 'منتجات'], 'en': ['product', 'products']}
U_PLANT = {'ar': ['نوع واحد', 'نوعان', 'أنواع'], 'en': ['plant type', 'plant types']}
U_SIZE = {'ar': ['مقاس لوح واحد', 'مقاسا لوح', 'مقاسات ألواح'], 'en': ['plate size', 'plate sizes']}
SERIES = [('models', 'Models / sizes', 'الموديلات والمقاسات'), ('data', 'Key data', 'أهم البيانات')]
C = lambda k, en, ar: (k, en, ar)
VOL = C('volume', 'Effective volume (m³)', 'الحجم الفعّال (م³)')
SPEED = C('speed', 'Impeller speed (r/min)', 'سرعة الدفّاعة (دورة/دقيقة)')
IMP = C('impeller', 'Impeller Ø (mm)', 'قطر الدفّاعة (مم)')
MOTOR = C('motor', 'Motor (kW)', 'المحرك (كيلوواط)')
TANK = C('tank', 'Tank Ø × height (mm)', 'قطر الحوض × الارتفاع (مم)')

# p3 complete gold processing plants -------------------------------------------------------------------------
F['complete-gold-processing-plants'] = family('complete-gold-processing-plants', CAT, [
    table('plants', ('Complete gold processing plants', 'مصانع معالجة الذهب المتكاملة'), ('Gravity, CIL / CIP, flotation', 'الجاذبية، CIL / CIP، التعويم'),
          [C('use', 'Ore and process', 'الخام والطريقة'), C('equipment', 'Main equipment', 'المعدات الرئيسية')],
          [('BX-0016-01-032', 'Gravity plant', 'مصنع الفصل بالجاذبية',
            ('For free-milling gold: crushing, grinding, classification and shaking tables, with low running cost and no chemicals',
             'للذهب الحر: تكسير وطحن وتصنيف وطاولات اهتزاز، بتكلفة تشغيل منخفضة وبلا كيماويات'),
            ('Jaw crusher, vibrating feeder and conveyors, ball mill, spiral classifier, shaking tables',
             'كسارة فكية، ومغذٍّ اهتزازي وسيور، وطاحونة كرات، ومصنّف حلزوني، وطاولات اهتزاز')),
           ('BX-0016-01-029', 'CIL / CIP plant', 'مصنع CIL / CIP',
            ('For fine and disseminated gold: leaching and carbon adsorption in the same tank train, then desorption, electrolysis and smelting',
             'للذهب الناعم والمنتشر: الإذابة والامتزاز على الكربون في سلسلة الأحواض نفسها، ثم الاستخلاص والتحليل الكهربائي والصهر'),
            ('Jaw crusher, vibrating screen, ball mill, hydrocyclone, thickener, leaching tanks, adsorption tanks, safety screens, desorption and electrolysis unit, filter press, melting furnace',
             'كسارة فكية، وغربال اهتزازي، وطاحونة كرات، وهيدروسيكلون، ومكثّف، وأحواض إذابة، وأحواض امتزاز، وغرابيل أمان، ووحدة استخلاص وتحليل كهربائي، ومكبس ترشيح، وفرن صهر')),
           ('BX-0016-01-030', 'Flotation plant', 'مصنع التعويم',
            ('For sulphide ores: grinding, conditioning with automatic reagent dosing and multi-stage flotation to a gold concentrate',
             'للخامات الكبريتيدية: طحن، وتكييف بجرعات كواشف آلية، وتعويم متعدد المراحل حتى مركّز الذهب'),
            ('Raw ore hopper, jaw and cone crushers, vibrating screen, belt conveyors, electromagnetic iron remover, vibrating feeder, energy-saving ball mill, hydrocyclone, agitation tanks, automatic reagent dosing, flotation machines, thickener, filter, dust collection for crushing and screening',
             'قادوس الخام، وكسارتان فكية ومخروطية، وغربال اهتزازي، وسيور ناقلة، ومزيل حديد كهرومغناطيسي، ومغذٍّ اهتزازي، وطاحونة كرات موفرة للطاقة، وهيدروسيكلون، وأحواض تقليب، وجرعات كواشف آلية، وآلات تعويم، ومكثّف، ومرشح، وتجميع غبار للتكسير والغربلة'))],
          intro=('Plant capacity and flowsheet are designed after ore testing.', 'تُصمَّم طاقة المصنع ومخطط المعالجة بعد اختبار الخام.'),
          unit=U_PLANT),
], type_label=('Plant', 'المصنع'), unit=U_PLANT)

# p4 flotation machines & agitation tanks --------------------------------------------------------------------
F['flotation-machines-agitation-tanks'] = family('flotation-machines-agitation-tanks', CAT, [
    table('sf-xjk', ('SF & XJK flotation machines', 'آلات التعويم SF وXJK'), ('0.13–4 m³ cells', 'خلايا 0.13–4 م³'),
          [C('cell', 'Cell volume (m³)', 'حجم الخلية (م³)'), IMP, C('capacity', 'Capacity (m³/min)', 'الطاقة (م³/دقيقة)'), SPEED,
           C('imp_motor', 'Impeller motor (kW)', 'محرك الدفّاعة (كيلوواط)'), C('scraper', 'Scraper motor (kW)', 'محرك الكاشطة (كيلوواط)')],
          [(None, 'SF0.37', None, '0.37', '300', '0.2–0.4', '352', '1.5', '1.1'),
           (None, 'SF0.7', None, '0.7', '350', '0.3–0.9', '400', '3', '1.1'),
           (None, 'SF1.2', None, '1.2', '450', '0.6–1.2', '312', '5.5', '1.1'),
           (None, 'SF2.8', None, '2.8', '550', '1.5–3.5', '268', '11', '1.1'),
           (None, 'SF4', None, '4', '650', '2–4', '238', '15', '1.5'),
           (None, 'XJK-0.13 (1A)', None, '0.13', '200', '0.05–0.16', '600', '2.2', '0.55'),
           (None, 'XJK-0.23 (2A)', None, '0.23', '250', '0.12–0.28', '500', '1.5', '0.55'),
           (None, 'XJK-0.35 (3A)', None, '0.35', '300', '0.18–0.4', '470', '1.5', '0.75'),
           (None, 'XJK-0.62 (4A)', None, '0.62', '350', '0.3–0.9', '400', '3', '0.75'),
           (None, 'XJK-1.1 (5A)', None, '1.1', '500', '0.6–1.6', '330', '5.5', '1.1'),
           (None, 'XJK-2.8 (6A)', None, '2.8', '600', '1.5–3.5', '280', '11', '1.1')],
          code='BX-0016-01-011', key_rows=['cell', 'capacity', 'imp_motor']),
    table('xb', ('XB agitation tanks', 'أحواض التقليب XB'), ('0.098–30 m³', '0.098–30 م³'),
          [TANK, VOL, SPEED, IMP, MOTOR, C('weight', 'Weight (t)', 'الوزن (طن)')],
          [(None, 'XB-500', None, '500 × 500', '0.098', '600', '200', '1.1', '0.15'),
           (None, 'XB-750', None, '750 × 750', '0.33', '530', '255', '1.5', '0.6'),
           (None, 'XB-1000', None, '1000 × 1000', '0.58', '530', '255', '1.5', '0.99'),
           (None, 'XB-1200', None, '1200 × 1200', '1.4', '300', '400', '3', '1.05'),
           (None, 'XB-1500', None, '1500 × 1500', '2.2', '320', '400', '3', '1.2'),
           (None, 'XB-2000', None, '2000 × 2000', '5.46', '230', '550', '5.5', '1.6'),
           (None, 'XB-2500', None, '2500 × 2500', '11.2', '230', '650', '11', '3.44'),
           (None, 'XB-3000', None, '3000 × 3000', '19.1', '210', '700', '18.5', '4.16'),
           (None, 'XB-3500', None, '3500 × 3500', '30', '230', '850', '22', '7.28')],
          code='BX-0016-01-013', key_rows=['volume', 'motor', 'tank']),
])

# p5 flotation, agitation & thickening – additional series ---------------------------------------------------
F['flotation-agitation-thickening-additional'] = family('flotation-agitation-thickening-additional', CAT, [
    table('flotation', ('Flotation machines and agitation tanks – additional series', 'آلات التعويم وأحواض التقليب – سلاسل إضافية'), ('0.15–65 m³', '0.15–65 م³'),
          [C('models', 'Models', 'الموديلات'), C('volume', 'Cell / tank volume (m³)', 'حجم الخلية أو الحوض (م³)'), C('capacity', 'Capacity (m³/min)', 'الطاقة (م³/دقيقة)'), C('power', 'Power (kW)', 'القدرة (كيلوواط)')],
          [('BX-0033-01-018', 'SF flotation machine – large cells', 'آلة تعويم SF – خلايا كبيرة', 'SF-8, SF-10, SF-16, SF-20', '8–20', '4–20', '30–55'),
           ('BX-0033-01-018', 'JJF flotation machine', 'آلة تعويم JJF', 'JJF-2, JJF-4, JJF-8, JJF-10, JJF-16, JJF-20', '2–20', '1–20', '11–37'),
           ('BX-0033-01-019', 'BF flotation machine', 'آلة تعويم BF', ('BF-0.15 to BF-8.0 (10 sizes)', 'من BF-0.15 إلى BF-8.0 ‏(10 مقاسات)'), '0.15–8', ('from 0.06', 'من 0.06'), '–'),
           ('BX-0033-01-020', 'BS-K flotation machine', 'آلة تعويم BS-K', ('BS-K2.2 to BS-K38 (7 sizes)', 'من BS-K2.2 إلى BS-K38 ‏(7 مقاسات)'), '2.2–38', '0.5–30', '5.5–45'),
           ('BX-0033-01-021', 'KYF / XCF air-forced flotation machine', 'آلة تعويم بالهواء المدفوع KYF / XCF', ('KYF-1 to KYF-50 and XCF-1 to XCF-50 (18 sizes)', 'من KYF-1 إلى KYF-50 ومن XCF-1 إلى XCF-50 ‏(18 مقاساً)'), '1–50', '0.2–50', '4–90'),
           ('BX-0033-01-022', 'TSO agitation tank', 'حوض تقليب TSO', 'TSO-750, TSO-1200, TSO-1500', '0.44–2.2', '–', '3–11'),
           ('BX-0033-01-024', 'GBJ high-efficiency agitation tank', 'حوض تقليب عالي الكفاءة GBJ', ('GBJ-1000×1000 to GBJ-4000×4000 (7 sizes)', 'من GBJ-1000×1000 إلى GBJ-4000×4000 ‏(7 مقاسات)'), '0.58–45', '–', '3–37'),
           ('BX-0033-01-026', 'XBN high-concentration mixing tank', 'حوض خلط عالي التركيز XBN', ('XBN-1000×1000 to XBN-4500×4500 (7 sizes)', 'من XBN-1000×1000 إلى XBN-4500×4500 ‏(7 مقاسات)'), '0.55–65', '–', '5.5–45')],
          key_rows=['volume', 'power', 'models'], unit=U_LINES),
    table('thickeners', ('Thickeners – additional series', 'المكثّفات – سلاسل إضافية'), ('2.5–20 m', '2.5–20 م'),
          [C('models', 'Models', 'الموديلات'), C('dia', 'Tank Ø (m)', 'قطر الحوض (م)'), C('area', 'Settling area (m²)', 'مساحة الترسيب (م²)'), C('power', 'Power (kW)', 'القدرة (كيلوواط)')],
          [('BX-0033-01-036', 'NZS centre-drive thickener – additional sizes', 'مكثّف بإدارة مركزية NZS – مقاسات إضافية', 'NZS2.5, NZS8', '2.5 / 8', '4.9 / 50.2', '1.1 / 3'),
           ('BX-0033-01-039', 'NZSG high-efficiency thickener', 'مكثّف عالي الكفاءة NZSG', ('NZSG-2.5 to NZSG-20 (12 sizes)', 'من NZSG-2.5 إلى NZSG-20 ‏(12 مقاساً)'), '2.5–20', '–', '1.1–7.5'),
           ('BX-0033-01-040', 'GX high-efficiency thickener', 'مكثّف عالي الكفاءة GX', 'GX-3.6, GX-5.18, GX-9, GX-12, GX-15', '3.6–15', '10–176', '1.5–11')],
          key_rows=['dia', 'area', 'power'], unit=U_LINES),
], type_label=('Series', 'السلسلة'))

# p6 leaching tanks ------------------------------------------------------------------------------------------
SJ = [('SJ2.0×2.5', '2000 × 2500', '7.07', '52', '909', '2.2', '2144'), ('SJ2.5×2.5', '2500 × 2500', '10.8', '43', '935', '4', '2729'),
      ('SJ2.5×3.15', '2500 × 3150', '13.92', '52', '935', '2.2', '3095'), ('SJ3.0×3.0', '3000 × 3000', '19', '43', '1130', '4', '4583'),
      ('SJ3×3.15', '3000 × 3150', '20', '43', '1130', '4', '4160.6'), ('SJ3×3.5', '3000 × 3500', '22.97', '43', '1130', '4', '4334.6'),
      ('SJ3.15×3.55', '3150 × 3550', '25.73', '43', '1260', '4', '4322.8'), ('SJ3.5×3.5', '3500 × 3500', '31.3', '52', '1310', '5.5', '5025'),
      ('SJ3.5×4', '3500 × 4000', '35.6', '52', '1310', '5.5', '5429'), ('SJ3.55×4', '3550 × 4000', '36.8', '43', '1310', '4', '5025'),
      ('SJ3.7×4.2', '3700 × 4200', '42', '42', '1310', '4', '6153'), ('SJ4.0×4.5', '4000 × 4500', '52.78', '35', '1750', '7.5', '7569'),
      ('SJ4.0×6', '4000 × 6000', '71', '33', '1750', '11', '9200'), ('SJ4.5×5.0', '4500 × 5000', '74.75', '35', '1750', '7.5', '10864'),
      ('SJ5.0×5.6', '5000 × 5600', '104.5', '31', '2046', '11', '14291'), ('SJ5.5×6.0', '5500 × 6000', '135.42', '31', '2100', '11', '18745'),
      ('SJ6.5×7.0', '6500 × 7000', '215', '21', '2400', '22', '25978'), ('SJ7.0×7.5', '7000 × 7500', '269', '21', '2400', '22', '29030'),
      ('SJ7.5×8.0', '7500 × 8000', '331', '23', '2900', '22', '32796'), ('SJ8.0×8.5', '8000 × 8500', '402', '18.5', '3200', '30', '42467.3'),
      ('SJ8.5×9.0', '8500 × 9000', '480', '18.5', '3300', '30', '46623'), ('SJ10.5×11.0', '10500 × 11000', '900', '13.28', '4400', '55', '72647'),
      ('SJ11.5×12.0', '11500 × 12000', '1190', '12.1', '4600', '75', '95669')]
F['leaching-tanks'] = family('leaching-tanks', CAT, [
    table('sj', ('SJ mechanically agitated leaching tanks', 'أحواض الإذابة SJ بالتقليب الميكانيكي'), ('7–1190 m³', '7–1190 م³'),
          [TANK, VOL, SPEED, IMP, MOTOR, C('weight', 'Gross weight (kg)', 'الوزن الإجمالي (كجم)')],
          [(None, m, None, *v) for m, *v in SJ],
          intro=('Tank body of steel plate or concrete, lined with acid-resistant material (such as ceramic tile or epoxy glass fibre) as required.',
                 'جسم الحوض من ألواح الفولاذ أو الخرسانة، ويُبطَّن عند الحاجة بمادة مقاومة للأحماض مثل البلاط الخزفي أو ألياف الزجاج بالإيبوكسي.'),
          code='BX-0028-01-036', key_rows=['volume', 'motor', 'tank']),
])

# p7 elution, electrowinning & heap leaching -----------------------------------------------------------------
GK = [('GKJD-200', '<150', '2–8'), ('GKJD-300', '150–300', '2–8'), ('GKJD-500', '300–500', '2–8'), ('GKJD-700', '300–500', '2–8'),
      ('GKJD-1000', '500–1000', '2–8'), ('GKJD-1500', '500–1000', '2–8'), ('GKJD-2000', '1000–2000', '2–20'), ('GKJD-2500', '1000–2000', '2–20'),
      ('GKJD-3000', '1000–2000', '2–20'), ('GKJD-3500', '2000–3000', '2–20'), ('GKJD-4000', '2000–3000', '2–20'), ('GKJD-5000', '2000–3000', '2–20'),
      ('GKJD-8000', '3000–5000', '2–20')]
F['elution-electrowinning-heap-leaching'] = family('elution-electrowinning-heap-leaching', CAT, [
    table('gkjd', ('GKJD elution & electrowinning sets', 'وحدات الاستخلاص والتحليل الكهربائي GKJD'), ('<150–5000 t/d mines', 'مناجم <150–5000 طن/يوم'),
          [C('scale', 'Mine scale (t/d)', 'حجم المنجم (طن/يوم)'), C('grade', 'Ore grade (g/t)', 'رتبة الخام (جم/طن)')],
          [(None, m, None, s, g) for m, s, g in GK],
          intro=('Operating parameters: working temperature 150 ± 2 °C; solution (NaOH) pH ≥ 13.5; elution cell pressure 0.5 MPa; electrowinning cell pressure 0.45 MPa.',
                 'بيانات التشغيل: حرارة العمل 150 ± 2 °م؛ ودرجة pH للمحلول (NaOH) ‏≥ 13.5؛ وضغط خلية الاستخلاص 0.5 ميجاباسكال؛ وضغط خلية التحليل الكهربائي 0.45 ميجاباسكال.'),
          code='BX-0028-01-035', key_rows=['scale', 'grade']),
    table('heap', ('Gold heap-leaching process (turnkey)', 'الإذابة الكومية للذهب (تسليم مفتاح)'), ('', ''),
          [C('steps', 'Process', 'المراحل'), C('equipment', 'Circuit equipment', 'معدات الدائرة')],
          [('BX-0028-01-047', 'Heap-leaching circuit', 'دائرة الإذابة الكومية',
            ('Crushing (or agglomeration) of low-grade ore; stacking on an impermeable asphalt or plastic pad; dilute leaching solution sprayed over the heap; the gold-bearing solution pumped to carbon adsorption, then elution and electrowinning',
             'تكسير الخام منخفض الرتبة (أو تكتيله)؛ ثم تكديسه على أرضية عازلة من الأسفلت أو البلاستيك؛ ثم رش محلول الإذابة المخفف فوق الكومة؛ ثم ضخ المحلول الحامل للذهب إلى أحواض الامتزاز على الكربون، ثم الاستخلاص والتحليل الكهربائي'),
            ('Vibrating feeder, jaw and cone crushers, circular vibrating screen, belt conveyors, pregnant-solution pump, adsorption tanks with air lifters, carbon sieves and fine-carbon safety screen, spray pump',
             'مغذٍّ اهتزازي، وكسارتان فكية ومخروطية، وغربال اهتزازي دائري، وسيور ناقلة، ومضخة المحلول الحامل، وأحواض امتزاز برافعات هوائية، ومناخل الكربون وغربال أمان للكربون الناعم، ومضخة رش'))],
          unit=U_PRODUCT),
])

# p8 rotary dryers ------------------------------------------------------------------------------------------
D1 = [('Ø1.2 × 10', '11.3', '2.4–3.0', '7.5'), ('Ø1.2 × 12', '13.5', '2.4–4.5', '7.5'), ('Ø1.5 × 12', '21.2', '4.5–5.7', '15'),
      ('Ø1.5 × 15', '26.5', '5.7–7.1', '15'), ('Ø1.8 × 14', '35.6', '7.6–9.7', '18.5'), ('Ø1.8 × 20', '50.8', '9–12.5', '22'),
      ('Ø2.0 × 16', '50.24', '9.5–13', '18.5'), ('Ø2.0 × 20', '62.8', '9.5–13', '30'), ('Ø2.2 × 12', '45.6', '9.7–12.2', '22'),
      ('Ø2.2 × 16', '60.8', '13.0–16.2', '22'), ('Ø2.4 × 18', '81.4', '17.4–21.7', '37'), ('Ø2.4 × 20', '90.4', '19.3–24.1', '45'),
      ('Ø2.4 × 22', '99.5', '21.2–26.5', '45'), ('Ø2.6 × 24', '127.4', '27.2–34.0', '55'), ('Ø3.0 × 20', '141.3', '30.1–37.7', '75'),
      ('Ø3.0 × 25', '176.6', '37.7–47.1', '75')]
D3 = [('Ø2.0 × 4', '12.56', '8–15', '5.5 × 2'), ('Ø2.2 × 5', '18.99', '12–20', '5.5 × 2'), ('Ø2.5 × 6', '29.43', '18–28', '7.5 × 2'),
      ('Ø2.8 × 6', '36.92', '25–35', '11 × 2'), ('Ø3.0 × 6', '42.39', '30–40', '7.5 × 4'), ('Ø3.0 × 7', '49.45', '30–45', '7.5 × 4'),
      ('Ø3.2 × 7', '56.27', '35–55', '11 × 4'), ('Ø3.6 × 8', '81.39', '55–75', '18.5 × 4'), ('Ø4.0 × 10', '125.6', '70–100', '22 × 4')]
CAPTH = C('capacity', 'Capacity (t/h)', 'الطاقة (طن/ساعة)')
F['rotary-dryers'] = family('rotary-dryers', CAT, [
    table('single', ('Single-pass rotary dryers', 'مجففات دوّارة أحادية المسار'), ('2.4–47.1 t/h', '2.4–47.1 طن/ساعة'),
          [C('volume', 'Volume (m³)', 'الحجم (م³)'), CAPTH, C('incl', 'Inclination (%)', 'الميل (%)'), C('inlet', 'Max. inlet temp. (°C)', 'أقصى حرارة دخول (°م)'), MOTOR],
          [(None, m, None, v, c, '3–5', '700–800', k) for m, v, c, k in D1],
          code='BX-0016-01-017', key_rows=['capacity', 'motor', 'volume']),
    table('triple', ('Triple-pass rotary dryers', 'مجففات دوّارة ثلاثية المسار'), ('8–100 t/h', '8–100 طن/ساعة'),
          [C('volume', 'Volume (m³)', 'الحجم (م³)'), C('rpm', 'Speed (r/min)', 'السرعة (دورة/دقيقة)'), C('air', 'Max. air temp. (°C)', 'أقصى حرارة للهواء (°م)'), CAPTH, C('power', 'Power (kW)', 'القدرة (كيلوواط)')],
          [(None, m, None, v, '4–10', '700–750', c, k) for m, v, c, k in D3],
          intro=('Thermal efficiency up to 70%; discharge at about 80 °C. Fuel: coal, oil, gas or wood.', 'كفاءة حرارية حتى 70%، والتفريغ عند نحو 80 °م. الوقود: فحم أو زيت أو غاز أو حطب.'),
          code='BX-0016-01-018', key_rows=['capacity', 'power', 'volume']),
], type_label=('Model (Ø × L, m)', 'الموديل (القطر × الطول، م)'))

# p9 rotary kilns -------------------------------------------------------------------------------------------
K = [('Ø2.5 × 40', '180', '0.44–2.44', '55', '150'), ('Ø2.5 × 50', '200', '0.62–1.86', '55', '187'), ('Ø2.5 × 54', '280', '0.48–1.45', '55', '197'),
     ('Ø2.7 × 42', '320', '0.10–1.52', '55', '200'), ('Ø2.8 × 44', '450', '0.437–2.18', '55', '210'), ('Ø3.0 × 45', '500', '0.5–2.47', '75', '220'),
     ('Ø3.0 × 48', '700', '0.6–3.48', '100', '237'), ('Ø3.0 × 60', '800', '0.3–2', '100', '310'), ('Ø3.2 × 50', '1000', '0.6–3', '125', '278'),
     ('Ø3.3 × 52', '1300', '0.266–2.66', '125', '283'), ('Ø3.5 × 54', '1500', '0.55–3.4', '220', '363'), ('Ø3.6 × 70', '1800', '0.25–1.25', '125', '419'),
     ('Ø4.0 × 56', '2300', '0.41–4.07', '315', '456'), ('Ø4.0 × 60', '2500', '0.396–3.96', '315', '510'), ('Ø4.2 × 60', '2750', '0.41–4.07', '375', '633'),
     ('Ø4.3 × 60', '3200', '0.396–3.96', '375', '583'), ('Ø4.5 × 66', '4000', '0.41–4.1', '560', '710'), ('Ø4.7 × 74', '4500', '0.35–4', '630', '849'),
     ('Ø4.8 × 74', '5000', '0.396–3.96', '630', '899'), ('Ø5.0 × 74', '6000', '0.35–4', '710', '944'), ('Ø5.6 × 87', '8000', ('max. 4.23', 'حتى 4.23'), '800', '1265')]
F['rotary-kilns'] = family('rotary-kilns', CAT, [
    table('kilns', ('Rotary kilns', 'الأفران الدوّارة'), ('180–8000 t/d', '180–8000 طن/يوم'),
          [C('incl', 'Inclination (%)', 'الميل (%)'), C('capacity', 'Capacity (t/d)', 'الطاقة (طن/يوم)'), C('rpm', 'Speed (r/min)', 'السرعة (دورة/دقيقة)'), MOTOR, C('weight', 'Weight (t)', 'الوزن (طن)')],
          [(None, m, None, '3–5', c, s, k, w) for m, c, s, k, w in K],
          intro=('For magnetic roasting of iron ore, oxidising roasting, and calcining of bauxite, chrome ore, lime, dolomite and cement clinker.',
                 'للتحميص المغناطيسي لخام الحديد، والتحميص المؤكسد، وتكليس البوكسيت وخام الكروم والجير والدولوميت وكلنكر الإسمنت.'),
          code='BX-0016-01-019', key_rows=['capacity', 'motor', 'weight']),
], type_label=('Model (Ø × L, m)', 'الموديل (القطر × الطول، م)'))

# p10 thickeners --------------------------------------------------------------------------------------------
DIA, DEPTH, AREA = C('dia', 'Tank Ø (m)', 'قطر الحوض (م)'), C('depth', 'Depth (m)', 'العمق (م)'), C('area', 'Settling area (m²)', 'مساحة الترسيب (م²)')
CAPTD = C('capacity', 'Capacity (t/d)', 'الطاقة (طن/يوم)')
WT = C('weight', 'Weight (t)', 'الوزن (طن)')
CD = [('NZS-1', '1.8', '1.8', '2.54', '2', '0.16', '5.6', '1.1', '–', '1.235'), ('NZS-3', '3.6', '1.8', '10.2', '2.5', '0.35', '22.4', '1.1', '–', '3.194'),
      ('NZS-6', '6', '3', '28.3', '3.7', '0.2', '62', '1.1', '–', '8.751'), ('NZS-9', '9', '3', '63.6', '4.34', '0.35', '140', '3', '–', '5.1'),
      ('NZF-9', '9', '3', '63.6', '4.34', '0.25', '140', '3', '0.8', '5.36'), ('NZS-12', '12', '3.5', '113', '5.28', '0.25', '250', '3', '–', '8.51'),
      ('NZ-15', '15', '4.4', '176', '10.4', '0.4', '350', '5.2', '2.2', '21.757'), ('NZ-20', '20', '4.4', '314', '10.4', '0.4', '960', '5.2', '2.2', '24.504')]
PD = [('NG-15', '15', '3.5', '177', '8.4', '390', '15.36', '–', 'Y132M2-6', '5.5', '960', '9.12'), ('NT-15', '15', '3.5', '177', '8.4', '390', '–', '15.56', 'Y132M2-6', '5.5', '960', '11'),
      ('NG-18', '18', '3.5', '255', '10', '560', '18.36', '–', 'Y132M2-6', '5.5', '960', '10'), ('NT-18', '18', '3.5', '255', '10', '560', '–', '18.57', 'Y132M2-6', '5.5', '960', '12.1'),
      ('NG-24', '24', '3.4', '452', '12.7', '1000', '24.36', '–', 'Y160M-6', '7.5', '970', '23.3'), ('NT-24', '24', '3.4', '452', '12.7', '1000', '–', '24.88', 'Y160M-6', '7.5', '970', '28.3'),
      ('NG-30', '30', '3.6', '707', '16', '1570', '30.36', '–', 'Y160M-6', '7.5', '970', '26.4'), ('NT-30', '30', '3.6', '707', '16', '1570', '–', '30.88', 'Y160M-6', '7.5', '970', '31.3'),
      ('NT-38', '38', '5.06', '1134', '24.3', '1600', '38.383', '38.629', 'Y160L-8', '7.5', '970', '59.82'), ('NT-45', '45', '5.06', '1590', '19.3', '2400', '45.383', '45.62', 'Y160L-6', '11', '970', '58.64'),
      ('NT-50', '50', '5.05', '1964', '21.7', '3000', '51.779', '52.025', 'Y160L-6', '11', '970', '65.92'), ('NT-53', '53', '5.07', '2202', '23.18', '3400', '55.16', '55.406', 'Y160L-6', '11', '970', '69.44'),
      ('NT-100', '100', '5.65', '7846', '43', '3030', '100.5', '100.77', 'Y180L-6', '15', '970', '198.08')]
F['thickeners'] = family('thickeners', CAT, [
    table('centre', ('Centre-drive thickeners', 'مكثّفات بإدارة مركزية'), ('1.8–20 m', '1.8–20 م'),
          [DIA, DEPTH, AREA, C('rev', 'Rake rev. time (min)', 'زمن دورة الكاشطة (دقيقة)'), C('lift', 'Rake lift (m)', 'رفع الكاشطة (م)'), CAPTD,
           C('drive', 'Drive (kW)', 'الإدارة (كيلوواط)'), C('lifting', 'Lifting (kW)', 'الرفع (كيلوواط)'), WT],
          [(None, *r[:1], None, *r[1:]) for r in CD],
          code='BX-0028-01-039', key_rows=['dia', 'capacity', 'drive']),
    table('peripheral', ('Peripheral-drive thickeners', 'مكثّفات بإدارة طرفية'), ('15–100 m', '15–100 م'),
          [DIA, DEPTH, AREA, C('rev', 'Rake rev. (min)', 'دورة الكاشطة (دقيقة)'), CAPTD, C('roller', 'Roller track Ø (m)', 'قطر مسار البكرات (م)'),
           C('rack', 'Rack track Ø (m)', 'قطر مسار الجريدة المسننة (م)'), C('motor', 'Motor', 'المحرك'), WT],
          [(None, r[0], None, *r[1:8], f'{r[8]} · {r[9]} kW · {r[10]} r/min', r[11]) for r in PD],
          intro=('NG = roller track drive; NT = rack track drive.', 'NG = إدارة على مسار بكرات؛ NT = إدارة على مسار جريدة مسننة.'),
          code='BX-0028-01-039', key_rows=['dia', 'capacity', 'motor']),
])

# p11 filter presses & reagent dosing -----------------------------------------------------------------------
FP = [('800×800×60', '20–80/800U', '20–80', '20–80', '30', '0.287–1.21', '2.2', '2750–4740', '3.5–7.16 × 1.35 × 1.16'),
      ('900×900×60', '40–70/900U', '40–70', '32–63', '30', '0.59–1.19', '2.2', '4500–5700', '4.23–6.12 × 1.48 × 1.28'),
      ('1000×1000×60', '60–120/1000U', '60–120', '38–75', '30', '0.9–1.8', '2.2', '7080–9250', '5.45–7.71 × 1.56 × 1.36'),
      ('1250×1250×65', '125–250/1250U', '125–250', '46–95', '32', '1.9–3.98', '4', '10900–14800', '6.5–9.74 × 1.77 × 1.62'),
      ('1500×1500×70', '300–500/1500U', '300–500', '77–128', '32', '4.76–7.96', '5.5', '26500–33390', '10.04–13.66 × 2.4 × 1.8'),
      ('2000×2000×83', '560–1180/2000U', '560–1180', '80–168', '40', '11.16–23.61', '11', '56500–79000', '10.6–19 × 2.9 × 2.45')]
F['filter-presses-reagent-dosing'] = family('filter-presses-reagent-dosing', CAT, [
    table('xmaz', ('X(M/A)Z automatic chamber filter presses', 'مكابس ترشيح حجرية آلية X(M/A)Z'), ('20–1180 m²', '20–1180 م²'),
          [C('models', 'Models', 'الموديلات'), C('area', 'Filter area (m²)', 'مساحة الترشيح (م²)'), C('chambers', 'Chambers', 'عدد الحجرات'), C('cake', 'Cake (mm)', 'سماكة الكعكة (مم)'),
           C('vol', 'Chamber vol. (m³)', 'حجم الحجرات (م³)'), MOTOR, C('weight', 'Weight (kg)', 'الوزن (كجم)'), C('dims', 'L × W × H (m)', 'الطول × العرض × الارتفاع (م)')],
          [(None, f'{p} mm', f'{p} مم', *v) for p, *v in FP],
          intro=('Filtration pressure 0.5–1.6 MPa for all sizes. Full model list per plate size on request.', 'ضغط الترشيح 0.5–1.6 ميجاباسكال لكل المقاسات. القائمة الكاملة للموديلات لكل مقاس لوح عند الطلب.'),
          code='BX-0028-01-041', key_rows=['area', 'chambers', 'motor'], unit=U_SIZE),
    table('dosing', ('HGGY-B CNC reagent dosing machine', 'آلة جرعات الكواشف HGGY-B بالتحكم الرقمي'), ('', ''), [C('desc', 'Description', 'الوصف')],
          [('BX-0028-01-024', 'HGGY-B reagent dosing machine', 'آلة جرعات الكواشف HGGY-B',
            ('Third-generation dosing machine with PLC control and an LCD touch screen; doses flotation reagents precisely for ferrous, non-ferrous and non-metallic ores and coal, replacing inaccurate manual dosing and the recovery losses it causes',
             'آلة جرعات من الجيل الثالث بتحكم PLC وشاشة لمس LCD؛ تضبط جرعات كواشف التعويم بدقة لخامات الحديد والمعادن غير الحديدية واللافلزية والفحم، بدل الجرعات اليدوية غير الدقيقة وما تسببه من فقد في الاستخلاص'))],
          unit=U_PRODUCT),
], type_label=('Plate size', 'مقاس اللوح'))

# p12 membrane & chamber filter presses ---------------------------------------------------------------------
M = lambda code, plate, models, area, data: (code, f'Membrane filter press – {plate} mm plates', f'مكبس ترشيح غشائي – ألواح {plate} مم', models, (area[0] + '; ' + data[0], area[1] + '؛ ' + data[1]))
CH = lambda code, plate, models, area, data: (code, f'Chamber filter press – {plate} mm plates', f'مكبس ترشيح حجري – ألواح {plate} مم', models, (area[0] + '; ' + data[0], area[1] + '؛ ' + data[1]))
F['membrane-chamber-filter-presses'] = family('membrane-chamber-filter-presses', CAT, [
    table('membrane', ('Membrane filter presses (XMG)', 'مكابس الترشيح الغشائية (XMG)'), ('30–1000 m²', '30–1000 م²'), SERIES,
          [M('BX-0422-01-003', '870×870', 'XMG(Y/Z)30/870, 40/870, 50/870, 60/870, 80/870', ('30–80 m²', '30–80 م²'), ('cake 30 mm; chambers 427–1103 L; 23–61 plates; 2.2 kW; length 3.9–6.4 m', 'كعكة 30 مم؛ الحجرات 427–1103 لتر؛ 23–61 لوحاً؛ 2.2 كيلوواط؛ الطول 3.9–6.4 م')),
           M('BX-0422-01-004', '1000×1000', 'XMG(Y/Z)50/1000, 60/1000, 70/1000, 80/1000, 120/1000', ('50–120 m²', '50–120 م²'), ('cake 30 mm; chambers 665–1663 L; 27–69 plates; 4 kW; length 4.3–7.3 m', 'كعكة 30 مم؛ الحجرات 665–1663 لتراً؛ 27–69 لوحاً؛ 4 كيلوواط؛ الطول 4.3–7.3 م')),
           M('BX-0422-01-005', '1250×1250', 'XMG(Y/Z)80/1250, 100/1250, 120/1250, 150/1250, 200/1250, 240/1250, 250/1250', ('80–250 m²', '80–250 م²'), ('cake 35 mm; chambers 1365–4186 L; 29–91 plates; 5.5 kW; length 5.0–9.8 m', 'كعكة 35 مم؛ الحجرات 1365–4186 لتراً؛ 29–91 لوحاً؛ 5.5 كيلوواط؛ الطول 5.0–9.8 م')),
           M('BX-0422-01-006', '1500×1500', 'XMG(Y/Z)200/1500, 250/1500, 300/1500, 400/1500, 450/1500, 500/1500', ('200–500 m²', '200–500 م²'), ('cake 35 mm; chambers 3332–8264 L; 49–123 plates; 7.5 kW; length 7.3–13.4 m', 'كعكة 35 مم؛ الحجرات 3332–8264 لتراً؛ 49–123 لوحاً؛ 7.5 كيلوواط؛ الطول 7.3–13.4 م')),
           M('BX-0422-01-007', '2000×2000', 'XMG(Y/Z)500/2000, 600/2000, 700/2000, 900/2000, 1000/2000', ('500–1000 m²', '500–1000 م²'), ('cake 40 mm; chambers 9936–19872 L; 71–143 plates; 7.5 kW; length 11.6–18.6 m', 'كعكة 40 مم؛ الحجرات 9936–19872 لتراً؛ 71–143 لوحاً؛ 7.5 كيلوواط؛ الطول 11.6–18.6 م'))],
          intro=('Membrane presses squeeze the cake for lower moisture. Y = hydraulic, Z = automatic pull-plate.', 'المكابس الغشائية تعصر الكعكة لرطوبة أقل. Y = هيدروليكي، Z = سحب آلي للألواح.'),
          unit=U_SIZE),
    table('chamber', ('Chamber filter presses (XM)', 'مكابس الترشيح الحجرية (XM)'), ('1–1000 m²', '1–1000 م²'), SERIES,
          [CH('BX-0422-01-008', '380×380', 'XMQ1/380, 2/380, 3/380', ('1–3 m²', '1–3 م²'), ('cake 30 mm; chambers 15–45 L; 4–14 plates; manual hand-jack pressing; length 1.3–1.7 m', 'كعكة 30 مم؛ الحجرات 15–45 لتراً؛ 4–14 لوحاً؛ ضغط يدوي برافعة؛ الطول 1.3–1.7 م')),
           CH('BX-0422-01-009', '500×500', 'XM(Y/Z)4/500, 8/500, 12/500', ('4–12 m²', '4–12 م²'), ('cake 30 mm; chambers 60–180 L; 9–29 plates; 2.2 kW; length 2.0–3.0 m', 'كعكة 30 مم؛ الحجرات 60–180 لتراً؛ 9–29 لوحاً؛ 2.2 كيلوواط؛ الطول 2.0–3.0 م')),
           CH('BX-0422-01-010', '700×700', 'XM(Y/Z)15/700, 20/700, 30/700, 40/700', ('15–40 m²', '15–40 م²'), ('cake 30 mm; chambers 226–595 L; 18–49 plates; 2.2 kW; length 2.8–4.4 m', 'كعكة 30 مم؛ الحجرات 226–595 لتراً؛ 18–49 لوحاً؛ 2.2 كيلوواط؛ الطول 2.8–4.4 م')),
           CH('BX-0422-01-011', '870×870', 'XM(Y/Z)30/870, 40/870, 50/870, 60/870, 80/870', ('30–80 m²', '30–80 م²'), ('cake 30 mm; chambers 460–1210 L; 23–62 plates; 2.2 kW; length 3.3–5.5 m', 'كعكة 30 مم؛ الحجرات 460–1210 لترات؛ 23–62 لوحاً؛ 2.2 كيلوواط؛ الطول 3.3–5.5 م')),
           CH('BX-0422-01-012', '1000×1000', 'XM(Y/Z)50/1000, 60/1000, 70/1000, 80/1000, 120/1000', ('50–120 m²', '50–120 م²'), ('cake 30 mm; chambers 751–1813 L; 28–69 plates; 3 kW; length 4.2–6.5 m', 'كعكة 30 مم؛ الحجرات 751–1813 لتراً؛ 28–69 لوحاً؛ 3 كيلوواط؛ الطول 4.2–6.5 م')),
           CH('BX-0422-01-013', '1250×1250', 'XM(Y/Z)100/1250, 120/1250, 140/1250, 160/1250, 200/1250, 220/1250, 250/1250', ('100–250 m²', '100–250 م²'), ('cake 30 mm; chambers 1517–3772 L; 36–91 plates; 5.5 kW; length 5.2–8.7 m', 'كعكة 30 مم؛ الحجرات 1517–3772 لتراً؛ 36–91 لوحاً؛ 5.5 كيلوواط؛ الطول 5.2–8.7 م')),
           CH('BX-0422-01-014', '1500×1500', 'XM(Y/Z)200/1500, 250/1500, 300/1500, 400/1500, 450/1500, 500/1500', ('200–500 m²', '200–500 م²'), ('cake 35 mm; chambers 3430–8506 L; 49–123 plates; 7.5 kW; length 6.6–11.8 m', 'كعكة 35 مم؛ الحجرات 3430–8506 لترات؛ 49–123 لوحاً؛ 7.5 كيلوواط؛ الطول 6.6–11.8 م')),
           CH('BX-0422-01-015', '2000×2000', 'XM(Y/Z)500/2000, 600/2000, 700/2000, 900/2000, 1000/2000', ('500–1000 m²', '500–1000 م²'), ('cake 40 mm; chambers 9936–20010 L; 71–144 plates; 7.5 kW; length 10–16 m', 'كعكة 40 مم؛ الحجرات 9936–20010 لترات؛ 71–144 لوحاً؛ 7.5 كيلوواط؛ الطول 10–16 م'))],
          intro=('Recessed-chamber presses suit tailings and small plants. Models are named by filter area and plate size.', 'المكابس الحجرية تناسب المخلفات والمصانع الصغيرة. تُسمّى الموديلات بمساحة الترشيح ومقاس اللوح.'),
          unit=U_SIZE),
], type_label=('Plate size', 'مقاس اللوح'), unit=U_SIZE)

# p13 filter plates, options, belt press & dosing -----------------------------------------------------------
F['filter-plates-options-belt-press-dosing'] = family('filter-plates-options-belt-press-dosing', CAT, [
    table('items', ('Plates, options, belt press and dosing', 'الألواح والإضافات ومكبس السير ووحدة الجرعات'), ('', ''), SERIES,
          [('BX-0422-01-001', 'Filter plates', 'ألواح الترشيح', ('Plate sizes 320, 450, 630, 800, 870, 1000, 1250, 1500, 2000 mm', 'مقاسات الألواح 320 و450 و630 و800 و870 و1000 و1250 و1500 و2000 مم'),
            ('PP, cast iron or stainless steel; recessed-chamber, plate-and-frame, membrane and round types', 'بولي بروبلين أو حديد زهر أو ستانلس؛ أنواع حجرية وبإطار ولوح وغشائية ودائرية')),
           ('BX-0422-01-002', 'Filter press options', 'إضافات مكابس الترشيح',
            ('Drip tray · belt conveyor · CGR plates · fast-open system · stainless 304 coating · vehicle-mounted system · cloth washing · light curtain', 'صينية تقطير · سير ناقل · ألواح CGR · نظام فتح سريع · طلاء ستانلس 304 · نظام محمول على مركبة · غسيل القماش · ستارة ضوئية'),
            ('Optional additions for new or existing presses', 'إضافات اختيارية للمكابس الجديدة أو القائمة')),
           ('BX-0422-01-017', 'Heavy-duty belt filter press DNYA', 'مكبس ترشيح بالسير للخدمة الشاقة DNYA', 'DNYA 1000, 1500, 2000, 2500, 3000',
            ('Belt width 1–3 m; filter area 37.2–111.2 m²; slurry 10–80 m³/h (0.8% solids); cake moisture 66–81%; 2.25–5.5 kW', 'عرض السير 1–3 م؛ مساحة الترشيح 37.2–111.2 م²؛ اللب 10–80 م³/ساعة (0.8% مواد صلبة)؛ رطوبة الكعكة 66–81%؛ 2.25–5.5 كيلوواط')),
           ('BX-0422-01-019', 'Automatic polymer dosing system PYJ', 'وحدة جرعات البوليمر الآلية PYJ', 'PYJ-1000, -1500, -2500, -4000, -6000, -10000',
            ('1000–10000 L/h; three tanks; stainless frame; water 0.6–28 m³/h; powder hopper 40–200 L', '1000–10000 لتر/ساعة؛ ثلاثة خزانات؛ إطار ستانلس؛ الماء 0.6–28 م³/ساعة؛ قادوس المسحوق 40–200 لتر'))],
          unit=U_PRODUCT),
], type_label=('Product', 'المنتج'))

# p14 filter press parts & vacuum filter belts --------------------------------------------------------------
F['filter-press-parts-vacuum-filter-belts'] = family('filter-press-parts-vacuum-filter-belts', CAT, [
    table('parts', ('Filter press parts and vacuum filter belts', 'قطع مكابس الترشيح وسيور المرشحات الفراغية'), ('', ''), SERIES,
          [('BX-0235-01-001', 'Filter press cloth', 'قماش مكبس الترشيح', ('For 1250×1250, 1500×1500 and 2000×2000 mm plates', 'لألواح 1250×1250 و1500×1500 و2000×2000 مم'), ('One cloth per plate', 'قماشة لكل لوح')),
           ('BX-0235-01-002', 'Filter press plates, membrane and chamber', 'ألواح مكابس الترشيح، غشائية وحجرية', ('1250×1250, 1500×1500, 2000×2000 mm', '1250×1250 و1500×1500 و2000×2000 مم'), ('Membrane (squeeze) and recessed chamber plates', 'ألواح غشائية (للعصر) وحجرية')),
           ('BX-0235-01-003', 'Lattice rubber belt for filter cake', 'سير مطاطي شبكي لكعكة الترشيح', ('B1000 (1250 press), B1400 (1500 press), B1800 (2000 press)', 'B1000 (لمكبس 1250)، وB1400 (لمكبس 1500)، وB1800 (لمكبس 2000)'),
            ('Carries the discharged cake away from the press; sold per metre', 'ينقل الكعكة المفرّغة بعيداً عن المكبس؛ يُباع بالمتر')),
           ('BX-0717-01-014', 'Vacuum belt filter belt', 'سير المرشح الفراغي', ('Width up to 6500 mm; length 10–200 m; 20–50 mm thick', 'عرض حتى 6500 مم؛ طول 10–200 م؛ سماكة 20–50 مم'),
            ('Polyester carcass with drainage grooves and holes; top cover 10–30 mm, bottom 5–15 mm; standard, heat-, acid / alkali- and oil-resistant', 'هيكل بوليستر بأخاديد وثقوب تصريف؛ غطاء علوي 10–30 مم وسفلي 5–15 مم؛ عادي ومقاوم للحرارة وللأحماض والقلويات وللزيت'))],
          unit=U_PRODUCT),
], type_label=('Product', 'المنتج'))
