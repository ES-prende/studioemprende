#!/usr/bin/env python3
"""Vuelca el texto visible de una o varias páginas ya construidas (web/...) para leerlas antes de reescribirlas.
Uso: python3 seo/scripts/texto_pagina.py servicios/pix/integraciones [otra ...] [--max 5000]"""
import re, sys
args = [a for a in sys.argv[1:] if not a.startswith("--")]
mx = int(sys.argv[sys.argv.index("--max") + 1]) if "--max" in sys.argv else 6000
args = [a for a in args if not a.isdigit()]
for u in args:
    u = u.replace("https://studioemprende.com/", "").strip("/")
    h = open("web/" + u + ".html").read()
    print("=" * 10, u)
    print("TITLE:", re.search(r"<title>(.*?)</title>", h).group(1))
    print("META:", re.search(r'<meta name="description" content="(.*?)"', h).group(1))
    b = h[h.find("<main"):h.find('<section class="cta">')]
    b = re.sub(r"<nav.*?</nav>", "", b, flags=re.S)
    b = re.sub(r"<(h[123])[^>]*>", lambda m: "¶" + "#" * int(m.group(1)[1]) + " ", b)
    b = b.replace("<summary>", "¶? ").replace('<p class="lead">', "¶LEAD: ")
    t = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", b)).replace("¶", "\n")
    print(t[:mx])
