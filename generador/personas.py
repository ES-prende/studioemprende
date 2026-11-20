# Bloques «primero la persona» para páginas internas (plan del 15/11/2026).
# Se insertan entre la cabecera y el contenido que ya existía. No cambian URL, título, H1 ni metadescripción.

def _t(h, p):
    return '<div class="tarjeta"><h3>%s</h3><p>%s</p></div>' % (h, p)

def _d(h, p, c=""):
    return '<div class="tarjeta dolor%s"><h3>%s</h3><p>%s</p></div>' % (c, h, p)

# slug del hub -> html (rutas relativas a /servicios/)
HUB_ANTES = {
"autonomos": """<section class="sec sec-suave"><div class="w">
<div class="cab"><p class="kicker">¿En qué punto estás?</p><h2>Tanto si solo tienes la idea como si ya eres autónomo</h2><p class="lead" style="margin-top:8px">No es lo mismo estar pensando en empezar que llevar meses trabajando. Por eso lo primero es saber dónde estás.</p></div>
<div class="rejilla">
<div class="tarjeta" style="border-top:4px solid var(--burdeos)"><h3>Tengo una idea, pero todavía no me he dado de alta</h3><p>Te ayudamos a darle forma, a decidir qué necesitas de verdad para empezar y a preparar tu presencia profesional para el día que arranques. Sin gastar de más antes de tiempo.</p><a class="mas" href="../guias/como-emprender-un-negocio.html">Guía: cómo emprender un negocio →</a></div>
<div class="tarjeta" style="border-top:4px solid var(--ocre)"><h3>Ya soy autónomo y quiero avanzar</h3><p>Te ayudamos a que te encuentren, a ordenar clientes, presupuestos y facturas, y a quitarte de encima las tareas que repites cada semana.</p><a class="mas" href="autonomos/automatizacion-del-dia-a-dia.html">Automatización del día a día →</a></div>
</div></div></section>
<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Lo que más preocupa al empezar</p><h2>Si te suena alguna de estas dudas, es normal</h2></div>
<div class="rejilla">"""
+ _d("«No sé por dónde empezar»", "Hay mil herramientas y consejos. Ordenamos contigo los primeros pasos y dejamos para más adelante lo que todavía no hace falta.")
+ _d("«Me da miedo invertir de más»", "Empiezas por lo imprescindible y con el precio por escrito antes de arrancar. Lo demás se añade cuando tenga sentido.", " d2")
+ _d("«Nadie me encuentra»", "Sin web ni ficha de Google es difícil que confíen en ti. Te dejamos una presencia profesional desde el primer día.", " d3")
+ """</div></div></section>
<section class="sec sec-suave"><div class="w">
<div class="cab"><p class="kicker">Así te ayudamos</p><h2>Cuatro apoyos para emprender con buen pie</h2></div>
<div class="rejilla">"""
+ _t("Presencia profesional", 'Identidad, <a href="webs.html">web</a> y <a href="presencia-digital.html">ficha de Google Business</a> para que te encuentren y te tomen en serio.')
+ _t("Organización inicial", 'Clientes, presupuestos y facturas en un <a href="software-de-gestion.html">programa de gestión</a> sencillo, en lugar de repartidos entre el móvil y el Excel.')
+ _t("Formación", 'Te enseñamos a usar lo que montamos y, si quieres, a aprovechar la IA en tu trabajo con <a href="formacion-ia.html">formación práctica</a>.')
+ _t("Acompañamiento", "Hablas siempre con la misma persona, que conoce tu proyecto y te orienta en cada paso.")
+ """</div>
<p class="mut" style="margin-top:22px;font-size:15px;max-width:820px">Importante: no somos gestoría ni asesoría. El alta de autónomo, la constitución de una sociedad y los trámites fiscales los lleva tu gestor. Nosotros nos ocupamos de la parte digital y de organización del negocio, y si lo necesitas te ayudamos a encontrar a ese profesional.</p>
<div class="botones" style="margin-top:22px"><a class="btn btn-p" href="../contacto.html?servicio=autonomos#diagnostico">Quiero saber por dónde empezar</a></div>
</div></section>""",
}

# Selector de /servicios/ (rutas relativas a /servicios/)
SELECTOR = """<section class="sec sec-suave" style="padding:56px 0"><div class="w">
<div class="cab" style="margin-bottom:26px"><p class="kicker">Empieza por tu necesidad</p><h2>¿Qué quieres resolver?</h2><p class="lead" style="margin-top:8px">No hace falta que sepas qué herramienta necesitas. Elige lo que más se parece a tu situación.</p></div>
<div class="rejilla">
<a class="tarjeta" href="autonomos.html"><h3>Empezar un negocio</h3><p>Tienes una idea o acabas de arrancar y quieres hacerlo con buen pie.</p><span class="mas">Emprendedores y autónomos →</span></a>
<a class="tarjeta" href="presencia-digital.html"><h3>Conseguir clientes</h3><p>Tu trabajo es bueno, pero te encuentran poco en Google y en redes.</p><span class="mas">Presencia digital →</span></a>
<a class="tarjeta" href="automatizacion-y-datos.html"><h3>Ahorrar tiempo</h3><p>Repites las mismas tareas cada semana y no te queda tiempo para lo importante.</p><span class="mas">Automatización →</span></a>
<a class="tarjeta" href="software-de-gestion.html"><h3>Organizar el negocio</h3><p>Clientes, presupuestos y facturas repartidos entre Excel, correo y WhatsApp.</p><span class="mas">Programa de gestión →</span></a>
<a class="tarjeta" href="../normativas.html"><h3>Cumplir requisitos</h3><p>Verifactu, registro de jornada o formación en IA: qué te afecta y desde cuándo.</p><span class="mas">Normativas →</span></a>
<a class="tarjeta" href="pequenas-empresas.html"><h3>Crecer</h3><p>El negocio funciona y quieres dar el siguiente paso sin perder el control.</p><span class="mas">Pequeñas empresas →</span></a>
</div>
<p style="margin-top:22px">¿No encaja ninguna? <a href="../contacto.html#diagnostico">Cuéntanos tu caso</a> y te orientamos. Debajo tienes el catálogo completo.</p>
</div></section>"""


# =====================================================================
# Lotes 2 y 3: resto de páginas de servicio. Cada página tiene su propia estructura.
# =====================================================================
import re as _re, unicodedata as _u

def _s(t):
    t = _u.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    return _re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:70]

def _a(hub, item, txt=None):
    return '<a href="%s/%s.html">%s</a>' % (hub, _s(item), txt or item)

def _sec(k, h2, inner, suave=False, lead=""):
    return '<section class="sec%s"><div class="w"><div class="cab"><p class="kicker">%s</p><h2>%s</h2>%s</div>%s</div></section>' % (
        " sec-suave" if suave else "", k, h2, ('<p class="lead" style="margin-top:8px">%s</p>' % lead) if lead else "", inner)

def _resp(k, t):
    return '<div class="respuesta"><p class="kicker" style="margin:0 0 6px">%s</p><p style="margin:0">%s</p></div>' % (k, t)

def _preg(*qs):
    return '<ul class="lista" style="font-size:18px;max-width:760px">%s</ul>' % "".join("<li>%s</li>" % q for q in qs)

def _tabla(cab, filas):
    return '<div class="tabla-wrap"><table class="tabla-norm"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (
        "".join("<th>%s</th>" % c for c in cab), "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in f) for f in filas))

def _pasos(*ps):
    return '<ol class="rejilla" style="list-style:none;margin:0;padding:0">%s</ol>' % "".join(
        '<li class="tarjeta"><span class="num">%02d</span><h3>%s</h3><p>%s</p></li>' % (i + 1, h, p) for i, (h, p) in enumerate(ps))

def _rej(*ts):
    return '<div class="rejilla">%s</div>' % "".join(ts)

def _ej(t):
    return '<div class="tarjeta" style="background:var(--suave);max-width:860px;margin-top:22px"><p class="kicker" style="margin:0">Ejemplo hipotético</p><p style="font-size:16px">%s</p></div>' % t

def _cta(slug, txt):
    return '<div class="botones" style="margin-top:24px"><a class="btn btn-p" href="../contacto.html?servicio=%s#diagnostico">%s</a></div>' % (slug, txt)

H = HUB_ANTES
F = {}  # preguntas frecuentes por página (se muestran y se marcan como FAQPage)

# ---------- WEBS: tres situaciones + respuesta directa ----------
H["webs"] = _sec("Tu web hoy", "No te encuentran, no confían o no te contactan", _rej(
    _d("Aún no tienes web", 'Empiezas de cero y quieres algo profesional sin complicarte. Lo habitual es una %s o una página única para arrancar.' % _a("webs", "Web corporativa con SEO", "web corporativa con SEO")),
    _d("Tu web se ha quedado vieja", 'Carga lenta, no se ve bien en el móvil o nadie la actualiza. Se puede %s o rehacerla conservando lo que ya posiciona.' % _a("webs", "Rescate de webs antiguas o hackeadas", "rescatar"), " d2"),
    _d("Quieres vender por internet", 'Necesitas una %s enlazada con tu stock y tu facturación, para no llevar dos sistemas.' % _a("webs", "Tienda online", "tienda online"), " d3"))
    + _resp("En pocas palabras", "Una web profesional sirve para tres cosas: que aparezcas cuando te buscan, que quien llega se fíe de ti y que le resulte fácil escribirte. Diseñamos webs rápidas y accesibles, preparadas para buscadores, en las que cada formulario entra directo en tu CRM.").replace('class="respuesta"', 'class="respuesta" style="margin-top:26px"')
    + _cta("webs", "Cuéntanos qué web necesitas"), True)
F["webs"] = [("¿Cuánto se tarda en tener una web lista?", "Depende del tipo. Como referencia, el pack Impulso Inicial, con web de una página, se entrega en 2 o 3 semanas, y una web completa con blog en 3 o 4, contando desde que nos pasas la información."),
             ("¿Puedo cambiar yo los textos y las fotos después?", "Sí. Te enseñamos a hacerlo y, si prefieres despreocuparte, existe un mantenimiento mensual que se ocupa de los cambios, las copias y la seguridad."),
             ("¿La web queda a mi nombre?", "Sí. El dominio y el contenido son tuyos. Lo dejamos por escrito para que puedas llevártelos si algún día cambias de proveedor.")]

# ---------- PRESENCIA DIGITAL: plan por fases ----------
H["presencia-digital"] = _sec("Visibilidad", "Tu negocio es bueno, pero casi nadie lo ve en Google", _preg(
    "¿Buscas tu actividad y tu ciudad y salen todos menos tú?", "¿Tu ficha de Google tiene el horario equivocado o apenas reseñas?", "¿Publicas en redes cuando te acuerdas y sin un orden?")
    + '<p style="margin:22px 0 26px;max-width:760px">Aparecer no depende de un truco. Es un trabajo por etapas, y conviene hacerlas en este orden:</p>'
    + _pasos(("Ficha de Google al día", '%s completo: categorías, horarios, fotos y respuesta a reseñas.' % _a("presencia-digital", "Google Business Profile")),
             ("Buscadores de tu zona", '%s para que te encuentren quienes buscan cerca de ti.' % _a("presencia-digital", "SEO local y por sectores")),
             ("Contenido constante", '%s, para publicar con regularidad sin dedicarle tus tardes.' % _a("presencia-digital", "Automatización de redes sociales")),
             ("Asistentes de IA", '%s: que ChatGPT o Gemini te mencionen cuando alguien pregunta.' % _a("presencia-digital", "Aparecer en ChatGPT y Gemini (GEO)", "Aparecer en ChatGPT y Gemini")))
    + '<p class="mut" style="margin-top:20px;font-size:15px">Nadie puede garantizar el primer puesto en Google. Lo que sí se puede es medir cada mes qué mejora y qué no.</p>', True)
F["presencia-digital"] = [("¿Cuánto tarda en notarse el SEO local?", "Las mejoras en la ficha de Google suelen verse en pocas semanas. El posicionamiento de la web en buscadores es más lento y lo habitual es valorarlo a partir de los tres meses."),
                          ("¿Qué es el GEO?", "Es preparar tu información para que los asistentes de inteligencia artificial, como ChatGPT o Gemini, puedan entender tu negocio y citarlo cuando alguien les pregunta por un servicio como el tuyo."),
                          ("¿Tengo que estar en todas las redes sociales?", "No. Es preferible atender bien una o dos, las que usan tus clientes, que abrir perfiles en todas y dejarlos abandonados.")]

# ---------- SOFTWARE DE GESTIÓN: antes / después ----------
H["software-de-gestion"] = _sec("Orden", "La información de tu negocio está repartida por todas partes", _tabla(
    ["Lo que pasa hoy", "Con un programa de gestión"],
    [["Los datos de cada cliente están entre el móvil, el correo y una hoja de cálculo", 'Una sola %s con su historial completo' % _a("software-de-gestion", "Ficha de cliente 360°", "ficha de cliente")],
     ["El presupuesto se hace en Word y luego se vuelve a teclear para facturar", _a("software-de-gestion", "Presupuestos que pasan a pedido y factura")],
     ["No sabes quién te debe dinero hasta que revisas el banco", _a("software-de-gestion", "Cobros, impagos y semáforo de clientes")],
     ["Las cifras del mes llegan tarde y a mano", _a("software-de-gestion", "Cuadro de mando en tiempo real")]])
    + '<p style="margin-top:22px;max-width:820px">Es un programa modular: se activan solo las partes que usas (CRM, facturación, agenda, almacén, equipo) y se añaden otras más adelante. Si necesitas unir además compras, producción y contabilidad, mira el <a href="erp-para-pymes.html">ERP para pymes</a>.</p>'
    + _cta("software-de-gestion", "Analizamos tu situación"), True)
F["software-de-gestion"] = [("¿Qué diferencia hay entre un CRM y un programa de gestión?", "El CRM se ocupa de clientes y ventas. El programa de gestión incluye el CRM y suma facturación, agenda, almacén o equipo, según los módulos que actives."),
                            ("¿Puedo empezar con un par de módulos y ampliar después?", "Sí. Está pensado así: comienzas por lo que más te urge y añades módulos cuando los necesitas, sin cambiar de programa."),
                            ("¿Qué pasa con los datos que tengo en Excel?", "Se importan. La migración desde Excel u otro programa está incluida al implantar el programa de gestión.")]

# ---------- ERP: definición + ERP frente a CRM + sectores ----------
H["erp-para-pymes"] = _sec("ERP para pymes", "Ventas, almacén, cobros y facturas en programas que no se hablan",
    _resp("Qué es un ERP", "Un ERP es un único programa que reúne ventas, compras, almacén, facturación, equipo y contabilidad, de modo que un dato se introduce una vez y lo ven todas las áreas. En una pyme evita teclear lo mismo en varias herramientas y cuadrar cifras a mano.")
    + '<div class="rejilla" style="margin-top:26px">'
    + _t("¿ERP o CRM?", 'El CRM gestiona la relación comercial. El ERP abarca toda la empresa e incluye ese CRM. Lo explicamos en la guía <a href="../guias/erp-vs-crm.html">ERP frente a CRM</a>.')
    + _t("Comercio y distribución", 'El stock real conectado con las ventas: %s.' % _a("erp-para-pymes", "Compras, proveedores y almacén", "compras, proveedores y almacén"))
    + _t("Obras, talleres y servicios", _a("erp-para-pymes", "Producción, obras o servicios según tu sector") + ", con el coste previsto frente al real.")
    + '</div><p style="margin-top:22px;max-width:820px">La implantación se hace por fases para no parar el negocio, empezando por el %s.</p>' % _a("erp-para-pymes", "Análisis de tus procesos y elección de módulos", "análisis de tus procesos")
    + _cta("erp-para-pymes", "Quiero saber si necesito un ERP"), True)
F["erp-para-pymes"] = [("¿Cuándo necesita una pyme un ERP?", "Cuando la misma información se introduce en varios programas, el stock no coincide con las ventas o cerrar el mes exige cruzar hojas de cálculo. Si solo necesitas ordenar clientes y facturas, suele bastar un programa de gestión más sencillo."),
                       ("¿Cuánto dura la implantación de un ERP?", "Depende de los módulos y de la calidad de los datos de partida. Se hace por fases, y tras el análisis inicial se entrega un calendario con fechas."),
                       ("¿Hay que parar la empresa para cambiar de programa?", "No. Los módulos entran en uso de forma escalonada y el equipo recibe formación con casos reales antes de cada cambio.")]

# ---------- APPS: clientes frente a equipo ----------
H["apps-moviles"] = _sec("Apps a medida", "Reservas, pedidos o partes de trabajo que no funcionan bien en el móvil", '<div class="rejilla">'
    + '<div class="tarjeta" style="border-top:4px solid var(--burdeos)"><h3>App para tus clientes</h3><p>Para que reserven, pidan, acumulen puntos o reciban avisos sin llamarte.</p><ul class="lista"><li>%s</li><li>%s</li></ul></div>' % (
        _a("apps-moviles", "App para clientes: reservas, pedidos, fidelización y avisos", "Reservas, pedidos y fidelización"), _a("apps-moviles", "App para socios, alumnos o pacientes"))
    + '<div class="tarjeta" style="border-top:4px solid var(--ocre)"><h3>App para tu equipo</h3><p>Para quien trabaja fuera de la oficina y hoy apunta en papel o manda fotos por WhatsApp.</p><ul class="lista"><li>%s</li><li>%s</li></ul></div>' % (
        _a("apps-moviles", "App interna para empleados y técnicos"), _a("apps-moviles", "App de catálogo y pedidos para distribuidores"))
    + '</div><p style="margin:26px 0 14px"><b>Del boceto a las tiendas, en tres etapas:</b> diseño de pantallas contigo, desarrollo conectado a tu programa de gestión y %s.</p>' % _a("apps-moviles", "Publicación en Google Play y App Store", "publicación en Google Play y App Store")
    + _cta("apps-moviles", "Cuéntanos qué app tienes en mente"), True)
F["apps-moviles"] = [("¿Necesito una app o me basta una web?", "Si tus clientes entran de vez en cuando, una web adaptada al móvil suele ser suficiente. La app compensa cuando hay uso frecuente, avisos al teléfono o trabajo sin cobertura."),
                     ("¿La app funciona en iPhone y en Android?", "Sí. Se publica en App Store y en Google Play."),
                     ("¿Quién actualiza la app cuando cambian los sistemas?", "Hay un servicio de mantenimiento y actualizaciones que la mantiene compatible con las nuevas versiones de iOS y Android.")]

# ---------- SOFTWARE ESPECIALIZADO: pregunta + casos concretos ----------
H["software-especializado"] = _sec("A medida", "¿Tu empresa trabaja de una forma que ningún programa resuelve bien?",
    '<p style="max-width:820px;margin-bottom:22px">A veces el programa estándar obliga a cambiar tu manera de trabajar o deja fuera justo lo que te diferencia. Estos son casos concretos que ya tenemos resueltos:</p>'
    + _tabla(["Necesidad", "Solución"],
             [["Registros sanitarios de cocina en papel", _a("software-especializado", "APPCC digital para hostelería y alimentación")],
              ["Documentación de contratas antes de entrar a una obra", _a("software-especializado", "Coordinación de actividades empresariales (CAE)")],
              ["Presupuestos que dependen de muchas opciones", _a("software-especializado", "Presupuestador y configurador online")],
              ["Clientes profesionales que piden por teléfono", _a("software-especializado", "Portal de pedidos B2B")],
              ["Paradas imprevistas de maquinaria", _a("software-especializado", "Mantenimiento predictivo con sensores")]])
    + '<p class="mut" style="margin-top:18px;font-size:15px">No todo merece un desarrollo propio. Si existe una herramienta que ya lo hace bien, te lo decimos.</p>'
    + _cta("software-especializado", "Cuéntanos cómo trabajas"), True)
F["software-especializado"] = [("¿Cuándo compensa un software a medida?", "Cuando el proceso es propio de tu empresa, se repite mucho y los programas estándar obligan a hacer rodeos. Para tareas comunes suele ser más sensato un programa ya existente."),
                               ("¿De quién es el código?", "Las condiciones de propiedad y de uso se fijan por escrito en la propuesta, antes de empezar el desarrollo."),
                               ("¿Se conecta con lo que ya uso?", "Sí, siempre que la otra herramienta permita intercambiar datos. Se revisa en el análisis previo.")]

# ---------- MIGRACIONES: proceso de cinco pasos ----------
H["migraciones-e-integraciones"] = _sec("Sin perder datos", "Copiar lo mismo de Excel al CRM y del CRM a la facturación",
    '<p style="max-width:820px;margin-bottom:26px">Cada vez que un dato se vuelve a teclear puede cambiar un número o quedarse un cliente por el camino. Una migración bien hecha sigue siempre el mismo recorrido:</p>'
    + _pasos(("Auditoría", "Vemos qué datos hay, dónde están y en qué estado."),
             ("Copia de seguridad", "Antes de tocar nada se guarda una copia completa."),
             ("Migración controlada", 'Se trasladan por bloques, como en la %s.' % _a("migraciones-e-integraciones", "Migración de Excel a programa de gestión", "migración de Excel a programa de gestión")),
             ("Pruebas", "Comprobamos contigo que los totales y los registros coinciden."),
             ("Continuidad", "El sistema anterior sigue disponible hasta que confirmas que todo está bien."))
    + '<p class="mut" style="margin-top:20px;font-size:15px">Ninguna migración tiene riesgo cero. Por eso se hace con copia previa y con pruebas antes de dar el cambio por bueno.</p>'
    + '<p style="margin-top:14px">Si lo que quieres es que tus programas se entiendan entre sí, mira %s.</p>' % _a("migraciones-e-integraciones", "Conectar ERP, tienda, CRM y contabilidad", "cómo conectar ERP, tienda, CRM y contabilidad"), True)
F["migraciones-e-integraciones"] = [("¿Se pueden pasar los datos de Holded, Clientify o HubSpot?", "Sí. Se exportan desde el programa de origen, se revisan y se cargan en el nuevo. Hay una página específica sobre esas migraciones."),
                                    ("¿Qué ocurre si un dato no cuadra tras la migración?", "Se detecta en la fase de pruebas, cuando todavía funciona el sistema anterior, y se corrige antes de hacer el cambio definitivo."),
                                    ("¿Es mejor migrar o integrar?", "Migrar significa dejar un programa y pasar a otro. Integrar significa conservar ambos y hacer que compartan datos. Depende de si el programa actual te sigue sirviendo.")]

# ---------- AGENTES DE IA: qué hace el agente y qué decide una persona ----------
H["agentes-de-ia"] = _sec("Atención y tareas", "Las mismas preguntas todos los días y mensajes que llegan cuando ya has cerrado",
    _resp("Qué es un agente de IA", "Un agente de IA es un asistente que entiende lo que le escriben o le dicen, consulta la información de tu negocio y lleva a cabo una tarea: responder, dar cita, preparar un presupuesto o reclamar un cobro. Lo entrenamos con tus datos y siempre queda definido qué puede hacer solo y qué necesita tu visto bueno.")
    + '<div style="margin-top:26px">' + _tabla(["Lo hace el agente", "Lo decide una persona"],
        [["Contestar dudas frecuentes a cualquier hora", "Las respuestas que comprometen precio o plazo no previstos"],
         ["Recoger los datos de un cliente nuevo", "Aceptar o rechazar un encargo"],
         ["Preparar el borrador de un presupuesto", "Aprobarlo antes de enviarlo"],
         ["Recordar una factura pendiente", "Negociar un aplazamiento"]]) + '</div>'
    + '<p style="margin-top:22px">Para empezar por lo más habitual: %s o %s.</p>' % (_a("agentes-de-ia", "Chatbot para tu web con la IA empresarial", "chatbot para tu web"), _a("agentes-de-ia", "Recepcionista de voz y atención fuera de horario", "recepcionista de voz fuera de horario"))
    + _cta("agentes-de-ia", "Cuéntanos qué tarea te quita más tiempo"), True)
F["agentes-de-ia"] = [("¿Un agente de IA puede equivocarse?", "Sí, como cualquier herramienta. Por eso se prueba unas semanas con revisión humana y las acciones importantes requieren aprobación."),
                      ("¿Dónde quedan los datos de mi empresa?", "Hay opciones para que la información no salga de tu entorno, incluida la IA en servidor propio. Se decide según lo sensibles que sean los datos."),
                      ("¿En qué se diferencia de un chatbot de botones?", "El chatbot clásico sigue un guion fijo. El agente comprende frases normales y además puede ejecutar acciones en tus programas.")]

# ---------- WHATSAPP IA: escena + cuándo pasa a una persona ----------
H["whatsapp-ia"] = _sec("WhatsApp", "Te escriben justo cuando estás atendiendo a otro cliente",
    '<p class="lead" style="max-width:820px">Estás con las manos ocupadas, el móvil vibra y, cuando por fin contestas, esa persona ya ha preguntado en otro sitio.</p>'
    + '<div class="rejilla" style="margin-top:26px">'
    + _t("Citas", 'El asistente propone huecos, confirma y avisa el día antes: %s.' % _a("whatsapp-ia", "Citas y recordatorios automáticos", "citas y recordatorios"))
    + _t("Seguimiento", 'Vuelve a escribir a quien pidió presupuesto o lleva tiempo sin venir: %s.' % _a("whatsapp-ia", "Reactivación de clientes y pacientes inactivos", "reactivación de inactivos"))
    + _t("Cuándo interviene una persona", "Si el cliente lo pide, si la consulta se sale de lo previsto o si hay una queja, la conversación pasa a ti con todo el historial.")
    + _t("Privacidad", "Funciona sobre WhatsApp Business. El asistente solo usa la información que tú le das y no pide datos sensibles.")
    + '</div>' + _cta("whatsapp-ia", "Quiero dejar de perder mensajes"), True)

# ---------- AUTOMATIZACIÓN: lista de comprobación ----------
H["automatizacion-y-datos"] = _sec("Tiempo", "¿Cuántas veces copias la misma información a lo largo de la semana?",
    '<p style="max-width:820px;margin-bottom:16px">Si marcas dos o más, hay horas que se pueden recuperar:</p>'
    + _preg("Pasas facturas de proveedores a mano. → %s" % _a("automatizacion-y-datos", "Lectura automática de documentos hacia tu programa", "Lectura automática de documentos"),
            "Persigues cobros uno a uno. → %s" % _a("automatizacion-y-datos", "Automatización de administración, facturas y cobros"),
            "Preparas el informe del lunes copiando cifras. → %s" % _a("automatizacion-y-datos", "Informe semanal por WhatsApp o voz"),
            "Compras según intuición y sobra o falta género. → %s" % _a("automatizacion-y-datos", "Previsión de ventas y stock"),
            "Organizas las visitas del día sobre un mapa. → %s" % _a("automatizacion-y-datos", "Optimización de rutas"))
    + '<p class="mut" style="margin-top:20px;font-size:15px;max-width:820px">El ahorro depende de cada negocio. Antes de automatizar medimos cuánto tiempo se lleva hoy cada tarea, y así sabes si compensa.</p>'
    + _cta("automatizacion-y-datos", "Analizamos qué puedes automatizar"), True)
F["automatizacion-y-datos"] = [("¿Qué tareas conviene automatizar primero?", "Las que se repiten cada semana, siguen siempre los mismos pasos y no requieren criterio: pasar datos, enviar recordatorios o montar informes."),
                               ("¿Hace falta cambiar de programa para automatizar?", "No siempre. Muchas automatizaciones se apoyan en las herramientas que ya usas, siempre que permitan conectarse."),
                               ("¿Qué pasa si una automatización falla?", "Cada proceso deja registro y avisa cuando algo no sale como se espera, para que una persona lo revise.")]

# ---------- PEQUEÑAS EMPRESAS: tabla problema-solución arriba + proceso gradual ----------
H["pequenas-empresas"] = _sec("Por problema", "Clientes que se pierden, cobros que tardan y demasiadas horas de oficina", _tabla(
    ["Lo que te ocurre", "Por dónde se empieza"],
    [["Llamadas y mensajes sin contestar", _a("pequenas-empresas", "No pierdas clientes: WhatsApp IA y recepcionista de voz", "WhatsApp con IA y recepcionista de voz")],
     ["Facturas que se cobran tarde", _a("pequenas-empresas", "Cobra antes: cobros y tesorería", "Cobros y tesorería")],
     ["Tardes enteras con papeles", _a("pequenas-empresas", "Ahorra horas: programa de gestión y facturas automáticas", "Programa de gestión y facturas automáticas")],
     ["Dudas con Verifactu o el registro horario", _a("pequenas-empresas", "Cumple la ley: Verifactu y registro de jornada", "Verifactu y registro de jornada")]])
    + '<p style="margin-top:24px;max-width:820px"><b>Poco a poco.</b> No hay que cambiarlo todo a la vez. Se resuelve primero lo que más duele, se comprueba que funciona y solo entonces se pasa a lo siguiente. Si prefieres un importe fijo, existe la opción de %s.</p>' % _a("pequenas-empresas", "Todo incluido por cuota mensual", "todo incluido por cuota mensual")
    + _cta("pequenas-empresas", "Cuéntanos qué te quita el sueño"), True)
F["pequenas-empresas"] = [("¿Por dónde empieza a digitalizarse una pequeña empresa?", "Por el problema que más dinero o tiempo cuesta hoy. En el diagnóstico gratuito se ordenan las prioridades y se deja para después lo que puede esperar."),
                          ("¿Tengo que formar a mi equipo?", "Sí, y lo hacemos nosotros. Cada herramienta se entrega con una explicación práctica para las personas que la van a usar."),
                          ("¿Trabajáis con negocios de pueblo o de zonas rurales?", "Sí. Trabajamos 100 % online con toda España y hay un servicio específico de digitalización de negocios rurales.")]

# ---------- GRANDES EMPRESAS: cuatro frenos + piloto ----------
H["grandes-empresas"] = _sec("Adopción de IA", "Silos, aprobaciones lentas y una IA que no pasa de la prueba", _rej(
    _t("Departamentos aislados", 'Cada área tiene sus datos y sus herramientas. %s.' % _a("grandes-empresas", "IA conectada a ERP y sistemas antiguos")),
    _t("Decisiones que se eternizan", 'Un piloto acotado permite decidir con resultados: %s.' % _a("grandes-empresas", "Piloto de agente IA en 30-60 días")),
    _t("Uso sin normas", 'Empleados que ya usan IA por su cuenta. %s fija qué se puede hacer y con qué datos.' % _a("grandes-empresas", "Gobernanza de IA", "La gobernanza de IA")),
    _t("Seguridad y calidad", '%s antes de ponerlos delante de un cliente.' % _a("grandes-empresas", "Pruebas de agentes IA")))
    + _resp("Cómo se plantea un piloto", "Se elige un único proceso, se acuerda de antemano el indicador con el que se va a medir y se trabaja con un alcance y un importe cerrados. Al terminar, la dirección decide con datos si se amplía, se corrige o se detiene.").replace('class="respuesta"', 'class="respuesta" style="margin-top:26px"'), True)
F["grandes-empresas"] = [("¿Cuánto dura un piloto de IA?", "Entre 30 y 60 días, según el proceso elegido y la disponibilidad de los datos."),
                         ("¿Cómo se mide si el piloto ha funcionado?", "Con el indicador pactado al inicio, por ejemplo tiempo de respuesta, consultas resueltas sin intervención o errores evitados."),
                         ("¿Podéis trabajar junto a nuestro departamento de sistemas?", "Sí. El piloto se coordina con vuestro equipo técnico y respeta sus políticas de acceso y seguridad.")]

# ---------- STARTUPS: preguntas del fundador ----------
H["startups-e-inversores"] = _sec("Del prototipo a la ronda", "Validar la idea sin quemar el presupuesto ni hipotecar el producto",
    '<div class="rejilla">'
    + _d("¿Qué construyo primero?", 'Solo lo necesario para comprobar si alguien lo quiere: %s.' % _a("startups-e-inversores", "MVP en 6-12 semanas", "un MVP en 6-12 semanas"))
    + _d("¿Quién toma las decisiones técnicas?", 'Si no hay perfil técnico entre los socios, un %s evita elecciones difíciles de deshacer.' % _a("startups-e-inversores", "CTO externalizado", "CTO externalizado"), " d2")
    + _d("¿Qué me van a pedir los inversores?", '%s y una %s.' % (_a("startups-e-inversores", "Métricas para inversores"), _a("startups-e-inversores", "Preparación de due diligence", "due diligence preparada")), " d3")
    + '</div><p style="margin-top:22px;max-width:820px"><b>Deuda técnica:</b> lanzar rápido tiene un coste que conviene conocer. En cada entrega te explicamos qué se ha simplificado y qué habría que rehacer para escalar.</p>'
    + '<p style="margin-top:10px">¿Inviertes en proyectos? Mira la %s.</p>' % _a("startups-e-inversores", "Due diligence técnica", "due diligence técnica"), True)
F["startups-e-inversores"] = [("¿Qué debe incluir un MVP?", "La función mínima que permite comprobar si los usuarios pagan o repiten. Todo lo demás se pospone hasta tener esa respuesta."),
                              ("¿Qué hace un CTO externo?", "Decide la tecnología, coordina el desarrollo y representa la parte técnica ante socios e inversores, sin incorporar a alguien a jornada completa."),
                              ("¿Preparáis la memoria técnica para ENISA o CDTI?", "Sí, redactamos la parte técnica de la solicitud. La concesión depende siempre del organismo.")]

# ---------- DELUXE: breve, tono propio ----------
H["deluxe"] = _sec("Servicio privado", "Tecnología que funciona sin que tengas que pensar en ella",
    '<p class="lead" style="max-width:820px">Para viviendas, fincas y familias que quieren comodidad y discreción: una sola persona de contacto, confidencialidad firmada y atención cuando se necesita.</p>'
    + '<ul class="lista" style="margin-top:22px;max-width:760px"><li>%s, con clima, luz y accesos coordinados.</li><li>%s para resolver cualquier incidencia.</li><li>%s cuando hay más de una residencia.</li><li>%s.</li></ul>' % (
        _a("deluxe", "Villa o casa inteligente de lujo"), _a("deluxe", "Técnico personal 24/7"), _a("deluxe", "Gestión de varias propiedades"), _a("deluxe", "Protección frente a suplantación y deepfakes")), True)
F["deluxe"] = [("¿Cómo se protege la confidencialidad?", "Con un acuerdo de confidencialidad firmado antes de empezar y un único interlocutor que conoce el encargo."),
               ("¿Atendéis fuera de Sevilla?", "Sí. La parte remota se presta en toda España, y los trabajos presenciales se planifican según la ubicación.")]

# ---------- CIBERSEGURIDAD: tres escenarios ----------
H["ciberseguridad-y-sistemas"] = _sec("Si mañana ocurriera", "Tres situaciones que paran una empresa", _rej(
    _d("Se pierde la información", 'Un disco estropeado o un borrado accidental. La respuesta está en las %s, probadas de verdad.' % _a("ciberseguridad-y-sistemas", "Copias de seguridad y plan de continuidad", "copias de seguridad y el plan de continuidad")),
    _d("Alguien entra donde no debe", 'Contraseñas compartidas o antiguos empleados con acceso. Un %s lo revisa.' % _a("ciberseguridad-y-sistemas", "Responsable de ciberseguridad externalizado", "responsable de ciberseguridad externo"), " d2"),
    _d("Los equipos dejan de tener soporte", 'Ordenadores sin actualizaciones: %s.' % _a("ciberseguridad-y-sistemas", "Renovación de equipos y fin de Windows 10", "renovación de equipos y fin de Windows 10"), " d3"))
    + '<p style="margin-top:22px;max-width:820px">Empezamos por una revisión y proponemos medidas proporcionadas al tamaño de tu empresa. La seguridad total no existe; se trata de reducir la probabilidad y de poder recuperarse pronto.</p>'
    + '<p class="mut" style="margin-top:10px;font-size:15px;max-width:820px">En AI Act, NIS2 o Ciberresiliencia nos ocupamos de la adaptación técnica. La interpretación jurídica corresponde a tu asesor legal.</p>', True)
F["ciberseguridad-y-sistemas"] = [("¿Cada cuánto hay que probar las copias de seguridad?", "Lo recomendable es hacer una restauración de prueba de forma periódica. Una copia que nunca se ha restaurado no ofrece garantías."),
                                  ("¿Mi empresa está obligada por NIS2?", "Depende del sector y del tamaño, y también puede afectarte como proveedor de una empresa obligada. Conviene confirmarlo con tu asesor legal."),
                                  ("¿Qué hago si sigo con Windows 10?", "Al terminar el soporte dejan de llegar parches de seguridad. Lo sensato es planificar la actualización o la sustitución de esos equipos.")]

# ---------- DEPARTAMENTO TECNOLÓGICO: qué cubre ----------
H["departamento-tecnologico"] = _sec("Un solo teléfono", "Muchas herramientas, varios proveedores y nadie que responda",
    '<p class="lead" style="max-width:820px">El de la web dice que es cosa del correo, el del correo culpa al dominio y tú sigues sin poder trabajar.</p>'
    + '<div class="rejilla" style="margin-top:26px">'
    + _t("Con quién hablas", '%s: una persona que conoce tus sistemas y coordina al resto.' % _a("departamento-tecnologico", "Soporte con un único interlocutor"))
    + _t("Qué se vigila", '%s, %s y %s.' % (_a("departamento-tecnologico", "Dominios y renovaciones"), _a("departamento-tecnologico", "Prueba mensual de copias de seguridad", "copias de seguridad"), _a("departamento-tecnologico", "Monitorización de la web 24/7", "estado de la web")))
    + _t("Qué recibes", _a("departamento-tecnologico", "Informe mensual en lenguaje claro") + ", sin tecnicismos.")
    + '</div><p class="mut" style="margin-top:20px;font-size:15px;max-width:820px">El alcance y los tiempos de respuesta se acuerdan por escrito en cada contrato, según lo que necesite tu empresa.</p>'
    + _cta("departamento-tecnologico", "Cuéntanos qué herramientas usas"), True)
F["departamento-tecnologico"] = [("¿Qué es un departamento tecnológico externo?", "Es un equipo ajeno a tu plantilla que se ocupa de web, programas, correo y equipos por una cuota mensual, con una sola persona de contacto."),
                                 ("¿Mantenéis programas que instaló otro proveedor?", "Sí. Hay un servicio para programas abandonados por su proveedor, tras revisar su estado."),
                                 ("¿De quién son la web y los datos?", "Tuyos. Uno de los servicios consiste precisamente en comprobar que dominios, web y datos están a nombre de tu empresa.")]

# ---------- FORMACIÓN IA: pregunta de apertura ----------
H["formacion-ia"] = _sec("Formación práctica", "¿Tu equipo ya usa IA, pero sin saber aplicarla con seguridad y con resultados?", _preg(
    "Cada persona prueba por su cuenta y nadie comparte lo que funciona.",
    "Se pegan datos de clientes en herramientas sin saber si es correcto.",
    "Se nota la curiosidad, pero no el ahorro de tiempo.")
    + '<p style="margin-top:22px;max-width:820px">La formación parte de las tareas reales de cada puesto y termina con unas normas de uso claras. Si aún no las tenéis, se puede empezar por la %s.</p>' % _a("formacion-ia", "Política de uso de IA para empresas", "política de uso de IA"), True)

# ---------- CONSULTORÍA: diagnóstico y hoja de ruta ----------
H["consultoria-y-ayudas"] = _sec("Prioridades", "Sabes que hay que digitalizar, pero no qué ni en qué orden",
    _resp("Qué obtienes del diagnóstico", "Una lista ordenada de lo que conviene hacer primero, lo que puede esperar y lo que no merece la pena, con una estimación de coste para cada paso. Sirve aunque después lo ejecutes con otro proveedor.")
    + '<div class="rejilla" style="margin-top:26px">'
    + _t("Diagnóstico", _a("consultoria-y-ayudas", "Diagnóstico de digitalización gratuito") + ": el punto de partida.")
    + _t("Hoja de ruta", _a("consultoria-y-ayudas", "Transformación digital por fases") + ", para repartir la inversión.")
    + _t("Otra mirada", _a("consultoria-y-ayudas", "Segunda opinión tecnológica") + " antes de firmar un presupuesto grande.")
    + '</div><p class="mut" style="margin-top:20px;font-size:15px;max-width:820px">Sobre ayudas públicas: las convocatorias abren y cierran, y cada una tiene sus requisitos. Antes de contar con una subvención comprobamos contigo si está vigente y si tu empresa puede solicitarla.</p>', True)
F["consultoria-y-ayudas"] = [("¿El diagnóstico de digitalización es gratuito?", "Sí. Nos cuentas cómo trabajas y te indicamos qué digitalizar o automatizar primero y cuánto costaría, sin compromiso."),
                             ("¿Tramitáis el Kit Digital?", "Gestionamos la solicitud cuando hay convocatoria abierta para tu tipo de empresa. La concesión depende del organismo que la convoca."),
                             ("¿Para qué sirve una segunda opinión tecnológica?", "Para contrastar un presupuesto o una propuesta que has recibido antes de comprometerte, con alguien que no vende esa solución.")]

# ---------- RELEVO: escena familiar ----------
H["relevo-y-continuidad"] = _sec("Empresa familiar", "Todo lo importante está en la cabeza de una sola persona",
    '<p class="lead" style="max-width:820px">Quién es cada proveedor, cómo se calcula un precio, qué cliente necesita un trato especial. Mientras esa persona está, todo funciona. El día que falta, se descubre cuánto dependía de ella.</p>'
    + _pasos(("Saber qué riesgo hay", _a("relevo-y-continuidad", "Diagnóstico de continuidad") + ": qué se perdería y qué es urgente recoger."),
             ("Dejarlo por escrito", _a("relevo-y-continuidad", "Manual de operaciones con vídeo e IA") + ", grabado mientras se trabaja."),
             ("Preparar a quien continúa", _a("relevo-y-continuidad", "Digitalización para el sucesor") + ", a su ritmo.")).replace('<ol class="rejilla"', '<ol class="rejilla" style="margin-top:26px"', 1)
    + '<p style="margin-top:22px">Si la idea es vender o traspasar: %s.</p>' % _a("relevo-y-continuidad", "Empresa lista para traspasar o vender", "empresa lista para traspasar o vender"), True)
F["relevo-y-continuidad"] = [("¿Cuándo hay que empezar a preparar el relevo?", "Cuanto antes. Documentar cómo se trabaja lleva tiempo y es más fácil hacerlo con calma que con una fecha encima."),
                             ("¿Hace falta que el fundador escriba un manual?", "No. Se recoge su conocimiento con entrevistas y grabaciones mientras trabaja, y después se ordena."),
                             ("¿Os ocupáis de la parte legal o fiscal del traspaso?", "No. Esa parte corresponde a tu asesor. Nosotros preparamos la documentación, los datos y las herramientas del negocio.")]

# ---------- PROBLEMAS SIN RESOLVER: tres frentes ----------
H["problemas-sin-resolver"] = _sec("Tres frentes", "Problemas concretos que ya sabemos resolver",
    _tabla(["Frente", "Qué ocurre", "Con qué se aborda"],
           [["Morosidad", "Clientes que pagan tarde o dejan de pagar", "%s y %s" % (_a("problemas-sin-resolver", "Sistema anti-impagos"), _a("problemas-sin-resolver", "Semáforo de clientes morosos", "semáforo de morosos"))],
            ["Burocracia", "Plazos, notificaciones y trámites que se escapan", "%s y %s" % (_a("problemas-sin-resolver", "Calendario de obligaciones"), _a("problemas-sin-resolver", "Buzón de notificaciones vigilado", "buzón vigilado"))],
            ["Falta de personal", "No encuentras a quién contratar o tardas en formarlo", "%s y %s" % (_a("problemas-sin-resolver", "Empleado digital"), _a("problemas-sin-resolver", "Formación rápida de nuevos empleados", "formación rápida"))]])
    + '<p style="margin-top:22px;max-width:820px"><b>Método:</b> primero se mide el problema (cuánto dinero o cuántas horas supone), luego se prueba la solución en pequeño y solo se extiende si los números mejoran.</p>', True)

# ---------- FICHADOR: caso práctico arriba ----------
H["fichador"] = _sec("Caso práctico", "Un negocio con turnos y el registro en una hoja de papel",
    _ej("Una cafetería con ocho empleados y dos turnos apunta las horas en una libreta. Cuando alguien olvida firmar, se rellena de memoria a final de mes. Con el fichador, cada persona marca la entrada y la salida desde su móvil, el encargado recibe un aviso si falta un fichaje y el informe mensual sale ya preparado.").replace("margin-top:22px", "margin-top:0")
    + _resp("Qué exige el registro de jornada", "Desde 2019 las empresas deben registrar cada día la hora de inicio y de fin de la jornada de cada trabajador y conservar esos registros durante cuatro años, a disposición de los trabajadores y de la Inspección de Trabajo.").replace('class="respuesta"', 'class="respuesta" style="margin-top:22px"')
    + '<p style="margin-top:18px">Tienes el detalle en %s y %s. El importe está en %s.</p>' % (
        _a("fichador", "Registros inalterables con historial", "registros inalterables"), _a("fichador", "Informe para Inspección en un clic", "informe para Inspección"), _a("fichador", "Precio por trabajador al mes", "precio por trabajador al mes")), True)
F["fichador"] = [("¿Es obligatorio el registro de jornada?", "Sí, desde 2019 para todas las empresas con trabajadores por cuenta ajena, sea cual sea su tamaño."),
                 ("¿Se puede fichar desde el móvil?", "Sí. Se puede fichar desde el móvil, una tablet, la web o con tarjeta NFC, y hay modo sin conexión para obras."),
                 ("¿Cuánto tiempo hay que guardar los registros?", "Cuatro años. El fichador los conserva y permite que cada trabajador consulte los suyos.")]

# ---------- ALOJAMIENTOS: un día con varias viviendas ----------
H["alojamientos-y-domotica"] = _sec("Varias viviendas", "Reservas, llaves, limpieza e incidencias repartidas en cuatro aplicaciones",
    '<p style="max-width:820px;margin-bottom:22px">Así cambia una jornada cuando todo se reúne en un panel:</p>'
    + _tabla(["Momento", "Qué pasa solo"],
             [["Entra una reserva", _a("alojamientos-y-domotica", "Calendario unificado con Airbnb, Booking y web propia", "El calendario se actualiza en Airbnb, Booking y tu web")],
              ["Antes de la llegada", "%s y %s" % (_a("alojamientos-y-domotica", "Check-in online con firma"), _a("alojamientos-y-domotica", "Envío automático a SES.HOSPEDAJES", "envío a SES.HOSPEDAJES"))],
              ["Llega el huésped", _a("alojamientos-y-domotica", "Cerradura con código por reserva")],
              ["Durante la estancia", _a("alojamientos-y-domotica", "Asistente del huésped por WhatsApp 24/7")],
              ["Al salir", _a("alojamientos-y-domotica", "Aviso automático a limpieza")]])
    + '<p class="mut" style="margin-top:18px;font-size:15px">Las conexiones disponibles dependen de las cerraduras, los sensores y los portales que utilices. Se comprueba antes de empezar.</p>', True)
F["alojamientos-y-domotica"] = [("¿Se envían los datos de los viajeros a SES.HOSPEDAJES?", "Sí. El registro de viajeros se envía de forma automática tras el check-in online."),
                                ("¿Puedo usar las cerraduras que ya tengo instaladas?", "Depende del modelo. Se revisa su compatibilidad antes de proponer cualquier cambio."),
                                ("¿Sirve si solo tengo una vivienda?", "Sí. El panel funciona con una vivienda y se amplía si incorporas más.")]

# Título propio de la sección de preguntas en cada página (para que no parezcan plantillas)
FH = {"webs": "Antes de encargar tu web", "presencia-digital": "Lo que suele preguntarse sobre visibilidad", "software-de-gestion": "Preguntas sobre el programa de gestión",
      "erp-para-pymes": "ERP para pymes: dudas frecuentes", "apps-moviles": "¿App o web? Y otras dudas", "software-especializado": "Lo que conviene saber del software a medida",
      "migraciones-e-integraciones": "Dudas al cambiar de programa", "agentes-de-ia": "Agentes de IA: preguntas habituales", "automatizacion-y-datos": "Preguntas sobre automatizar tareas",
      "pequenas-empresas": "Lo que nos preguntan las pequeñas empresas", "grandes-empresas": "Sobre los pilotos de IA", "startups-e-inversores": "Preguntas de fundadores",
      "deluxe": "Confidencialidad y alcance", "ciberseguridad-y-sistemas": "Seguridad informática: tres dudas comunes", "departamento-tecnologico": "Cómo funciona el soporte externo",
      "consultoria-y-ayudas": "Diagnóstico y ayudas: lo que hay que saber", "relevo-y-continuidad": "Preguntas sobre el relevo", "fichador": "Registro de jornada: respuestas rápidas",
      "alojamientos-y-domotica": "Dudas de propietarios y gestores"}


# =====================================================================
# Páginas generales: sobre nosotros, sectores, IA empresarial, blog, guías y precios
# =====================================================================

# Sobre nosotros (rutas relativas a la raíz)
SOBRE = _sec("A quién acompañamos", "Tres momentos distintos de un mismo camino", _rej(
    '<div class="tarjeta" style="border-top:4px solid var(--burdeos)"><h3>Quien tiene una idea</h3><p>Todavía no hay negocio, solo ganas y muchas dudas. Ayudamos a decidir qué hace falta para arrancar y qué puede esperar.</p><a class="mas" href="servicios/autonomos.html">Emprendedores y autónomos →</a></div>',
    '<div class="tarjeta" style="border-top:4px solid #83503A"><h3>Quien acaba de empezar</h3><p>Ya hay clientes, pero falta visibilidad y orden. Ponemos la base: presencia profesional y una forma sencilla de llevar el día a día.</p><a class="mas" href="servicios/presencia-digital.html">Presencia digital →</a></div>',
    '<div class="tarjeta" style="border-top:4px solid var(--ocre)"><h3>Quien ya tiene empresa</h3><p>El negocio funciona y toca ganar tiempo, cobrar antes o preparar el crecimiento sin perder el control.</p><a class="mas" href="servicios/pequenas-empresas.html">Pequeñas empresas →</a></div>')
    + '<div class="rejilla" style="margin-top:26px">'
    + _t("Lo que hacemos", "Presencia digital, programas de gestión, automatización, inteligencia artificial y formación, con soporte posterior.")
    + _t("Lo que no hacemos", "No somos gestoría ni asesoría fiscal o jurídica. Si la necesitas, te ayudamos a encontrar a ese profesional.")
    + _t("Dónde trabajamos", "100 % online para toda España. La sede está en Alcolea del Río (Sevilla).")
    + '</div>', True)

# Sectores: acceso por forma de trabajar (los anclajes son los id de las tarjetas que ya existen)
def _anc(*ss):
    return " · ".join('<a href="#%s">%s</a>' % (s.lower().replace(" ", "-"), s) for s in ss)

SECTORES = _sec("Encuentra el tuyo", "¿Cómo es tu día a día?", _tabla(
    ["Tu forma de trabajar", "Lo que suele complicarse", "Sectores"],
    [["Atiendes con cita previa", "Huecos vacíos, ausencias sin avisar y el teléfono sonando mientras atiendes", _anc("Clínicas", "Academias", "Talleres")],
     ["Trabajas en casa del cliente", "Presupuestos a mano, partes en papel y desplazamientos mal repartidos", _anc("Reformas e instaladores")],
     ["Vendes producto", "Stock que no cuadra, pedidos por varios canales y márgenes poco claros", _anc("Comercios", "Distribuidores", "Industria", "Hostelería")],
     ["Gestionas inmuebles o estancias", "Reservas, visitas y documentación repartidas en varias aplicaciones", _anc("Inmobiliarias", "Alojamientos turísticos")],
     ["Llevas expedientes de clientes", "Plazos, documentos y seguimiento de cada caso", _anc("Gestorías", "Asesorías energéticas")]])
    + '<p style="margin-top:18px">¿Tu sector no aparece? <a href="contacto.html#diagnostico">Cuéntanos a qué te dedicas</a> y vemos qué se puede adaptar.</p>', True)

# IA empresarial: tres situaciones reales (rutas relativas a /servicios/pix/)
PIX = _sec("Tres momentos de cualquier semana", "Cuándo se nota tener a la IA empresarial en la empresa", _rej(
    _d("Lunes, 9:00", "Quieres saber cómo fue la semana y los datos están en tres programas. La IA empresarial los reúne y te da el resumen, con lo que requiere tu atención."),
    _d("Martes, 22:15", "Un cliente escribe por WhatsApp con el negocio cerrado. La IA empresarial responde con tu información y, si hace falta, deja la cita apuntada.", " d2"),
    _d("Jueves, 13:30", "Hay facturas vencidas y nadie encuentra el momento de reclamarlas. La IA empresarial prepara los avisos y espera tu visto bueno antes de enviarlos.", " d3"))
    + '<p style="margin-top:22px;max-width:820px"><b>Siempre con supervisión.</b> Tú decides qué puede hacer la IA empresarial por su cuenta y qué necesita aprobación. Las condiciones y las fases de puesta en marcha están en <a href="implantacion-y-precios.html">implantación y precios</a>.</p>', True)

# Blog: acceso por temas (rutas relativas a /blog/)
BLOG = '<section class="sec sec-suave" style="padding:48px 0"><div class="w"><div class="cab" style="margin-bottom:22px"><p class="kicker">Por temas</p><h2>¿Qué te interesa leer?</h2></div><div class="pildoras">' + "".join(
    '<a class="pildora" href="../temas/%s.html">%s</a>' % (s, n) for s, n in [
        ("emprender-y-crecer", "Emprender y crecer"), ("webs-y-visibilidad", "Webs y visibilidad"), ("gestion-y-crm", "Gestión y CRM"),
        ("inteligencia-artificial", "Inteligencia artificial"), ("normativas-y-cumplimiento", "Normativas"), ("formacion-para-empresas", "Formación para empresas")]
) + '</div><p class="mut" style="margin-top:18px;font-size:15px">Cada artículo responde a una pregunta concreta. Si la tuya no está, <a href="../contacto.html">escríbenos</a> y la tendremos en cuenta.</p></div></section>'

# Guías: recorrido recomendado (rutas relativas a /guias/)
GUIAS = _sec("Si no sabes por cuál empezar", "Un recorrido en cuatro lecturas", _pasos(
    ("Aclara la idea", '<a href="como-emprender-un-negocio.html">Cómo emprender un negocio</a>, paso a paso.'),
    ("Mira cómo financiarla", '<a href="financiacion-para-emprendedores.html">Financiación para emprendedores</a> y <a href="ayudas-para-jovenes-emprendedores.html">ayudas para jóvenes</a>.'),
    ("Dale forma legal", '<a href="como-registrar-una-empresa-en-espana.html">Cómo registrar una empresa en España</a>. Los trámites los lleva tu gestor.'),
    ("Hazte visible", '<a href="como-crear-una-pagina-web.html">Cómo crear una página web</a> para que te encuentren.'))
    + '<p style="margin-top:20px">¿Prefieres comentarlo con alguien? <a href="../contacto.html#diagnostico">Cuéntanos en qué punto estás</a>.</p>', True)

# Precios: para quién es cada pack, antes de los importes (rutas relativas a la raíz)
PRECIOS = _sec("Antes de mirar importes", "¿Qué pack resuelve tu situación?", _tabla(
    ["Tu situación", "Pack", "Qué problema resuelve"],
    [["Acabas de empezar y nadie te encuentra en internet", "Impulso Inicial", "Te da imagen, una web sencilla y presencia en Google para recibir los primeros contactos"],
     ["Ya tienes clientes y el papeleo se come tus tardes", "Negocio en Marcha", "Añade un programa de gestión y automatizaciones a una web con blog preparada para buscadores"],
     ["Lanzas un proyecto y quieres que lo monten de principio a fin", "Llave en Mano", "Marca, web, embudo de ventas y gestión, con dos meses de acompañamiento"],
     ["Solo necesitas una parte", "Arma tu pack", "Eliges los servicios sueltos y recibes el precio antes de empezar"]])
    + '<p style="margin-top:18px">¿Dudas entre dos? En el <a href="contacto.html#diagnostico">diagnóstico gratuito</a> lo vemos contigo. El detalle de cada pack está en <a href="#que-incluye">qué incluye cada pack</a>.</p>', True)
