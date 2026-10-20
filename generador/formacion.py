# Contenido de Formación en IA: página principal, sesión 1 a 1 y formador
DOM = "https://studioemprende.com"
WA = "https://wa.me/34601869668?text=Hola%2C%20quiero%20reservar%20una%20sesi%C3%B3n%20de%20IA%201%20a%201"

JORDAN = {"@type": "Person", "@id": DOM + "/sobre-nosotros#jordan-garcia", "name": "Jordan García",
          "jobTitle": "Formador de inteligencia artificial", "worksFor": {"@id": DOM + "/#org"},
          "affiliation": {"@id": DOM + "/#org"},
          "knowsAbout": ["Inteligencia artificial", "Prompt engineering", "ChatGPT", "Automatización de procesos", "Formación en IA para empresas"],
          "url": DOM + "/sobre-nosotros#equipo"}

JORDAN_BIO = ("Formador de inteligencia artificial en Studio Emprende, prompt engineer y CEO de Inteligencia Sevilla. Ha aplicado inteligencia artificial en 11 empresas distintas para resolver "
              "problemas reales, y todo lo que enseña lo ha usado antes en producción. Sus sesiones son prácticas de principio a fin: "
              "se trabaja sobre las tareas reales de cada persona, no sobre ejemplos de manual.")

def tarjeta_formador(r):
    return ('<div class="tarjeta formador"><div class="formador-av" aria-hidden="true">JG</div><div><p class="kicker" style="margin:0 0 4px">Tu formador</p>'
            '<h3 style="margin:0 0 8px">Jordan García</h3><p style="margin:0">%s</p>'
            '<p style="margin:10px 0 0"><a href="%ssobre-nosotros.html#equipo">Conoce al equipo →</a></p></div></div>') % (JORDAN_BIO, r)

# ---------- Página principal: servicios/formacion-ia.html ----------
HUB_FAQS = [
    ("¿Hace falta que el equipo sepa de tecnología?", "No. Empezamos desde el nivel de cada persona. Si alguien nunca ha abierto ChatGPT, se parte de ahí; si ya lo usa, se va directo a sus tareas."),
    ("¿Cuánto dura la formación?", "Depende de cuántas personas y áreas haya. Tras la entrevista previa te damos una propuesta cerrada con número de sesiones y calendario."),
    ("¿La formación en IA para equipos es online o presencial?", "Las dos. Online en directo para cualquier punto de España y presencial cuando el equipo lo prefiere."),
    ("¿Hay obligación legal de formar al equipo en IA?", "Sí, si tu empresa usa sistemas de IA. El artículo 4 del Reglamento europeo de IA (AI Act) exige desde el 2 de febrero de 2025 que el personal que los utiliza tenga un nivel suficiente de alfabetización en IA."),
    ("¿Entregáis materiales?", "Sí. Cada área se queda con sus instrucciones y ejemplos guardados, y la empresa con sus normas de uso de la IA por escrito."),
    ("¿Cuánto cuesta la formación en IA para empresas?", "La sesión individual cuesta desde 40 € la hora (sin IVA). La formación para equipos se presupuesta cerrada según el número de personas, áreas y horas, después de la entrevista previa."),
    ("¿La formación en IA es bonificable o subvencionada?", "Puede bonificarse con el crédito de formación que cada empresa tiene en FUNDAE, siempre que se comunique antes de empezar y se justifique la asistencia."),
    ("¿Hay formación en IA gratis?", "Hay cursos gratuitos que explican los conceptos básicos. Lo que no suelen ofrecer es práctica sobre las tareas de tu empresa ni normas de uso adaptadas, que es donde se nota el ahorro."),
    ("¿Formáis en ChatGPT, Copilot, Gemini y Claude?", "Sí. Trabajamos con la herramienta que ya tenga la empresa o ayudamos a elegir una según cómo trabajáis."),
    ("¿Y si solo soy yo, sin equipo?", "Para eso está la sesión de IA 1 a 1: una hora práctica sobre tu negocio desde 40 € la hora (sin IVA)."),
]

def hub_extra(r):
    """Bloques que se añaden a servicios/formacion-ia.html (r = ruta relativa a la raíz, '../')."""
    return """<section class="sec sec-suave"><div class="w"><div class="cab"><p class="kicker">El problema</p><h2>Por qué la formación en IA no suele calar</h2></div>
<div class="rejilla">
<div class="tarjeta"><h3>Se enseña la herramienta, no la tarea</h3><p>Una demostración de ChatGPT no le dice a nadie cómo hacer más rápido su trabajo del lunes. Por eso, a las dos semanas, nadie la usa.</p></div>
<div class="tarjeta"><h3>Se da lo mismo a todo el mundo</h3><p>Administración, comercial y dirección no necesitan lo mismo. Un curso único aburre a la mitad y se queda corto para la otra mitad.</p></div>
<div class="tarjeta"><h3>Nadie dice qué no se puede hacer</h3><p>Sin normas claras, alguien acaba pegando datos de clientes en una herramienta pública. La formación tiene que marcar los límites.</p></div>
</div></div></section>
<section class="sec"><div class="w"><div class="cab"><p class="kicker">Método</p><h2>Cómo la planteamos</h2></div>
<div class="rejilla">
<div class="tarjeta"><h3>1. Entrevista con cada área</h3><p>Antes de preparar nada, vemos qué tareas repite cada persona y cuáles le roban más tiempo.</p></div>
<div class="tarjeta"><h3>2. Sesión práctica en directo</h3><p>Cada uno trabaja sobre sus propios casos, delante de su ordenador. Sin diapositivas de relleno.</p></div>
<div class="tarjeta"><h3>3. Normas de uso de la empresa</h3><p>Dejamos por escrito qué herramientas se usan, qué datos no se meten nunca y quién revisa el resultado.</p></div>
<div class="tarjeta"><h3>4. Seguimiento</h3><p>A las pocas semanas revisamos qué se está usando de verdad y resolvemos las dudas que han ido saliendo.</p></div>
</div></div></section>
<section class="sec sec-suave"><div class="w"><div class="cab"><p class="kicker">Por áreas</p><h2>Qué se trabaja en cada área</h2></div>
<div class="rejilla">
<div class="tarjeta"><h3>Administración</h3><p>Correos y respuestas tipo, revisión de facturas y documentos, resúmenes y tablas a partir de datos sueltos.</p></div>
<div class="tarjeta"><h3>Comercial</h3><p>Propuestas y presupuestos más rápidos, seguimiento de clientes y respuestas a las preguntas de siempre.</p></div>
<div class="tarjeta"><h3>Operaciones</h3><p>Procedimientos escritos, partes e informes, y documentación interna que por fin está al día.</p></div>
<div class="tarjeta"><h3>Dirección</h3><p>Informes para decidir, preparación de reuniones y la política de uso de la IA en la empresa.</p></div>
</div></div></section>
<section class="sec"><div class="w"><div class="cab"><p class="kicker">Herramientas</p><h2>¿Con qué herramientas de IA trabajamos?</h2></div>
<p class="lead" style="max-width:760px;margin-bottom:20px">Formamos en la herramienta que ya uséis o os ayudamos a elegir una. Lo que cambia entre ellas lo explicamos en <a href="../blog/chatgpt-gemini-copilot-o-claude-para-empresas.html">ChatGPT, Gemini, Copilot o Claude: qué IA usar en tu empresa</a>.</p>
<div class="rejilla">
<div class="tarjeta"><h3>Formación en ChatGPT</h3><p>Instrucciones bien escritas, asistentes propios y análisis de documentos para el trabajo diario.</p></div>
<div class="tarjeta"><h3>Formación en Copilot</h3><p>IA dentro de Outlook, Word, Excel y Teams para empresas que trabajan con Microsoft 365.</p></div>
<div class="tarjeta"><h3>Formación en Gemini</h3><p>IA dentro de Gmail, Drive, Docs y Sheets para equipos que usan Google Workspace.</p></div>
<div class="tarjeta"><h3>Formación en Claude</h3><p>Trabajo con documentos largos, redacción cuidada y análisis detallados.</p></div>
</div></div></section>
<section class="sec sec-suave"><div class="w"><div class="cab"><p class="kicker">Por perfiles</p><h2>Formación en IA para cada perfil profesional</h2></div><div class="rejilla">
<div class="tarjeta"><h3>Directivos y empresarios</h3><p>Dónde aplicar la IA en el negocio, cómo medir el retorno y qué riesgos vigilar. Ver <a href="formacion-ia/mentoria-para-directivos.html">mentoría para directivos</a>.</p></div>
<div class="tarjeta"><h3>Recursos humanos</h3><p>Ofertas de empleo, cribado de candidaturas con criterio, planes de formación y comunicación interna.</p></div>
<div class="tarjeta"><h3>Abogados y despachos</h3><p>Resumen de documentos, borradores y búsqueda en expedientes sin comprometer la confidencialidad.</p></div>
<div class="tarjeta"><h3>Marketing y ventas</h3><p>Contenidos, campañas, propuestas comerciales y respuestas a clientes en la mitad de tiempo.</p></div>
<div class="tarjeta"><h3>Administración y finanzas</h3><p>Conciliaciones, informes, revisión de facturas y hojas de cálculo con ayuda de la IA.</p></div>
<div class="tarjeta"><h3>Autónomos y pymes</h3><p>Lo justo para ganar horas desde la primera semana. Ver <a href="formacion-ia/ia-para-autonomos-por-profesion.html">IA para autónomos por profesión</a>.</p></div>
</div></div></section>
<section class="sec"><div class="w"><div class="rejilla">
{formador}
<div class="tarjeta"><p class="kicker" style="margin:0 0 4px">Si estás solo en tu negocio</p><h3 style="margin:0 0 8px">Sesión de IA 1 a 1</h3><p style="margin:0">Una hora práctica sobre tu negocio, online o presencial en Sevilla capital. Desde 40 € la hora (sin IVA).</p><p style="margin:10px 0 0"><a href="formacion-ia/sesion-de-ia-1-a-1.html">Ver la sesión 1 a 1 →</a></p></div>
</div></div></section>
<section class="sec sec-suave"><div class="w"><div class="cab"><h2>Preguntas frecuentes</h2></div>{faq}</div></section>"""

def curso_hub():
    return {"@type": "Course", "@id": DOM + "/servicios/formacion-ia#curso", "name": "Formación en IA para empresas y equipos",
            "description": "Formación práctica en inteligencia artificial sobre las tareas reales de cada área de la empresa, con normas de uso y seguimiento.",
            "provider": {"@id": DOM + "/#org"}, "inLanguage": "es", "educationalLevel": "Principiante",
            "teaches": ["Uso práctico de ChatGPT y otras herramientas de IA en el trabajo", "Normas de uso de la IA y protección de datos", "Alfabetización en IA según el AI Act"],
            "hasCourseInstance": [
                {"@type": "CourseInstance", "courseMode": "Online", "instructor": {"@id": JORDAN["@id"]}},
                {"@type": "CourseInstance", "courseMode": "Onsite", "instructor": {"@id": JORDAN["@id"]}}],
            "offers": {"@type": "Offer", "category": "Paid", "url": DOM + "/servicios/formacion-ia", "availability": "https://schema.org/InStock"}}

# ---------- Sesión de IA 1 a 1 ----------
SESION_SLUG = "sesion-de-ia-1-a-1"
SESION_FAQS = [
    ("¿Hace falta que sepa algo de IA?", "No. Si nunca has abierto ChatGPT, se empieza por ahí. Si ya lo usas y quieres sacarle más partido, vamos directos a tus tareas."),
    ("¿La clase de IA 1 a 1 es online o presencial?", "Online por videollamada desde cualquier punto de España, o presencial en Sevilla capital. Mismo precio."),
    ("¿Qué incluye el precio?", "Desde 40 € la hora (sin IVA). En las sesiones presenciales en Sevilla capital el desplazamiento está incluido; si la sesión necesita preparación especial, te lo decimos antes de reservar."),
    ("¿Y si necesito más de una hora?", "Al terminar vemos si te hace falta otra sesión y buscamos hueco. Las siguientes siguen la misma tarifa, desde 40 € la hora."),
    ("¿Y si lo que necesito no aparece en la lista?", "Escríbenos y cuéntanoslo. Si podemos enseñártelo, lo trabajamos; si no, te lo decimos claro y te orientamos."),
]
SESION_TITULO = "Clase de IA 1 a 1 para emprendedores, desde 40 €/hora"
SESION_META = "Aprende a usar la IA en tu negocio en una sesión práctica 1 a 1 de una hora: online en toda España o presencial en Sevilla capital. Desde 40 € la hora, sin IVA."

def sesion_html(migas_html, faq_html, r):
    return """<section class="page-hero"><div class="w">{m}<p class="kicker">Formación en IA · Sesión individual</p><h1>Clase de IA 1 a 1: una hora práctica sobre tu negocio</h1>
<p class="lead">Sin cursos genéricos ni diapositivas. Te sientas delante de tu ordenador, nos cuentas qué haces cada día y aprendes a hacerlo con IA. Desde 40 € la hora (sin IVA), online o presencial en Sevilla capital.</p>
<div class="botones" style="margin-top:24px"><a class="btn btn-p" href="{wa}" target="_blank" rel="noopener">Reservar por WhatsApp</a><a class="btn btn-s" href="../formacion-ia.html">Formación para equipos</a></div></div></section>
<section class="sec"><div class="w"><div class="rejilla">
<div class="tarjeta"><b style="font-size:30px;font-weight:500;color:var(--burdeos)">Desde 40 €</b><p>por hora, sin IVA</p></div>
<div class="tarjeta"><b style="font-size:30px;font-weight:500;color:var(--burdeos)">1 a 1</b><p>sesión individual</p></div>
<div class="tarjeta"><b style="font-size:30px;font-weight:500;color:var(--burdeos)">100 %</b><p>práctica, sobre tus tareas</p></div>
<div class="tarjeta"><b style="font-size:30px;font-weight:500;color:var(--burdeos)">Online</b><p>o presencial en Sevilla capital</p></div>
</div></div></section>
<section class="sec sec-suave"><div class="w"><div class="cab"><p class="kicker">Para quién</p><h2>¿Es para ti?</h2></div><div class="rejilla">
<div class="tarjeta"><h3>Emprendedores y pequeños negocios</h3><p>Sabes que la IA te puede ahorrar horas, pero no sabes por dónde empezar ni tienes tiempo para tutoriales.</p></div>
<div class="tarjeta"><h3>Profesionales independientes</h3><p>Gestores, abogados, agentes inmobiliarios, comerciales… que quieren trabajar más rápido sin perder calidad.</p></div>
<div class="tarjeta"><h3>Ya usas ChatGPT, pero quieres más</h3><p>Intuyes que le puedes sacar mucho más partido y quieres dar el salto a automatizaciones y asistentes propios.</p></div>
</div></div></section>
<section class="sec"><div class="w"><div class="cab"><p class="kicker">Así funciona</p><h2>Tres pasos</h2></div><div class="rejilla">
<div class="tarjeta"><h3>1. Nos escribes</h3><p>Por WhatsApp. Nos cuentas tu negocio y qué te gustaría aprender o resolver con IA.</p></div>
<div class="tarjeta"><h3>2. Fijamos el día</h3><p>Sesiones entre semana por la tarde. Si necesitas otro horario, lo buscamos.</p></div>
<div class="tarjeta"><h3>3. Aprendes haciendo</h3><p>Una hora intensiva sobre tus tareas reales. Te llevas lo que hemos montado funcionando.</p></div>
</div></div></section>
<section class="sec sec-suave"><div class="w"><div class="cab"><p class="kicker">Tú eliges el temario</p><h2>Qué podemos trabajar</h2></div><div class="rejilla">
<div class="tarjeta"><h3>ChatGPT para el día a día</h3><p>Instrucciones que te ahorran horas en correos, documentos, propuestas y análisis.</p></div>
<div class="tarjeta"><h3>Automatizar tareas repetitivas</h3><p>Eso que haces veinte veces al día, lo dejamos automatizado en la propia sesión.</p></div>
<div class="tarjeta"><h3>Un sistema sencillo de clientes</h3><p>Sin programar: seguimientos, recordatorios y contactos ordenados con ayuda de la IA.</p></div>
<div class="tarjeta"><h3>Imágenes y vídeos con IA</h3><p>Contenido para redes, catálogos y anuncios sin depender de un diseñador.</p></div>
<div class="tarjeta"><h3>Tu asistente de IA</h3><p>Un asistente con instrucciones pensadas para tu negocio, listo para usar cada día.</p></div>
<div class="tarjeta"><h3>Lo que necesites</h3><p>¿Algo más concreto? Cuéntanoslo. Si podemos ayudarte, lo hacemos; si no, te lo decimos.</p></div>
</div></div></section>
<section class="sec"><div class="w">{formador}</div></section>
<section class="sec sec-suave"><div class="w"><div class="cab"><h2>Preguntas frecuentes</h2></div>{faq}
<div class="botones" style="margin-top:24px"><a class="btn btn-p" href="{wa}" target="_blank" rel="noopener">Reservar mi sesión por WhatsApp</a></div></div></section>""".format(
        m=migas_html, wa=WA, formador=tarjeta_formador(r), faq=faq_html)

def curso_sesion():
    u = DOM + "/servicios/formacion-ia/" + SESION_SLUG
    return {"@type": "Course", "@id": u + "#curso", "name": "Clase de IA 1 a 1 para emprendedores",
            "description": "Sesión individual y práctica de una hora para aprender a usar la inteligencia artificial en las tareas reales de tu negocio.",
            "provider": {"@id": DOM + "/#org"}, "inLanguage": "es", "educationalLevel": "Principiante",
            "hasCourseInstance": [
                {"@type": "CourseInstance", "courseMode": "Online", "courseWorkload": "PT1H", "instructor": {"@id": JORDAN["@id"]}},
                {"@type": "CourseInstance", "courseMode": "Onsite", "courseWorkload": "PT1H", "instructor": {"@id": JORDAN["@id"]},
                 "location": {"@type": "Place", "name": "Sevilla capital", "address": {"@type": "PostalAddress", "addressLocality": "Sevilla", "addressCountry": "ES"}}}],
            "offers": {"@type": "Offer", "category": "Paid", "price": "40", "priceCurrency": "EUR", "url": u, "availability": "https://schema.org/InStock",
                       "priceSpecification": {"@type": "UnitPriceSpecification", "minPrice": "40", "priceCurrency": "EUR", "unitCode": "HUR", "valueAddedTaxIncluded": False}}}

# ---------- Sobre nosotros: equipo ----------
def equipo_html(r):
    return '<section class="sec sec-suave" id="equipo"><div class="w"><div class="cab"><p class="kicker">Equipo</p><h2>Quién está detrás</h2></div><p class="lead" style="max-width:780px;margin-bottom:22px">Studio Emprende es una marca de INTELIGENCIA SEVILLA SL, con sede en Alcolea del Río (Sevilla), que desarrolla software de gestión, agentes de IA y webs para negocios de toda España. La formación en IA la imparte Jordan García; el equipo técnico implanta y da soporte a cada proyecto.</p>%s</div></section>' % tarjeta_formador(r).replace(
        '<p style="margin:10px 0 0"><a href="%ssobre-nosotros.html#equipo">Conoce al equipo →</a></p>' % r,
        '<p style="margin:10px 0 0"><a href="%sservicios/formacion-ia.html">Ver la formación en IA →</a></p>' % r)

# ---------- Precios: producto de entrada ----------
def banda_precios():
    return ('<section class="sec"><div class="w"><div class="tarjeta" style="display:flex;flex-wrap:wrap;gap:16px;align-items:center;justify-content:space-between">'
            '<div><p class="kicker" style="margin:0 0 4px">¿Todavía no necesitas un pack?</p><h2 style="margin:0 0 6px;font-size:24px">Empieza con una sesión de IA 1 a 1</h2>'
            '<p style="margin:0">Una hora práctica para aprender a usar la IA en tu negocio. Desde 40 € la hora (sin IVA), online o presencial en Sevilla capital.</p></div>'
            '<a class="btn btn-p" href="servicios/formacion-ia/sesion-de-ia-1-a-1.html">Ver la sesión</a></div></div></section>')
