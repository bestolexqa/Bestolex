"""Image designer for Bestolex blog articles.

Builds the article cover (1200x630, brand colours, Arabic + English title, product photo, logo)
and inline product figures, saved as WebP under public/blog/ so every image is hosted by
Bestolex (never hot-linked from a supplier site).

Product photos are fetched through the live site's image optimiser
(https://www.bestolex.com/_vercel/image), one request at a time with a pause: parallel
requests made the optimiser lose its connection to sabtech.com.sa for ~10 minutes on
20 Nov 2026.

    python3 tools/blog/images.py cover server/assets/blog/<slug>.json --product scissors-lift [--photo-index 0]
    python3 tools/blog/images.py figure <slug> <product-id> [--photo-index 1] [--n 1] \
        --alt-ar "..." --alt-en "..."      # prints the <figure> HTML for ar and en

Requires google-chrome (headless) and Pillow. Fonts are in tools/blog/fonts (OFL).
"""
from __future__ import annotations

import argparse
import html
import io
import json
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.parse
import urllib.request
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from catalog import Catalog  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
FONTS = Path(__file__).resolve().parent / 'fonts'
OUT_DIR = ROOT / 'public' / 'blog'
LOGO_ON_DARK = ROOT / 'public' / 'logo-dark-transparent.png'
SITE = 'https://www.bestolex.com'

GOLD, BLACK, SLATE = '#E99E05', '#191919', '#6F7070'


def product_photos(cat: Catalog, pid: str) -> list[str]:
    p = cat.get(pid)
    urls = []
    for key in ('coverImage', 'image', 'cardImage'):
        if isinstance(p.get(key), str):
            urls.append(p[key])
    for item in p.get('images') or []:
        if isinstance(item, str):
            urls.append(item)
        elif isinstance(item, dict) and item.get('image'):
            urls.append(item['image'])
    seen, out = set(), []
    for u in urls:
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out


ALLOWED_WIDTHS = (320, 640, 768, 1024, 1280, 1536)  # widths the site's optimiser accepts (q=80)


def fetch_photo(url: str, width: int = 1280) -> Image.Image:
    width = min(ALLOWED_WIDTHS, key=lambda w: abs(w - width))
    if url.startswith('/'):
        local = ROOT / 'public' / url.lstrip('/')
        if local.exists():
            return Image.open(local).convert('RGB')
        url = SITE + url
    proxied = f"{SITE}/_vercel/image?url={urllib.parse.quote(url, safe='')}&w={width}&q=80"
    last = None
    for attempt in range(4):
        try:
            req = urllib.request.Request(proxied, headers={'User-Agent': 'bestolex-blog-images', 'Accept': 'image/webp,image/*'})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            time.sleep(1.0)
            return Image.open(io.BytesIO(data)).convert('RGB')
        except Exception as e:  # one at a time, back off before retrying
            last = e
            time.sleep(5 * (attempt + 1))
    raise RuntimeError(f'could not fetch {url}: {last}')


def font_face() -> str:
    faces = [
        ('Cairo', 'cairo-arabic-800-normal.woff2', 800, 'U+0600-06FF, U+0750-077F, U+08A0-08FF, U+FB50-FDFF, U+FE70-FEFF'),
        ('Cairo', 'cairo-arabic-600-normal.woff2', 600, 'U+0600-06FF, U+0750-077F, U+08A0-08FF, U+FB50-FDFF, U+FE70-FEFF'),
        ('Cairo', 'cairo-latin-800-normal.woff2', 800, 'U+0000-00FF'),
        ('Cairo', 'cairo-latin-600-normal.woff2', 600, 'U+0000-00FF'),
        ('Poppins', 'poppins-latin-700-normal.woff2', 700, 'U+0000-00FF, U+2013-2014'),
        ('Poppins', 'poppins-latin-600-normal.woff2', 600, 'U+0000-00FF, U+2013-2014'),
        ('Poppins', 'poppins-latin-400-normal.woff2', 400, 'U+0000-00FF, U+2013-2014'),
    ]
    return '\n'.join(
        f"@font-face{{font-family:'{f}';src:url('{(FONTS / file).as_uri()}') format('woff2');font-weight:{w};unicode-range:{r};}}"
        for f, file, w, r in faces
    )


def render_html(page: str, width: int, height: int) -> Image.Image:
    chrome = shutil.which('google-chrome') or shutil.which('chromium') or shutil.which('chromium-browser')
    if not chrome:
        raise RuntimeError('google-chrome is required')
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / 'page.html'
        out = Path(tmp) / 'shot.png'
        src.write_text(page, encoding='utf-8')
        cmd = [chrome, '--headless=new', '--disable-gpu', '--no-sandbox', '--hide-scrollbars',
               '--force-device-scale-factor=1', f'--window-size={width},{height}',
               '--virtual-time-budget=4000', f'--screenshot={out}', src.as_uri()]
        subprocess.run(cmd, check=True, capture_output=True, timeout=120)
        img = Image.open(out).convert('RGB')
        if img.size != (width, height):
            img = img.crop((0, 0, width, height))
        return img


def cover(article_path: Path, pid: str, photo_index: int = 0) -> Path:
    cat = Catalog()
    a = json.loads(article_path.read_text(encoding='utf-8'))
    slug = a['id']
    photos = product_photos(cat, pid)
    if not photos:
        raise RuntimeError(f'no photo for {pid}')
    photo = fetch_photo(photos[min(photo_index, len(photos) - 1)])
    with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as f:
        photo.save(f.name, quality=92)
        photo_uri = Path(f.name).as_uri()
    title_ar = html.escape(a['title']['ar'])
    title_en = html.escape(a['title']['en'])
    cat_label = html.escape(f"{a['category']['ar']}  ·  {a['category']['en']}")
    page = f"""<!doctype html><html><head><meta charset="utf-8"><style>
{font_face()}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1200px;height:630px;overflow:hidden;background:{BLACK}}}
.stage{{position:relative;width:1200px;height:630px;background:{BLACK};overflow:hidden}}
.shard1{{position:absolute;left:-120px;top:-60px;width:520px;height:760px;background:{GOLD};transform:skewX(-14deg);opacity:.95}}
.shard2{{position:absolute;left:330px;top:-60px;width:26px;height:760px;background:{SLATE};transform:skewX(-14deg)}}
.photo{{position:absolute;left:44px;top:58px;width:450px;height:450px;background:#fff;border-radius:28px;
  box-shadow:0 24px 60px rgba(0,0,0,.45);display:flex;align-items:center;justify-content:center;overflow:hidden}}
.photo img{{max-width:92%;max-height:92%;object-fit:contain}}
.text{{position:absolute;right:52px;top:56px;width:600px;height:450px;display:flex;flex-direction:column;justify-content:center;gap:18px}}
.chip{{align-self:flex-end;background:{GOLD};color:{BLACK};font:600 20px 'Cairo','Poppins',sans-serif;padding:6px 18px;border-radius:999px;direction:rtl}}
.ar{{direction:rtl;text-align:right;color:#fff;font:800 50px/1.32 'Cairo',sans-serif}}
.en{{direction:ltr;text-align:right;color:#d6d6d6;font:600 25px/1.35 'Poppins',sans-serif}}
.bar{{position:absolute;left:0;right:0;bottom:0;height:86px;background:#111;border-top:3px solid {GOLD};
  display:flex;align-items:center;justify-content:space-between;padding:0 44px}}
.site{{color:{GOLD};font:600 22px 'Poppins',sans-serif;letter-spacing:.5px}}
.logo{{height:64px}}
</style></head><body><div class="stage">
<div class="shard1"></div><div class="shard2"></div>
<div class="photo"><img src="{photo_uri}"></div>
<div class="text"><div class="chip">{cat_label}</div><div class="ar" id="ar">{title_ar}</div><div class="en" id="en">{title_en}</div></div>
<div class="bar"><div class="site">www.bestolex.com</div><img class="logo" src="{LOGO_ON_DARK.as_uri()}"></div>
</div>
<script>
function fit(id,max,min){{var el=document.getElementById(id),s=max;el.style.fontSize=s+'px';
while((el.scrollHeight>el.clientHeight+2||el.getBoundingClientRect().height>(id=='ar'?250:110))&&s>min){{s-=2;el.style.fontSize=s+'px';}}}}
document.fonts.ready.then(function(){{fit('ar',52,30);fit('en',26,17);}});
</script></body></html>"""
    img = render_html(page, 1200, 630)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / f'{slug}.webp'
    img.save(out, 'WEBP', quality=82, method=6)
    return out


def figure(slug: str, pid: str, photo_index: int, n: int, alt_ar: str, alt_en: str) -> dict:
    cat = Catalog()
    photos = product_photos(cat, pid)
    if not photos:
        raise RuntimeError(f'no photo for {pid}')
    photo = fetch_photo(photos[min(photo_index, len(photos) - 1)], width=1280)
    # Landscape canvas (1200x750) with the photo contained and centred on white, so figures
    # never dominate the article column.
    photo.thumbnail((1120, 680))
    canvas = Image.new('RGB', (1200, 750), 'white')
    canvas.paste(photo, ((1200 - photo.width) // 2, (750 - photo.height) // 2))
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / f'{slug}-{n}.webp'
    canvas.save(out, 'WEBP', quality=80, method=6)
    src = f'/blog/{out.name}'
    w, h = canvas.size
    return {
        'path': str(out),
        'ar': f'<figure><img src="{src}" alt="{html.escape(alt_ar)}" width="{w}" height="{h}" loading="lazy"><figcaption>{html.escape(alt_ar)}</figcaption></figure>',
        'en': f'<figure><img src="{src}" alt="{html.escape(alt_en)}" width="{w}" height="{h}" loading="lazy"><figcaption>{html.escape(alt_en)}</figcaption></figure>',
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    c = sub.add_parser('cover')
    c.add_argument('article')
    c.add_argument('--product', required=True)
    c.add_argument('--photo-index', type=int, default=0)
    f = sub.add_parser('figure')
    f.add_argument('slug')
    f.add_argument('product')
    f.add_argument('--photo-index', type=int, default=1)
    f.add_argument('--n', type=int, default=1)
    f.add_argument('--alt-ar', required=True)
    f.add_argument('--alt-en', required=True)
    sub.add_parser('photos').add_argument('product')
    args = ap.parse_args()
    if args.cmd == 'cover':
        print(cover(Path(args.article), args.product, args.photo_index))
    elif args.cmd == 'figure':
        print(json.dumps(figure(args.slug, args.product, args.photo_index, args.n, args.alt_ar, args.alt_en), ensure_ascii=False, indent=2))
    elif args.cmd == 'photos':
        for i, u in enumerate(product_photos(Catalog(), args.product)):
            print(i, u)
    return 0


if __name__ == '__main__':
    sys.exit(main())
