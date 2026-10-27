# Casos de éxito: hub /casos/ y una página por caso (/casos/<slug>), con estilos y script propios
# (assets/css/casos.css y assets/js/casos.js) para no tocar lo que comparten las páginas indexadas.

MEDIA = "assets/img/casos/"

# Páginas no indexadas (Anexo B o sin descubrir) que enlazan al caso; nunca páginas del Anexo A
ENLACES_ENTRANTES = {
    "servicios/presencia-digital": "Así lanzamos la presencia digital completa de una empresa de software, de la marca a las redes.",
    "servicios/presencia-digital/automatizacion-de-redes-sociales": "En ContrataLux creamos los perfiles de Facebook, Instagram y LinkedIn y dejamos la publicación automatizada.",
    "servicios/presencia-digital/seo-programatico": "La web de ContrataLux salió con 251 URLs repartidas en 10 sitemaps por sección.",
    "servicios/presencia-digital/videos-y-anuncios-con-ia": "Los reels y carruseles de ContrataLux forman parte de su lanzamiento.",
    "servicios/software-especializado": "ContrataLux es un CRM sectorial para asesorías energéticas construido a medida.",
    "servicios/software-de-gestion/cuadro-de-mando-en-tiempo-real": "Mira el panel de dirección del programa de gestión que hicimos para ContrataLux.",
    "servicios/software-de-gestion/comerciales-y-comisiones": "En ContrataLux cada contrato calcula la comisión bruta, la neta y la repartida entre comerciales.",
    "servicios/departamento-tecnologico/dominios-y-renovaciones": "En ContrataLux registramos el dominio y el hosting a nombre del cliente.",
    "servicios/departamento-tecnologico/correo-que-no-llega-a-spam": "ContrataLux arrancó con correos profesionales en su propio dominio.",
    "servicios/autonomos/packs-con-precio-cerrado": "Un ejemplo de lanzamiento completo de principio a fin: el caso ContrataLux.",
    "servicios/pix": "PIX va integrado en el programa de gestión de ContrataLux.",
    "sobre-nosotros": "Conoce un proyecto completo nuestro: ContrataLux.",
}

CONTRATALUX = {
    "slug": "contratalux",
    "nombre": "ContrataLux",
    "web": "https://contratalux.com/",
    "sector": "Software para asesorías energéticas",
    "titulo": "Caso ContrataLux: marca, web, SEO y CRM a medida",
    "h1": "ContrataLux: de una idea a un software con marca, web indexada y redes en marcha",
    "meta": "Caso real: marca, web con 251 URLs leídas por Google y Bing, redes, dominio, correo y CRM a medida para ContrataLux, software de asesorías energéticas.",
    "resumen": "ContrataLux es un programa de gestión para asesorías energéticas que venden luz, gas, fibra, alarmas y CAEs. Le hicimos todo el lanzamiento digital: identidad de marca, dominio, hosting y correos profesionales, una web con 251 URLs en 10 sitemaps por sección dada de alta en Google Search Console y Bing Webmaster Tools, perfiles de empresa en Facebook, Instagram y LinkedIn con contenido automatizado, y el propio CRM a medida.",
    "fecha": "2026-10-24",
}

SERVICIOS = [  # (qué hicimos, detalle, enlace a nuestro servicio)
    ("Identidad de marca", "Nombre visual, logotipo horizontal y vertical, icono de app en claro y oscuro, favicon y paleta: un sol naranja que sale sobre dos líneas, turquesa y azul, sobre fondo noche.", "precios.html"),
    ("Dominio, hosting y correos", "Dominio contratalux.com y hosting a nombre del cliente, con correos profesionales en su propio dominio desde el primer día.", "servicios/departamento-tecnologico/dominios-y-renovaciones.html"),
    ("Web con SEO por secciones", "Una web de 251 URLs: funciones, integraciones con comercializadoras, calculadoras, soluciones por tipo de cliente, zonas, suministros, recursos y comparativas, cada sección con su sitemap.", "servicios/webs/web-corporativa-con-seo.html"),
    ("Indexación en Google y Bing", "Alta en Google Search Console y Bing Webmaster Tools con el índice de sitemaps. Los dos buscadores lo leyeron sin errores y descubrieron las 251 URLs.", "servicios/presencia-digital/seo-programatico.html"),
    ("Redes sociales", "Creación, optimización y configuración de la página de empresa en Facebook (con su portafolio), Instagram y LinkedIn, con la misma imagen de marca.", "servicios/presencia-digital/automatizacion-de-redes-sociales.html"),
    ("Contenido y automatización", "Reels y carruseles con la marca y un calendario de publicación automatizado, para que las redes trabajen sin depender de que alguien se acuerde de publicar.", "servicios/presencia-digital/videos-y-anuncios-con-ia.html"),
    ("Programa de gestión personalizado", "El CRM de ContrataLux: contratos, comisiones, retrocomisiones, liquidaciones, calculadora de ahorro, mercado energético, equipo y permisos, con PIX integrado.", "servicios/software-especializado/index.html"),
]

PASOS = ["Marca", "Dominio y correo", "Web", "Google y Bing", "Redes", "Contenido", "CRM"]

CAPTURAS = [  # (archivo, alt, pie)
    ("contratalux-panel.webp", "Panel de dirección del CRM de ContrataLux con contratos por estado y gráfico de cartera", "Panel de dirección: contratos del periodo, mix de cartera y avisos. Datos de demostración."),
    ("contratalux-contrato.webp", "Ficha de contrato de luz en el CRM de ContrataLux con comisiones y retrocomisión", "Ficha de contrato: comisión bruta, neta y repartida, días de retrocomisión y datos técnicos. Datos de demostración."),
    ("contratalux-calculadora.webp", "Calculadora de ahorro de ContrataLux para clientes B2C y B2B", "Calculadora de ahorro en cuatro pasos para particulares, comunidades, autónomos y empresas. Datos de demostración."),
    ("contratalux-comercializadoras.webp", "Listado de comercializadoras precargadas en el CRM de ContrataLux", "Comercializadoras precargadas con sus tarifas y comisiones. Datos de demostración."),
]

FAQS = [
    ("¿Qué incluye un lanzamiento completo como el de ContrataLux?", "Identidad de marca, dominio, hosting y correos profesionales, una web con SEO dada de alta en Google y Bing, perfiles de empresa en redes con contenido automatizado y, si el negocio lo necesita, un programa de gestión a medida. En ContrataLux hicimos todo."),
    ("¿Puedo contratar solo una parte, por ejemplo la web y la indexación?", "Sí. Cada pieza se contrata por separado o dentro de un pack. Con «Arma tu pack» eliges solo lo que te hace falta."),
    ("¿El CRM de ContrataLux es una plantilla o está hecho a medida?", "Está hecho a medida para el sector energético: gestiona luz, gas, dual, fibra, alarmas y CAEs, las comisiones de cada comercial y las retrocomisiones. Usamos la misma base modular que nuestro programa de gestión y la adaptamos al sector."),
    ("¿Cómo se consigue que Google y Bing lean una web nueva desde el principio?", "Con un índice de sitemaps bien estructurado, enviado en Google Search Console y Bing Webmaster Tools el mismo día que se publica la web. En ContrataLux los dos buscadores leyeron los sitemaps sin errores y descubrieron sus 251 URLs."),
    ("¿Los datos de las capturas son de clientes reales?", "No. Todas las capturas y el vídeo usan datos de demostración, con nombres como «Demo 11 Cliente», para no exponer información de nadie."),
]

VIDEO = {"archivo": "contratalux-demo.mp4", "poster": "contratalux-demo-poster.webp", "duracion": "PT20S", "subido": "2026-10-13T12:00:00+02:00",
         "nombre": "Recorrido por el panel del CRM de ContrataLux",
         "desc": "Veinte segundos por el panel de dirección del programa de gestión de ContrataLux: avisos, contratos por estado, mix de cartera y actividad del equipo. Datos de demostración."}


def _svg_ruta():
    # Línea de tiempo animada: el trazo se dibuja al entrar en pantalla (casos.js) y se queda quieto
    n = len(PASOS); x0, x1 = 40, 1040; paso = (x1 - x0) / (n - 1)
    nodos = "".join(
        '<g class="cr-nodo" style="--i:%d"><circle cx="%.0f" cy="70" r="15"/><text x="%.0f" y="122" text-anchor="middle">%s</text></g>'
        % (i, x0 + i * paso, x0 + i * paso, t) for i, t in enumerate(PASOS))
    return ('<svg class="cr-ruta" viewBox="0 0 1080 140" role="img" aria-label="Orden del lanzamiento de ContrataLux: %s">'
            '<path class="cr-linea" d="M%d 70H%d" pathLength="1"/>%s</svg>' % (", ".join(PASOS), x0, x1, nodos))


def html_caso(c, r, migas_html, faq_html, cta_html):
    m = r + MEDIA
    servicios = "".join(
        '<a class="tarjeta cr-serv" href="%s%s"><span class="num">%02d</span><h3>%s</h3><p>%s</p><span class="mas">Ver el servicio →</span></a>' % (r, h, i, t, d)
        for i, (t, d, h) in enumerate(SERVICIOS, 1))
    capturas = "".join(
        '<figure class="cr-fig"><img src="%s%s" alt="%s" width="1280" height="720" loading="lazy" decoding="async"><figcaption>%s</figcaption></figure>' % (m, f, a, p)
        for f, a, p in CAPTURAS)
    return """<section class="page-hero"><div class="w">{migas}<p class="kicker">Caso de éxito · {sector}</p><h1>{h1}</h1>
<p class="lead">Un lanzamiento digital completo, hecho de principio a fin por Studio Emprende: marca, dominio y correo, web con SEO, Google y Bing, redes con contenido automatizado y un programa de gestión a medida.</p>
<div class="cr-cliente"><img src="{m}contratalux-logo.svg" alt="Logotipo de ContrataLux, software para asesorías energéticas" width="310" height="100"><a href="{web}" target="_blank" rel="noopener">contratalux.com ↗</a></div><p class="cr-nota">Proyecto desarrollado para una empresa del mismo grupo.</p></div></section>

<section class="sec" style="padding-bottom:0"><div class="w"><div class="respuesta"><p class="kicker" style="margin:0 0 6px">Resumen</p><p style="margin:0">{resumen}</p></div></div></section>

<section class="sec sec-noche"><div class="w cifras">
<div class="cifra"><b>7</b><span>Servicios en un mismo proyecto</span></div>
<div class="cifra"><b>251</b><span>URLs descubiertas por Google y Bing</span></div>
<div class="cifra"><b>10</b><span>Sitemaps, uno por sección</span></div>
<div class="cifra"><b>0</b><span>Errores de sitemap en los dos buscadores</span></div>
</div></section>

<section class="sec"><div class="w"><div class="cab"><p class="kicker">El punto de partida</p><h2>¿Qué necesitaba ContrataLux?</h2></div>
<div class="bloque"><div class="bloque-txt">
<p>ContrataLux nacía como un programa de gestión para asesorías energéticas, agencias y redes comerciales que venden luz, gas, fibra, alarmas y certificados de ahorro energético (CAEs). Tenía claro el producto y el cliente, pero no tenía nada de lo que hace falta para venderlo: ni marca, ni web, ni presencia en buscadores, ni redes, ni el propio software terminado.</p>
<p>Las asesorías energéticas trabajan hoy con Excel, WhatsApp sueltos y hojas de comisiones. Para convencerlas de cambiar, ContrataLux necesitaba parecer desde el primer día lo que es: una herramienta seria, hecha para su sector, que se puede probar sin compromiso.</p>
<p>El encargo fue hacerlo todo, en orden y con un único interlocutor, para que cada pieza se apoyara en la anterior.</p>
</div><div class="bloque-vis"><img class="cr-icono" src="{m}contratalux-icono-app.svg" alt="Icono de la app de ContrataLux en versión oscura" width="200" height="200" loading="lazy"></div></div></div></section>

<section class="sec sec-suave"><div class="w"><div class="cab"><p class="kicker">Cómo lo hicimos</p><h2>Siete piezas, en este orden</h2></div>
{ruta}
<p class="lead" style="margin-top:18px">El orden importa: primero la marca, porque todo lo demás la usa; luego el dominio y el correo, porque la web y las redes se registran con ellos; la web antes que los buscadores, y las redes cuando ya hay una web a la que llevar tráfico.</p>
<div class="rejilla" style="margin-top:28px">{servicios}</div></div></section>

<section class="sec"><div class="w"><div class="cab"><p class="kicker">Identidad</p><h2>Una marca pensada para el sector energético</h2></div>
<div class="bloque"><div class="bloque-txt">
<p>El símbolo es un sol que sale sobre el horizonte: energía, pero también el «amanecer» de una asesoría que deja el Excel. Las dos líneas, turquesa y azul, representan la luz y el gas, los dos suministros con los que trabaja casi todo el sector.</p>
<p>Entregamos el kit completo: logotipo horizontal y vertical, versión clara y oscura, icono de app y favicon. Es el mismo sistema que se ve en la web, en el programa, en la portada de Facebook y en cada publicación de LinkedIn.</p>
</div><div class="bloque-vis cr-marca"><img src="{m}contratalux-icono-app-claro.svg" alt="Icono de ContrataLux en versión clara" width="120" height="120" loading="lazy"><img src="{m}contratalux-icono-app.svg" alt="Icono de ContrataLux en versión oscura" width="120" height="120" loading="lazy"></div></div></div></section>

<section class="sec sec-suave"><div class="w"><div class="cab"><p class="kicker">Web y buscadores</p><h2>Una web de 251 URLs que Google y Bing leyeron sin errores</h2></div>
<p>No hicimos una web de cinco páginas. Organizamos contratalux.com como lo hacen los sitios que posicionan en su nicho, con una sección por cada forma en que una asesoría busca una solución:</p>
<ul class="lista" style="margin:14px 0 18px">
<li><strong>Funciones del programa</strong>: contratos, comisiones, retrocomisiones, liquidaciones, CAEs, área del cliente.</li>
<li><strong>Integraciones</strong> con cada comercializadora: Naturgy, Iberdrola, Endesa, Repsol, TotalEnergies.</li>
<li><strong>Herramientas gratuitas</strong>: calculadoras de factura 2.0TD, 3.0TD y 6.1TD, de gas, de comisiones y un comparador de tarifas.</li>
<li><strong>Soluciones por tipo de cliente</strong>: agentes energéticos, franquicias, administradores de fincas, instaladores fotovoltaicos, corredurías.</li>
<li><strong>Zonas</strong> por comunidad autónoma y <strong>suministros</strong>: luz, gas, dual, fibra, alarmas y CAEs.</li>
</ul>
<p>Cada sección tiene su propio sitemap colgando de un índice. Enviamos ese índice a <strong>Bing Webmaster Tools el 15 de octubre de 2026</strong> y a <strong>Google Search Console el 16 de octubre</strong>. A 24 de octubre, los dos buscadores lo han leído con estado «Correcto», sin errores ni advertencias, y han descubierto las 251 URLs. Al estar separado por secciones, se ve qué parte de la web entra en el índice y cuál necesita más trabajo.</p>
<p>Es la misma forma de trabajar que aplicamos en nuestras <a href="{r}servicios/webs/web-corporativa-con-seo.html">webs corporativas con SEO</a> y en el <a href="{r}servicios/presencia-digital/seo-programatico.html">SEO programático</a>.</p></div></section>

<section class="sec"><div class="w"><div class="cab"><p class="kicker">Programa de gestión</p><h2>Un CRM hecho para cómo trabaja una asesoría energética</h2></div>
<p>El corazón del proyecto es el propio software. Partimos de la base modular de nuestro <a href="{r}servicios/software-de-gestion/index.html">programa de gestión</a> y lo convertimos en un CRM sectorial:</p>
<ul class="lista" style="margin:14px 0 18px">
<li>Contratos de luz, gas, dual, fibra, alarmas y CAEs en una tabla en tiempo real, con Kanban, calendario y cronología de cada contrato.</li>
<li>Comisiones por contrato: bruta, neta para la empresa y repartida entre comerciales, con los <a href="{r}servicios/software-de-gestion/comerciales-y-comisiones.html">comerciales y comisiones</a> calculados solos.</li>
<li>Días de retrocomisión pendientes en cada contrato, para saber qué baja costaría dinero.</li>
<li>Calculadora de ahorro y comparador de tarifas para enseñar al cliente cuánto ahorra.</li>
<li>Usuarios con permisos, doble factor de acceso y revisión de cada contrato antes de enviarlo a la comercializadora.</li>
<li><a href="{r}servicios/pix/index.html">PIX</a>, el agente de IA, dentro del programa para consultar y automatizar en lenguaje normal.</li>
</ul>
<figure class="cr-video"><video controls muted playsinline preload="none" poster="{m}{vposter}" width="1280" height="720"><source src="{m}{varchivo}" type="video/mp4"></video><figcaption>{vdesc}</figcaption></figure>
<div class="cr-galeria">{capturas}</div></div></section>

<section class="sec sec-suave"><div class="w"><div class="cab"><p class="kicker">Redes</p><h2>Perfiles de empresa con contenido que se publica solo</h2></div>
<div class="bloque"><div class="bloque-txt">
<p>Creamos, optimizamos y configuramos la página de empresa de ContrataLux en <strong>Facebook</strong>, con su portada, su descripción y su portafolio, y en <strong>Instagram</strong> y <strong>LinkedIn</strong>, todas con la misma identidad.</p>
<p>Después llegó el contenido: reels y carruseles que hablan de los problemas reales de una asesoría («¿cuántos días te quedan de retrocomisión?», «tu catálogo, con tus comercializadoras») y un calendario de publicación automatizado. Cada publicación lleva a una página concreta de la web, que es la que convierte.</p>
<p>Es lo que hacemos en <a href="{r}servicios/presencia-digital/automatizacion-de-redes-sociales.html">automatización de redes sociales</a> y en <a href="{r}servicios/presencia-digital/videos-y-anuncios-con-ia.html">vídeos y anuncios con IA</a>.</p>
</div><div class="bloque-vis"><a class="tarjeta" href="https://www.linkedin.com/company/contratalux/" target="_blank" rel="noopener" style="max-width:340px"><h3>ContrataLux en LinkedIn</h3><p>Página de empresa con publicaciones periódicas para asesorías energéticas.</p><span class="mas">Ver la página ↗</span></a></div></div></div></section>

<section class="sec"><div class="w"><div class="cab"><p class="kicker">Lo que aprendimos</p><h2>Qué puedes aplicar a tu negocio</h2></div><div class="rejilla">
<div class="tarjeta"><h3>Un solo interlocutor</h3><p>Marca, web, redes y software hechos por el mismo equipo encajan entre sí. No hay que coordinar a cuatro proveedores.</p></div>
<div class="tarjeta"><h3>Estructura antes que volumen</h3><p>Una web nueva sin autoridad entra en Google mejor si está ordenada por secciones con sus sitemaps desde el primer día.</p></div>
<div class="tarjeta"><h3>Medir desde el día uno</h3><p>Search Console y Bing Webmaster Tools dados de alta al publicar: así sabes qué se indexa y qué no, en vez de suponerlo.</p></div>
</div></div></section>

<section class="sec sec-suave"><div class="w"><div class="cab"><p class="kicker">Preguntas frecuentes</p><h2>Sobre este caso</h2></div>{faq}</div></section>
<section class="sec"><div class="w" style="display:flex;flex-wrap:wrap;gap:24px;justify-content:space-between;align-items:center"><div style="flex:999 1 420px;min-width:0"><p class="kicker">Tu proyecto</p><h2>¿Quieres un lanzamiento así para tu negocio?</h2><p class="lead" style="margin-top:12px">Cuéntanos tu idea y te decimos qué piezas necesitas y en qué orden, con plazo y precio cerrados.</p></div><a class="btn btn-p" href="{r}contacto.html?servicio=caso-contratalux#diagnostico">Pedir diagnóstico gratis</a></div></section>
{cta}<script src="{r}assets/js/casos.js" defer></script>""".format(
        migas=migas_html, sector=c["sector"], h1=c["h1"], m=m, web=c["web"], resumen=c["resumen"], ruta=_svg_ruta(),
        servicios=servicios, capturas=capturas, r=r, faq=faq_html, cta=cta_html,
        vposter=VIDEO["poster"], varchivo=VIDEO["archivo"], vdesc=VIDEO["desc"])


def ld_caso(c, dom):
    url = "%s/casos/%s" % (dom, c["slug"])
    m = dom + "/" + MEDIA
    cliente = {"@type": "Organization", "@id": c["web"] + "#org", "name": c["nombre"], "url": c["web"],
               "logo": m + "contratalux-logo.svg", "sameAs": ["https://www.linkedin.com/company/contratalux/"]}
    articulo = {"@type": "Article", "@id": url + "#caso", "headline": c["h1"], "description": c["meta"],
                "datePublished": c["fecha"], "dateModified": "__FMOD__", "inLanguage": "es",
                "author": {"@id": dom + "/#org"}, "publisher": {"@id": dom + "/#org"}, "mainEntityOfPage": {"@id": url},
                "about": {"@id": c["web"] + "#org"}, "image": [m + f for f, _, _ in CAPTURAS],
                "video": {"@id": url + "#video"}}
    video = {"@type": "VideoObject", "@id": url + "#video", "name": VIDEO["nombre"], "description": VIDEO["desc"],
             "thumbnailUrl": m + VIDEO["poster"], "contentUrl": m + VIDEO["archivo"], "uploadDate": VIDEO["subido"],
             "duration": VIDEO["duracion"], "inLanguage": "es"}
    imagenes = [{"@type": "ImageObject", "contentUrl": m + f, "caption": p, "width": 1280, "height": 720} for f, _, p in CAPTURAS]
    return [cliente, articulo, video] + imagenes


def html_hub(r, migas_html, casos, cta_html):
    tarjetas = "".join(
        '<a class="tarjeta" href="%scasos/%s.html"><img src="%s%scontratalux-panel.webp" alt="Panel del CRM de %s" width="1280" height="720" loading="lazy" style="border-radius:10px"><span class="etiqueta">%s</span><h3>%s</h3><p>%s</p><span class="mas">Leer el caso →</span></a>'
        % (r, c["slug"], r, MEDIA, c["nombre"], c["sector"], c["titulo"].replace("Caso ", ""), c["meta"]) for c in casos)
    return """<section class="page-hero"><div class="w">{migas}<p class="kicker">Casos de éxito</p><h1>Casos de éxito: proyectos reales de software, web y SEO</h1>
<p class="lead">Proyectos que hemos hecho de principio a fin, contados con lo que se hizo, en qué orden y qué datos podemos enseñar. Sin cifras infladas: lo que no se puede medir, no lo contamos.</p></div></section>
<section class="sec"><div class="w"><div class="rejilla">{tarjetas}</div></div></section>
<section class="sec"><div class="w"><div class="cab"><p class="kicker">Por qué los publicamos</p><h2>Casos de éxito con datos que se pueden comprobar</h2></div>
<p>Cuando eliges a quién encargar tu web, tu programa de gestión o tu agente de IA, lo que más ayuda es ver un proyecto parecido terminado: qué había al principio, qué se hizo, en qué orden y qué resultado se puede medir. Por eso cada caso incluye capturas del producto con datos de demostración, enlaces a la web real del proyecto y, cuando existen, las cifras de Google Search Console o Bing Webmaster Tools.</p>
<p>El primer caso es <a href="contratalux.html">ContrataLux</a>, un software para asesorías energéticas al que hicimos todo el lanzamiento: identidad de marca, dominio y correo, una web de 251 URLs leída sin errores por Google y Bing, perfiles en redes con contenido automatizado y un CRM a medida para gestionar contratos y comisiones. Es un buen ejemplo de lo que incluye un <a href="../precios.html">pack completo</a> cuando se hace con un único interlocutor.</p>
<p>Si tu proyecto se parece a alguno de estos, en el <a href="../contacto.html#diagnostico">diagnóstico gratuito</a> te decimos qué piezas necesitas y en qué orden.</p></div></section>
<section class="sec sec-suave"><div class="w"><div class="cab"><p class="kicker">Cómo los contamos</p><h2>Qué encontrarás en cada caso</h2></div><div class="rejilla">
<div class="tarjeta"><h3>El punto de partida</h3><p>Qué tenía el negocio y qué le faltaba antes de empezar.</p></div>
<div class="tarjeta"><h3>Lo que hicimos y en qué orden</h3><p>Cada servicio, enlazado a su página, para que veas qué incluye.</p></div>
<div class="tarjeta"><h3>Capturas y datos comprobables</h3><p>Pantallas del producto con datos de demostración y cifras de Search Console o Bing cuando las hay.</p></div>
</div></div></section>
{cta}""".format(migas=migas_html, tarjetas=tarjetas, cta=cta_html)


def bloque_entrante(r, texto):
    return ('<section class="sec" style="padding-top:0"><div class="w"><a class="tarjeta" href="%scasos/contratalux.html" style="flex-direction:row;flex-wrap:wrap;align-items:center;gap:18px">'
            '<img src="%s%scontratalux-icono-app-claro.svg" alt="" width="64" height="64" loading="lazy">'
            '<span style="flex:1 1 260px;display:flex;flex-direction:column;gap:6px"><span class="kicker" style="margin:0">Caso real</span><b style="font-weight:500">%s</b></span>'
            '<span class="mas">Ver el caso ContrataLux →</span></a></div></section>' % (r, r, MEDIA, texto))
