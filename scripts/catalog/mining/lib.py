"""Helpers that turn compact Python tables into the family JSON files read by
/api/catalog/family/:id (server/assets/catalog/mining/<id>.json)."""
import json, re

LRI, PDI = '⁦', '⁩'
LATIN = re.compile(r'[A-Za-z0-9][A-Za-z0-9\s.,:;/×·+\-–≤≥<>±~°%()\'"#*]*[A-Za-z0-9°%"]|[A-Za-z0-9]')


def iso(s):
    """Wrap Latin/number runs in an Arabic string in isolates so they keep their order."""
    if not s:
        return s
    if not re.search(r'[؀-ۿ]', s):
        # Pure Latin/number values ("34–45", "60 / 120", "≤ 65") read right-to-left on Arabic pages
        # unless isolated as one LTR run.
        s = s.replace(LRI, '').replace(PDI, '')
        return f'{LRI}{s}{PDI}' if re.search(r'[0-9A-Za-z]', s) and re.search(r'[^0-9A-Za-z]', s) else s
    s = s.replace(LRI, '').replace(PDI, '')
    return LATIN.sub(lambda m: f'{LRI}{m.group(0)}{PDI}', s)


def bi(en, ar=None):
    return {'en': en, 'ar': iso(ar if ar is not None else en)}


def table(tid, label, key, cols, rows, intro=None, key_rows=None, code=None, unit=None):
    """cols: [(key, en, ar)]; rows: [(code|None, name_en, name_ar|None, v1, v2, ...)].
    A value is a str (same in both languages) or a (en, ar) tuple. unit: countUnit when the rows are
    lines, grades or groups rather than models."""
    models = []
    for r in rows:
        c, ne, na, *vals = r
        specs = {}
        for (k, _, _), v in zip(cols, vals):
            if v in (None, '', '–', '—'):
                continue
            specs[k] = bi(*v) if isinstance(v, tuple) else bi(v)
        # One table code for many models: add the model name so each column has its own id and v-for key.
        mc = c or (f'{code} / {ne}' if code and len(rows) > 1 else code)
        models.append({'code': mc, 'name': bi(ne, na or ne), 'specs': specs})
    # The page shows the count (countLabel); drop "N models · " from the key when N is the row count.
    ke, ka = key
    m = re.match(rf'^{len(rows)} [^·]+?(?: · |$)', ke) if len(rows) > 1 else None
    if m:
        ke = ke[m.end():]
        ka = re.sub(rf'^{len(rows)} [^·]+?(?: · |$)', '', ka)
    t = {'id': tid, 'label': bi(*label), 'models': models}
    if ke:
        t['key'] = bi(ke, ka)
    if unit:
        t['countUnit'] = unit
    if intro:
        t['intro'] = bi(*intro)
    if key_rows:
        t['keyRows'] = key_rows
    t['_cols'] = cols
    return t


def family(fid, catalogue, types, type_label=('Product line', 'خط المنتج'), unit=None):
    rows, seen = [], set()
    for t in types:
        for k, en, ar in t.pop('_cols'):
            if k not in seen:
                seen.add(k)
                rows.append({'key': k, 'label': bi(en, ar)})
    out = {
        'id': fid,
        'updated': '2026-11-27',
        'title': {'ar': 'المنتجات والمواصفات', 'en': 'Products and specifications'},
        'source': {'ar': iso(f'المصدر: كتالوج بيستوليكس {catalogue} · المواصفات من المصنّعين وقد تتغير دون إشعار'),
                   'en': f'Source: Bestolex catalogue {catalogue} · specifications come from the manufacturers and may change without notice'},
        'typeLabel': bi(*type_label),
        'missing': {'ar': '—', 'en': '—'},
        'rows': rows,
        'keyRows': [r['key'] for r in rows[:3]],
        'types': types,
    }
    if unit:
        out['countUnit'] = unit
    return out


def write(path, obj):
    with open(path, 'w') as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write('\n')
