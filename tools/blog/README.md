# Daily product articles for bestolex.com

Two bilingual (Arabic + English) product articles are published every Sunday–Thursday.
Each article is a JSON file in `server/assets/blog/<slug>.json`, with its images in
`public/blog/`. A file merged into `main` and deployed to production appears on the site,
in the sitemap and in `/llms.txt` once its `publishAt` time has passed. Preview deployments
show scheduled articles early.

The user approved this pipeline on 20 Nov 2026: articles are written, checked by the QA
script, reviewed and corrected by an independent reviewer, and then published without a
manual approval step. If the reviewer cannot clear an article, it is not published that day.

## Tools

| Tool | What it does |
| --- | --- |
| `catalog.py` | Product lookup; spec tables and side-by-side comparison tables from `data/products.json`; `relatedProducts` entries. Supply voltage/frequency rows are withheld until confirmed for Qatar. |
| `images.py` | Branded cover (1200×630 WebP, Arabic + English title, product photo, logo) and inline product figures, saved under `public/blog/`. Fetches photos one at a time through the site's image optimiser. |
| `qa.py` | Automatic gate: structure, SEO, glossary, claims policy, prices, brands, phone order, links, images, tables, FAQ, duplication with the live blog, and figures not found in the catalog. Exit 1 = errors. |
| `topics.json` | Backlog of topics with target keyword (Semrush, Qatar), products, planned tables and live posts the new angle must not repeat. |

## Article file

```json
{
  "id": "scissor-lift-table-guide-qatar",
  "slug": "scissor-lift-table-guide-qatar",
  "publishAt": "2026-11-22T07:00:00+03:00",
  "date": "2026-11-22",
  "updatedAt": "2026-11-22",
  "category": { "ar": "أنظمة التحميل والمستودعات", "en": "Loading & Warehouse Systems" },
  "title": { "ar": "…", "en": "…" },
  "seoTitle": { "ar": "≤ 60 characters, keyword first, «| بيستوليكس» if it fits", "en": "≤ 60 characters" },
  "desc": { "ar": "120–155 characters, a full sentence with a benefit and a call", "en": "120–155 characters" },
  "keyword": { "ar": "رافعة مقصية", "en": "scissor lift", "volume": 590, "kd": 26, "source": "Semrush qa, 2026-11-16" },
  "image": "/blog/scissor-lift-table-guide-qatar.webp",
  "imageAlt": { "ar": "…", "en": "…" },
  "readTime": { "ar": "7 دقائق قراءة", "en": "7 min read" },
  "content": { "ar": "<div class=\"key-takeaways\">…</div><h2>…</h2>…", "en": "…" },
  "faq": [ { "q": { "ar": "…", "en": "…" }, "a": { "ar": "…", "en": "…" } } ],
  "relatedProducts": [ { "id": "scissors-lift", "name": { "ar": "…", "en": "…" }, "image": "…" } ],
  "reviewer": null,
  "review": { "qa": "PASS", "reviewedAt": "…", "notes": ["…"] }
}
```

- `id` = file name = short lowercase English slug with hyphens.
- `category` is one of the five fixed names in `qa.py` (`CATEGORIES`).
- `reviewer` stays `null` until the user names a technical reviewer; the page then shows
  "مراجعة فنية: …".
- `faq` (4–6 items) is rendered under the article and as FAQPage structured data, so do not
  repeat the FAQ inside `content`.
- `relatedProducts` comes from `python3 tools/blog/catalog.py related <ids…>`; the page shows
  each product with a WhatsApp quote button (+974 51505014).

## Content HTML conventions

- No `<h1>` (the page title is the H1). At least three `<h2>` sections; `<h3>` inside them.
- Open with a short intro, then `<div class="key-takeaways"><strong>باختصار</strong><ul>…</ul></div>`
  (`In short` in English).
- Tables from `catalog.py` (spec and comparison) plus at least one decision/selection table
  written for the reader; every table inside `<div class="table-wrap">`. Add a
  one-line source under catalog tables: «المصدر: كتالوج المنتج المعتمد لدى بيستوليكس».
- 3–5 internal links with descriptive anchor text: product pages (`/products/<id>`), the
  category page (`/products/category/<id>`), one or two related live posts. English content
  uses `/en/...` links. External links only to standards bodies or Qatar government sites.
- Images: inline figures from `images.py figure` (`/blog/<slug>-<n>.webp`) with alt text.
- Qatar angle: mention Qatar/Doha and the local context that the catalog supports (site
  survey, installation, after-sales in Qatar, the heat and dust only where the spec supports
  it, e.g. an operating temperature range).
- Close with the service stages that apply (survey → solution → supply → installation →
  testing → training → maintenance → spare parts) and a call:
  «اطلب معاينة أو عرض سعر» → `/contact` and `https://wa.me/97451505014`.
- English is written for a B2B reader in Qatar, not translated word for word, and targets the
  English keyword.

## Facts and claims (from the skill `bestolex-content-writer`)

- Figures only from `data/products.json` (via `catalog.py`) or the approved catalogs. Anything
  else is left out — never guessed. `qa.py` lists numbers that are not in the catalog.
- 25+ years, ISO 9001, CE marking belong to SAB TECH (the manufacturer), never to Bestolex.
- PAS 68 / IWA 14-1 / ASTM F2656: explain the standard only; no rating for any product.
- No prices or discounts. No suppliers or brands other than SAB TECH; Inkema, Beringer and
  Garsite may appear because they are on the site already.
- Glossary: مفجر إطارات، مصد طريق، رصيف تحميل. Official name: بيستوليكس لتجارة الآلات والمعدات
  الثقيلة (ذ.م.م) / Bestolex Trading of Heavy Equipment and Machinery W.L.L.
- Phone: +974 51505014 first. Hydraulic services only "on request through a technical partner".
- No supply voltage or frequency (pending confirmation for Qatar's 50 Hz grid).
- Door products are blocked until their specifications are reconciled (handoff task 38).

## Daily procedure (scheduled task)

1. Read `bestolex-website-handoff.md` (Claude project) and this file. Pull `main`.
2. Take the first two `planned` topics without `blockedBy` from `topics.json`. Re-check each
   keyword in Semrush (database `qa`; `phrase_this`/`phrase_related`) and adjust the target if
   a closer term has demand. Read the live posts named in `avoidOverlapWith`.
3. Write both languages per article (1,000–1,800 words each), with tables from `catalog.py`.
4. Images: `python3 tools/blog/images.py cover server/assets/blog/<slug>.json --product <id>`
   and one or two `figure` images. Look at each image before using it.
5. `python3 tools/blog/qa.py server/assets/blog/<slug>.json` until there are no errors.
6. Independent review: a separate agent that has not seen the drafting reads both files with
   the reviewer checklist below, fixes what it can in place, and returns PASS or FAIL with
   notes. Run `qa.py` again after its edits.
7. Branch `content/<date>`, commit articles + images + `topics.json` (status `published`,
   `publishedAt`, `file`), open a PR, deploy a preview, open both language pages on the
   preview (`web_fetch_vercel_url`), then merge and deploy production.
8. Log the day in the content log doc and the monitoring log; update the handoff only for
   decisions or problems.

## Reviewer checklist

1. Every number in text and tables matches `data/products.json` for the named product.
2. No claim outside the claims policy; no superlatives; no prices; no foreign brands.
3. The article answers the reader's decision with a clear recommendation by case, not
   generic praise; the Qatar angle is concrete.
4. Arabic reads naturally (no literal translation), glossary terms used, no typos; English
   reads as native B2B copy.
5. Titles: `title` informative, `seoTitle` ≤ 60 with the keyword, `desc` 120–155.
6. Headings form a logical outline; key-takeaways box matches the body.
7. Tables render as intended and each has a reason to exist.
8. Internal links point to the right product/category pages in the same language.
9. FAQ answers are short, factual and not copied from the body.
10. Not a rewrite of a live post (compare with the posts named in the topic).
