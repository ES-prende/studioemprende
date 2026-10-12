# Envia a IndexNow las URL nuevas o modificadas en este despliegue.
# Compara fechas.json del commit actual con el del commit anterior.
import json, subprocess, sys, urllib.request
DOM = "https://studioemprende.com"
KEY = "0e7088fe2e96eae098138bb5db5e8322"
def cargar(ref):
    try: return json.loads(subprocess.check_output(["git", "show", ref + ":generador/fechas.json"]))
    except Exception: return {}
nuevo, viejo = cargar("HEAD"), cargar("HEAD~1")
NOINDEX = {"404.html", "gracias.html"}
urls = []
for p, v in nuevo.items():
    if p in NOINDEX: continue
    if viejo.get(p, [None, None])[1] != v[1]:
        u = p[:-len("index.html")] if p.endswith("index.html") else p[:-5]
        urls.append(DOM + "/" + u)
if not urls:
    print("IndexNow: no hay paginas nuevas o modificadas"); sys.exit(0)
datos = json.dumps({"host": "studioemprende.com", "key": KEY, "keyLocation": DOM + "/" + KEY + ".txt", "urlList": urls[:10000]}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=datos, headers={"Content-Type": "application/json; charset=utf-8"})
try:
    r = urllib.request.urlopen(req, timeout=30); print("IndexNow:", r.status, "-", len(urls), "URL enviadas")
except Exception as e:
    print("IndexNow: aviso, no se pudo enviar:", e)
