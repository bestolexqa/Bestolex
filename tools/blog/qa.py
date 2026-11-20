"""Bestolex article checker: the automatic gate every article passes before it is published.

Checks one or more article files (server/assets/blog/<slug>.json) against the content rules
of the project (official name, glossary, claims policy, prices, brands, phone order), SEO
(title/description length, headings, keyword placement, internal links, tables, FAQ, alt
text), structure (fields, images on disk, product ids), duplication against the live blog,
and figures that do not appear in the catalog of the products the article discusses.

    python3 tools/blog/qa.py server/assets/blog/my-article.json [more.json ...]
    python3 tools/blog/qa.py --all            # every article file
    python3 tools/blog/qa.py --json FILE      # machine-readable report

Exit code 0 = no errors (warnings may remain), 1 = errors. Errors block publishing; warnings
are for the reviewer to confirm or fix. Every finding names the language and the rule.
"""
from __future__ import annotations

import difflib
import html as htmllib
import json
import re
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from catalog import Catalog  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
ARTICLES_DIR = ROOT / 'server' / 'assets' / 'blog'
PUBLIC = ROOT / 'public'
LIVE_CACHE = Path('/tmp/bestolex-live-articles.json')

CATEGORIES = {
    'أنظمة التحميل والمستودعات': 'Loading & Warehouse Systems',
    'النفايات وإعادة التدوير': 'Waste & Recycling',
    'الحماية المحيطية': 'Perimeter Protection',
    'الأبواب الصناعية': 'Industrial Doors',
    'المعدات الثقيلة': 'Heavy Equipment',
}

ALLOWED_BRANDS = {'sab tech', 'sabtech', 'inkema', 'beringer', 'garsite'}
OTHER_BRANDS = [
    'hörmann', 'hormann', 'assa abloy', 'crawford', 'stertil', 'efaflex', 'rite-hite', 'nordock', 'kelley',
    'blue giant', 'genie', 'jlg', 'skyjack', 'haulotte', 'gradeall', 'dutco', 'stebilex', 'orwak', 'bramidan',
    'strautmann', 'harmony', 'marathon', 'wastequip', 'mil-tek', 'avermann', 'presona', 'macpresse',
    'heald', 'frontier pitts', 'atg access', 'gunnebo', 'boon edam', 'came', 'faac', 'nice ', 'bft ',
    'dormakaba', 'hikvision', 'dahua', 'uveye', 'comm port', 'gatekeeper',
]

ALLOWED_EXTERNAL = (
    'bsigroup.com', 'iso.org', 'astm.org', 'gov.qa', 'mme.gov.qa', 'moi.gov.qa', 'mm.gov.qa',
    'km.qa', 'kahramaa.qa', 'qcs', 'wa.me/97451505014', 'tel:+97451505014', 'mailto:info@bestolex.com',
)


def strip_html(s: str) -> str:
    s = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', s or '', flags=re.S | re.I)
    s = re.sub(r'<br\s*/?>|</(p|li|h\d|tr|div|td|th)>', '\n', s, flags=re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'[ \t]+', ' ', htmllib.unescape(s)).strip()


def words(s: str) -> list[str]:
    return re.findall(r'[\w؀-ۿ]+', s)


def sentences(text: str) -> list[str]:
    return [x.strip() for x in re.split(r'(?<=[.!؟?])\s+|\n+', text) if x.strip()]


def load_live_articles() -> list[dict]:
    if LIVE_CACHE.exists() and (datetime.now().timestamp() - LIVE_CACHE.stat().st_mtime) < 6 * 3600:
        return json.loads(LIVE_CACHE.read_text(encoding='utf-8'))
    try:
        req = urllib.request.Request('https://www.bestolex.com/api/blog', headers={'User-Agent': 'bestolex-qa'})
        with urllib.request.urlopen(req, timeout=60) as r:
            data = json.loads(r.read().decode('utf-8'))
        LIVE_CACHE.write_text(json.dumps(data, ensure_ascii=False), encoding='utf-8')
        return data
    except Exception as e:  # network may be unavailable; duplication check is then skipped
        print(f'(note) live articles not loaded: {e}', file=sys.stderr)
        return []


class Report:
    def __init__(self, path: Path):
        self.path = path
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.stats: dict = {}

    def err(self, msg: str):
        self.errors.append(msg)

    def warn(self, msg: str):
        self.warnings.append(msg)


def check_article(path: Path, cat: Catalog, live: list[dict], others: list[dict]) -> Report:
    rep = Report(path)
    try:
        a = json.loads(path.read_text(encoding='utf-8'))
    except Exception as e:
        rep.err(f'file: not valid JSON ({e})')
        return rep

    # ---------- structure ----------
    slug = a.get('id') or ''
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', slug):
        rep.err('structure: id must be a short lowercase English slug with hyphens')
    if path.stem != slug:
        rep.err(f'structure: file name {path.name} must match id "{slug}"')
    if a.get('slug') not in (None, slug):
        rep.err('structure: slug must equal id')
    for field in ('title', 'seoTitle', 'desc', 'category', 'content', 'imageAlt', 'readTime'):
        val = a.get(field)
        if not isinstance(val, dict) or not str(val.get('ar') or '').strip() or not str(val.get('en') or '').strip():
            rep.err(f'structure: {field} needs both ar and en')
    for field in ('date', 'publishAt', 'image'):
        if not a.get(field):
            rep.err(f'structure: {field} is missing')
    if a.get('date') and not re.fullmatch(r'\d{4}-\d{2}-\d{2}', a['date']):
        rep.err('structure: date must be YYYY-MM-DD')
    if a.get('publishAt'):
        try:
            pub = datetime.fromisoformat(a['publishAt'])
            if a.get('date') and pub.date().isoformat() != a['date']:
                rep.err('structure: date must be the day of publishAt')
        except ValueError:
            rep.err('structure: publishAt must be ISO 8601 with offset, e.g. 2026-11-22T07:00:00+03:00')
    cat_ar = (a.get('category') or {}).get('ar')
    if cat_ar not in CATEGORIES:
        rep.err(f'structure: category.ar must be one of {list(CATEGORIES)}')
    elif (a.get('category') or {}).get('en') != CATEGORIES[cat_ar]:
        rep.err(f'structure: category.en must be "{CATEGORIES[cat_ar]}"')
    img = a.get('image') or ''
    if not img.startswith('/blog/') or not (PUBLIC / img.lstrip('/')).exists():
        rep.err(f'images: cover {img or "(none)"} must be a file under public/blog/')
    kw = a.get('keyword') or {}
    if not kw.get('en') or not kw.get('ar'):
        rep.err('structure: keyword.ar and keyword.en (target search terms) are required')
    if not kw.get('source'):
        rep.warn('seo: keyword.source should name where the volume came from (e.g. Semrush qa, date)')

    pids = [p.get('id') for p in (a.get('relatedProducts') or []) if isinstance(p, dict)]
    if not pids:
        rep.err('structure: relatedProducts must list at least one product discussed')
    for pid in pids:
        if pid not in cat.products:
            rep.err(f'structure: relatedProducts has unknown product id "{pid}"')

    faq = a.get('faq') or []
    if not (4 <= len(faq) <= 6):
        rep.err(f'seo: faq must have 4–6 questions (has {len(faq)})')
    for i, item in enumerate(faq, 1):
        for lang in ('ar', 'en'):
            if not (item.get('q') or {}).get(lang) or not (item.get('a') or {}).get(lang):
                rep.err(f'structure: faq #{i} needs q and a in {lang}')

    # ---------- per language ----------
    full_text_all = ''
    for lang in ('ar', 'en'):
        L = lang.upper()
        content = (a.get('content') or {}).get(lang) or ''
        text = strip_html(content)
        faq_text = ' '.join(((f.get('q') or {}).get(lang, '') + ' ' + (f.get('a') or {}).get(lang, '')) for f in faq)
        all_text = '\n'.join([((a.get('title') or {}).get(lang) or ''), ((a.get('desc') or {}).get(lang) or ''), text, faq_text])
        full_text_all += '\n' + all_text
        n_words = len(words(text))
        rep.stats[f'words_{lang}'] = n_words
        if n_words < 800:
            rep.err(f'{L} length: {n_words} words; at least 800 are required (aim for 1,000–1,800)')
        elif n_words < 1000:
            rep.warn(f'{L} length: {n_words} words; 1,000–1,800 reads as a complete guide')

        seo_title = (a.get('seoTitle') or {}).get(lang) or ''
        if len(seo_title) > 60:
            rep.err(f'{L} seo: seoTitle is {len(seo_title)} characters (max 60)')
        desc = (a.get('desc') or {}).get(lang) or ''
        if not (110 <= len(desc) <= 160):
            rep.err(f'{L} seo: desc is {len(desc)} characters (keep 120–155)')
        elif not (120 <= len(desc) <= 155):
            rep.warn(f'{L} seo: desc is {len(desc)} characters (best 120–155)')

        if re.search(r'<h1[\s>]', content, re.I):
            rep.err(f'{L} headings: no <h1> inside content (the page title is the only H1)')
        h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', content, re.I | re.S)
        if len(h2s) < 3:
            rep.err(f'{L} headings: {len(h2s)} <h2> sections; at least 3 needed')
        if re.search(r'<h[45][\s>]', content, re.I):
            rep.warn(f'{L} headings: prefer h2/h3 only')

        k = (kw.get(lang) or '').lower()
        if k:
            first100 = ' '.join(words(text)[:100]).lower()
            core = [w for w in words(k) if len(w) > 2]
            if core and not all(w in first100 for w in core):
                rep.warn(f'{L} seo: target keyword "{kw.get(lang)}" not in the first 100 words')
            if core and not any(all(w in strip_html(h).lower() for w in core) for h in h2s):
                rep.warn(f'{L} seo: target keyword "{kw.get(lang)}" not in any <h2>')
            if core and not all(w in seo_title.lower() for w in core):
                rep.warn(f'{L} seo: seoTitle does not contain the target keyword')

        tables = len(re.findall(r'<table[\s>]', content, re.I))
        rep.stats[f'tables_{lang}'] = tables
        if tables < 1:
            rep.err(f'{L} tables: at least one comparison or specification table is required')
        if tables and content.count('class="table-wrap"') < tables:
            rep.warn(f'{L} tables: wrap every <table> in <div class="table-wrap"> for mobile scrolling')
        if not re.search(r'class="key-takeaways"', content):
            rep.warn(f'{L} structure: add a short "key takeaways" box (<div class="key-takeaways">) near the top')

        # links
        links = re.findall(r'<a\s[^>]*href="([^"]+)"', content, re.I)
        internal = [l for l in links if l.startswith('/')]
        prefix_ok = (lambda l: not l.startswith('/en/')) if lang == 'ar' else (lambda l: l.startswith('/en/') or l == '/en')
        if len(internal) < 3:
            rep.err(f'{L} links: {len(internal)} internal links; 3–5 needed (products, category, related posts)')
        for l in internal:
            if not prefix_ok(l):
                rep.err(f'{L} links: {l} points to the other language')
            m = re.match(r'^(?:/en)?/products/([^/#?]+)$', l)
            if m and m.group(1) not in cat.products:
                rep.err(f'{L} links: product {m.group(1)} does not exist')
        if not any(re.search(r'/products/', l) for l in internal):
            rep.err(f'{L} links: link at least one product page')
        for l in links:
            if l.startswith('http') and not any(d in l for d in ALLOWED_EXTERNAL):
                rep.err(f'{L} links: external link {l} is not on the allowed list (standards bodies, Qatar government)')
            if 'sabtech.com' in l:
                rep.err(f'{L} links: no links to SAB TECH pages')

        # images inside content
        for src in re.findall(r'<img\s[^>]*src="([^"]+)"', content, re.I):
            if not src.startswith('/blog/') or not (PUBLIC / src.lstrip('/')).exists():
                rep.err(f'{L} images: {src} must be a file under public/blog/')
        for tag in re.findall(r'<img\s[^>]*>', content, re.I):
            if not re.search(r'alt="[^"]{5,}"', tag):
                rep.err(f'{L} images: every image needs descriptive alt text')

        # Qatar angle and call to action
        if lang == 'ar' and not re.search(r'قطر|الدوحة', text):
            rep.err('AR local: mention Qatar/Doha in the body')
        if lang == 'en' and not re.search(r'Qatar|Doha', text):
            rep.err('EN local: mention Qatar/Doha in the body')
        if not re.search(r'wa\.me/97451505014|/contact|عرض سعر|quotation|quote', content, re.I):
            rep.err(f'{L} cta: end with a quote request (link to /contact or WhatsApp 51505014)')

        # ---------- content rules ----------
        low = all_text.lower()
        rules_err = [
            (r'للتجارة\s+والمقاولات|trading\s+(?:and|&)\s+contracting', 'wrong company name (للتجارة والمقاولات)'),
            (r'bestolex\s+for\s+trading|heavy\s+machinery\s+and\s+equipment', 'wrong English company name'),
            (r'مفرقع', 'glossary: use «مفجر إطارات»'),
            (r'مصد(?:ّ)?ة', 'glossary: use «مصد طريق» (not مصدة)'),
            (r'منصة\s+تحميل\s*[–-]?\s*(?:هيدروليكي|دوك)', 'glossary: dock leveler is «رصيف تحميل»'),
            (r'اختراق\s+صفري|zero\s+penetration|crash[-\s]?tested|تم\s+اختباره\s+وفق', 'claims: crash/penetration claims need a certificate'),
            (r'\b(?:P1|M50|M40|M30|K12|K8|K4)\b', 'claims: crash rating codes need a certificate for a named model'),
            (r'(?:\d[\d,.]*\s*(?:ريال|ر\.ق|qar|qr\b|\$|usd|دولار|درهم|aed))|(?:(?:qar|qr|\$|usd)\s*\d)', 'prices are not allowed without approval'),
            (r'الأفضل\s+في\s+قطر|الرائد[ةه]|الأول\s+في\s+قطر|best\s+in\s+qatar|\bthe\s+leading\b|\bleading\s+(?:supplier|company|provider|brand|distributor)|number\s+one|no\.\s*1|\bpremier\b|market\s+leader', 'unverifiable superlative'),
            (r'60\s*(?:hz|هرتز)|220\s*/\s*380', 'electrical supply 60 Hz / 220-380 V is not confirmed for Qatar (task 33)'),
            (r'\[يحتاج تأكيد|\btodo\b|lorem|image prompt|data-placeholder|\[n\d+\]|as an ai|كنموذج ذكاء', 'placeholder or AI leftover in text'),
        ]
        for pattern, msg in rules_err:
            m = re.search(pattern, all_text, re.I)
            if m:
                rep.err(f'{L} rules: {msg} (found "{m.group(0)}")')
        for b in OTHER_BRANDS:
            if re.search(r'(?<![\w])' + re.escape(b.strip()) + r'(?![\w])', low):
                rep.err(f'{L} rules: brand "{b.strip()}" is not SAB TECH (needs approval)')

        for s in sentences(all_text):
            sl = s.lower()
            mentions_sabtech = bool(re.search(r'ساب\s*تك|sab\s*tech|sabtech|المصنّع|المصنع|manufacturer', sl))
            if re.search(r'\biso\s*9001|\biso\b', sl) and not mentions_sabtech:
                rep.err(f'{L} claims: ISO is SAB TECH\'s certificate; name SAB TECH in the same sentence: "{s[:90]}"')
            if re.search(r'علامة\s*ce|\bce\s*mark|\bce\b\s*(?:certified|marking)', sl) and not mentions_sabtech:
                rep.err(f'{L} claims: CE marking belongs to SAB TECH products; say so: "{s[:90]}"')
            if re.search(r'25\s*\+|\+\s*25|25\s*(?:عام|سنة|عاماً|years)', sl) and not mentions_sabtech:
                rep.err(f'{L} claims: 25+ years is SAB TECH\'s experience, not Bestolex\'s: "{s[:90]}"')
            if re.search(r'pas\s*68|iwa\s*14|astm\s*f\s*2656|hcis', sl):
                rep.warn(f'{L} claims: standard named; allowed only to explain the standard, never as a product rating: "{s[:90]}"')
            if re.search(r'(?:خدمات|ورشة|ورش|إصلاح)\s+(?:الأنظمة\s+|المعدات\s+)?(?:ال)?هيدروليك|hydraulic\s+(?:services|repairs?|workshop)', sl) and not re.search(r'شريك|partner', sl):
                rep.warn(f'{L} positioning: hydraulic services are on request through a technical partner: "{s[:90]}"')

        phones = re.findall(r'(?:\+?974\s*)?(5150\s*5014|51505014|5070\s*8833|50708833)', all_text)
        norm = [p.replace(' ', '') for p in phones]
        if norm and norm[0] != '51505014':
            rep.err(f'{L} rules: the primary number +974 51505014 must come first')

    # ---------- figures vs catalog ----------
    if pids:
        known = cat.numbers(pids)
        text_numbers = set()
        for lang in ('ar', 'en'):
            body = strip_html((a.get('content') or {}).get(lang) or '')
            for m in re.finditer(r'(\d+(?:[.,]\d+)?)\s*(طن|tons?|t\b|كجم|kg|ملم|مم|mm|متر|m\b|كيلوواط|kw|حصان|hp|م/ث|m/s|ثانية|seconds?|cm|سم|%)', body, re.I):
                n = m.group(1).replace(',', '')
                if n not in known and n not in {'1', '2', '3', '4', '5', '10', '100'}:
                    text_numbers.add(f'{m.group(1)} {m.group(2)}')
        if text_numbers:
            rep.warn('figures: not found in the catalog of the related products; confirm each or remove: ' + ', '.join(sorted(text_numbers)))

    # ---------- duplication ----------
    title_ar = (a.get('title') or {}).get('ar') or ''
    body_ar = ' '.join(words(strip_html((a.get('content') or {}).get('ar') or ''))[:400])
    for other in live + others:
        if (other.get('id') or other.get('slug')) == slug:
            continue
        ot = (other.get('title') or {}).get('ar') if isinstance(other.get('title'), dict) else str(other.get('title') or '')
        r_title = difflib.SequenceMatcher(None, title_ar, ot or '').ratio()
        if r_title > 0.75:
            rep.err(f'duplication: title too close to existing "{ot[:70]}" ({r_title:.2f})')
        elif r_title > 0.6:
            rep.warn(f'duplication: title similar to "{ot[:70]}" ({r_title:.2f}); make the angle distinct')
        oc = other.get('content')
        ob = strip_html(oc.get('ar') if isinstance(oc, dict) else str(oc or ''))
        if ob and body_ar:
            ob400 = ' '.join(words(ob)[:400])
            sa, sb = set(body_ar.split()), set(ob400.split())
            jac = len(sa & sb) / max(1, len(sa | sb))
            if jac > 0.5:
                rep.err(f'duplication: opening text overlaps {jac:.0%} with "{(ot or "")[:70]}"')
    return rep


def main(argv: list[str]) -> int:
    as_json = '--json' in argv
    argv = [x for x in argv if x != '--json']
    if '--all' in argv:
        files = sorted(ARTICLES_DIR.glob('*.json'))
    else:
        files = [Path(x) for x in argv]
    if not files:
        print(__doc__)
        return 2
    cat = Catalog()
    live = load_live_articles()
    all_repo = []
    for f in ARTICLES_DIR.glob('*.json'):
        try:
            all_repo.append(json.loads(f.read_text(encoding='utf-8')))
        except Exception:
            pass
    reports = []
    for f in files:
        others = [x for x in all_repo if x.get('id') != f.stem]
        reports.append(check_article(f, cat, live, others))
    if as_json:
        print(json.dumps([{'file': str(r.path), 'errors': r.errors, 'warnings': r.warnings, 'stats': r.stats} for r in reports], ensure_ascii=False, indent=2))
    else:
        for r in reports:
            status = 'PASS' if not r.errors else 'FAIL'
            print(f'\n== {status}: {r.path.name}  {r.stats}')
            for e in r.errors:
                print(f'  ERROR   {e}')
            for w in r.warnings:
                print(f'  warning {w}')
    return 1 if any(r.errors for r in reports) else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
