"""BXS-01 Ed2 (Safety & PPE) model tables, catalogue pages 3–17. Typed from the page text and checked against the
page images where cells wrap. Every code is in the supplier list under BXS-01. Rows that carry the same product from
two suppliers (pages 16–17) take the first code; the ceramic-fibre row on page 9 is split into rope and cloth/tape by
the footnote's code."""
from lib import table, family

CAT = 'BXS-01 Ed2'
F = {}
U_LINES = {'ar': ['خط واحد', 'خطان', 'خطوط'], 'en': ['product line', 'product lines']}
U_PRODUCT = {'ar': ['منتج واحد', 'منتجان', 'منتجات'], 'en': ['product', 'products']}
U_MODEL = {'ar': ['موديل واحد', 'موديلان', 'موديلات'], 'en': ['model', 'models']}
SERIES = [('models', 'Sizes / models', 'المقاسات والموديلات'), ('data', 'Key data', 'أهم البيانات')]
SPEC = [('spec', 'Specification', 'المواصفات')]
C = lambda k, en, ar: (k, en, ar)
CE = lambda en, ar: (en, ar)

# p3 high-visibility workwear & safety helmets ---------------------------------------------------------------
F['high-visibility-workwear-helmets'] = family('high-visibility-workwear-helmets', CAT, [
    table('hivis', ('High-visibility workwear and helmets', 'ملابس عالية الوضوح وخوذ'), ('S–5XL', 'S–5XL'),
          [C('spec', 'Specification', 'المواصفات'), C('models', 'Models', 'الموديلات')],
          [('BX-0346-01-009', 'Hi-vis safety vests', 'سترات سلامة عاكسة',
            ('EN ISO 20471; knitted or mesh polyester 60–130 g/m² or 300D Oxford; yellow, orange, lime; S–5XL; zip or hook-and-loop; 5 cm reflective tape; logo printing',
             'EN ISO 20471؛ بوليستر محبوك أو شبكي 60–130 جم/م² أو أكسفورد 300D؛ أصفر أو برتقالي أو ليموني؛ S–5XL؛ سحّاب أو لاصق؛ شريط عاكس 5 سم؛ طباعة الشعار'), '23'),
           ('BX-0327-01-030', 'Economy reflective vests', 'سترات عاكسة اقتصادية', ('Polyester 60–120 g, EN 471 Class 2 tape, S–3XL', 'بوليستر 60–120 جم، شريط EN 471 الفئة 2، S–3XL'), '6'),
           ('BX-0346-01-010', 'Hi-vis T-shirts & polo shirts', 'قمصان وبولو عالية الوضوح', ('EN 20471 with reflective tape', 'EN 20471 بشريط عاكس'), '9'),
           ('BX-0346-01-011', 'Hi-vis jackets', 'سترات (جاكيتات) عالية الوضوح', ('EN 20471; hooded, soft-shell and rain styles', 'EN 20471؛ بقلنسوة وسوفت شل وللمطر'), '9'),
           ('BX-0346-01-012', 'Hi-vis caps & headwear', 'قبعات وأغطية رأس عالية الوضوح', ('Reflective trim; made to order', 'حواف عاكسة؛ حسب الطلب'), '–'),
           ('BX-0327-01-035', 'Safety helmets', 'خوذ السلامة', ('ABS or HDPE, CE; about 435 g; colours to order', 'ABS أو HDPE، CE؛ نحو 435 جم؛ الألوان حسب الطلب'), '6')],
          intro=('Standards and certificates as stated by the manufacturers; customer logos printed on request.', 'المعايير والشهادات حسب بيانات المصنّعين؛ وتُطبع شعارات العملاء عند الطلب.'),
          unit=U_LINES),
], type_label=('Product', 'المنتج'))

# p4 helmets, eye, face, respiratory, hearing & fall protection ----------------------------------------------
F['head-eye-face-respiratory-hearing-fall-protection'] = family('head-eye-face-respiratory-hearing-fall-protection', CAT, [
    table('ppe', ('Head, eye, face, respiratory, hearing and fall protection', 'حماية الرأس والعين والوجه والتنفس والسمع والسقوط'), ('13 product lines', '13 خط منتجات'), SERIES,
          [('BX-0326-01-001', 'Safety helmets', 'خوذ السلامة', '1606001–1606025, 1606027, 1606028',
            ('PE, ABS, anti-static ABS and fibreglass (FRP); red, white, yellow, blue, orange; 235–510 g; vented, anti-slip', 'PE وABS وABS مضاد للكهرباء الساكنة وألياف زجاجية (FRP)؛ أحمر وأبيض وأصفر وأزرق وبرتقالي؛ 235–510 جم؛ بفتحات تهوية ومانعة للانزلاق')),
           ('BX-0326-02-001', 'Safety spectacles – CE', 'نظارات سلامة – CE', ('AS-01 to AS-10, AS-12 to AS-18, AS-20', 'من AS-01 إلى AS-10، ومن AS-12 إلى AS-18، وAS-20'),
            ('CE; standard, anti-scratch (AS) or anti-fog (AF) lenses', 'CE؛ عدسات عادية أو مقاومة للخدش (AS) أو مانعة للضباب (AF)')),
           ('BX-0326-02-002', 'Safety goggles – CE', 'نظارات واقية محكمة – CE', 'AS-50, AS-50V, AS-50W, AS-61, AS-61V, AS-61W, AS-80, AS-84',
            ('CE; sealed eye protection; vented and wide-view versions', 'CE؛ حماية محكمة للعين؛ نسخ بتهوية وبمجال رؤية واسع')),
           ('BX-0326-01-003', 'Safety glasses', 'نظارات السلامة', '1603001–1603033', ('Clear, anti-fog, anti-glare, laser and impact-resistant lenses', 'عدسات شفافة ومانعة للضباب ومضادة للوهج وللّيزر ومقاومة للصدمات')),
           ('BX-0326-01-004', 'Protective goggles', 'نظارات واقية', '1603201–1603224', ('Anti-fog, impact-resistant, foldable and closed types', 'مانعة للضباب ومقاومة للصدمات وقابلة للطي ومغلقة')),
           ('BX-0326-01-005', 'Face shields', 'واقيات الوجه', '1602001–1602011, 1602019–1602027', ('Acrylic full-face, rotatable, insulating, helmet-mounted and explosion-proof', 'أكريليك للوجه كاملاً، دوّارة وعازلة وتُركّب على الخوذة ومقاومة للانفجار')),
           ('BX-0326-01-006', 'Heat-resistant and welding face shields', 'واقيات وجه للحرارة واللحام', '1602012–1602018',
            ('Heat- and impact-resistant, aluminised reflective layer, welding masks; for smelting rooms', 'مقاومة للحرارة والصدمات، بطبقة عاكسة مؤلمنة، وأقنعة لحام؛ لغرف الصهر')),
           ('BX-0326-01-007', 'Dust masks, half-face respirators and gas masks', 'كمامات الغبار وأقنعة نصف الوجه والأقنعة الواقية من الغاز', '1602201–1602235',
            ('Reusable dust masks, single or twin-filter half masks, full-face masks; for crushing and grinding dust', 'كمامات غبار قابلة لإعادة الاستخدام، وأقنعة نصف وجه بمرشح واحد أو مرشحين، وأقنعة للوجه كاملاً؛ لغبار التكسير والطحن')),
           ('BX-0326-01-008', 'Disposable dust masks', 'كمامات غبار للاستعمال مرة واحدة', '1602401–1602417', ('Cup-shape and foldable, with or without valve; filtration class on request', 'كأسية وقابلة للطي، بصمام أو بدونه؛ فئة الترشيح حسب الطلب')),
           ('BX-0326-01-009', 'Earplugs', 'سدادات الأذن', '1602601–1602612', ('Foam, PU and silicone, corded or uncorded; SNR 27–38 dB; NRR up to 31 dB; EN 352-2, ANSI S3.19', 'إسفنج وبولي يوريثان وسيليكون، بحبل أو بدونه؛ SNR ‏27–38 ديسيبل؛ NRR حتى 31 ديسيبل؛ EN 352-2 وANSI S3.19')),
           ('BX-0326-01-010', 'Earmuffs', 'واقيات الأذن', ('1602801–1602822 (adult models)', '1602801–1602822 (موديلات للبالغين)'),
            ('ABS cups, PU cushions; SNR 21–31 dB; EN 352-1, ANSI S3.19; Bluetooth and radio models', 'أكواب ABS ووسائد بولي يوريثان؛ SNR ‏21–31 ديسيبل؛ EN 352-1 وANSI S3.19؛ موديلات ببلوتوث وراديو')),
           ('BX-0326-01-026', 'Full-body and half-body safety harnesses', 'أحزمة أمان للجسم كاملاً ولنصفه', '1604401–1604412',
            ('45 mm polyester or flame-retardant aramid webbing; breaking strength ≥ 22 kN; 100 kg user; CE, ISO', 'حزام بوليستر 45 مم أو أراميد مقاوم للهب؛ قوة كسر ≥ 22 كيلونيوتن؛ لمستخدم 100 كجم؛ CE وISO')),
           ('BX-0326-01-027', 'Lanyards and retractable lifelines', 'حبال الربط وخطوط الحياة القابلة للسحب', '1604413–1604424',
            ('Elastic and retractable; breaking strength ≥ 22 kN; width and length to order; CE, ISO', 'مرنة وقابلة للسحب؛ قوة كسر ≥ 22 كيلونيوتن؛ العرض والطول حسب الطلب؛ CE وISO'))],
          unit=U_LINES),
], type_label=('Series', 'السلسلة'))

# p5 work & safety gloves -----------------------------------------------------------------------------------
G = lambda code, m, use, lining, coat, sizes: (code, m, None, use, lining, coat, sizes)
F['work-safety-gloves'] = family('work-safety-gloves', CAT, [
    table('gloves', ('Work and safety gloves', 'قفازات العمل والسلامة'), ('14 models', '14 موديلاً'),
          [C('use', 'Use', 'الاستخدام'), C('lining', 'Lining', 'البطانة'), C('coat', 'Coating / material', 'الطلاء أو المادة'), C('sizes', 'Sizes', 'المقاسات')],
          [G('BX-0069-01-001', 'MJFZ504', ('Impact and cut resistant, anti-slip', 'مقاومة للصدمات والقطع ومانعة للانزلاق'), ('Nylon / HPPE + glass fibre + Lycra, 13 g', 'نايلون / HPPE + ألياف زجاجية + ليكرا، 13 g'), ('Silica dots on palm, TPR on back', 'نقاط سيليكا على الكف وTPR على الظهر'), '8, 9, 10'),
           G('BX-0069-01-004', 'MJFZ502', ('Impact and cut resistant', 'مقاومة للصدمات والقطع'), ('Nylon / HPPE + glass fibre + Lycra', 'نايلون / HPPE + ألياف زجاجية + ليكرا'), ('Sandy nitrile palm, TPR back; Velcro cuff', 'كف نتريل رملي وظهر TPR؛ كُم بلاصق'), '8, 9, 10'),
           G('BX-0069-01-009', 'MJFZ509', ('Impact resistant (economy)', 'مقاومة للصدمات (اقتصادية)'), ('Polyester', 'بوليستر'), ('Sandy nitrile palm, TPR back', 'كف نتريل رملي وظهر TPR'), '8–12'),
           G('BX-0069-01-020', 'MJFG502', ('Cut resistant level 5', 'مقاومة للقطع المستوى 5'), ('HPPE + glass fibre + Lycra, 13 g', 'HPPE + ألياف زجاجية + ليكرا، 13 g'), ('Sandy nitrile palm', 'كف نتريل رملي'), '8, 9, 10'),
           G('BX-0069-01-028', 'MJDJ001', ('Heavy-duty work', 'عمل شاق'), ('Cotton jersey', 'جيرسيه قطني'), ('Smooth nitrile palm; safety cuff', 'كف نتريل أملس؛ كُم أمان'), ('One size', 'مقاس واحد')),
           G('BX-0069-01-045', 'MJDJ016', ('Heavy-duty work', 'عمل شاق'), ('Cotton jersey', 'جيرسيه قطني'), ('Sandy nitrile; safety cuff', 'نتريل رملي؛ كُم أمان'), '–'),
           G('BX-0069-01-055', 'MJZW005', ('General handling', 'مناولة عامة'), ('Polyester, 13 g', 'بوليستر، 13 g'), ('Crinkle latex palm', 'كف لاتكس مجعّد'), '8–11'),
           G('BX-0069-01-084', 'MJPS001', ('General handling (economy)', 'مناولة عامة (اقتصادية)'), ('Polycotton', 'قطن وبوليستر'), ('PVC dots, one side', 'نقاط PVC على وجه واحد'), ('Length 21–25 cm', 'الطول 21–25 سم')),
           G('BX-0069-01-075', 'MJNC001', ('Chemical handling', 'مناولة الكيماويات'), ('Flocked', 'مبطّن بزغب'), ('Neoprene / latex, 320 mm', 'نيوبرين / لاتكس، 320 مم'), '–'),
           G('BX-0069-01-077', 'MJNC003', ('Chemical handling', 'مناولة الكيماويات'), ('Unlined', 'بلا بطانة'), ('Nitrile, 320–380 mm', 'نتريل، 320–380 مم'), '–'),
           G('BX-0069-01-078', 'MJPD001', ('Wet work, tanks', 'العمل الرطب والأحواض'), ('Cotton fleece', 'صوف قطني'), ('Sandy PVC, 65 cm with oversleeve', 'PVC رملي، 65 سم بكُم إضافي'), '–'),
           G('BX-0069-01-018', 'MJLT002', ('Welding and workshop', 'اللحام والورشة'), ('Cotton', 'قطن'), ('Cow split leather + TPR', 'جلد بقري مشقوق + TPR'), '8, 9, 10'),
           G('BX-0069-01-091', 'MJLP004', ('Heavy-duty, warm', 'عمل شاق، دافئة'), ('Cotton', 'قطن'), ('Cow split leather', 'جلد بقري مشقوق'), ('10.5 and 13 in', '10.5 و13 بوصة')),
           G('BX-0069-01-092', 'MJLP005', ('Welding and smelting', 'اللحام والصهر'), ('Cotton', 'قطن'), ('Cow split leather', 'جلد بقري مشقوق'), ('10.5 and 13 in', '10.5 و13 بوصة'))],
          intro=('Packed 10–12 pairs per bag, 100–240 pairs per carton depending on model.', 'التعبئة 10–12 زوجاً في الكيس و100–240 زوجاً في الكرتونة حسب الموديل.'),
          key_rows=['use', 'coat', 'sizes'], unit=U_MODEL),
], type_label=('Model', 'الموديل'), unit=U_MODEL)

# p6 work & safety gloves – additional range ----------------------------------------------------------------
F['work-safety-gloves-additional-range'] = family('work-safety-gloves-additional-range', CAT, [
    table('range', ('Work and safety gloves – additional range', 'قفازات العمل والسلامة – تشكيلة إضافية'), ('10–21 G', '10–21 G'), SERIES,
          [('BX-0342-01-001', 'Micro-foam nitrile coated gloves', 'قفازات مطلية بنتريل رغوي دقيق', '15 G / 18 G', ('Nylon-spandex liner; matt, breathable micro-foam nitrile; grip in dry, wet and oily conditions; EN 388 4121 or 4131', 'بطانة نايلون وسباندكس؛ نتريل رغوي دقيق مطفأ يسمح بالتنفس؛ قبضة في الجاف والرطب والزيتي؛ EN 388 4121 أو 4131')),
           ('BX-0342-01-003', 'Sandy nitrile coated gloves', 'قفازات مطلية بنتريل رملي', '15 G / 18 G', ('Nylon-spandex liner; sandy nitrile for a stronger grip in oil and mud; EN 388 4121 or 4131', 'بطانة نايلون وسباندكس؛ نتريل رملي لقبضة أقوى في الزيت والطين؛ EN 388 4121 أو 4131')),
           ('BX-0342-01-004', '3/4 micro-foam nitrile coated gloves', 'قفازات مطلية بنتريل رغوي على ثلاثة أرباع اليد', '15 G / 18 G', ('Coating over three quarters of the hand to protect the finger backs; EN 388 4121 or 4131', 'طلاء على ثلاثة أرباع اليد لحماية ظهر الأصابع؛ EN 388 4121 أو 4131')),
           ('BX-0342-01-007', 'Cut-resistant nitrile gloves', 'قفازات نتريل مقاومة للقطع', ('15 G / 18 G / 21 G; ANSI A2 to A8', '15 G / 18 G / 21 G؛ ANSI من A2 إلى A8'), ('Micro-foam or sandy nitrile; for mesh, sheet metal and sharp edges', 'نتريل رغوي أو رملي؛ للشبك والصفائح والحواف الحادة')),
           ('BX-0342-01-010', 'TPR heavy-duty impact gloves', 'قفازات صدمات TPR للخدمة الشاقة', ('13 G / 15 G cut-resistant liner', 'بطانة مقاومة للقطع 13 G / 15 G'), ('Sandy nitrile palm, TPR knuckle guard, EVA-padded palm against vibration', 'كف نتريل رملي، وواقي مفاصل TPR، وكف مبطن بـ EVA ضد الاهتزاز')),
           ('BX-0342-01-012', 'Latex coated gloves (economy)', 'قفازات مطلية باللاتكس (اقتصادية)', '10 G / 13 G', ('Polyester liner, latex coating; flexible grip; EN 388 1121', 'بطانة بوليستر وطلاء لاتكس؛ قبضة مرنة؛ EN 388 1121')),
           ('BX-0326-01-011', 'Seamless knitted cotton and polycotton gloves', 'قفازات قطنية محبوكة بلا درزات', '1601001–1601021', ('Sizes 8–10; 400–800 g per dozen', 'المقاسات 8–10؛ 400–800 جم للدزينة')),
           ('BX-0326-01-013', 'Latex coated gloves (crinkle, foam, fully coated)', 'قفازات مطلية باللاتكس (مجعّدة ورغوية ومطلية بالكامل)', '1601201–1601316, 1601321–1601324', ('Cotton or polyester liner; tear- and water-resistant', 'بطانة قطن أو بوليستر؛ مقاومة للتمزق والماء')),
           ('BX-0326-01-015', 'Nitrile coated gloves (palm and foam)', 'قفازات مطلية بالنتريل (الكف والرغوي)', '1601401–1601413', ('13–15 G polyester or nylon liner; oil-resistant', 'بطانة بوليستر أو نايلون 13–15 G؛ مقاومة للزيت')),
           ('BX-0326-01-016', 'Heavy-duty nitrile-dipped jersey gloves', 'قفازات جيرسيه مغموسة بالنتريل للخدمة الشاقة', '1601414–1601418', ('Full or 3/4 nitrile on cotton jersey; safety cuff; oil- and abrasion-resistant', 'نتريل كامل أو ثلاثة أرباع على جيرسيه قطني؛ كُم أمان؛ مقاومة للزيت والتآكل')),
           ('BX-0326-01-018', 'Industrial chemical gloves', 'قفازات كيماويات صناعية', '1601605–1601607', ('Long latex and neoprene gloves for handling process chemicals', 'قفازات طويلة من اللاتكس والنيوبرين لمناولة كيماويات المعالجة')),
           ('BX-0326-01-019', 'PVC-dipped gauntlet gloves', 'قفازات طويلة مغموسة بـ PVC', '1601701–1601715', ('Full PVC on cotton liner; 27–35 cm long; oil, slip and chemical resistant', 'PVC كامل على بطانة قطنية؛ طول 27–35 سم؛ مقاومة للزيت والانزلاق والكيماويات')),
           ('BX-0326-01-020', 'HPPE cut-resistant gloves', 'قفازات HPPE مقاومة للقطع', '1601801–1601810', ('Cut level 3–5; PU, nitrile or latex coating', 'مستوى القطع 3–5؛ طلاء بولي يوريثان أو نتريل أو لاتكس')),
           ('BX-0326-01-021', 'Leather combination work gloves', 'قفازات عمل جلدية مركّبة', ('9 models', '9 موديلات'), ('Cowhide or pigskin split with canvas back; safety cuff; 10.5 in', 'جلد بقري أو خنزيري مشقوق بظهر قماشي؛ كُم أمان؛ 10.5 بوصة')),
           ('BX-0326-01-023', 'Leather welding gloves', 'قفازات لحام جلدية', ('18 models', '18 موديلاً'), ('Lined cowhide split; 14 and 16 in long', 'جلد بقري مشقوق مبطن؛ بطول 14 و16 بوصة'))],
          unit=U_LINES),
], type_label=('Series', 'السلسلة'))

# p7 safety footwear ----------------------------------------------------------------------------------------
F['safety-footwear'] = family('safety-footwear', CAT, [
    table('footwear', ('Safety footwear', 'أحذية السلامة'), ('SB–S3, EU 37–48', 'SB–S3، مقاسات 37–48'), SERIES,
          [('BX-0349-02-001', 'Leather safety shoes and boots, rubber or PU/rubber sole', 'أحذية وبوت سلامة جلدية بنعل مطاطي أو بولي يوريثان/مطاط',
            ('13 models: 8013, 8005, 8003, 8007, 6029, 8034, 9002, 8062, 1004, 1009, 1016, 8039, 6038', '13 موديلاً: 8013، 8005، 8003، 8007، 6029، 8034، 9002، 8062، 1004، 1009، 1016، 8039، 6038'),
            ('Nubuck, suede, smooth, printed or microfibre leather; steel toe, puncture-resistant sole; SB to S3; heat, oil and slip resistant', 'جلد نوبوك أو شمواه أو أملس أو مطبوع أو ميكروفايبر؛ مقدمة فولاذية ونعل مقاوم للثقب؛ SB حتى S3؛ مقاومة للحرارة والزيت والانزلاق')),
           ('BX-0349-02-002', 'Embossed cowhide safety shoes, PU sole (economy)', 'أحذية سلامة من جلد بقري منقوش بنعل بولي يوريثان (اقتصادية)',
            ('28 models: 8019, 8017, 8026, 8032, 8029, 9008, 1002, 1003, 1015, 8048, 1039 …', '28 موديلاً: 8019، 8017، 8026، 8032، 8029، 9008، 1002، 1003، 1015، 8048، 1039 …'),
            ('PU or PU/TPU sole; steel toe, puncture-resistant sole; SB to S3', 'نعل بولي يوريثان أو بولي يوريثان/TPU؛ مقدمة فولاذية ونعل مقاوم للثقب؛ SB حتى S3')),
           ('BX-0349-02-003', 'Nubuck, suede and smooth leather safety shoes, PU or MD sole', 'أحذية سلامة من النوبوك والشمواه والجلد الأملس بنعل بولي يوريثان أو MD',
            ('21 models: 8011, 8014, 8008, 9001, 1006, 6001, 1025, 1024, 1030, 9016, 8057 …', '21 موديلاً: 8011، 8014، 8008، 9001، 1006، 6001، 1025، 1024، 1030، 9016، 8057 …'),
            ('Toe cap and puncture-resistant sole; SB to S3', 'مقدمة واقية ونعل مقاوم للثقب؛ SB حتى S3')),
           ('BX-0349-02-004', 'Microfibre leather safety shoes, PU or EVA sole', 'أحذية سلامة من جلد الميكروفايبر بنعل بولي يوريثان أو EVA', '1001, 1012, 1027, 6023, 6036, 8044',
            ('Toe cap and puncture-resistant sole; SB to S3', 'مقدمة واقية ونعل مقاوم للثقب؛ SB حتى S3')),
           ('BX-0349-02-005', 'Electrical safety shoes – dielectric, insulating, ESD', 'أحذية سلامة كهربائية – عازلة ومضادة للكهرباء الساكنة', '1005, 1010, 6040, 8023',
            ('Printed or microfibre leather, PU sole; for electricians and generator technicians', 'جلد مطبوع أو ميكروفايبر بنعل بولي يوريثان؛ للكهربائيين وفنيي المولدات')),
           ('BX-0349-01-001', 'Construction and industry safety shoes and boots', 'أحذية وبوت سلامة للإنشاءات والصناعة',
            ('23 models: 8128, 8128H, 8003, 8005, 8006, 8008, 8009, 6001, 6002, 6003, 6005, 8201 …', '23 موديلاً: 8128، 8128H، 8003، 8005، 8006، 8008، 8009، 6001، 6002، 6003، 6005، 8201 …'),
            ('Water-resistant cowhide, mesh lining, dual-density PU sole (8101 rubber); toe cap, puncture-resistant sole; EU 37–48', 'جلد بقري مقاوم للماء وبطانة شبكية ونعل بولي يوريثان مزدوج الكثافة (8101 مطاطي)؛ مقدمة واقية ونعل مقاوم للثقب؛ 37–48')),
           ('BX-0349-01-005', 'Goodyear-welted safety boots', 'بوت سلامة بخياطة غوديير', '7001, 7002, 7003, 7005, 7006, 7007, 7009',
            ('Crazy Horse or full-grain cowhide; stitched rubber sole, heat and abrasion resistant; EU 37–48', 'جلد بقري كريزي هورس أو كامل الحبيبات؛ نعل مطاطي مخيط مقاوم للحرارة والتآكل؛ 37–48')),
           ('BX-0349-01-006', 'Heavy-duty safety shoes and boots', 'أحذية وبوت سلامة للخدمة الشاقة', ('30 models: 8601, 8602, 8605–8611, 8701–8703, 8705–8713, 8715–8723', '30 موديلاً: 8601، 8602، 8605–8611، 8701–8703، 8705–8713، 8715–8723'),
            ('Nubuck, frosted or suede leather; PU/PU, PU/rubber or EVA/rubber sole; EU 37–48', 'جلد نوبوك أو مصنفر أو شمواه؛ نعل بولي يوريثان مزدوج أو بولي يوريثان/مطاط أو EVA/مطاط؛ 37–48')),
           ('BX-0349-01-008', 'Rigger (high-leg) safety boots', 'بوت سلامة طويل (ريغر)', '9002, 9003, 9006, 9018',
            ('Water-resistant cowhide, dual-density PU sole; for mud and water at washing and dredging sites; EU 37–48', 'جلد بقري مقاوم للماء ونعل بولي يوريثان مزدوج الكثافة؛ للطين والماء في مواقع الغسيل والتجريف؛ 37–48')),
           ('BX-0326-01-030', 'Ultra-light safety shoes', 'أحذية سلامة خفيفة جداً', '1607001–1607012',
            ('Steel or composite toe; impact and puncture resistant; Flyknit, microfibre or leather; rubber, EVA or PU sole', 'مقدمة فولاذية أو مركّبة؛ مقاومة للصدمات والثقب؛ فلاي نِت أو ميكروفايبر أو جلد؛ نعل مطاطي أو EVA أو بولي يوريثان')),
           ('BX-0326-01-031', 'Electrical insulation safety shoes 6 / 10 / 15 kV', 'أحذية سلامة عازلة للكهرباء 6 / 10 / 15 كيلوفولت', '1607101–1607112', ('Steel toe, dual-density PU sole', 'مقدمة فولاذية ونعل بولي يوريثان مزدوج الكثافة')),
           ('BX-0326-01-033', 'Welder safety shoes', 'أحذية سلامة للحامين', '1607301–1607306', ('Alcantara upper, steel toe, rubber sole', 'وجه ألكانتارا، مقدمة فولاذية، نعل مطاطي')),
           ('BX-0326-01-035', 'Cowhide safety boots', 'بوت سلامة من الجلد البقري', '1607501–1607512', ('Split cowhide, iron or steel toe, dual-density PU or rubber sole; wool-lined models', 'جلد بقري مشقوق، مقدمة حديدية أو فولاذية، نعل بولي يوريثان مزدوج أو مطاطي؛ موديلات مبطنة بالصوف')),
           ('BX-0326-01-039', 'Steel-toe, steel-midsole rain boots', 'بوت مطر بمقدمة ونعل أوسط فولاذيين', '1608501–1608512', ('Quick-dry lining; for wet washing and processing areas', 'بطانة سريعة الجفاف؛ لمناطق الغسيل والمعالجة الرطبة'))],
          unit=U_LINES),
], type_label=('Series', 'السلسلة'))

# p8 disposable protective coveralls ------------------------------------------------------------------------
CV = lambda code, m, t, fab, col, pack: (code, m, None, t, fab, col, pack)
F['disposable-protective-coveralls'] = family('disposable-protective-coveralls', CAT, [
    table('coveralls', ('Coverall range', 'تشكيلة الأوفرولات'), ('40–90 g/m²', '40–90 جم/م²'),
          [C('type', 'Type', 'النوع'), C('fabric', 'Fabric', 'القماش'), C('colours', 'Colours', 'الألوان'), C('packing', 'Packing', 'التعبئة')],
          [CV('BX-0340-02-001', 'Type 500', '1P / 2P', 'PP 40 g/m²', ('Grey', 'رمادي'), ('24 pcs/box', '24 قطعة/صندوق')),
           CV('BX-0340-02-001', 'Type 1000', '1P / 2P', 'PP 50 g/m²', ('Grey', 'رمادي'), ('24 pcs/box', '24 قطعة/صندوق')),
           CV('BX-0340-02-001', 'Type 1200', '1P / 2P', 'PP 60 g/m²', ('White / blue / pink', 'أبيض / أزرق / وردي'), ('24 pcs/box', '24 قطعة/صندوق')),
           CV('BX-0340-02-002', 'SMS-2000', '1P', 'SMS 50 g/m²', ('White / grey / blue', 'أبيض / رمادي / أزرق'), ('24 pcs/box', '24 قطعة/صندوق')),
           CV('BX-0340-02-002', 'SMS-2500', '1P / 2P', 'SMS 60 g/m²', ('Grey / blue / orange', 'رمادي / أزرق / برتقالي'), ('24–50 pcs/box', '24–50 قطعة/صندوق')),
           CV('BX-0340-02-003', 'SF-4000', '1P', ('Laminated PP+PE 50 / 55 / 60 g/m²', 'PP+PE مصفّح 50 / 55 / 60 جم/م²'), ('White', 'أبيض'), ('25 pcs/box', '25 قطعة/صندوق')),
           CV('BX-0340-02-003', 'SF-4500', '1P', ('Laminated PP+PE 60 g/m²', 'PP+PE مصفّح 60 جم/م²'), ('White', 'أبيض'), ('25 pcs/box', '25 قطعة/صندوق')),
           CV('BX-0340-02-003', 'SF-5000', '1P', ('Laminated PP+PE 60 g/m²', 'PP+PE مصفّح 60 جم/م²'), ('White', 'أبيض'), ('50 pcs/box', '50 قطعة/صندوق')),
           CV('BX-0340-02-004', 'Type 6000', '1P', ('Laminated PP+PE 90 g/m²', 'PP+PE مصفّح 90 جم/م²'), ('Yellow', 'أصفر'), ('25 pcs/box', '25 قطعة/صندوق')),
           CV('BX-0340-02-004', 'Type 7000', '1P', ('Laminated PP+PE 90 g/m², double layer at knees and placket', 'PP+PE مصفّح 90 جم/م²، طبقة مزدوجة عند الركبتين والسحّاب'), ('Yellow / grey', 'أصفر / رمادي'), ('20 pcs/box', '20 قطعة/صندوق'))],
          intro=('1P = one-piece, 2P = two-piece. Sizes L / XL.', '1P = قطعة واحدة، 2P = قطعتان. المقاسات L / XL.'),
          key_rows=['fabric', 'type', 'colours'], unit=U_MODEL),
], type_label=('Model', 'الموديل'), unit=U_MODEL)

# p9 heat & fire protection for smelting -------------------------------------------------------------------
F['heat-fire-protection-smelting'] = family('heat-fire-protection-smelting', CAT, [
    table('heat', ('Heat and fire protection', 'الحماية من الحرارة والحريق'), ('Up to 1000 °C', 'حتى 1000 °م'), SPEC,
          [('BX-0043-01-001', 'Fire-resistant suits', 'بدلات مقاومة للحريق', ('Ceramic fibre 1000 °C, fibreglass 550 °C, aluminised carbon fibre 400 °C; large and special large', 'ألياف خزفية 1000 °م، وألياف زجاجية 550 °م، وألياف كربون مؤلمنة 400 °م؛ مقاس كبير وكبير خاص')),
           ('BX-0043-01-002', 'Leather welder suit sets', 'أطقم بدلات لحام جلدية', ('Double-layer leather: suit, apron, sleeves, gaiters, hood; L–4XL', 'جلد بطبقتين: بدلة ومريلة وأكمام وواقيات ساق وغطاء رأس؛ L–4XL')),
           ('BX-0043-01-003', 'Heat-resistant gloves & mittens', 'قفازات وكفوف مقاومة للحرارة', ('12", 15", 18"; fibreglass 550 °C, aluminised carbon 300 °C, aluminised aramid 400 °C, aramid 250 °C, ceramic 1000 °C', '12 و15 و18 بوصة؛ ألياف زجاجية 550 °م، وكربون مؤلمن 300 °م، وأراميد مؤلمن 400 °م، وأراميد 250 °م، وخزف 1000 °م')),
           ('BX-0043-01-004', 'Fire blankets & blanket/extinguisher sets', 'بطانيات الحريق وأطقم البطانية والطفاية', ('Fibreglass 550 °C; 1 × 1 to 1.8 × 1.8 m; EN 1869 / ASTM F1989', 'ألياف زجاجية 550 °م؛ من 1 × 1 إلى 1.8 × 1.8 م؛ EN 1869 / ASTM F1989')),
           ('BX-0043-01-010', 'Welding blankets & curtains', 'بطانيات وستائر اللحام', ('Fibreglass 550 °C; 1.8 × 1.8 to 20 × 20 m', 'ألياف زجاجية 550 °م؛ من 1.8 × 1.8 إلى 20 × 20 م')),
           ('BX-0043-01-016', 'Foundry mats & fire sleeves', 'حصائر المسابك وأكمام الحريق', ('Mats to 1000 °C; sleeves ID 10–200 mm', 'حصائر حتى 1000 °م؛ أكمام بقطر داخلي 10–200 مم')),
           ('BX-0043-02-003', 'Ceramic-fibre rope', 'حبال الألياف الخزفية', ('Furnace door seals and lining, about 1000 °C', 'لإحكام أبواب الأفران وبطانتها، نحو 1000 °م')),
           ('BX-0043-02-004', 'Ceramic-fibre cloth & tape', 'قماش وشريط الألياف الخزفية', ('Furnace door seals and lining, about 1000 °C', 'لإحكام أبواب الأفران وبطانتها، نحو 1000 °م')),
           ('BX-0043-02-024', 'Mica sheet', 'ألواح الميكا', ('Coil insulation for induction furnaces', 'عزل ملفات أفران الحث'))],
          intro=('Temperature ratings and standards as stated by the manufacturer.', 'درجات الحرارة والمعايير حسب بيانات المصنّع.'),
          unit=U_PRODUCT),
], type_label=('Product', 'المنتج'))

# p10 breathing apparatus, respirators & suits --------------------------------------------------------------
F['breathing-apparatus-respirators-suits'] = family('breathing-apparatus-respirators-suits', CAT, [
    table('ba', ('Breathing apparatus & compressors', 'أجهزة التنفس والضواغط'), ('30 MPa', '30 ميجاباسكال'), SERIES,
          [('BX-0761-01-001', 'Self-contained breathing apparatus (SCBA)', 'جهاز تنفس ذاتي (SCBA)', 'RHZK5/30, RHZKF3/30, RHZKF6.8/30, RHZKF9/30, RHZKF6.8-1 / -2, RHZKF6.8 /A /B /C /CT /D /E, 6.8C, 6.8CT/B',
            ('Positive pressure; steel or carbon-fibre cylinders 3–9 L, 30 MPa; about 60 min with a 6.8 L cylinder', 'ضغط موجب؛ أسطوانات فولاذ أو ألياف كربون 3–9 لترات، 30 ميجاباسكال؛ نحو 60 دقيقة بأسطوانة 6.8 لتر')),
           ('BX-0761-01-002', 'Long-tube air breathing apparatus on trolley', 'جهاز تنفس بخرطوم طويل على عربة', 'HKC-30/60', ('Cylinder air supply on a trolley with a long hose', 'هواء من أسطوانات على عربة بخرطوم طويل')),
           ('BX-0761-01-003', 'Emergency escape breathing device (EEBD)', 'جهاز تنفس للهروب في الطوارئ (EEBD)', 'THDX-15', ('Escape set with hood', 'طقم هروب بغطاء رأس')),
           ('BX-0761-01-004', 'Powered air-purifying respirators & blower air supply', 'أقنعة تنقية هواء آلية وتغذية هواء بالنافخ', ('ELSP-100 and others', 'ELSP-100 وغيره'), ('Powered and blower respirators; axial-flow fan', 'أقنعة آلية وبالنافخ؛ مروحة محورية')),
           ('BX-0761-01-010', 'Breathing-air compressors', 'ضواغط هواء التنفس', 'CQ-155, MCH-6, TRD-H-W, CQ-200', ('High-pressure compressors for filling breathing-apparatus cylinders', 'ضواغط ضغط عالٍ لتعبئة أسطوانات أجهزة التنفس'))],
          unit=U_PRODUCT),
    table('suits', ('Respirators & protective suits', 'الأقنعة والبدلات الواقية'), ('', ''), SERIES,
          [('BX-0761-01-005', 'Full- and half-face respirator masks', 'أقنعة تنفس للوجه كاملاً ولنصفه', 'A100, A200, A300, A400', ('Masks with replaceable filters', 'أقنعة بمرشحات قابلة للتبديل')),
           ('BX-0761-01-006', 'Protective suits', 'بدلات واقية', ('RFH-01 / -02 and others', 'RFH-01 / -02 وغيرها'), ('Chemical splash and gas-tight suits, aluminised fire-proximity suits, anti-bee and low-temperature suits', 'بدلات للرذاذ الكيماوي ومحكمة ضد الغاز، وبدلات مؤلمنة للاقتراب من النار، وبدلات ضد النحل وللحرارة المنخفضة')),
           ('BX-0761-01-007', 'Firefighting protective clothing', 'ملابس واقية للإطفاء', ('02-type, 17-type', 'طراز 02 وطراز 17'), ('Firefighter suits', 'بدلات رجال الإطفاء'))],
          unit=U_PRODUCT),
    table('extra', ('Additional PPE', 'معدات وقاية إضافية'), ('', ''), SERIES,
          [('BX-0763-02-004', 'Nitrile disposable gloves, powder-free', 'قفازات نتريل للاستعمال مرة واحدة بلا بودرة', ('3.0 g, 3.5 g; blue, black', '3.0 جم و3.5 جم؛ أزرق وأسود'), ('Medical grade, AQL 1.5; 100 per box, 10 boxes per carton; CE and ISO', 'درجة طبية، AQL 1.5؛ 100 في العلبة و10 علب في الكرتونة؛ CE وISO')),
           ('BX-0774-01-001', 'Hi-vis mesh safety vest', 'سترة سلامة شبكية عالية الوضوح', ('Mesh vest, 120 g/m²', 'سترة شبكية، 120 جم/م²'), ('100% polyester mesh; fluorescent colours', 'شبك بوليستر 100%؛ ألوان فسفورية'))],
          unit=U_PRODUCT),
])

# p11 cap lamps, ventilation & gas detection ----------------------------------------------------------------
F['cap-lamps-ventilation-gas-detection'] = family('cap-lamps-ventilation-gas-detection', CAT, [
    table('kl', ('KL LED mining cap lamps', 'مصابيح خوذ المناجم KL LED'), ('4–6 Ah', '4–6 أمبير ساعة'),
          [C('cap', 'Capacity (Ah)', 'السعة (أمبير ساعة)'), C('volt', 'Voltage (V)', 'الجهد (فولت)'), C('dis', 'Discharge time (h)', 'زمن التفريغ (ساعة)'), C('chg', 'Charging time (h)', 'زمن الشحن (ساعة)'),
           C('lux', 'Illuminance (lux)', 'شدة الإضاءة (لوكس)'), C('cycles', 'Battery cycles', 'دورات البطارية')],
          [(None, 'KL4LM(B)', None, '4', '3.7', '18–20', '6–8', '3500–4000', '> 600'),
           (None, 'KL5LM(B)', None, '5', '3.7', '20–22', '6–8', '4500–5000', '> 600'),
           (None, 'KL6LM(B)', None, '6', '3.7', '23–25', '6–8', '5500–6000', '> 600')],
          intro=('High-power LED: one main and two auxiliary light sources.', 'LED عالي القدرة: مصدر ضوء رئيسي ومصدران مساعدان.'),
          code='BX-0005-01-027', key_rows=['cap', 'dis', 'lux']),
    table('vent', ('Ventilation and gas detection', 'التهوية وكشف الغاز'), ('', ''), [C('desc', 'Description', 'الوصف')],
          [('BX-0004-01-030', 'Local mine ventilation fans', 'مراوح تهوية موضعية للمناجم', ('Local ventilation fans for tunnels: K, DK, FBD, FBCD and FBCDZ series; KCS wet dust-removal fan', 'مراوح تهوية موضعية للأنفاق: سلاسل K وDK وFBD وFBCD وFBCDZ؛ ومروحة KCS لإزالة الغبار بالماء')),
           ('BX-0004-01-031', 'Flexible ventilation duct', 'مجرى تهوية مرن', ('Tensile, water- and flame-resistant duct, −20 to +80 °C', 'مجرى متين مقاوم للماء واللهب، من −20 إلى +80 °م')),
           ('BX-0004-01-037', 'Gas detection instruments', 'أجهزة كشف الغاز', ('Portable four-in-one gas detectors, methane and gas alarms, dust, temperature and smoke sensors, anemometers', 'كواشف غاز محمولة أربعة في واحد، وأجهزة إنذار الميثان والغاز، وحساسات الغبار والحرارة والدخان، وأجهزة قياس سرعة الهواء'))],
          unit=U_PRODUCT),
])

# p12 gas detectors & emergency eyewash ---------------------------------------------------------------------
F['gas-detectors-emergency-eyewash'] = family('gas-detectors-emergency-eyewash', CAT, [
    table('gas', ('Gas detection and emergency eyewash', 'كشف الغاز وغسيل العين في الطوارئ'), ('8 product lines', '8 خطوط منتجات'), SERIES,
          [('BX-0768-01-006', 'Portable four-gas detector', 'كاشف غاز محمول رباعي', 'BX616', ('H2S 0–100 ppm, CO 0–500 ppm, O2 0–25%, LEL 0–100%; optional pump; T90 < 30 s; ≥ 80 dB alarm; ≥ 8 h; IP66; Ex ia IIC T4 Gb; 220 g', 'H2S ‏0–100 ppm، وCO ‏0–500 ppm، وO2 ‏0–25%، وLEL ‏0–100%؛ مضخة اختيارية؛ T90 < 30 ثانية؛ إنذار ≥ 80 ديسيبل؛ ≥ 8 ساعات؛ IP66؛ Ex ia IIC T4 Gb؛ 220 جم')),
           ('BX-0768-01-007', 'Portable single-gas detector', 'كاشف غاز محمول أحادي', ('BZ100 (O2, H2S or CO)', 'BZ100 (O2 أو H2S أو CO)'), ('Electrochemical; 90 dB, light and vibration alarm; data log; 2-year sensor; IP66; Ex ia IIC T4 Ga; 85 g', 'كهروكيميائي؛ إنذار صوتي 90 ديسيبل وضوئي واهتزازي؛ تسجيل البيانات؛ حساس لسنتين؛ IP66؛ Ex ia IIC T4 Ga؛ 85 جم')),
           ('BX-0768-01-011', 'Fixed gas transmitter', 'ناقل غاز ثابت', ('GTQ-TRAX 20 (Cl2, O3, N2, H2, CO, CO2, H2S)', 'GTQ-TRAX 20 ‏(Cl2 وO3 وN2 وH2 وCO وCO2 وH2S)'), ('4–20 mA; IP66; two alarm relays; colour LCD; plug-in digital sensor', '4–20 مللي أمبير؛ IP66؛ مرحلا إنذار؛ شاشة LCD ملونة؛ حساس رقمي قابل للتركيب')),
           ('BX-0768-01-012', 'Explosion-proof fixed gas detector', 'كاشف غاز ثابت مقاوم للانفجار', ('GTQ-BS03 (CH4, H2S, HCl, LEL)', 'GTQ-BS03 ‏(CH4 وH2S وHCl وLEL)'), ('24 V DC ≤ 2.5 W; T90 ≤ 15 s (LEL), ≤ 30 s (toxic); 4–20 mA; 3 relays; Ex d IIC T6 Gb; IP67', '24 فولت مستمر ≤ 2.5 واط؛ T90 ≤ 15 ثانية (LEL) و≤ 30 ثانية (السامة)؛ 4–20 مللي أمبير؛ 3 مرحلات؛ Ex d IIC T6 Gb؛ IP67')),
           ('BX-0768-01-013', 'Fixed gas detector with LED display', 'كاشف غاز ثابت بشاشة LED', 'GTQ-TRAX 30', ('4–20 mA; IP66; two relays; external sounder-strobe; plug-in digital sensor', '4–20 مللي أمبير؛ IP66؛ مرحلان؛ جرس وضوء خارجي؛ حساس رقمي قابل للتركيب')),
           ('BX-0836-01-001', 'Portable eyewash stations', 'محطات غسيل العين المحمولة', ('8, 15 and 16 gal (30, 53, 61 L)', '8 و15 و16 جالوناً (30 و53 و61 لتراً)'), ('1.5 L/min for ≥ 15 min; 3.5–7.7 kg empty; for cyanide and acid handling areas', '1.5 لتر/دقيقة لمدة ≥ 15 دقيقة؛ 3.5–7.7 كجم فارغة؛ لمناطق مناولة السيانيد والأحماض')),
           ('BX-0836-01-002', 'Combination eyewash and safety shower', 'مغسلة عين ودش أمان مدمجان', ('Stainless 304', 'ستانلس 304'), ('Eyewash ≥ 11.4 L/min, shower > 76 L/min; 230 × 76 × 47 cm; 14 kg', 'غسيل العين ≥ 11.4 لتر/دقيقة، والدش > 76 لتر/دقيقة؛ 230 × 76 × 47 سم؛ 14 كجم')),
           ('BX-0836-01-003', 'Emergency eye-flush bottle', 'زجاجة غسيل العين للطوارئ', ('600 mL', '600 مل'), ('≥ 15 min flushing; 0.8 kg; 10 per carton', 'غسيل ≥ 15 دقيقة؛ 0.8 كجم؛ 10 في الكرتونة'))],
          unit=U_LINES),
], type_label=('Series', 'السلسلة'))

# p13 gas detection systems --------------------------------------------------------------------------------
F['gas-detection-systems'] = family('gas-detection-systems', CAT, [
    table('systems', ('Gas detectors & controllers', 'كواشف الغاز ووحدات التحكم'), ('Portable · Fixed', 'محمولة · ثابتة'), SERIES,
          [('BX-0825-01-001', 'Portable gas detectors', 'كواشف غاز محمولة', ('Single-gas, 4-in-1, pump-suction', 'أحادية، وأربعة في واحد، وبمضخة شفط'), ('O2, CO, EX (LEL), H2S and other gases; audible, visual and vibration alarms', 'O2 وCO وEX ‏(LEL) وH2S وغازات أخرى؛ إنذار صوتي وضوئي واهتزازي')),
           ('BX-0825-01-002', 'Fixed / online gas detectors', 'كواشف غاز ثابتة / متصلة', ('Single-gas, 4-in-1, wireless, high-temperature', 'أحادية، وأربعة في واحد، ولاسلكية، وللحرارة العالية'), ('For permanent installation in plants and stores', 'للتركيب الدائم في المصانع والمخازن')),
           ('BX-0825-01-003', 'Gas alarm controllers', 'وحدات التحكم بإنذار الغاز', ('Control panels', 'لوحات تحكم'), ('Connect and monitor fixed detectors', 'تربط الكواشف الثابتة وتراقبها'))],
          unit=U_PRODUCT),
], type_label=('Product', 'المنتج'))

# p14 fire extinguishers, hose reels & fire alarms -----------------------------------------------------------
F['fire-extinguishers-hose-reels-fire-alarms'] = family('fire-extinguishers-hose-reels-fire-alarms', CAT, [
    table('fire', ('Fire extinguishers, hose reels and fire alarms', 'طفايات الحريق وبكرات الخراطيم وإنذار الحريق'), ('EN3 · UL · ISO', 'EN3 · UL · ISO'), SERIES,
          [('BX-0781-01-001', 'UL-listed dry powder and CO2 extinguishers', 'طفايات بودرة جافة وثاني أكسيد الكربون مدرجة لدى UL', ('SNG01-01 to 04 (ABC 2.5–20 lb); SNG01-54 to 57 (CO2 5–20 lb)', 'SNG01-01 إلى 04 ‏(ABC ‏2.5–20 رطلاً)؛ SNG01-54 إلى 57 ‏(CO2 ‏5–20 رطلاً)'),
            ('ABC rating 1-A:10-B:C to 6-A:80-B:C, 13.5 bar; CO2 in AA6061 aluminium cylinders, 124 bar', 'تصنيف ABC من 1-A:10-B:C إلى 6-A:80-B:C، ‏13.5 بار؛ CO2 في أسطوانات ألومنيوم AA6061، ‏124 بار')),
           ('BX-0781-01-002', 'BS EN3 portable extinguishers', 'طفايات محمولة BS EN3', ('SNG01-05 to 08A, SNG01-05P1 to P12 (powder 1–12 kg); CO2 2–5 kg; water and foam 6–9 L', 'SNG01-05 إلى 08A، وSNG01-05P1 إلى P12 (بودرة 1–12 كجم)؛ CO2 ‏2–5 كجم؛ ماء ورغوة 6–9 لترات'),
            ('Kitemark EN3; nitrogen-charged ABC powder, 18 bar; up to 55A 233B C; fluorine-free foam option', 'Kitemark EN3؛ بودرة ABC مضغوطة بالنيتروجين، 18 بار؛ حتى 55A 233B C؛ خيار رغوة خالية من الفلور')),
           ('BX-0781-01-003', 'BS EN3 wheeled powder and CO2 extinguishers', 'طفايات بودرة وثاني أكسيد الكربون على عجلات BS EN3', 'SNG01-58A, 60A, 63A / B / C', ('EN3-approved wheeled units', 'وحدات على عجلات معتمدة EN3')),
           ('BX-0781-01-004', 'ISO powder and CO2 extinguishers', 'طفايات بودرة وثاني أكسيد الكربون ISO', ('SNG01-15 to 53 (powder 0.5–12 kg; CO2 1.4–10 kg)', 'SNG01-15 إلى 53 (بودرة 0.5–12 كجم؛ CO2 ‏1.4–10 كجم)'),
            ('Alloy-steel or CK45 carbon-steel CO2 cylinders; lower-cost alternative to EN3', 'أسطوانات CO2 من فولاذ سبائكي أو فولاذ كربوني CK45؛ بديل أقل تكلفة من EN3')),
           ('BX-0781-01-005', 'American-style and automatic hanging powder extinguishers', 'طفايات بودرة أمريكية الطراز وآلية معلّقة', ('SNG01-01A to 05A (lb); SNG01-73A to G (automatic)', 'SNG01-01A إلى 05A (بالرطل)؛ SNG01-73A إلى G (آلية)'),
            ('Automatic units release by heat; for generator rooms and switchboards', 'الوحدات الآلية تنطلق بالحرارة؛ لغرف المولدات ولوحات التوزيع')),
           ('BX-0781-01-006', 'Wheeled, CE powder, foam and water extinguishers', 'طفايات على عجلات وبودرة CE ورغوة وماء', 'SNG01-09 to 14, 58–64, 68–72',
            ('Wheeled 25–100 kg; CE powder 1–6 kg; foam and water 2–10 L; stainless foam tank option', 'على عجلات 25–100 كجم؛ بودرة CE ‏1–6 كجم؛ رغوة وماء 2–10 لترات؛ خيار خزان رغوة ستانلس')),
           ('BX-0781-01-010', 'Ceiling-mounted and tube-type automatic extinguishers', 'طفايات آلية سقفية وأنبوبية', ('SNG01-87A / B (3 kg ceiling); tube type for panels', 'SNG01-87A / B (سقفية 3 كجم)؛ وأنبوبية للوحات'),
            ('ABC powder or clean agent; tube bursts by heat inside electrical panels', 'بودرة ABC أو عامل نظيف؛ ينفجر الأنبوب بالحرارة داخل اللوحات الكهربائية')),
           ('BX-0781-01-018', 'Fire hose reels and semi-rigid hose', 'بكرات خراطيم الحريق والخرطوم شبه الصلب', 'SNG07-02A to 06B', ('EN 671 / LPCB hose reels with EN 694 semi-rigid hose', 'بكرات EN 671 / LPCB بخرطوم شبه صلب EN 694')),
           ('BX-0769-01-002', 'Conventional fire alarm control panels', 'لوحات تحكم إنذار حريق تقليدية', 'SR-P02, SR-P03', ('1–8 / 10 zones, up to 35 detectors per zone; AC 220 V with backup battery; sounder and relay outputs', '1–8 / 10 مناطق، حتى 35 كاشفاً لكل منطقة؛ 220 فولت متردد مع بطارية احتياطية؛ مخارج للجرس والمرحلات')),
           ('BX-0769-01-003', 'Smoke, heat and beam detectors', 'كواشف الدخان والحرارة والشعاع', 'SR-805, SR-505, SR-801, SR-B510', ('Photoelectric smoke and heat detectors (2 / 4-wire, 9–28 V DC); beam detector 5–100 m, EN 54-12', 'كواشف دخان كهروضوئية وحرارة (2 / 4 أسلاك، 9–28 فولت مستمر)؛ كاشف شعاع 5–100 م، EN 54-12')),
           ('BX-0769-01-004', 'Manual call points, sounders, strobes and bells', 'نقاط النداء اليدوية والأجراس والأضواء الوامضة', 'SR-A05, SR-A06, SR-A02, SR-A08, SR-108, SR-A82, SR-A01, SR-A93', ('Indoor and outdoor call points, sounder-strobes, 24 V fire bells', 'نقاط نداء داخلية وخارجية، وأجراس بضوء وامض، وأجراس حريق 24 فولت')),
           ('BX-0769-01-005', 'Siren strobes, call point and remote indicator', 'صفارات بضوء وامض ونقطة نداء ومؤشر عن بُعد', 'SR-A88, SR-A83, SR-A09, SR-A78-R', ('Sounder-strobes 10–30 V DC; LED remote indicator', 'أجراس بضوء وامض 10–30 فولت مستمر؛ مؤشر LED عن بُعد')),
           ('BX-0769-01-013', '30 W alarm horn', 'بوق إنذار 30 واط', 'SR-A76-30', ('12 V, 300 mA, 135 dB, two tones, 0.9 kg; for site, blasting and evacuation alarms', '12 فولت، 300 مللي أمبير، 135 ديسيبل، نغمتان، 0.9 كجم؛ لإنذارات الموقع والتفجير والإخلاء'))],
          unit=U_LINES),
], type_label=('Series', 'السلسلة'))

# p15 fire pumps, hydrants, sprinklers & foam --------------------------------------------------------------
F['fire-pumps-hydrants-sprinklers-foam'] = family('fire-pumps-hydrants-sprinklers-foam', CAT, [
    table('water', ('Fire-water & foam equipment', 'معدات مياه الحريق والرغوة'), ('8–20 bar', '8–20 بار'), SERIES,
          [('BX-0178-01-016', 'Fire-fighting pump sets', 'مجموعات مضخات الإطفاء', 'XBD-W, XBD-L', ('Horizontal (W) and vertical (L) fire pump sets', 'مجموعات مضخات حريق أفقية (W) ورأسية (L)')),
           ('BX-0791-01-001', 'Fire hoses, reels, cabinets, couplings & nozzles', 'خراطيم وبكرات وخزائن ووصلات وفوهات الحريق', ('DN50 / 65 / 80; 8–20 bar; reels 20–30 m', 'DN50 / 65 / 80؛ 8–20 بار؛ بكرات 20–30 م'), ('Hose lines and reels for hydrant cabinets', 'خطوط خراطيم وبكرات لخزائن الحنفيات')),
           ('BX-0791-01-002', 'Sprinkler heads', 'رؤوس الرشاشات', ('DN15 / DN20; 68 °C bulb', 'DN15 / DN20؛ أمبولة 68 °م'), ('Pendant, upright, sidewall, concealed and dry types; standard and quick response', 'متدلية وقائمة وجانبية ومخفية وجافة؛ استجابة عادية وسريعة')),
           ('BX-0791-01-003', 'Fire hydrant & landing valves', 'حنفيات الحريق وصمامات الهبوط', 'SN50 / 65; SS100 / 150; SSF100', ('Indoor and outdoor hydrant valves and hydrants', 'صمامات حنفيات وحنفيات داخلية وخارجية')),
           ('BX-0791-01-004', 'Fire service valves & flow indicators', 'صمامات شبكات الحريق ومؤشرات التدفق', ('Gate, butterfly, alarm, pressure-reducing', 'بوابة وفراشة وإنذار وتخفيض ضغط'), ('Valve series for fire-water networks', 'سلاسل صمامات لشبكات مياه الحريق')),
           ('BX-0791-01-005', 'Fire extinguishers', 'طفايات الحريق', ('ABC 1–50 kg; CO2 2–24 kg; water-based 1–45', 'ABC ‏1–50 كجم؛ CO2 ‏2–24 كجم؛ مائية 1–45'), ('Dry powder, CO2 and water-based types', 'بودرة جافة وثاني أكسيد الكربون ومائية')),
           ('BX-0791-01-006', 'Foam systems', 'أنظمة الرغوة', ('4–24 L/s; tanks 500–13,000 L', '4–24 لتر/ثانية؛ خزانات 500–13,000 لتر'), ('Foam nozzles, generators, hydrants, proportioners, bladder tanks, mobile foam trolleys and AFFF concentrate', 'فوهات ومولدات وحنفيات رغوة، ومُناسِبات، وخزانات بمثانة، وعربات رغوة متنقلة، ومركّز AFFF'))],
          unit=U_PRODUCT),
], type_label=('Product', 'المنتج'))

# p16 traffic cones, barriers & delineators ----------------------------------------------------------------
F['traffic-cones-barriers-delineators'] = family('traffic-cones-barriers-delineators', CAT, [
    table('traffic', ('Traffic cones, barriers and delineators', 'أقماع المرور والحواجز وعلامات التحديد'), ('300–900 mm cones', 'أقماع 300–900 مم'), SPEC,
          [('BX-0327-01-001', 'PVC traffic cones', 'أقماع مرور PVC', ('300–900 mm; reflective collars 100–150 mm; orange or black base; standard, wide and slim', '300–900 مم؛ أطواق عاكسة 100–150 مم؛ قاعدة برتقالية أو سوداء؛ قياسية وعريضة ونحيفة')),
           ('BX-0327-01-027', 'Water-filled road barriers', 'حواجز طرق تُملأ بالماء', ('Plastic, 800 mm and above; New Jersey type', 'بلاستيك، 800 مم فأكثر؛ طراز New Jersey')),
           ('BX-0331-01-016', 'Folding plastic barricades', 'حواجز بلاستيكية قابلة للطي', ('Reinforced plastic boards, galvanised legs, reflective sheeting', 'ألواح بلاستيك مقوّى وأرجل مجلفنة وشرائح عاكسة')),
           ('BX-0327-01-017', 'Flexible warning posts', 'أعمدة تحذير مرنة', ('PU / PE, high-intensity reflective bands, 450 mm and above', 'PU / PE بأشرطة عاكسة عالية الكثافة، 450 مم فأكثر')),
           ('BX-0331-01-011', 'Cone bars', 'قضبان الأقماع', ('1.8–2.15 m; yellow/black or red/white', '1.8–2.15 م؛ أصفر/أسود أو أحمر/أبيض')),
           ('BX-0327-01-020', 'Plastic chains & hooks', 'سلاسل بلاستيكية وخطافات', ('HDPE Ø 6 and 8 mm, 25 m rolls; aluminium hooks', 'HDPE بقطر 6 و8 مم، لفات 25 م؛ خطافات ألمنيوم')),
           ('BX-0327-01-014', 'Safety mesh fence & flags', 'شبك أسوار الأمان والأعلام', ('Orange HDPE 1 × 50 m, 80 g/m²; warning bunting', 'HDPE برتقالي 1 × 50 م، 80 جم/م²؛ أعلام تحذير'))],
          unit=U_PRODUCT),
], type_label=('Product', 'المنتج'))

# p17 warning lights, mirrors, tapes & wheel stops ---------------------------------------------------------
F['warning-lights-mirrors-tapes-wheel-stops'] = family('warning-lights-mirrors-tapes-wheel-stops', CAT, [
    table('warning', ('Warning lights, mirrors, tapes and wheel stops', 'مصابيح التحذير والمرايا والأشرطة ومصدات العجلات'), ('', ''), SPEC,
          [('BX-0331-01-001', 'Battery warning lamps', 'مصابيح تحذير بالبطارية', ('PC lens Ø 190–205 mm; 2–24 LEDs; flashing or steady; 4R25 6 V or D cells; visible beyond 500–1000 m', 'عدسة PC بقطر 190–205 مم؛ 2–24 LED؛ وميض أو ثابت؛ بطارية 4R25 ‏6 فولت أو D؛ رؤية أبعد من 500–1000 م')),
           ('BX-0331-01-004', 'Solar warning lamps', 'مصابيح تحذير شمسية', ('0.3–0.5 W 5.5 V panel; 3.7 V 2300 mAh lithium battery; visible beyond 1000–1500 m', 'لوح 0.3–0.5 واط 5.5 فولت؛ بطارية ليثيوم 3.7 فولت 2300 مللي أمبير ساعة؛ رؤية أبعد من 1000–1500 م')),
           ('BX-0327-01-023', 'Convex safety mirrors', 'مرايا أمان محدبة', ('PC, Ø 450, 600, 800, 1000, 1200 mm; indoor and outdoor', 'PC بقطر 450 و600 و800 و1000 و1200 مم؛ داخلية وخارجية')),
           ('BX-0327-01-028', 'Warning & barrier tapes', 'أشرطة التحذير والحواجز', ('HDPE / PVC, 50–135 mm wide, 33–500 m; printed to order; 150 mm detectable underground tape', 'HDPE / PVC بعرض 50–135 مم وطول 33–500 م؛ طباعة حسب الطلب؛ شريط كشف تحت الأرض 150 مم')),
           ('BX-0327-01-008', 'Wheel stoppers', 'مصدات العجلات', ('Rubber and plastic, up to 1830 mm long; custom logo', 'مطاط وبلاستيك بطول حتى 1830 مم؛ شعار حسب الطلب'))],
          intro=('Visibility distances as stated by the manufacturers.', 'مسافات الرؤية حسب بيانات المصنّعين.'),
          unit=U_PRODUCT),
], type_label=('Product', 'المنتج'))
