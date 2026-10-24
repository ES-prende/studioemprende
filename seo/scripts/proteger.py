"""Guarda las 111 páginas indexadas (Anexo A) frente a cualquier cambio.

  python3 seo/scripts/proteger.py --guardar   # crea seo/huellas-anexo-a.json desde web/
  python3 seo/scripts/proteger.py             # comprueba web/ contra las huellas; sale con error si algo cambió
"""
import hashlib, json, os, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WEB, SEO = os.path.join(RAIZ, "web"), os.path.join(RAIZ, "seo")
HUELLAS = os.path.join(SEO, "huellas-anexo-a.json")


def archivo(url):
    p = url.strip("/")
    if p == "":
        return "index.html"
    return p + "/index.html" if url.endswith("/") else p + ".html"


urls = [l.strip() for l in open(os.path.join(SEO, "anexo-a-indexadas.txt")) if l.strip()]
actual = {}
for u in urls:
    f = os.path.join(WEB, archivo(u))
    actual[u] = hashlib.sha256(open(f, "rb").read()).hexdigest() if os.path.exists(f) else None

if "--guardar" in sys.argv:
    json.dump(actual, open(HUELLAS, "w"), indent=0, sort_keys=True)
    print("Huellas guardadas:", len(actual), "| sin archivo:", [u for u, h in actual.items() if h is None])
    sys.exit(0)

base = json.load(open(HUELLAS))
cambiadas = [u for u in urls if base.get(u) != actual[u]]
if cambiadas:
    print("ERROR: han cambiado %d páginas indexadas (Anexo A):" % len(cambiadas))
    for u in cambiadas:
        print("  ", u)
    sys.exit(1)
print("OK: las %d páginas del Anexo A siguen idénticas." % len(urls))
