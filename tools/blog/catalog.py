"""Catalog helpers for blog articles: product lookup, spec tables and comparison tables.

All figures come from data/products.json (the approved catalog on the site), so tables in
articles never carry numbers typed by hand. Electrical supply rows are left out until the
supply for Qatar (50 Hz) is confirmed with SAB TECH (handoff task 33).

Usage from Python:
    from catalog import Catalog
    cat = Catalog()
    html = cat.spec_table('scissors-lift', 'ar')
    html = cat.compare_table(['cardboard-plastic-baler-200', 'horizontal-plastic-baler-70'], 'en')

Command line (prints HTML):
    python3 tools/blog/catalog.py spec scissors-lift ar
    python3 tools/blog/catalog.py compare ar cardboard-plastic-baler-200 horizontal-plastic-baler-70
    python3 tools/blog/catalog.py related scissors-lift movable-scissors-lifts   # JSON for relatedProducts
    python3 tools/blog/catalog.py list                                          # ids and names
"""
from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRODUCTS = ROOT / 'data' / 'products.json'

# Rows withheld from articles until confirmed (supply voltage/frequency for Qatar).
EXCLUDED_LABEL = re.compile(r'(كهرب|التغذية|الجهد|الفولت|مصدر الطاقة|مصدر التيار|electric|power supply|voltage|supply)', re.I)

MOTOR_LABEL = re.compile(r'(محرك|موتور|منفاخ|قدرة|قوة|motor|blower)', re.I)
SUPPLY_VALUE = re.compile(r'(\d{2,3}\s*/\s*\d{2,3}\s*V|\b\d0\s*Hz|هرتز)', re.I)

HEAD = {
    'ar': {'spec': 'المواصفة', 'value': 'القيمة', 'source': 'المصدر: كتالوج المنتج المعتمد لدى بيستوليكس'},
    'en': {'spec': 'Specification', 'value': 'Value', 'source': 'Source: Bestolex approved product catalogue'},
}


# Glossary fixes applied to catalog text shown in articles (the catalog still has some old terms).
GLOSSARY_AR = [('المصدّة', 'المصد'), ('المصدة', 'المصد'), ('مصدّة', 'مصد'), ('مصدة', 'مصد'), ('مفرقع', 'مفجر'),
               ('قطر العمود (المصد)', 'قطر العمود')]


def glossary(text: str, lang: str) -> str:
    if lang == 'ar':
        for old, new in GLOSSARY_AR:
            text = text.replace(old, new)
    return text


def _norm(label: str) -> str:
    return re.sub(r'[^\w]+', ' ', label.lower()).strip()


class Catalog:
    def __init__(self, path: Path = PRODUCTS):
        self.categories = json.loads(Path(path).read_text(encoding='utf-8'))
        self.products: dict[str, dict] = {}
        self.category_of: dict[str, dict] = {}
        for cat in self.categories:
            for p in cat.get('products', []):
                self.products[p['id']] = p
                self.category_of[p['id']] = cat

    def get(self, pid: str) -> dict:
        if pid not in self.products:
            raise KeyError(f'unknown product id: {pid}')
        return self.products[pid]

    def name(self, pid: str, lang: str) -> str:
        return glossary(self.get(pid)['name'][lang], lang)

    def value(self, pid: str, lang: str, *labels: str) -> str:
        """Value of the first matching spec label (case-insensitive substring), or '—'."""
        rows = self.spec_rows(pid, lang)
        for want in labels:
            for label, val in rows:
                if want.lower() in label.lower():
                    return val
        return '—'

    def url(self, pid: str, lang: str) -> str:
        return f"/products/{pid}" if lang == 'ar' else f"/en/products/{pid}"

    def category_url(self, pid: str, lang: str) -> str:
        cid = self.category_of[pid]['id']
        return f"/products/category/{cid}" if lang == 'ar' else f"/en/products/category/{cid}"

    def image(self, pid: str) -> str | None:
        p = self.get(pid)
        for key in ('cardImage', 'image', 'coverImage'):
            if p.get(key):
                return p[key]
        imgs = p.get('images') or []
        return imgs[0] if imgs and isinstance(imgs[0], str) else None

    def spec_rows(self, pid: str, lang: str) -> list[tuple[str, str]]:
        specs = (self.get(pid).get('specs') or {}).get(lang) or []
        rows = []
        for row in specs:
            label = glossary(str(row.get('label', '')).strip(), lang)
            value = glossary(str(row.get('value', '')).strip(), lang)
            is_supply = EXCLUDED_LABEL.search(label) and not MOTOR_LABEL.search(label)
            if label and value and not is_supply and not SUPPLY_VALUE.search(value):
                rows.append((label, value))
        return rows

    def spec_table(self, pid: str, lang: str, caption: str | None = None) -> str:
        h = HEAD[lang]
        rows = ''.join(
            f'<tr><td>{html.escape(l)}</td><td>{html.escape(v)}</td></tr>' for l, v in self.spec_rows(pid, lang)
        )
        cap = f'<caption>{html.escape(caption)}</caption>' if caption else ''
        return (
            f'<div class="table-wrap"><table>{cap}<thead><tr><th>{h["spec"]}</th><th>{h["value"]}</th></tr></thead>'
            f'<tbody>{rows}</tbody></table></div>'
        )

    def compare_table(self, pids: list[str], lang: str, labels: list[str] | None = None) -> str:
        """Side-by-side table. Rows are matched by label text; a missing value shows as —.

        `labels` (optional) limits and orders the rows, matched case-insensitively against
        each product's own labels in that language.
        """
        h = HEAD[lang]
        per = [dict((_norm(l), (l, v)) for l, v in self.spec_rows(pid, lang)) for pid in pids]
        if labels:
            order = [_norm(l) for l in labels]
        else:
            order = []
            for rows in per:
                for key in rows:
                    if key not in order:
                        order.append(key)
        head = ''.join(f'<th>{html.escape(self.name(pid, lang))}</th>' for pid in pids)
        body = ''
        for key in order:
            shown = next((rows[key][0] for rows in per if key in rows), key)
            cells = ''.join(f'<td>{html.escape(rows[key][1]) if key in rows else "—"}</td>' for rows in per)
            if any(key in rows for rows in per):
                body += f'<tr><td><strong>{html.escape(shown)}</strong></td>{cells}</tr>'
        return (
            f'<div class="table-wrap"><table><thead><tr><th>{h["spec"]}</th>{head}</tr></thead>'
            f'<tbody>{body}</tbody></table></div>'
        )

    def related(self, pids: list[str]) -> list[dict]:
        """Entries for the article's relatedProducts field (cards with a quote button)."""
        out = []
        for pid in pids:
            p = self.get(pid)
            out.append({'id': pid, 'name': {'ar': p['name']['ar'], 'en': p['name']['en']}, 'image': self.image(pid)})
        return out

    def numbers(self, pids: list[str]) -> set[str]:
        """Every number that appears in the products' specs, descriptions and features."""
        text = ''
        for pid in pids:
            text += json.dumps(self.get(pid), ensure_ascii=False)
        return set(n.replace(',', '') for n in re.findall(r'\d+(?:[.,]\d+)?', text))


def main(argv: list[str]) -> int:
    cat = Catalog()
    if not argv or argv[0] == 'list':
        for c in cat.categories:
            print(f"# {c['id']} – {c['title']['ar']} / {c['title']['en']}")
            for p in c['products']:
                print(f"  {p['id']}: {p['name']['ar']} / {p['name']['en']} (brand: {p.get('brand') or '-'})")
        return 0
    cmd = argv[0]
    if cmd == 'spec':
        print(cat.spec_table(argv[1], argv[2]))
    elif cmd == 'compare':
        print(cat.compare_table(argv[2:], argv[1]))
    elif cmd == 'related':
        print(json.dumps(cat.related(argv[1:]), ensure_ascii=False, indent=2))
    elif cmd == 'show':
        print(json.dumps(cat.get(argv[1]), ensure_ascii=False, indent=2))
    else:
        print(__doc__)
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
