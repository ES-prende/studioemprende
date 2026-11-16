# Reescritura «dolores primero» · familia WhatsApp IA (noviembre 2026).
# Cada página tiene su propio recorrido; no se repite estructura ni frases entre ellas.
D = {}

# Estructura: frases que dice el dueño + tabla «qué pasa hoy / qué pasaría» + límites
D["servicios/whatsapp-ia/asistente-de-ia-para-whatsapp"] = {
 "estructura": "frases-en-primera-persona + tabla-por-franja-horaria + lista-de-limites",
 "lead": "Te escriben a las once de la noche, mientras atiendes a otro cliente o en pleno fin de semana, y cuando por fin contestas ya han preguntado en otro sitio. Un asistente de IA en tu WhatsApp Business responde en el momento con la información de tu negocio y te deja la gestión hecha.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">¿Te pasa esto con el WhatsApp del negocio?</p><h2>El móvil no para y aun así se te escapan clientes</h2></div>
<ul class="lista" style="font-size:18px;max-width:820px">
<li>«Contesto por la noche, cuando cierro, y la mitad ya no responde.»</li>
<li>«Me preguntan veinte veces al día el precio, el horario y si hay hueco esta semana.»</li>
<li>«Tengo mensajes sin leer de hace tres días y no sé cuáles eran para comprar.»</li>
<li>«Si me pongo malo o me voy de vacaciones, el WhatsApp se queda mudo.»</li>
</ul>
<p style="max-width:820px;margin-top:18px">No es dejadez: es que atender un chat y trabajar a la vez no cabe en la misma hora. Las respuestas automáticas de la aplicación («ahora no estamos, te contestamos mañana») no arreglan nada, porque el cliente quería una contestación, no un acuse de recibo.</p>
<div class="tabla-wrap" style="margin-top:22px"><table class="tabla-norm"><thead><tr><th>Cuándo escriben</th><th>Qué ocurre ahora</th><th>Qué hace el asistente de IA</th></tr></thead><tbody>
<tr><td>En horario, con el local lleno</td><td>El mensaje espera a que alguien quede libre</td><td>Responde precio, disponibilidad o dirección y solo te avisa si hace falta una persona</td></tr>
<tr><td>Por la noche o en festivo</td><td>Se lee al día siguiente, a veces tarde</td><td>Deja la cita reservada o el pedido anotado en tu programa</td></tr>
<tr><td>Cuando vuelve días después</td><td>Hay que releer toda la conversación</td><td>Retoma lo hablado y continúa desde ahí</td></tr>
<tr><td>Con una queja o un caso delicado</td><td>Se mezcla con el resto de chats</td><td>Lo pasa a tu equipo con un resumen y deja de contestar por su cuenta</td></tr>
</tbody></table></div>
<h3 style="margin-top:30px">Lo que no le dejamos hacer</h3>
<p style="max-width:820px">Un chatbot de WhatsApp mal planteado genera más problemas que los que quita. Por eso acordamos contigo qué puede contestar y qué no: no negocia precios que tú no hayas fijado, no da consejo médico ni legal, no promete plazos que tu agenda no confirma y se presenta siempre como asistente automático. Antes de activarlo lo probamos con conversaciones reales de tu negocio y, si usas ya un <a href="/servicios/software-de-gestion">programa de gestión</a>, comprobamos que la conexión es posible antes de darte presupuesto.</p>
</div></section>""",
 "faq": [
  ("¿Cómo automatizar WhatsApp Business con IA sin perder el trato cercano?", "Dejando al asistente lo repetitivo (precios, horarios, disponibilidad, estado de un pedido) y reservando para tu equipo lo que requiere criterio. El cliente puede pedir hablar con una persona en cualquier momento y la conversación pasa con su resumen."),
  ("¿En qué se diferencia de las respuestas automáticas de WhatsApp Business?", "Las respuestas automáticas envían un texto fijo. El asistente de IA lee lo que pregunta cada cliente, contesta con los datos de tu negocio y completa la gestión: reservar, anotar el pedido o abrir la incidencia."),
 ],
}

# Estructura: cuenta de huecos perdidos (cálculo con tus propios números) + línea de tiempo de una cita + para quién no compensa
D["servicios/whatsapp-ia/citas-y-recordatorios-automaticos"] = {
 "estructura": "calculo-con-numeros-propios + linea-de-tiempo-de-una-cita + cuando-no-compensa",
 "lead": "Una silla vacía a las cinco de la tarde porque alguien olvidó su cita es dinero que ya no recuperas, y llamar uno por uno para confirmar te come la mañana. Con las citas y los recordatorios por WhatsApp el cliente reserva, confirma o cambia desde el chat y el hueco libre vuelve a ofrecerse.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Antes de nada, haz esta cuenta</p><h2>¿Cuánto te cuestan las ausencias y los plantones?</h2><p class="lead" style="margin-top:8px">No necesitas ninguna herramienta para saberlo, solo tu agenda del mes pasado.</p></div>
<ol class="rejilla" style="list-style:none;margin:0;padding:0">
<li class="tarjeta"><h3>1. Cuenta las citas que no se presentaron</h3><p>Las que avisaron tarde también valen: ese hueco tampoco se llenó.</p></li>
<li class="tarjeta"><h3>2. Multiplica por tu servicio medio</h3><p>Una limpieza dental, una sesión de fisioterapia, un corte y color, una revisión de taller.</p></li>
<li class="tarjeta"><h3>3. Suma el tiempo de confirmar por teléfono</h3><p>Llamadas que no cogen, mensajes sueltos y la agenda de papel corregida a boli.</p></li>
</ol>
<p style="max-width:820px;margin-top:20px">La cifra que salga es tuya, no una estadística nuestra, y sirve para decidir si te compensa automatizar los recordatorios de cita. En clínicas, centros de estética, peluquerías, academias y talleres suele ser el primer punto que se arregla.</p>
<h3 style="margin-top:30px">Qué le ocurre a una cita desde que se pide hasta que se atiende</h3>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Momento</th><th>Mensaje por WhatsApp</th><th>Efecto en tu agenda</th></tr></thead><tbody>
<tr><td>El cliente pide hora</td><td>Recibe dos o tres huecos reales y elige</td><td>La cita aparece en el profesional o la sala que toca</td></tr>
<tr><td>Días u horas antes</td><td>Recordatorio con dirección e indicaciones</td><td>Queda marcada como confirmada, cambiada o anulada</td></tr>
<tr><td>Si anula</td><td>Se le ofrece otra fecha</td><td>El hueco se propone a quien estaba en lista de espera</td></tr>
<tr><td>Después de la visita</td><td>Aviso de la próxima revisión, si la hay</td><td>El seguimiento no depende de la memoria de nadie</td></tr>
</tbody></table></div>
<h3 style="margin-top:30px">Cuándo no te hace falta</h3>
<p style="max-width:820px">Si atiendes sin cita, si das menos de un puñado de horas a la semana o si tus clientes prefieren llamar, un sistema de reserva por WhatsApp aporta poco y te lo diremos. Tampoco sustituye a recepción en lo que requiere valorar un caso. Si lo que buscas es que la reserva se haga desde la web, mira la <a href="/servicios/software-de-gestion/agenda-y-citas-online">agenda y citas online</a>; las dos vías pueden convivir sobre la misma agenda.</p>
</div></section>""",
 "faq": [
  ("¿Cómo reducir las ausencias a las citas sin llamar a cada cliente?", "Con un recordatorio automático por WhatsApp que permite confirmar, cambiar o anular respondiendo al mensaje. Quien no puede ir libera el hueco con antelación y ese hueco se ofrece a otra persona."),
  ("¿Necesito cambiar de programa de agenda para dar citas por WhatsApp?", "No siempre. Depende de si tu agenda actual permite conectarse. Lo comprobamos antes de presupuestar y, si no es posible, te proponemos la alternativa con menos cambios para tu equipo."),
 ],
}
