import sys, re, html
p = sys.argv[1]
s = open(p, encoding='utf-8', errors='replace').read()
s = re.sub(r'(?is)<script.*?</script>', ' ', s)
s = re.sub(r'(?is)<style.*?</style>', ' ', s)
s = re.sub(r'(?is)<svg.*?</svg>', ' [svg] ', s)
# capture alt texts and hrefs separately
s = re.sub(r'(?i)<img[^>]*?alt="([^"]*)"[^>]*>', r' [IMG alt=\1] ', s)
s = re.sub(r'(?i)<img[^>]*>', ' [IMG no-alt] ', s)
s = re.sub(r'(?i)<a [^>]*href="([^"]*)"[^>]*>', r' [LINK \1 | ', s)
s = re.sub(r'(?i)</a>', '] ', s)
s = re.sub(r'(?i)<(h1|h2|h3|h4|li|tr|p|div|section|br|td|th|button|label|input|select|option|textarea|form)\b[^>]*>', r'\n<\1> ', s)
s = re.sub(r'(?s)<[^>]+>', ' ', s)
s = html.unescape(s)
s = re.sub(r'[ \t]+', ' ', s)
s = re.sub(r'\n\s*\n+', '\n', s)
print(s.strip())
