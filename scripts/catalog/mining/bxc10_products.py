"""BXC-10 Ed4 (Fleet support) product pages, catalogue pages 3–11 and 14. Text from the catalogue intros and tables.
Ed4 has product photos on pages 8 and 14 only; the other pages use photos from the suppliers' own catalogues
(prep_bxc10.py in the work dir), and the weighbridge pages (12–13) photos from the suppliers' websites
(prep_bxc10_wb.py)."""
from bxc02_products import FAQ_QUOTE, FAQ_SHIP

P = []


def prod(pid, ar, en, img, desc, features, specs, stats, summary, faq, seo):
    P.append(dict(id=pid, ar=ar, en=en, img=img, desc=desc, features=features, specs=specs, stats=stats,
                  summary=summary, faq=faq + [FAQ_QUOTE, FAQ_SHIP], seo=seo))


S = ' التوريد للشرق الأوسط وأفريقيا.'
SE = ' Supply to the Middle East and Africa.'
PICK = ('اختر من الجدول أدناه.', 'Pick from the table below.')
FQ_TYRE = ('ما المطلوب لطلب الإطارات؟', 'What do you need to order tyres?',
           'المقاس المكتوب على جانب الإطار، وعدد الطبقات (PR) أو فئة الخدمة، وبأنبوب أو بدونه، ونوع المعدة وطبيعة الأرض (صخر أو رمل أو طين)، والكمية.',
           'The size on the sidewall, the ply rating or service class, tube or tubeless, the machine and the ground (rock, sand or mud), and the quantity.')
FQ_BIAS = ('ما الفرق بين الإطار العادي والراديال؟', 'What is the difference between bias and radial tyres?',
           'الإطار العادي (Bias) أمتن في الجوانب وأرخص ويناسب المسافات القصيرة والأرض الوعرة، والراديال أبرد في التشغيل وأطول عمراً على المسافات الطويلة والسرعات الأعلى.',
           'Bias tyres have tougher sidewalls, cost less and suit short runs on rough ground; radials run cooler and last longer over long distances and higher speeds.')

prod('truck-haulage-tyres', 'إطارات الشاحنات والنقل', 'Truck & Haulage Tyres', 'tbr-tyres',
     ('إطارات عادية وراديال للقلابات وشاحنات الخدمة وناقلات التعدين: إطارات شاحنات راديال للطرق المختلطة والوعرة، وراديال التعدين للطرق الوعرة، وإطارات الصحراء والرمال، وإطارات راديال للمعدات الترابية حتى 57 بوصة للقلابات الصلبة والمفصلية.',
      'Bias and radial tyres for dump trucks, service trucks and mining haulers: mixed-road and rough-road TBR tyres, off-road mining radials, desert and sand tyres, and earthmover radials up to 57 in for rigid and articulated dump trucks.'),
     [('63 نقشة للطرق المختلطة والوعرة والتعدين', '63 tread patterns for mixed, rough and mining roads'), ('جنوط من 16 إلى 57 بوصة', 'Rims from 16 to 57 in'),
      ('إطارات راديال للقلابات الصلبة حتى 46/90R57', 'Rigid dump truck radials up to 46/90R57'), ('نقشات عميقة حتى 33.5 مم للحمولة الزائدة', 'Deep treads up to 33.5 mm for overload service')],
     [('المقاسات', '6.50-16 إلى 46/90R57', 'Sizes', '6.50-16 to 46/90R57'), ('الطبقات', 'حتى 40 PR', 'Ply rating', 'Up to 40 PR'),
      ('الفئة', 'E3–E4 للمعدات الترابية', 'Class', 'E3–E4 earthmover'), ('التركيب', 'عادي وراديال', 'Construction', 'Bias and radial')],
     [('63', 'نقشة', '63', 'Tread patterns'), ('16–57', 'قطر الجنط (بوصة)', '16–57', 'Rim (in)'), ('E3–E4', 'فئة المعدات الترابية', 'E3–E4', 'Earthmover class')],
     ('إطارات لكل شاحنة في الموقع، من شاحنة الخدمة إلى القلاب الصلب. ' + PICK[0], 'Tyres for every truck on site, from service trucks to rigid dump trucks. ' + PICK[1]),
     [FQ_TYRE, FQ_BIAS],
     ('إطارات الشاحنات والقلابات وشاحنات التعدين', 'Truck, Dump Truck and Mining Haul Tyres',
      'إطارات شاحنات راديال وعادية للطرق المختلطة والوعرة والتعدين، وإطارات راديال للقلابات حتى 46/90R57، بـ 63 نقشة.' + S,
      'Radial and bias truck tyres for mixed, rough and mining roads, and dump truck radials up to 46/90R57, in 63 tread patterns.' + SE))

prod('loader-grader-underground-tyres', 'إطارات اللوادر والجريدرات والمناجم تحت الأرض', 'Loader, Grader & Underground Tyres', 'otr-loader',
     ('إطارات عادية وراديال للوادر والجرافات والجريدرات والحفارات اللودرية والحفارات ذات العجلات، وإطارات خدمة الصخور L-4 وL-5 بنقشات حتى 105 مم، وإطارات شبه صلبة، وإطارات ملساء عميقة النقشة للوادر LHD وشاحنات المناجم تحت الأرض.',
      'Bias and radial tyres for wheel loaders, dozers, graders, backhoe loaders and wheeled excavators, rock-service L-4 and L-5 tyres with treads up to 105 mm, semi-solid tyres, and smooth deep-tread tyres for LHD loaders and underground trucks.'),
     [('نقشات L-4 وL-5 مقاومة للقطع لخدمة الصخور', 'Cut-resistant L-4 and L-5 rock-service treads'), ('نقشة حتى 105 مم', 'Tread depth up to 105 mm'),
      ('إطارات أمامية وخلفية للحفارات اللودرية', 'Front and rear backhoe loader tyres'), ('إطارات ملساء L5S للمناجم تحت الأرض', 'Smooth L5S tyres for underground mines')],
     [('المقاسات', '7.50-15 إلى 60×25-25', 'Sizes', '7.50-15 to 60×25-25'), ('الطبقات', '6.5–46 PR', 'Ply rating', '6.5–46 PR'),
      ('الفئة', 'L-3 إلى L-5، وG2 للجريدرات', 'Class', 'L-3 to L-5, G2 for graders'), ('الأنبوب', 'بأنبوب أو بدونه', 'Tube', 'Tube type or tubeless')],
     [('37', 'نقشة', '37', 'Tread patterns'), ('L-3 – L-5', 'فئة الخدمة', 'L-3 – L-5', 'Service class'), ('105 مم', 'أقصى عمق نقشة', '105 mm', 'Max tread depth')],
     ('إطارات لمعدات التحميل والتسوية، فوق الأرض وتحتها. ' + PICK[0], 'Tyres for loading and grading machines, above and below ground. ' + PICK[1]),
     [('متى أحتاج إطار L-5 بدل L-3؟', 'When do I need an L-5 tyre instead of L-3?',
       'عند التحميل على صخر مكسّر أو حواف حادة كما في المحاجر وساحات الكسارات، فنقشة L-5 أعمق وأقوى ضد القطع. للتربة والحصى يكفي L-3.',
       'When loading broken rock or sharp edges, as in quarries and crusher yards: the L-5 tread is deeper and stands up better to cuts. L-3 is enough for soil and gravel.'), FQ_TYRE],
     ('إطارات اللوادر والجريدرات والحفارات اللودرية والمناجم تحت الأرض', 'Loader, Grader, Backhoe and Underground Mining Tyres',
      'إطارات لوادر وجرافات وجريدرات وحفارات لودرية، وإطارات صخور L-4 وL-5 بنقشة حتى 105 مم، وإطارات للوادر LHD تحت الأرض.' + S,
      'Tyres for loaders, dozers, graders and backhoe loaders, L-4 and L-5 rock tyres with treads up to 105 mm, and underground LHD tyres.' + SE))

prod('loader-mining-underground-otr-tyres', 'إطارات OTR للوادر والتعدين والمناجم تحت الأرض', 'Loader, Mining & Underground OTR Tyres', 'cover-otr',
     ('إطارات للطرق الوعرة (OTR) للوادر والقلابات والشاحنات المفصلية ولوادر LHD تحت الأرض: إطارات عادية من E-3/L-3 إلى نقشات التعدين العميقة L-5، وإطارات راديال فولاذية بالكامل حتى 29.5R25.',
      'Off-the-road tyres for wheel loaders, dump trucks, articulated trucks and underground LHD loaders: bias tyres from E-3/L-3 to L-5 deep-tread mining patterns, and all-steel radial tyres up to 29.5R25.'),
     [('نقشات عادية من E-3/L-3 إلى L-5', 'Bias patterns from E-3/L-3 to L-5'), ('راديال فولاذي بالكامل حتى 29.5R25', 'All-steel radials up to 29.5R25'),
      ('إطارات ملساء L-5S للوادر LHD', 'Smooth L-5S tyres for LHD loaders'), ('مقاسات من 7.50-16 إلى 29.5-25', 'Sizes from 7.50-16 to 29.5-25')],
     [('التركيب', 'عادي وراديال فولاذي', 'Construction', 'Bias and all-steel radial'), ('الفئات', 'E-2 إلى L-5S', 'Classes', 'E-2 to L-5S'),
      ('الطبقات', '8–44 PR حسب المقاس', 'Ply rating', '8–44 PR by size'), ('الأنبوب', 'بأنبوب أو بدونه', 'Tube', 'Tube type or tubeless')],
     [('18', 'نقشة', '18', 'Patterns'), ('عادي · راديال', 'التركيب', 'Bias · Radial', 'Construction'), ('E-2 – L-5S', 'فئات الخدمة', 'E-2 – L-5S', 'Service classes')],
     ('نقشات OTR من الإنشاءات إلى التعدين تحت الأرض. ' + PICK[0], 'OTR patterns from construction to underground mining. ' + PICK[1]),
     [FQ_TYRE, FQ_BIAS],
     ('إطارات OTR للوادر والقلابات والتعدين تحت الأرض', 'OTR Tyres for Loaders, Dump Trucks and Underground Mining',
      'إطارات OTR عادية من E-3/L-3 إلى L-5، وراديال فولاذي بالكامل حتى 29.5R25، وإطارات L-5S للوادر LHD تحت الأرض.' + S,
      'Bias OTR tyres from E-3/L-3 to L-5, all-steel radials up to 29.5R25, and L-5S tyres for underground LHD loaders.' + SE))

prod('grader-roller-backhoe-truck-tyres', 'إطارات الجريدرات والمداحل والحفارات اللودرية والشاحنات', 'Grader, Roller, Backhoe & Truck Tyres', 'bias-truck',
     ('إطارات لمعدات شق الطرق ومركبات الدعم في الموقع: إطارات المداحل والجريدرات والحفارات ذات العجلات، وإطارات R-4 للحفارات اللودرية والرافعات التلسكوبية، وإطارات شاحنات راديال وعادية، وإطارات رملية لمواقع الصحراء.',
      'Tyres for site road-building and support vehicles: roller, grader and wheeled-excavator tyres, R-4 backhoe and telehandler tyres, radial and bias truck tyres, and sand tyres for desert sites.'),
     [('إطارات مداحل ملساء C-1', 'Smooth C-1 roller tyres'), ('إطارات جريدرات G-2/L-2', 'G-2/L-2 grader tyres'),
      ('إطارات R-4 للحفارات اللودرية والرافعات التلسكوبية', 'R-4 backhoe and telehandler tyres'), ('إطارات رملية من 9.00-16 إلى 16.00-20', 'Sand tyres from 9.00-16 to 16.00-20')],
     [('الفئات', 'C-1 وG-2 وR-3 وR-4', 'Classes', 'C-1, G-2, R-3, R-4'), ('قطر الجنط', '16–28 بوصة', 'Rim diameter', '16–28 in'),
      ('إطارات الشاحنات', 'راديال بأنبوب وبدونه، وعادي', 'Truck tyres', 'Radial tube and tubeless, and bias'), ('الإطارات الرملية', 'عادي للرمال', 'Sand tyres', 'Bias for sand')],
     [('21', 'نقشة وخطاً', '21', 'Patterns & lines'), ('C-1 · G-2 · R-4', 'فئات الخدمة', 'C-1 · G-2 · R-4', 'Service classes'), ('16–28', 'قطر الجنط (بوصة)', '16–28', 'Rim (in)')],
     ('إطارات لمعدات الطرق ومركبات الدعم. ' + PICK[0], 'Tyres for road-building machines and support vehicles. ' + PICK[1]),
     [FQ_TYRE, FQ_BIAS],
     ('إطارات المداحل والجريدرات والحفارات اللودرية والشاحنات والرمال', 'Roller, Grader, Backhoe, Truck and Sand Tyres',
      'إطارات مداحل C-1 وجريدرات G-2 وحفارات لودرية R-4، وإطارات شاحنات راديال وعادية، وإطارات رملية للصحراء.' + S,
      'C-1 roller, G-2 grader and R-4 backhoe tyres, radial and bias truck tyres, and sand tyres for desert sites.' + SE))

prod('solid-industrial-skid-steer-tyres', 'الإطارات الصلبة الصناعية وإطارات اللوادر الانزلاقية', 'Solid Industrial & Skid-Steer Tyres', 'narrow-lug',
     ('إطارات صلبة لا تُثقب للرافعات الشوكية ومركبات الموانئ والمصانع في مخازن الموقع وساحاته، وإطارات عادية للوادر الانزلاقية من SKS-1 إلى SKS-5.',
      'Puncture-proof solid tyres for forklifts and port or industrial vehicles in site stores and yards, and bias tyres for skid steer loaders from SKS-1 to SKS-5.'),
     [('إطارات صلبة لا تُثقب', 'Puncture-proof solid tyres'), ('مقاسات من 4.00-8 إلى 12.00-20', 'Sizes from 4.00-8 to 12.00-20'),
      ('إطارات لوادر انزلاقية SKS-1 إلى SKS-5', 'Skid steer tyres SKS-1 to SKS-5'), ('نقشة عميقة SKS-L5', 'Deep-tread SKS-L5')],
     [('الإطارات الصلبة', '4.00-8 إلى 12.00-20', 'Solid tyres', '4.00-8 to 12.00-20'), ('إطارات اللوادر الانزلاقية', '10-16.5 إلى 15-19.5', 'Skid steer tyres', '10-16.5 to 15-19.5'),
      ('فئات اللوادر الانزلاقية', 'SKS-1 إلى SKS-5', 'Skid steer classes', 'SKS-1 to SKS-5'), ('التركيب', 'صلب، وعادي', 'Construction', 'Solid, and bias')],
     [('13', 'نقشة', '13', 'Patterns'), ('صلبة', 'للرافعات والمصانع', 'Solid', 'Forklift & industrial'), ('SKS-1 – SKS-5', 'فئات اللوادر الانزلاقية', 'SKS-1 – SKS-5', 'Skid steer classes')],
     ('إطارات لمعدات المخازن والساحات. ' + PICK[0], 'Tyres for store and yard machines. ' + PICK[1]),
     [('لماذا الإطار الصلب للرافعة الشوكية؟', 'Why a solid tyre for a forklift?',
       'لأنه لا يُثقب ولا يحتاج ضبط ضغط، فيناسب الساحات التي فيها حديد وحجارة حادة ويقلل التوقف.',
       'It cannot puncture and needs no pressure checks, so it suits yards with scrap and sharp stones and cuts downtime.'), FQ_TYRE],
     ('إطارات صلبة للرافعات الشوكية وإطارات اللوادر الانزلاقية', 'Solid Forklift Tyres and Skid Steer Loader Tyres',
      'إطارات صلبة لا تُثقب من 4.00-8 إلى 12.00-20 للرافعات الشوكية والمركبات الصناعية، وإطارات لوادر انزلاقية SKS-1 إلى SKS-5.' + S,
      'Puncture-proof solid tyres from 4.00-8 to 12.00-20 for forklifts and industrial vehicles, and SKS-1 to SKS-5 skid steer tyres.' + SE))

prod('tyre-service-valves-repair-tools', 'صمامات الإطارات ومواد الإصلاح والعدد', 'Tyre Valves, Repair Materials & Tools', 'i-008-008',
     ('صمامات إطارات الشاحنات والحافلات وإطارات OTR العملاقة، وأشرطة ورقع وأطقم إصلاح، ومفاتيح صدم هوائية وروافع هوائية لإبقاء اللوادر وشاحنات النقل في العمل.',
      'Truck, bus and giant OTR tyre valves, repair strings, patches and kits, pneumatic impact wrenches and air jacks to keep loaders and haul trucks moving.'),
     [('صمامات TR وTRJ للإطارات بدون أنبوب وبأنبوب', 'TR and TRJ valves for tubeless and tube-type tyres'), ('صمامات هواء وماء للإطارات العملاقة', 'Air-water valves for giant tyres'),
      ('أطقم إصلاح للموقع والورشة', 'Repair kits for the field and the workshop'), ('مفاتيح صدم وروافع هوائية', 'Impact wrenches and air jacks')],
     [('الصمامات', 'TR وTRJ وV3', 'Valves', 'TR, TRJ and V3'), ('السدادات الفطرية', '3–6 مم', 'Mushroom plugs', '3–6 mm'),
      ('أشرطة الإصلاح', '100–200 مم', 'Repair strings', '100–200 mm'), ('العدد', 'مفاتيح صدم وروافع ونافخات حافة', 'Tools', 'Impact wrenches, jacks, bead seaters')],
     [('6', 'مجموعات منتجات', '6', 'Product groups'), ('TR · TRJ', 'الصمامات', 'TR · TRJ', 'Valves'), ('3–6 مم', 'السدادات الفطرية', '3–6 mm', 'Mushroom plugs')],
     ('كل ما تحتاجه ورشة الإطارات في الموقع. ' + PICK[0], 'Everything a site tyre shop needs. ' + PICK[1]),
     [('كيف أطلب الصمام الصحيح؟', 'How do I order the right valve?',
       'أرسل رقم الصمام المكتوب عليه (مثل TR570 أو TRJ650-03) أو صورته، مع مقاس الإطار والجنط.',
       'Send the number stamped on the valve (such as TR570 or TRJ650-03) or a photo of it, with the tyre and rim size.')],
     ('صمامات الإطارات وأطقم الإصلاح ومفاتيح الصدم الهوائية', 'Tyre Valves, Repair Kits and Pneumatic Impact Wrenches',
      'صمامات TR وTRJ للشاحنات وإطارات OTR، وأشرطة ورقع وأطقم إصلاح، ومفاتيح صدم وروافع هوائية ونافخات حافة.' + S,
      'TR and TRJ valves for truck and OTR tyres, repair strings, patches and kits, impact wrenches, air jacks and bead seaters.' + SE))

prod('bearings-mill-spares', 'المحامل وقطع غيار المطاحن', 'Bearings & Mill Spares', 'ball-mill',
     ('محامل أسطوانية كروية للكسارات والغرابيل والمطاحن، وقطع غيار طاحونة الكرات: كرات الطحن، والتبطين، والترس المحيطي، ومخفّض السرعة.',
      'Spherical roller bearings for crushers, screens and mills, and ball mill spares: grinding balls, liners, girth gear and reducer.'),
     [('محامل كروية بأنواع CA وCC وMA وMB وE1', 'Spherical roller bearings in CA, CC, MA, MB and E1 types'), ('محامل منقسمة ومحكمة 2CS', 'Split and sealed 2CS bearings'),
      ('كرات طحن فولاذية وخزفية', 'Steel and ceramic grinding balls'), ('ترس محيطي ومخفّض وألواح تبطين', 'Girth gear, reducer and liner plates')],
     [('المحامل', 'أسطوانية كروية', 'Bearings', 'Spherical roller'), ('الاستخدام', 'الكسارات والغرابيل والمطاحن', 'Use', 'Crushers, screens and mills'),
      ('كرات الطحن', 'فولاذية وخزفية', 'Grinding balls', 'Steel and ceramic'), ('قطع المطحنة', 'تبطين، ترس محيطي، مخفّض، صندوق تحكم', 'Mill parts', 'Liners, girth gear, reducer, control box')],
     [('2', 'مجموعتا منتجات', '2', 'Product groups'), ('كروية', 'نوع المحامل', 'Spherical', 'Bearing type'), ('كرات · تبطين', 'قطع المطحنة', 'Balls · liners', 'Mill spares')],
     ('قطع الغيار التي تبقي خط التكسير والطحن يعمل. ' + PICK[0], 'The spares that keep the crushing and grinding line running. ' + PICK[1]),
     [('ما المطلوب لطلب قطع المطحنة أو المحامل؟', 'What do you need to order mill spares or bearings?',
       'رقم المحمل المكتوب عليه، أو مقاس المطحنة (القطر × الطول) وصورة اللوحة، مع الكمية المطلوبة.',
       'The number marked on the bearing, or the mill size (diameter × length) and a photo of its plate, with the quantity.')],
     ('محامل الكسارات والمطاحن وقطع غيار طاحونة الكرات', 'Crusher and Mill Bearings and Ball Mill Spares',
      'محامل أسطوانية كروية للكسارات والغرابيل والمطاحن، وكرات طحن فولاذية وخزفية وتبطين وترس محيطي ومخفّض لطاحونة الكرات.' + S,
      'Spherical roller bearings for crushers, screens and mills, plus steel and ceramic grinding balls, liners, girth gear and reducer for ball mills.' + SE))

prod('workshop-tools-operator-seats-belt-parts', 'عدد الورشة ومقاعد المشغلين وقطع سيور المحركات', 'Workshop Tools, Operator Seats & Engine Belt Parts', 'seat-wrench',
     ('مثاقب وصنفرة وجلاخات ومفاتيح صدم هوائية لورشة الموقع، وغسالات ضغط بالبنزين لتنظيف المعدات، ومقاعد مشغلين بتعليق ميكانيكي أو هوائي ووحدات تعليق بديلة، وشدّادات سيور لمحركات الحفارات والجرارات والشاحنات.',
      'Air drills, sanders, grinders and impact wrenches for the site workshop, petrol pressure washers for cleaning machines, operator seats with mechanical or air suspension and spare suspension units, and belt tensioners for excavator, tractor and truck engines.'),
     [('عدد هوائية من 700 إلى 35,000 دورة/دقيقة', 'Air tools from 700 to 35,000 r/min'), ('غسالات ضغط 190 و200 بار', '190 and 200 bar pressure washers'),
      ('مقاعد بتعليق ميكانيكي أو هوائي لمستخدمين 50–150 كجم', 'Mechanical or air-suspension seats for 50–150 kg occupants'), ('شدّادات سيور برقم القطعة الأصلية', 'Belt tensioners by OE number')],
     [('العدد الهوائية', 'مثاقب، صنفرة، جلاخات، مفاتيح صدم', 'Air tools', 'Drills, sanders, grinders, impact wrenches'), ('مفتاح الصدم', '500 نيوتن·م', 'Impact wrench', '500 N·m'),
      ('غسالات الضغط', '190–200 بار، 9 لتر/دقيقة', 'Pressure washers', '190–200 bar, 9 L/min'), ('المقاعد', 'شوط تعليق 40–150 مم', 'Seats', '40–150 mm suspension stroke')],
     [('70', 'موديلاً', '70', 'Models'), ('200', 'ضغط الغسالة (بار)', '200', 'Washer pressure (bar)'), ('50–150', 'وزن المستخدم (كجم)', '50–150', 'Seat occupant (kg)')],
     ('عدد الورشة وقطع الراحة والصيانة للمعدات. ' + PICK[0], 'Workshop tools and comfort and service parts for the fleet. ' + PICK[1]),
     [('هل تناسب المقاعد معداتي؟', 'Will the seats fit my machines?',
       'أرسل نوع المعدة وموديلها وصورة قاعدة المقعد الحالي أو مسافات ثقوب التثبيت، ونطابق المقعد أو وحدة التعليق.',
       'Send the machine type and model and a photo of the current seat base or its mounting hole spacing, and we match the seat or suspension unit.'),
      ('كيف أطلب شدّاد السير؟', 'How do I order a belt tensioner?',
       'برقم القطعة الأصلية (OE) المكتوب على القطعة أو في دليل المحرك، ونؤكد المطابقة قبل التوريد.',
       'By the OE part number on the part or in the engine manual; we confirm the match before supply.')],
     ('العدد الهوائية وغسالات الضغط ومقاعد المشغلين وشدّادات السيور', 'Air Tools, Pressure Washers, Operator Seats and Belt Tensioners',
      'مثاقب وجلاخات ومفاتيح صدم هوائية، وغسالات ضغط 200 بار، ومقاعد مشغلين بتعليق ميكانيكي أو هوائي، وشدّادات سيور برقم القطعة الأصلية.' + S,
      'Air drills, grinders and impact wrenches, 200 bar pressure washers, mechanical and air-suspension operator seats, and belt tensioners by OE number.' + SE))

prod('hydraulic-hoses', 'خراطيم الهيدروليك', 'Hydraulic Hoses', 'hydraulic-hoses',
     ('خراطيم هيدروليك بديلة لمعدات الموقع والشاحنات: خراطيم ضغط عالٍ مجدولة وحلزونية بالسلك الفولاذي، وخراطيم مقوّاة بالنسيج وحرارية اللدونة، وخراطيم معدنية من الستانلس، وأنابيب نايلون لفرامل الهواء.',
      'Replacement hydraulic hoses for site machines and trucks: steel-wire braided and spiral high-pressure hoses, textile-reinforced and thermoplastic hoses, stainless metal hoses and nylon air-brake tubing.'),
     [('خراطيم SAE 100 R1AT إلى R17', 'SAE 100 R1AT to R17 hoses'), ('خراطيم EN 853 وEN 856 حلزونية 4SP / 4SH', 'EN 853 and EN 856 4SP / 4SH spiral hoses'),
      ('خراطيم حرارية اللدونة R7 / R8', 'R7 / R8 thermoplastic hoses'), ('أنابيب نايلون SAE J844 لفرامل الهواء', 'SAE J844 nylon air-brake tubing')],
     [('المعايير', 'SAE 100 وEN 853 وEN 856', 'Standards', 'SAE 100, EN 853, EN 856'), ('التقوية', 'سلك فولاذي مجدول أو حلزوني، أو نسيج', 'Reinforcement', 'Braided or spiral steel wire, or textile'),
      ('أنابيب الفرامل', 'SAE J844 النوع B', 'Brake tubing', 'SAE J844 type B'), ('الأنواع', '23 نوعاً', 'Types', '23')],
     [('23', 'نوعاً', '23', 'Types'), ('SAE · EN', 'معايير الخراطيم', 'SAE · EN', 'Hose standards'), ('J844', 'أنابيب فرامل الهواء', 'J844', 'Air-brake tubing')],
     ('الخرطوم المناسب لكل خط هيدروليك في المعدات. ' + PICK[0], 'The right hose for every hydraulic line on the fleet. ' + PICK[1]),
     [('ما المطلوب لطلب خرطوم هيدروليك؟', 'What do you need to order a hydraulic hose?',
       'المعيار المكتوب على الخرطوم (مثل R2AT أو 4SP)، والقطر الداخلي، وضغط التشغيل، والطول ونوع الوصلات في الطرفين.',
       'The standard printed on the hose (such as R2AT or 4SP), the inside diameter, the working pressure, and the length and end fittings.')],
     ('خراطيم الهيدروليك SAE وEN وأنابيب فرامل الهواء', 'SAE and EN Hydraulic Hoses and Air-Brake Tubing',
      'خراطيم هيدروليك SAE 100 من R1AT إلى R17 وEN 853 وEN 856، وخراطيم حرارية اللدونة وستانلس، وأنابيب نايلون SAE J844.' + S,
      'SAE 100 R1AT to R17, EN 853 and EN 856 hydraulic hoses, thermoplastic and stainless hoses, and SAE J844 nylon tubing.' + SE))

prod('mobile-light-towers', 'أبراج الإنارة المتنقلة', 'Mobile Light Towers', 'i-014-009',
     ('أبراج إنارة يدوية الدفع وعلى مقطورة للعمل الليلي في الحُفر والمصانع والمخيمات، بتدفق ضوئي حتى 440,000 لومن وتشغيل متواصل حتى 120 ساعة.',
      'Hand-push and trailer light towers for night work at pits, plants and camps, with up to 440,000 lumens and up to 120 hours of continuous running.'),
     [('حتى 440,000 لومن', 'Up to 440,000 lumens'), ('تشغيل حتى 120 ساعة بخزان 170 لتر', 'Up to 120 hours on a 170 L tank'),
      ('صاري حتى 11 م', 'Masts up to 11 m'), ('محركات Honda وKubota وغيرها', 'Honda, Kubota and other engines')],
     [('التدفق الضوئي', '72,000–440,000 لومن', 'Luminous flux', '72,000–440,000 lm'), ('القدرة', '2–8 كيلوواط', 'Power', '2–8 kW'),
      ('الصاري', '1.7–11 م', 'Mast', '1.7–11 m'), ('النوع', 'يدوي الدفع أو مقطورة', 'Type', 'Hand-push or trailer')],
     [('7', 'موديلات', '7', 'Models'), ('440,000', 'لومن كحد أقصى', '440,000', 'Max lumens'), ('120 ساعة', 'أقصى مدة تشغيل', '120 h', 'Max runtime')],
     ('إنارة متنقلة للعمل الليلي في الموقع. ' + PICK[0], 'Mobile lighting for night work on site. ' + PICK[1]),
     [('أي برج يناسب الحفرة الليلية؟', 'Which tower suits a pit at night?',
       'برج على مقطورة بأربعة مصابيح 1000 واط وصاري 11 م يغطي مساحة أوسع، والأبراج اليدوية للورش والمخيمات والمساحات الصغيرة.',
       'A trailer tower with four 1000 W lamps and an 11 m mast covers a wider area; hand-push towers suit workshops, camps and small areas.')],
     ('أبراج الإنارة المتنقلة بالديزل والبنزين', 'Mobile Light Towers',
      'أبراج إنارة يدوية وعلى مقطورة من 72,000 إلى 440,000 لومن، بصاري حتى 11 م وتشغيل حتى 120 ساعة.' + S,
      'Hand-push and trailer light towers from 72,000 to 440,000 lm, with masts up to 11 m and up to 120 hours of running.' + SE))

FQ_WB = ('ما المطلوب لاختيار ميزان الشاحنات؟', 'What do you need to choose a weighbridge?',
         'أثقل شاحنة محمّلة تزنها، وأطول شاحنة، وعدد الشاحنات في اليوم، وهل يُركّب في حفرة أو فوق الأرض، ونوع التربة ومصدر الكهرباء في الموقع.',
         'The heaviest loaded truck, the longest truck, the trucks per day, pit or pitless installation, and the ground and power on site.')

prod('weighbridges-axle-scales', 'موازين الشاحنات وموازين المحاور', 'Weighbridges & Axle Scales', 'wb-axle',
     ('موازين شاحنات رقمية كاملة بطول 7 إلى 24 م لشاحنات 30–120 طناً، مع خلايا الوزن والمؤشر وصندوق التوصيل وأدوات التثبيت، وموازين محاور محمولة للتحقق من حمولات الخام والمركّز عند بوابة المنجم.',
      'Complete digital weighbridges 7 to 24 m long for 30–120 t trucks, with load cells, indicator, junction box and fixings, plus portable axle weighing pads for checking ore and concentrate loads at the mine gate.'),
     [('طقم كامل بمنصة 12 مم من 2 إلى 4 أقسام', 'Complete set with a 12 mm deck in 2–4 sections'), ('خلايا وزن رقمية 30 طن (OIML R76، CE)', '30 t digital load cells (OIML R76, CE)'),
      ('كابل 50 م في أنبوب فولاذي وصندوق توصيل IP68', '50 m cable in steel conduit and IP68 junction box'), ('وسائد محاور محمولة مع عربة نقل', 'Portable axle pads with a carrying trolley')],
     [('السعة', '30–120 طن', 'Capacity', '30–120 t'), ('طول المنصة', '7–24 م', 'Deck length', '7–24 m'),
      ('خلايا الوزن', 'رقمية 30 طن، OIML R76', 'Load cells', 'Digital 30 t, OIML R76'), ('موازين المحاور', 'OP-923 وOP-928', 'Axle scales', 'OP-923 and OP-928')],
     [('14', 'موديلاً ومقاساً', '14', 'Models and sizes'), ('30–120', 'السعة (طن)', '30–120', 'Capacity (t)'), ('7–24', 'طول المنصة (م)', '7–24', 'Deck length (m)')],
     ('وزن شاحنات الخام عند بوابة الموقع. ' + PICK[0], 'Weighing ore trucks at the site gate. ' + PICK[1]),
     [FQ_WB, ('متى أختار وسائد المحاور بدل الميزان الثابت؟', 'When do I choose axle pads instead of a fixed weighbridge?',
       'حين يتنقل الوزن بين مواقع، أو يلزم التحقق من الحمولة قبل تركيب ميزان ثابت. الوسائد تُحمل وتُفرد على أرض مستوية، والميزان الثابت أنسب للوزن اليومي الكثيف.',
       'When weighing moves between sites, or loads must be checked before a fixed weighbridge is installed. The pads are carried and laid on level ground; a fixed weighbridge suits heavy daily weighing.')],
     ('موازين الشاحنات الرقمية وموازين المحاور المحمولة', 'Digital Weighbridges and Portable Axle Scales',
      'موازين شاحنات رقمية كاملة 30–120 طناً بطول 7–24 م، مع خلايا الوزن والمؤشر، ووسائد وزن محاور محمولة.' + S,
      'Complete digital weighbridges for 30–120 t trucks, 7–24 m long, with load cells and indicator, plus portable axle weighing pads.' + SE))

prod('weighbridges-platform-scales-load-cells', 'موازين الشاحنات وموازين المنصة وخلايا الوزن', 'Weighbridges, Platform Scales & Load Cells', 'wb-cells',
     ('موازين شاحنات رقمية من 30 إلى 200 طن بمنصات حتى 30 م لوزن شاحنات الخام، وخلايا وزن رقمية للموازين الجديدة والقائمة، وموازين منصة من 1 إلى 5 أطنان لأكياس الخام والمواد في المخازن.',
      'Digital weighbridges from 30 to 200 t with decks up to 30 m for weighing ore trucks, digital load cells for new and existing weighbridges, and 1–5 t platform scales for ore bags and materials in stores.'),
     [('منصة فولاذ Q235 بعوارض U ولوح 8–14 مم', 'Q235 steel deck with U-beams and 8–14 mm plate'), ('OIML R76 الفئة III وحمل زائد آمن 125%', 'OIML R76 Class III and 125% safe overload'),
      ('خلايا QS-D وQSA بمخرج RS485', 'QS-D and QSA cells with RS485 output'), ('موازين منصة 1–5 طن بلوح مضلّع', '1–5 t platform scales with checker plate')],
     [('السعة', '30–200 طن', 'Capacity', '30–200 t'), ('المنصة', 'عرض 3–6 م، طول 4–30 م', 'Deck', '3–6 m wide, 4–30 m long'),
      ('التدريج', '10 / 20 / 50 كجم', 'Division', '10 / 20 / 50 kg'), ('خلايا الوزن', 'C3، ±0.02%، IP68', 'Load cells', 'C3, ±0.02%, IP68')],
     [('3', 'خطوط منتجات', '3', 'Product lines'), ('30–200 طن', 'سعة ميزان الشاحنات', '30–200 t', 'Truck scale capacity'), ('4–30 م', 'طول المنصة', '4–30 m', 'Deck length')],
     ('من ميزان الشاحنات إلى ميزان المخزن. ' + PICK[0], 'From the weighbridge to the store scale. ' + PICK[1]),
     [FQ_WB, ('هل تناسب الخلايا الرقمية ميزاناً قائماً؟', 'Do the digital load cells fit an existing weighbridge?',
       'نعم في الغالب، بخلايا QS-D أو QSA من 20 إلى 50 طناً. أرسل عدد الخلايا وسعتها وطريقة تركيبها، أو صورة لها، ونؤكد المطابقة.',
       'Usually yes, with QS-D or QSA cells from 20 to 50 t. Send the number of cells, their capacity and mounting, or a photo, and we confirm the match.')],
     ('موازين الشاحنات حتى 200 طن وخلايا الوزن وموازين المنصة', 'Weighbridges up to 200 t, Load Cells and Platform Scales',
      'موازين شاحنات رقمية 30–200 طن بمنصات حتى 30 م (OIML R76)، وخلايا وزن QS-D وQSA، وموازين منصة 1–5 طن.' + S,
      'Digital weighbridges from 30 to 200 t with decks up to 30 m (OIML R76), QS-D and QSA load cells, and 1–5 t platform scales.' + SE))
