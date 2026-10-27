import os, shutil, sys, re
from html import escape as e
sys.path.insert(0, os.path.dirname(__file__))
import formacion as FORM
import cursos_empresa as CE
import funciones as FN
import partners as PT
import casos as CS
import intenciones as INT
import enlaces_extra as EX
import blog_nuevos as BN
import temas as TM
import precio_fichador as PF
import precio_plazo as PP
from ejemplos import EJEMPLOS as EJ
from datos import SECCIONES, NORMATIVAS, NORM_EXTRA, SECTORES, PACKS, MENU
from blog import ARTICULOS
from alt_blog import ALT
import blog_formacion as BF
import blog_pymes as BP
import resumenes_blog as RB
import enlaces_normas as EN
ARTICULOS = [(a[0], a[1], a[2], a[3], a[4], a[5], a[6] + BP.EXCEL_EXTRA) if a[0] == "como-dejar-de-usar-excel-en-mi-empresa" else a for a in ARTICULOS]
NUEVOS = {a[0] for a in BF.ARTICULOS + BP.ARTICULOS}
ARTICULOS = BP.ARTICULOS + BF.ARTICULOS + ARTICULOS
ALT.update(BF.ALT); ALT.update(BP.ALT)
FAQS_BLOG = dict(BF.FAQS); FAQS_BLOG.update(BP.FAQS); FAQS_BLOG.update(BN.FAQS)
ALT.update(BN.ALT); RB.RESUMEN.update(BN.RESUMEN)
from guias import GUIAS, GRUPOS, SERVICIO_GUIAS
from pix import PIX_HUB, PIX_PAGINAS
from legales import HIST, AVISO, PRIVACIDAD, COOKIES

AQUI = os.path.dirname(os.path.abspath(__file__))
KIT = sys.argv[1]; OUT = sys.argv[2]
DOM = "https://studioemprende.com"
WA_NUM = "34601869668"; WA_VER = "601 86 96 68"; EMAIL = "info@studioemprende.com"
from urllib.parse import quote as _q
shutil.rmtree(OUT, ignore_errors=True)
for d in ("assets/css", "assets/js", "assets/img", "servicios"):
    os.makedirs(os.path.join(OUT, d), exist_ok=True)
os.makedirs(os.path.join(OUT, "blog"), exist_ok=True)
shutil.copytree(sys.argv[3], OUT + "/assets/img/blog")
# Las imagenes og (1200x630) de cada articulo estan en portadas/og/
shutil.copy(os.path.join(AQUI, "estilos.css"), OUT + "/assets/css/estilos.css")
shutil.copytree(os.path.join(AQUI, "fonts"), OUT + "/assets/fonts")
# Casos de éxito: estilos, script y medios propios (no se cargan en el resto de páginas)
shutil.copy(os.path.join(AQUI, "casos.css"), OUT + "/assets/css/casos.css")
shutil.copytree(os.path.join(AQUI, "casos_media"), OUT + "/assets/img/casos")
for src, dst in [("horizontal/studio-emprende-horizontal-color.svg", "logo-horizontal.svg"),
                 ("horizontal/studio-emprende-horizontal-blanco.svg", "logo-horizontal-blanco.svg"),
                 ("vertical/studio-emprende-vertical-color.svg", "logo-vertical.svg"),
                 ("simbolo/studio-emprende-simbolo-color.svg", "simbolo.svg"),
                 ("redes/portada-og-web-1200x630.png", "og-imagen.png")]:
    shutil.copy(os.path.join(KIT, src), OUT + "/assets/img/" + dst)
for f in os.listdir(KIT + "/favicon"):
    if not f.endswith(".txt"):
        shutil.copy(KIT + "/favicon/" + f, OUT + "/" + f)

open(OUT + "/assets/js/main.js", "w").write("""
(function(){
  var h=document.querySelector('.hamburguesa'),n=document.querySelector('.nav');
  if(h&&n){h.addEventListener('click',function(){var a=n.classList.toggle('abierta');h.setAttribute('aria-expanded',a)})}
  document.querySelectorAll('.desplegable>button').forEach(function(b){
    b.addEventListener('click',function(ev){ev.stopPropagation();var p=b.parentNode,a=p.classList.toggle('abierto');b.setAttribute('aria-expanded',a)})
  });
  document.addEventListener('click',function(ev){document.querySelectorAll('.desplegable.abierto').forEach(function(d){if(!d.contains(ev.target)){d.classList.remove('abierto');d.querySelector('button').setAttribute('aria-expanded','false')}})});
  document.addEventListener('keydown',function(ev){if(ev.key==='Escape'){document.querySelectorAll('.desplegable.abierto').forEach(function(d){d.classList.remove('abierto')})}});
  var q=new URLSearchParams(location.search),sv=document.getElementById('servicio'),fn=document.getElementById('funcion');if(sv&&q.get('servicio')){sv.value=q.get('servicio')}if(fn&&q.get('funcion')){fn.value=q.get('funcion')}
  var f=document.querySelector('form[data-contacto]');
  if(f){var t0=Date.now(),hum=false,tk=document.getElementById('_t'),av=document.getElementById('form-aviso');
    ['mousemove','touchstart','keydown','scroll'].forEach(function(e){window.addEventListener(e,function(){hum=true},{once:true,passive:true})});
    function aviso(m){if(av){av.textContent=m;av.hidden=false}}
    f.addEventListener('submit',function(ev){
      var bad=null,msg=(f.mensaje&&f.mensaje.value)||'',urls=(msg.match(/https?:\/\/|www\./gi)||[]).length,last=0;
      try{last=+localStorage.getItem('se_envio')||0}catch(x){}
      if(f._honey.value||f.website.value)bad='spam';
      else if(Date.now()-t0<4000)bad='Espera unos segundos antes de enviar.';
      else if(!hum)bad='Mueve el ratón o toca la pantalla y vuelve a intentarlo.';
      else if(urls>1)bad='Por seguridad, no incluyas más de un enlace en el mensaje.';
      else if(/[Ѐ-ӿ一-鿿]/.test(msg))bad='Escribe el mensaje en español o inglés.';
      else if(Date.now()-last<60000)bad='Ya has enviado un mensaje hace un momento. Espera un minuto.';
      if(bad){ev.preventDefault();if(bad!=='spam')aviso(bad);return}
      if(tk)tk.value=String(Date.now()-t0);
      try{localStorage.setItem('se_envio',String(Date.now()))}catch(x){}
      var b=f.querySelector('button[type=submit]');if(b){b.disabled=true;b.textContent='Enviando…'}
    },true);
  }
  if(f){f.addEventListener('submit',function(ev){var ok=true;f.querySelectorAll('[required]').forEach(function(i){var m=i.parentNode.querySelector('.error');if(!i.value.trim()){ok=false;if(m)m.hidden=false}else if(m){m.hidden=true}});if(!ok){ev.preventDefault()}})}
})();
""")

def by_menu(k): return [s for s in SECCIONES if s[1] == k]

def cabecera(r):
    cols = ""
    for k, nombre in MENU:
        cols += '<div role="group" aria-label="%s"><p class="mega-titulo">%s</p>%s</div>' % (e(nombre), nombre, "".join('<a href="%sservicios/%s.html">%s</a>' % (r, s[0], e(s[2])) for s in by_menu(k)))
    return """<a class="saltar" href="#contenido" style="position:absolute;left:-9999px">Saltar al contenido</a>
<div class="franja"></div>
<header class="cabecera"><div class="w">
<a class="logo" href="{r}index.html" aria-label="Studio Emprende, inicio"><img src="{r}assets/img/logo-horizontal.svg" alt="Studio Emprende" width="200" height="56"></a>
<nav class="nav" aria-label="Principal">
<div class="desplegable"><button type="button" aria-expanded="false">Servicios ▾</button><div class="mega">{cols}</div></div>
<a href="{r}servicios/pix/index.html">PIX IA</a>
<a href="{r}servicios/fichador.html">Fichador</a>
<a href="{r}sectores.html">Sectores</a>
<a href="{r}precios.html">Precios</a>
<a href="{r}normativas.html">Normativas</a>
<a href="{r}blog/index.html">Blog</a>
<a href="{r}contacto.html">Contacto</a>
</nav>
<div class="acciones"><a class="btn btn-s" href="{r}contacto.html">Hablar con nosotros</a><a class="btn btn-p" href="{r}contacto.html#diagnostico">Diagnóstico gratis</a>
<button class="hamburguesa" type="button" aria-label="Abrir menú" aria-expanded="false"><span></span><span></span><span></span></button></div>
</div></header>""".format(r=r, cols=cols)

def pie(r):
    prod = "".join('<a href="%sservicios/%s.html">%s</a>' % (r, s[0], e(s[2].split(" ·")[0])) for s in SECCIONES if s[1] in ("software", "producto", "ia"))
    quien = "".join('<a href="%sservicios/%s.html">%s</a>' % (r, s[0], e(s[2])) for s in by_menu("clientes"))
    return """<footer class="pie"><div class="w">
<div class="pie-top"><div class="pie-marca"><img src="{r}assets/img/logo-horizontal-blanco.svg" alt="Studio Emprende" width="200" height="56"><p>Software, IA y webs para emprender. 100 % online, para toda España.</p></div>
<div class="pie-cols"><div><b>Productos</b>{prod}</div><div><b>Para quién</b>{quien}</div>
<div><b>Recursos</b><a href="{r}guias/index.html">Guías para emprender</a><a href="{r}blog/index.html">Blog</a><a href="{r}normativas.html">Normativas</a><a href="{r}sectores.html">Sectores</a><a href="{r}precios.html">Precios</a><a href="{r}mapa-web.html">Mapa de la web</a></div>
<div><b>Empresa</b><a href="{r}sobre-nosotros.html">Sobre nosotros</a><a href="{r}partners.html">Hazte partner</a><a href="{r}contacto.html">Contacto</a><a href="{r}contacto.html#diagnostico">Diagnóstico gratis</a></div><div><b>Contacto</b><a href="https://wa.me/34601869668" target="_blank" rel="noopener">WhatsApp 601 86 96 68</a><a href="mailto:info@studioemprende.com">info@studioemprende.com</a><span style="display:block;margin-top:8px">Calle Betis 3, 41449 Alcolea del Río (Sevilla)</span></div></div></div>
<div class="pie-base"><span>© 2026 Studio Emprende · INTELIGENCIA SEVILLA SL · NIF B88763818 · Página actualizada el <!--FECHA_ACT--></span><span><a href="{r}aviso-legal.html">Aviso legal</a> · <a href="{r}privacidad.html">Privacidad</a> · <a href="{r}cookies.html">Cookies</a> · <a href="#" data-abrir-cookies>Configurar cookies</a></span></div>
</div></footer>
<script src="{r}assets/js/main.js"></script>
<div class="cookies" id="cookies" role="dialog" aria-live="polite" aria-label="Aviso de cookies" hidden>
<p><b>Cookies</b> Usamos cookies técnicas necesarias y, solo si nos das permiso, cookies de analítica y publicidad para medir visitas y campañas. <a href="{r}cookies.html">Más información</a></p>
<div class="cookies-opc" id="cookies-opc" hidden><label><input type="checkbox" checked disabled> Técnicas (siempre activas)</label><label><input type="checkbox" id="ck-ana"> Analítica</label><label><input type="checkbox" id="ck-pub"> Publicidad</label></div>
<div class="cookies-btn"><button type="button" class="btn btn-s" data-ck="rechazar">Rechazar</button><button type="button" class="btn btn-s" data-ck="config">Configurar</button><button type="button" class="btn btn-s" data-ck="guardar" hidden>Guardar selección</button><button type="button" class="btn btn-p" data-ck="aceptar">Aceptar todas</button></div>
</div>
<script>(function(){{var b=document.getElementById('cookies');if(!b)return;var k='se_consent';function g(){{try{{return localStorage.getItem(k)}}catch(e){{return null}}}}
function cid(){{var i='';try{{i=localStorage.getItem('se_cid');if(!i){{i=(Date.now().toString(36)+Math.random().toString(36).slice(2,12));localStorage.setItem('se_cid',i)}}}}catch(e){{i='sin-id'+Math.random().toString(36).slice(2,10)}}return i}}
function reg(acc,a,p){{try{{var d=JSON.stringify({{id:cid(),accion:acc,analitica:a,publicidad:p,version:'2026-10',url:location.href.split('#')[0]}});if(navigator.sendBeacon){{navigator.sendBeacon('/consentimiento.php',new Blob([d],{{type:'application/json'}}))}}else{{fetch('/consentimiento.php',{{method:'POST',body:d,keepalive:true}})}}}}catch(e){{}}}}
function save(a,p,acc){{var v={{analytics_storage:a?'granted':'denied',ad_storage:p?'granted':'denied',ad_user_data:p?'granted':'denied',ad_personalization:p?'granted':'denied'}};try{{localStorage.setItem(k,JSON.stringify(v))}}catch(e){{}}if(window.gtag)gtag('consent','update',v);window.dataLayer&&dataLayer.push({{event:'consent_update'}});reg(acc,a,p);b.hidden=true;}}
if(!g())b.hidden=false;
b.addEventListener('click',function(e){{var t=e.target.getAttribute('data-ck');if(!t)return;
if(t==='aceptar')save(true,true,'aceptar');else if(t==='rechazar')save(false,false,'rechazar');
else if(t==='config'){{document.getElementById('cookies-opc').hidden=false;e.target.hidden=true;b.querySelector('[data-ck=guardar]').hidden=false;}}
else if(t==='guardar')save(document.getElementById('ck-ana').checked,document.getElementById('ck-pub').checked,'guardar');}});
document.addEventListener('click',function(e){{if(e.target.closest&&e.target.closest('[data-abrir-cookies]')){{e.preventDefault();var c={{}};try{{c=JSON.parse(g()||'{{}}')}}catch(x){{}}document.getElementById('ck-ana').checked=c.analytics_storage==='granted';document.getElementById('ck-pub').checked=c.ad_storage==='granted';b.hidden=false;}}}});}})();</script>
""".format(r=r, prod=prod, quien=quien)

import json as _json
from urllib.parse import urljoin as _uj
MIGAS = []
ORG = {"@type": "Organization", "@id": DOM + "/#org", "name": "Studio Emprende", "url": DOM + "/", "logo": DOM + "/assets/img/logo-vertical.svg",
       "description": "Software de gestión modular, agentes de IA y webs con SEO para autónomos, pymes y empresas. 100 % online en toda España.",
       "areaServed": "ES", "knowsLanguage": "es", "email": EMAIL, "telephone": "+34 601 86 96 68",
       "contactPoint": {"@type": "ContactPoint", "telephone": "+34 601 86 96 68", "email": EMAIL, "contactType": "customer service", "availableLanguage": "es"},
       "sameAs": ["https://www.linkedin.com/company/studio-emprende", "https://maps.google.com/?cid=15547878701347304086"], "legalName": "INTELIGENCIA SEVILLA SL", "alternateName": "Studio Emprende", "taxID": "B88763818", "vatID": "ESB88763818",
       "address": {"@type": "PostalAddress", "streetAddress": "Calle Betis 3", "postalCode": "41449", "addressLocality": "Alcolea del Río", "addressRegion": "Sevilla", "addressCountry": "ES"}}

def _meta(d):
    d = " ".join(d.split())
    if len(d) > 155:
        c = d[:155]; c = c[:c.rfind(" ")].rstrip(",;:·-") ; d = c + "."
    for extra in [" 100 % online en toda España.", " Pide tu diagnóstico gratis."]:
        if extra.strip().rstrip(".").lower() in d.lower(): continue
        if "100 % online" in extra and "100 % online" in d: continue
        if len(d) < 140 and len(d + extra) <= 155: d += extra
    return d

def _tit(t):
    if len(t) <= 60: return t
    base = t.split(" · ")[0]
    return base if len(base) <= 60 else base[:57].rsplit(" ", 1)[0] + "…"


# ---- Ampliaciones de contenido (ampliaciones_lote_*.py) ----
import glob as _glob, importlib as _imp
AMPL = {}; AMPL_USADAS = set()
for _f in sorted(_glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "ampliaciones_lote_*.py"))):
    _m = _imp.import_module(os.path.basename(_f)[:-3])
    for _r, _v in _m.AMPL.items():
        AMPL[_r.replace("/index.html", "").replace(".html", "").strip("/")] = _v

def _clave(ruta):
    return ruta.replace("/index.html", "").replace(".html", "").strip("/")

def _ampliar(cuerpo, faqs, a):
    secs = "".join('<h2>%s</h2>%s' % (e(t), h) for t, h in a.get("secciones", []))
    extra_faq = a.get("faq", [])
    det = "".join("<details><summary>%s</summary><p>%s</p></details>" % (e(q), e(r)) for q, r in extra_faq)
    tiene_faq = 'class="faq"' in cuerpo
    if extra_faq and tiene_faq:
        i = cuerpo.find('<div class="faq">'); j = cuerpo.find("</div>", i)
        cuerpo = cuerpo[:j] + det + cuerpo[j:]
        faqs = list(faqs or FAQ) + list(extra_faq)
    elif extra_faq:
        secs += '<h2>Preguntas frecuentes</h2><div class="faq">' + det + "</div>"
        faqs = list(extra_faq)
    if "</article>" in cuerpo:
        i = cuerpo.rfind("</article>")
        return cuerpo[:i] + '<div class="ampliacion">' + secs + "</div>" + cuerpo[i:], faqs
    bloque = '<section class="sec ampliacion"><div class="w"><div class="texto-largo">' + secs + "</div></div></section>\n"
    fin = cuerpo.find('<section class="cta">')
    if fin < 0: fin = len(cuerpo)
    # retrocede por encima de las secciones de "relacionados" y de FAQ final
    while True:
        k = cuerpo.rfind("<section", 0, fin)
        if k < 0: break
        trozo = cuerpo[k:fin]
        if any(x in trozo for x in ('class="faq"', 'Más de ', 'También te puede interesar', 'Sigue leyendo', 'Relacionad', 'Preguntas frecuentes')) and k > cuerpo.find("</section>"):
            fin = k
        else: break
    return cuerpo[:fin] + bloque + cuerpo[fin:], faqs

TITULOS = {
 "servicios/software-de-gestion/gestion-de-flotas.html": "Gestión de flotas de vehículos en tu programa de gestión",
 "servicios/software-de-gestion/integraciones-por-api.html": "Integraciones por API con tu programa de gestión",
 "servicios/software-de-gestion/portal-de-pedidos-b2b.html": "Portal de pedidos B2B para distribuidores y clientes",
 "blog/index.html": "Blog de software, IA y webs para emprender · Studio Emprende",
 "servicios/webs/index.html": "Diseño de páginas web con SEO para negocios · Studio Emprende",
 "servicios/index.html": "Servicios de software, IA y webs · Studio Emprende",
 "servicios/whatsapp-ia/index.html": "Agentes de IA para WhatsApp Business · Studio Emprende",
 "servicios/erp-para-pymes/cuadro-de-mando-en-tiempo-real.html": "Cuadro de mando en tiempo real para pymes",
 "servicios/agentes-de-ia/index.html": "Agentes de IA para empresas y pymes · Studio Emprende",
 "mapa-web.html": "Mapa de la web: todas las páginas · Studio Emprende",
 "servicios/erp-para-pymes/index.html": "ERP para pymes modular y a medida · Studio Emprende",
 "sobre-nosotros.html": "Sobre nosotros: quiénes somos y cómo trabajamos · Studio Emprende",
 "guias/como-crear-una-startup.html": "Cómo crear una startup tecnológica paso a paso",
 "servicios/deluxe/index.html": "Servicios Deluxe: tecnología para hogar y familia · Studio Emprende",
 "servicios/grandes-empresas/index.html": "Software e IA para grandes empresas · Studio Emprende",
 "servicios/pequenas-empresas/index.html": "Software y webs para pequeñas empresas · Studio Emprende",
 "guias/diferencia-entre-hardware-y-software.html": "Diferencia entre hardware y software, con ejemplos",
 "servicios/software-de-gestion/presupuestador-y-configurador-online.html": "Presupuestador y configurador online para tu web",
 "guias/cuanto-cuesta-una-pagina-web.html": "Cuánto cuesta una página web en España en 2026",
 "guias/index.html": "Guías para emprender y digitalizar tu negocio · Studio Emprende",
 "guias/crear-pagina-web-para-vender.html": "Crear una página web para vender online paso a paso",
 "servicios/apps-moviles/index.html": "Apps móviles a medida para negocios · Studio Emprende",
 "servicios/alojamientos-y-domotica/index.html": "Software y domótica para viviendas turísticas · Studio Emprende",
 "servicios/automatizacion-y-datos/index.html": "Automatización de procesos para pymes · Studio Emprende",
 "servicios/ciberseguridad-y-sistemas/index.html": "Ciberseguridad para pymes y cumplimiento normativo",
 "servicios/consultoria-y-ayudas/index.html": "Consultoría de digitalización y ayudas para pymes",
 "servicios/fichador/index.html": "App de fichaje y control horario para empresas",
 "servicios/migraciones-e-integraciones/index.html": "Migración de datos e integraciones entre programas",
 "servicios/relevo-y-continuidad/index.html": "Relevo generacional y continuidad del negocio familiar",
 "blog/agente-de-ia-para-whatsapp.html": "Agente de IA para WhatsApp: automatiza las respuestas",
 "blog/app-de-control-horario-para-pequenas-empresas.html": "App de control horario para pequeñas empresas",
 "servicios/startups-e-inversores/index.html": "Software y desarrollo tecnológico para startups",
 "blog/que-es-un-erp-y-cuando-lo-necesito.html": "ERP para pymes: cuándo dejar de usar Excel",
 "blog/software-de-gestion-modular-con-automatizaciones.html": "Software de gestión modular con automatizaciones",
}

# Enlaces entre páginas que responden a búsquedas parecidas (grupos de intención), solo en páginas no indexadas
_INT_DE = {u: (g, k) for g, ms in INT.GRUPOS.items() for u, k, h in ms}
def _bloque_intencion(u):
    if u not in _INT_DE or u in INT.INDEXADAS: return ""
    g, _ = _INT_DE[u]
    otros = [(v, k, h) for v, k, h in INT.GRUPOS[g] if v != u][:6]
    if not otros: return ""
    li = "".join('<li><a href="%s">%s</a>: %s</li>' % (v, e(EX.cap(k)), e(h)) for v, k, h in otros)
    return ('<section class="sec" style="padding-top:0"><div class="w"><div class="tarjeta"><h2 class="h3" style="margin:0">¿Buscabas otra cosa? Lo mismo, con otro enfoque</h2>'
            '<ul class="lista lista-enl" style="margin-top:6px">%s</ul></div></div></section>' % li)

def pagina(ruta, titulo, desc, cuerpo, ld_extra=None, tipo="website", faqs=None, tipo_pagina="WebPage", indexar=True, fecha=None, og=None, extra_pagina=None, css=""):
    global MIGAS
    _k = _clave(ruta)
    if _k in CS.ENLACES_ENTRANTES:  # enlace al caso de éxito, solo en páginas no indexadas
        _b = CS.bloque_entrante("../" * ruta.count("/"), CS.ENLACES_ENTRANTES[_k]); _i = cuerpo.rfind('<section class="cta">')
        cuerpo = cuerpo[:_i] + _b + cuerpo[_i:] if _i >= 0 else cuerpo + _b
    if PF.aplica(_k) and "/" + _k + ("/" if ruta.endswith("index.html") or ruta.count("/") == 1 else "") not in INT.INDEXADAS:
        _bp = PF.bloque(_k)
        if _k in PF.DESTACADO:
            _i = cuerpo.find("</section>") + len("</section>")
            cuerpo = cuerpo[:_i] + _bp + cuerpo[_i:]
            ld_extra = (ld_extra if isinstance(ld_extra, list) else ([ld_extra] if ld_extra else [])) + PF.ofertas(DOM)
        else:
            _i = cuerpo.rfind('<section class="cta">')
            cuerpo = cuerpo[:_i] + _bp + cuerpo[_i:] if _i >= 0 else cuerpo + _bp
    _uk = "/" + _k + ("/" if ruta.endswith("index.html") or ruta.count("/") == 1 and ruta.startswith("servicios/") else "")
    if _uk in EJ and _uk not in INT.INDEXADAS:  # ejemplo aplicado y FAQ propias
        _ej = EJ[_uk]
        _be = '<section class="sec" style="padding-top:0"><div class="w"><div class="tarjeta"><p class="kicker" style="margin:0">Ejemplo aplicado</p><h2 class="h3" style="margin:0">%s</h2>%s</div></div></section>' % (e(_ej["titulo"]), _ej["html"])
        _i = cuerpo.rfind('<section class="cta">')
        cuerpo = cuerpo[:_i] + _be + cuerpo[_i:] if _i >= 0 else cuerpo + _be
        _nf = list(_ej.get("faqs", []))
        if _nf:
            faqs = list(faqs or FAQ) + _nf
            _i = cuerpo.rfind('<div class="faq">')
            _dh = "".join("<details><summary>%s</summary><p>%s</p></details>" % (e(q), e(a)) for q, a in _nf)
            if _i >= 0:
                _i += len('<div class="faq">')
                cuerpo = cuerpo[:_i] + _dh + cuerpo[_i:]
            else:  # sin bloque de FAQ: se crea visible, para que el schema y la página coincidan
                faqs = _nf
                _sf = '<section class="sec sec-suave"><div class="w"><div class="cab"><h2>Preguntas frecuentes</h2></div><div class="faq">%s</div></div></section>' % _dh
                _i = cuerpo.rfind('<section class="cta">')
                cuerpo = cuerpo[:_i] + _sf + cuerpo[_i:] if _i >= 0 else cuerpo + _sf
    _bpp = PP.bloque(_k)
    if _bpp and "/" + _k + ("/" if ruta.endswith("index.html") or ruta.count("/") == 1 else "") not in INT.INDEXADAS:
        _i = cuerpo.rfind('<section class="cta">')
        cuerpo = cuerpo[:_i] + _bpp + cuerpo[_i:] if _i >= 0 else cuerpo + _bpp
    _u = "/" + _k + ("/" if ruta.endswith("index.html") or ruta.count("/") == 1 and ruta.startswith("servicios/") else "")
    _bi = _bloque_intencion(_u)
    if _u in EX.POR_ORIGEN and _u not in INT.INDEXADAS:  # enlaces contextuales hacia páginas poco enlazadas
        _bi += ('<section class="sec" style="padding-top:0"><div class="w"><p class="kicker" style="margin:0 0 8px">También te puede interesar</p><p>%s</p></div></section>'
                % " · ".join('<a href="%s">%s</a>' % (d, e(a)) for d, a in EX.POR_ORIGEN[_u]))
    if _bi:
        _i = cuerpo.rfind('<section class="cta">')
        cuerpo = cuerpo[:_i] + _bi + cuerpo[_i:] if _i >= 0 else cuerpo + _bi
    if _k in AMPL:
        cuerpo, faqs = _ampliar(cuerpo, faqs, AMPL[_k]); AMPL_USADAS.add(_k)
    for (_rr, _hh), _txt in RB.RESP_H.items():
        if _clave(_rr) == _clave(ruta):
            for _hx in (_hh, e(_hh)):
                _m = re.search(r"(<h([23])[^>]*>)%s(</h\2>)" % re.escape(_hx), cuerpo)
                if _m:
                    cuerpo = cuerpo[:_m.end()] + '<p class="resp-directa">%s</p>' % e(_txt) + cuerpo[_m.end():]; break
    url = DOM + "/" + ruta.replace("index.html", "")
    titulo = {_clave(k): v for k, v in TITULOS.items()}.get(_clave(ruta), titulo)
    titulo = _tit(titulo); desc = _meta(desc)
    grafo = [ORG, {"@type": "WebSite", "@id": DOM + "/#web", "url": DOM + "/", "name": "Studio Emprende", "inLanguage": "es", "publisher": {"@id": DOM + "/#org"}}]
    wp = {"@type": tipo_pagina, "@id": url, "url": url, "name": titulo, "description": desc, "inLanguage": "es", "isPartOf": {"@id": DOM + "/#web"}, "about": {"@id": DOM + "/#org"}}
    wp["dateModified"] = "__FMOD__"
    if extra_pagina: wp.update(extra_pagina)
    grafo.append(wp)
    if MIGAS:
        el = [{"@type": "ListItem", "position": 1, "name": "Inicio", "item": DOM + "/"}]
        for i, (t, h) in enumerate(MIGAS, 2):
            el.append({"@type": "ListItem", "position": i, "name": t, "item": _uj(url, h) if h else url})
        grafo.append({"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": el})
        wp["breadcrumb"] = {"@id": url + "#breadcrumb"}
    if ruta.startswith("servicios/") and ruta != "servicios/index.html" and not ruta.startswith("servicios/pix/"):
        grafo.append({"@type": "Service", "@id": url + "#servicio", "name": titulo.split(" · ")[0], "description": desc, "provider": {"@id": DOM + "/#org"}, "areaServed": "ES", "url": url})
        wp["mainEntity"] = {"@id": url + "#servicio"}
    if 'class="faq"' in cuerpo:
        grafo.append({"@type": "FAQPage", "@id": url + "#faq", "isPartOf": {"@id": url}, "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in (faqs or FAQ)]})
        wp["hasPart"] = {"@id": url + "#faq"}
    if ld_extra: grafo.extend(ld_extra if isinstance(ld_extra, list) else [ld_extra])
    if not indexar: NOINDEX.add(ruta)
    OGIMG[ruta] = og or (DOM + "/assets/img/og-imagen.png")
    MIGAS = []
    ldj = '<script type="application/ld+json">%s</script>' % _json.dumps({"@context": "https://schema.org", "@graph": grafo}, ensure_ascii=False).replace("</", "<\\/")
    seo = """<meta name="robots" content="{rob}">
<meta property="og:url" content="{u}"><meta property="og:locale" content="es_ES"><meta property="og:site_name" content="Studio Emprende">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{t}"><meta name="twitter:description" content="{d}"><meta name="twitter:image" content="{og}">
{ld}""".format(u=url, t=e(titulo), d=e(desc), dom=DOM, ld=ldj, og=OGIMG[ruta], rob="index,follow,max-image-preview:large,max-snippet:-1" if indexar else "noindex,follow")
    cuerpo = cuerpo + "\n" + seo + "\n" if False else cuerpo
    _pagina(ruta, titulo, desc, cuerpo, seo, tipo, css)

def _ordenar_h(html):
    # Evita saltos H1 -> H3: un h3 sin h2 previo se convierte en h2 con aspecto de h3
    out = []; hay_h2 = False; pila = []; pos = 0
    for m in _re_h.finditer(html):
        out.append(html[pos:m.start()]); tag = m.group(0); pos = m.end()
        cierre, n = m.group(1) == "/", int(m.group(2))
        if not cierre:
            if n == 1: hay_h2 = False
            elif n == 2: hay_h2 = True
            if n == 3 and not hay_h2:
                pila.append(True); tag = tag.replace("<h3", "<h2", 1)
                tag = tag.replace('class="', 'class="h3 ', 1) if 'class="' in tag else tag.replace("<h2", '<h2 class="h3"', 1)
            elif n == 3: pila.append(False)
        elif n == 3 and pila and pila.pop(): tag = "</h2>"
        out.append(tag)
    return "".join(out) + html[pos:]
import re as _rem
_re_h = _rem.compile(r"<(/?)h([1-6])\b[^>]*>")

def _pagina(ruta, titulo, desc, cuerpo, seo, tipo, css=""):
    cuerpo = _ordenar_h(cuerpo)
    r = "../" * ruta.count("/")
    html = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}
gtag('consent','default',{{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',analytics_storage:'denied',functionality_storage:'granted',security_storage:'granted',wait_for_update:500}});
try{{var c=localStorage.getItem('se_consent');if(c)gtag('consent','update',JSON.parse(c));}}catch(e){{}}</script>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
}})(window,document,'script','dataLayer','GTM-52BRGTG9');</script>
<!-- End Google Tag Manager -->
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
{canonical}{bing}
<meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:image" content="{og}"><meta property="og:type" content="{tipo}">
{seo}
<link rel="icon" href="{r}favicon.ico" sizes="any"><link rel="icon" type="image/svg+xml" href="{r}favicon.svg"><link rel="apple-touch-icon" href="{r}apple-touch-icon.png"><link rel="manifest" href="{r}site.webmanifest"><meta name="theme-color" content="#7A2638">
<link rel="preload" href="/assets/fonts/jost.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="/assets/fonts/marcellus.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{r}assets/css/estilos.css">{css}
</head>
<body>
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-52BRGTG9"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
{cab}
<main id="contenido">
{c}
</main>
{pie}
<a class="wa-flot" href="https://wa.me/{wan}?text={wat}" target="_blank" rel="noopener" aria-label="Escríbenos por WhatsApp">
<span class="wa-burbuja"><b>¿Hablamos?</b>Te respondemos por WhatsApp</span>
<span class="wa-icono"><svg viewBox="0 0 32 32" width="30" height="30" aria-hidden="true"><path fill="currentColor" d="M16 3C8.8 3 3 8.6 3 15.6c0 2.5.8 4.9 2.1 6.9L3.6 29l6.7-1.7c1.8 1 3.8 1.5 5.7 1.5 7.2 0 13-5.6 13-12.6S23.2 3 16 3zm0 23.1c-1.8 0-3.6-.5-5.1-1.4l-.4-.2-4 1 .9-3.8-.2-.4c-1.1-1.7-1.6-3.6-1.6-5.6C5.6 10 10.2 5.5 16 5.5S26.4 10 26.4 15.6 21.8 26.1 16 26.1zm5.7-7.8c-.3-.2-1.9-.9-2.2-1-.3-.1-.5-.2-.7.2-.2.3-.8 1-1 1.2-.2.2-.4.2-.7.1-.3-.2-1.3-.5-2.5-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.5-.6c.2-.2.2-.3.3-.5.1-.2 0-.4 0-.6-.1-.2-.7-1.7-1-2.3-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.2 1.1-1.2 2.7s1.2 3.1 1.4 3.3c.2.2 2.4 3.6 5.8 5 2.9 1.1 3.4.9 4 .8.6-.1 1.9-.8 2.2-1.5.3-.7.3-1.4.2-1.5-.1-.2-.3-.3-.6-.4z"/></svg></span></a>
</body>
</html>""".format(t=e(titulo), d=e(desc), dom=DOM, ruta=ruta.replace("index.html", ""), canonical=("" if (ruta == "404.html" or ruta in NOINDEX) else '<link rel="canonical" href="%s/%s">' % (DOM, CANON.get(ruta, ruta).replace("index.html", ""))), r=r, css=('<link rel="stylesheet" href="%sassets/css/%s">' % (r, css) if css else ""), cab=cabecera(r), c=cuerpo, pie=pie(r), seo=seo, tipo=tipo, og=OGIMG[ruta], bing=('\n<meta name="msvalidate.01" content="AB0BB421B154681CB3B932E814F90956" />' if ruta == "index.html" else ""), wan=WA_NUM, wat=_q("Hola, vengo de la web de Studio Emprende (%s) y quiero información." % titulo.split(" · ")[0]))
    if ruta not in NOINDEX and ruta.split("/")[0] in ("blog", "guias", "servicios"):
        html = EN.enlazar(html)
    p = os.path.join(OUT, ruta); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w").write(html)
    PAGS.append(ruta)

PAGS = []
NOINDEX = set()
# Funciones que aparecen en dos secciones: la copia apunta (canonical) a la principal y sale del sitemap
CANON = {"servicios/software-de-gestion/gestion-de-flotas.html": "servicios/software-especializado/gestion-de-flotas.html",
         "servicios/software-de-gestion/presupuestador-y-configurador-online.html": "servicios/software-especializado/presupuestador-y-configurador-online.html",
         "servicios/software-de-gestion/portal-de-pedidos-b2b.html": "servicios/software-especializado/portal-de-pedidos-b2b.html",
         "servicios/erp-para-pymes/cuadro-de-mando-en-tiempo-real.html": "servicios/software-de-gestion/cuadro-de-mando-en-tiempo-real.html",
         "servicios/software-de-gestion/integraciones-por-api.html": "servicios/migraciones-e-integraciones/integraciones-por-api.html"}
FAQ_HOME = [("¿Qué es Studio Emprende?", "Un estudio que monta todo lo digital de un negocio: marca, web con SEO, programa de gestión, automatizaciones e inteligencia artificial, en packs con precio cerrado."),
 ("¿A quién ayudáis?", "A emprendedores, autónomos y pequeñas empresas que empiezan o quieren ordenar su negocio, y a asesores que montan negocios para sus clientes."),
 ("¿Usáis inteligencia artificial en los proyectos?", "Sí, cuando ahorra trabajo de verdad: automatizaciones, asistentes en WhatsApp y nuestro agente PIX conectado a tu programa de gestión, siempre con tu aprobación en lo importante."),
 ("¿Cómo funciona el diagnóstico gratis?", "Nos cuentas cómo trabajas y te decimos qué digitalizar o automatizar primero y cuánto costaría, sin compromiso."),
 ("¿Dais formación?", "Sí: formación en IA para equipos, sesiones individuales desde 40 € la hora y cursos a medida según la operativa de tu empresa.")]
OGIMG = {}

def cta(r):
    return """<section class="cta"><div class="w"><h2>Empieza hoy con tu diagnóstico gratis</h2>
<div class="botones"><a class="btn btn-claro" href="{r}contacto.html#diagnostico">Pedir diagnóstico</a><a class="btn btn-borde-claro" href="{r}contacto.html">Hablar con nosotros</a></div></div></section>""".format(r=r)

FAQ = [("¿Cuánto tardáis en tenerlo todo listo?", "Impulso Inicial: de 2 a 3 semanas. Negocio en Marcha: de 3 a 4 semanas. Llave en Mano: unos 2 meses. Los plazos cuentan desde que nos pasas la información necesaria, y te damos una fecha cerrada al empezar."),
       ("¿Qué incluye la cuota de 40 € al mes?", "El soporte y el mantenimiento de tu programa de gestión."),
       ("¿Puedo contratar un solo servicio?", "Sí. Con «Arma tu pack» eliges solo lo que necesitas."),
       ("¿Trabajáis con negocios de cualquier provincia?", "Sí. Somos 100 % online y trabajamos con autónomos, pymes y empresas de toda España."),
       ("¿Podéis importar mis datos de Excel u otro programa?", "Sí, la migración está incluida al implantar el programa de gestión.")]

def faq():
    return '<div class="faq">' + "".join("<details><summary>%s</summary><p>%s</p></details>" % (e(q), e(a)) for q, a in FAQ) + "</div>"

def packs(r):
    out = '<div class="rejilla">'
    for n, p, d, dest in PACKS:
        out += '<div class="tarjeta pack%s">%s<h3>%s</h3><p>%s</p><div class="precio">%s</div><span class="cuota">%s</span><a class="btn %s" href="%scontacto.html?pack=%s#diagnostico">%s</a></div>' % (
            " dest" if dest else "", '<span class="etiqueta">Más elegido</span>' if dest else "", e(n), e(d), p,
            "Según los servicios" if p == "A medida" else "+ 40 €/mes de soporte", "btn-p" if dest else "btn-s", r, n.replace(" ", "-").lower(), "Montar mi pack" if p == "A medida" else "Lo quiero")
    return out + "</div>"

def foto_blog(sl, alt, portada=False):
    b = "/assets/img/blog/" + sl
    carga = 'fetchpriority="high" decoding="async"' if portada else 'loading="lazy" decoding="async"'
    tam = "(max-width: 760px) 100vw, 820px" if portada else "(max-width: 760px) 100vw, 400px"
    return ('<picture><source type="image/webp" srcset="%s-600.webp 600w, %s.webp 1200w" sizes="%s">'
            '<img%s src="%s.jpg" srcset="%s-600.jpg 600w, %s.jpg 1200w" sizes="%s" alt="%s" width="1200" height="675" %s></picture>') % (
            b, b, tam, ' class="portada"' if portada else "", b, b, b, tam, e(alt), carga)

def tarjeta_blog(a, pre):
    img = foto_blog(a[0], ALT.get(a[0], a[1]))
    return '<a class="tarjeta tarjeta-blog" href="%s%s.html">%s<span class="etiqueta">%s</span><h3>%s</h3><p>%s</p><span class="mas">Leer artículo →</span></a>' % (pre, a[0], img, e(a[4]), e(a[1]), e(a[2]))
BLOGHOME = "".join(tarjeta_blog(a, "blog/") for a in ARTICULOS[:3])
# ---------- INICIO ----------
r = ""
cats = [("software", "Software de gestión", "ERP, CRM, apps y software especializado por módulos."),
        ("ia", "Inteligencia artificial", "Agentes, WhatsApp IA y automatización con PIX."),
        ("web", "Webs y presencia digital", "Webs con SEO, Google, redes y pantallas digitales."),
        ("soporte", "Soporte y seguridad", "Tu departamento tecnológico, sistemas y ciberseguridad."),
        ("formacion", "Consultoría y formación", "Formación IA, ayudas, relevo y problemas sin resolver."),
        ("producto", "Productos propios", "Fichador y CRM con domótica para alojamientos.")]
serv = ""
for k, n, d in cats:
    links = "".join('<li><a href="servicios/%s.html">%s</a></li>' % (s[0], e(s[2])) for s in by_menu(k))
    serv += '<div class="tarjeta"><h3>%s</h3><p>%s</p><ul class="lista" style="margin-top:6px">%s</ul></div>' % (n, d, links)
tec = "".join("<span>%s</span>" % t for t in ["WhatsApp", "Google Business", "OpenAI", "Claude", "Verifactu", "WordPress", "Next.js", "Stripe", "Microsoft 365", "Android", "iOS", "API REST"] * 2)
inicio = """
<section class="hero"><div class="w">
<div class="hero-txt"><p class="kicker">Software · IA · Webs para emprender</p>
<h1>Tu negocio, <span class="acento">llave en mano</span>.</h1>
<p class="lead">Programa de gestión modular, agentes de IA y web profesional en una sola cuenta. Empieza con lo que necesitas y crece cuando quieras.</p>
<div class="botones"><a class="btn btn-p" href="contacto.html#diagnostico">Pide tu diagnóstico gratis</a><a class="btn btn-s" href="precios.html">Ver los packs</a></div>
<div class="confianza"><span>Una sola cuenta</span><span>100 %% online</span><span>Toda España</span><span>Soporte que responde</span></div></div>
<div class="hero-card" data-nosnippet aria-label="Ejemplo del agente PIX trabajando"><div class="estado"><span>Agente PIX · en marcha</span><b>● activo</b></div>
<div class="fila">Nuevo contacto por WhatsApp: «Necesito una web y facturar con Verifactu»</div>
<div class="fila ok"><span>✓ Contacto creado en el CRM</span><span>✓ Pack «Negocio en Marcha» propuesto</span><span>✓ Reunión agendada el jueves a las 10:00</span></div>
<div class="fin">Presupuesto enviado al cliente</div></div>
</div></section>

<section class="sec sec-suave"><div class="w">
<div class="cab"><p class="kicker">Demo del programa · datos de ejemplo</p><h2>Tus ventas, en un tablero</h2></div>
<div class="demo" data-nosnippet><div class="demo-lat"><b style="color:#fff;font-weight:500">Studio Emprende</b><span class="act">CRM</span><span>Facturación</span><span>Agenda</span><span>Fichaje</span><span>PIX</span></div>
<div class="tablero">
<div class="col"><span>Nuevo · 3</span><div class="trato">Taller López<br><b>1.790 €</b></div><div class="trato">Clínica Sur<br><b>990 €</b></div></div>
<div class="col"><span>Propuesta · 2</span><div class="trato">Reformas Vega<br><b>3.690 €</b></div></div>
<div class="col"><span>Negociación · 1</span><div class="trato">Academia Norte<br><b>1.790 €</b></div></div>
<div class="col"><span>Ganado · 4</span><div class="trato ganado">Café Central<br><b>990 €</b></div></div>
</div></div>
<p class="aviso">● Nuevo contacto desde la web: Fisioterapia Ruiz</p>
<p class="mut" style="font-size:13px;margin-top:10px">Demostración con nombres y datos ficticios: así se ve el tablero de ventas del programa.</p>
</div></section>

<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Lo que hacemos</p><h2>Todo lo que necesitas para emprender</h2></div>
<div class="rejilla">
<a class="tarjeta" href="servicios/software-de-gestion.html"><span class="num">01</span><h3>Programa de gestión modular</h3><p>CRM, facturación con Verifactu, agenda y fichaje. Solo los módulos que uses.</p><span class="mas">Ver módulos →</span></a>
<a class="tarjeta" href="servicios/agentes-de-ia.html"><span class="num">02</span><h3>Agentes de IA</h3><p>PIX atiende, presupuesta y agenda por WhatsApp, entrenado con tu negocio.</p><span class="mas">Conocer a PIX →</span></a>
<a class="tarjeta" href="servicios/webs.html"><span class="num">03</span><h3>Webs y presencia digital</h3><p>Web con SEO, Google Business y redes listas desde el primer día.</p><span class="mas">Ver webs →</span></a>
<a class="tarjeta" href="servicios/departamento-tecnologico.html"><span class="num">04</span><h3>Acompañamiento</h3><p>Soporte mensual, formación y un único interlocutor para que no estés solo.</p><span class="mas">Ver soporte →</span></a>
</div></div></section>

<section class="tecno" aria-label="Tecnologías con las que trabajamos"><div class="cinta">%s</div></section>

<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Lo que frena al que empieza</p><h2>Si te suena alguno, te ayudamos</h2></div>
<div class="rejilla">
<div class="tarjeta dolor"><h3>No sabes por dónde empezar</h3><p>Mil herramientas, cursos milagro y meses perdidos. Te damos un plan claro.</p></div>
<div class="tarjeta dolor d2"><h3>Lo haces todo tú</h3><p>Facturas, clientes y redes en Excel y WhatsApp. Lo ordenamos y automatizamos.</p></div>
<div class="tarjeta dolor d3"><h3>No te encuentran</h3><p>Sin web, sin Google ni credibilidad. Te damos presencia profesional desde el primer día.</p></div>
</div></div></section>

<section class="sec sec-suave"><div class="w conectado">
<div style="flex:999 1 420px;min-width:0;display:flex;flex-direction:column;gap:14px"><p class="kicker">Una cuenta, todo conectado</p><h2>Clientes, cobros, equipo y web hablan entre sí</h2><p class="lead">Lo que entra por la web aparece en tu CRM, se factura con Verifactu, se cobra con recordatorios y PIX te lo resume cada lunes.</p></div>
<div class="nodos"><div class="nodo">Clientes</div><div class="nodo">Web</div><div class="nodo">Cobros</div><div class="nodo">Equipo</div><div class="nodo centro">PIX</div><div class="nodo">Facturas</div><div class="nodo">Agenda</div><div class="nodo">WhatsApp</div><div class="nodo">Informes</div></div>
</div></section>

<section class="sec"><div class="w">
<div class="bloque"><div class="bloque-txt"><p class="kicker">Facturación</p><h2>Factura con Verifactu sin pensarlo</h2><p class="lead">Facturas, presupuestos y cobros conectados a tus clientes. Preparado para 2027.</p><a href="servicios/software-de-gestion.html">Ver facturación →</a></div>
<div class="bloque-vis"><div class="factura"><div class="l"><b style="color:var(--tinta);font-weight:500">Factura 2026-0142</b><span class="pagada">Cobrada</span></div><div class="l"><span>Pack Negocio en Marcha</span><span>1.790,00 €</span></div><div class="l"><span>IVA 21 %%</span><span>375,90 €</span></div><div class="t"><span>Total</span><span>2.165,90 €</span></div><span class="mut" style="font-size:13px">QR Verifactu · registro enviado</span></div></div></div>
<div class="bloque inv"><div class="bloque-vis"><div class="chat"><div class="msg yo">¿Qué clientes no han pagado este mes?</div><div class="msg pix">Tienes 3 facturas pendientes por 2.470 €. ¿Les envío un recordatorio por WhatsApp?</div><div class="msg yo">Sí, envíalo</div></div></div>
<div class="bloque-txt"><p class="kicker">Agente de IA</p><h2>PIX trabaja mientras tú emprendes</h2><p class="lead">Pregúntale en lenguaje normal: consulta, crea y automatiza dentro de tu programa.</p><a href="servicios/agentes-de-ia.html">Conocer a PIX →</a></div></div>
<div class="bloque"><div class="bloque-txt"><p class="kicker">Fichaje</p><h2>Registro de jornada desde el móvil</h2><p class="lead">Cumple la ley desde el primer empleado. Informe para Inspección en un clic.</p><a href="servicios/fichador.html">Ver fichador →</a></div>
<div class="bloque-vis"><div class="movil"><span class="mut" style="font-size:13px">Lunes, 12 oct</span><span class="hora">08:59</span><span class="fichar">Fichar entrada</span><span class="mut" style="font-size:12px">Jornada de hoy: 0 h 00 min</span></div></div></div>
</div></section>

<section class="sec sec-suave"><div class="w bloque">
<div class="bloque-txt"><p class="kicker">A medida</p><h2>Si no existe, lo desarrollamos</h2><p class="lead">Módulos, apps e integraciones a medida de tu forma de trabajar, conectados a lo que ya usas.</p><a href="servicios/software-especializado.html">Ver software especializado →</a></div>
<div class="bloque-vis"><div class="terminal"><span>$ studio desplegar --cliente taller-lopez</span><span class="v">✓ Módulo órdenes de trabajo</span><span class="v">✓ Conexión con WhatsApp</span><span class="v">✓ Agente PIX entrenado</span><span class="v">✓ App móvil publicada</span><span>Listo en producción</span></div></div>
</div></section>

<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Servicios</p><h2>Todo lo que hacemos, por áreas</h2></div>
<div class="rejilla">%s</div>
<p style="margin-top:28px"><a class="btn btn-s" href="servicios/index.html">Ver todos los servicios</a></p>
</div></section>

<section class="sec sec-noche"><div class="w cifras">
<div class="cifra"><b>4</b><span>Packs para empezar</span></div><div class="cifra"><b>+150</b><span>Servicios a elegir</span></div><div class="cifra"><b>40 €</b><span>Soporte al mes</span></div><div class="cifra"><b>0 €</b><span>Diagnóstico inicial</span></div>
</div></section>

<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Precios</p><h2>Elige tu punto de partida</h2></div>%s
</div></section>

<section class="sec sec-suave"><div class="w">
<div class="cab"><p class="kicker">Para tu sector</p><h2>Soluciones pensadas para tu día a día</h2></div>
<div class="pildoras">%s</div>
</div></section>

<section class="sec"><div class="w" style="display:flex;flex-wrap:wrap;gap:32px;justify-content:space-between;align-items:center">
<div style="flex:999 1 420px;min-width:0"><p class="kicker">Normativas 2026-2027</p><h2>¿Te afecta Verifactu, el fichaje digital o el AI Act?</h2><p class="lead" style="margin-top:12px">Depende de tu forma jurídica y tu actividad. Verifactu: 1/1/2027 para sociedades y 1/7/2027 para el resto, con un aplazamiento a octubre de 2028 anunciado y pendiente de BOE. Factura electrónica B2B: 6/10/2027 o 6/10/2028 según facturación. Formación en IA: obligatoria desde el 2/2/2025. Registro de jornada: desde 2019.</p><p class="mut" style="margin-top:10px;font-size:14px">Fuentes oficiales: <a href="https://www.boe.es/eli/es/rd/2023/12/05/1007" target="_blank" rel="noopener">RD 1007/2023 (Verifactu)</a>, <a href="https://www.boe.es/eli/es/l/2022/09/28/18" target="_blank" rel="noopener">Ley 18/2022 (factura electrónica)</a>, <a href="https://eur-lex.europa.eu/eli/reg/2024/1689/oj" target="_blank" rel="noopener">Reglamento (UE) 2024/1689 (AI Act)</a> y <a href="https://www.boe.es/eli/es/rdl/2019/03/08/8" target="_blank" rel="noopener">RDL 8/2019 (registro de jornada)</a>. Normativa revisada el <time datetime="2026-10-12">12 de octubre de 2026</time>.</p><p style="margin-top:6px"><a href="normativas.html">Ver todas las normas, plazos y fuentes oficiales →</a></p></div>
<a class="btn btn-s" href="normativas.html">Ver normativas</a>
</div></section>

<section class="sec"><div class="w"><div class="cab"><p class="kicker">Blog</p><h2>Ideas claras para tu negocio</h2></div><div class="rejilla">%s</div><p style="margin-top:28px"><a class="btn btn-s" href="blog/index.html">Ver todos los artículos</a></p></div></section>
<section class="sec sec-suave"><div class="w"><div class="cab"><p class="kicker">Preguntas frecuentes</p><h2>Lo que más nos preguntan</h2></div>%s</div></section>
""" % (tec, serv, packs(""), "".join('<a class="pildora" href="sectores.html#%s">%s</a>' % (s.lower().replace(" ", "-"), s) for s in SECTORES), BLOGHOME, '<div class="faq">' + "".join("<details><summary>%s</summary><p>%s</p></details>" % (e(q), e(a)) for q, a in FAQ_HOME) + "</div>")
pagina("index.html", "Studio Emprende · Software, IA y webs para emprender", "Programa de gestión modular, agentes de IA y webs con SEO en una sola cuenta. Para autónomos, pymes y empresas de toda España.", inicio + cta(""), faqs=FAQ_HOME)

import unicodedata, re as _re
def slugify(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    return _re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:70]
def _faq_html(fs):
    return '<div class="faq">' + "".join("<details><summary>%s</summary><p>%s</p></details>" % (e(q), e(a)) for q, a in fs) + "</div>"
# ---------- SERVICIOS ----------
def migas(r, *items):
    global MIGAS
    MIGAS = list(items)
    s ='<nav class="migas" aria-label="Migas de pan"><a href="%sindex.html">Inicio</a>' % r
    for t, h in items:
        s += " / " + ('<a href="%s">%s</a>' % (h, e(t)) if h else e(t))
    return s + "</nav>"

hub = ""
for k, n, d in cats + [("clientes", "Para quién", "Autónomos, pymes, grandes empresas, startups y clientes Deluxe.")]:
    hub += '<div class="cab" style="margin:48px 0 20px"><p class="kicker">%s</p><h2>%s</h2></div><div class="rejilla">' % (n, d)
    for s in by_menu(k):
        hub += '<a class="tarjeta" href="%s.html"><h3>%s</h3><p>%s</p><span class="mas">Ver servicio →</span></a>' % (s[0], e(s[2]), e(s[3]))
    hub += "</div>"
pagina("servicios/index.html", "Servicios · Studio Emprende", "Todos los servicios de Studio Emprende: software de gestión, IA, webs, soporte, formación y más.",
       '<section class="page-hero"><div class="w">%s<h1>Servicios</h1><p class="lead">Todo lo que hacemos, organizado por áreas. Empieza por lo que más te urge.</p></div></section><section class="sec" style="padding-top:24px"><div class="w">%s</div></section>%s' % (migas("../", ("Servicios", None)), hub, cta("../")))

# H1 y bloque propio en hubs no indexados (el nombre del servicio sigue igual en menús)
HUB_H1 = {"whatsapp-ia": "Agentes de IA para WhatsApp: atienden, agendan y recuerdan citas por ti",
          "alojamientos-y-domotica": "Software y domótica para viviendas turísticas y casas",
          "automatizacion-y-datos": "Automatización de procesos y datos para pymes",
          "ciberseguridad-y-sistemas": "Ciberseguridad, sistemas y cumplimiento para pymes",
          "consultoria-y-ayudas": "Consultoría de digitalización y ayudas para pymes",
          "fichador": "App de fichaje y control horario para empresas",
          "startups-e-inversores": "Software y desarrollo tecnológico para startups",
          "migraciones-e-integraciones": "Migración de datos e integraciones entre programas",
          "relevo-y-continuidad": "Relevo generacional y continuidad del negocio"}
HUB_EXTRA = {"whatsapp-ia": """<section class="sec"><div class="w"><div class="cab"><p class="kicker">Agentes de IA para WhatsApp</p><h2>¿Qué es un agente de IA para WhatsApp y qué hace en un negocio?</h2></div>
<p>Un agente de IA para WhatsApp es un asistente conectado a tu número de WhatsApp Business que contesta a los clientes con la información de tu negocio, agenda citas en tu calendario, envía recordatorios y pasa la conversación a una persona cuando hace falta. No es un menú de opciones: entiende lo que el cliente escribe y responde con tus horarios, tarifas y disponibilidad reales.</p>
<table><thead><tr><th>Lo que hace</th><th>Lo que no hace</th></tr></thead><tbody>
<tr><td>Responde preguntas frecuentes a cualquier hora</td><td>Inventar precios o plazos que no le has dado</td></tr>
<tr><td>Da cita y la apunta en tu agenda</td><td>Cerrar acuerdos delicados sin tu aprobación</td></tr>
<tr><td>Recuerda la cita y recoloca huecos</td><td>Escribir en masa a quien no ha dado su consentimiento</td></tr>
<tr><td>Crea la ficha del cliente en tu CRM</td><td>Sustituir la atención humana cuando el cliente la pide</td></tr>
</tbody></table>
<h3 style="margin-top:28px">¿Cuánto cuesta?</h3>
<p>Con PIX, WhatsApp va incluido en el plan Profesional, de <strong>145 €/mes para 5 personas</strong>, junto con Instagram, Facebook, LinkedIn y las principales herramientas de CRM. Aparte, Meta cobra los mensajes de plantilla que se envían fuera de una conversación abierta, según el país y el tipo de mensaje. Precios y fases del piloto en <a href="../servicios/pix/implantacion-y-precios.html">implantación y precios de PIX</a>.</p>
<h3 style="margin-top:28px">Por dónde empezar</h3>
<p>Por el proceso que más mensajes genera: casi siempre, pedir cita o preguntar disponibilidad. Se configura con tus respuestas reales, se prueba unas semanas con revisión humana y se amplía después a recordatorios y a la <a href="whatsapp-ia/reactivacion-de-clientes-y-pacientes-inactivos.html">reactivación de clientes inactivos</a>. Si quieres entender antes cómo funciona, tienes la guía <a href="../blog/agente-de-ia-para-whatsapp.html">cómo automatizar las respuestas de WhatsApp con IA</a>.</p>
</div></section>"""}
for slug, menu, titulo, intro, bloques in SECCIONES:
    cuerpo = ""
    for b, items in bloques:
        cuerpo += '<div class="tarjeta" style="margin-bottom:18px"><h3>%s</h3><ul class="lista lista-enl">%s</ul></div>' % (e(b), "".join('<li><a href="%s/%s.html">%s</a></li>' % (slug, slugify(i), e(i)) for i in items))
    rel = [s for s in by_menu(menu) if s[0] != slug]
    relh = "".join('<a class="tarjeta" href="%s.html"><h3>%s</h3><p>%s</p><span class="mas">Ver →</span></a>' % (s[0], e(s[2]), e(s[3])) for s in rel[:3])
    norm = [n for n in NORMATIVAS if n[3] == slug]
    normh = ("".join('<p style="font-size:14px;color:#C9C1BB"><b style="color:#fff;font-weight:500">%s</b> · %s</p>' % (e(n[0]), e(n[2])) for n in norm)) if norm else ""
    aside = """<aside class="lateral-aside"><h3>¿Hablamos?</h3><p style="color:#C9C1BB">Cuéntanos qué necesitas y te preparamos una propuesta sin compromiso.</p>{n}
<a class="btn btn-claro" href="../contacto.html?servicio={s}#diagnostico">Pedir diagnóstico gratis</a><a class="btn btn-borde-claro" href="../precios.html">Ver packs</a></aside>""".format(s=slug, n=normh)
    html = """<section class="page-hero"><div class="w">{m}<p class="kicker">{cat}</p><h1>{t}</h1><p class="lead">{i}</p>
<div class="botones" style="margin-top:24px"><a class="btn btn-p" href="../contacto.html?servicio={s}#diagnostico">Pedir información</a><a class="btn btn-s" href="index.html">Ver todos los servicios</a></div></div></section>
<section class="sec"><div class="w lateral"><div class="lateral-main">{c}</div>{a}</div></section>
{x}{rel}""".format(x=FORM.hub_extra("../").format(formador=FORM.tarjeta_formador("../"), faq=_faq_html(FORM.HUB_FAQS)) if slug == "formacion-ia" else "", m=migas("../", ("Servicios", "index.html"), (titulo, None)), cat=dict(MENU)[menu], t=e(HUB_H1.get(slug, titulo)), i=e(intro), s=slug, c=cuerpo, a=aside,
                 rel=('<section class="sec sec-suave"><div class="w"><div class="cab"><p class="kicker">También te puede interesar</p><h2>Servicios relacionados</h2></div><div class="rejilla">%s</div></div></section>' % relh) if relh else "")
    html += HUB_EXTRA.get(slug, "")
    gs = [g for g in GUIAS if g[0] in SERVICIO_GUIAS.get(slug, [])]
    if gs:
        html += '<section class="sec"><div class="w"><div class="cab"><p class="kicker">Guías para emprender</p><h2>Antes de empezar, te puede servir</h2></div><div class="rejilla">%s</div></div></section>' % "".join('<a class="tarjeta" href="../guias/%s.html"><h3>%s</h3><p>%s</p><span class="mas">Leer guía →</span></a>' % (g[0], e(g[4]), e(g[3][:120].rsplit(" ",1)[0] + "…")) for g in gs[:3])
    if slug in ("agentes-de-ia", "whatsapp-ia", "automatizacion-y-datos", "software-de-gestion", "erp-para-pymes"):
        html += '<section class="sec sec-suave"><div class="w"><div class="cab"><p class="kicker">Nuestro agente de IA</p><h2>Conoce PIX, la IA que trabaja dentro de tu empresa</h2></div><p class="lead" style="max-width:760px">PIX se conecta a tus datos y herramientas, atiende por web, WhatsApp, correo y voz y completa procesos con aprobación humana. Desde 90 €/mes.</p><div class="botones" style="margin-top:20px"><a class="btn btn-p" href="pix/index.html">Descubrir PIX</a><a class="btn btn-s" href="pix/implantacion-y-precios.html">Precios de PIX</a></div></div></section>'
    if slug == "formacion-ia":
        pagina("servicios/formacion-ia.html", "Formación en IA para empresas y equipos · Studio Emprende", "Formación en IA práctica para tu equipo: casos reales de cada área, normas de uso y seguimiento. Online o presencial, con Jordan García.", html + cta("../"), faqs=FORM.HUB_FAQS, ld_extra=[FORM.curso_hub(), FORM.JORDAN])
    else:
        pagina("servicios/%s.html" % slug, "%s · Studio Emprende" % titulo, intro[:155], html + cta("../"))


# ---------- PAGINAS DE CADA FUNCION ----------
for slug, menu, titulo, intro, bloques in SECCIONES:
    for b, items in bloques:
        for it in items:
            fs = slugify(it)
            if slug == "formacion-ia" and (fs == FORM.SESION_SLUG or fs in CE.SLUGS): continue
            _fk = "%s/%s" % (slug, fs)
            if _fk in FN.PAGINAS:
                _c = FN.PAGINAS[_fk]
                _h = FN.html(_fk, _c, migas("../../", ("Servicios", "../index.html"), (titulo, "../%s.html" % slug), (it, None)), _faq_html(_c["faqs"]), titulo)
                pagina("servicios/%s/%s.html" % (slug, fs), _c["titulo"] + " · Studio Emprende", _c["meta"], _h + cta("../../"), faqs=_c["faqs"], fecha=FN.FECHA)
                continue
            herm = [x for x in items if x != it]
            hermh = "".join('<li><a href="%s.html">%s</a></li>' % (slugify(x), e(x)) for x in herm)
            otros = [(bb, ii) for bb, ii in bloques if bb != b]
            otrosh = "".join('<div class="tarjeta"><h3>%s</h3><ul class="lista lista-enl">%s</ul></div>' % (e(bb), "".join('<li><a href="%s.html">%s</a></li>' % (slugify(x), e(x)) for x in ii[:5])) for bb, ii in otros[:3])
            html = """<section class="page-hero"><div class="w">{m}<p class="kicker">{cat} · {b}</p><h1>{t}</h1><p class="lead">{t} forma parte de nuestro servicio de {sec_l}. {intro}</p>
<div class="botones" style="margin-top:24px"><a class="btn btn-p" href="../../contacto.html?servicio={s}&amp;funcion={fs}#diagnostico">Quiero esto en mi negocio</a><a class="btn btn-s" href="../{s}.html">Ver {sec_l}</a></div></div></section>
<section class="sec"><div class="w lateral"><div class="lateral-main">
<div class="tarjeta" style="margin-bottom:18px"><h3>Cómo lo trabajamos</h3><ul class="lista">
<li>Analizamos cómo lo haces hoy y qué te gustaría mejorar.</li>
<li>Lo adaptamos a tu forma de trabajar y a tu sector.</li>
<li>Lo conectamos con el resto de tus herramientas y, si quieres, con el agente PIX.</li>
<li>Te formamos y te acompañamos las primeras semanas.</li></ul></div>
<div class="tarjeta"><h3>Se combina bien con</h3><ul class="lista lista-enl">{herm}</ul></div>
</div>
<aside class="lateral-aside"><h3>¿Te interesa?</h3><p style="color:#C9C1BB">Te contamos cómo encaja {tl} en tu negocio y te damos un presupuesto sin compromiso.</p><a class="btn btn-claro" href="../../contacto.html?servicio={s}&amp;funcion={fs}#diagnostico">Pedir información</a><a class="btn btn-borde-claro" href="../../precios.html">Ver packs</a></aside></div></section>
{otros}""".format(m=migas("../../", ("Servicios", "../index.html"), (titulo, "../%s.html" % slug), (it, None)), cat=dict(MENU)[menu], b=e(b), t=e(it), tl=e(it[0].lower() + it[1:]), sec_l=e(titulo[0].lower() + titulo[1:]), intro=e(intro), s=slug, fs=fs, herm=hermh,
                 otros=('<section class="sec sec-suave"><div class="w"><div class="cab"><p class="kicker">Más de %s</p><h2>Otras funciones</h2></div><div class="rejilla">%s</div></div></section>' % (e(titulo), otrosh)) if otrosh else "")
            pagina("servicios/%s/%s.html" % (slug, fs), "%s · %s · Studio Emprende" % (it, titulo), ("%s: %s" % (it, intro))[:155], html + cta("../../"), indexar=("servicios/%s/%s.html" % (slug, fs)) in CANON)

_ses = FORM.sesion_html(migas("../../", ("Servicios", "../index.html"), ("Formación en IA", "../formacion-ia.html"), ("Sesión de IA 1 a 1", None)), _faq_html(FORM.SESION_FAQS), "../../")
pagina("servicios/formacion-ia/%s.html" % FORM.SESION_SLUG, FORM.SESION_TITULO, FORM.SESION_META, _ses + cta("../../"), faqs=FORM.SESION_FAQS, ld_extra=[FORM.curso_sesion(), FORM.JORDAN])

for _c in CE.CURSOS:
    _m = migas("../../", ("Servicios", "../index.html"), ("Formación en IA", "../formacion-ia.html"), (_c["titulo"], None))
    _ld = [FORM.JORDAN] + ([CE.curso_ld(_c, FORM.JORDAN["@id"])] if _c["curso"] else [])
    pagina("servicios/formacion-ia/%s.html" % _c["slug"], _c["titulo"] + " · Studio Emprende", _c["meta"], CE.html(_c, _m, _faq_html(_c["faqs"]), FORM.tarjeta_formador("../../")) + cta("../../"), faqs=_c["faqs"], ld_extra=_ld, fecha=CE.FECHA)

# ---------- PIX (agente de IA empresarial) ----------
def _pix_nav(actual):
    return '<aside class="lateral-aside"><h3>PIX por dentro</h3><ul class="lista lista-enl" style="margin:8px 0 18px">%s</ul><a class="btn btn-claro" href="../../contacto.html?servicio=agentes-de-ia#diagnostico">Solicitar demo de PIX</a><a class="btn btn-borde-claro" href="implantacion-y-precios.html">Ver precios</a></aside>' % "".join(
        '<li><a style="color:#fff" href="%s">%s</a></li>' % ("index.html" if s == "" else s + ".html", e(n)) for s, n in [("", "Qué es PIX")] + [(x["slug"], x["nav"]) for x in PIX_PAGINAS] if s != actual)
_PIXAPP = {"@type": "SoftwareApplication", "@id": DOM + "/servicios/pix/#app", "name": "PIX", "alternateName": "PIX, agente de IA empresarial",
           "applicationCategory": "BusinessApplication", "operatingSystem": "Windows, macOS, Linux, Android, Web",
           "description": PIX_HUB["resumen"], "url": DOM + "/servicios/pix/", "provider": {"@id": DOM + "/#org"},
           "offers": [{"@type": "Offer", "name": n, "availability": "https://schema.org/InStock", "price": pr, "priceCurrency": "EUR", "priceSpecification": {"@type": "UnitPriceSpecification", "price": pr, "priceCurrency": "EUR", "unitCode": "MON", "valueAddedTaxIncluded": False}, "seller": {"@id": DOM + "/#org"}}
                      for n, pr in [("PIX 3 personas", "90"), ("PIX 5 personas", "145")]]}
_cap = "".join('<a class="tarjeta" href="%s.html"><h3>%s</h3><p>%s</p><span class="mas">Ver más →</span></a>' % (sl, e(t), e(d)) for t, d, sl in PIX_HUB["capacidades"])
_dol = "".join('<div class="tarjeta"><h3>%s</h3><p>%s</p></div>' % (e(t), e(d)) for t, d in PIX_HUB["dolor"])
_mapa = "".join('<a class="tarjeta" href="%s.html"><h3>%s</h3><p>%s</p><span class="mas">Leer →</span></a>' % (x["slug"], e(x["nav"]), e(x["meta"][:140].rsplit(" ", 1)[0] + "…")) for x in PIX_PAGINAS)
_impacto = """<section class="sec sec-oscura"><div class="w"><div class="cab"><p class="kicker">Lo que PIX te devuelve</p><h2>¿Cuánto tiempo ahorra PIX?</h2></div>
<p class="lead" style="max-width:780px;margin-bottom:28px">De media, PIX devuelve 11 horas a la semana a cada persona de los equipos comerciales y de administración, porque se queda con el trabajo de copiar, cuadrar y dar formato.</p>
<div class="cifras"><div class="cifra"><b>11 h</b><span>a la semana por persona, libres para el trabajo que pide criterio</span></div><div class="cifra"><b>4 min</b><span>para tener una oferta lista, frente a unos 45 minutos haciéndola a mano</span></div><div class="cifra"><b>87 %</b><span>menos tiempo en correo, PDF, seguimientos y agenda del día</span></div><div class="cifra"><b>48 h</b><span>para verlo funcionando con tu equipo, sin proyectos de seis meses</span></div></div>
<p style="color:#C9C1BB;font-size:14px;margin-top:22px">Cifras medias en equipos comerciales y de administración que usan PIX.</p></div></section>
<section class="sec"><div class="w"><div class="cab"><p class="kicker">Calcula tu caso</p><h2>¿Cuántas horas recupera tu equipo con PIX?</h2></div>
<p class="lead" style="max-width:780px">Multiplica 11 horas por cada persona del equipo: con 5 personas son 55 horas a la semana y 2.530 al año, el trabajo de una persona más sin contratarla.</p>
<div class="texto-largo" style="margin-top:18px"><table><thead><tr><th>Personas en el equipo</th><th>Horas recuperadas a la semana</th><th>Horas recuperadas al año</th></tr></thead><tbody><tr><td>1</td><td>11 h</td><td>506 h</td></tr><tr><td>5</td><td>55 h</td><td>2.530 h</td></tr><tr><td>12</td><td>132 h</td><td>6.072 h</td></tr></tbody></table><p class="mut" style="font-size:14px">Cálculo con 11 horas por persona y 46 semanas de trabajo al año.</p></div></div></section>
<section class="sec sec-suave"><div class="w"><div class="cab"><p class="kicker">Cómo trabaja</p><h2>¿Qué hace PIX mientras tu equipo atiende a los clientes?</h2></div>
<p class="lead" style="max-width:780px;margin-bottom:20px">PIX es un agente, no un chat de preguntas y respuestas: lee lo que entra, prepara el trabajo y avisa a quien toca, y tu equipo solo revisa y aprueba.</p>
<div class="rejilla"><div class="tarjeta"><h3>Observa</h3><p>Lee el correo, los documentos y los datos de las herramientas que le autorizas.</p></div><div class="tarjeta"><h3>Actúa</h3><p>Redacta la respuesta, monta el presupuesto y genera el PDF listo para enviar.</p></div><div class="tarjeta"><h3>Coordina</h3><p>Avisa a la persona responsable, agenda la cita y hace el seguimiento.</p></div></div></div></section>
<section class="sec"><div class="w"><div class="cab"><p class="kicker">En cada puesto</p><h2>¿Qué hace PIX en cada departamento?</h2></div>
<p class="lead" style="max-width:780px;margin-bottom:20px">Cada departamento delega en PIX su parte más repetitiva: ofertas en comercial, facturas en administración, bandeja de entrada en atención al cliente y resúmenes en dirección.</p>
<div class="rejilla"><div class="tarjeta"><h3>Comercial</h3><p>De la petición del cliente al PDF de la oferta el mismo día, con recordatorios de seguimiento y un resumen cada semana.</p></div><div class="tarjeta"><h3>Administración</h3><p>Lee facturas, prepara los correos a proveedores, avisa de los vencimientos y entrega un informe semanal.</p></div><div class="tarjeta"><h3>Atención al cliente</h3><p>Ordena la bandeja, redacta las respuestas habituales, escala lo urgente y guarda el historial de cada cliente.</p></div><div class="tarjeta"><h3>Dirección</h3><p>En unas dos páginas: lo que se ha cerrado, lo que está bloqueado y lo que hay que decidir, con riesgos y seguimientos.</p></div></div></div></section>
<section class="sec sec-suave"><div class="w"><div class="cab"><p class="kicker">Primeros días</p><h2>¿Cómo empieza PIX a trabajar en tu empresa?</h2></div>
<p class="lead" style="max-width:780px;margin-bottom:20px">En días, no en un trimestre: se conecta a lo que ya usas, empieza por un proceso y en 48 horas lo ves funcionando; las dos primeras semanas sirven para medir tiempos reales.</p>
<div class="rejilla"><div class="tarjeta"><h3>1. Se conecta a tus herramientas</h3><p>Correo, Drive, CRM o tu programa de gestión. Nadie tiene que cambiar de correo ni de programas.</p></div><div class="tarjeta"><h3>2. Trabaja con tu aprobación</h3><p>Por defecto prepara y espera a que revises antes de enviar. Si quieres, decides qué puede enviar solo.</p></div><div class="tarjeta"><h3>3. Se mide y se amplía</h3><p>Se comparan los tiempos de antes y de después y, con datos, se suma el siguiente proceso o departamento.</p></div></div>
<ul class="lista" style="margin-top:22px"><li>Usa las herramientas que tu equipo ya tiene.</li><li>Ningún envío sale sin el visto bueno que tú definas.</li><li>Un solo agente al que le hablas, en lugar de un panel lleno de botones.</li></ul></div></section>
"""
_hub = """<section class="page-hero"><div class="w">{m}<p class="kicker">IA empresarial</p><h1>{h1}</h1><p class="lead">{lead}</p>
<div class="botones" style="margin-top:24px"><a class="btn btn-p" href="../../contacto.html?servicio=agentes-de-ia#diagnostico">Solicitar demo de PIX</a><a class="btn btn-s" href="implantacion-y-precios.html">Ver precios</a></div></div></section>
<section class="sec"><div class="w"><div class="resumen"><b>Respuesta rápida</b><p>{res}</p></div>
<h2>Dos capacidades, un mismo objetivo</h2><div class="rejilla" style="margin-top:20px"><a class="tarjeta" href="inteligencia-conectada.html"><h3>1. Inteligencia conectada</h3><p>Consulta la información real del negocio y la convierte en control, alertas, estadísticas, informes y decisiones accionables.</p><span class="mas">Ver inteligencia conectada →</span></a><a class="tarjeta" href="asistente-empresarial.html"><h3>2. Asistente que ejecuta</h3><p>Ejecuta tareas entre herramientas, mantiene el contexto y escala a una persona cuando el proceso lo necesita.</p><span class="mas">Ver el asistente →</span></a></div></div></section>
{imp}<section class="sec sec-suave"><div class="w"><div class="cab"><p class="kicker">El problema</p><h2>La empresa ya tiene datos. Lo que falta es que trabajen.</h2></div><div class="rejilla">{dol}</div><div class="resumen" style="margin-top:28px"><b>Con PIX</b><p>{con}</p></div></div></section>
<section class="sec"><div class="w"><div class="cab"><p class="kicker">Capacidades en acción</p><h2>Así convierte PIX una necesidad en acción</h2></div><div class="rejilla">{cap}</div><p class="mut" style="margin-top:18px">Diseñado para cada empresa · conectado a sus datos · supervisado por su equipo.</p></div></section>
<section class="sec sec-suave"><div class="w"><div class="cab"><p class="kicker">Todo sobre PIX</p><h2>Conoce PIX a fondo</h2></div><div class="rejilla">{mapa}</div></div></section>
<section class="sec"><div class="w"><div class="cab"><h2>Preguntas frecuentes sobre PIX</h2></div>{faq}</div></section>""".format(
    m=migas("../../", ("Servicios", "../index.html"), ("PIX", None)), h1=e(PIX_HUB["h1"]), lead=e(PIX_HUB["lead"]), res=e(PIX_HUB["resumen"]), dol=_dol, con=e(PIX_HUB["con_pix"]), cap=_cap, mapa=_mapa, faq=_faq_html(PIX_HUB["faqs"]), imp=_impacto)
pagina("servicios/pix/index.html", PIX_HUB["titulo"], PIX_HUB["meta"], _hub + cta("../../"), faqs=PIX_HUB["faqs"], ld_extra=_PIXAPP, extra_pagina={"mainEntity": {"@id": DOM + "/servicios/pix/#app"}})
for x in PIX_PAGINAS:
    cuerpo = '<div class="resumen"><b>Respuesta rápida</b><p>%s</p></div>' % e(x["resumen"])
    for h2, intro, items in x["secciones"]:
        cuerpo += '<h2 style="margin:32px 0 12px">%s</h2>' % e(h2)
        if intro: cuerpo += "<p>%s</p>" % e(intro)
        if items: cuerpo += '<div class="rejilla" style="margin-top:16px">%s</div>' % "".join('<div class="tarjeta"><h3>%s</h3><p>%s</p></div>' % (e(a), e(b)) for a, b in items)
    cuerpo += x.get("html", "")  # HTML propio (tablas, enlaces); solo lo usan páginas no indexadas
    html = """<section class="page-hero"><div class="w">{m}<p class="kicker">{k}</p><h1>{h1}</h1><p class="lead">{lead}</p></div></section>
<section class="sec"><div class="w lateral"><div class="lateral-main">{c}</div>{a}</div></section>
<section class="sec sec-suave"><div class="w"><div class="cab"><h2>Preguntas frecuentes</h2></div>{faq}</div></section>""".format(
        m=migas("../../", ("Servicios", "../index.html"), ("PIX", "index.html"), (x["nav"], None)), k=e(x["kicker"]), h1=e(x["h1"]), lead=e(x["lead"]), c=cuerpo, a=_pix_nav(x["slug"]), faq=_faq_html(x["faqs"]))
    pagina("servicios/pix/%s.html" % x["slug"], x["titulo"], x["meta"], html + cta("../../"), faqs=x["faqs"], extra_pagina={"about": {"@id": DOM + "/servicios/pix/#app"}})

# ---------- PRECIOS ----------
def _num(p): return p.replace(" €", "").replace(".", "")
_offers = []
for n, pr, d, dest in PACKS:
    sl = n.lower().replace(" ", "-").replace("á","a")
    srv = {"@type": "Service", "@id": DOM + "/precios#" + sl, "name": n, "description": d, "provider": {"@id": DOM + "/#org"}, "areaServed": "ES"}
    of = {"@type": "Offer", "@id": DOM + "/precios#offer-" + sl, "name": "Pack " + n, "availability": "https://schema.org/InStock", "url": DOM + "/precios", "seller": {"@id": DOM + "/#org"}, "itemOffered": srv}
    if pr == "A medida":
        continue
    else:
        v = _num(pr); of.update({"price": v, "priceCurrency": "EUR", "priceSpecification": [
            {"@type": "UnitPriceSpecification", "price": v, "priceCurrency": "EUR", "valueAddedTaxIncluded": False},
            {"@type": "UnitPriceSpecification", "price": "40", "priceCurrency": "EUR", "valueAddedTaxIncluded": False, "unitCode": "MON", "referenceQuantity": {"@type": "QuantitativeValue", "value": 1, "unitCode": "MON"}, "name": "Soporte y mantenimiento"}]})
    _offers.append(of)
_cat = {"@type": "OfferCatalog", "@id": DOM + "/precios#packs", "name": "Precios y packs", "url": DOM + "/precios", "itemListElement": _offers}
pagina("precios.html", "Precios y packs de software, IA y webs · Studio Emprende", "Packs para empezar desde 990 € más 40 €/mes de soporte, o arma tu propio pack con solo lo que necesitas.",
       '<section class="page-hero"><div class="w">%s<h1>Precios y packs</h1><p class="lead">Pago único por el pack y una cuota de 40 € al mes de soporte y mantenimiento. Precios sin IVA, vigentes desde octubre de 2026.</p><p class="mut" style="font-size:14px;margin-top:10px">Última revisión de precios: <time datetime="2026-10-20">20 de octubre de 2026</time>.</p></div></section><section class="sec"><div class="w"><h2 style="margin-bottom:24px">Packs para empezar</h2>%s</div></section>%s<section class="sec sec-suave"><div class="w"><div class="cab"><h2>Preguntas frecuentes</h2></div>%s</div></section>%s'
       % (migas("", ("Precios", None)), packs(""), FORM.banda_precios(), faq(), cta("")), ld_extra=_cat, extra_pagina={"mainEntity": {"@id": DOM + "/precios#packs"}})

# ---------- NORMATIVAS ----------
REV_FECHA = "2026-10-12"
def _fila_norm(n):
    a, b, c, d = n; x = NORM_EXTRA[a]
    ref = ", ".join('<a href="%s" target="_blank" rel="noopener">%s</a>' % (u, e(t)) for t, u in x["fuentes"])
    enl = " · ".join('<a href="%s">%s</a>' % (h, e(t)) for h, t in x["enlaces"])
    return '<tr><td><b style="font-weight:500">%s</b></td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (e(a), e(x["afecta"]), e(c), ref, enl)
filas = "".join(_fila_norm(n) for n in NORMATIVAS)
_leg = [{"@type": "Legislation", "name": t, "legislationIdentifier": t, "url": u} for n in NORMATIVAS for t, u in NORM_EXTRA[n[0]]["fuentes"]]
pagina("normativas.html", "Normativas 2026-2027 para empresas · Studio Emprende", "Verifactu, factura electrónica, registro de jornada, AI Act, accesibilidad, NIS2 y más: qué es, a quién afecta y cuándo.",
       '<section class="page-hero"><div class="w">%s<h1>Normativas que afectan a tu empresa</h1><p class="lead">Resumen de las leyes que más preguntan nuestros clientes: a quién afectan, plazos y enlace al texto oficial (BOE o EUR-Lex).</p><p class="mut" style="font-size:14px;margin-top:10px">Revisado por el equipo de Studio Emprende el <time datetime="%s">12 de octubre de 2026</time>.</p></div></section><section class="sec"><div class="w"><h2 style="margin-bottom:18px">Plazos y obligaciones 2026-2027</h2><div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Norma</th><th>A quién afecta</th><th>Estado y plazos</th><th>Texto oficial</th><th>Cómo cumplir</th></tr></thead><tbody>%s</tbody></table></div><p class="mut" style="margin-top:16px;font-size:14px">Esta página es informativa y no sustituye el asesoramiento legal. Consulta siempre la fuente oficial.</p></div></section>%s'
       % (migas("", ("Normativas", None)), REV_FECHA, filas, cta("")), fecha=REV_FECHA, extra_pagina={"mentions": _leg, "reviewedBy": {"@id": DOM + "/#org"}, "lastReviewed": REV_FECHA})

# ---------- SECTORES ----------
SECT_TXT = {
 "Talleres": ("Órdenes de reparación en papel, presupuestos que no se aprueban y facturas que tienen que cumplir Verifactu.", "Programa de gestión de taller con órdenes, fotos del vehículo y aviso por WhatsApp cuando el coche está listo; facturación preparada para Verifactu.", "normativas.html"),
 "Clínicas": ("Agenda llena de huecos por citas olvidadas y fichas de paciente repartidas entre papel y Excel.", "Agenda online con recordatorios automáticos por WhatsApp, ficha de paciente digital y cobros registrados en el mismo programa.", None),
 "Reformas e instaladores": ("Presupuestos que tardan días, partes de trabajo a mano y obras sin saber si dan beneficio.", "Presupuestos con plantillas, partes desde el móvil con fotos y firma del cliente, y control de horas y materiales por obra.", None),
 "Hostelería": ("Registros APPCC en papel, turnos que cambian cada semana y reservas por teléfono que se pierden.", "APPCC digital desde el móvil, fichaje del personal y reservas online con confirmación automática.", "blog/appcc-digital-hosteleria.html"),
 "Inmobiliarias": ("Contactos de portales que nadie contesta a tiempo y fichas de inmuebles duplicadas en varias webs.", "CRM inmobiliario que recoge los contactos de los portales, responde al momento con IA y agenda visitas.", None),
 "Academias": ("Matrículas, cobros mensuales y listas de asistencia gestionados a mano.", "Matrícula online, recibos domiciliados con aviso de impago y asistencia desde el móvil del profesor.", None),
 "Asesorías energéticas": ("Comparativas de tarifas en Excel y renovaciones de contratos que se escapan.", "Programa de gestión de clientes y contratos con alertas de renovación y comparativas en un clic.", None),
 "Alojamientos turísticos": ("Registro de viajeros obligatorio, check-in en persona y llaves que hay que entregar.", "Check-in online con envío automático del registro de viajeros, cerraduras inteligentes y mensajes al huésped.", "normativas.html"),
 "Gestorías": ("Documentación que llega por correo, WhatsApp y en papel, y plazos fiscales que hay que vigilar uno a uno.", "Portal del cliente para subir documentos, avisos de vencimientos y respuestas automáticas a las preguntas frecuentes.", None),
 "Comercios": ("Ventas de tienda y online por separado, stock que no cuadra y poca visibilidad en Google.", "TPV y tienda online conectados al mismo stock, ficha de Google Business optimizada y campañas a clientes habituales.", None),
 "Distribuidores": ("Pedidos por teléfono y WhatsApp que hay que pasar a mano y rutas de reparto sin planificar.", "Portal de pedidos para tus clientes, albaranes y facturas automáticos y control de rutas y entregas.", None),
 "Industria": ("Producción controlada en hojas de cálculo y mantenimiento que se hace cuando algo se rompe.", "ERP con órdenes de fabricación, trazabilidad de lotes y mantenimiento preventivo con avisos.", None),
}
def _tarj_sect(s):
    sl = s.lower().replace(" ", "-"); prob, sol, enl = SECT_TXT[s]
    extra = ' <a href="%s">Más información →</a>' % enl if enl else ""
    return '<div class="tarjeta" id="%s"><h3>%s</h3><p><b style="font-weight:500">El problema:</b> %s</p><p><b style="font-weight:500">Cómo lo resolvemos:</b> %s%s</p><a class="mas" href="contacto.html?sector=%s#diagnostico">Pedir propuesta para %s →</a></div>' % (sl, s, e(prob), e(sol), extra, sl, s.lower())
sect = "".join(_tarj_sect(s) for s in SECTORES)
pagina("sectores.html", "Software, IA y webs por sector · Studio Emprende", "Software de gestión, IA y webs adaptados a talleres, clínicas, reformas, hostelería, inmobiliarias y más: problema típico y cómo lo resolvemos.",
       '<section class="page-hero"><div class="w">%s<h1>Software, IA y webs para tu sector</h1><p class="lead">Partimos de lo que ya funciona en tu sector y lo adaptamos a tu forma de trabajar.</p></div></section><section class="sec"><div class="w"><div class="rejilla" style="margin-bottom:36px"><div class="tarjeta"><b style="font-size:30px;font-weight:500;color:var(--burdeos)">12</b><p>sectores con solución adaptada</p></div><div class="tarjeta"><b style="font-size:30px;font-weight:500;color:var(--burdeos)">990 €</b><p>pack de inicio, + 40 €/mes de soporte (sin IVA)</p></div><div class="tarjeta"><b style="font-size:30px;font-weight:500;color:var(--burdeos)">2-3 semanas</b><p>para tener el pack de inicio en marcha</p></div><div class="tarjeta"><b style="font-size:30px;font-weight:500;color:var(--burdeos)">90 €/mes</b><p>PIX, el agente de IA, para 3 personas</p></div></div><h2 style="margin-bottom:24px">Problemas típicos y cómo los resolvemos</h2><div class="rejilla">%s</div></div></section>%s' % (migas("", ("Sectores", None)), sect, cta("")), tipo_pagina="CollectionPage")

# ---------- CONTACTO ----------
opts = "".join('<option value="%s">%s</option>' % (s[0], e(s[2])) for s in SECCIONES)
contacto = """<section class="page-hero"><div class="w">{m}<h1>Hablemos de tu negocio</h1><p class="lead">Cuéntanos qué necesitas y te respondemos con un diagnóstico gratuito y una propuesta clara. Si ya sabes lo que buscas, mira antes los <a href="precios.html">precios y packs</a> o nuestros servicios de <a href="servicios/software-de-gestion.html">software de gestión</a>, <a href="servicios/webs.html">webs con SEO</a> y <a href="servicios/agentes-de-ia.html">agentes de IA</a>.</p></div></section>
<section class="sec" id="diagnostico"><div class="w lateral"><div class="lateral-main">
<form class="form" data-contacto action="https://formsubmit.co/info@studioemprende.com" method="post">
<input type="hidden" name="_subject" value="Nuevo contacto desde studioemprende.com">
<input type="hidden" name="_cc" value="socialstudioemprende@gmail.com">
<input type="hidden" name="_template" value="table">
<input type="hidden" name="_next" value="{dom}/gracias.html">
<input type="hidden" name="funcion" id="funcion" value="">
<input type="hidden" name="_captcha" value="true">
<input type="hidden" name="_blacklist" value="viagra, casino, crypto, bitcoin, forex, loan, seo services, backlinks, porn, betting, http://, https://bit.ly">
<input type="hidden" name="_autoresponse" value="Hola, hemos recibido tu mensaje en Studio Emprende. Te respondemos en menos de 24 horas laborables. Si es urgente, escríbenos por WhatsApp al 601 86 96 68.">
<input type="hidden" name="_t" id="_t" value="">
<div aria-hidden="true" style="position:absolute;left:-10000px;top:auto;width:1px;height:1px;overflow:hidden"><label>No rellenar<input type="text" name="_honey" tabindex="-1" autocomplete="off"></label><label>Web<input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
<p class="form-aviso" id="form-aviso" role="alert" hidden></p>
<div class="dos"><div class="campo"><label for="nombre">Nombre</label><input id="nombre" name="nombre" autocomplete="name" required minlength="2" maxlength="80" pattern="[A-Za-zÀ-ÿñÑ' .-]{{2,80}}"><span class="error" hidden style="color:#A3222F;font-size:13px">Escribe tu nombre</span></div>
<div class="campo"><label for="telefono">Teléfono</label><input id="telefono" name="telefono" type="tel" autocomplete="tel" required inputmode="tel" maxlength="20" pattern="[+0-9 ()-]{{9,20}}"><span class="error" hidden style="color:#A3222F;font-size:13px">Escribe tu teléfono</span></div></div>
<div class="dos"><div class="campo"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" required maxlength="120"><span class="error" hidden style="color:#A3222F;font-size:13px">Escribe tu email</span></div>
<div class="campo"><label for="empresa">Empresa (opcional)</label><input id="empresa" name="empresa" autocomplete="organization" maxlength="120"></div></div>
<div class="campo"><label for="servicio">¿Qué te interesa?</label><select id="servicio" name="servicio"><option value="">Aún no lo sé, quiero el diagnóstico</option>{o}</select></div>
<div class="campo"><label for="mensaje">Cuéntanos tu caso</label><textarea id="mensaje" name="mensaje" rows="5" maxlength="2000"></textarea></div>
<label style="display:flex;gap:10px;font-size:14px;align-items:flex-start"><input type="checkbox" name="privacidad" required style="margin-top:4px"> He leído y acepto la <a href="privacidad.html">política de privacidad</a>.</label>
<div><button class="btn btn-p" type="submit">Enviar y recibir mi diagnóstico</button></div>
</form></div>
<aside class="lateral-aside"><h2 style="font-size:22px;color:#fff">Otras formas de contacto</h2><p style="color:#C9C1BB"><a style="color:#fff" href="https://wa.me/34601869668?text=Hola%2C%20quiero%20pedir%20mi%20diagn%C3%B3stico%20gratis" target="_blank" rel="noopener">WhatsApp: 601 86 96 68</a><br><a style="color:#fff" href="mailto:info@studioemprende.com">info@studioemprende.com</a></p><p style="color:#C9C1BB">Respondemos en menos de 24 horas laborables.</p></aside>
</div></section>""".format(m=migas("", ("Contacto", None)), o=opts, dom=DOM)
pagina("contacto.html", "Contacto y diagnóstico gratis · Studio Emprende", "Pide tu diagnóstico gratuito: te decimos qué puedes automatizar y digitalizar en tu negocio.", contacto, tipo_pagina="ContactPage")

pagina("gracias.html", "Mensaje recibido · Studio Emprende", "Hemos recibido tu mensaje. Te respondemos en menos de 24 horas laborables; si es urgente, escríbenos por WhatsApp al 601 86 96 68.",
       '<section class="sec"><div class="w" style="text-align:center;display:flex;flex-direction:column;gap:18px;align-items:center"><img src="assets/img/simbolo.svg" alt="" width="70" height="101"><h1>¡Gracias! Hemos recibido tu mensaje</h1><p class="lead">Te respondemos en menos de 24 horas laborables. Si es urgente, escríbenos por WhatsApp.</p><div class="botones"><a class="btn btn-p" href="https://wa.me/34601869668" target="_blank" rel="noopener">Escribir por WhatsApp</a><a class="btn btn-s" href="index.html">Volver al inicio</a></div></div></section>', indexar=False)

# ---------- SOBRE NOSOTROS ----------
pagina("sobre-nosotros.html", "Sobre nosotros · Studio Emprende", "Studio Emprende ayuda a emprendedores y pymes con software, IA y webs, 100 % online.",
       '<section class="page-hero"><div class="w">%s<h1>Sobre nosotros</h1><p class="lead">Ayudamos a quien emprende a tener un negocio ordenado, visible y automatizado desde el primer día.</p></div></section><section class="sec"><div class="w rejilla"><div class="tarjeta"><h3>Un interlocutor fijo</h3><p>Hablas siempre con la misma persona, que conoce tu negocio.</p></div><div class="tarjeta"><h3>Plazos por escrito</h3><p>Cada propuesta lleva sus fases y fechas antes de empezar.</p></div><div class="tarjeta"><h3>100 %% online</h3><p>Trabajamos con negocios de toda España.</p></div></div></div>%s</section>%s%s' % (migas("", ("Sobre nosotros", None)), HIST, FORM.equipo_html(""), cta("")), tipo_pagina="AboutPage", ld_extra=FORM.JORDAN)

pagina("partners.html", PT.TITULO + " · Studio Emprende", PT.META, PT.html(migas("", ("Partners", None)), _faq_html(PT.FAQS), DOM) + cta(""), faqs=PT.FAQS)

# ---------- CASOS DE ÉXITO (/casos/) ----------
open(OUT + "/assets/js/casos.js", "w").write(open(os.path.join(AQUI, "casos.js")).read())
_CL = CS.CONTRATALUX
pagina("casos/index.html", "Casos de éxito de software, webs y SEO · Studio Emprende", "Casos reales de Studio Emprende: qué hicimos, en qué orden y con qué datos. Marca, web con SEO, indexación, redes y programas de gestión a medida.",
       CS.html_hub("../", migas("../", ("Casos de éxito", None)), [_CL], cta("../")), css="casos.css", og=DOM + "/" + CS.MEDIA + "contratalux-og.jpg")
pagina("casos/%s.html" % _CL["slug"], _CL["titulo"], _CL["meta"],
       CS.html_caso(_CL, "../", migas("../", ("Casos de éxito", "index.html"), (_CL["nombre"], None)), _faq_html(CS.FAQS), cta("../")),
       ld_extra=CS.ld_caso(_CL, DOM), tipo="article", faqs=CS.FAQS, css="casos.css", og=DOM + "/" + CS.MEDIA + "contratalux-og.jpg",
       extra_pagina={"mainEntity": {"@id": DOM + "/casos/%s#caso" % _CL["slug"]}, "datePublished": _CL["fecha"]})

LEG = {"aviso-legal": AVISO, "privacidad": PRIVACIDAD, "cookies": COOKIES}
# ---------- LEGALES ----------
for slug, t in [("aviso-legal", "Aviso legal"), ("privacidad", "Política de privacidad"), ("cookies", "Política de cookies")]:
    _tl = {"aviso-legal": "Aviso legal y datos de la empresa · Studio Emprende", "privacidad": "Política de privacidad y protección de datos · Studio Emprende", "cookies": "Política de cookies y cómo gestionarlas · Studio Emprende"}[slug]
    _ctx = {"aviso-legal": 'Aquí tienes los datos de la empresa titular de Studio Emprende y las condiciones de uso de la web. Para saber cómo tratamos tus datos, consulta la <a href="privacidad.html">política de privacidad</a>; si prefieres hablar con nosotros, tienes todas las vías en <a href="contacto.html">contacto</a>.',
            "privacidad": 'Esta política explica qué datos recogemos cuando nos escribes o pides un <a href="contacto.html#diagnostico">diagnóstico gratis</a>, para qué los usamos y cómo ejercer tus derechos. Las cookies tienen su propia <a href="cookies.html">política de cookies</a>, y los datos de la empresa están en el <a href="aviso-legal.html">aviso legal</a>.',
            "cookies": 'Esta página detalla qué cookies usa la web, para qué sirven y cómo cambiar tu elección. El tratamiento del resto de tus datos se explica en la <a href="privacidad.html">política de privacidad</a>, y quién está detrás de la web, en <a href="sobre-nosotros.html">sobre nosotros</a>.'}[slug]
    pagina(slug + ".html", _tl, t + " de Studio Emprende.",
           '<section class="page-hero"><div class="w">%s<h1>%s</h1></div></section><section class="sec"><div class="w legal-txt"><p class="mut">Última actualización: octubre de 2026.</p><p>%s</p>%s</div></section>' % (migas("", (t, None)), t, _ctx, LEG[slug]))

pagina("404.html", "Página no encontrada · Studio Emprende", "La página que buscas no existe.",
       '<section class="sec"><div class="w" style="text-align:center;display:flex;flex-direction:column;gap:18px;align-items:center"><img src="assets/img/simbolo.svg" alt="" width="70" height="101"><h1>Esta página no existe</h1><p class="lead">Puede que el enlace haya cambiado.</p><div class="botones"><a class="btn btn-p" href="index.html">Ir al inicio</a><a class="btn btn-s" href="mapa-web.html">Ver el mapa de la web</a></div></div></section>', indexar=False)

# ---------- BLOG ----------
pagina("blog/index.html", "Blog · Studio Emprende", "Artículos sobre gestión, normativas, IA y webs para autónomos y pymes.",
       '<section class="page-hero"><div class="w">%s<h1>Blog</h1><p class="lead">Ideas claras sobre gestión, normativas, inteligencia artificial y webs, sin tecnicismos.</p><p class="firma">Escritos y revisados por el equipo de Studio Emprende. <a href="../politica-editorial.html">Lee nuestra política editorial</a>.</p></div></section><section class="sec"><div class="w"><div class="rejilla">%s</div></div></section>%s' % (migas("../", ("Blog", None)), "".join(tarjeta_blog(a, "") for a in ARTICULOS), cta("../")))
_BN = {a[0] for a in BN.ARTICULOS}  # artículos nuevos: fuera de portada, índice, mapa web y "otros artículos" de los demás
for slug, titulo, desc, fecha, cat, serv_rel, cuerpo in ARTICULOS + BN.ARTICULOS:
    sr = [x for x in SECCIONES if x[0] == serv_rel][0]
    if slug in _BN:
        otros = "".join([tarjeta_blog(a, "") for a in sorted(ARTICULOS, key=lambda a: a[4] != cat)][:3])
    else:
        otros = "".join([tarjeta_blog(a, "") for a in ARTICULOS if a[0] != slug][:3])
    ld = ""
    _fq = FAQS_BLOG.get(slug)
    if _fq: cuerpo = cuerpo + '<h2>Preguntas frecuentes</h2>' + _faq_html(_fq)
    _d, _mm, _y = fecha.split(); _fp = "%s-%02d-%02d" % (_y, ["ene","feb","mar","abr","may","jun","jul","ago","sep","oct","nov","dic"].index(_mm) + 1, int(_d))
    _fd = "__FMOD__"
    _url = "%s/blog/%s" % (DOM, slug)
    _res = RB.RESUMEN.get(slug)
    if _res: cuerpo = '<div class="resumen"><b>En resumen</b><p>%s</p></div>' % e(_res) + cuerpo
    bp = {"@type": "BlogPosting", "@id": _url + "#article", "headline": titulo, "description": desc, "inLanguage": "es", "articleSection": cat, "datePublished": _fp, "dateModified": _fd,
          "image": ["%s/assets/img/blog/%s.jpg" % (DOM, slug), "%s/assets/img/blog/og/%s.jpg" % (DOM, slug)], "author": {"@id": DOM + "/#org"}, "publisher": {"@id": DOM + "/#org"},
          "mainEntityOfPage": {"@id": _url}}
    html = """<section class="page-hero"><div class="w">{m}<p class="kicker">{cat} · <time datetime="{fiso}">{f}</time></p><h1>{t}</h1><p class="lead">{d}</p><p class="firma">Por el <a href="../sobre-nosotros.html#equipo">equipo de Studio Emprende</a> · Actualizado el <!--FECHA_ACT-->{rev} · <a href="../politica-editorial.html">Cómo escribimos y revisamos</a></p></div></section>
<section class="sec"><div class="w lateral"><article class="lateral-main articulo">{fp}{c}</article>
<aside class="lateral-aside"><h3>{st}</h3><p style="color:#C9C1BB">{si}</p><a class="btn btn-claro" href="../servicios/{ss}.html">Ver el servicio</a><a class="btn btn-borde-claro" href="../contacto.html?servicio={ss}#diagnostico">Pedir diagnóstico</a></aside></div></section>
<section class="sec sec-suave"><div class="w"><div class="cab"><p class="kicker">Sigue leyendo</p><h2>Otros artículos</h2></div><div class="rejilla">{o}</div></div></section>{ld}""".format(fp=foto_blog(slug, ALT.get(slug, titulo), True), 
        m=migas("../", ("Blog", "index.html"), (titulo, None)), cat=e(cat), f=fecha, fiso=_fp, rev=(' · Normativa revisada el <time datetime="%s">%s</time>' % (REV_FECHA, "12 de octubre de 2026")) if cat == "Normativas" else "", t=e(titulo), d=e(desc), c=cuerpo, sl=slug, st=e(sr[2]), si=e(sr[3]), ss=serv_rel, o=otros, ld=ld)
    pagina("blog/%s.html" % slug, "%s · Studio Emprende" % titulo, desc, html + cta("../"), ld_extra=bp, tipo="article", og=DOM + "/assets/img/blog/og/%s.jpg" % slug, faqs=_fq, tipo_pagina="WebPage", extra_pagina={"mainEntity": {"@id": _url + "#article"}})

# ---------- TEMAS DEL BLOG (/temas/) ----------
_TODOS = {a[0]: a for a in ARTICULOS + BN.ARTICULOS}
pagina("temas/index.html", "Temas del blog de Studio Emprende", "Los artículos del blog de Studio Emprende ordenados por tema: inteligencia artificial, gestión y CRM, normativas, formación, webs y emprender.",
       TM.html_hub("../", migas("../", ("Temas del blog", None)), cta("../")), tipo_pagina="CollectionPage")
for _t in TM.TEMAS:
    _arts = [_TODOS[x] for x in _t[4] if x in _TODOS]
    _il = {"@type": "ItemList", "@id": "%s/temas/%s#lista" % (DOM, _t[0]), "itemListElement": [{"@type": "ListItem", "position": i, "url": "%s/blog/%s" % (DOM, a[0]), "name": a[1]} for i, a in enumerate(_arts, 1)]}
    pagina("temas/%s.html" % _t[0], _t[1], _t[2], TM.html_tema("../", migas("../", ("Temas del blog", "index.html"), (_t[1], None)), _t, "".join(tarjeta_blog(a, "../blog/") for a in _arts), cta("../")),
           ld_extra=_il, tipo_pagina="CollectionPage", extra_pagina={"mainEntity": {"@id": "%s/temas/%s#lista" % (DOM, _t[0])}})

# ---------- GUIAS ----------
GD = {g[0]: g for g in GUIAS}
SD = {x[0]: x for x in SECCIONES}
AD = {a[0]: a for a in ARTICULOS}
def tarjeta_guia(g, pre=""):
    return '<a class="tarjeta" href="%s%s.html"><span class="etiqueta">%s</span><h3>%s</h3><p>%s</p><span class="mas">Leer guía →</span></a>' % (pre, g[0], e(dict(GRUPOS)[g[1]]), e(g[4]), e(g[3][:130].rsplit(" ", 1)[0] + "…"))
hubg = ""
for k, n in GRUPOS:
    hubg += '<div class="cab" style="margin:40px 0 20px"><p class="kicker">%s</p></div><div class="rejilla">%s</div>' % (n, "".join(tarjeta_guia(g) for g in GUIAS if g[1] == k))
pagina("guias/index.html", "Guías para emprender · Studio Emprende", "Guías claras para emprender en España: qué es un emprendedor, cómo montar un negocio, ayudas, financiación, registro de empresa y cómo crear tu web.",
       '<section class="page-hero"><div class="w">%s<h1>Guías para emprender</h1><p class="lead">Respuestas directas a lo que más se pregunta al empezar un negocio en España, enlazadas a los servicios que lo resuelven.</p></div></section><section class="sec" style="padding-top:24px"><div class="w">%s</div></section>%s' % (migas("../", ("Guías", None)), hubg, cta("../")))
for slug, grupo, titulo, meta, h1, resumen, secciones, faqs, servs, blogs, rel in GUIAS:
    secs = "".join("<h2>%s</h2>%s" % (e(h), c) for h, c in secciones)
    faqh = '<h2>Preguntas frecuentes</h2><div class="faq">' + "".join("<details><summary>%s</summary><p>%s</p></details>" % (e(q), e(a)) for q, a in faqs) + "</div>"
    indice = '<nav class="indice" aria-label="En esta guía"><b>En esta guía</b>' + "".join('<a href="#s%d">%s</a>' % (i, e(h)) for i, (h, c) in enumerate(secciones)) + "</nav>"
    secs = "".join('<h2 id="s%d">%s</h2>%s' % (i, e(h), c) for i, (h, c) in enumerate(secciones))
    sv = [SD[x] for x in servs if x in SD]
    aside = '<aside class="lateral-aside"><h3>Te ayudamos con esto</h3>%s<a class="btn btn-claro" href="../contacto.html?servicio=%s#diagnostico">Pedir diagnóstico gratis</a></aside>' % ("".join('<a href="../servicios/%s.html" style="color:#fff">%s →</a>' % (x[0], e(x[2])) for x in sv), servs[0])
    relh = "".join(tarjeta_guia(GD[x]) for x in rel if x in GD)
    blogh = "".join(tarjeta_blog(AD[b], "../blog/") for b in blogs if b in AD).replace('src="../../assets', 'src="../assets')
    html = """<section class="page-hero"><div class="w">{m}<p class="kicker">Guía · {gn}</p><h1>{h1}</h1><p class="lead">{lead}</p><p class="firma">Por el <a href="../sobre-nosotros.html#equipo">equipo de Studio Emprende</a> · Actualizado el <!--FECHA_ACT--> · <a href="../politica-editorial.html">Cómo escribimos y revisamos</a></p></div></section>
<section class="sec"><div class="w lateral"><article class="lateral-main articulo"><div class="resumen"><b>Respuesta rápida</b><p>{res}</p></div>{ind}{secs}{faq}</article>{aside}</div></section>
<section class="sec sec-suave"><div class="w"><div class="cab"><p class="kicker">Sigue aprendiendo</p><h2>Guías relacionadas</h2></div><div class="rejilla">{rel}</div>{blog}</div></section>""".format(
        m=migas("../", ("Guías", "index.html"), (h1, None)), gn=e(dict(GRUPOS)[grupo]), h1=e(h1), res=e(resumen), ind=indice, lead=e(meta), secs=secs, faq=faqh, aside=aside, rel=relh,
        blog=('<div class="cab" style="margin:40px 0 20px"><p class="kicker">Del blog</p></div><div class="rejilla">%s</div>' % blogh) if blogh else "")
    art = {"@type": "Article", "headline": h1, "description": meta, "inLanguage": "es", "author": {"@id": DOM + "/#org"}, "publisher": {"@id": DOM + "/#org"},
           "@id": "%s/guias/%s#article" % (DOM, slug), "datePublished": "2026-10-12", "dateModified": "__FMOD__", "mainEntityOfPage": {"@id": "%s/guias/%s" % (DOM, slug)}, "image": DOM + "/assets/img/og-imagen.png",
           "abstract": resumen}
    pagina("guias/%s.html" % slug, titulo, meta, html + cta("../"), ld_extra=art, tipo="article", faqs=faqs, extra_pagina={"mainEntity": {"@id": "%s/guias/%s#article" % (DOM, slug)}})

# ---------- MAPA ----------
grupos = [("Principal", [("Inicio", "index.html"), ("Servicios", "servicios/index.html"), ("Precios y packs", "precios.html"), ("Sectores", "sectores.html"), ("Normativas", "normativas.html"), ("Sobre nosotros", "sobre-nosotros.html"), ("Programa de partners", "partners.html"), ("Política editorial", "politica-editorial.html"), ("Contacto y diagnóstico", "contacto.html")])]
for k, n in MENU:
    grupos.append((n, [(s[2], "servicios/%s.html" % s[0]) for s in by_menu(k)]))
grupos.append(("Guías para emprender", [("Todas las guías", "guias/index.html")] + [(g[4], "guias/%s.html" % g[0]) for g in GUIAS]))
grupos.append(("Blog", [("Todos los artículos", "blog/index.html")] + [(a[1], "blog/%s.html" % a[0]) for a in ARTICULOS]))
grupos.append(("Legal", [("Aviso legal", "aviso-legal.html"), ("Privacidad", "privacidad.html"), ("Cookies", "cookies.html")]))
mapa = '<div class="mapa-raiz"><a href="index.html">STUDIO EMPRENDE</a></div><div class="mapa">' + "".join('<div class="grupo"><h3>%s</h3>%s</div>' % (g, "".join('<a href="%s">%s</a>' % (h, e(t)) for t, h in ls)) for g, ls in grupos) + "</div>"
# ---------- POLÍTICA EDITORIAL ----------
_PE = """<section class="page-hero"><div class="w">%s<h1>Política editorial</h1><p class="lead">Cómo escribimos, revisamos y corregimos los artículos del blog y las guías de Studio Emprende.</p></div></section>
<section class="sec"><div class="w"><div class="texto-largo">
<h2>¿Quién escribe los artículos y las guías?</h2><p>Los escribe el equipo de Studio Emprende, la marca de INTELIGENCIA SEVILLA SL que desarrolla software de gestión, agentes de IA y webs. Usamos herramientas de inteligencia artificial como apoyo en la redacción, y una persona del equipo revisa cada texto antes de publicarlo. Puedes ver quiénes somos en <a href="sobre-nosotros.html">sobre nosotros</a>.</p>
<h2>¿Cómo comprobamos los datos legales y los plazos?</h2><p>Cada obligación y cada fecha se contrasta con la fuente oficial: el <a href="https://www.boe.es/" target="_blank" rel="noopener">BOE</a>, la sede de la Agencia Tributaria o <a href="https://eur-lex.europa.eu/" target="_blank" rel="noopener">EUR-Lex</a> para las normas europeas. Enlazamos la norma en el propio texto y reunimos todas, con su fecha de revisión, en la página de <a href="normativas.html">normativas 2026-2027</a>. Cuando un plazo está anunciado pero no publicado en el BOE, lo decimos así.</p>
<h2>¿Los ejemplos son casos reales?</h2><p>No. Cuando un artículo pone un ejemplo de un taller, una clínica o una academia, es un caso hipotético para explicar cómo funciona algo. No publicamos datos de clientes sin su permiso por escrito, ni testimonios ni cifras que no podamos demostrar.</p>
<h2>¿Cada cuánto se actualizan?</h2><p>Revisamos los textos cuando cambia una norma, una herramienta o un plazo. Cada página muestra la fecha de su última actualización, y los artículos de normativa indican además cuándo se revisaron los plazos legales.</p>
<h2>¿Por qué hablamos de nuestros servicios?</h2><p>Studio Emprende vende software, IA y webs, y algunos artículos enlazan a esos servicios cuando encajan con lo que se explica. La información de los artículos es válida aunque no nos contrates.</p>
<h2>¿Has visto un error?</h2><p>Escríbenos a <a href="mailto:info@studioemprende.com">info@studioemprende.com</a> indicando la página y el dato. Lo revisamos y, si hay que corregirlo, actualizamos el texto y su fecha.</p>
</div></div></section>"""
pagina("politica-editorial.html", "Política editorial: cómo escribimos y revisamos · Studio Emprende", "Cómo redacta, revisa y corrige Studio Emprende los artículos del blog y las guías: fuentes oficiales, fechas de revisión y correo para avisar de errores.", _PE % migas("", ("Política editorial", None)) + cta(""))

pagina("mapa-web.html", "Mapa de la web · Studio Emprende", "Todas las páginas de Studio Emprende.", '<section class="page-hero"><div class="w">%s<h1>Mapa de la web</h1><p class="lead">Todas las páginas y cómo se organizan.</p></div></section><section class="sec"><div class="w">%s</div></section>' % (migas("", ("Mapa de la web", None)), mapa))

# ---------- SEO ----------
import datetime as _dt
HOY = _dt.date.today().isoformat()
import hashlib as _hl
_FP = os.path.join(AQUI, "fechas.json")
try: _FECH = _json.load(open(_FP))
except Exception: _FECH = {}
LASTMOD = {}
for p in PAGS:
    h = _hl.sha1(open(os.path.join(OUT, p), "rb").read()).hexdigest()
    if _FECH.get(p, [None])[0] != h: _FECH[p] = [h, _dt.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")]
    if len(_FECH[p][1]) == 10: _FECH[p][1] += "T12:00:00"
    LASTMOD[p] = _FECH[p][1][:10]
_json.dump({k: _FECH[k] for k in sorted(_FECH) if k in LASTMOD}, open(_FP, "w"), indent=0)
# Fechas reales: "__FMOD__" (JSON-LD) y <!--FECHA_ACT--> (texto visible) = última modificación real del contenido
_MESES = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
def _fh(iso):
    _y, _m, _d = iso.split("-"); return "%d de %s de %s" % (int(_d), _MESES[int(_m) - 1], _y)
for p in PAGS:
    _f = os.path.join(OUT, p); _t = open(_f, encoding="utf-8").read()
    if "__FMOD__" in _t or "<!--FECHA_ACT-->" in _t:
        _t = _t.replace("__FMOD__", LASTMOD[p]).replace("<!--FECHA_ACT-->", '<time datetime="%s">%s</time>' % (LASTMOD[p], _fh(LASTMOD[p])))
        open(_f, "w", encoding="utf-8").write(_t)
# Un sitemap por familia de servicio (hub + sus funciones) para ver la indexación sección a sección en Search Console
def _grupo(p):
    if p.startswith("blog/"): return "blog"
    if p.startswith("guias/"): return "guias"
    if p.startswith("casos/"): return "casos"
    if p.startswith("temas/"): return "temas"
    if p.startswith("servicios/") and p != "servicios/index.html": return "servicios-" + p.split("/")[1].replace(".html", "")
    return "paginas"
PRIO = {"guias": "0.8", "paginas": "0.8", "blog": "0.7", "casos": "0.8", "temas": "0.6"}
SMS = []
_GRUPOS = ["paginas", "casos", "temas", "guias", "blog"] + sorted({_grupo(p) for p in PAGS if _grupo(p).startswith("servicios-")})
for g in _GRUPOS:
    xs = ""
    # el hub de la familia va primero
    for p in sorted(PAGS, key=lambda q: q.count("/") > 1) if g.startswith("servicios-") else sorted(PAGS, key=lambda q: not q.endswith("index.html")) if g in ("casos", "temas") else PAGS:
        if p in NOINDEX or p in CANON or _grupo(p) != g: continue
        img = ""
        if g == "blog" and p != "blog/index.html":
            img = "<image:image><image:loc>%s/assets/img/blog/%s.jpg</image:loc></image:image>" % (DOM, p[5:-5])
        pr = "1.0" if p == "index.html" else PRIO.get(g, "0.9" if p.count("/") == 1 else "0.6")
        xs += "<url><loc>%s/%s</loc><lastmod>%s</lastmod><changefreq>%s</changefreq><priority>%s</priority>%s</url>\n" % (DOM, p.replace("index.html", ""), LASTMOD[p], "weekly" if g in ("blog", "paginas", "guias") else "monthly", pr, img)
    if not xs: continue
    open(OUT + "/sitemap-%s.xml" % g, "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n' + xs + "</urlset>\n")
    SMS.append("sitemap-%s.xml" % g)
open(OUT + "/sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join("<sitemap><loc>%s/%s</loc><lastmod>%s</lastmod></sitemap>\n" % (DOM, s, max(LASTMOD[p] for p in PAGS if p not in NOINDEX and _grupo(p) == s[8:-4])) for s in SMS) + "</sitemapindex>\n")
INDEXNOW = "0e7088fe2e96eae098138bb5db5e8322"
for _php in ("consentimiento.php", "registro-consentimientos.php"):
    shutil.copy(os.path.join(AQUI, "php", _php), OUT + "/" + _php)
open(OUT + "/%s.txt" % INDEXNOW, "w").write(INDEXNOW)
open(OUT + "/indexnow-urls.txt", "w").write("".join("%s/%s\n" % (DOM, p.replace("index.html", "")) for p in PAGS if p not in NOINDEX and p not in CANON))
bots = ["Googlebot", "Bingbot", "GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User", "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot-Extended", "CCBot", "Meta-ExternalAgent"]
open(OUT + "/robots.txt", "w").write("".join("User-agent: %s\nAllow: /\n\n" % b for b in bots) + "User-agent: *\nAllow: /\nDisallow: /registro-consentimientos.php\nDisallow: /consentimiento.php\n\n# Indice y sitemaps por tipo\nSitemap: %s/sitemap.xml\n" % DOM + "".join("Sitemap: %s/%s\n" % (DOM, s) for s in SMS) + "\n# Resumen para IA: %s/llms.txt · %s/llms-full.txt\n" % (DOM, DOM))
llms = "# Studio Emprende\n\n> %s\n\n## Empresa\n- Nombre comercial: Studio Emprende\n- Titular: INTELIGENCIA SEVILLA SL (NIF B88763818)\n- Domicilio social: Calle Betis 3, 41449 Alcolea del Río (Sevilla), España\n- Contacto: info@studioemprende.com · WhatsApp +34 601 86 96 68\n- Ámbito: 100 %% online, toda España\n\n## Precios\n" % ORG["description"] + "".join("- %s: %s%s. %s\n" % (n, p, "" if p == "A medida" else " + 40 €/mes de soporte (sin IVA)", d) for n, p, d, x in PACKS) + "\n## Servicios\n"
llms += "".join("- [%s](%s/servicios/%s.html): %s\n" % (s[2], DOM, s[0], " ".join(s[3].split())) for s in SECCIONES)
llms += "\n## PIX, agente de IA empresarial\n- [PIX](%s/servicios/pix/): %s\n" % (DOM, PIX_HUB["resumen"]) + "".join("- [%s](%s/servicios/pix/%s.html): %s\n" % (x["nav"], DOM, x["slug"], x["resumen"]) for x in PIX_PAGINAS)
llms += "\n## Guías para emprender\n" + "".join("- [%s](%s/guias/%s.html): %s\n" % (g[4], DOM, g[0], g[5].split(". ")[0] + ".") for g in GUIAS)
llms += "\n## Casos de éxito\n- [Caso ContrataLux: marca, web, SEO, redes y CRM a medida](%s/casos/contratalux)\n" % DOM
llms += "\n## Páginas clave\n- [Precios y packs](%s/precios.html)\n- [Normativas 2026-2027](%s/normativas.html)\n- [Sectores](%s/sectores.html)\n- [Programa de partners](%s/partners.html)\n- [Contacto](%s/contacto.html)\n\n## Blog\n" % (DOM, DOM, DOM, DOM, DOM)
llms += "".join("- [%s](%s/blog/%s.html): %s\n" % (a[1], DOM, a[0], a[2]) for a in ARTICULOS + BN.ARTICULOS)
llms += "\n## Optional\n- [Todas las funciones, página a página](%s/llms-full.txt)\n- [Mapa de la web](%s/mapa-web.html)\n- [Sitemap](%s/sitemap.xml)\n" % (DOM, DOM, DOM)
open(OUT + "/llms.txt", "w").write(llms)
full = "# Studio Emprende — contenido completo\n\n> %s\n\nAtendemos 100 %% online en toda España. Contacto y diagnóstico gratis: %s/contacto.html\n" % (ORG["description"], DOM)
full += "\n## Packs y precios\n" + "".join("- %s: %s. %s\n" % (n, p, d) for n, p, d, _ in PACKS)
for slug, menu, titulo, intro, bloques in SECCIONES:
    full += "\n## %s\nURL: %s/servicios/%s.html\n%s\n" % (titulo, DOM, slug, " ".join(intro.split()))
    for b, items in bloques:
        _ok = [i for i in items if "servicios/%s/%s.html" % (slug, slugify(i)) not in NOINDEX and "servicios/%s/%s.html" % (slug, slugify(i)) not in CANON]
        full += "\n### %s\n" % b + "".join("- [%s](%s/servicios/%s/%s.html)\n" % (i, DOM, slug, slugify(i)) for i in _ok) + ("".join("- %s\n" % i for i in items if i not in _ok))
for g in GUIAS:
    full += "\n## %s\nURL: %s/guias/%s.html\n%s\n" % (g[4], DOM, g[0], g[5]) + "".join("**%s**\n%s\n\n" % (q, a) for q, a in g[7])
full += "\n## Normativas\n" + "".join("- %s (%s): %s\n" % (a, b, c) for a, b, c, d in NORMATIVAS)
full += "\n## Preguntas frecuentes\n" + "".join("**%s**\n%s\n\n" % (q, a) for q, a in FAQ)
full += "## Blog\n" + "".join("- [%s](%s/blog/%s.html): %s\n" % (a[1], DOM, a[0], a[2]) for a in ARTICULOS + BN.ARTICULOS)
open(OUT + "/llms-full.txt", "w").write(full)
print(len(PAGS), "páginas")

# ---------- URLS LIMPIAS (sin .html) ----------
import re as _re2
# Paginas que chocan con una carpeta del mismo nombre (servicios/fichador.html + servicios/fichador/):
# se mueven a servicios/fichador/index.html para que la URL sea /servicios/fichador/
_CHOQUES = []
for _d, _, _fs in os.walk(OUT):
    for _f in _fs:
        if _f.endswith(".html") and _f != "index.html" and os.path.isdir(os.path.join(_d, _f[:-5])):
            _CHOQUES.append(os.path.relpath(os.path.join(_d, _f[:-5]), OUT).replace(os.sep, "/"))
_dom = _re2.escape(DOM)
for _d, _, _fs in os.walk(OUT):
    for _f in _fs:
        if not _f.endswith((".html", ".xml", ".txt")): continue
        _p = os.path.join(_d, _f); _s = open(_p, encoding="utf-8").read(); _o = _s
        _s = _re2.sub(r'(%s/[^"\'\s)<>]*?)index\.html' % _dom, r'\1', _s)
        _s = _re2.sub(r'(%s/[^"\'\s)<>]*?)\.html' % _dom, r'\1', _s)
        _s = _re2.sub(r'href="((?:\.\./)*(?:[\w-]+/)*)index\.html', lambda m: 'href="%s' % (m.group(1) or "./"), _s)
        _s = _re2.sub(r'href="([^":#?]+?)\.html', r'href="\1', _s)
        if _f.endswith(".html"):
            _rel = os.path.relpath(_d, OUT)
            def _abs(m):
                attr, h = m.group(1), m.group(2)
                if h.startswith(("http:", "https:", "mailto:", "tel:", "#", "/", "data:", "javascript:")): return m.group(0)
                path, sep, tail = h.partition("?") if "?" in h else (h.partition("#") if "#" in h else (h, "", ""))
                dirlike = path.endswith("/") or path in ("", ".", "./")
                full = os.path.normpath(os.path.join(_rel, path or "."))
                full = "/" if full in (".", "") else "/" + full.replace(os.sep, "/")
                if dirlike and full != "/": full += "/"
                return '%s="%s%s%s"' % (attr, full, sep, tail)
            _s = _re2.sub(r'\b(href|src)="([^"]*)"', _abs, _s)
            for _c in _CHOQUES:
                _s = _re2.sub(r'"/%s(?=["#?])' % _re2.escape(_c), '"/%s/' % _c, _s)
        for _c in _CHOQUES:
            _s = _re2.sub(r'(%s/%s)(?=[\s"<)#?]|$)' % (_dom, _re2.escape(_c)), r'\1/', _s, flags=_re2.M)
        if _s != _o: open(_p, "w", encoding="utf-8").write(_s)
for _c in _CHOQUES:
    shutil.move(os.path.join(OUT, _c + ".html"), os.path.join(OUT, _c, "index.html"))
open(OUT + "/.htaccess", "w").write("""Options -MultiViews
<IfModule mod_speling.c>
CheckSpelling Off
CheckCaseOnly Off
</IfModule>
DirectoryIndex index.html
ErrorDocument 404 /404.html
RewriteEngine On

# URL antigua de la web multidioma
RewriteRule ^servicios/webs/webs-multidioma-para-espana-y-latinoamerica(\\.html)?/?$ https://studioemprende.com/servicios/webs/webs-multidioma-para-espana-y-exportacion [R=301,L]

# Sitemaps antiguos (hoy hay uno por familia de servicio): al indice
RewriteRule ^sitemap-(funciones|servicios)\\.xml$ https://studioemprende.com/sitemap.xml [R=301,L]

# http o www -> https sin www en UN solo salto (quitando tambien la barra final o el .html)
RewriteCond %{HTTPS} off [OR]
RewriteCond %{HTTP_HOST} ^www\\. [NC]
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.+)/$ https://studioemprende.com/$1 [R=301,L]
RewriteCond %{HTTPS} off [OR]
RewriteCond %{HTTP_HOST} ^www\\. [NC]
RewriteRule ^(.*/)?index\\.html$ https://studioemprende.com/$1 [R=301,L]
RewriteCond %{HTTPS} off [OR]
RewriteCond %{HTTP_HOST} ^www\\. [NC]
RewriteRule ^(.+?)\\.html$ https://studioemprende.com/$1 [R=301,L]
RewriteCond %{HTTPS} off [OR]
RewriteCond %{HTTP_HOST} ^www\\. [NC]
RewriteRule ^ https://studioemprende.com%{REQUEST_URI} [R=301,L,NE]

# /algo/index.html -> /algo/
RewriteCond %{THE_REQUEST} \\s/+(.*/)?index\\.html[\\s?] [NC]
RewriteRule ^ /%1 [R=301,L,NE]

# /pagina/ -> /pagina  (quitar barra final si no es carpeta real; un solo salto)
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.+)/$ /$1 [R=301,L]

# /pagina.html -> /pagina  (las URL antiguas siguen funcionando)
RewriteCond %{THE_REQUEST} \\s/+([^?\\s]+?)\\.html[\\s?] [NC]
RewriteRule ^ /%1 [R=301,L,NE]

# /pagina -> sirve pagina.html sin mostrar la extension
# (sin comprobar -f sobre REQUEST_FILENAME: en IONOS esa comprobacion falla)
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_URI} !\\.[a-zA-Z0-9]+$
RewriteRule ^(.*[^/])$ /$1.html [L]

# Compresion gzip
<IfModule mod_deflate.c>
AddOutputFilterByType DEFLATE text/html text/css text/plain text/xml application/javascript text/javascript application/json application/xml image/svg+xml
</IfModule>

# Cache de recursos estaticos
<IfModule mod_expires.c>
ExpiresActive On
ExpiresByType text/css "access plus 7 days"
ExpiresByType application/javascript "access plus 7 days"
ExpiresByType image/svg+xml "access plus 30 days"
ExpiresByType image/png "access plus 30 days"\nExpiresByType font/woff2 "access plus 1 year"
ExpiresByType image/jpeg "access plus 1 year"
ExpiresByType image/webp "access plus 1 year"
</IfModule>
""")
# Hubs (carpetas con index.html): .html, sin barra, http o www -> URL final con barra en UN solo salto.
# Sin esto: /servicios/x.html -> /servicios/x -> /servicios/x/ (dos 301, y tres desde http o www).
_hubs = ["casos", "temas", "blog", "guias", "servicios"] + sorted("servicios/" + x for x in os.listdir(OUT + "/servicios") if os.path.isdir(OUT + "/servicios/" + x))
_alt = "|".join(re.escape(h) for h in _hubs)
_regla = ("# Hubs: variantes antiguas (.html, /index.html, sin barra, http, www) a la URL final con barra, en un solo salto\n"
          "RewriteRule ^(" + _alt + ")(\\.html|/index\\.html)?$ https://studioemprende.com/$1/ [R=301,L]\n"
          "RewriteCond %{HTTPS} off [OR]\nRewriteCond %{HTTP_HOST} ^www\\. [NC]\n"
          "RewriteRule ^(" + _alt + ")/$ https://studioemprende.com/$1/ [R=301,L]\n\n")
_ht = open(OUT + "/.htaccess").read().replace("# Sitemaps antiguos", _regla + "# Sitemaps antiguos", 1)
open(OUT + "/.htaccess", "w").write(_ht)
# Nota: no se cambia la fecha de los archivos (os.utime): el despliegue usa --only-newer
# y fechas antiguas impedian que se subieran las paginas modificadas.

# Last-Modified real: cada pagina conserva la fecha y hora en que cambio de verdad (fechas.json).
# El despliegue compara tamano y fecha, asi que solo se suben las paginas modificadas.
import calendar as _cal, time as _time
for _p in PAGS:
    _f = os.path.join(OUT, _p)
    if not os.path.exists(_f): _f = os.path.join(OUT, _p[:-5], "index.html")
    if os.path.exists(_f) and _p in _FECH:
        _t = _cal.timegm(_time.strptime(_FECH[_p][1], "%Y-%m-%dT%H:%M:%S"))
        os.utime(_f, (_t, _t))
