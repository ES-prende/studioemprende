# Landings de captación (desde el 13/11/2026). Páginas nuevas en la raíz: hablan solo de los dolores de la persona
# y terminan en un formulario. Público: quien quiere montar su propio negocio vendiendo a empresas las soluciones
# de Studio Emprende (agencia de IA; programas de gestión con IA).
# Reglas del texto: sin precios, sin promesas de ingresos ni plazos, sin cifras ni testimonios inventados,
# sin condiciones económicas (no están definidas) y no se presenta como gestoría ni asesoría: se ayuda a encontrarlas.
import html as _h



def _e(s):
    return _h.escape(s, quote=True)


def html(L, migas_html, dom):
    dolores = "".join('<div class="tarjeta"><h3>«%s»</h3><p>%s</p></div>' % (_e(d[0]), _e(d[1])) for d in L["dolores"])
    opciones = "".join("<option>%s</option>" % _e(o) for o in L["opciones"])
    faq = ""
    if L.get("faqs"):
        faq = ('<section class="sec"><div class="w"><div class="cab"><h2>Dudas antes de escribirnos</h2></div><div class="faq">%s</div></div></section>'
               % "".join("<details><summary>%s</summary><p>%s</p></details>" % (_e(q), _e(a)) for q, a in L["faqs"]))
    otra = ('<section class="sec" style="padding-top:0"><div class="w"><p class="mut">%s <a href="%s">%s</a></p></div></section>' % (_e(L["otra"][0]), L["otra"][1], _e(L["otra"][2]))) if L.get("otra") else ""
    preguntas = "".join('<div class="campo"><label for="%s">%s</label><select id="%s" name="%s" required><option value="">Elige una opción</option>%s</select><span class="error" hidden style="color:#A3222F;font-size:13px">Elige una opción</span></div>'
                        % (n, _e(t), n, n, "".join("<option>%s</option>" % _e(o) for o in ops)) for n, t, ops in L.get("preguntas", []))
    if preguntas: preguntas = '<div class="dos">%s</div>' % preguntas
    extra = ""
    if L.get("incluye"):
        extra += ('<section class="sec"><div class="w"><div class="cab"><p class="kicker">Qué incluye</p><h2>Todo lo que te damos para arrancar</h2></div><div class="rejilla">%s</div></div></section>'
                  % "".join('<div class="tarjeta"><h3>%s</h3><p>%s</p></div>' % (_e(a), _e(b)) for a, b in L["incluye"]))
    if L.get("fases"):
        extra += ('<section class="sec sec-suave"><div class="w"><div class="cab"><p class="kicker">Cómo es el programa</p><h2>%s</h2><p class="lead" style="margin-top:8px">%s</p></div><div class="rejilla">%s</div></div></section>'
                  % (_e(L["fases_titulo"]), _e(L["fases_intro"]), "".join('<div class="tarjeta"><p class="kicker" style="margin:0">Fase %d</p><h3>%s</h3><p>%s</p></div>' % (i + 1, _e(a), _e(b)) for i, (a, b) in enumerate(L["fases"]))))
    if L.get("profesor"):
        extra += ('<section class="sec"><div class="w lateral"><div class="lateral-main"><div class="cab" style="margin-bottom:16px"><p class="kicker">Quién te forma</p><h2>%s</h2></div><p class="lead">%s</p></div>'
                  '<aside class="lateral-aside"><h2 class="h3">Para quién es</h2>%s<h2 class="h3" style="margin-top:10px">Para quién no es</h2>%s</aside></div></section>'
                  % (_e(L["profesor"][0]), _e(L["profesor"][1]), "".join('<p style="color:#C9C1BB">✓ %s</p>' % _e(x) for x in L["para_si"]), "".join('<p style="color:#C9C1BB">✗ %s</p>' % _e(x) for x in L["para_no"])))
        if L.get("no_es"):
            extra += ('<section class="sec sec-noche"><div class="w"><div class="cab"><p class="kicker">Antes de seguir</p><h2>%s</h2></div><div class="rejilla">%s</div></div></section>'
                      % (_e(L["no_es"][0]), "".join('<div class="tarjeta" style="background:#2B2427;border-color:#3A3134"><p style="color:#E9E4E0">%s</p></div>' % _e(x) for x in L["no_es"][1])))
        extra += '<section class="sec"><div class="w"><div class="botones"><a class="btn btn-p" href="#formulario">%s</a></div></div></section>' % _e(L["boton_hero"])
    return """<section class="page-hero"><div class="w">{m}<p class="kicker">{kicker}</p><h1>{h1}</h1>
<p class="lead">{entradilla}</p>
<div class="botones" style="margin-top:24px"><a class="btn btn-p" href="#formulario">{boton_hero}</a></div></div></section>

<section class="sec"><div class="w"><div class="cab"><h2>{titulo_dolores}</h2></div>
<div class="rejilla">{dolores}</div></div></section>

<section class="sec sec-noche"><div class="w"><div class="cab" style="margin-bottom:0"><h2>{puente_titulo}</h2><p class="lead" style="margin-top:10px">{puente}</p>
<div class="botones" style="margin-top:20px"><a class="btn btn-claro" href="#formulario">{boton_hero}</a></div></div></div></section>

{extra}<section class="sec sec-suave" id="formulario"><div class="w lateral"><div class="lateral-main">
<div class="cab"><h2>{form_titulo}</h2><p class="lead" style="margin-top:8px">{form_intro}</p></div>
<form class="form" data-contacto action="https://formsubmit.co/info@studioemprende.com" method="post">
<input type="hidden" name="_subject" value="{asunto}">
<input type="hidden" name="_cc" value="socialstudioemprende@gmail.com">
<input type="hidden" name="_template" value="table">
<input type="hidden" name="_next" value="{dom}/gracias.html">
<input type="hidden" name="origen" value="{origen}">
<input type="hidden" name="_captcha" value="true">
<input type="hidden" name="_blacklist" value="viagra, casino, crypto, bitcoin, forex, loan, seo services, backlinks, porn, betting, http://, https://bit.ly">
<input type="hidden" name="_autoresponse" value="Hola, hemos recibido tu mensaje en Studio Emprende. Te escribimos en menos de 24 horas laborables para hablar de tu caso.">
<input type="hidden" name="_t" id="_t" value="">
<input type="hidden" name="utm_source" value=""><input type="hidden" name="utm_medium" value=""><input type="hidden" name="utm_campaign" value=""><input type="hidden" name="utm_content" value="">
<div aria-hidden="true" style="position:absolute;left:-10000px;top:auto;width:1px;height:1px;overflow:hidden"><label>No rellenar<input type="text" name="_honey" tabindex="-1" autocomplete="off"></label><label>Web<input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
<p class="form-aviso" id="form-aviso" role="alert" hidden></p>
<div class="dos"><div class="campo"><label for="nombre">Nombre</label><input id="nombre" name="nombre" autocomplete="name" required minlength="2" maxlength="80" pattern=".*\\S.*"><span class="error" hidden style="color:#A3222F;font-size:13px">Escribe tu nombre</span></div>
<div class="campo"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" required maxlength="120"><span class="error" hidden style="color:#A3222F;font-size:13px">Escribe tu email</span></div></div>
<div class="dos"><div class="campo"><label for="telefono">Teléfono (opcional, si prefieres que te llamemos)</label><input id="telefono" name="telefono" type="tel" autocomplete="tel" inputmode="tel" maxlength="20" pattern="[+0-9 .\\(\\)\\-]{{9,20}}" title="Solo números, mínimo 9 cifras"></div>
<div class="campo"><label for="punto">{etiqueta_punto}</label><select id="punto" name="punto" required><option value="">Elige una opción</option>{opciones}</select><span class="error" hidden style="color:#A3222F;font-size:13px">Elige una opción</span></div></div>
{preguntas}<div class="campo"><label for="mensaje">{etiqueta_texto}</label><textarea id="mensaje" name="mensaje" rows="5" maxlength="2000" aria-describedby="mensaje-ayuda"></textarea><span id="mensaje-ayuda" class="mut" style="font-size:13px">Basta con unas líneas sobre tu situación profesional. No incluyas datos de salud ni otros datos sensibles.</span></div>
<label style="display:flex;gap:10px;font-size:14px;align-items:flex-start"><input type="checkbox" name="privacidad" required style="margin-top:4px"> <span>He leído y acepto la <a href="privacidad.html">política de privacidad</a>.</span></label>
<p class="mut" style="font-size:13px;margin:0">Responsable: INTELIGENCIA SEVILLA SL (Studio Emprende). Finalidad: responder a tu solicitud y valorar contigo si encaja montar tu negocio con nuestras soluciones. Base: tu consentimiento. Puedes ejercer tus derechos de acceso, rectificación y supresión en info@studioemprende.com.</p>
<div><button class="btn btn-p" type="submit">{boton}</button></div>
</form></div>
<aside class="lateral-aside"><h2 class="h3">Qué pasa después</h2>
<p style="color:#C9C1BB">1. Leemos lo que nos cuentas.</p>
<p style="color:#C9C1BB">2. Te escribimos en menos de 24 horas laborables.</p>
<p style="color:#C9C1BB">3. Hablamos de tu caso por videollamada o por teléfono.</p></aside>
</div></section>
{faq}{otra}
<script>(function(){{var q=new URLSearchParams(location.search);["utm_source","utm_medium","utm_campaign","utm_content"].forEach(function(k){{var v=q.get(k),i=document.querySelector('form[data-contacto] input[name="'+k+'"]');if(v&&i)i.value=v.slice(0,100)}})}})();</script>""".format(m=migas_html, dom=dom, dolores=dolores, otra=otra, extra=extra, preguntas=preguntas, opciones=opciones, faq=faq,
                **{k: _e(L[k]) for k in ("kicker", "h1", "entradilla", "boton_hero", "titulo_dolores", "puente_titulo", "puente", "form_titulo",
                                         "form_intro", "asunto", "origen", "etiqueta_punto", "etiqueta_texto", "boton")})


_FORM_INTRO = "Rellena el formulario y te respondemos en menos de 24 horas laborables. La primera conversación es gratuita y sin compromiso: vemos tu caso y te decimos con sinceridad si esto encaja contigo."
_PUENTE_FIN = ("Te formamos, te montamos tu empresa digital y te damos las herramientas y el equipo comercial para vender. "
               "Te aconsejamos en la gestión, en lo fiscal y en las ayudas, y seguimos detrás como soporte. Con tus clientes no nos metemos: el negocio es tuyo. ")

_INCLUYE = [
 ("Formación online con profesor certificado", "Clases en directo y grabadas, desde cualquier sitio, impartidas por un profesor con certificado de docencia. Y te acompañamos durante todo tu inicio."),
 ("Tu web y tu presencia digital", "Te montamos la web, la infraestructura y la presencia digital de tu empresa, con los accesos y las herramientas ya listos."),
 ("Qué vender y a quién", "Te ayudamos a decidir en qué productos y en qué sectores centrarte, y a preparar la oferta para cada empresa."),
 ("Herramientas para vender", "Todo lo necesario para presentar y vender las soluciones a las empresas, y para buscar clientes."),
 ("Equipo comercial", "Te damos un equipo comercial que capta clientes e incluso cierra ventas, con una base de datos con la que trabajar. Y te aconsejamos en cómo gestionarlo."),
 ("Cómo hacer una consultoría", "Te enseñamos a analizar una empresa y a hacerle una propuesta, algo que casi nadie sabe hacer cuando empieza."),
 ("Gestión y organización", "Facturas, presupuestos, organización del día a día: te ayudamos a llevarlo todo con orden desde el principio."),
 ("Fiscalidad y ayudas", "Charlas y reuniones uno a uno con asesores para conocer la parte fiscal, las ayudas y subvenciones y las plataformas para pedirlas. Te acompañamos en todo el proceso."),
 ("Charlas de economía", "Una persona experta en economía te da charlas para que, cuando empieces a ganar, sepas conservar ese dinero y hacer crecer tu patrimonio."),
 ("Te ayudamos a encontrar a tus profesionales", "No somos gestoría ni asesoría, ni tenemos espacio de coworking, pero te ayudamos a encontrar los que te encajen."),
 ("Soporte cuando lo necesites", "Cuando te atasques tienes a quién preguntar, también cuando termine la formación. A ti te ayudamos en todo; con tus clientes no nos metemos."),
]
_FASES = [
 ("Base", "Formación en las herramientas, cómo se instalan y cómo se gestionan, con casos prácticos."),
 ("Tu empresa", "Te montamos la web, la presencia digital y tu entorno de trabajo, y eliges sector y producto."),
 ("Salir a vender", "Aprendes a hacer una consultoría y a preparar ofertas. Arranca el equipo comercial."),
 ("Crecer con orden", "Gestión, fiscalidad, ayudas y economía, con reuniones uno a uno y soporte continuo."),
]
_PROFESOR = ("Un profesor con certificado de docencia, asesores y un equipo que desarrolla software cada día",
             "La formación la imparte un profesor con certificado de docencia. Tendrás reuniones uno a uno con asesores en fiscalidad y ayudas, y charlas de economía con una persona experta. Detrás está el equipo de Studio Emprende, que desarrolla las herramientas que vas a vender. No aprendes de alguien que solo vende cursos, sino de quien hace las herramientas.")
_FASES_INTRO = "Formación online y acompañamiento en todo tu inicio, por fases. Te contamos la duración y el calendario en la primera conversación."
_NO_ES = ("Si ya quieres tu Ferrari, este no es tu sitio", [
 "Si buscas hacerte rico en 90 días, aquí no lo vas a encontrar. No prometemos ingresos.",
 "Si no quieres hablar con empresas ni trabajar tu negocio, esto no es para ti.",
 "Si esperas que otro lo haga todo por ti, tampoco. Te damos la base, el equipo y el apoyo; la empresa la levantas tú.",
 "Si quieres construir algo serio, empezar con poco, gestionarlo bien y saber conservar lo que ganes, hablemos.",
])
_PREGUNTAS = [
 ("tiempo", "¿Cuánto tiempo puedes dedicarle a la semana?", ["Menos de 5 horas", "Entre 5 y 15 horas", "Entre 15 y 30 horas", "Más de 30 horas, a tiempo completo"]),
 ("situacion", "¿Cuál es tu situación ahora?", ["Trabajo por cuenta ajena", "Soy autónomo o tengo empresa", "Estoy en paro o buscando algo nuevo", "Estudio", "Otra"]),
 ("cuando", "¿Cuándo te gustaría empezar?", ["Ya, cuanto antes", "En el próximo mes", "En unos meses", "Solo quiero información"]),
 ("invertir", "¿Estás dispuesto a invertir en tu formación y en tu negocio?", ["Sí", "Depende de las condiciones", "Ahora mismo no"]),
]

LANDINGS = [
 {"slug": "montar-agencia-de-ia", "no_es": _NO_ES, "preguntas": _PREGUNTAS, "incluye": _INCLUYE, "fases": _FASES, "fases_titulo": 'De cero a tu agencia de IA, paso a paso', "fases_intro": _FASES_INTRO, "profesor": _PROFESOR, "para_si": ['Quieres montar tu propia agencia de IA y no sabes por dónde empezar', 'Has hecho cursos o visto vídeos y te falta saber vender', 'Puedes dedicarle tiempo de verdad'], "para_no": ['Buscas dinero rápido sin trabajar', 'No quieres hablar con empresas'], "miga": "Montar tu agencia de IA",
  "titulo": "Montar una agencia de IA: por dónde empezar a vender",
  "meta": "Meses de tutoriales de IA y ningún cliente. Si no sabes qué vender ni a quién, cuéntanos en qué punto estás. La primera conversación es gratuita.",
  "kicker": "Para quien quiere montar su agencia de IA",
  "h1": "Muchos vídeos de IA. Ningún cliente.",
  "entradilla": "Llevas meses aprendiendo herramientas, montando asistentes y viendo tutoriales. Lo que falta es venderlo: qué ofrecer, a quién y qué decir cuando te sientas delante de una empresa.",
  "boton_hero": "Cuéntanos en qué punto estás",
  "titulo_dolores": "Si te reconoces en alguna de estas frases, esto va contigo",
  "dolores": [
   ("He visto mil vídeos y sigo sin vender nada.", "Tengo asistentes y automatizaciones montados. Los he enseñado a amigos, pero no se los he vendido a nadie."),
   ("Lo técnico lo voy sacando. Lo que no sé es vender.", "No sé cómo conseguir una reunión con una empresa ni qué decir cuando me la dan. Y si me preguntan el precio, me quedo en blanco."),
   ("No sé qué ofrecer ni a quién.", "Hoy escribo a una clínica, mañana a un taller y pasado a una inmobiliaria, con el mismo mensaje. Y elegir un sector me da miedo, porque siento que pierdo a todos los demás."),
   ("Cada mes sale una herramienta nueva y no domino ninguna.", "Empiezo con una, me recomiendan otra y cambio. Siempre estoy aprendiendo y nunca siento que ya puedo salir a vender."),
   ("Me da miedo que algo falle delante del cliente.", "Que el asistente se invente una respuesta o que algo deje de funcionar. Quien da la cara soy yo, y no tengo a nadie al lado a quien preguntar."),
   ("Y de papeles no sé nada.", "Si tengo que darme de alta de autónomo antes de vender, qué contrato firmo, qué pasa con los datos de los clientes de mi cliente."),
  ],
  "otra": ("¿Lo tuyo son más los programas de gestión?", "vender-programas-de-gestion-con-ia.html", "Tenemos otra página para ti →"),
  "puente_titulo": "Te formamos y te acompañamos en todo tu inicio",
  "puente": ("En Studio Emprende hacemos los asistentes de IA y los programas de gestión; tú los vendes y los pones en marcha en las empresas, con tu propia empresa. "
             + _PUENTE_FIN + "No prometemos ingresos: la empresa la levantas tú, pero no a ciegas."),
  "form_titulo": "Cuéntanos en qué punto estás", "form_intro": _FORM_INTRO,
  "asunto": "Landing agencia de IA: nuevo contacto", "origen": "landing-agencia-de-ia",
  "etiqueta_punto": "¿En qué punto estás?",
  "opciones": ["Todavía no he empezado", "He montado pruebas, pero no tengo ningún cliente", "He tenido algún cliente y no consigo más",
               "Ya tengo clientes de otros servicios y quiero ofrecerles IA", "Otra situación (cuéntanosla abajo)"],
  "etiqueta_texto": "Cuéntanos tu situación y qué es lo que más te frena",
  "boton": "Quiero que hablemos",
  "faqs": [
   ("¿Hace falta saber programar para montar una agencia de IA con vosotros?", "No hace falta saber programar: las herramientas ya están hechas. Sí hace falta entender cómo funcionan, porque quien las pone en marcha y responde ante el cliente eres tú."),
   ("¿Me ayudáis a conseguir clientes?", "Sí. Te damos un equipo comercial que capta clientes e incluso cierra ventas, y te enseñamos a gestionarlo. El negocio y la relación con tus clientes son tuyos. Tampoco garantizamos clientes ni ingresos: es tu negocio y depende de tu trabajo."),
   ("¿Cuánto cuesta y qué condiciones tiene montar la agencia con vosotros?", "Depende de tu caso. Te explicamos las condiciones con claridad en la primera conversación, antes de que te comprometas a nada."),
   ("¿Sois gestoría o asesoría?", "No. Te damos charlas y reuniones uno a uno con asesores sobre fiscalidad y ayudas, y te ayudamos a encontrar la gestoría, la asesoría o el coworking que te encaje. Los trámites los cierras con ellos."),
  ]},
 {"slug": "vender-programas-de-gestion-con-ia", "no_es": _NO_ES, "preguntas": _PREGUNTAS, "incluye": _INCLUYE, "fases": _FASES, "fases_titulo": 'De cero a vender programas de gestión con IA', "fases_intro": _FASES_INTRO, "profesor": _PROFESOR, "para_si": ['Conoces un sector y ves que las empresas siguen con Excel', 'No sabes programar o no tienes producto propio', 'Puedes dedicarle tiempo de verdad'], "para_no": ['Buscas dinero rápido sin trabajar', 'No quieres hablar con empresas'], "miga": "Vender programas de gestión con IA",
  "titulo": "Vender programas de gestión con IA: por dónde empezar",
  "meta": "Conoces un sector que sigue con Excel y papel, pero no sabes programar ni tienes producto. Cuéntanos en qué punto estás. La primera charla es gratuita.",
  "kicker": "Para quien quiere vender programas de gestión a empresas",
  "h1": "Sabes qué les hace falta. No tienes qué venderles.",
  "entradilla": "Conoces tu sector por dentro. Ves empresas que siguen con el Excel, la libreta y el WhatsApp, y sabes que con un buen programa de gestión trabajarían mejor. Pero no sabes programar ni tienes producto.",
  "boton_hero": "Cuéntanos en qué punto estás",
  "titulo_dolores": "Si te suena alguna de estas frases, sigue leyendo",
  "dolores": [
   ("Sé qué les hace falta, pero no tengo nada que enseñarles.", "Entro en una empresa, veo cómo trabajan y lo tengo claro. Pero no sé programar y no tengo ningún programa."),
   ("Encargar un programa a medida se me va de presupuesto.", "Pagar un desarrollo desde cero para luego ver si lo vendo es un riesgo que no puedo asumir."),
   ("No sé qué ofrecer ni a qué sector.", "Un día pienso en un CRM, otro en la facturación, otro en algo con IA. Y elegir me da vértigo, porque siento que cierro puertas."),
   ("Sé mucho de mi sector, pero no sé vender.", "Cuando tengo delante al dueño me pongo a hablar de tecnología en vez de hablar de su negocio. Me dice que se lo piensa y ya no vuelvo a saber de él."),
   ("Llevo meses dándole vueltas y sigo sin un solo cliente.", "He mirado herramientas, he pensado el nombre y he hecho números. Todo menos ofrecérselo a una empresa, que es justo lo que no sé cómo hacer."),
   ("Me da miedo venderlo y no tener a quién acudir cuando algo falle.", "Pasar los datos del Excel del cliente, que algo salga mal, que me llamen y no sepa arreglarlo. Y de contratos y protección de datos no sé nada."),
  ],
  "otra": ("¿Lo tuyo son más los asistentes de IA y las automatizaciones?", "montar-agencia-de-ia.html", "Tenemos otra página para ti →"),
  "puente_titulo": "Te formamos y te acompañamos en todo tu inicio",
  "puente": ("En Studio Emprende hacemos los programas de gestión con IA; tú los vendes y los pones en marcha en las empresas, con tu propia empresa. "
             + _PUENTE_FIN + "No prometemos ingresos: la empresa la levantas tú, pero no partes de cero."),
  "form_titulo": "Cuéntanos en qué punto estás", "form_intro": _FORM_INTRO,
  "asunto": "Landing programas de gestión con IA: nuevo contacto", "origen": "landing-vender-programas-de-gestion",
  "etiqueta_punto": "¿En qué punto estás?",
  "opciones": ["Tengo la idea y todavía no he hecho nada", "He hablado con alguna empresa y no he vendido nada", "Tengo una empresa interesada y nada que entregarle",
               "Ya trabajo con empresas de un sector y quiero ofrecerles programas", "Ya vendo programas de otra empresa y quiero cambiar de proveedor", "Otra situación (cuéntanosla abajo)"],
  "etiqueta_texto": "¿A qué te dedicas ahora y qué es lo que más te frena? Si conoces bien algún sector, dinos cuál",
  "boton": "Quiero que hablemos",
  "faqs": [
   ("¿Hace falta saber programar para vender programas de gestión?", "No. Las herramientas ya están hechas y tienes nuestro soporte técnico para consultarnos. Lo que sí tendrás que aprender es a ponerlas en marcha y a gestionarlas, porque quien responde ante tu cliente eres tú."),
   ("¿Me ayudáis a conseguir clientes?", "Sí. Te damos un equipo comercial que capta clientes e incluso cierra ventas, y te enseñamos a gestionarlo. El negocio y la relación con tus clientes son tuyos. Tampoco garantizamos clientes ni ingresos: es tu negocio y depende de tu trabajo."),
   ("¿Cuánto cuesta y qué condiciones tiene vender vuestros programas?", "Depende de tu caso. Te explicamos las condiciones con claridad en la primera conversación, antes de que te comprometas a nada."),
   ("¿Sois gestoría o asesoría?", "No. Te damos charlas y reuniones uno a uno con asesores sobre fiscalidad y ayudas, y te ayudamos a encontrar la gestoría, la asesoría o el coworking que te encaje. Los trámites los cierras con ellos."),
  ]},
]
