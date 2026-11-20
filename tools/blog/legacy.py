"""Copy a live dashboard article into the repo so it can be corrected under its original URL.

    python3 tools/blog/legacy.py export <article-id> <file-stem>   # writes server/assets/blog/<file-stem>.json
    python3 tools/blog/legacy.py list                              # live articles: index, id, words, title

A repo file with the same id replaces the dashboard (Bunny) version on every public reader
(/api/blog, /api/blog/[id], sitemap, llms.txt), so the article keeps its URL. The export applies
only safe mechanical fixes; everything else is edited by hand and then checked with qa.py:

- category normalised to the five fixed blog categories;
- glossary: مفرقع → مفجر, مصدة → مصد, «منصة تحميل – دوك ليفيلر» → رصيف تحميل;
- «ساب تكـ» → «ساب تك»;
- links to sabtech.com.sa removed (product links become the matching Bestolex product page);
- markup cleaned to article tags only (comments, inline styles, data-/js attributes, spans,
  divs, copy buttons and <pre> diagrams from editors and AI tools removed); h1 → h2, h4 → h3.

The file gets "legacy": true, keeps date and cover, and adds updatedAt and empty seoTitle,
imageAlt, faq, relatedProducts and keyword fields to fill in.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from html import escape
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa import ARTICLES_DIR, CATEGORIES, load_live_articles, strip_html, words  # noqa: E402

CATEGORY_MAP = {
    'النفايات وإعادة التدوير': 'النفايات وإعادة التدوير',
    'المخلفات والتدوير': 'النفايات وإعادة التدوير',
    'انظمة التحميل': 'أنظمة التحميل والمستودعات',
    'أنظمة حديثة وموثوقة التحميل': 'أنظمة التحميل والمستودعات',
    'أنظمة حماية المحيط الأمنية': 'الحماية المحيطية',
    'الابواب الصناعية': 'الأبواب الصناعية',
    'الات ومعدات ثقيله': 'المعدات الثقيلة',
    'النظم الهيدروليكية المتقدمة': 'المعدات الثقيلة',
    'الصيانة الشاملة والدعم الفني': 'المعدات الثقيلة',
    'الصيانة دورية متقدمة والدعم الفني': 'المعدات الثقيلة',
}

# SAB TECH product slugs → Bestolex product ids
SABTECH_PRODUCTS = {
    'horizontal-baling-press-70t': 'horizontal-plastic-baler-70',
    'vertical-baling-press-20t': 'cardboard-plastic-baler-200',
    'vertical-baling-press-50t': 'cardboard-plastic-baler-500',
    'vertical-pet-baling-press-80t': 'can-bottle-baler-80',
    'textile-baler': 'textile-baler',
    'solar-bin-waste-compactor': 'solar-bin-waste-compactor',
}


KEEP_TAGS = {'p', 'h2', 'h3', 'ul', 'ol', 'li', 'strong', 'em', 'a', 'table', 'thead', 'tbody', 'tr', 'th',
             'td', 'br', 'blockquote', 'small', 'figure', 'figcaption', 'img'}
RENAME = {'h1': 'h2', 'h4': 'h3', 'h5': 'h3', 'h6': 'h3', 'b': 'strong', 'i': 'em'}
DROP_WITH_CONTENT = {'script', 'style', 'button', 'svg', 'pre', 'noscript', 'template'}
KEEP_ATTRS = {'a': ('href',), 'img': ('src', 'alt', 'width', 'height', 'loading'), 'td': ('colspan', 'rowspan'),
              'th': ('colspan', 'rowspan')}
VOID = {'br', 'img', 'hr'}


class Sanitizer(HTMLParser):
    """Keep article markup only: drops editor/AI-tool junk (comments, inline styles, data-*,
    js* attributes, spans and divs, copy buttons, ASCII diagrams in <pre>)."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out: list[str] = []
        self.skip = 0
        self.stack: dict[str, list] = {'div': [], 'span': []}

    def handle_starttag(self, tag, attrs):
        # Text pasted from Google AI Mode marks headings, paragraphs and bold text with classes
        # on <div>/<span> instead of tags: map them back before the allow-list is applied.
        if tag in ('div', 'span') and not self.skip:
            d = dict(attrs)
            cls = d.get('class') or ''
            mapped = None
            if tag == 'div' and (d.get('role') == 'heading' or 'otQkpb' in cls):
                mapped = 'h2'
            elif tag == 'div' and 'n6owBd' in cls:
                mapped = 'p'
            elif tag == 'span' and 'rQesXe' in cls:
                mapped = 'strong'
            self.stack[tag].append(mapped)
            if mapped:
                self.out.append(f'<{mapped}>')
            return
        tag = RENAME.get(tag, tag)
        if tag in DROP_WITH_CONTENT:
            if tag not in VOID:
                self.skip += 1
            return
        if self.skip or tag not in KEEP_TAGS:
            return
        keep = KEEP_ATTRS.get(tag, ())
        a = ''.join(f' {k}="{escape(v or "", quote=True)}"' for k, v in attrs if k in keep and v)
        self.out.append(f'<{tag}{a}>')

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag):
        if tag in ('div', 'span') and not self.skip:
            mapped = self.stack[tag].pop() if self.stack[tag] else None
            if mapped:
                self.out.append(f'</{mapped}>')
            return
        tag = RENAME.get(tag, tag)
        if tag in DROP_WITH_CONTENT:
            self.skip = max(0, self.skip - 1)
            return
        if self.skip or tag not in KEEP_TAGS or tag in VOID:
            return
        self.out.append(f'</{tag}>')

    def handle_data(self, data):
        if not self.skip:
            self.out.append(escape(data.replace('\xa0', ' '), quote=False))


def sanitize(html: str) -> str:
    ai_mode = 'n6owBd' in (html or '')
    p = Sanitizer()
    p.feed(re.sub(r'<!--.*?-->', '', html or '', flags=re.S))
    p.close()
    s = ''.join(p.out)
    s = re.sub(r'[ \t\r\f\v]+', ' ', s)
    s = re.sub(r'\s*\n\s*', '\n', s)
    for _ in range(3):
        s = re.sub(r'<(p|li|strong|em|h2|h3|small|a)>\s*</\1>', '', s)
    s = re.sub(r'\s*(</?(?:p|h2|h3|ul|ol|li|table|thead|tbody|tr|th|td|blockquote|figure|figcaption)>)\s*', r'\1', s)
    # "<p>Heading?<br>Paragraph…</p>" (AI Mode) → heading + paragraph
    def split_heading(m):
        head, rest = m.group(1).strip(), m.group(2).strip()
        plain = re.sub(r'<[^>]+>', '', head)
        if len(plain) <= 110 and not re.search(r'[.:،,؛;]$', plain):
            return f'<h2>{plain}</h2><p>{rest}</p>'
        return m.group(0)
    if ai_mode:
        s = re.sub(r'<p>((?:(?!</p>|<br>).)+?)<br>(.+?)</p>', split_heading, s, flags=re.S)
    # a short line on its own with no closing punctuation, followed by a list or paragraph → heading
    def short_heading(m):
        plain = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        if len(plain) <= 75 and len(plain.split()) <= 12 and not re.search(r'[.:،,؛;!]$', plain):
            return f'<h2>{plain}</h2>'
        return m.group(0)
    if ai_mode:
        s = re.sub(r'<p>((?:(?!</p>).){3,120}?)</p>(?=\s*<(?:ul|ol|p|h2))', short_heading, s, flags=re.S)
    # sections written as <h3> with no <h2> at all → promote them to <h2>
    if '<h2>' not in s and '<h3>' in s:
        s = s.replace('<h3>', '<h2>').replace('</h3>', '</h2>')
    s = re.sub(r'(</(?:p|h2|h3|ul|ol|table|blockquote|figure)>)', r'\1\n', s)
    return s.strip()


def fix_text(html: str, lang: str) -> str:
    s = sanitize(html)
    s = s.replace('ساب تكـ', 'ساب تك')
    s = re.sub(r'مفرقعات', 'مفجرات', s)
    s = re.sub(r'مفرقع', 'مفجر', s)
    s = re.sub(r'(ال)?مصد(?:ّ)?ة\b', lambda m: (m.group(1) or '') + 'مصد', s)
    s = re.sub(r'منصة\s+تحميل\s*[–-]?\s*دوك\s*ليفيلر', 'رصيف تحميل', s)

    def sab(m):
        href, text = m.group(1), m.group(2)
        pm = re.search(r'/product/([^/?#"]+)', href)
        if pm and pm.group(1) in SABTECH_PRODUCTS:
            prefix = '/en' if lang == 'en' else ''
            return f'<a href="{prefix}/products/{SABTECH_PRODUCTS[pm.group(1)]}">{text}</a>'
        return text
    s = re.sub(r'<a\s[^>]*href="(https?://[^"]*sabtech[^"]*)"[^>]*>(.*?)</a>', sab, s, flags=re.I | re.S)
    return s


def export(article_id: str, stem: str) -> Path:
    live = load_live_articles()
    a = next((x for x in live if x.get('id') == article_id or x.get('slug') == article_id), None)
    if not a:
        sys.exit(f'not found in the live blog: {article_id}')
    cat_ar = CATEGORY_MAP.get(((a.get('category') or {}).get('ar') or '').strip(), ((a.get('category') or {}).get('ar') or '').strip())
    if cat_ar not in CATEGORIES:
        sys.exit(f'unknown category {cat_ar!r}; add it to CATEGORY_MAP')
    out = {
        'id': a['id'],
        'slug': a.get('slug') or a['id'],
        'legacy': True,
        'title': a['title'],
        'seoTitle': {'ar': '', 'en': ''},
        'desc': a['desc'],
        'category': {'ar': cat_ar, 'en': CATEGORIES[cat_ar]},
        'date': a.get('date'),
        'updatedAt': date.today().isoformat(),
        'readTime': a.get('readTime'),
        'image': a.get('image'),
        'imageAlt': {'ar': '', 'en': ''},
        'is_featured': a.get('is_featured', False),
        'keyword': {'ar': '', 'en': '', 'source': ''},
        'content': {lang: fix_text((a.get('content') or {}).get(lang) or '', lang) for lang in ('ar', 'en')},
        'faq': [],
        'relatedProducts': [],
        'review': {'notes': []},
    }
    path = ARTICLES_DIR / f'{stem}.json'
    path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return path


def main(argv):
    if argv[:1] == ['list']:
        for i, a in enumerate(load_live_articles()):
            print(i, a['id'][:60], len(words(strip_html((a.get('content') or {}).get('ar') or ''))), (a.get('title') or {}).get('ar', '')[:60])
        return 0
    if len(argv) == 3 and argv[0] == 'export':
        print(export(argv[1], argv[2]))
        return 0
    print(__doc__)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
