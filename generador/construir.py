import os, shutil, sys
from html import escape as e
sys.path.insert(0, os.path.dirname(__file__))
from datos import SECCIONES, NORMATIVAS, SECTORES, PACKS, MENU
from blog import ARTICULOS
from alt_blog import ALT
from guias import GUIAS, GRUPOS, SERVICIO_GUIAS
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
shutil.copy(os.path.join(AQUI, "estilos.css"), OUT + "/assets/css/estilos.css")
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
        cols += "<div><h4>%s</h4>%s</div>" % (nombre, "".join('<a href="%sservicios/%s.html">%s</a>' % (r, s[0], e(s[2])) for s in by_menu(k)))
    return """<a class="saltar" href="#contenido" style="position:absolute;left:-9999px">Saltar al contenido</a>
<div class="franja"></div>
<header class="cabecera"><div class="w">
<a class="logo" href="{r}index.html" aria-label="Studio Emprende, inicio"><img src="{r}assets/img/logo-horizontal.svg" alt="Studio Emprende" width="200" height="56"></a>
<nav class="nav" aria-label="Principal">
<div class="desplegable"><button type="button" aria-expanded="false">Servicios ▾</button><div class="mega">{cols}</div></div>
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
<div class="pie-top"><div class="pie-marca"><img src="{r}assets/img/logo-horizontal-blanco.svg" alt="Studio Emprende" width="200" height="56"><p>Software, IA y webs para emprender. 100 % online, en España y Latinoamérica.</p></div>
<div class="pie-cols"><div><b>Productos</b>{prod}</div><div><b>Para quién</b>{quien}</div>
<div><b>Recursos</b><a href="{r}guias/index.html">Guías para emprender</a><a href="{r}blog/index.html">Blog</a><a href="{r}normativas.html">Normativas</a><a href="{r}sectores.html">Sectores</a><a href="{r}precios.html">Precios</a><a href="{r}mapa-web.html">Mapa de la web</a></div>
<div><b>Empresa</b><a href="{r}sobre-nosotros.html">Sobre nosotros</a><a href="{r}contacto.html">Contacto</a><a href="{r}contacto.html#diagnostico">Diagnóstico gratis</a></div><div><b>Contacto</b><a href="https://wa.me/34601869668" target="_blank" rel="noopener">WhatsApp 601 86 96 68</a><a href="mailto:info@studioemprende.com">info@studioemprende.com</a></div></div></div>
<div class="pie-base"><span>© 2026 Studio Emprende</span><span><a href="{r}aviso-legal.html">Aviso legal</a> · <a href="{r}privacidad.html">Privacidad</a> · <a href="{r}cookies.html">Cookies</a></span></div>
</div></footer>
<script src="{r}assets/js/main.js"></script>""".format(r=r, prod=prod, quien=quien)

import json as _json
from urllib.parse import urljoin as _uj
MIGAS = []
ORG = {"@type": "Organization", "@id": DOM + "/#org", "name": "Studio Emprende", "url": DOM + "/", "logo": DOM + "/assets/img/logo-vertical.svg",
       "description": "Software de gestión modular, agentes de IA y webs con SEO para autónomos, pymes y empresas. 100 % online en España y Latinoamérica.",
       "areaServed": ["ES", "Latinoamérica"], "knowsLanguage": "es", "email": EMAIL, "telephone": "+34 601 86 96 68",
       "contactPoint": {"@type": "ContactPoint", "telephone": "+34 601 86 96 68", "email": EMAIL, "contactType": "customer service", "availableLanguage": "es"}}

def _meta(d):
    d = " ".join(d.split())
    if len(d) > 155:
        c = d[:155]; c = c[:c.rfind(" ")].rstrip(",;:·-") ; d = c + "."
    for extra in [" 100 % online en España y Latinoamérica.", " Pide tu diagnóstico gratis."]:
        if len(d) < 140 and len(d + extra) <= 155: d += extra
    return d

def _tit(t):
    if len(t) <= 60: return t
    base = t.split(" · ")[0]
    return base if len(base) <= 60 else base[:57].rsplit(" ", 1)[0] + "…"

def pagina(ruta, titulo, desc, cuerpo, ld_extra=None, tipo="website", faqs=None):
    global MIGAS
    url = DOM + "/" + ruta.replace("index.html", "")
    titulo = _tit(titulo); desc = _meta(desc)
    grafo = [ORG]
    if ruta == "index.html":
        grafo.append({"@type": "WebSite", "@id": DOM + "/#web", "url": DOM + "/", "name": "Studio Emprende", "inLanguage": "es", "publisher": {"@id": DOM + "/#org"}})
    grafo.append({"@type": "WebPage", "@id": url, "url": url, "name": titulo, "description": desc, "inLanguage": "es", "isPartOf": {"@id": DOM + "/#web"}, "about": {"@id": DOM + "/#org"}})
    if MIGAS:
        el = [{"@type": "ListItem", "position": 1, "name": "Inicio", "item": DOM + "/"}]
        for i, (t, h) in enumerate(MIGAS, 2):
            el.append({"@type": "ListItem", "position": i, "name": t, "item": _uj(url, h) if h else url})
        grafo.append({"@type": "BreadcrumbList", "itemListElement": el})
    if ruta.startswith("servicios/") and ruta != "servicios/index.html":
        grafo.append({"@type": "Service", "name": titulo.split(" · ")[0], "description": desc, "provider": {"@id": DOM + "/#org"}, "areaServed": ["ES", "Latinoamérica"], "url": url})
    if 'class="faq"' in cuerpo:
        grafo.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in (faqs or FAQ)]})
    if ld_extra: grafo.append(ld_extra)
    MIGAS = []
    ldj = '<script type="application/ld+json">%s</script>' % _json.dumps({"@context": "https://schema.org", "@graph": grafo}, ensure_ascii=False).replace("</", "<\\/")
    seo = """<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
<link rel="alternate" hreflang="es" href="{u}"><link rel="alternate" hreflang="x-default" href="{u}">
<meta property="og:url" content="{u}"><meta property="og:locale" content="es_ES"><meta property="og:site_name" content="Studio Emprende">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{t}"><meta name="twitter:description" content="{d}"><meta name="twitter:image" content="{dom}/assets/img/og-imagen.png">
{ld}""".format(u=url, t=e(titulo), d=e(desc), dom=DOM, ld=ldj)
    cuerpo = cuerpo + "\n" + seo + "\n" if False else cuerpo
    _pagina(ruta, titulo, desc, cuerpo, seo, tipo)

def _pagina(ruta, titulo, desc, cuerpo, seo, tipo):
    r = "../" * ruta.count("/")
    html = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{dom}/{ruta}">
<meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:image" content="{dom}/assets/img/og-imagen.png"><meta property="og:type" content="{tipo}">
{seo}
<link rel="icon" href="{r}favicon.ico" sizes="any"><link rel="icon" type="image/svg+xml" href="{r}favicon.svg"><link rel="apple-touch-icon" href="{r}apple-touch-icon.png"><link rel="manifest" href="{r}site.webmanifest"><meta name="theme-color" content="#7A2638">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Marcellus&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/css/estilos.css">
</head>
<body>
{cab}
<main id="contenido">
{c}
</main>
{pie}
<a class="wa-flot" href="https://wa.me/{wan}?text={wat}" target="_blank" rel="noopener" aria-label="Escríbenos por WhatsApp">
<span class="wa-burbuja"><b>¿Hablamos?</b>Te respondemos por WhatsApp</span>
<span class="wa-icono"><svg viewBox="0 0 32 32" width="30" height="30" aria-hidden="true"><path fill="currentColor" d="M16 3C8.8 3 3 8.6 3 15.6c0 2.5.8 4.9 2.1 6.9L3.6 29l6.7-1.7c1.8 1 3.8 1.5 5.7 1.5 7.2 0 13-5.6 13-12.6S23.2 3 16 3zm0 23.1c-1.8 0-3.6-.5-5.1-1.4l-.4-.2-4 1 .9-3.8-.2-.4c-1.1-1.7-1.6-3.6-1.6-5.6C5.6 10 10.2 5.5 16 5.5S26.4 10 26.4 15.6 21.8 26.1 16 26.1zm5.7-7.8c-.3-.2-1.9-.9-2.2-1-.3-.1-.5-.2-.7.2-.2.3-.8 1-1 1.2-.2.2-.4.2-.7.1-.3-.2-1.3-.5-2.5-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.5-.6c.2-.2.2-.3.3-.5.1-.2 0-.4 0-.6-.1-.2-.7-1.7-1-2.3-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.2 1.1-1.2 2.7s1.2 3.1 1.4 3.3c.2.2 2.4 3.6 5.8 5 2.9 1.1 3.4.9 4 .8.6-.1 1.9-.8 2.2-1.5.3-.7.3-1.4.2-1.5-.1-.2-.3-.3-.6-.4z"/></svg></span></a>
</body>
</html>""".format(t=e(titulo), d=e(desc), dom=DOM, ruta=ruta.replace("index.html", ""), r=r, cab=cabecera(r), c=cuerpo, pie=pie(r), seo=seo, tipo=tipo, wan=WA_NUM, wat=_q("Hola, vengo de la web de Studio Emprende (%s) y quiero información." % titulo.split(" · ")[0]))
    p = os.path.join(OUT, ruta); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w").write(html)
    PAGS.append(ruta)

PAGS = []

def cta(r):
    return """<section class="cta"><div class="w"><h2>Empieza hoy con tu diagnóstico gratis</h2>
<div class="botones"><a class="btn btn-claro" href="{r}contacto.html#diagnostico">Pedir diagnóstico</a><a class="btn btn-borde-claro" href="{r}contacto.html">Hablar con nosotros</a></div></div></section>""".format(r=r)

FAQ = [("¿Cuánto tardáis en tenerlo todo listo?", "Depende del pack y de lo rápido que nos pases tu información. Te damos un plazo cerrado al empezar."),
       ("¿Qué incluye la cuota de 40 € al mes?", "El soporte y el mantenimiento de tu programa de gestión."),
       ("¿Puedo contratar un solo servicio?", "Sí. Con «Arma tu pack» eliges solo lo que necesitas."),
       ("¿Trabajáis fuera de España?", "Sí. Somos 100 % online y trabajamos con España y Latinoamérica."),
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
<div class="confianza"><span>Una sola cuenta</span><span>100 %% online</span><span>España y Latinoamérica</span><span>Soporte que responde</span></div></div>
<div class="hero-card" aria-label="Ejemplo del agente PIX trabajando"><div class="estado"><span>Agente PIX · en marcha</span><b>● activo</b></div>
<div class="fila">Nuevo contacto por WhatsApp: «Necesito una web y facturar con Verifactu»</div>
<div class="fila ok"><span>✓ Contacto creado en el CRM</span><span>✓ Pack «Negocio en Marcha» propuesto</span><span>✓ Reunión agendada el jueves a las 10:00</span></div>
<div class="fin">Presupuesto enviado al cliente</div></div>
</div></section>

<section class="sec sec-suave"><div class="w">
<div class="cab"><p class="kicker">Demo del programa</p><h2>Tus ventas, en un tablero</h2></div>
<div class="demo"><div class="demo-lat"><b style="color:#fff;font-weight:500">Studio Emprende</b><span class="act">CRM</span><span>Facturación</span><span>Agenda</span><span>Fichaje</span><span>PIX</span></div>
<div class="tablero">
<div class="col"><span>Nuevo · 3</span><div class="trato">Taller López<br><b>1.790 €</b></div><div class="trato">Clínica Sur<br><b>990 €</b></div></div>
<div class="col"><span>Propuesta · 2</span><div class="trato">Reformas Vega<br><b>3.690 €</b></div></div>
<div class="col"><span>Negociación · 1</span><div class="trato">Academia Norte<br><b>1.790 €</b></div></div>
<div class="col"><span>Ganado · 4</span><div class="trato ganado">Café Central<br><b>990 €</b></div></div>
</div></div>
<p class="aviso">● Nuevo contacto desde la web: Fisioterapia Ruiz</p>
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
<div style="flex:999 1 420px;min-width:0"><p class="kicker">Normativas 2026-2027</p><h2>¿Te afecta Verifactu, el fichaje digital o el AI Act?</h2><p class="lead" style="margin-top:12px">Te explicamos qué es, cuándo llega y cómo cumplir sin complicarte.</p></div>
<a class="btn btn-s" href="normativas.html">Ver normativas</a>
</div></section>

<section class="sec"><div class="w"><div class="cab"><p class="kicker">Blog</p><h2>Ideas claras para tu negocio</h2></div><div class="rejilla">%s</div><p style="margin-top:28px"><a class="btn btn-s" href="blog/index.html">Ver todos los artículos</a></p></div></section>
<section class="sec sec-suave"><div class="w"><div class="cab"><p class="kicker">Preguntas frecuentes</p><h2>Lo que más nos preguntan</h2></div>%s</div></section>
""" % (tec, serv, packs(""), "".join('<a class="pildora" href="sectores.html#%s">%s</a>' % (s.lower().replace(" ", "-"), s) for s in SECTORES), BLOGHOME, faq())
pagina("index.html", "Studio Emprende · Software, IA y webs para emprender", "Programa de gestión modular, agentes de IA y webs con SEO en una sola cuenta. Para autónomos, pymes y empresas en España y Latinoamérica.", inicio + cta(""))

import unicodedata, re as _re
def slugify(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    return _re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:70]
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
{rel}""".format(m=migas("../", ("Servicios", "index.html"), (titulo, None)), cat=dict(MENU)[menu], t=e(titulo), i=e(intro), s=slug, c=cuerpo, a=aside,
                 rel=('<section class="sec sec-suave"><div class="w"><div class="cab"><p class="kicker">También te puede interesar</p><h2>Servicios relacionados</h2></div><div class="rejilla">%s</div></div></section>' % relh) if relh else "")
    gs = [g for g in GUIAS if g[0] in SERVICIO_GUIAS.get(slug, [])]
    if gs:
        html += '<section class="sec"><div class="w"><div class="cab"><p class="kicker">Guías para emprender</p><h2>Antes de empezar, te puede servir</h2></div><div class="rejilla">%s</div></div></section>' % "".join('<a class="tarjeta" href="../guias/%s.html"><h3>%s</h3><p>%s</p><span class="mas">Leer guía →</span></a>' % (g[0], e(g[4]), e(g[3][:120].rsplit(" ",1)[0] + "…")) for g in gs[:3])
    pagina("servicios/%s.html" % slug, "%s · Studio Emprende" % titulo, intro[:155], html + cta("../"))


# ---------- PAGINAS DE CADA FUNCION ----------
for slug, menu, titulo, intro, bloques in SECCIONES:
    for b, items in bloques:
        for it in items:
            fs = slugify(it)
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
            pagina("servicios/%s/%s.html" % (slug, fs), "%s · %s · Studio Emprende" % (it, titulo), ("%s: %s" % (it, intro))[:155], html + cta("../../"))

# ---------- PRECIOS ----------
pagina("precios.html", "Precios y packs · Studio Emprende", "Packs para empezar desde 990 € más 40 €/mes de soporte, o arma tu propio pack con solo lo que necesitas.",
       '<section class="page-hero"><div class="w">%s<h1>Precios y packs</h1><p class="lead">Pago único por el pack y una cuota de 40 € al mes de soporte y mantenimiento. Precios sin IVA.</p></div></section><section class="sec"><div class="w">%s</div></section><section class="sec sec-suave"><div class="w"><div class="cab"><h2>Preguntas frecuentes</h2></div>%s</div></section>%s'
       % (migas("", ("Precios", None)), packs(""), faq(), cta("")))

# ---------- NORMATIVAS ----------
filas = "".join('<tr><td><b style="font-weight:500">%s</b></td><td>%s</td><td>%s</td><td><a href="servicios/%s.html">Cómo cumplir →</a></td></tr>' % (e(a), e(b), e(c), d) for a, b, c, d in NORMATIVAS)
pagina("normativas.html", "Normativas 2026-2027 para empresas · Studio Emprende", "Verifactu, factura electrónica, registro de jornada, AI Act, accesibilidad, NIS2 y más: qué es, a quién afecta y cuándo.",
       '<section class="page-hero"><div class="w">%s<h1>Normativas que afectan a tu empresa</h1><p class="lead">Resumen de las leyes que más preguntan nuestros clientes. Fechas revisadas en octubre de 2026; consulta siempre la fuente oficial (BOE, AEAT o EUR-Lex).</p></div></section><section class="sec"><div class="w"><div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Norma</th><th>Referencia</th><th>Estado y plazos</th><th></th></tr></thead><tbody>%s</tbody></table></div><p class="mut" style="margin-top:16px;font-size:14px">Esta página es informativa y no sustituye el asesoramiento legal.</p></div></section>%s'
       % (migas("", ("Normativas", None)), filas, cta("")))

# ---------- SECTORES ----------
sect = "".join('<div class="tarjeta" id="%s"><h3>%s</h3><p>Programa de gestión, PIX y web adaptados a %s.</p><a class="mas" href="contacto.html?sector=%s#diagnostico">Pedir propuesta →</a></div>' % (s.lower().replace(" ", "-"), s, s.lower(), s.lower().replace(" ", "-")) for s in SECTORES)
pagina("sectores.html", "Sectores · Studio Emprende", "Software de gestión, IA y webs adaptados a talleres, clínicas, reformas, hostelería, inmobiliarias y más.",
       '<section class="page-hero"><div class="w">%s<h1>Sectores</h1><p class="lead">Partimos de lo que ya funciona en tu sector y lo adaptamos a tu forma de trabajar.</p></div></section><section class="sec"><div class="w"><div class="rejilla">%s</div></div></section>%s' % (migas("", ("Sectores", None)), sect, cta("")))

# ---------- CONTACTO ----------
opts = "".join('<option value="%s">%s</option>' % (s[0], e(s[2])) for s in SECCIONES)
contacto = """<section class="page-hero"><div class="w">{m}<h1>Hablemos de tu negocio</h1><p class="lead">Cuéntanos qué necesitas y te respondemos con un diagnóstico gratuito y una propuesta clara.</p></div></section>
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
<aside class="lateral-aside"><h3>Otras formas de contacto</h3><p style="color:#C9C1BB"><a style="color:#fff" href="https://wa.me/34601869668?text=Hola%2C%20quiero%20pedir%20mi%20diagn%C3%B3stico%20gratis" target="_blank" rel="noopener">WhatsApp: 601 86 96 68</a><br><a style="color:#fff" href="mailto:info@studioemprende.com">info@studioemprende.com</a></p><p style="color:#C9C1BB">Respondemos en menos de 24 horas laborables.</p></aside>
</div></section>""".format(m=migas("", ("Contacto", None)), o=opts, dom=DOM)
pagina("contacto.html", "Contacto y diagnóstico gratis · Studio Emprende", "Pide tu diagnóstico gratuito: te decimos qué puedes automatizar y digitalizar en tu negocio.", contacto)

pagina("gracias.html", "Mensaje recibido · Studio Emprende", "Hemos recibido tu mensaje. Te respondemos en menos de 24 horas laborables; si es urgente, escríbenos por WhatsApp al 601 86 96 68.",
       '<section class="sec"><div class="w" style="text-align:center;display:flex;flex-direction:column;gap:18px;align-items:center"><img src="assets/img/simbolo.svg" alt="" width="70" height="101"><h1>¡Gracias! Hemos recibido tu mensaje</h1><p class="lead">Te respondemos en menos de 24 horas laborables. Si es urgente, escríbenos por WhatsApp.</p><div class="botones"><a class="btn btn-p" href="https://wa.me/34601869668" target="_blank" rel="noopener">Escribir por WhatsApp</a><a class="btn btn-s" href="index.html">Volver al inicio</a></div></div></section>')

# ---------- SOBRE NOSOTROS ----------
pagina("sobre-nosotros.html", "Sobre nosotros · Studio Emprende", "Studio Emprende ayuda a emprendedores y pymes con software, IA y webs, 100 % online.",
       '<section class="page-hero"><div class="w">%s<h1>Sobre nosotros</h1><p class="lead">Ayudamos a quien emprende a tener un negocio ordenado, visible y automatizado desde el primer día.</p></div></section><section class="sec"><div class="w rejilla"><div class="tarjeta"><h3>Siempre respondemos</h3><p>Un único interlocutor que conoce tu negocio.</p></div><div class="tarjeta"><h3>Entregamos en plazo</h3><p>Plazos cerrados desde el primer día.</p></div><div class="tarjeta"><h3>100 %% online</h3><p>Trabajamos con toda España y Latinoamérica.</p></div></div></div>%s</section>%s' % (migas("", ("Sobre nosotros", None)), HIST, cta("")))

LEG = {"aviso-legal": AVISO, "privacidad": PRIVACIDAD, "cookies": COOKIES}
# ---------- LEGALES ----------
for slug, t in [("aviso-legal", "Aviso legal"), ("privacidad", "Política de privacidad"), ("cookies", "Política de cookies")]:
    pagina(slug + ".html", "%s · Studio Emprende" % t, t + " de Studio Emprende.",
           '<section class="page-hero"><div class="w">%s<h1>%s</h1></div></section><section class="sec"><div class="w legal-txt"><p class="mut">Última actualización: octubre de 2026.</p>%s</div></section>' % (migas("", (t, None)), t, LEG[slug]))

pagina("404.html", "Página no encontrada · Studio Emprende", "La página que buscas no existe.",
       '<section class="sec"><div class="w" style="text-align:center;display:flex;flex-direction:column;gap:18px;align-items:center"><img src="assets/img/simbolo.svg" alt="" width="70" height="101"><h1>Esta página no existe</h1><p class="lead">Puede que el enlace haya cambiado.</p><div class="botones"><a class="btn btn-p" href="index.html">Ir al inicio</a><a class="btn btn-s" href="mapa-web.html">Ver el mapa de la web</a></div></div></section>')

# ---------- BLOG ----------
pagina("blog/index.html", "Blog · Studio Emprende", "Artículos sobre gestión, normativas, IA y webs para autónomos y pymes.",
       '<section class="page-hero"><div class="w">%s<h1>Blog</h1><p class="lead">Ideas claras sobre gestión, normativas, inteligencia artificial y webs, sin tecnicismos.</p></div></section><section class="sec"><div class="w"><div class="rejilla">%s</div></div></section>%s' % (migas("../", ("Blog", None)), "".join(tarjeta_blog(a, "") for a in ARTICULOS), cta("../")))
for slug, titulo, desc, fecha, cat, serv_rel, cuerpo in ARTICULOS:
    sr = [x for x in SECCIONES if x[0] == serv_rel][0]
    otros = "".join([tarjeta_blog(a, "") for a in ARTICULOS if a[0] != slug][:3])
    ld = ""
    bp = {"@type": "BlogPosting", "headline": titulo, "description": desc, "inLanguage": "es", "articleSection": cat,
          "image": "%s/assets/img/blog/%s.jpg" % (DOM, slug), "author": {"@id": DOM + "/#org"}, "publisher": {"@id": DOM + "/#org"},
          "mainEntityOfPage": "%s/blog/%s.html" % (DOM, slug)}
    html = """<section class="page-hero"><div class="w">{m}<p class="kicker">{cat} · {f}</p><h1>{t}</h1><p class="lead">{d}</p></div></section>
<section class="sec"><div class="w lateral"><article class="lateral-main articulo">{fp}{c}</article>
<aside class="lateral-aside"><h3>{st}</h3><p style="color:#C9C1BB">{si}</p><a class="btn btn-claro" href="../servicios/{ss}.html">Ver el servicio</a><a class="btn btn-borde-claro" href="../contacto.html?servicio={ss}#diagnostico">Pedir diagnóstico</a></aside></div></section>
<section class="sec sec-suave"><div class="w"><div class="cab"><p class="kicker">Sigue leyendo</p><h2>Otros artículos</h2></div><div class="rejilla">{o}</div></div></section>{ld}""".format(fp=foto_blog(slug, ALT.get(slug, titulo), True), 
        m=migas("../", ("Blog", "index.html"), (titulo, None)), cat=e(cat), f=fecha, t=e(titulo), d=e(desc), c=cuerpo, sl=slug, st=e(sr[2]), si=e(sr[3]), ss=serv_rel, o=otros, ld=ld)
    pagina("blog/%s.html" % slug, "%s · Studio Emprende" % titulo, desc, html + cta("../"), ld_extra=bp, tipo="article")

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
    html = """<section class="page-hero"><div class="w">{m}<p class="kicker">Guía · {gn}</p><h1>{h1}</h1><p class="lead">{lead}</p></div></section>
<section class="sec"><div class="w lateral"><article class="lateral-main articulo"><div class="resumen"><b>Respuesta rápida</b><p>{res}</p></div>{ind}{secs}{faq}</article>{aside}</div></section>
<section class="sec sec-suave"><div class="w"><div class="cab"><p class="kicker">Sigue aprendiendo</p><h2>Guías relacionadas</h2></div><div class="rejilla">{rel}</div>{blog}</div></section>""".format(
        m=migas("../", ("Guías", "index.html"), (h1, None)), gn=e(dict(GRUPOS)[grupo]), h1=e(h1), res=e(resumen), ind=indice, lead=e(meta), secs=secs, faq=faqh, aside=aside, rel=relh,
        blog=('<div class="cab" style="margin:40px 0 20px"><p class="kicker">Del blog</p></div><div class="rejilla">%s</div>' % blogh) if blogh else "")
    art = {"@type": "Article", "headline": h1, "description": meta, "inLanguage": "es", "author": {"@id": DOM + "/#org"}, "publisher": {"@id": DOM + "/#org"},
           "datePublished": "2026-10-12", "dateModified": "2026-10-12", "mainEntityOfPage": "%s/guias/%s.html" % (DOM, slug), "image": DOM + "/assets/img/og-imagen.png",
           "abstract": resumen}
    pagina("guias/%s.html" % slug, titulo, meta, html + cta("../"), ld_extra=art, tipo="article", faqs=faqs)

# ---------- MAPA ----------
grupos = [("Principal", [("Inicio", "index.html"), ("Servicios", "servicios/index.html"), ("Precios y packs", "precios.html"), ("Sectores", "sectores.html"), ("Normativas", "normativas.html"), ("Sobre nosotros", "sobre-nosotros.html"), ("Contacto y diagnóstico", "contacto.html")])]
for k, n in MENU:
    grupos.append((n, [(s[2], "servicios/%s.html" % s[0]) for s in by_menu(k)]))
grupos.append(("Guías para emprender", [("Todas las guías", "guias/index.html")] + [(g[4], "guias/%s.html" % g[0]) for g in GUIAS]))
grupos.append(("Blog", [("Todos los artículos", "blog/index.html")] + [(a[1], "blog/%s.html" % a[0]) for a in ARTICULOS]))
grupos.append(("Legal", [("Aviso legal", "aviso-legal.html"), ("Privacidad", "privacidad.html"), ("Cookies", "cookies.html")]))
mapa = '<div class="mapa-raiz"><a href="index.html">STUDIO EMPRENDE</a></div><div class="mapa">' + "".join('<div class="grupo"><h3>%s</h3>%s</div>' % (g, "".join('<a href="%s">%s</a>' % (h, e(t)) for t, h in ls)) for g, ls in grupos) + "</div>"
pagina("mapa-web.html", "Mapa de la web · Studio Emprende", "Todas las páginas de Studio Emprende.", '<section class="page-hero"><div class="w">%s<h1>Mapa de la web</h1><p class="lead">Todas las páginas y cómo se organizan.</p></div></section><section class="sec"><div class="w">%s</div></section>' % (migas("", ("Mapa de la web", None)), mapa))

# ---------- SEO ----------
import datetime as _dt
HOY = _dt.date.today().isoformat()
def _grupo(p):
    if p.startswith("blog/"): return "blog"
    if p.startswith("guias/"): return "guias"
    if p.startswith("servicios/") and p.count("/") == 2: return "funciones"
    if p.startswith("servicios/"): return "servicios"
    return "paginas"
PRIO = {"guias": "0.8", "paginas": "0.8", "servicios": "0.9", "funciones": "0.6", "blog": "0.7"}
SMS = []
for g in ["paginas", "servicios", "guias", "funciones", "blog"]:
    xs = ""
    for p in PAGS:
        if p == "404.html" or _grupo(p) != g: continue
        img = ""
        if g == "blog" and p != "blog/index.html":
            img = "<image:image><image:loc>%s/assets/img/blog/%s.jpg</image:loc></image:image>" % (DOM, p[5:-5])
        pr = "1.0" if p == "index.html" else PRIO[g]
        xs += "<url><loc>%s/%s</loc><lastmod>%s</lastmod><changefreq>%s</changefreq><priority>%s</priority>%s</url>\n" % (DOM, p.replace("index.html", ""), HOY, "weekly" if g in ("blog", "paginas", "guias") else "monthly", pr, img)
    open(OUT + "/sitemap-%s.xml" % g, "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n' + xs + "</urlset>\n")
    SMS.append("sitemap-%s.xml" % g)
open(OUT + "/sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join("<sitemap><loc>%s/%s</loc><lastmod>%s</lastmod></sitemap>\n" % (DOM, s, HOY) for s in SMS) + "</sitemapindex>\n")
INDEXNOW = "5e7a2c38b1d94f6a8c0e3d2b7f61a9c4"
open(OUT + "/%s.txt" % INDEXNOW, "w").write(INDEXNOW)
open(OUT + "/indexnow-urls.txt", "w").write("".join("%s/%s\n" % (DOM, p.replace("index.html", "")) for p in PAGS if p != "404.html"))
bots = ["Googlebot", "Bingbot", "GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User", "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot-Extended", "CCBot", "Meta-ExternalAgent"]
open(OUT + "/robots.txt", "w").write("".join("User-agent: %s\nAllow: /\n\n" % b for b in bots) + "User-agent: *\nAllow: /\nDisallow: /404.html\n\n# Indice y sitemaps por tipo\nSitemap: %s/sitemap.xml\n" % DOM + "".join("Sitemap: %s/%s\n" % (DOM, s) for s in SMS) + "\n# Resumen para IA: %s/llms.txt · %s/llms-full.txt\n" % (DOM, DOM))
llms = "# Studio Emprende\n\n> %s\n\n## Servicios\n" % ORG["description"]
llms += "".join("- [%s](%s/servicios/%s.html): %s\n" % (s[2], DOM, s[0], " ".join(s[3].split())) for s in SECCIONES)
llms += "\n## Guías para emprender\n" + "".join("- [%s](%s/guias/%s.html): %s\n" % (g[4], DOM, g[0], g[5].split(". ")[0] + ".") for g in GUIAS)
llms += "\n## Páginas clave\n- [Precios y packs](%s/precios.html)\n- [Normativas 2026-2027](%s/normativas.html)\n- [Sectores](%s/sectores.html)\n- [Contacto](%s/contacto.html)\n\n## Blog\n" % (DOM, DOM, DOM, DOM)
llms += "".join("- [%s](%s/blog/%s.html): %s\n" % (a[1], DOM, a[0], a[2]) for a in ARTICULOS)
llms += "\n## Optional\n- [Todas las funciones, página a página](%s/llms-full.txt)\n- [Mapa de la web](%s/mapa-web.html)\n- [Sitemap](%s/sitemap.xml)\n" % (DOM, DOM, DOM)
open(OUT + "/llms.txt", "w").write(llms)
full = "# Studio Emprende — contenido completo\n\n> %s\n\nAtendemos 100 %% online en España y Latinoamérica. Contacto y diagnóstico gratis: %s/contacto.html\n" % (ORG["description"], DOM)
full += "\n## Packs y precios\n" + "".join("- %s: %s. %s\n" % (n, p, d) for n, p, d, _ in PACKS)
for slug, menu, titulo, intro, bloques in SECCIONES:
    full += "\n## %s\nURL: %s/servicios/%s.html\n%s\n" % (titulo, DOM, slug, " ".join(intro.split()))
    for b, items in bloques:
        full += "\n### %s\n" % b + "".join("- [%s](%s/servicios/%s/%s.html)\n" % (i, DOM, slug, slugify(i)) for i in items)
for g in GUIAS:
    full += "\n## %s\nURL: %s/guias/%s.html\n%s\n" % (g[4], DOM, g[0], g[5]) + "".join("**%s**\n%s\n\n" % (q, a) for q, a in g[7])
full += "\n## Normativas\n" + "".join("- %s (%s): %s\n" % (a, b, c) for a, b, c, d in NORMATIVAS)
full += "\n## Preguntas frecuentes\n" + "".join("**%s**\n%s\n\n" % (q, a) for q, a in FAQ)
full += "## Blog\n" + "".join("- [%s](%s/blog/%s.html): %s\n" % (a[1], DOM, a[0], a[2]) for a in ARTICULOS)
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
open(OUT + "/.htaccess", "w").write("""DirectoryIndex index.html
ErrorDocument 404 /404.html
RewriteEngine On

# Forzar https
RewriteCond %{HTTPS} off
RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [R=301,L]

# www -> sin www
RewriteCond %{HTTP_HOST} ^www\\.(.+)$ [NC]
RewriteRule ^ https://%1%{REQUEST_URI} [R=301,L]

# /algo/index.html -> /algo/
RewriteCond %{THE_REQUEST} \\s/+(.*/)?index\\.html[\\s?] [NC]
RewriteRule ^ /%1 [R=301,L,NE]

# /pagina.html -> /pagina  (las URL antiguas siguen funcionando)
RewriteCond %{THE_REQUEST} \\s/+([^?\\s]+?)\\.html[\\s?] [NC]
RewriteRule ^ /%1 [R=301,L,NE]

# /pagina/ -> /pagina  (quitar barra final si no es carpeta real)
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.+)/$ /$1 [R=301,L]

# /pagina -> sirve pagina.html sin mostrar la extension
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_FILENAME}.html -f
RewriteRule ^(.+)$ $1.html [L]

# Cache de recursos estaticos
<IfModule mod_expires.c>
ExpiresActive On
ExpiresByType text/css "access plus 7 days"
ExpiresByType application/javascript "access plus 7 days"
ExpiresByType image/svg+xml "access plus 30 days"
ExpiresByType image/png "access plus 30 days"
ExpiresByType image/jpeg "access plus 1 year"
ExpiresByType image/webp "access plus 1 year"
</IfModule>
""")
