"""Valida generador/ejemplos/lote_*.py contra seo/ejemplos/lote_*.txt.

Uso: python3 seo/scripts/validar_ejemplos.py [N]   (sin N valida todos los lotes presentes)
Comprueba: todas las URLs del lote, 110-260 palabras, 2 FAQ, preguntas únicas en toda la web,
sin nombres de clientes inventados ni precios de Studio Emprende distintos de los publicados.
"""
import glob, html, importlib.util, json, os, re, sys

R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PRECIOS_OK = {"990", "1.790", "3.690", "40", "90", "145", "8", "5", "300"}


def cargar(f):
    spec = importlib.util.spec_from_file_location("x", f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.EJEMPLOS


def preguntas_existentes():
    qs = {}
    for d, _, fs in os.walk(os.path.join(R, "web")):
        for f in fs:
            if not f.endswith(".html"): continue
            h = open(os.path.join(d, f), encoding="utf-8").read()
            for q in re.findall(r"<summary>(.*?)</summary>", h):
                qs.setdefault(html.unescape(q).strip().lower(), set()).add(os.path.join(d, f))
    return qs


lotes = sys.argv[1:] or [os.path.basename(f)[5:-3] for f in glob.glob(os.path.join(R, "generador/ejemplos/lote_*.py"))]
existentes = preguntas_existentes()
vistas = {}
errores = 0
for n in sorted(lotes, key=int):
    esperadas = [l.split("|")[1] for l in open(os.path.join(R, "seo/ejemplos/lote_%s.txt" % n)) if l.strip()]
    datos = cargar(os.path.join(R, "generador/ejemplos/lote_%s.py" % n))
    falt = [u for u in esperadas if u not in datos]
    sobr = [u for u in datos if u not in esperadas]
    msgs = []
    if falt: msgs.append("faltan %d: %s" % (len(falt), falt[:5]))
    if sobr: msgs.append("sobran %d: %s" % (len(sobr), sobr[:5]))
    for u, d in datos.items():
        if not {"titulo", "html", "faqs"} <= set(d): msgs.append("%s: faltan campos" % u); continue
        txt = html.unescape(re.sub(r"<[^>]+>", " ", d["html"]))
        np = len(txt.split())
        if not 110 <= np <= 260: msgs.append("%s: %d palabras" % (u, np))
        if len(d["faqs"]) != 2: msgs.append("%s: %d FAQ" % (u, len(d["faqs"])))
        if re.search(r"<(script|style|h1|h2)\b", d["html"]): msgs.append("%s: etiqueta no permitida" % u)
        if re.search(r"\bSL\b|S\.L\.|\bS\.A\.", txt): msgs.append("%s: posible nombre de empresa" % u)
        for frase in re.findall(r"[^.]*Studio Emprende[^.]*\.", txt):
            for p in re.findall(r"(\d[\d.]*)\s?€", frase):
                if p not in PRECIOS_OK: msgs.append("%s: precio de Studio Emprende no publicado (%s €)" % (u, p))
        for q, a in d["faqs"]:
            k = q.strip().lower()
            if k in existentes and not any(u.strip("/") in f for f in existentes[k]): msgs.append("%s: FAQ ya existe en otra página: %s" % (u, q))
            if k in vistas and vistas[k] != u: msgs.append("%s: FAQ repetida con %s: %s" % (u, vistas[k], q))
            vistas[k] = u
    errores += len(msgs)
    print("lote %s: %d/%d URLs, %s" % (n, len(datos), len(esperadas), "OK" if not msgs else "%d avisos" % len(msgs)))
    for m in msgs[:40]: print("   -", m)
sys.exit(1 if errores else 0)
