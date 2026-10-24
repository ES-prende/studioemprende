"""Genera seo/PRIORIZACION.md y seo/priorizacion.csv a partir de medidas.json y keywords.txt."""
import csv, json, os
from collections import defaultdict

SEO = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
m = json.load(open(os.path.join(SEO, "medidas.json")))
leer = lambda n: [l.strip() for l in open(os.path.join(SEO, n)) if l.strip() and not l.startswith("#")]
A, B, C = set(leer("anexo-a-indexadas.txt")), set(leer("anexo-b-descubiertas.txt")), set(leer("anexo-c-rastreadas.txt"))
kw = {}
for l in leer("keywords.txt"):
    u, k, g = (l.split("|") + [""])[:3]
    kw[u] = (k, g)

# Orden de valor comercial: familia -> peso (menor = antes)
FAMILIA = [
    ("/servicios/fichador", 1), ("/blog/app-de-control-horario", 1),
    ("/servicios/software-de-gestion", 2), ("/servicios/erp-para-pymes", 2),
    ("/servicios/pix", 3), ("/servicios/agentes-de-ia", 3), ("/servicios/whatsapp-ia", 3), ("/blog/agente-de-ia-para-whatsapp", 3),
    ("/servicios/webs", 4), ("/servicios/presencia-digital", 4),
    ("/servicios/migraciones-e-integraciones", 5), ("/servicios/apps-moviles", 5), ("/servicios/automatizacion-y-datos", 5),
    ("/servicios/pequenas-empresas", 5), ("/servicios/autonomos", 5),
    ("/servicios/software-especializado", 6), ("/servicios/ciberseguridad-y-sistemas", 6), ("/servicios/departamento-tecnologico", 6),
    ("/servicios/consultoria-y-ayudas", 7), ("/servicios/formacion-ia", 7), ("/blog/plan-de-formacion", 7),
    ("/servicios/alojamientos-y-domotica", 7), ("/servicios/grandes-empresas", 8), ("/servicios/startups-e-inversores", 8),
    ("/servicios/problemas-sin-resolver", 8), ("/servicios/relevo-y-continuidad", 8), ("/servicios/deluxe", 9),
    ("/blog/", 9), ("/guias/", 10),
]

def peso(u):
    if u in C:
        return 0
    for p, w in FAMILIA:
        if u.startswith(p):
            return w
    return 11  # legales, partners, sobre nosotros

def canon(u):
    return m[u]["canonical"].replace("https://studioemprende.com", "")

filas = []
grupos = defaultdict(list)
for u, x in m.items():
    if u in A or not x.get("existe") or canon(u) != u:
        continue
    k, g = kw.get(u, ("(sin asignar)", ""))
    if g:
        grupos[g].append(u)
    estado = "Rastreada sin indexar" if u in C else ("Descubierta sin indexar" if u in B else "Aún no descubierta")
    falta = []
    if not x["precio"]:
        falta.append("precio o rango")
    if not x["plazo"]:
        falta.append("plazo de implantación")
    if not x["ejemplo"]:
        falta.append("ejemplo aplicado")
    if x["imagen"] + x["svg"] == 0:
        falta.append("visual (SVG/captura)")
    if len(x["entrantes_contenido"]) < 3:
        falta.append(f"enlaces entrantes ({len(x['entrantes_contenido'])})")
    if x["faq"] < 3:
        falta.append(f"FAQ propias ({x['faq']})")
    if g:
        falta.append(f"diferenciar · grupo {g}")
    if u in C:
        falta.insert(0, "REESCRITURA A FONDO")
    if estado == "Aún no descubierta":
        falta.insert(0, "enviar a indexar")
    filas.append({"url": u, "peso": peso(u), "estado": estado, "keyword": k, "grupo": g,
                  "palabras": x["palabras"], "faq": x["faq"], "entrantes": len(x["entrantes_contenido"]),
                  "title": x["title"], "falta": "; ".join(falta) or "solo enlazado y seguimiento"})

# hubs no descubiertos y Anexo C delante dentro de su familia
filas.sort(key=lambda f: (f["peso"], f["estado"] != "Rastreada sin indexar", f["estado"] != "Aún no descubierta",
                          not f["url"].endswith("/"), f["url"]))
TAM = 25
for i, f in enumerate(filas):
    f["tanda"] = i // TAM + 1

with open(os.path.join(SEO, "priorizacion.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=["tanda", "url", "estado", "keyword", "grupo", "palabras", "faq", "entrantes", "title", "falta"])
    w.writeheader()
    for f in filas:
        w.writerow({k: f[k] for k in w.fieldnames})

dup = sorted(u for u, x in m.items() if x.get("existe") and u not in A and canon(u) != u)
md = ["# Priorización SEO · Bloque 1", "",
      f"{len(filas)} páginas a trabajar (no indexadas y con canonical propio), en tandas de {TAM}.",
      "Orden: valor comercial de la familia → Anexo C → hubs sin descubrir → páginas de función.",
      "Las 111 URLs del Anexo A quedan fuera: no se tocan.", "",
      "Columnas: **entr.** = enlaces entrantes desde el contenido de otras páginas (sin contar menú ni pie).", ""]
t = None
for f in filas:
    if f["tanda"] != t:
        t = f["tanda"]
        md += ["", f"## Tanda {t}", "", "| URL | Estado | Keyword principal | Pal. | FAQ | Entr. | Qué le falta |", "|---|---|---|--:|--:|--:|---|"]
    md.append(f"| `{f['url']}` | {f['estado']} | {f['keyword']} | {f['palabras']} | {f['faq']} | {f['entrantes']} | {f['falta']} |")
md += ["", "## Grupos de canibalización", "",
       "Páginas que hoy responden a la misma intención. No se fusionan: cada una tiene ya su keyword propia (columna de arriba) y en su tanda se reenfoca el ángulo, el title y el H1.", ""]
for g in sorted(grupos):
    md.append(f"- **{g}**: " + ", ".join(f"`{u}` ({kw[u][0]})" for u in sorted(grupos[g])))
md += ["", "## Fuera de la tabla: duplicados con canonical a otra página", "",
       "Ya se resolvieron el 15/10 apuntando el canonical a la versión principal. No necesitan trabajo; Google las consolidará.", ""]
md += [f"- `{u}` → `{canon(u)}`" + (" (**indexada, Anexo A**)" if u in A else "") for u in dup]
open(os.path.join(SEO, "PRIORIZACION.md"), "w").write("\n".join(md) + "\n")
print(len(filas), "filas,", max(f["tanda"] for f in filas), "tandas;", len(grupos), "grupos")
sin = [f["url"] for f in filas if f["keyword"] == "(sin asignar)"]
print("sin keyword:", sin)
