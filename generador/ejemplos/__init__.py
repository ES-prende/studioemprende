# Ejemplos aplicados y FAQ propias por página (Bloque 1). Un archivo por lote: lote_N.py con EJEMPLOS = {url: {...}}.
# Solo para páginas NO indexadas; el generador ignora cualquier URL del Anexo A.
import glob, importlib, os
EJEMPLOS = {}
for _f in sorted(glob.glob(os.path.join(os.path.dirname(__file__), "lote_*.py"))):
    EJEMPLOS.update(importlib.import_module("ejemplos." + os.path.basename(_f)[:-3]).EJEMPLOS)
