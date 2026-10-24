"""Mide las páginas de la web construida (web/) para la priorización SEO.

Uso: python3 seo/scripts/medir.py  (desde la raíz del repo)
Genera seo/medidas.json con una entrada por URL del sitemap.
"""
import html, json, os, re, sys
from collections import defaultdict

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WEB = os.path.join(RAIZ, "web")
SEO = os.path.join(RAIZ, "seo")


def archivo(url):
    p = url.strip("/")
    if p == "":
        return os.path.join(WEB, "index.html")
    if url.endswith("/"):
        return os.path.join(WEB, p, "index.html")
    return os.path.join(WEB, p + ".html")


def url_de_archivo(f):
    r = os.path.relpath(f, WEB).replace(os.sep, "/")
    if r == "index.html":
        return "/"
    if r.endswith("/index.html"):
        return "/" + r[: -len("index.html")]
    return "/" + r[:-5]


def texto(h):
    h = re.sub(r"<script.*?</script>|<style.*?</style>", " ", h, flags=re.S)
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h))).strip()


def main_html(h):
    m = re.search(r"<main[^>]*>(.*)</main>", h, re.S)
    return m.group(1) if m else h


def normaliza_href(href, origen):
    href = href.split("#")[0].split("?")[0]
    if not href or href.startswith(("http", "mailto:", "tel:", "javascript:")):
        if href.startswith("https://studioemprende.com"):
            href = href[len("https://studioemprende.com"):] or "/"
        else:
            return None
    if not href.startswith("/"):
        base = origen if origen.endswith("/") else origen.rsplit("/", 1)[0] + "/"
        href = os.path.normpath(base + href).replace(os.sep, "/")
        if href.endswith(("/.", "/")) or href == ".":
            href = href.rstrip(".")
    href = re.sub(r"\.html$", "", href)
    href = re.sub(r"/index$", "/", href)
    return href or "/"


def shingles(t, n=5):
    w = re.findall(r"\w+", t.lower())
    return {" ".join(w[i:i + n]) for i in range(max(0, len(w) - n + 1))}


urls = [l.strip() for l in open(os.path.join(SEO, "sitemap-actual.txt")) if l.strip()]
todas = []
for d, _, fs in os.walk(WEB):
    for f in fs:
        if f.endswith(".html"):
            todas.append(os.path.join(d, f))

entrantes_main = defaultdict(set)
entrantes_total = defaultdict(set)
paginas = {}
for f in todas:
    u = url_de_archivo(f)
    h = open(f, encoding="utf-8").read()
    mh = main_html(h)
    for href in re.findall(r'<a [^>]*href="([^"]+)"', h):
        dst = normaliza_href(html.unescape(href), u)
        if dst and dst != u:
            entrantes_total[dst].add(u)
    for href in re.findall(r'<a [^>]*href="([^"]+)"', mh):
        dst = normaliza_href(html.unescape(href), u)
        if dst and dst != u:
            entrantes_main[dst].add(u)
    paginas[u] = h

res = {}
sh = {}
for u in urls:
    h = paginas.get(u)
    if h is None:
        res[u] = {"existe": False}
        continue
    mh = main_html(h)
    t = texto(mh)
    g = lambda pat: (re.search(pat, h, re.S) or [None, ""])[1]
    faq = len(re.findall(r'"@type": ?"Question"', h))
    res[u] = {
        "existe": True,
        "title": html.unescape(g(r"<title>(.*?)</title>")),
        "desc": html.unescape(g(r'<meta name="description" content="([^"]*)"')),
        "h1": texto(g(r"<h1[^>]*>(.*?)</h1>")),
        "canonical": g(r'<link rel="canonical" href="([^"]*)"'),
        "robots": g(r'<meta name="robots" content="([^"]*)"'),
        "palabras": len(t.split()),
        "faq": faq,
        "precio": bool(re.search(r"\d[\d.,]*\s?(€|euros|EUR)", t)),
        "plazo": bool(re.search(r"\d+\s?(-|a|–)?\s?\d*\s?(días|semanas|horas|meses)", t)),
        "ejemplo": bool(re.search(r"\b(ejemplo|caso|por ejemplo|imagina)\b", t, re.I)),
        "imagen": len(re.findall(r"<img ", mh)),
        "svg": len(re.findall(r"<svg", mh)),
        "entrantes_contenido": sorted(entrantes_main.get(u, ())),
        "entrantes_total": len(entrantes_total.get(u, ())),
    }
    sh[u] = shingles(t)

# parecido de contenido (Jaccard de 5-gramas) entre páginas del sitemap
lista = [u for u in sh if sh[u]]
for u in lista:
    mejor, mu = 0.0, None
    for v in lista:
        if v == u:
            continue
        a, b = sh[u], sh[v]
        j = len(a & b) / len(a | b)
        if j > mejor:
            mejor, mu = j, v
    res[u]["mas_parecida"] = mu
    res[u]["parecido"] = round(mejor, 3)

json.dump(res, open(os.path.join(SEO, "medidas.json"), "w"), ensure_ascii=False, indent=1)
print(len(res), "URLs medidas")
