# Enlaza la primera mención de cada norma (en el texto principal) a su fuente oficial.
import re
B = "https://www.boe.es/eli/es/"
E = "https://eur-lex.europa.eu/eli/"
NORMAS = [
 (r"(?:Real Decreto|RD) 1007/2023|Verifactu|VeriFactu|VERI\*FACTU", B + "rd/2023/12/05/1007"),
 (r"(?:Real Decreto-ley|RDL) 15/2025", B + "rdl/2025/12/02/15"),
 (r"Ley 18/2022|factura electrónica (?:B2B|entre empresas)", B + "l/2022/09/28/18"),
 (r"(?:Real Decreto|RD) 238/2026", B + "rd/2026/03/25/238"),
 (r"(?:Real Decreto-ley|RDL) 8/2019|registro (?:diario )?de jornada", B + "rdl/2019/03/08/8"),
 (r"Reglamento \(UE\) 2024/1689|AI Act|Reglamento europeo de (?:IA|Inteligencia Artificial)", E + "reg/2024/1689/oj"),
 (r"Ley 11/2023", B + "l/2023/05/08/11"),
 (r"Directiva \(UE\) 2022/2555|NIS2", E + "dir/2022/2555/oj"),
 (r"Reglamento \(UE\) 2024/2847|Reglamento de Ciberresiliencia", E + "reg/2024/2847/oj"),
 (r"(?:Real Decreto|RD) 933/2021", B + "rd/2021/10/26/933"),
 (r"(?:Real Decreto|RD) 1312/2024", B + "rd/2024/12/23/1312"),
 (r"Reglamento \(UE\) 2024/1028", E + "reg/2024/1028/oj"),
 (r"Ley 2/2023", B + "l/2023/02/20/2"),
 (r"Ley 3/2004", B + "l/2004/12/29/3"),
 (r"(?:Ley Orgánica|LO) 3/2018|LOPDGDD", B + "lo/2018/12/05/3"),
 (r"Ley 39/2015", B + "l/2015/10/01/39"),
 (r"Ley 31/1995|Ley de Prevención de Riesgos Laborales", B + "l/1995/11/08/31"),
 (r"Ley 34/2002|LSSI(?:-CE)?\b", B + "l/2002/07/11/34"),
 (r"Reglamento \(UE\) 2016/679|RGPD", E + "reg/2016/679/oj"),
 (r"Estatuto de los Trabajadores", B + "rdlg/2015/10/23/2"),
 (r"Ley 10/2021", B + "l/2021/07/09/10"),
 (r"(?:Real Decreto|RD) 171/2004", B + "rd/2004/01/30/171"),
]
_COMP = [(re.compile(r"(?<![\w/])(" + p + r")(?![\w/])"), u) for p, u in NORMAS]
_TAG = re.compile(r"(<[^>]+>)")
_BLOQ = {"a", "h1", "h2", "h3", "h4", "h5", "h6", "summary", "script", "style", "button", "title", "nav", "label", "th"}

def enlazar(html):
    i = html.find("<main"); j = html.rfind("</main>")
    if i < 0 or j < 0: return html
    trozos = _TAG.split(html[i:j]); pila = []; hechos = set(); out = []
    ya = set(re.findall(r'href="(https://(?:www\.boe\.es|eur-lex\.europa\.eu)[^"]*)"', html))
    for t in trozos:
        if t.startswith("<"):
            m = re.match(r"<(/?)([a-zA-Z0-9]+)", t)
            if m:
                n = m.group(2).lower()
                if n in _BLOQ:
                    if m.group(1): 
                        if n in pila: pila.remove(n)
                    elif not t.endswith("/>"): pila.append(n)
            out.append(t); continue
        if pila or not t.strip():
            out.append(t); continue
        for rx, u in _COMP:
            if u in hechos or u in ya: continue
            mm = rx.search(t)
            if mm:
                t = t[:mm.start()] + '<a href="%s" target="_blank" rel="noopener">%s</a>' % (u, mm.group(1)) + t[mm.end():]
                hechos.add(u)
                # el texto ya enlazado no debe volver a analizarse: se corta aquí
                break
        out.append(t)
    return html[:i] + "".join(out) + html[j:]
