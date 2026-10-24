"""Genera seo/COLA-INDEXACION.md: envíos diarios a Search Console (10/día) y Bing (100/día) por valor comercial."""
import csv, os
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOM = "https://studioemprende.com"
filas = list(csv.DictReader(open(os.path.join(R, "seo/priorizacion.csv"))))
# Primero lo nuevo y lo que más vende; dentro, el orden de la tabla de priorización
nuevas = ["/casos/contratalux", "/servicios/whatsapp-ia/", "/blog/cuanto-cuesta-un-crm-para-autonomos", "/servicios/fichador/", "/casos/", "/temas/", "/temas/gestion-y-crm", "/temas/inteligencia-artificial"]
orden = nuevas + [f["url"] for f in filas if f["url"] not in nuevas]
orden += [u for u in ["/temas/normativas-y-cumplimiento", "/temas/formacion-para-empresas", "/temas/webs-y-visibilidad", "/temas/emprender-y-crecer"] if u not in orden]
md = ["# Cola de envío a indexación", "",
      "Generada con `python3 seo/scripts/cola.py`. Orden: páginas nuevas y hubs sin descubrir, Anexo C y después las tandas de la tabla de priorización.", "",
      "## Bing Webmaster Tools (100 URLs/día)", "",
      "Envío de URL → pegar el bloque del día. Con IndexNow automático en cada despliegue, esto refuerza las que no se hayan cambiado.", ""]
for d in range(0, len(orden), 100):
    md += ["### Día %d" % (d // 100 + 1), "", "```"] + [DOM + u for u in orden[d:d + 100]] + ["```", ""]
md += ["## Google Search Console (10 URLs/día)", "",
       "Inspección de URLs → pegar la URL → «Solicitar indexación». Marca cada día al terminarlo.", ""]
for d in range(0, len(orden), 10):
    md += ["- [ ] **Día %d**: " % (d // 10 + 1) + ", ".join("`%s`" % u for u in orden[d:d + 10])]
open(os.path.join(R, "seo/COLA-INDEXACION.md"), "w").write("\n".join(md) + "\n")
print(len(orden), "URLs;", -(-len(orden) // 10), "días en Google;", -(-len(orden) // 100), "en Bing")
