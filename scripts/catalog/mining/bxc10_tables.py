"""BXC-10 Ed4 (Fleet support) model tables, catalogue pages 3–14. Typed from the page text and checked against the
page images where cells wrap. Every code is in the supplier list under BXC-10. Machine and truck brand names in the
belt-tensioner rows are left out (compatibility by OE number on request); engine makes in the light-tower table stay."""
from lib import table, family

CAT = 'BXC-10 Ed4'
F = {}
U_LINES = {'ar': ['خط واحد', 'خطان', 'خطوط'], 'en': ['product line', 'product lines']}
U_PRODUCT = {'ar': ['منتج واحد', 'منتجان', 'منتجات'], 'en': ['product', 'products']}
U_PATTERN = {'ar': ['نقشة واحدة', 'نقشتان', 'نقشات'], 'en': ['tyre line', 'tyre lines']}
SERIES = [('models', 'Sizes / models', 'المقاسات والموديلات'), ('data', 'Key data', 'أهم البيانات')]
C = lambda k, en, ar: (k, en, ar)
BIAS = ('Bias', 'عادي (Bias)')

# p3 truck & haulage tyres ---------------------------------------------------------------------------------
F['truck-haulage-tyres'] = family('truck-haulage-tyres', CAT, [
    table('truck', ('Truck and haulage tyres', 'إطارات الشاحنات والنقل'), ('16–57 in rims', 'جنوط 16–57 بوصة'), SERIES,
          [('BX-0256-01-002', 'Mixed-road TBR tyres', 'إطارات شاحنات راديال للطرق المختلطة',
            'A9, A805, A807, A958, B958, A803, A802, A812, A815, A928, A816', ('Heavy load; drive and all-position; 10.00R20, 11.00R20, 12.00R20, 12.00R24, 12R22.5, 13R22.5, 295/80R22.5, 315/80R22.5; 16–22 PR; tread 18–25 mm', 'أحمال ثقيلة؛ للدفع وكل المواضع؛ 10.00R20 و11.00R20 و12.00R20 و12.00R24 و12R22.5 و13R22.5 و295/80R22.5 و315/80R22.5؛ 16–22 PR؛ عمق النقشة 18–25 مم')),
           ('BX-0256-01-003', 'Rough-road & mining TBR tyres', 'إطارات شاحنات راديال للطرق الوعرة',
            'A903, A906, A916, A66+ / A990, A907, A908, A913, A917, A918, A915', ('Mining and overload service; 9.00R20 to 12.00R20, 12.00R24, 12R22.5, 13R22.5, 295/80R22.5; 16–22 PR; tread 21–33.5 mm', 'للتعدين والحمولة الزائدة؛ 9.00R20 إلى 12.00R20، و12.00R24 و12R22.5 و13R22.5 و295/80R22.5؛ 16–22 PR؛ عمق النقشة 21–33.5 مم')),
           ('BX-0297-02-003', 'On / off-road radial TBR tyres', 'إطارات راديال للطرق المعبّدة والوعرة', 'SYT705, SYT706, SYT901, SYT902, SYT988, SYT733',
            ('11R22.5 to 13R22.5, 9.00R20 to 12.00R24, 295/75R22.5, 295/80R22.5, 17.5 in and 16 in LT sizes; 14–20 PR', '11R22.5 إلى 13R22.5، و9.00R20 إلى 12.00R24، و295/75R22.5 و295/80R22.5، ومقاسات LT ‏17.5 و16 بوصة؛ 14–20 PR')),
           ('BX-0297-02-004', 'Off-road (mining) radial TBR tyres', 'إطارات راديال للتعدين والطرق الوعرة', 'SYT903, SYT908, SYT917, SYT928, SYT930, SYT996, SYT998, SYT990',
            ('10.00R20 to 12.00R24, 12R22.5, 13R22.5, 315/80R22.5, 8.25R16LT; up to 24 PR; tread 19–27 mm', '10.00R20 إلى 12.00R24، و12R22.5 و13R22.5 و315/80R22.5 و8.25R16LT؛ حتى 24 PR؛ عمق النقشة 19–27 مم')),
           ('BX-0297-03-002', 'Mining truck drive radial tyres', 'إطارات راديال لدفع شاحنات التعدين', 'M255, M253, M256, M257, M259',
            ('12.00R20 22 PR, 12.00R24, 315/80R22.5 22 PR; tread 24–30 mm; low-speed drive wheels on poor roads', '12.00R20 ‏22 PR، و12.00R24، و315/80R22.5 ‏22 PR؛ عمق النقشة 24–30 مم؛ لعجلات الدفع منخفضة السرعة على الطرق الرديئة')),
           ('BX-0297-03-001', 'Haulage service radial tyres', 'إطارات راديال لخدمة النقل', 'TCM01, TCS01',
            ('TCM01: 14.00R20 and 16.00R20, 20 PR, tread 21.5 mm, rough and desert roads; TCS01: 525/65R20.5, 20 PR, E-7, 6500 kg at 50 km/h, for sand', 'TCM01: ‏14.00R20 و16.00R20، ‏20 PR، عمق 21.5 مم، للطرق الوعرة والصحراوية؛ TCS01: ‏525/65R20.5، ‏20 PR، ‏E-7، ‏6500 كجم عند 50 كم/ساعة، للرمل')),
           ('BX-0297-01-021', 'Mining truck bias tyres', 'إطارات عادية لشاحنات التعدين', 'AP-MNT, AP233, AP988, AP310, AP316, AP222, AP-MNR',
            ('6.50-16 to 16.00-25; 14–40 PR; TT; loads up to 14,500 kg', '6.50-16 إلى 16.00-25؛ 14–40 PR؛ بأنبوب؛ أحمال حتى 14,500 كجم')),
           ('BX-0297-03-003', 'TC200 mining truck radials', 'إطارات تعدين راديال TC200', 'TC207, TC208, TC208 PRO, TC202, TC205, TC209', ('14.00R25 and 16.00R25; E3 / E4', '14.00R25 و16.00R25؛ E3 / E4')),
           ('BX-0297-03-004', 'Mining truck radial tyres', 'إطارات راديال لشاحنات التعدين', 'TC219, TC217',
            ('TC219: 16.00R25, E3, heat-resistant compound; TC217: 18.00R25, 480/95R29, 505/95R29, E3, groove-crack resistant', 'TC219: ‏16.00R25، ‏E3، خليط مقاوم للحرارة؛ TC217: ‏18.00R25 و480/95R29 و505/95R29، ‏E3، مقاوم لتشقق الأخاديد')),
           ('BX-0297-03-008', 'Articulated dump truck radial tyres', 'إطارات راديال للقلابات المفصلية', 'TAD01, TAD02', ('26.5R25, 29.5R25; E4 / L4; open tread for low heat build-up', '26.5R25 و29.5R25؛ E4 / L4؛ نقشة مفتوحة لحرارة أقل')),
           ('BX-0297-03-009', 'Rigid dump truck radial tyres', 'إطارات راديال للقلابات الصلبة', 'TCD01, TCD04, TCD02, TCD03',
            ('18.00R33 to 46/90R57, incl. 21.00R35, 24.00R35, 27.00R49, 33.00R51, 37.00R57, 40.00R57; E4; extra-deep tread', '18.00R33 إلى 46/90R57، منها 21.00R35 و24.00R35 و27.00R49 و33.00R51 و37.00R57 و40.00R57؛ E4؛ نقشة عميقة جداً'))],
          unit=U_PATTERN),
], type_label=('Series', 'السلسلة'), unit=U_PATTERN)

# p4 loader, grader & underground tyres ---------------------------------------------------------------------
F['loader-grader-underground-tyres'] = family('loader-grader-underground-tyres', CAT, [
    table('loader', ('Loader, dozer, grader, backhoe and underground tyres', 'إطارات اللوادر والجرافات والجريدرات والحفارات اللودرية والمناجم تحت الأرض'), ('L-3 to L-5', 'L-3 إلى L-5'), SERIES,
          [('BX-0297-01-007', 'Loader & mini loader tyres', 'إطارات اللوادر الكبيرة والصغيرة', 'AT-LMAX', ('L-3 / E-3; 16/70-20 to 33.25-35, incl. 13.00-25, 17.5-25, 20.5-25, 23.5-25, 26.5-25, 29.5-25; 8–44 PR; cut-resistant', 'L-3 / E-3؛ 16/70-20 إلى 33.25-35، منها 13.00-25 و17.5-25 و20.5-25 و23.5-25 و26.5-25 و29.5-25؛ 8–44 PR؛ مقاومة للقطع')),
           ('BX-0297-01-010', 'L-5 rock & semi-solid loader tyres', 'إطارات لوادر صخور L-5 وشبه صلبة', ('AT-ML5, semi-solid', 'AT-ML5، شبه صلبة'), ('AT-ML5: 16/70-16 to 35/65-33; 14–42 PR; tread up to 105 mm; semi-solid: 16/70-24, 16/70-20, 20.5/70-16, 16/70-16', 'AT-ML5: ‏16/70-16 إلى 35/65-33؛ 14–42 PR؛ نقشة حتى 105 مم؛ شبه الصلبة: 16/70-24 و16/70-20 و20.5/70-16 و16/70-16')),
           ('BX-0297-01-011', 'L-4 loader & dozer tyres', 'إطارات لوادر وجرافات L-4', 'AT-L4C, AT-ML4, AT-LMAX4, AT-ZLUG4', ('Heavy-duty rock service; 17.5-25, 23.5-25, 26.5-25, 29.5-25, 29.5-29; 16–46 PR; tread 45–64 mm; TL', 'خدمة شاقة على الصخور؛ 17.5-25 و23.5-25 و26.5-25 و29.5-25 و29.5-29؛ 16–46 PR؛ نقشة 45–64 مم؛ بدون أنبوب')),
           ('BX-0297-01-008', 'Loader, grader and dozer tyres', 'إطارات اللوادر والجريدرات والجرافات', 'AT-ZLUG', ('20.5/70-16, 15.5-25 to 26.5-25; 12–36 PR; TT / TL', '20.5/70-16، و15.5-25 إلى 26.5-25؛ 12–36 PR؛ بأنبوب أو بدونه')),
           ('BX-0297-01-009', 'Loader tyres', 'إطارات اللوادر', 'AT-DURO', ('17.5-25, 23.5-25, 23.1-26; 16–28 PR; TT / TL', '17.5-25 و23.5-25 و23.1-26؛ 16–28 PR؛ بأنبوب أو بدونه')),
           ('BX-0297-03-006', 'Loader and dozer radial tyres', 'إطارات راديال للوادر والجرافات', 'TCL01, TCL03, TCL04, TCL05', ('17.5R25 to 29.5R25; TCL01 E3 / L3, TCL03 and TCL04 L5, TCL05 E3 / L3 / G3', '17.5R25 إلى 29.5R25؛ TCL01 ‏E3 / L3، وTCL03 وTCL04 ‏L5، وTCL05 ‏E3 / L3 / G3')),
           ('BX-0297-01-012', 'Grader tyres', 'إطارات الجريدرات', 'AT-MGR', ('13.00-24, 14.00-24, 16.00-24, 15.5-25, 17.5-25, 20.5-25, 23.5-25; 12–20 PR', '13.00-24 و14.00-24 و16.00-24 و15.5-25 و17.5-25 و20.5-25 و23.5-25؛ 12–20 PR')),
           ('BX-0297-03-007', 'Grader radial tyres', 'إطارات راديال للجريدرات', 'TGR01', ('14.00R24, 17.5R25; G2; open non-directional tread that sheds mud', '14.00R24 و17.5R25؛ G2؛ نقشة مفتوحة غير اتجاهية تطرد الطين')),
           ('BX-0297-01-002', 'Backhoe loader rear tyres', 'إطارات خلفية للحفارات اللودرية', 'AT-BKR1, AT-BKR1A, AT-BKR1B, AT-BKR1C, AT-BKR1G, AT-BKRN, AT-BKR2', ('14.9-24, 16.9-24 / 28, 17.5L-24, 18.4-24 / 26 / 28, 19.5L-24, 21L-24; 10–16 PR; TL', '14.9-24 و16.9-24 / 28 و17.5L-24 و18.4-24 / 26 / 28 و19.5L-24 و21L-24؛ 10–16 PR؛ بدون أنبوب')),
           ('BX-0297-01-003', 'Backhoe loader front tyres', 'إطارات أمامية للحفارات اللودرية', 'AT-BKF1, AT-BKF1N, AT-BKF2', ('10.5/80-18, 12.5/80-18, 11L-15, 11L-16; 10–16 PR; TL', '10.5/80-18 و12.5/80-18 و11L-15 و11L-16؛ 10–16 PR؛ بدون أنبوب')),
           ('BX-0297-01-005', 'Wheeled excavator tyres', 'إطارات الحفارات ذات العجلات', ('AT-EX1 to AT-EX6', 'AT-EX1 إلى AT-EX6'), ('7.50-16, 8.25-16, 8.25-20, 9.00-20, 10.00-20, 11.00-20; 14–18 PR; TT', '7.50-16 و8.25-16 و8.25-20 و9.00-20 و10.00-20 و11.00-20؛ 14–18 PR؛ بأنبوب')),
           ('BX-0297-01-018', 'Underground mining tyres', 'إطارات المناجم تحت الأرض', 'AT-UB1, AT-UB3, AT-US5L, AT-US5LA, AT-US5', ('7.50-15 to 60×25-25, for LHD loaders and underground trucks; 6.5–40 PR; tread up to 100 mm', '7.50-15 إلى 60×25-25، للوادر LHD وشاحنات المناجم تحت الأرض؛ 6.5–40 PR؛ نقشة حتى 100 مم')),
           ('BX-0297-03-010', 'Underground vehicle radial tyres', 'إطارات راديال للمناجم تحت الأرض', 'TCU01', ('17.5R25, 18.00R25, 23.5R25, 26.5R25; L5S extra-deep smooth tread', '17.5R25 و18.00R25 و23.5R25 و26.5R25؛ L5S بنقشة ملساء عميقة جداً'))],
          unit=U_PATTERN),
], type_label=('Series', 'السلسلة'), unit=U_PATTERN)

# p5 loader, mining & underground OTR tyres -----------------------------------------------------------------
OT = lambda code, en, ar, models, data: (code, en, ar, models, data)
F['loader-mining-underground-otr-tyres'] = family('loader-mining-underground-otr-tyres', CAT, [
    table('otr', ('Loader & dump truck OTR tyres', 'إطارات OTR للوادر والقلابات'), ('E-2 to E-4', 'E-2 إلى E-4'), SERIES,
          [OT('BX-0290-01-001', 'Loader & dump truck OTR tyre, E-3/L-3', 'إطار OTR للوادر والقلابات، E-3/L-3',
              'SH311: 7.50-16, 8.25-16, 12.00-16, 14/90-16, 14.00-24, 15.5-25, 16.00-24, 16.00-25, 16/70-20, 16/70-24, 17.5-25, 18.00-25, 20.5/70-16, 20.5-25, 23.5-25, 26.5-25, 29.5-25',
              ('Bias; horizontal block, wide tread; 8–44 PR by size; TT / TL; construction, gravel roads and mining', 'عادي؛ نقشة كتل أفقية عريضة؛ 8–44 PR حسب المقاس؛ بأنبوب أو بدونه؛ للإنشاءات والطرق الحصوية والتعدين')),
           OT('BX-0290-01-002', 'Wheel loader OTR tyre, E-3/L-3', 'إطار OTR للوادر، E-3/L-3', 'SH312: 14.00-24, 17.5-25, 20.5-25, 23.5-25', ('Bias; loaders and dump trucks; TT / TL', 'عادي؛ للوادر والقلابات؛ بأنبوب أو بدونه')),
           OT('BX-0290-01-003', 'Wheel loader OTR tyre, L-3', 'إطار OTR للوادر، L-3', 'SH313: 16/70-20, 20.5/70-16, 17.5-25, 20.5-25, 26.5-25', ('Bias; loaders', 'عادي؛ للوادر')),
           OT('BX-0290-01-004', 'Wheel loader OTR tyre, L-3', 'إطار OTR للوادر، L-3', 'SH316: 17.5-25, 20.5-25, 23.5-25', ('Bias; loaders', 'عادي؛ للوادر')),
           OT('BX-0290-01-005', 'Wheel loader OTR tyre, L-3', 'إطار OTR للوادر، L-3', 'SH318: 16/70-20, 20.5/70-16', ('Bias; loaders', 'عادي؛ للوادر')),
           OT('BX-0290-01-006', 'All-steel radial OTR tyre, E-3/L-3', 'إطار OTR راديال فولاذي E-3/L-3', 'SH391: 17.5R25, 20.5R25, 23.5R25, 26.5R25', ('Loaders and articulated trucks', 'للوادر والشاحنات المفصلية')),
           OT('BX-0290-01-007', 'All-steel radial OTR tyre, E-4/L-4', 'إطار OTR راديال فولاذي E-4/L-4', 'SH392: 26.5R25, 29.5R25', ('TL; load index 193B/209A2 (26.5R25), 200B/216A2 (29.5R25)', 'بدون أنبوب؛ مؤشر الحمولة 193B/209A2 ‏(26.5R25) و200B/216A2 ‏(29.5R25)')),
           OT('BX-0290-01-008', 'All-steel radial OTR tyre, E-2', 'إطار OTR راديال فولاذي E-2', 'SH393: 14.00R25 (385/95R25)', ('3-star; tread 23 mm; 6,000 kg; TL; 170E / 170F', '3 نجوم؛ نقشة 23 مم؛ 6,000 كجم؛ بدون أنبوب؛ 170E / 170F')),
           OT('BX-0290-01-009', 'All-steel radial mining tyre, E-3', 'إطار تعدين راديال فولاذي E-3', 'SH395: 14.00R25 (385/95R25)', ('Tread 26 mm; 6,050 / 10,000 kg; TT; 170B / 188A2', 'نقشة 26 مم؛ 6,050 / 10,000 كجم؛ بأنبوب؛ 170B / 188A2')),
           OT('BX-0290-01-010', 'All-steel radial mining tyre, E-4', 'إطار تعدين راديال فولاذي E-4', 'SH396: 14.00R25 (385/95R25)', ('Tread 40 mm; 6,050 / 10,000 kg; TT; 170B / 188A2', 'نقشة 40 مم؛ 6,050 / 10,000 كجم؛ بأنبوب؛ 170B / 188A2'))],
          unit=U_PATTERN),
    table('mining', ('Mining & underground tyres', 'إطارات التعدين والمناجم تحت الأرض'), ('L-4 to L-5S', 'L-4 إلى L-5S'), SERIES,
          [OT('BX-0290-01-011', 'Mining loader tyre, L-4 deep tread', 'إطار لوادر تعدين L-4 بنقشة عميقة', 'SH321: 23.5-25', BIAS),
           OT('BX-0290-01-012', 'Mining loader tyre, L-5 extra-deep tread', 'إطار لوادر تعدين L-5 بنقشة عميقة جداً', 'SH322: 23.5-25', ('Bias; cut-resistant', 'عادي؛ مقاوم للقطع')),
           OT('BX-0290-01-013', 'Mining tyre', 'إطار تعدين', 'SH325: 14.00-20', ('Bias; mining category', 'عادي؛ فئة التعدين')),
           OT('BX-0290-01-014', 'Mining tyre', 'إطار تعدين', 'SH326: 12.00-20, 13.00-25', ('Bias; mining category', 'عادي؛ فئة التعدين')),
           OT('BX-0290-01-015', 'Mining loader tyre, L-4', 'إطار لوادر تعدين L-4', 'SH328: 17.5-25', BIAS),
           OT('BX-0290-01-016', 'Mining loader tyre, L-5', 'إطار لوادر تعدين L-5', ('SH329: 16/70-20, 20.5/70-16, 17.5-25, 20.5-25 and larger sizes', 'SH329: ‏16/70-20 و20.5/70-16 و17.5-25 و20.5-25 ومقاسات أكبر'), BIAS),
           OT('BX-0290-01-017', 'Underground mine tyre, E-4', 'إطار مناجم تحت الأرض E-4', 'SH368: 10.00-20', ('Bias; underground trucks and loaders; 18 PR; 3,900 kg; TT', 'عادي؛ لشاحنات ولوادر المناجم تحت الأرض؛ 18 PR؛ 3,900 كجم؛ بأنبوب')),
           OT('BX-0290-01-018', 'Underground mine smooth tyre, L-5S', 'إطار أملس للمناجم تحت الأرض L-5S', 'SH369: 10.00-20, 12.00-24, 17.5-25', ('Bias; underground LHD loaders', 'عادي؛ للوادر LHD تحت الأرض'))],
          unit=U_PATTERN),
], type_label=('Product', 'المنتج'), unit=U_PATTERN)

# p6 grader, roller, backhoe & truck tyres -------------------------------------------------------------------
F['grader-roller-backhoe-truck-tyres'] = family('grader-roller-backhoe-truck-tyres', CAT, [
    table('road', ('Road-building & excavator tyres', 'إطارات معدات الطرق والحفارات'), ('C-1 · G-2 · R-3', 'C-1 · G-2 · R-3'), SERIES,
          [OT('BX-0290-01-019', 'Road roller tyre, C-1 smooth', 'إطار مدحلة أملس C-1', 'SH302: 9.00-20, 10.00-20, 11.00-20', ('Bias; pneumatic rollers', 'عادي؛ للمداحل الهوائية')),
           OT('BX-0290-01-020', 'Roller / loader tyre, R-3', 'إطار مدحلة / لودر R-3', 'SH303: 23.1-26', ('Bias; compactors and loaders', 'عادي؛ للمداحل واللوادر')),
           OT('BX-0290-01-021', 'Grader / roller tyre, G-2/L-2', 'إطار جريدر / مدحلة G-2/L-2', 'SH317: 15.5-25, 17.5-25', ('Bias; graders and rollers', 'عادي؛ للجريدرات والمداحل')),
           OT('BX-0290-01-022', 'Motor grader tyre, G-2/L-2', 'إطار جريدر G-2/L-2', 'SH319: 13.00-24, 14.00-24', ('Bias; motor graders', 'عادي؛ للجريدرات')),
           OT('BX-0290-01-023', 'Wheeled excavator tyre', 'إطار حفار بعجلات', 'SH331: 9.00-20, 10.00-20', ('Bias; wheeled excavators', 'عادي؛ للحفارات ذات العجلات'))],
          unit=U_PATTERN),
    table('backhoe', ('Backhoe loader & industrial tyres', 'إطارات الحفارات اللودرية والإطارات الصناعية'), ('R-4', 'R-4'), SERIES,
          [OT('BX-0290-01-037', 'Backhoe loader tyre, R-4', 'إطار حفار لودري R-4', 'SH211: 16.9-28', ('Bias; backhoe loaders and industrial tractors', 'عادي؛ للحفارات اللودرية والجرارات الصناعية')),
           OT('BX-0290-01-038', 'Backhoe loader tyre, R-4', 'إطار حفار لودري R-4', 'SH215: 12.5/80-18', ('Bias; backhoe loaders', 'عادي؛ للحفارات اللودرية')),
           OT('BX-0290-01-039', 'Backhoe loader tyre, R-4', 'إطار حفار لودري R-4', 'SH216: 16.9-24, 18.4-26', ('Bias; backhoe loaders', 'عادي؛ للحفارات اللودرية')),
           OT('BX-0290-01-040', 'Backhoe loader tyre, R-4A', 'إطار حفار لودري R-4A', 'SH217: 12.5/80-18', ('Bias; backhoe loaders', 'عادي؛ للحفارات اللودرية')),
           OT('BX-0290-01-041', 'Industrial tyre, R-4B', 'إطار صناعي R-4B', 'SH218: 19.5L-24', ('Bias; DW16 rim; 16 PR; 4,035 kg; TL', 'عادي؛ جنط DW16؛ 16 PR؛ 4,035 كجم؛ بدون أنبوب')),
           OT('BX-0290-01-042', 'Backhoe & telehandler tyre, R-4', 'إطار حفار لودري ورافعة تلسكوبية R-4', 'SH219: 10.5/80-18', ('Bias; backhoe loaders and telehandlers', 'عادي؛ للحفارات اللودرية والرافعات التلسكوبية'))],
          unit=U_PATTERN),
    table('truck', ('Truck & sand tyres', 'إطارات الشاحنات والرمال'), ('16–24 in', '16–24 بوصة'), SERIES,
          [OT('BX-0311-01-001', 'Truck & bus radials, tube type', 'إطارات راديال للشاحنات بأنبوب', '9.00R20, 10.00R20, 11.00R20, 12.00R20, 12.00R24', ('Trucks and buses; steer, drive, trailer and all-position patterns', 'للشاحنات والحافلات؛ نقشات للتوجيه والدفع والمقطورة وكل المواضع')),
           OT('BX-0311-01-002', 'Truck & bus radials, tubeless', 'إطارات راديال للشاحنات بدون أنبوب', '11R22.5, 12R22.5, 13R22.5, 275/80R22.5, 295/75R22.5, 295/80R22.5, 315/80R22.5, 385/65R22.5, 11R24.5, 325/95R24', ('Trucks and buses; long-haul, regional and mixed service', 'للشاحنات والحافلات؛ للمسافات الطويلة والإقليمية والخدمة المختلطة')),
           OT('BX-0290-01-050', 'Heavy-duty bias truck tyres', 'إطارات شاحنات عادية للخدمة الشاقة', 'SH613, SH614, SH625: 7.00-20, 7.50-20, 8.25-20, 9.00-20, 10.00-20', ('Dump and service trucks', 'للقلابات وشاحنات الخدمة')),
           OT('BX-0290-01-052', 'Sand / desert flotation tyres', 'إطارات رملية للصحراء', 'SH701, SH702, SH703, SH705, SH706: 9.00-16, 9.00-17, 12.00-20, 14.00-20, 16.00-20', ('Bias; trucks and off-road vehicles on sand', 'عادي؛ للشاحنات والمركبات على الرمال'))],
          unit=U_PATTERN),
], type_label=('Product', 'المنتج'), unit=U_PATTERN)

# p7 solid industrial & skid-steer tyres ---------------------------------------------------------------------
F['solid-industrial-skid-steer-tyres'] = family('solid-industrial-skid-steer-tyres', CAT, [
    table('solid', ('Solid forklift & industrial tyres', 'إطارات صلبة للرافعات الشوكية والمركبات الصناعية'), ('Solid', 'صلبة'), SERIES,
          [OT('BX-0290-01-024', 'Solid forklift tyre', 'إطار صلب للرافعات الشوكية', ('SH268 A: 8.25-15 and other sizes', 'SH268 A: ‏8.25-15 ومقاسات أخرى'), ('Press-on / pneumatic-shaped solid tyre', 'إطار صلب بالضغط أو بشكل الإطار الهوائي')),
           OT('BX-0290-01-025', 'Solid forklift tyre', 'إطار صلب للرافعات الشوكية', ('SH268 B: 4.00-8, 21x8-9 and other sizes', 'SH268 B: ‏4.00-8 و21x8-9 ومقاسات أخرى'), ('Solid tyre', 'إطار صلب')),
           OT('BX-0290-01-026', 'Solid forklift tyre', 'إطار صلب للرافعات الشوكية', ('SH268 C: 5.00-8, 8.15-15, 28x9-15 and other sizes', 'SH268 C: ‏5.00-8 و8.15-15 و28x9-15 ومقاسات أخرى'), ('Solid tyre', 'إطار صلب')),
           OT('BX-0290-01-027', 'Solid forklift tyre', 'إطار صلب للرافعات الشوكية', 'SH278: 5.00-8, 6.00-9, 7.00-9, 6.50-10, 7.00-12, 8.25-12, 7.00-15, 7.50-15, 28x9-15, 8.25-15', ('Solid tyre', 'إطار صلب')),
           OT('BX-0290-01-028', 'Solid industrial tyre', 'إطار صناعي صلب', 'SH288: 10.00-20, 12.00-20', ('Heavy forklifts, port and industrial vehicles', 'للرافعات الشوكية الثقيلة ومركبات الموانئ والمصانع')),
           OT('BX-0290-01-029', 'Solid forklift tyre', 'إطار صلب للرافعات الشوكية', 'SH298: 5.00-8, 6.00-9, 6.50-10, 7.00-12, 7.00-15, 7.50-15, 7.50-16, 8.25-15, 18x7-8, 23x10-12, 28x9-15', ('Solid tyre', 'إطار صلب'))],
          unit=U_PATTERN),
    table('skid', ('Skid steer loader tyres', 'إطارات اللوادر الانزلاقية'), ('SKS-1 to SKS-5', 'SKS-1 إلى SKS-5'), SERIES,
          [OT('BX-0290-01-030', 'Skid steer loader tyre, SKS-1', 'إطار لودر انزلاقي SKS-1', 'SH231: 10-16.5', BIAS),
           OT('BX-0290-01-031', 'Skid steer loader tyre, SKS-2', 'إطار لودر انزلاقي SKS-2', 'SH232: 10-16.5, 12-16.5', BIAS),
           OT('BX-0290-01-032', 'Skid steer loader tyre, SKS-4', 'إطار لودر انزلاقي SKS-4', 'SH234: 10-16.5, 12-16.5', BIAS),
           OT('BX-0290-01-033', 'Skid steer loader tyre, SKS-L5', 'إطار لودر انزلاقي SKS-L5', 'SH235: 10-16.5, 12-16.5', ('Bias; deep tread', 'عادي؛ نقشة عميقة')),
           OT('BX-0290-01-034', 'Skid steer loader tyre, SKS-5', 'إطار لودر انزلاقي SKS-5', 'SH236: 10-16.5, 12-16.5, 12.5/80-18', BIAS),
           OT('BX-0290-01-035', 'Skid steer / loader tyre, G-2/L-2', 'إطار لودر انزلاقي / لودر G-2/L-2', 'SH237: 10-16.5, 12-16.5, 15-19.5', BIAS),
           OT('BX-0290-01-036', 'Skid steer / loader tyre, G-2/L-2', 'إطار لودر انزلاقي / لودر G-2/L-2', 'SH239: 14-17.5', BIAS)],
          unit=U_PATTERN),
], type_label=('Product', 'المنتج'), unit=U_PATTERN)

# p8 tyre service: valves, repair & tools --------------------------------------------------------------------
F['tyre-service-valves-repair-tools'] = family('tyre-service-valves-repair-tools', CAT, [
    table('service', ('Valves, repair materials and tyre tools', 'الصمامات ومواد الإصلاح وعدد الإطارات'), ('6 product groups', '6 مجموعات منتجات'),
          [C('range', 'Range', 'المدى'), C('purpose', 'Purpose', 'الغرض')],
          [('BX-0254-01-003', 'Truck & bus tyre valves', 'صمامات إطارات الشاحنات والحافلات', 'TR570 series (TR500–TR575), V3-02 to V3-20 metal valves, TR75A–TR179A, TR543–TR547',
            ('Tubeless and tube-type valves for trucks, buses and tractors', 'صمامات للإطارات بدون أنبوب وبأنبوب للشاحنات والحافلات والجرارات')),
           ('BX-0254-01-005', 'OTR tyre valves', 'صمامات إطارات OTR', 'TR618A, TR621A–TR623A, TRJ650-03 to TRJ658-03, TRJ691, TRJ694, TRJ1014A, TR218A / TR220A, TRJ1175C, TRJ661, TRJ662',
            ('Giant tyres on loaders and mining dump trucks, incl. air-water valves', 'للإطارات العملاقة على اللوادر وقلابات التعدين، منها صمامات الهواء والماء')),
           ('BX-0254-01-008', 'Repair strings & patches', 'أشرطة ورقع الإصلاح', ('Strings 100–200 mm; inner-tube, tubeless, radial and bias patches; mushroom plugs 3–6 mm', 'أشرطة 100–200 مم؛ رقع للأنبوب الداخلي وللإطارات بدون أنبوب والراديال والعادية؛ سدادات فطرية 3–6 مم'),
            ('Puncture repair in the field and the workshop', 'إصلاح الثقوب في الموقع والورشة')),
           ('BX-0254-01-010', 'Tyre repair kits', 'أطقم إصلاح الإطارات', ('Cased kits with reamer, inserter, strings and cement', 'أطقم في حقائب بمثقاب ومُدخل وأشرطة ولاصق'), ('Vehicle and fleet emergency kits', 'أطقم طوارئ للمركبات والأسطول')),
           ('BX-0254-01-012', 'Pneumatic impact wrenches', 'مفاتيح صدم هوائية', ('3880, 7032, 8810, 950 and 799 series; cased kits with sockets', 'سلاسل 3880 و7032 و8810 و950 و799؛ أطقم في حقائب مع لقم'), ('Removing and fitting wheel nuts', 'فك صواميل العجلات وتركيبها')),
           ('BX-0254-01-013', 'Air jacks & bead seaters', 'روافع هوائية وأجهزة تثبيت حافة الإطار', ('Air-bag jacks and bead-blaster tanks', 'روافع بالوسائد الهوائية وخزانات نفخ الحافة'), ('Lifting vehicles and seating tubeless tyres', 'رفع المركبات وتثبيت الإطارات بدون أنبوب'))],
          intro=('Valve codes follow the standard TR / TRJ designations.', 'أكواد الصمامات حسب تسميات TR / TRJ القياسية.'),
          unit=U_PRODUCT),
], type_label=('Product', 'المنتج'))

# p9 bearings & mill spares ---------------------------------------------------------------------------------
F['bearings-mill-spares'] = family('bearings-mill-spares', CAT, [
    table('spares', ('Bearings and mill spares', 'المحامل وقطع غيار المطاحن'), ('', ''), [C('desc', 'Description', 'الوصف')],
          [('BX-0061-02-001', 'Spherical roller bearings', 'محامل أسطوانية كروية (دحروجية متمركزة ذاتياً)',
            ('Types CA, CC, MA, MB, E1, toroidal, SAC, sealed 2CS, BS/SB, split, extended inner ring, and mixer bearings; for crushers, screens and mills', 'أنواع CA وCC وMA وMB وE1 وحلقية وSAC ومحكمة 2CS وBS/SB ومنقسمة وبحلقة داخلية ممتدة ومحامل الخلاطات؛ للكسارات والغرابيل والمطاحن')),
           ('BX-0018-05-002', 'Ball mill components', 'مكونات طاحونة الكرات', ('Steel and ceramic grinding balls, liner plates, girth gear, reducer and electrical control box', 'كرات طحن فولاذية وخزفية، وألواح تبطين، وترس محيطي، ومخفّض سرعة، وصندوق تحكم كهربائي'))],
          unit=U_PRODUCT),
], type_label=('Product', 'المنتج'))

# p10 workshop tools, operator seats & engine belt parts ------------------------------------------------------
F['workshop-tools-operator-seats-belt-parts'] = family('workshop-tools-operator-seats-belt-parts', CAT, [
    table('tools', ('Workshop tools', 'عدد الورشة'), ('', ''), SERIES,
          [('BX-0711-01-008', 'Straight air drills', 'مثاقب هوائية مستقيمة', 'PS-L35T6 / T8 / T10, PS-L35A, PS-950 series', ('Chuck 6–10 mm (3/8–1/2 in); 700–35,000 r/min; 0.72–1.4 kg', 'ظرف 6–10 مم (3/8–1/2 بوصة)؛ 700–35,000 دورة/دقيقة؛ 0.72–1.4 كجم')),
           ('BX-0711-01-009', 'Pistol air drills', 'مثاقب هوائية مسدسية', 'PS-750T6 / T8 / T10, PS-750A and PS-750S series', ('Chuck 6–10 mm; 700–18,000 r/min; 0.75–1.15 kg', 'ظرف 6–10 مم؛ 700–18,000 دورة/دقيقة؛ 0.75–1.15 كجم')),
           ('BX-0711-01-010', 'Angle air drills', 'مثاقب هوائية زاوية', 'PS-550P45RB, PS-550P36RB, PS-550P20RB, PS-550P07RB', ('1/4 in-28 UNF head; 700–4500 r/min; 1.35–1.65 kg; for tight spaces', 'رأس 1/4 بوصة-28 UNF؛ 700–4500 دورة/دقيقة؛ 1.35–1.65 كجم؛ للأماكن الضيقة')),
           ('BX-0711-01-011', 'Air belt sanders', 'صنفرة هوائية بالسير', 'PS-10330, PS-20520, PS-30540, PS-6330A, PS-10330A, PS-20520A, PS-13457A, PS-13610A, PS-25260, PS-60260, PS-100260, PS-60260A', ('Belts 6×330 to 100×260 mm; 240 W; 7000–18,000 r/min', 'سيور 6×330 إلى 100×260 مم؛ 240 واط؛ 7000–18,000 دورة/دقيقة')),
           ('BX-0711-01-015', 'Air angle grinders', 'جلاخات زاوية هوائية', 'PS-2D-1, PS-2D-1F, PS-2D-1K, PS-2D-1KL, PS-180, PS-180F, PS-180L, PS-3D-1, PS-3D-2, PS-4CH-1, PS-4CH-2', ('Discs 50, 75 / 100, 100 / 125 mm; 290–1100 W; 10,900–15,000 r/min', 'أقراص 50 و75 / 100 و100 / 125 مم؛ 290–1100 واط؛ 10,900–15,000 دورة/دقيقة')),
           ('BX-0711-01-018', 'Air die grinders', 'جلاخات هوائية للقوالب', 'PS-05-1F, PS-10-1F, PS-380, PS-480MT, PS-20H-2, PS-13-2, PS-26-20, PS-26-20F, PS-26-20L, PS-26-20LF', ('Collet 3 and 6 mm; 20,000–30,000 r/min; 0.35–1.06 kg', 'ظرف 3 و6 مم؛ 20,000–30,000 دورة/دقيقة؛ 0.35–1.06 كجم')),
           ('BX-0711-01-020', 'Air impact wrench', 'مفتاح صدم هوائي', 'PS-D800P', ('Bolts to 22 mm; 3/8 and 1/2 in square drive; 500 N·m; 1.4 kg', 'براغي حتى 22 مم؛ مربع 3/8 و1/2 بوصة؛ 500 نيوتن·م؛ 1.4 كجم')),
           ('BX-0529-01-011', 'Petrol high-pressure washers', 'غسالات ضغط عالٍ بالبنزين', 'YLHPW190, YLHTP200', ('190 and 200 bar; 9 L/min; 212 cm³ petrol engine; 30–34 kg', '190 و200 بار؛ 9 لتر/دقيقة؛ محرك بنزين 212 سم³؛ 30–34 كجم'))],
          unit=U_PRODUCT),
    table('seats', ('Operator seats and engine belt parts', 'مقاعد المشغلين وقطع سيور المحركات'), ('50–150 kg', '50–150 كجم'), SERIES,
          [('BX-0119-01-001', 'Operator seats, mechanical suspension', 'مقاعد مشغلين بتعليق ميكانيكي', 'KL02, KL02.10', ('Fore-aft travel 190 mm; 50–130 kg occupants; 70 mm suspension stroke; PVC or fabric', 'حركة أمامية خلفية 190 مم؛ لمستخدمين 50–130 كجم؛ شوط تعليق 70 مم؛ PVC أو قماش')),
           ('BX-0119-01-002', 'Heavy-duty operator seat', 'مقعد مشغل للخدمة الشاقة', 'YS15', ('Travel 176 mm; 50–130 kg; 40–110 mm stroke; options: air suspension, 360° swivel, armrest controls, heater', 'حركة 176 مم؛ 50–130 كجم؛ شوط 40–110 مم؛ خيارات: تعليق هوائي ودوران 360° وأدوات تحكم في المسند وتدفئة')),
           ('BX-0119-01-003', 'Compact machine seats', 'مقاعد للمعدات الصغيرة', 'YS2-8, KL10', ('50–120 kg occupants; stroke 40–110 mm (YS2-8) or 50 mm (KL10)', 'لمستخدمين 50–120 كجم؛ شوط 40–110 مم (YS2-8) أو 50 مم (KL10)')),
           ('BX-0119-01-006', 'Air-suspension seats with 24 V compressor', 'مقاعد بتعليق هوائي وضاغط 24 فولت', 'KL03, YJ03', ('KL03: 150 mm air stroke, 50–150 kg; YJ03: 80 mm air stroke, 50–130 kg; heater and head rest options', 'KL03: شوط هوائي 150 مم، 50–150 كجم؛ YJ03: شوط هوائي 80 مم، 50–130 كجم؛ خيارات تدفئة ومسند رأس')),
           ('BX-0119-01-008', 'Seat suspension units', 'وحدات تعليق المقاعد', 'J03, J0303, J07, J08, J11, J0301, J0308, J12', ('Mechanical and air suspension units for operator seats', 'وحدات تعليق ميكانيكية وهوائية لمقاعد المشغلين')),
           ('BX-0119-01-010', 'Operator seat belts', 'أحزمة مقاعد المشغلين', 'A01, A02, A03, A21', ('Seat belts for machine operator seats', 'أحزمة أمان لمقاعد مشغلي المعدات')),
           ('BX-0475-02-003', 'Machine engine belt tensioners', 'شدّادات سيور محركات المعدات', ('About 12 parts with OE numbers', 'نحو 12 قطعة بأرقام القطع الأصلية'), ('Backhoe, excavator and tractor engines; match by OE number on request', 'محركات الحفارات اللودرية والحفارات والجرارات؛ المطابقة برقم القطعة الأصلية عند الطلب')),
           ('BX-0475-02-004', 'Truck engine belt tensioners', 'شدّادات سيور محركات الشاحنات', ('About 10 parts with OE numbers', 'نحو 10 قطع بأرقام القطع الأصلية'), ('Heavy-truck diesel engines; match by OE number on request', 'محركات ديزل الشاحنات الثقيلة؛ المطابقة برقم القطعة الأصلية عند الطلب'))],
          unit=U_PRODUCT),
])

# p11 hydraulic hoses ---------------------------------------------------------------------------------------
F['hydraulic-hoses'] = family('hydraulic-hoses', CAT, [
    table('hoses', ('Hydraulic & air hoses', 'خراطيم الهيدروليك والهواء'), ('SAE · EN', 'SAE · EN'), SERIES,
          [('BX-0295-01-001', 'Steel-wire hydraulic hoses', 'خراطيم هيدروليك بالسلك الفولاذي', 'SAE 100 R1AT, R2AT, R12, R13, R15, R16, R17; EN 853 1SN / 2SN; EN 856 4SP / 4SH', ('Braided and spiral wire; high-pressure hydraulic lines', 'سلك مجدول وحلزوني؛ خطوط هيدروليك بضغط عالٍ')),
           ('BX-0295-01-002', 'Textile & thermoplastic hoses', 'خراطيم بالنسيج وحرارية اللدونة', 'SAE 100 R3, R4, R5, R6, R7, R8, R9, R10; EN 853 1ST / 2ST', ('Textile-reinforced lower-pressure hydraulic lines; thermoplastic types R7 / R8', 'خطوط هيدروليك مقوّاة بالنسيج بضغط أقل؛ الأنواع حرارية اللدونة R7 / R8')),
           ('BX-0295-01-003', 'Stainless & nylon hoses', 'خراطيم ستانلس ونايلون', ('Stainless metal hoses; nylon tubing to SAE J844 type B', 'خراطيم معدنية ستانلس؛ أنابيب نايلون وفق SAE J844 النوع B'), ('SAE J844 is the air-brake tubing standard', 'SAE J844 هو معيار أنابيب فرامل الهواء'))],
          unit=U_PRODUCT),
], type_label=('Product', 'المنتج'))

# p14 mobile light towers ----------------------------------------------------------------------------------
LT = [('MO-400A', ('Hand-push', 'يدوي الدفع'), 'Honda GX160K1', '2', '2 × 400 W', '72 000', '12.1', '15', '1.7–4.8'),
      ('MO-400B', ('Hand-push', 'يدوي الدفع'), 'Honda GX240K1', '2.8', '4 × 400 W', '144 000', '13', '25', '1.7–4.8'),
      ('MO-1000A', ('Hand-push', 'يدوي الدفع'), 'Honda GX270H1', '3.2', '2 × 1 kW', '220 000', '11.9', '24', '1.7–4.8'),
      ('MO-1000B', ('Hand-push', 'يدوي الدفع'), 'Honda GX390K1', '5', '4 × 1 kW', '440 000', '9', '25', '1.7–4.8'),
      ('MO-1000QA', ('Hand-push', 'يدوي الدفع'), 'Honda GX270H1', '3.2', '2 × 1 kW', '220 000', '11.9', '24', '1.7–4.8'),
      ('4VA4000', ('Trailer', 'مقطورة'), 'Kohler KD440 / Kipor 186F / Changchai 186F', '5', '4 × 1000 W', '440 000', '25', '38', '5–11'),
      ('4TN4000', ('Trailer', 'مقطورة'), 'Kubota D1105', '8', '4 × 1000 W', '440 000', '120', '170', '7–11')]
F['mobile-light-towers'] = family('mobile-light-towers', CAT, [
    table('towers', ('Mobile light towers', 'أبراج الإنارة المتنقلة'), ('72,000–440,000 lm', '72,000–440,000 لومن'),
          [C('type', 'Type', 'النوع'), C('engine', 'Engine', 'المحرك'), C('power', 'Rated power (kW)', 'القدرة المقننة (كيلوواط)'), C('lamps', 'Lamps', 'المصابيح'),
           C('lm', 'Luminous flux (lm)', 'التدفق الضوئي (لومن)'), C('runtime', 'Runtime (h)', 'مدة التشغيل (ساعة)'), C('tank', 'Fuel tank (L)', 'خزان الوقود (لتر)'), C('mast', 'Mast height (m)', 'ارتفاع الصاري (م)')],
          [(None, m, None, *v) for m, *v in LT],
          code='BX-0004-02-007', key_rows=['lm', 'runtime', 'mast']),
])

# p12 weighbridges & axle scales ---------------------------------------------------------------------------
F['weighbridges-axle-scales'] = family('weighbridges-axle-scales', CAT, [
    table('weigh', ('Weighbridges and axle scales', 'موازين الشاحنات وموازين المحاور'), ('30–120 t', '30–120 طن'), SERIES,
          [('BX-0464-01-001', 'Truck scale set, 12 mm deck', 'طقم ميزان شاحنات بمنصة 12 مم',
            ('3×7, 3×8, 3×9, 3×10, 3×12, 3×15, 3×16, 3×18, 3×20, 3×22, 3×24 m (30–120 t)', '3×7 و3×8 و3×9 و3×10 و3×12 و3×15 و3×16 و3×18 و3×20 و3×22 و3×24 م (30–120 طن)'),
            ('Complete digital set; 2–4 sections; digital indicator and 30 t digital load cells (OIML R76, CE); IP68 junction box; 50 m cable in steel conduit; base plates and fixings',
             'طقم رقمي كامل؛ 2–4 أقسام؛ مؤشر رقمي وخلايا وزن رقمية 30 طن (OIML R76، CE)؛ صندوق توصيل IP68؛ كابل 50 م في أنبوب فولاذي؛ ألواح القاعدة وأدوات التثبيت')),
           ('BX-0460-01-001', 'Truck scale', 'ميزان شاحنات', 'OP-100', ('Capacity and deck size on request', 'السعة ومقاس المنصة عند الطلب')),
           ('BX-0460-01-002', 'Axle scales & weighing pads', 'موازين ووسائد المحاور', ('OP-923; OP-928 with OP-928-C trolley', 'OP-923؛ وOP-928 مع عربة OP-928-C'),
            ('Portable axle weighing', 'وزن المحاور المحمول'))],
          unit=U_PRODUCT),
], type_label=('Product', 'المنتج'))

# p13 weighbridges, platform scales & load cells -------------------------------------------------------------
F['weighbridges-platform-scales-load-cells'] = family('weighbridges-platform-scales-load-cells', CAT, [
    table('weigh', ('Weighbridges, platform scales and load cells', 'موازين الشاحنات وموازين المنصة وخلايا الوزن'), ('1–200 t', '1–200 طن'), SERIES,
          [('BX-0462-01-001', 'Digital truck scales (weighbridges)', 'موازين شاحنات رقمية', ('30, 60, 80, 100, 120, 150, 200 t', '30 و60 و80 و100 و120 و150 و200 طن'),
            ('Deck 3–6 m wide, 4–30 m long; Q235 steel, U-beams, 8–14 mm plate; OIML R76 Class III; 10 / 20 / 50 kg division; 125% safe overload; pit or pitless; IP68',
             'منصة بعرض 3–6 م وطول 4–30 م؛ فولاذ Q235 وعوارض U ولوح 8–14 مم؛ OIML R76 الفئة III؛ تدريج 10 / 20 / 50 كجم؛ حمل زائد آمن 125%؛ في حفرة أو فوق الأرض؛ IP68')),
           ('BX-0462-01-002', 'Digital load cells', 'خلايا وزن رقمية', ('QS-D, QSA; 20, 30, 40, 50 t', 'QS-D وQSA؛ 20 و30 و40 و50 طن'),
            ('RS485; C3; ±0.02% FS; IP68; -30 to +70 °C; lightning protection; 4–10 cells per weighbridge', 'RS485؛ C3؛ ±0.02% من المدى؛ IP68؛ من -30 إلى +70 °م؛ حماية من الصواعق؛ 4–10 خلايا لكل ميزان')),
           ('BX-0464-01-003', 'Platform scales', 'موازين منصة', ('SCS 1–3 t (1×1 to 2×2 m); SCS 5 t (1.2×1.2 to 2×2 m)', 'SCS ‏1–3 طن (1×1 إلى 2×2 م)؛ SCS ‏5 طن (1.2×1.2 إلى 2×2 م)'),
            ('0.5 / 1 kg division; 5 mm checker plate, U-beams; 4 load cells; IP68 junction box; 10 m cable', 'تدريج 0.5 / 1 كجم؛ لوح مضلّع 5 مم وعوارض U؛ 4 خلايا وزن؛ صندوق توصيل IP68؛ كابل 10 م'))],
          unit=U_PRODUCT),
], type_label=('Product', 'المنتج'))
