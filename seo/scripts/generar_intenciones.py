"""Regenera generador/intenciones.py desde seo/keywords.txt y seo/medidas.json (H1 actuales).

Uso (desde la raíz): python3 generador/construir.py marca web portadas && python3 seo/scripts/medir.py && python3 seo/scripts/generar_intenciones.py
"""
import json, os
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
A = [l.strip() for l in open(os.path.join(R, "seo/anexo-a-indexadas.txt")) if l.strip()]
m = json.load(open(os.path.join(R, "seo/medidas.json")))
filas = []
for l in open(os.path.join(R, "seo/keywords.txt")):
    if l.startswith("#") or not l.strip(): continue
    u, k, g = (l.strip().split("|") + [""])[:3]
    if g: filas.append((u, k, g))
# Páginas indexadas que compiten en un grupo: solo reciben enlaces
for l in open(os.path.join(R, "seo/intenciones-indexadas.txt")):
    if l.strip() and not l.startswith("#"):
        u, k, g = l.strip().split("|"); filas.append((u, k, g))
grupos = {}
for u, k, g in filas:
    x = m.get(u)
    if not x or not x.get("existe") or x["canonical"].replace("https://studioemprende.com", "") != u: continue
    grupos.setdefault(g, []).append((u, k, x["h1"]))
out = ["# Grupos de intención (canibalización): páginas que responden a búsquedas parecidas.",
       "# GENERADO por seo/scripts/generar_intenciones.py desde seo/keywords.txt. No editar a mano.",
       "# Cada página NO indexada del grupo enlaza a las demás con su keyword como anchor; las del Anexo A solo reciben enlaces.",
       "INDEXADAS = %r" % sorted(A), "GRUPOS = {"]
for g in sorted(grupos):
    out.append("  %r: [" % g)
    out += ["    (%r, %r, %r)," % t for t in sorted(grupos[g])]
    out.append("  ],")
out.append("}")
open(os.path.join(R, "generador/intenciones.py"), "w").write("\n".join(out) + "\n")
print({g: len(v) for g, v in grupos.items()})
