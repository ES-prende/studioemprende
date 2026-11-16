#!/usr/bin/env python3
"""Valida la reescritura «dolores primero» (generador/dolores_*.py).
Uso: python3 seo/scripts/validar_dolores.py [familia]   (p. ej. fichador, guias, webs)
Comprueba, página a página: que existe, longitudes mínimas, estructura distinta, frases y titulares no repetidos,
enlaces internos existentes, promesas prohibidas y precios donde no deben ir."""
import glob, importlib, os, re, sys, collections
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(R, "generador")); os.chdir(R)
D = {}; ORIGEN = {}
for f in sorted(glob.glob("generador/dolores_*.py")):
    m = importlib.import_module(os.path.basename(f)[:-3])
    for k, v in m.D.items():
        if k in D: print("DUPLICADA en dos archivos:", k)
        D[k.strip("/")] = v; ORIGEN[k.strip("/")] = os.path.basename(f)
LEGAL = {"aviso-legal", "cookies", "privacidad", "politica-editorial"}
PEND = [l.split(" — ")[0][2:].replace("https://studioemprende.com/", "") for l in open("seo/PAGINAS-SIN-REESCRIBIR.md") if l.startswith("- https")]
PEND = [u for u in PEND if u not in LEGAL]
fam = sys.argv[1] if len(sys.argv) > 1 else None
def familia(u): return u.split("/")[1] if u.startswith("servicios/") else u.split("/")[0]
txt = lambda h: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h)).strip()
err = collections.defaultdict(list)
for k in D:
    if k not in PEND: err[k].append("NO está en la lista de páginas a reescribir (no tocar)")
falta = [u for u in PEND if u not in D and (not fam or familia(u) == fam)]
firmas = collections.defaultdict(list); estr = collections.defaultdict(list); h2s = collections.defaultdict(list); frases = collections.defaultdict(set); preg = collections.defaultdict(list); leads = collections.defaultdict(list)
SINPRECIO = ("software-de-gestion", "erp-para-pymes")
for k, v in D.items():
    b = v.get("bloque", ""); t = txt(b); lead = txt(v.get("lead", ""))
    if len(lead.split()) < 28: err[k].append("lead corto (%d palabras, mínimo 28)" % len(lead.split()))
    if len(t.split()) < 230: err[k].append("bloque corto (%d palabras, mínimo 230)" % len(t.split()))
    if len(v.get("faq", [])) < 2: err[k].append("faltan preguntas frecuentes nuevas (mínimo 2)")
    if not v.get("estructura"): err[k].append("falta la etiqueta 'estructura'")
    if "<article" not in b and k.split("/")[0] == "servicios" and not b.lstrip().startswith("<section"): err[k].append("el bloque de una página de servicio debe ser <section class=\"sec\">…")
    if k.split("/")[0] in ("guias", "blog") and "<section" in b: err[k].append("en guías y blog el bloque va sin <section> (h2, h3, p, ul, tablas)")
    if "<h1" in b: err[k].append("no se puede usar <h1>")
    todo = (t + " " + lead + " " + " ".join(q + " " + a for q, a in v.get("faq", []))).lower()
    for mal in ("garantiz", "100 %", "100%", "líder", "el mejor ", "sin errores", "nunca falla", "cero llamadas", "testimonio"):
        if mal in todo: err[k].append("promesa o término a evitar: «%s»" % mal)
    if familia(k) in SINPRECIO and "€" in todo: err[k].append("precio en una página de programa de gestión/ERP/CRM (prohibido)")
    if " crm" in todo and "€" in todo and re.search(r"crm[^.]{0,80}€|€[^.]{0,80}crm", todo): err[k].append("precio junto a CRM (prohibido)")
    for href in re.findall(r'href="([^"]+)"', b):
        if href.startswith(("http", "#", "mailto", "tel")): continue
        if not href.startswith("/"): err[k].append("enlace relativo %s: usa rutas absolutas /…" % href); continue
        p = href.split("#")[0].split("?")[0].strip("/")
        if "?" in href: err[k].append("enlace con parámetros %s" % href)
        if p and not (os.path.exists("web/%s.html" % p) or os.path.exists("web/%s/index.html" % p)): err[k].append("enlace roto: %s" % href)
    firmas[" ".join(re.findall(r"<(section|h2|h3|ul|ol|table|blockquote|dl|details|div class=\"rejilla\"|p)\b", b))].append(k)
    estr[v.get("estructura", "").strip().lower()].append(k)
    for h in re.findall(r"<h[23][^>]*>(.*?)</h[23]>", b, re.S): h2s[txt(h).lower()].append(k)
    leads[" ".join(lead.lower().split()[:5])].append(k)
    for q, a in v.get("faq", []): preg[q.lower()].append(k)
    for s in re.split(r"(?<=[.!?»:])\s+", t + " " + lead):
        w = s.lower().split()
        for i in range(0, max(1, len(w) - 7)):
            if len(w) >= 8: frases[k].add(" ".join(w[i:i + 8]))
    # preguntas que ya existían en la página
    p = "web/%s.html" % k
    if os.path.exists(p):
        h = open(p).read()
        for q, a in v.get("faq", []):
            if h.count("<summary>%s</summary>" % q.replace("&", "&amp;")) > 1: err[k].append("pregunta frecuente duplicada con una que ya tenía la página: %s" % q)
for d, nombre in ((firmas, "misma secuencia de bloques HTML que"), (estr, "misma etiqueta de estructura que"), (h2s, "mismo titular que"), (preg, "misma pregunta frecuente que"), (leads, "el lead empieza igual que")):
    for kx, ks in d.items():
        if len(ks) > 1 and kx:
            for k in ks: err[k].append("%s %s%s" % (nombre, ", ".join(x for x in ks if x != k)[:160], (" → «%s»" % kx[:70]) if d is not firmas else ""))
ks = list(D)
for i, a in enumerate(ks):
    for b in ks[i + 1:]:
        c = frases[a] & frases[b]
        if len(c) >= 3:
            ej = sorted(c)[0]
            err[a].append("%d secuencias de 8 palabras repetidas con %s (p. ej. «%s»)" % (len(c), b, ej)); err[b].append("%d secuencias de 8 palabras repetidas con %s (p. ej. «%s»)" % (len(c), a, ej))
n = 0
for k in sorted(err):
    if fam and familia(k) != fam: continue
    print("\n✗ %s  [%s]" % (k, ORIGEN.get(k, "")))
    for x in err[k]: print("   -", x); n += 1
print("\nPáginas reescritas: %d de %d%s" % (len([k for k in D if not fam or familia(k) == fam]), len([u for u in PEND if not fam or familia(u) == fam]), (" (familia %s)" % fam) if fam else ""))
if falta: print("Faltan %d: %s" % (len(falta), ", ".join(falta[:12]) + (" …" if len(falta) > 12 else "")))
print("Avisos: %d" % n)
sys.exit(1 if n or falta else 0)
