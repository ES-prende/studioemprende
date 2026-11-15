# Portada centrada en las personas: tres caminos, problemas reales, beneficios, cómo acompañamos,
# historia, servicios por resultados, pruebas de confianza y formulario breve.
# El contenido SEO que ya tenía la portada (sectores, normativas, blog, preguntas) se conserva debajo.

TITULO = "Studio Emprende · De tu primera idea a un negocio que crece"
META = "Te ayudamos a emprender, dar tus primeros pasos o mejorar tu negocio: presencia profesional, clientes, organización y tiempo. Para toda España."

CAMINOS = [
    ("idea", "Tengo una idea y quiero emprender",
     "Tienes una idea, pero no sabes exactamente por dónde empezar. Te ayudamos a darle forma, identificar tus primeras necesidades y construir una presencia profesional para ponerla en marcha.",
     "Quiero empezar", "Tengo una idea"),
    ("pasos", "Estoy dando mis primeros pasos",
     "Ya has comenzado, pero necesitas darte a conocer, encontrar clientes, organizarte mejor y construir una base sólida. Te ayudamos a avanzar sin complicaciones innecesarias.",
     "Quiero impulsar mi proyecto", "Estoy empezando"),
    ("negocio", "Ya tengo un negocio",
     "Has llegado hasta aquí con esfuerzo, pero sabes que todavía puedes mejorar. Te ayudamos a optimizar procesos, ganar tiempo, aumentar tu visibilidad y preparar tu empresa para seguir creciendo.",
     "Quiero mejorar mi negocio", "Ya tengo un negocio"),
]

PROBLEMAS = [
    "Tengo una idea, pero no sé cómo empezar.",
    "Trabajo muchas horas y siento que no avanzo.",
    "Necesito conseguir clientes, pero no sé cómo.",
    "Mi negocio depende demasiado de mí.",
    "Tengo demasiadas tareas y poco tiempo.",
    "No sé en qué merece la pena invertir.",
    "Necesito ayuda, pero no sé a quién acudir.",
]

BENEFICIOS = [
    ("Empieza con más confianza", "Ten claridad sobre tus primeros pasos y evita complicaciones innecesarias."),
    ("Hazte visible", "Consigue que más personas conozcan tu proyecto y puedan descubrir lo que ofreces."),
    ("Aprovecha mejor tu tiempo", "Reduce tareas repetitivas y céntrate en las actividades que aportan valor."),
    ("Trabaja con más organización", "Mantén la información de tu negocio ordenada y accesible."),
    ("Toma decisiones con más claridad", "Conoce mejor lo que ocurre en tu negocio y descubre dónde mejorar."),
    ("Crece a tu ritmo", "Empieza por lo que necesitas hoy y añade nuevas soluciones cuando tenga sentido."),
]

FASES = [
    ("Te escuchamos", "Conocemos tu idea, tu situación, tus objetivos y tus dificultades."),
    ("Encontramos oportunidades", "Analizamos dónde podemos ayudarte y qué conviene priorizar."),
    ("Ponemos soluciones en marcha", "Diseñamos e implementamos las soluciones acordadas, adaptadas a tus necesidades."),
    ("Te acompañamos", "Te explicamos cómo utilizarlas y ofrecemos el seguimiento y soporte que hayas contratado."),
]

# (resultado, beneficio, herramienta, [(texto, enlace)])
SERVICIOS = [
    ("Crear tu presencia profesional", "Que quien te busque encuentre un negocio serio desde el primer día.",
     "Identidad, páginas web, tiendas online y soluciones para lanzar proyectos.",
     [("Webs con SEO", "servicios/webs.html"), ("Presencia digital", "servicios/presencia-digital.html"), ("Para autónomos", "servicios/autonomos.html")]),
    ("Atraer nuevas oportunidades", "Que más personas conozcan lo que ofreces y te escriban.",
     "Visibilidad, posicionamiento, marketing y captación.",
     [("Presencia digital y crecimiento", "servicios/presencia-digital.html"), ("WhatsApp con IA", "servicios/whatsapp-ia.html")]),
    ("Organizar mejor tu negocio", "Clientes, ventas y papeles en un solo sitio, sin depender de la memoria.",
     "CRM a medida, gestión comercial y herramientas empresariales.",
     [("Programa de gestión", "servicios/software-de-gestion.html"), ("ERP para pymes", "servicios/erp-para-pymes.html"), ("Fichador", "servicios/fichador.html")]),
    ("Recuperar tiempo", "Menos tareas repetidas y más horas para lo que solo puedes hacer tú.",
     "Automatizaciones y asistentes de inteligencia artificial.",
     [("Agentes de IA", "servicios/agentes-de-ia.html"), ("Automatización y datos", "servicios/automatizacion-y-datos.html")]),
    ("Aprender y avanzar", "Entender lo que usas y decidir con criterio, con alguien a tu lado.",
     "Formación, orientación y acompañamiento tecnológico.",
     [("Formación en IA", "servicios/formacion-ia.html"), ("Departamento tecnológico", "servicios/departamento-tecnologico.html")]),
    ("Adaptarte a nuevas necesidades", "Si lo que necesitas no existe, se construye a tu medida.",
     "Desarrollo de soluciones a medida e integraciones.",
     [("Software especializado", "servicios/software-especializado.html"), ("Migraciones e integraciones", "servicios/migraciones-e-integraciones.html"), ("Apps móviles", "servicios/apps-moviles.html")]),
]

HUECOS = [
    ("Nuevo caso en preparación", "Estamos documentando el siguiente proyecto: punto de partida, lo que hicimos y los datos que se pueden comprobar."),
    ("Tu proyecto puede ser el próximo", "Cuéntanos en qué punto estás y vemos juntos cuál es el siguiente paso."),
]


def html(e, dom, formador, sectores, blog, faq, existe):
    caminos = "".join(
        '<div class="tarjeta ini-camino"><span class="ini-paso">%02d</span><h3>%s</h3><p>%s</p><a class="btn btn-p" href="#contacto" data-perfil="%s">%s</a></div>'
        % (i + 1, e(t), e(d), e(v), e(c)) for i, (_, t, d, c, v) in enumerate(CAMINOS))
    problemas = "".join('<li>«%s»</li>' % e(p[:-1]) for p in PROBLEMAS)
    beneficios = "".join('<div class="tarjeta"><h3>%s</h3><p>%s</p></div>' % (e(t), e(d)) for t, d in BENEFICIOS)
    fases = "".join('<li class="tarjeta"><h3>%s</h3><p>%s</p></li>' % (e(t), e(d)) for t, d in FASES)
    servicios = "".join(
        '<div class="tarjeta"><h3>%s</h3><p class="ini-benef">%s</p><p>%s</p><ul class="lista" style="margin-top:6px">%s</ul></div>'
        % (e(t), e(b), e(h), "".join('<li><a href="%s">%s</a></li>' % (u, e(n)) for n, u in ls if existe(u)))
        for t, b, h, ls in SERVICIOS)
    # Huecos para los próximos casos: al publicar uno nuevo, se sustituye un hueco por su tarjeta
    huecos = ''.join('<div class="tarjeta ini-hueco"><span class="etiqueta">Próximamente</span><h3>%s</h3><p>%s</p><a class="mas" href="#contacto">Quiero que el siguiente sea el mío →</a></div>' % (e(t), e(d)) for t, d in HUECOS)
    opciones = "".join('<option>%s</option>' % e(v) for _, _, _, _, v in CAMINOS)
    return """<div class="ini">
<section class="hero ini-hero"><div class="w"><div class="hero-txt">
<h1>Tu negocio, <span class="acento">llave en mano</span>.</h1>
<p class="ini-apoyo">De tu primera idea a un negocio que crece</p>
<p class="lead">Tanto si sueñas con emprender como si estás dando tus primeros pasos o ya tienes un negocio en marcha, en Studio Emprende te ayudamos a avanzar.</p>
<p class="lead">Escuchamos tus ideas, entendemos tus dificultades y buscamos contigo las soluciones que necesitas para empezar, mejorar y crecer.</p>
<p class="lead">Queremos que tengas más claridad, más oportunidades y menos complicaciones. Porque detrás de cada negocio hay una persona que necesita apoyo, orientación y soluciones reales.</p>
<div class="botones"><a class="btn btn-p" href="#contacto">Cuéntanos tu proyecto</a><a class="btn btn-s" href="#caminos">Descubre cómo podemos ayudarte</a></div>
</div></div></section>

<section class="sec sec-suave" id="caminos"><div class="w">
<div class="cab"><p class="kicker">Tu punto de partida</p><h2>Estés donde estés, podemos ayudarte a dar el siguiente paso</h2></div>
<div class="rejilla">{caminos}</div>
</div></section>

<section class="sec"><div class="w ini-dos">
<div><div class="cab"><p class="kicker">Te entendemos</p><h2>Sabemos que emprender y sacar adelante un negocio no siempre es fácil</h2></div>
<p class="lead">No tienes que resolverlo todo por tu cuenta. Estamos aquí para escucharte, orientarte y ayudarte a encontrar el mejor camino para tu proyecto.</p>
<p style="margin-top:22px"><a class="btn btn-s" href="#contacto">Cuéntanos tu caso</a></p></div>
<ul class="ini-frases">{problemas}</ul>
</div></section>

<section class="sec sec-suave"><div class="w">
<div class="cab"><p class="kicker">Lo que consigues</p><h2>Queremos que tu negocio te dé oportunidades, no más preocupaciones</h2></div>
<div class="rejilla ini-benefs">{beneficios}</div>
</div></section>

<section class="sec sec-noche"><div class="w">
<div class="cab"><p class="kicker">Cómo te acompañamos</p><h2>No necesitas saber qué herramientas contratar. Primero queremos entenderte</h2></div>
<ol class="rejilla ini-fases">{fases}</ol>
</div></section>

<section class="sec"><div class="w ini-dos">
<div><div class="cab"><p class="kicker">Nuestra historia</p><h2>Sabemos lo que supone emprender, porque también hemos recorrido ese camino</h2></div>
<p>Studio Emprende nace de nuestra propia experiencia al emprender. Pasamos por cursos milagro que solo nos quitaron tiempo y dinero, por horas montando herramientas improvisadas que nadie podía mantener, por datos de clientes repartidos entre el móvil y el correo, y por una web hecha deprisa que no traía clientes.</p>
<p style="margin-top:14px">Aprendimos a base de equivocarnos. Y entendimos que el problema no era la falta de ganas, sino empezar sin una base sólida. Creamos Studio Emprende para que no tengas que pasar por lo mismo, con alguien a tu lado que conoce tu negocio.</p>
<p style="margin-top:18px"><a href="sobre-nosotros.html">Conoce nuestra historia y al equipo →</a></p></div>
<div>{formador}</div>
</div></section>

<section class="sec sec-suave" id="servicios"><div class="w">
<div class="cab"><p class="kicker">Servicios</p><h2>Todo lo que necesitas para poner en marcha, mejorar o hacer crecer tu negocio</h2></div>
<div class="rejilla ini-serv">{servicios}</div>
<div class="ini-banda"><p>Las soluciones se adaptan a tu etapa: empiezas por lo que necesitas hoy y añades lo demás cuando tenga sentido. Los packs, sus cuotas y lo que incluye cada uno están explicados en la página de precios.</p>
<div class="botones"><a class="btn btn-p" href="#contacto">Descubre qué necesitas para empezar</a><a class="btn btn-s" href="servicios/index.html">Ver todos los servicios</a><a class="btn btn-s" href="precios.html">Ver precios y packs</a></div></div>
</div></section>

<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Confianza</p><h2>Proyectos, personas y soluciones reales</h2><p class="lead" style="margin-top:8px">Contamos cada proyecto con lo que se hizo, en qué orden y los datos que se pueden comprobar. Sin cifras infladas.</p></div>
<div class="rejilla ini-casos">
<a class="tarjeta" href="casos/contratalux.html"><img src="assets/img/casos/contratalux-panel.webp" alt="Panel del programa de gestión de ContrataLux" width="1280" height="720" loading="lazy" decoding="async" style="border-radius:10px"><span class="etiqueta">Asesorías energéticas</span><h3>ContrataLux: de la idea al lanzamiento completo</h3><p><b>El problema:</b> un proyecto nuevo sin marca, web ni herramienta para gestionar contratos y comisiones.</p><p><b>La solución:</b> identidad, dominio y correo, web preparada para buscadores, redes y un programa de gestión a medida.</p><span class="mas">Leer el caso →</span></a>
{huecos}
</div>
<p style="margin-top:28px"><a class="btn btn-s" href="casos/index.html">Ver todos los casos</a></p>
</div></section>

<section class="sec sec-suave"><div class="w">
<div class="cab"><p class="kicker">Para tu sector</p><h2>Soluciones pensadas para tu día a día</h2></div>
<div class="pildoras">{sectores}</div>
</div></section>

<section class="sec"><div class="w" style="display:flex;flex-wrap:wrap;gap:32px;justify-content:space-between;align-items:center">
<div style="flex:999 1 420px;min-width:0"><p class="kicker">Normativas 2026-2027</p><h2>¿Te afecta Verifactu, el fichaje digital o el AI Act?</h2><p class="lead" style="margin-top:12px">Depende de tu forma jurídica y tu actividad. Verifactu: 1/1/2027 para sociedades y 1/7/2027 para el resto, con un aplazamiento a octubre de 2028 anunciado y pendiente de BOE. Factura electrónica B2B: 6/10/2027 o 6/10/2028 según facturación. Formación en IA: obligatoria desde el 2/2/2025. Registro de jornada: desde 2019.</p><p class="mut" style="margin-top:10px;font-size:14px">Fuentes oficiales: <a href="https://www.boe.es/eli/es/rd/2023/12/05/1007" target="_blank" rel="noopener">RD 1007/2023 (Verifactu)</a>, <a href="https://www.boe.es/eli/es/l/2022/09/28/18" target="_blank" rel="noopener">Ley 18/2022 (factura electrónica)</a>, <a href="https://eur-lex.europa.eu/eli/reg/2024/1689/oj" target="_blank" rel="noopener">Reglamento (UE) 2024/1689 (AI Act)</a> y <a href="https://www.boe.es/eli/es/rdl/2019/03/08/8" target="_blank" rel="noopener">RDL 8/2019 (registro de jornada)</a>. Normativa revisada el <time datetime="2026-10-12">12 de octubre de 2026</time>.</p><p style="margin-top:6px"><a href="normativas.html">Ver todas las normas, plazos y fuentes oficiales →</a></p></div>
<a class="btn btn-s" href="normativas.html">Ver normativas</a>
</div></section>

<section class="sec sec-suave"><div class="w"><div class="cab"><p class="kicker">Blog</p><h2>Ideas claras para tu negocio</h2></div><div class="rejilla">{blog}</div><p style="margin-top:28px"><a class="btn btn-s" href="blog/index.html">Ver todos los artículos</a></p></div></section>
<section class="sec"><div class="w"><div class="cab"><p class="kicker">Preguntas frecuentes</p><h2>Lo que más nos preguntan</h2></div>{faq}</div></section>

<section class="sec sec-suave" id="contacto"><div class="w lateral"><div class="lateral-main ini-form">
<div class="cab"><p class="kicker">Hablemos de tu proyecto</p><h2>No importa si todavía es una idea o si tu negocio ya lleva años funcionando</h2>
<p class="lead" style="margin-top:8px">Cada proyecto tiene una historia, unas dificultades y unos objetivos diferentes.</p>
<p class="lead">Cuéntanos en qué punto estás y qué te gustaría conseguir. Queremos escucharte y ayudarte a encontrar el siguiente paso.</p>
<p class="lead">No tienes que llegar con todas las respuestas. Para eso estamos aquí.</p></div>
<form class="form" data-contacto action="https://formsubmit.co/info@studioemprende.com" method="post">
<input type="hidden" name="_subject" value="Nuevo contacto desde la portada de studioemprende.com">
<input type="hidden" name="_cc" value="socialstudioemprende@gmail.com">
<input type="hidden" name="_template" value="table">
<input type="hidden" name="_next" value="{dom}/gracias.html">
<input type="hidden" name="origen" value="portada">
<input type="hidden" name="_captcha" value="true">
<input type="hidden" name="_blacklist" value="viagra, casino, crypto, bitcoin, forex, loan, seo services, backlinks, porn, betting, http://, https://bit.ly">
<input type="hidden" name="_autoresponse" value="Hola, hemos recibido tu mensaje en Studio Emprende. Te respondemos en menos de 24 horas laborables. Si es urgente, escríbenos por WhatsApp al 601 86 96 68.">
<input type="hidden" name="_t" id="_t" value="">
<div aria-hidden="true" style="position:absolute;left:-10000px;top:auto;width:1px;height:1px;overflow:hidden"><label>No rellenar<input type="text" name="_honey" tabindex="-1" autocomplete="off"></label><label>Web<input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
<p class="form-aviso" id="form-aviso" role="alert" hidden></p>
<div class="dos"><div class="campo"><label for="nombre">Nombre</label><input id="nombre" name="nombre" autocomplete="name" required minlength="2" maxlength="80" pattern=".*\\S.*"><span class="error" hidden style="color:#A3222F;font-size:13px">Escribe tu nombre</span></div>
<div class="campo"><label for="email">Correo electrónico</label><input id="email" name="email" type="email" autocomplete="email" required maxlength="120"><span class="error" hidden style="color:#A3222F;font-size:13px">Escribe tu correo</span></div></div>
<div class="dos"><div class="campo"><label for="telefono">Teléfono (opcional)</label><input id="telefono" name="telefono" type="tel" autocomplete="tel" inputmode="tel" maxlength="20" pattern="[+0-9 .\\(\\)\\-]{{9,20}}" title="Solo números, mínimo 9 cifras"></div>
<div class="campo"><label for="punto">¿En qué punto estás?</label><select id="punto" name="punto" required><option value="">Elige una opción</option>{opciones}</select><span class="error" hidden style="color:#A3222F;font-size:13px">Elige una opción</span></div></div>
<div class="campo"><label for="mensaje">¿En qué necesitas ayuda?</label><textarea id="mensaje" name="mensaje" rows="5" maxlength="2000" aria-describedby="mensaje-ayuda"></textarea><span id="mensaje-ayuda" class="mut" style="font-size:13px">Basta con unas líneas. No incluyas datos de salud ni otros datos sensibles.</span></div>
<label style="display:flex;gap:10px;font-size:14px;align-items:flex-start"><input type="checkbox" name="privacidad" required style="margin-top:4px"> <span>He leído y acepto la <a href="privacidad.html">política de privacidad</a>.</span></label>
<p class="mut" style="font-size:13px;margin:0">Responsable: INTELIGENCIA SEVILLA SL (Studio Emprende). Finalidad: responder a tu consulta. Base: tu consentimiento. Puedes ejercer tus derechos de acceso, rectificación y supresión en info@studioemprende.com.</p>
<div><button class="btn btn-p" type="submit">Hablemos de tu proyecto</button></div>
</form></div>
<aside class="lateral-aside"><h2 class="h3">Qué pasa después</h2>
<p style="color:#C9C1BB">1. Leemos lo que nos cuentas.</p>
<p style="color:#C9C1BB">2. Te respondemos en menos de 24 horas laborables.</p>
<p style="color:#C9C1BB">3. Hablamos de tu proyecto y de por dónde conviene empezar.</p>
<a class="btn btn-borde-claro" href="https://api.whatsapp.com/send/?phone=34601869668&text=Hola%2C%20quiero%20contaros%20mi%20proyecto&type=phone_number&app_absent=0" target="_blank" rel="noopener">Prefiero WhatsApp</a></aside>
</div></section>
</div>
<script>(function(){{var s=document.getElementById('punto');document.querySelectorAll('a[data-perfil]').forEach(function(a){{a.addEventListener('click',function(){{if(s)s.value=a.getAttribute('data-perfil')}})}});
var rd=matchMedia('(prefers-reduced-motion: reduce)').matches,els=document.querySelectorAll('.ini .tarjeta,.ini .cab,.ini-frases li');
if(!rd&&'IntersectionObserver' in window){{els.forEach(function(x){{x.classList.add('rv')}});var io=new IntersectionObserver(function(es){{es.forEach(function(x){{if(x.isIntersecting){{x.target.classList.add('si');io.unobserve(x.target)}}}})}},{{rootMargin:'0px 0px -6% 0px'}});els.forEach(function(x){{io.observe(x)}})}}}})();</script>""".format(
        caminos=caminos, problemas=problemas, beneficios=beneficios, fases=fases, servicios=servicios, opciones=opciones, huecos=huecos,
        formador=formador, sectores=sectores, blog=blog, faq=faq, dom=dom)
