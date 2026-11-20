"""Check the blog metadata files in server/blog-meta/ before they are merged.

    python3 tools/blog/meta_check.py            # exit code 1 if any ERROR

redirects.json  merged articles: old id -> id of the article it was merged into (301 on the site)
overrides.json  category, SEO title and description for dashboard (Bunny) articles

Rules:
- a redirect target exists (a repo file or a live article) and is not itself redirected (no chains);
- a redirected article is not also a repo file (delete the file instead) and has no override;
- an override is for a live dashboard article, not a repo file (repo files carry their own metadata);
- category is one of the five fixed blog categories, in both languages;
- seoTitle 20–60 characters and desc 120–155 characters, in both languages;
- the text follows the content rules (company name, glossary, claims, superlatives, prices).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa import ARTICLES_DIR, CATEGORIES, OTHER_BRANDS, ROOT, load_live_articles  # noqa: E402

META = ROOT / 'server' / 'blog-meta'

TEXT_RULES = [
    (r'للتجارة\s+والمقاولات|trading\s+(?:and|&)\s+contracting', 'wrong company name'),
    (r'مفرقع', 'glossary: use «مفجر إطارات»'),
    (r'مصد(?:ّ)?ة', 'glossary: use «مصد طريق» (not مصدة)'),
    (r'منصة\s+تحميل\s*[–-]?\s*(?:هيدروليكي|دوك)', 'glossary: dock leveler is «رصيف تحميل»'),
    (r'اختراق\s+صفري|zero\s+penetration|crash[-\s]?tested|pas\s*68|iwa\s*14|astm|\b(?:P1|M50|K12)\b', 'crash claims belong in the article with a certificate, not in metadata'),
    (r'\biso\b|\bce\b|25\s*\+|\+\s*25', 'ISO / CE / 25+ years are SAB TECH claims; keep them out of metadata'),
    (r'الأفضل|الرائد[ةه]|الأول\s+في|best\s+in|\bleading\b|number\s+one|\bpremier\b', 'unverifiable superlative'),
    (r'\d[\d,.]*\s*(?:ريال|ر\.ق|qar|qr\b|\$|usd|دولار)|(?:qar|qr|\$|usd)\s*\d', 'prices are not allowed'),
    (r'60\s*(?:hz|هرتز)|220\s*/\s*380', 'electrical supply not confirmed for Qatar'),
]


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    redirects = json.loads((META / 'redirects.json').read_text(encoding='utf-8')).get('redirects', [])
    overrides = json.loads((META / 'overrides.json').read_text(encoding='utf-8')).get('articles', {})

    repo_ids = set()
    for f in ARTICLES_DIR.glob('*.json'):
        a = json.loads(f.read_text(encoding='utf-8'))
        repo_ids.update(x for x in (a.get('id'), a.get('slug')) if x)
    live = load_live_articles()
    live_ids = {a.get('id') for a in live if isinstance(a, dict)} | {a.get('slug') for a in live if isinstance(a, dict)}
    live_ids.discard(None)
    dashboard_ids = {a.get('id') for a in live if isinstance(a, dict) and a.get('source') != 'repo'}
    if not live:
        warnings.append('live articles not loaded: existence of ids not checked against the site')

    froms = [str(r.get('from')) for r in redirects]
    from_set = set(froms)
    if len(froms) != len(from_set):
        errors.append('redirects: the same article is redirected twice')
    for r in redirects:
        src, dst = str(r.get('from') or ''), str(r.get('to') or '')
        tag = f'redirect {src[:40]} -> {dst[:40]}'
        if not src or not dst:
            errors.append(f'{tag}: from and to are required')
            continue
        if src == dst:
            errors.append(f'{tag}: redirects to itself')
        if dst in from_set:
            errors.append(f'{tag}: target is itself redirected (chain)')
        if src in repo_ids:
            errors.append(f'{tag}: source is a repo file; delete the file instead of redirecting it')
        if dst not in repo_ids and live and dst not in live_ids:
            errors.append(f'{tag}: target is neither a repo file nor a live article')
        if live and src not in live_ids:
            warnings.append(f'{tag}: source not in the live list (fine once this redirect is deployed)')
        if src in overrides:
            errors.append(f'{tag}: a redirected article must not have an override')
        if not r.get('reason'):
            warnings.append(f'{tag}: add a reason')

    for aid, o in overrides.items():
        tag = f'override {aid[:50]}'
        if aid in repo_ids:
            errors.append(f'{tag}: repo articles carry their own metadata; edit the file instead')
        if live and aid not in dashboard_ids:
            errors.append(f'{tag}: not a live dashboard article')
        cat = o.get('category')
        if cat:
            if cat.get('ar') not in CATEGORIES or cat.get('en') != CATEGORIES.get(cat.get('ar')):
                errors.append(f'{tag}: category must be one of {list(CATEGORIES.items())}')
        for field, lo, hi in (('seoTitle', 20, 60), ('desc', 120, 155)):
            val = o.get(field)
            if val is None:
                continue
            for lang in ('ar', 'en'):
                s = (val.get(lang) or '').strip()
                if not lo <= len(s) <= hi:
                    errors.append(f'{tag}: {field}.{lang} is {len(s)} characters (keep {lo}–{hi})')
                if lang == 'en' and re.search(r'[؀-ۿ]', s):
                    errors.append(f'{tag}: {field}.en contains Arabic')
                if lang == 'ar' and not re.search(r'[؀-ۿ]', s):
                    errors.append(f'{tag}: {field}.ar is not Arabic')
                for pattern, msg in TEXT_RULES:
                    m = re.search(pattern, s, re.I)
                    if m:
                        errors.append(f'{tag}: {field}.{lang}: {msg} (found "{m.group(0)}")')
                low = s.lower()
                for b in OTHER_BRANDS:
                    if re.search(r'(?<![\w])' + re.escape(b.strip()) + r'(?![\w])', low):
                        errors.append(f'{tag}: {field}.{lang}: brand "{b.strip()}" is not SAB TECH')
        titles = [((o.get('seoTitle') or {}).get('ar') or '').strip()]
        if titles[0] and sum(1 for x in overrides.values() if ((x.get('seoTitle') or {}).get('ar') or '').strip() == titles[0]) > 1:
            errors.append(f'{tag}: the same Arabic seoTitle is used twice')

    print(f'redirects: {len(redirects)}  overrides: {len(overrides)}  repo files: {len(repo_ids)}  live: {len(live)}')
    for w in warnings:
        print('  WARN  ', w)
    for e in errors:
        print('  ERROR ', e)
    print('== PASS' if not errors else f'== FAIL ({len(errors)} errors)')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
