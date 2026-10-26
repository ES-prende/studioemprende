"""Auditoría on-page de las páginas NO indexadas de web/ (título, meta, H1, jerarquía, alt, JSON-LD, palabras, keyword)."""
import html, json, os, re, collections, sys
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
A = set(open(os.path.join(R, "seo/anexo-a-indexadas.txt")).read().split())
kw = {}
for l in open(os.path.join(R, "seo/keywords.txt")):
    if l.strip() and not l.startswith("#"):
        u, k = l.strip().split("|")[:2]; kw[u] = k
sm = [l.strip() for l in open(os.path.join(R, "seo/sitemap-actual.txt")) if l.strip()]
def f(u):
    p = u.strip("/"); return os.path.join(R, "web", "index.html" if not p else (p + "/index.html" if u.endswith("/") else p + ".html"))
txt = lambda h: html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>|<style.*?</style>", " ", h, flags=re.S)))).strip()
norm = lambda s: re.sub(r"[^a-z0-9ñ ]", "", s.lower().translate(str.maketrans("áéíóúü", "aeiouu")))
issues = collections.defaultdict(list); titles = collections.Counter(); metas = collections.Counter(); filas = []
for u in sm:
    if u in A or not os.path.exists(f(u)): continue
    h = open(f(u), encoding="utf-8").read()
    if 'content="noindex' in h: continue
    can = (re.search(r'rel="canonical" href="([^"]*)"', h) or [0, ""])[1]
    if can != "https://studioemprende.com" + u: continue
    t = html.unescape((re.search(r"<title>(.*?)</title>", h) or [0, ""])[1]); d = html.unescape((re.search(r'name="description" content="([^"]*)"', h) or [0, ""])[1])
    titles[t] += 1; metas[d] += 1
    main = re.search(r"<main.*?</main>", h, re.S).group(0); mt = txt(main)
    h1 = re.findall(r"<h1[^>]*>(.*?)</h1>", main, re.S)
    if len(t) > 60 or len(t) < 25: issues["título fuera de 25-60"].append((u, len(t)))
    if t.endswith("…"): issues["título truncado con …"].append(u)
    if not 110 <= len(d) <= 160: issues["meta fuera de 110-160"].append((u, len(d)))
    if len(h1) != 1: issues["H1 distinto de 1"].append((u, len(h1)))
    hs = [int(x) for x in re.findall(r"<h([1-6])\b", main)]
    if any(b - a > 1 for a, b in zip(hs, hs[1:])): issues["salto de encabezado"].append(u)
    for im in re.findall(r"<img\b[^>]*>", main):
        if 'alt="' not in im: issues["imagen sin alt"].append(u)
        if "width=" not in im or "height=" not in im: issues["imagen sin width/height"].append(u)
    for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
        try: json.loads(m)
        except Exception: issues["JSON-LD inválido"].append(u)
    np = len(mt.split())
    if np < 600: issues["menos de 600 palabras"].append((u, np))
    k = kw.get(u, "")
    if k:
        toks = [w for w in norm(k).split() if len(w) > 3]
        prim = norm(" ".join(mt.split()[:120]))
        if toks and sum(w in prim for w in toks) / len(toks) < 0.5: issues["keyword poco presente en las primeras 120 palabras"].append((u, k))
        if toks and sum(w in norm(t) for w in toks) / len(toks) < 0.5: issues["keyword poco presente en el título"].append((u, k, t))
    filas.append(u)
for t, c in titles.items():
    if c > 1: issues["título duplicado"].append((t, c))
for d, c in metas.items():
    if c > 1: issues["meta duplicada"].append((d[:60], c))
print("Páginas auditadas:", len(filas))
for k, v in sorted(issues.items(), key=lambda kv: -len(kv[1])):
    print("%-55s %d" % (k, len(v)))
    for x in v[:int(sys.argv[1]) if len(sys.argv) > 1 else 4]: print("     ", x)
