"""BXC-08 Ed7 product pages (catalogue pages 3–8): induction furnaces, additional melting furnaces, firebricks and
induction units, crucibles, refractories and ceramics, ceramic fibre insulation. Text from the catalogue intros and
tables; header figures from the catalogue pages, except the refractories page, which has none (from its table)."""
from bxc02_products import FAQ_QUOTE, FAQ_SHIP

P = []


def prod(pid, ar, en, img, desc, features, specs, stats, summary, faq, seo):
    P.append(dict(id=pid, ar=ar, en=en, img=img, desc=desc, features=features, specs=specs, stats=stats,
                  summary=summary, faq=faq + [FAQ_QUOTE, FAQ_SHIP], seo=seo))


S = ' التوريد للشرق الأوسط وأفريقيا.'
SE = ' Supply to the Middle East and Africa.'
PICK = ('اختر من الجدول أدناه.', 'Pick from the table below.')

prod('induction-gold-smelting-furnaces', 'أفران صهر الذهب بالحث', 'Induction Gold Smelting Furnaces', 'furnace',
     ('أفران حث لصهر الذهب والفضة والنحاس: تسخن البوتقة بسرعة للصهر والتنقية والصب والتحبيب. من وحدات محمولة تصهر 1 كجم في دقائق إلى أفران متوسطة التردد بلا قلب تتسع لـ 500 كجم.',
      'Induction furnaces for melting gold, silver and copper: the crucible heats rapidly for smelting, refining, casting and granulating. From portable units melting 1 kg in minutes to medium-frequency coreless furnaces holding 500 kg.'),
     [('8 أفران محمولة عالية ومتوسطة التردد من 2 إلى 70 كيلوواط، بسعة 1–100 كجم للصهرة', '8 portable high/medium-frequency furnaces, 2–70 kW, 1–100 kg per melt'),
      ('فرنا WGR عاليا التردد لـ 1–4 كجم ذهب في أقل من 5–8 دقائق', '2 WGR high-frequency furnaces for 1–4 kg of gold in under 5–8 minutes'),
      ('3 أفران GWJ متوسطة التردد بلا قلب بسعة 150 و250 و500 كجم وحرارة مقننة 1600 °م', '3 GWJ medium-frequency coreless furnaces, 150, 250 and 500 kg, rated 1600 °C'),
      ('تغذية 220 فولت للوحدات الصغيرة و380 فولت ثلاثية الأطوار للأكبر', '220 V supply for the smallest unit, 380 V three-phase for the rest')],
     [('سعة الصهرة', '1–500 كجم', 'Capacity per melt', '1–500 kg'), ('حرارة الفرن', '1500–2000 °م', 'Furnace temperature', '1500–2000 °C'),
      ('القدرة', '2–275 كيلوواط', 'Power', '2–275 kW'), ('التغذية', '220 أو 380 فولت', 'Supply', '220 or 380 V')],
     [('13', 'موديلاً', '13', 'Models'), ('1–500 كجم', 'سعة الصهرة', '1–500 kg', 'Capacity per melt'), ('1500–2000 °م', 'حرارة الفرن', '1500–2000 °C', 'Furnace temperature')],
     ('أفران حث لصهر الذهب من وحدات محمولة 1 كجم إلى أفران GWJ بسعة 500 كجم. ' + PICK[0],
      'Induction furnaces for gold, from 1 kg portable units to 500 kg GWJ furnaces. ' + PICK[1]),
     [('أي فرن يناسب كمية الذهب لدي؟', 'Which furnace suits the amount of gold I melt?',
       'اختر الفرن بسعة الصهرة في الجدول: الأفران المحمولة حتى 100 كجم، وWGR لـ 1–4 كجم بسرعة، وGWJ من 150 إلى 500 كجم. أرسل لنا الكمية في كل صهرة ومصدر الكهرباء في الموقع لنحدد الموديل.',
       'Choose by the melting capacity in the table: portable furnaces up to 100 kg, WGR for 1–4 kg quickly, and GWJ from 150 to 500 kg. Send us the amount per melt and the power on site and we set the model.')],
     ('أفران صهر الذهب بالحث 1–500 كجم', 'Induction Gold Smelting Furnaces 1–500 kg',
      'أفران حث لصهر الذهب والفضة والنحاس: وحدات محمولة 2–70 كيلوواط، وأفران WGR عالية التردد، وأفران GWJ متوسطة التردد حتى 500 كجم.' + S,
      'Induction furnaces for melting gold, silver and copper: portable 2–70 kW units, WGR high-frequency furnaces and GWJ medium-frequency furnaces up to 500 kg.' + SE))

prod('gold-melting-furnaces', 'أفران صهر الذهب – موديلات إضافية', 'Gold Melting Furnaces – Additional Models', 'furnace',
     ('فرن منضدي 1 كجم للورش الصغيرة، ووحدات حث عالية التردد تصهر 1–5 كجم من الذهب أو الفضة في 3–5 دقائق، وأفران حث بخزانة من 1 إلى 8 كجم، وأفران متوسطة التردد حتى 160 كيلوواط للمصافي.',
      'A 1 kg bench furnace for small workshops, high-frequency induction units melting 1–5 kg of gold or silver in 3–5 minutes, cabinet induction furnaces from 1 to 8 kg, and medium-frequency furnaces up to 160 kW for refineries.'),
     [('فرن JL-MF-1 لصهر حتى 1 كجم بقدرة 1500 واط وحرارة حتى 1150 °م', 'JL-MF-1 for up to 1 kg, 1500 W, up to 1150 °C'),
      ('أفران JL-15KW وJL-25KW عالية التردد لـ 1–5 كجم في 3–5 دقائق', 'JL-15KW and JL-25KW high-frequency furnaces for 1–5 kg in 3–5 minutes'),
      ('أفران JL-MFG بخزانة من 1 إلى 8 كجم بتشغيل 24 ساعة بالحمل الكامل', 'JL-MFG cabinet furnaces from 1 to 8 kg, 24 h full-load duty'),
      ('أفران JLZ متوسطة التردد 15–160 كيلوواط، ثابتة أو قلّابة أو بالدفع', 'JLZ medium-frequency furnaces, 15–160 kW, fixed, tilting or push-out')],
     [('المعدن الثمين في الصهرة', '1–250 كجم', 'Precious metal per melt', '1–250 kg'), ('زمن الصهر (الوحدات الصغيرة)', '3–5 دقائق', 'Melting time (small units)', '3–5 min'),
      ('القدرة', '1.5–160 كيلوواط', 'Power', '1.5–160 kW'), ('التغذية', '110 أو 220 أو 380 فولت', 'Supply', '110, 220 or 380 V')],
     [('19', 'موديلاً ومقاساً', '19', 'Models and sizes'), ('1–250 كجم', 'المعدن الثمين في الصهرة', '1–250 kg', 'Precious metal per melt'), ('3–5 دقائق', 'زمن الصهر (الصغيرة)', '3–5 min', 'Melting time (small units)')],
     ('أربع سلاسل إضافية لصهر الذهب، من فرن منضدي 1 كجم إلى أفران JLZ حتى 160 كيلوواط. ' + PICK[0],
      'Four more gold-melting series, from a 1 kg bench furnace to JLZ furnaces up to 160 kW. ' + PICK[1]),
     [('هل تصلح هذه الأفران لمعادن غير الذهب؟', 'Do these furnaces melt metals other than gold?',
       'نعم. الأفران عالية التردد وأفران الخزانة تصهر الذهب والفضة والنحاس، وأفران JLZ تصهر أيضاً الفولاذ والألومنيوم بسعات مختلفة مذكورة في الجدول.',
       'Yes. The high-frequency and cabinet furnaces melt gold, silver and copper, and the JLZ furnaces also melt steel and aluminium, with the capacities given in the table.')],
     ('أفران صهر الذهب: JL-MF وJL وJL-MFG وJLZ', 'Gold Melting Furnaces: JL-MF, JL, JL-MFG and JLZ',
      'أفران صهر الذهب والمعادن الثمينة من 1 إلى 250 كجم: فرن منضدي 1 كجم، وأفران حث عالية التردد وبخزانة، وأفران JLZ متوسطة التردد حتى 160 كيلوواط.' + S,
      'Gold and precious-metal melting furnaces from 1 to 250 kg: a 1 kg bench furnace, high-frequency and cabinet induction furnaces, and JLZ medium-frequency furnaces up to 160 kW.' + SE))

prod('firebricks-electrodes-induction-units', 'الطوب الحراري والأقطاب ووحدات الحث', 'Firebricks, Electrodes & Induction Units', 'bricks',
     ('طوب حراري وملاط حراري وأقطاب جرافيت لبطانات الأفران، مع وحدات تسخين وصهر بالحث عالية ومتوسطة التردد ومبرّدات هوائية مناسبة لها.',
      'Firebricks, refractory mortars and graphite electrodes for furnace linings, plus high- and medium-frequency induction heating and melting units with matching air-cooled chillers.'),
     [('طوب حراري عازل بـ 9 درجات من 1200 إلى 1730 °م', 'Insulating firebrick in 9 grades, 1200–1730 °C'),
      ('طوب طيني حراري وعالي الألومينا SK30–SK40، وملاط HJM حتى 1760 °م', 'SK30–SK40 fire clay and high-alumina bricks, HJM mortars up to 1760 °C'),
      ('أقطاب جرافيت RP وHP وUHP لأفران القوس الكهربائي', 'RP, HP and UHP graphite electrodes for electric-arc furnaces'),
      ('وحدات حث GHF وGMF من 8 إلى 500 كيلوواط، ومبرّدات CA بسعة 1.5–26 كيلوواط', 'GHF and GMF induction units from 8 to 500 kW, CA chillers 1.5–26 kW')],
     [('حرارة الطوب والملاط', '1200–1760 °م', 'Brick and mortar rating', '1200–1760 °C'), ('قدرة وحدات الحث', '8–500 كيلوواط', 'Induction power', '8–500 kW'),
      ('التردد', '1–100 كيلوهرتز', 'Frequency', '1–100 kHz'), ('التبريد', 'مائي، مع مبرّدات CA', 'Cooling', 'Water, with CA chillers')],
     [('63', 'موديلاً ودرجة', '63', 'Models & grades'), ('15–500 كيلوواط', 'قدرة الحث', '15–500 kW', 'Induction power'), ('1200–1760 °م', 'حرارة الطوب والملاط', '1200–1760 °C', 'Brick & mortar rating')],
     ('مواد بطانة الأفران ووحدات الحث والمبرّدات من مصدر واحد. ' + PICK[0],
      'Furnace lining materials, induction units and chillers from one source. ' + PICK[1]),
     [('هل تحتاج وحدة الحث إلى مبرّد؟', 'Does an induction unit need a chiller?',
       'وحدات الحث مبرّدة بالماء: تحتاج ماءً بضغط نحو 0.2 ميجاباسكال، ومبرّدات CA الهوائية توفر ذلك بخزان ومضخة. أرسل لنا موديل الوحدة لنختار سعة المبرّد.',
       'The induction units are water cooled and need water at about 0.2 MPa; the air-cooled CA chillers supply it with their own tank and pump. Send us the unit model and we size the chiller.')],
     ('الطوب الحراري وأقطاب الجرافيت ووحدات الحث', 'Firebricks, Graphite Electrodes & Induction Units',
      'طوب حراري عازل وطيني وعالي الألومينا، وملاط حراري حتى 1760 °م، وأقطاب جرافيت، ووحدات حث GHF وGMF حتى 500 كيلوواط ومبرّدات CA.' + S,
      'Insulating, fire clay and high-alumina firebricks, refractory mortars up to 1760 °C, graphite electrodes, GHF and GMF induction units up to 500 kW and CA chillers.' + SE))

prod('fused-quartz-silicon-carbide-crucibles', 'بوتقات الكوارتز المنصهر وكربيد السيليكون', 'Fused-Quartz & Silicon-Carbide Crucibles', 'crucibles',
     ('بوتقات من الكوارتز المنصهر (السيليكا) لصهر الذهب بالحث، مقاساتها لصهرات من 1 إلى 20 كجم، وبوتقات من كربيد السيليكون تُصنع حسب الطلب لأفران الصهر بالغاز والديزل.',
      'Fused-quartz (silica) crucibles for induction gold melting, sized for 1 to 20 kg melts, and silicon-carbide crucibles made to order for gas and diesel melting furnaces.'),
     [('7 مقاسات متوفرة من الكوارتز المنصهر بقطر 100–365 مم', '7 fused-quartz sizes in stock, 100–365 mm diameter'),
      ('لصهرات ذهب 1 و2 و3 و5 و10 و20 كجم', 'For 1, 2, 3, 5, 10 and 20 kg gold melts'),
      ('مقاسات أخرى تُصنع حسب الطلب', 'Other sizes made to order'),
      ('بوتقات كربيد السيليكون لأفران الغاز والديزل حسب المقاس والسعة', 'Silicon-carbide crucibles for gas and diesel furnaces, made to size and capacity')],
     [('القطر', '100–365 مم', 'Diameter', '100–365 mm'), ('الارتفاع', '130–345 مم', 'Height', '130–345 mm'),
      ('صهرة الذهب', '1–20 كجم', 'Gold melt', '1–20 kg'), ('كربيد السيليكون', 'حسب الطلب', 'Silicon carbide', 'Made to order')],
     [('7', 'مقاسات متوفرة', '7', 'Sizes in stock'), ('1–20 كجم', 'صهرة الذهب', '1–20 kg', 'Gold melt'), ('100–365 مم', 'القطر', '100–365 mm', 'Diameter')],
     ('بوتقات كوارتز منصهر لصهر الذهب بالحث، وبوتقات كربيد سيليكون حسب الطلب. ' + PICK[0],
      'Fused-quartz crucibles for induction gold melting and silicon-carbide crucibles made to order. ' + PICK[1]),
     [('ما المطلوب لعرض سعر بوتقة كربيد السيليكون؟', 'What do you need to quote a silicon-carbide crucible?',
       'القطر الخارجي والارتفاع وسعة المعدن ونوع الفرن (غاز أو ديزل)، فهي تُصنع حسب الطلب.',
       'The outer diameter, height, metal capacity and furnace type (gas or diesel), as they are made to order.')],
     ('بوتقات صهر الذهب: كوارتز منصهر وكربيد السيليكون', 'Gold Melting Crucibles: Fused Quartz & Silicon Carbide',
      'بوتقات كوارتز منصهر لصهر الذهب بالحث بقطر 100–365 مم لصهرات 1–20 كجم، وبوتقات كربيد السيليكون لأفران الغاز والديزل حسب الطلب.' + S,
      'Fused-quartz crucibles for induction gold melting, 100–365 mm diameter for 1–20 kg melts, and silicon-carbide crucibles for gas and diesel furnaces made to order.' + SE))

prod('refractories-quartz-glass-ceramics', 'الحراريات وزجاج الكوارتز والسيراميك', 'Refractories, Quartz Glass & Ceramics', 'bricks-2',
     ('خرسانات حرارية وطوب وعوازل لأفران الصهر وأفران الكربون، مع بوتقات الكوارتز والسيراميك الفني لخدمة الحرارة العالية والتآكل.',
      'Castables, bricks and insulation for smelting furnaces and carbon kilns, with quartz crucibles and technical ceramics for high-temperature and wear service.'),
     [('خرسانات حرارية منخفضة الأسمنت وعازلة خفيفة حتى 1400 °م', 'Low-cement and lightweight insulating castables up to 1400 °C'),
      ('طوب عالي الألومينا وفوسفاتي وطيني بمقاومة حرارية 1720–1790 °م', 'High-alumina, phosphate-bonded and fire-clay bricks, refractoriness 1720–1790 °C'),
      ('طوب وخرسانات عازلة بكرات ألومينا مجوفة وموليت، وألواح عزل', 'Hollow-sphere alumina and mullite insulating bricks and castables, insulation boards'),
      ('زجاج كوارتز وسيراميك صناعي يُصنعان حسب الطلب أو الرسم', 'Quartz glass and industrial ceramics made to order or to drawing')],
     [('أقصى حرارة تشغيل', '900–1400 °م', 'Max. service temperature', '900–1400 °C'), ('مقاومة الطوب الحرارية', '1720–1790 °م', 'Brick refractoriness', '1720–1790 °C'),
      ('الكثافة الظاهرية', '0.28–2.7 جم/سم³', 'Bulk density', '0.28–2.7 g/cm³'), ('زجاج الكوارتز والسيراميك', 'حسب الطلب', 'Quartz glass and ceramics', 'Made to order')],
     [('12', 'منتجاً', '12', 'Products'), ('900–1400 °م', 'حرارة تشغيل الخرسانات والألواح', '900–1400 °C', 'Castable and board service temp.'), ('1720–1790 °م', 'مقاومة الطوب الحرارية', '1720–1790 °C', 'Brick refractoriness')],
     ('مواد حرارية وعازلة لأفران الصهر، مع زجاج الكوارتز والسيراميك الصناعي. ' + PICK[0],
      'Refractory and insulating materials for smelting furnaces, with quartz glass and industrial ceramics. ' + PICK[1]),
     [('ما الفرق بين الخرسانة الحرارية والخرسانة العازلة؟', 'What is the difference between a castable and an insulating castable?',
       'الخرسانة الحرارية منخفضة الأسمنت كثيفة (2.30–2.55 جم/سم³) للبطانة الملامسة للحرارة حتى 1400 °م، والعازلة خفيفة (0.8–1.2 جم/سم³) خلفها لتقليل فقد الحرارة.',
       'Low-cement castable is dense (2.30–2.55 g/cm³) for the hot-face lining up to 1400 °C; the insulating castable is light (0.8–1.2 g/cm³) and goes behind it to cut heat loss.')],
     ('الحراريات وزجاج الكوارتز والسيراميك للأفران', 'Furnace Refractories, Quartz Glass & Ceramics',
      'خرسانات حرارية وعازلة، وطوب عالي الألومينا وفوسفاتي وطيني، وألواح عزل، وزجاج كوارتز وسيراميك صناعي لأفران صهر الذهب.' + S,
      'Refractory and insulating castables, high-alumina, phosphate-bonded and fire-clay bricks, insulation boards, quartz glass and industrial ceramics for gold smelting furnaces.' + SE))

prod('ceramic-fibre-furnace-insulation', 'الألياف الخزفية وعزل الأفران', 'Ceramic Fibre & Furnace Insulation', 'fibre',
     ('بطانيات وألواح وورق ومنسوجات من الألياف الخزفية والألياف القابلة للذوبان حيوياً، وألواح ميكروبورية، لتبطين أفران الصهر وعزلها، ولأغطية البوتقات وأبواب الأفران والوصلات.',
      'Ceramic and bio-soluble fibre blankets, boards, paper, textiles and microporous panels for lining and insulating melting furnaces, crucible covers, furnace doors and joints.'),
     [('بطانيات ألياف خزفية بتصنيف 1260 و1430 °م وكثافة 80–160 كجم/م³', 'Ceramic fibre blankets rated 1260 and 1430 °C, 80–160 kg/m³'),
      ('ألواح وأشكال مشكّلة بالتفريغ لـ 950–1350 °م، وورق ألياف بدرجات STD وHA وHZ', 'Boards and vacuum-formed shapes for 950–1350 °C, fibre paper in STD, HA and HZ grades'),
      ('قماش وأشرطة وحبال لأبواب الأفران والوصلات حتى 1000 °م', 'Cloth, tape and rope for furnace doors and joints up to 1000 °C'),
      ('ألياف قابلة للذوبان حيوياً وألواح ميكروبورية لأفران الصهر', 'Bio-soluble fibres and microporous boards for melting furnaces')],
     [('حرارة التصنيف', '950–1430 °م', 'Classification temperature', '950–1430 °C'), ('الكثافة', '80–650 كجم/م³', 'Density', '80–650 kg/m³'),
      ('الأشكال', 'بطانيات وألواح وورق وقماش وأشرطة وحبال', 'Forms', 'Blanket, board, paper, cloth, tape, rope'), ('الاستخدام', 'تبطين الأفران وأغطية البوتقات والأبواب', 'Use', 'Furnace linings, crucible covers, doors')],
     [('30', 'درجة ونوعاً', '30', 'Grades & types'), ('950–1430 °م', 'حرارة التصنيف', '950–1430 °C', 'Classification temp.'), ('80–650 كجم/م³', 'الكثافة', '80–650 kg/m³', 'Density')],
     ('ألياف خزفية ومواد عزل لأفران الصهر بكل الأشكال. ' + PICK[0],
      'Ceramic fibre and insulation for melting furnaces in every form. ' + PICK[1]),
     [('متى أختار الألياف القابلة للذوبان حيوياً؟', 'When should I choose bio-soluble fibre?',
       'حين تكفي حرارة تصنيف 1260 °م وتريد أليافاً أسهل في المناولة، فهي ذات ذوبانية ≥ 200 ملغ/لتر. للحرارة الأعلى اختر ألياف 1430 °م الخزفية.',
       'When a 1260 °C classification is enough and you want fibre that is easier to handle, as its solubility is ≥ 200 mg/l. For higher temperatures choose the 1430 °C ceramic fibre.')],
     ('الألياف الخزفية وعزل أفران الصهر حتى 1430 °م', 'Ceramic Fibre & Furnace Insulation up to 1430 °C',
      'بطانيات وألواح وورق وقماش وأشرطة وحبال من الألياف الخزفية والقابلة للذوبان حيوياً، وألواح ميكروبورية لعزل أفران صهر الذهب.' + S,
      'Ceramic and bio-soluble fibre blankets, boards, paper, cloth, tape and rope, and microporous boards for insulating gold melting furnaces.' + SE))
