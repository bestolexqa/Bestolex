"""Build the gold-mining section: family JSON files, product entries in data/products.json, images in
public/products/<id>/ and the family registrations, one subpage per Bestolex catalogue. Run from this folder:
    python3 build.py [BXC-02=<dir>] [BXC-03=<dir>] [BXC-04=<dir>] [BXC-05=<dir>] [BXC-07=<dir>] [BXC-08=<dir>] [BXC-09=<dir>]
Images are written only for the catalogues given (prepared cut-outs: prep_*.py); otherwise the files already in
public/ are kept and only their paths are used."""
import json, os, re, sys
from lib import iso, write
import bxc02_tables, bxc02_products, bxc03_tables, bxc03_products, bxc04_tables, bxc04_products, bxc08_tables, bxc08_products, bxc05_tables, bxc05_products, bxc09_tables, bxc09_products, bxc07_tables, bxc07_products
from bxc02_products import SERVICE_AR, SERVICE_EN

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
IMGDIRS = dict(a.split('=', 1) for a in sys.argv[1:] if '=' in a)

CATEGORY = {
    'id': 'gold-mining',
    'title': {'ar': 'تعدين الذهب', 'en': 'Gold Mining'},
    'image': '/categories/gold-mining.webp',
    'description': {
        'ar': 'معدات تعدين الذهب على مراحل خط الإنتاج: التنقيب والحفر واستخراج الخام، ثم التكسير والطحن والغسيل والتركيز والمعالجة والصهر، مع المختبر ودعم الموقع. نورّد للمشاريع في الشرق الأوسط وأفريقيا بأكواد BX وجداول موديلات من كتالوجاتنا.',
        'en': 'Gold-mining equipment along the production line: exploration, drilling and ore extraction, then crushing, grinding, washing, concentration, processing and smelting, with laboratory and site support. We supply projects in the Middle East and Africa with BX codes and model tables from our catalogues.'},
    'seo': {'title': {'ar': 'معدات تعدين الذهب: التنقيب والحفر والتكسير', 'en': 'Gold Mining Equipment: Exploration, Drilling and Crushing'},
            'description': {'ar': 'معدات تعدين الذهب من بيستوليكس: أجهزة المسح والكشف، وحفارات الاستكشاف وDTH، والضواغط، ومطارق ولقم DTH وRC ومستهلكات الحفر، والكسارات الفكية والمخروطية والصدمية والمطرقية ومحطات التكسير المتنقلة. التوريد للشرق الأوسط وأفريقيا.',
                            'en': 'Gold-mining equipment from Bestolex: survey instruments and detectors, exploration and DTH rigs, compressors, DTH and RC hammers, bits and drilling consumables, and jaw, cone, impact and hammer crushers and mobile crushing plants. Supply to the Middle East and Africa.'}},
    'subcategories': [],
}
SUBPAGES = [
    ('BXC-02', {'id': 'exploration-drilling', 'title': {'ar': 'التنقيب والحفر واستخراج الخام', 'en': 'Exploration, Drilling & Ore Extraction'}},
     bxc02_tables.F, bxc02_products.P),
    ('BXC-03', {'id': 'drilling-consumables', 'title': {'ar': 'مستهلكات الحفر', 'en': 'Drilling Consumables'}},
     bxc03_tables.F, bxc03_products.P),
    ('BXC-04', {'id': 'crushing-grinding-screening', 'title': {'ar': 'التكسير والطحن والغربلة', 'en': 'Crushing, Grinding & Screening'}},
     bxc04_tables.F, bxc04_products.P),
    ('BXC-05', {'id': 'washing-gold-concentration', 'title': {'ar': 'الغسيل وتركيز الذهب', 'en': 'Washing & Gold Concentration'}},
     bxc05_tables.F, bxc05_products.P),
    ('BXC-08', {'id': 'smelting-refining', 'title': {'ar': 'الصهر والتنقية', 'en': 'Smelting & Refining'}},
     bxc08_tables.F, bxc08_products.P),
    ('BXC-07', {'id': 'pumps-slurry-handling', 'title': {'ar': 'المضخات ونقل اللب', 'en': 'Pumps & Slurry Handling'}},
     bxc07_tables.F, bxc07_products.P),
    ('BXC-09', {'id': 'laboratory-assay', 'title': {'ar': 'المختبر والتحليل', 'en': 'Laboratory & Assay'}},
     bxc09_tables.F, bxc09_products.P),
]

def specs(rows):
    return {'ar': [{'label': a, 'value': iso(v)} for a, v, _, _ in rows], 'en': [{'label': b, 'value': w} for _, _, b, w in rows]}


def stats(rows):
    return {'ar': [{'value': iso(v), 'label': a} for v, a, _, _ in rows], 'en': [{'value': w, 'label': b} for _, _, w, b in rows]}


def faq(rows):
    return {'ar': [{'q': q, 'a': iso(a)} for q, _, a, _ in rows], 'en': [{'q': q, 'a': a} for _, q, _, a in rows]}


EXTRA = {'metal-detectors-water-well-drill-rigs': ['i-004-010'],
         # BXC-02 Ed4 has no photo of these rigs: photos from the supplier's own product pages (CAT-0098-01),
         # cut out of the factory background; Chinese stickers and the maker's name removed (sup/hw in the work dir)
         'core-rc-exploration-drill-rigs': ['hw-gl', 'hw-b30', 'hw-rc'],
         # BXC-05: the other photos on the same catalogue page
         'magnetic-reclaimers-pulleys': ['i-014-012'],
         'mobile-gold-washing-plants': ['i-015-013', 'i-015-016', 'i-015-014'],
         'sluice-boxes-gold-carpets-pans': ['i-016-019', 'i-016-020'],
         'dredgers': ['i-017-022', 'i-017-024', 'i-017-023'],
         'amphibious-dredgers-excavators': ['i-018-027', 'i-018-028'],
         # BXC-09
         'sample-crushing-pulverizing': ['i-003-001', 'i-003-002'],
         'fire-assay-furnaces-cupels': ['i-006-008'],
         'laboratory-balances-micropipettes': ['i-008-012', 'i-008-013'],
         'atomic-absorption-fluorescence-spectrometers': ['i-011-017']}
PLACEHOLDER = set()
PHOTO = {'dth-hammers-bits', 'c-series-jaw-gyratory-impact-crushers', 'refractories-quartz-glass-ceramics', 'slurry-pipes-packings-gaskets', 'ductile-iron-steel-pipes-fittings-hoses'}                         # scene photo: centre-cropped to a square, not letterboxed


def image_for(cat, pid, src, n=0):
    """Prepared cut-out → 1200×1200 WebP on white, product at 86% of the canvas."""
    from PIL import Image
    out_dir = f'{REPO}/public/products/{pid}'
    os.makedirs(out_dir, exist_ok=True)
    name = pid if n == 0 else f'{pid}-{n + 1}'
    dst = f'{out_dir}/{name}.webp'
    d = IMGDIRS.get(cat)
    if d and pid not in PLACEHOLDER:
        im = Image.open(f'{d}/{src}.png').convert('RGB')
        if pid in PHOTO:
            e = min(im.size)
            im = im.crop(((im.width - e) // 2, (im.height - e) // 2, (im.width + e) // 2, (im.height + e) // 2)).resize((1200, 1200), Image.LANCZOS)
            im.save(dst, 'WEBP', quality=84, method=6)
        else:
            s = min(1200 * 0.86 / im.width, 1200 * 0.86 / im.height, 2.2)
            im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
            c = Image.new('RGB', (1200, 1200), (255, 255, 255))
            c.paste(im, ((1200 - im.width) // 2, (1200 - im.height) // 2))
            c.save(dst, 'WEBP', quality=84, method=6)
    assert os.path.exists(dst), f'missing image {dst}'
    return f'/products/{pid}/{name}.webp'


def product(cat, p):
    pid = p['id']
    img = image_for(cat, pid, p['img'])
    imgs = [img] + [image_for(cat, pid, e, k + 1) for k, e in enumerate(EXTRA.get(pid, []))]
    return {
        'id': pid,
        'name': {'ar': p['ar'], 'en': p['en']},
        'coverImage': img,
        'description': {'ar': iso(p['desc'][0]) + '\n' + SERVICE_AR, 'en': p['desc'][1] + '\n' + SERVICE_EN},
        'features': {'ar': [iso(a) for a, _ in p['features']], 'en': [b for _, b in p['features']]},
        'featureImages': [],
        'specs': specs(p['specs']),
        'specDrawings': [],
        'images': imgs,
        'image': img,
        'cardImage': img,
        'seo': {'title': {'ar': p['seo'][0], 'en': p['seo'][1]}, 'description': {'ar': iso(p['seo'][2]), 'en': p['seo'][3]}},
        'summary': {'ar': iso(p['summary'][0]), 'en': p['summary'][1]},
        'faq': faq(p['faq']),
        'stats': stats(p['stats']),
    }


F = {}
CATEGORY['subcategories'] = []
for cat, sub, fams, prods in SUBPAGES:
    assert not set(fams) & set(F), 'family id used twice'
    F.update(fams)
    CATEGORY['subcategories'].append({**sub, 'products': [product(cat, p) for p in prods]})
P = [p for s_ in CATEGORY['subcategories'] for p in s_['products']]

# family tables
os.makedirs(f'{REPO}/server/assets/catalog/mining', exist_ok=True)
for fid, fam in F.items():
    write(f'{REPO}/server/assets/catalog/mining/{fid}.json', fam)

# products.json: add or replace the gold-mining category (kept last)
pj = f'{REPO}/data/products.json'
data = json.load(open(pj))
data = [c for c in data if c['id'] != 'gold-mining'] + [CATEGORY]
with open(pj, 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

# registrations: family files map and the ids list
api = f'{REPO}/server/api/catalog/family/[id].get.ts'
s = open(api).read()
for fid in F:
    line = f"  '{fid}': 'catalog/mining/{fid}.json'"
    if line not in s:
        s = re.sub(r"(\n)(}\n\nconst cache)", lambda m: f",\n{line}\n" + m.group(2), s, count=1)
open(api, 'w').write(s.replace("json'\n,\n", "json',\n"))
ids = f'{REPO}/utils/catalogFamilies.ts'
t = open(ids).read()
for fid in F:
    if f"'{fid}'" not in t:
        t = re.sub(r"(\n\])", f",\n  '{fid}'\\1", t, count=1)
open(ids, 'w').write(t)
print('subpages', len(SUBPAGES), 'families', len(F), 'products', len(P))
