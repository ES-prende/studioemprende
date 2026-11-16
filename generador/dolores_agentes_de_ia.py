# Reescritura «dolores primero» · familia Agentes de IA (noviembre 2026).
# Cada página es un caso de uso concreto, con su propio recorrido y sus límites dichos con claridad.
# Las capacidades generales del producto se enlazan a /servicios/pix/… en vez de repetirse aquí.
D = {}

# Estructura: escena de la semana previa al cierre + cómo llegan los papeles + pasos previos de privacidad + cuándo no compensa
D["servicios/agentes-de-ia/agente-documental-para-gestorias"] = {
 "estructura": "escena-semana-de-cierre + lista-de-como-llegan-los-papeles + pasos-previos-de-privacidad + cuando-no-compensa",
 "lead": "La semana antes de cada trimestre tu gestoría no asesora: persigue. Fotos de tickets por WhatsApp, correos con diez adjuntos sin nombre y clientes que juran haberlo enviado todo. Un agente de IA para gestorías recibe, ordena y reclama esa documentación para que el técnico empiece el cierre revisando, no buscando.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Del día 1 al día 20</p><h2>¿Por qué el cierre empieza siempre persiguiendo papeles?</h2></div>
<p style="max-width:820px">Porque cada cliente envía la documentación como le viene bien y nadie en el despacho tiene tiempo de ordenarla según llega. El trabajo difícil de una asesoría no suele ser calcular un modelo, sino conseguir a tiempo lo que hace falta para calcularlo.</p>
<p style="max-width:820px">Si llevas una gestoría, esto te sonará:</p>
<ul class="lista" style="max-width:820px">
<li>La foto torcida de una factura, mandada al móvil personal de la técnica un sábado.</li>
<li>Un PDF llamado «escaneo0047» que no dice de qué empresa es ni de qué mes.</li>
<li>El extracto del banco que llega el día 18, después de tres llamadas.</li>
<li>El mismo justificante enviado por correo y por WhatsApp «por si acaso».</li>
<li>Una hoja de cálculo donde alguien apunta a mano qué falta de cada cliente y que siempre va por detrás.</li>
</ul>
<h3 style="margin-top:30px">Qué hay que dejar decidido antes de conectar nada</h3>
<ol style="max-width:820px">
<li><strong>Qué se espera de cada cliente y cuándo.</strong> Sin esa lista, el agente no puede saber qué falta.</li>
<li><strong>Por dónde entra la documentación.</strong> Conviene acordar uno o dos canales y avisar a los clientes; el móvil personal de nadie debería ser uno de ellos.</li>
<li><strong>Quién ve qué.</strong> Tratas datos de terceros: permisos por cliente, encargo de tratamiento y plazo de conservación se revisan antes, no después. Cómo se controla está explicado en <a href="/servicios/pix/seguridad-y-control">seguridad y control humano de PIX</a>.</li>
<li><strong>Qué se hace con lo dudoso.</strong> Un archivo ilegible o contradictorio se marca para una persona; no se da por bueno.</li>
</ol>
<h3 style="margin-top:30px">Cuándo todavía no te compensa</h3>
<p style="max-width:820px">Si tus clientes ya suben todo a un portal ordenado, o si llevas pocas empresas y la documentación llega bien, automatizar la recepción aporta poco. Y si el cuello de botella es teclear facturas y no reclamarlas, puede bastarte con la <a href="/servicios/automatizacion-y-datos/lectura-automatica-de-documentos-hacia-tu-programa">lectura automática de documentos hacia tu programa</a>. En el <a href="/contacto#diagnostico">diagnóstico gratuito</a> vemos cuál de las dos fases se te atasca; lo que el agente no hará en ningún caso es decidir cómo se contabiliza o se presenta nada.</p>
</div></section>""",
 "faq": [
  ("¿Cómo automatizar la recogida de documentación de los clientes de una asesoría?", "Definiendo primero qué documentos se esperan de cada cliente en cada periodo y por qué canal deben llegar. Con esa lista, un agente de IA clasifica lo que entra, detecta lo que falta y envía los recordatorios; el técnico revisa el expediente y decide."),
  ("¿Qué pasa si el agente clasifica mal una factura o la asigna a otro cliente?", "Puede ocurrir, sobre todo con fotos malas o documentos sin datos claros. Por eso lo que no reconoce con seguridad queda marcado para revisión, cada documento conserva su origen y el técnico puede corregir la clasificación antes de usar los datos."),
  ("¿Tienen que cambiar mis clientes su forma de enviar los papeles?", "Poco. Pueden seguir usando correo o WhatsApp, pero conviene indicarles la dirección o el número del despacho al que deben enviar y dejar de usar teléfonos personales, para que nada quede fuera del archivo."),
 ],
}

# Estructura: cronología de un contacto de portal un sábado (tabla por horas) + lo que sigue siendo del comercial
D["servicios/agentes-de-ia/agente-inmobiliario"] = {
 "estructura": "cronologia-de-un-sabado-en-tabla + reparto-agente-comercial",
 "lead": "Quien pregunta por un piso en un portal ha escrito a otras tres agencias a la vez, y suele quedarse con la primera que le contesta algo útil. Si tus comerciales están enseñando viviendas, ese contacto espera. Un agente de IA inmobiliario lo atiende en el momento y te lo deja calificado.",
 "bloque": """<section class="sec"><div class="w">
<p class="kicker">Sábado por la mañana, tres visitas seguidas</p>
<h2>¿Cuántos contactos de portales se te enfrían antes de que nadie los llame?</h2>
<p style="max-width:820px">Más de los que parece, porque los interesados escriben justo cuando la oficina no puede atender: por la noche, en fin de semana o mientras el equipo está en la calle. Sigue un contacto cualquiera, hora a hora.</p>
<blockquote style="max-width:820px"><p>«Hola, he visto el piso de tres habitaciones con terraza. ¿Sigue disponible? ¿Se podría ver este fin de semana?»</p></blockquote>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Hora</th><th>Lo que suele pasar</th><th>Con un agente inmobiliario con IA</th></tr></thead><tbody>
<tr><td>10:12</td><td>Entra un correo del portal: «¿sigue disponible?». Nadie lo ve</td><td>Responde por el canal que dejó el interesado y confirma disponibilidad con tu cartera</td></tr>
<tr><td>10:20</td><td>El interesado escribe a otra agencia</td><td>Pregunta zona, presupuesto, si necesita hipoteca y para cuándo</td></tr>
<tr><td>13:30</td><td>El comercial ve el aviso entre otros quince</td><td>Hay una ficha de demanda creada y una visita propuesta en un hueco real</td></tr>
<tr><td>Lunes</td><td>Se devuelve la llamada; no lo cogen</td><td>El comercial llama sabiendo qué busca y qué otros inmuebles le encajan</td></tr>
</tbody></table></div>
<h3 style="margin-top:30px">Lo que sigue en manos del comercial</h3>
<ul class="lista" style="max-width:820px">
<li><strong>Valorar una vivienda y captar al propietario.</strong> Eso se hace mirando el piso y a la persona.</li>
<li><strong>Negociar.</strong> Cualquier oferta llega al comercial con el contexto; el agente no sube ni baja un precio.</li>
<li><strong>Opinar sobre hipotecas, impuestos o contratos.</strong> Recoge la duda y la pasa; no aconseja.</li>
<li><strong>Decidir a quién no se enseña.</strong> La calificación es una ayuda para ordenar la agenda, no un filtro automático de personas.</li>
</ul>
<h3 style="margin-top:30px">Dos avisos antes de activarlo</h3>
<p style="max-width:820px">Si tu cartera no está al día, el agente contestará con datos viejos: antes de activarlo se revisa de dónde lee precios y disponibilidad. Y si te entran pocos contactos al mes, quizá te renta más ordenar el seguimiento con un <a href="/servicios/software-de-gestion/embudo-de-ventas-y-oportunidades">embudo de ventas y oportunidades</a> o empezar solo por el canal de chat con el <a href="/servicios/whatsapp-ia/asistente-de-ia-para-whatsapp">asistente de IA para WhatsApp</a>. Hay más situaciones del sector en la <a href="/guias/software-a-medida-para-inmobiliarias">guía de software para inmobiliarias</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo responder rápido a los leads de los portales inmobiliarios sin contratar a más gente?", "Con un agente de IA que recoja los avisos del portal en tu correo o tu CRM, conteste al interesado con los datos del inmueble y le haga las preguntas de calificación. Tu equipo recibe la ficha hecha y dedica el tiempo a las visitas y a cerrar."),
  ("¿Qué pasa si el agente da un dato equivocado de un piso?", "El agente responde con lo que hay en tu cartera, así que el riesgo real es tener datos desactualizados. Se limita a los campos que tú autorizas, avisa cuando no encuentra un dato en lugar de suponerlo y las conversaciones quedan registradas para corregir a tiempo."),
 ],
}

# Estructura: preguntas de autodiagnóstico numeradas + tres perfiles de negocio en tarjetas + cierre con límites
D["servicios/agentes-de-ia/agentes-que-gestionan-pedidos-presupuestos-o-incidencias-de-principio-"] = {
 "estructura": "test-de-autodiagnostico + tarjetas-por-tipo-de-negocio + parrafo-de-limites",
 "lead": "Un pedido entra por WhatsApp, alguien lo copia al programa, otro mira si hay stock, un tercero confirma la fecha y el cliente llama dos veces para saber cómo va. Los agentes de IA que gestionan pedidos, presupuestos e incidencias hacen ese recorrido completo y te consultan solo las decisiones.",
 "bloque": """<section class="sec sec-suave"><div class="w">
<div class="cab"><p class="kicker">Cinco preguntas, dos minutos</p><h2>¿Tu equipo gestiona el trabajo o se dedica a pasarlo de un sitio a otro?</h2><p class="lead" style="margin-top:8px">Contesta pensando en la semana pasada, no en cómo debería funcionar.</p></div>
<ol style="max-width:820px">
<li>¿Un mismo pedido se escribe más de una vez (en el chat, en una libreta, en el programa)?</li>
<li>¿Cuando un cliente pregunta «cómo va lo mío», alguien tiene que levantarse a preguntar?</li>
<li>¿Hay incidencias que se quedan en el móvil de quien las recibió?</li>
<li>¿Los presupuestos salen cuando hay un rato, y no cuando se piden?</li>
<li>¿Si falta la persona que «lo lleva», el proceso se para?</li>
</ol>
<p style="max-width:820px">Con tres síes, el problema no es de personas: es que el proceso vive repartido entre conversaciones y memoria. Ahí es donde un agente que ejecuta pasos, y no solo conversa, tiene sentido.</p>
<h3 style="margin-top:30px">Por dónde empieza cada tipo de negocio</h3>
<div class="rejilla">
<div class="tarjeta"><h3>Distribuidora o mayorista</h3><p>Por los pedidos repetitivos de clientes habituales: mismo catálogo, mismas condiciones, hora de corte clara.</p></div>
<div class="tarjeta"><h3>Instaladora o servicio técnico</h3><p>Por las incidencias: recoger fotos, comprobar si está en garantía y asignar el aviso sin tres llamadas.</p></div>
<div class="tarjeta"><h3>Taller, imprenta o fabricación corta</h3><p>Por los presupuestos sencillos, que son los que más se retrasan y menos margen dejan si se hacen a mano.</p></div>
</div>
<p style="max-width:820px;margin-top:20px">Lo que conviene saber antes de ilusionarse: un agente solo puede ser tan fiable como los datos que consulta. Si el stock del programa no coincide con el almacén, confirmará fechas que no son. Por eso se empieza con un único proceso, con permisos cortos y con todo lo que toca dinero pendiente de tu visto bueno; se amplía cuando los casos reales demuestran que acierta. Cómo se encadenan los pasos está explicado en los <a href="/servicios/pix/flujos-de-trabajo">flujos de trabajo de PIX</a>, y si aún no tienes un programa donde registrar pedidos, lo primero es un <a href="/servicios/software-de-gestion">software de gestión</a>. El <a href="/contacto#diagnostico">diagnóstico</a> es gratuito y sirve para elegir ese primer proceso.</p>
</div></section>""",
 "faq": [
  ("¿Cómo sé si un proceso de mi empresa se puede dejar en manos de un agente de IA?", "Se puede cuando se repite muchas veces, sigue reglas que alguien sabe explicar y los datos necesarios están en un programa al que el agente puede acceder. Si cada caso es distinto o depende de la intuición de una persona, el agente solo debería preparar el trabajo."),
  ("¿Qué pasa si el agente se equivoca al crear un pedido?", "Cada acción queda registrada con la conversación que la originó, de modo que se puede localizar y corregir. Para reducir el riesgo se limita lo que puede hacer solo, se le obliga a preguntar cuando duda y los primeros días se revisan todos los pedidos que crea."),
  ("¿Cuánto tarda en estar funcionando un agente que lleva un proceso completo?", "Lo habitual es un piloto de unas cuatro semanas sobre un solo proceso. El plazo depende sobre todo de lo fácil que sea conectar con tu programa y de que haya una persona en tu equipo que conozca bien las excepciones."),
 ],
}

# Estructura: errores del alta a mano en lista de definiciones + datos que no debe pedir + arranque por un solo canal
D["servicios/agentes-de-ia/alta-automatica-de-clientes-y-pacientes"] = {
 "estructura": "errores-del-alta-a-mano-en-definiciones + minimizacion-de-datos + arranque-por-un-canal",
 "lead": "Hay cola en el mostrador, suena el teléfono y la persona nueva está rellenando a boli una ficha que luego alguien tendrá que descifrar y teclear. El alta automática de clientes y pacientes recoge esos datos antes de la visita, por web o WhatsApp, y deja la ficha creada en tu programa.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Lo que cuesta una ficha mal hecha</p><h2>¿Cuánto tiempo pierde recepción dando de alta a mano?</h2></div>
<p style="max-width:820px">Pierde el rato de copiar y, sobre todo, el de arreglar después lo que se copió mal. El alta manual de un cliente, un socio o un paciente falla casi siempre por los mismos sitios:</p>
<dl style="max-width:820px">
<dt><strong>El teléfono con un número bailado</strong></dt><dd>El recordatorio de la cita no llega y la primera visita se convierte en una ausencia.</dd>
<dt><strong>La ficha duplicada</strong></dt><dd>«María García» y «Mª García López» son la misma persona con dos historiales a medias.</dd>
<dt><strong>El consentimiento en una carpeta</strong></dt><dd>El papel firmado existe, pero el día que hace falta nadie sabe en qué archivador está.</dd>
<dt><strong>El documento que «ya traeré»</strong></dt><dd>Sin nadie que lo recuerde, el expediente se queda incompleto durante meses.</dd>
<dt><strong>El correo ilegible</strong></dt><dd>La factura rebota y hay que llamar para pedir de nuevo un dato que ya se dio.</dd>
</dl>
<h3 style="margin-top:30px">Pedir menos datos también es parte del trabajo</h3>
<p style="max-width:820px">Un formulario de alta largo espanta, y además obliga a custodiar información que quizá no necesitas. Antes de automatizar repasamos contigo qué campos son imprescindibles para prestar el servicio y cuáles se han ido acumulando por costumbre. En una clínica o un centro de fisioterapia, el asistente se queda en lo administrativo: no pregunta por síntomas más allá del motivo de la visita ni interpreta informes. Si alguien escribe algo clínico, lo deriva al personal autorizado.</p>
<h3 style="margin-top:30px">Empieza por un solo canal</h3>
<p style="max-width:820px">Lo sensato es arrancar donde más altas entran, comparar durante unas semanas con el método de siempre y mantener el papel para quien no se maneja con el móvil: una persona mayor o alguien sin correo no debería quedarse fuera. Si el alta desemboca en una reserva, encaja con la <a href="/servicios/software-de-gestion/agenda-y-citas-online">agenda y citas online</a>; si después quieres ver todo lo de cada persona en una pantalla, es la <a href="/servicios/software-de-gestion/ficha-de-cliente-360">ficha de cliente 360</a>. Para documentos que requieren firma, mira los <a href="/servicios/software-de-gestion/contratos-con-firma-online">contratos con firma online</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo dar de alta a un cliente nuevo sin que tenga que rellenar papeles en el mostrador?", "Enviándole antes de la visita un enlace o un mensaje de WhatsApp donde un asistente le pide los datos, los comprueba y recoge los documentos y la aceptación de protección de datos. Cuando llega, su ficha ya está creada y recepción solo confirma."),
  ("¿Qué pasa con las personas mayores o que no usan el móvil?", "Se mantiene el alta presencial. Recepción puede completar la ficha con la persona delante usando el mismo proceso guiado, de forma que los datos se validan igual y nadie queda excluido por no manejar la tecnología."),
 ],
}

# Estructura: frases que se oyen en la oficina (cita) + síntomas + lo que no hace + primeras dos semanas
D["servicios/agentes-de-ia/asistente-interno-de-procedimientos"] = {
 "estructura": "cita-de-oficina + lista-de-sintomas + plan-de-dos-semanas",
 "lead": "En casi todas las empresas hay una persona a la que todo el mundo pregunta cómo se hace cada cosa. Cuando está de vacaciones, el trabajo se frena; cuando está, no la dejan trabajar. Un asistente de IA interno para procedimientos contesta esas dudas con vuestros propios manuales y cita de dónde sale cada respuesta.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">La empresa que cabe en una cabeza</p><h2>¿Qué pasa el día que no está quien sabe cómo se hace todo?</h2></div>
<blockquote style="max-width:820px"><p>«Eso pregúntaselo a Mari Carmen, que es la que lo lleva.» · «Yo lo hago así porque me lo enseñó el anterior.» · «Hay un documento, pero no sé si es la última versión.»</p></blockquote>
<p style="max-width:820px">Lo que pasa es que cada uno improvisa, y lo improvisado se queda como costumbre. No es culpa de nadie: el conocimiento de un negocio se va acumulando en personas, correos y carpetas que solo entiende quien las creó.</p>
<h3 style="margin-top:28px">Síntomas de que dependes demasiado de la memoria de alguien</h3>
<ul class="lista" style="max-width:820px">
<li>La misma tarea se hace de dos formas según quién esté de turno.</li>
<li>A la persona veterana la interrumpen tantas veces que termina su trabajo fuera de horario.</li>
<li>Los errores se repiten en cada incorporación, siempre en el mismo paso.</li>
<li>Existe un manual, pero nadie lo abre porque buscar en él cuesta más que preguntar.</li>
</ul>
<h3 style="margin-top:28px">Las dos primeras semanas</h3>
<ol style="max-width:820px">
<li><strong>Días 1 a 3.</strong> Se anotan las preguntas que más se repiten en un departamento. Suelen ser menos de lo que se cree.</li>
<li><strong>Días 4 a 8.</strong> Se reúnen o se escriben los documentos que las responden y alguien con autoridad les da el visto bueno.</li>
<li><strong>Días 9 a 14.</strong> Un grupo pequeño lo usa y marca cada respuesta floja. Lo que no supo contestar indica qué falta por escribir.</li>
</ol>
<p style="max-width:820px">Un asistente así no inventa procedimientos, no decide excepciones y no sustituye a la formación práctica en tareas delicadas: si el documento está mal, la respuesta saldrá mal, con cita incluida. Por eso cada procedimiento necesita un responsable con nombre. Si lo que buscas es dejar por escrito y en vídeo cómo se trabaja antes de un relevo, mira el <a href="/servicios/relevo-y-continuidad/manual-de-operaciones-con-video-e-ia">manual de operaciones con vídeo e IA</a>; si el problema está en las incorporaciones, el <a href="/servicios/formacion-ia/plan-de-formacion-para-nuevos-empleados">plan de formación para nuevos empleados</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo evitar que el conocimiento de la empresa dependa de una sola persona?", "Pasando a documentos revisados lo que esa persona sabe y poniendo esos documentos al alcance del equipo de una forma fácil de consultar. Un asistente interno ayuda en lo segundo: responde en lenguaje normal y enseña de qué procedimiento ha sacado la respuesta."),
  ("¿Qué pasa si el asistente responde con un procedimiento que está mal escrito?", "Repetirá el error, porque no juzga si el documento es correcto. Por eso cada respuesta indica su origen, cualquier persona puede marcarla como dudosa y cada procedimiento tiene un responsable que lo corrige."),
  ("¿Cuántos documentos hacen falta para que el asistente interno sea útil?", "No hacen falta muchos. Con los procedimientos que responden a las preguntas más repetidas de un departamento ya se nota; el resto se va añadiendo a partir de las consultas que se quedan sin respuesta."),
 ],
}

# Estructura: mito / realidad en tabla + cuándo no hace falta + qué preparar
D["servicios/agentes-de-ia/chatbot-para-tu-web-con-pix"] = {
 "estructura": "tabla-mito-realidad + cuando-no-hace-falta + que-preparar",
 "lead": "La gente entra en tu web con una duda concreta, no encuentra la respuesta en diez segundos y se marcha sin rellenar el formulario. Nunca sabrás que estuvo. Un chatbot con IA para tu web le responde al instante con lo que sabe tu empresa y te pasa su contacto.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Antes de poner una burbuja de chat</p><h2>¿Sirve de algo un chatbot en la web de un negocio pequeño?</h2></div>
<p style="max-width:820px">Sirve cuando tus visitas tienen preguntas que la web no resuelve de un vistazo y tú no puedes atender un chat en directo. Si has probado alguno y te pareció un estorbo, casi seguro era de los antiguos. Conviene separar lo que se cuenta de lo que pasa.</p>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Lo que se suele pensar</th><th>Lo que ocurre de verdad</th></tr></thead><tbody>
<tr><td>«Los chatbots desesperan a la gente»</td><td>Desesperan los de botones, que no entienden nada fuera del menú. Uno con IA lee la pregunta tal como se escribe</td></tr>
<tr><td>«Se inventará precios»</td><td>Puede pasar si se le deja improvisar. Se configura para contestar solo con lo que le has dado y decir «no lo sé» en lo demás</td></tr>
<tr><td>«Con ponerlo ya vendo más»</td><td>Un chat no arregla una web lenta o confusa. Ayuda a que la visita que ya tienes no se vaya con la duda</td></tr>
<tr><td>«Me quitará el trato personal»</td><td>Filtra lo repetido y te pasa, con resumen, lo que merece una llamada tuya</td></tr>
<tr><td>«Es instalar y olvidarse»</td><td>Hay que revisar conversaciones y actualizar tarifas y horarios cuando cambian</td></tr>
</tbody></table></div>
<h3 style="margin-top:30px">Casos en los que una burbuja de chat sobra</h3>
<p style="max-width:820px">Con pocas visitas al mes, una página de preguntas frecuentes bien escrita y un botón de WhatsApp te darán casi lo mismo por menos. Tampoco compensa si tus clientes siempre llaman. Y si el problema es que la web no convierte, primero toca una <a href="/servicios/webs/auditoria-de-conversion">auditoría de conversión</a>.</p>
<h3 style="margin-top:30px">Qué preparar para que conteste bien</h3>
<p style="max-width:820px">Lo que más mejora un asistente virtual para la web no es la tecnología, sino tener por escrito lo que hoy solo sabes tú:</p>
<ul class="lista" style="max-width:820px">
<li>Tarifas o, al menos, rangos de precio.</li>
<li>Zonas donde trabajas, plazos y condiciones.</li>
<li>Las quince preguntas que más te hacen, con tu respuesta.</li>
</ul>
<p style="max-width:820px">Con eso sale una primera versión que después se afina con conversaciones reales. Antes de pedir el teléfono o el correo, el chat explica para qué los recoge y solicita el consentimiento. Cómo se integra en el diseño está en <a href="/servicios/webs/chatbot-pix">chatbot PIX para páginas web</a>; si tus clientes prefieren escribir al móvil, el mismo conocimiento sirve para el <a href="/servicios/whatsapp-ia/asistente-de-ia-para-whatsapp">asistente de IA para WhatsApp</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo sé si mi web necesita un chatbot o basta con un formulario?", "Mira cuántas visitas tienes y cuántas te escriben. Si entra gente pero casi nadie contacta, y las dudas que te llegan por teléfono se repiten, un chatbot con IA puede recoger a quienes hoy se van. Con muy poco tráfico, un formulario claro y un botón de WhatsApp suelen bastar."),
  ("¿Qué pasa si alguien intenta que el chatbot diga algo inapropiado o fuera de tema?", "Se configura para ceñirse a los temas de tu negocio y rechazar con educación lo demás. No es infalible, por eso las conversaciones quedan registradas y se revisan muestras periódicas para ajustar las instrucciones."),
 ],
}

# Estructura: cuenta con tus propios números + tabla qué sale solo / qué espera a una persona
D["servicios/agentes-de-ia/clasificacion-y-respuesta-de-correos"] = {
 "estructura": "cuenta-de-la-bandeja + tabla-autonomia-por-tipo-de-correo",
 "lead": "Abres el correo a las ocho con cuarenta mensajes nuevos y a las diez sigues decidiendo cuál es urgente, cuál es de un cliente y cuál es publicidad. Mientras, un pedido espera en la bandeja de info@ sin dueño. Clasificar y responder correos con IA te entrega cada mensaje ya etiquetado, asignado y con un borrador.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Haz la prueba con la bandeja de ayer</p><h2>¿Cuántas horas a la semana se van solo en leer y repartir correos?</h2></div>
<p style="max-width:820px">Se van más de las que nadie apunta, porque es un trabajo invisible. Para saberlo en tu caso no hace falta ninguna herramienta:</p>
<ol style="max-width:820px">
<li>Cuenta los correos que entraron ayer en los buzones compartidos (info@, pedidos@, administración@).</li>
<li>Separa los que eran para otra persona y hubo que reenviar.</li>
<li>Anota cuántas respuestas fueron prácticamente iguales a otras que ya has escrito cien veces.</li>
<li>Busca alguno que siga sin contestar porque «creía que lo llevabas tú».</li>
</ol>
<p style="max-width:820px">El segundo y el tercer número son lo que un agente de correo quita de en medio. El cuarto es el que cuesta clientes.</p>
<h3 style="margin-top:30px">Qué puede salir solo y qué conviene que espere</h3>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Tipo de correo</th><th>Tratamiento razonable</th><th>Por qué</th></tr></thead><tbody>
<tr><td>Consulta de horario, dirección o documentación necesaria</td><td>Respuesta automática</td><td>La contestación es siempre la misma y está escrita</td></tr>
<tr><td>Pedido de un cliente habitual</td><td>Acuse automático y aviso a ventas</td><td>El cliente sabe que ha llegado; alguien confirma condiciones</td></tr>
<tr><td>Factura de proveedor</td><td>Se archiva y se pasa a administración</td><td>No requiere respuesta, sí registro</td></tr>
<tr><td>Reclamación o queja</td><td>Borrador para revisar</td><td>El tono y lo que se ofrece son decisión de una persona</td></tr>
<tr><td>Correo con asunto legal o de un organismo</td><td>Solo se etiqueta como prioritario</td><td>No debería contestarlo ninguna automatización</td></tr>
</tbody></table></div>
<p style="max-width:820px;margin-top:20px">Dos límites que conviene conocer. Un borrador redactado por IA puede sonar seguro y estar equivocado en un dato, así que durante las primeras semanas lo normal es no enviar nada sin leerlo. Y un correo mal clasificado es peor que uno sin clasificar si nadie lo vigila: por eso existe una bandeja de dudas y se revisa a diario. Qué buzones se pueden conectar lo tienes en las <a href="/servicios/pix/integraciones">integraciones de PIX con Gmail y Outlook</a>. Si lo que te desborda son las facturas que llegan adjuntas, mira la <a href="/servicios/software-de-gestion/lectura-automatica-de-facturas-de-proveedores">lectura automática de facturas de proveedores</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo organizar un buzón compartido para que ningún correo se quede sin contestar?", "Haciendo que cada mensaje tenga un responsable desde que entra. Un agente de IA lo clasifica, lo asigna a una persona según tus reglas y avisa si pasa un tiempo sin respuesta, de modo que deja de depender de quién abrió antes la bandeja."),
  ("¿Qué pasa si la IA clasifica un correo importante como publicidad?", "Puede ocurrir alguna vez. Para reducirlo, los remitentes que son clientes o proveedores conocidos no se descartan nunca de forma automática, lo dudoso va a una bandeja de revisión y nada se borra: solo se etiqueta."),
  ("¿Cuánto tarda el agente de correo en aprender cómo responde mi empresa?", "Con una muestra de respuestas ya enviadas y las reglas de reparto por escrito se puede empezar en pocos días. Después mejora con las correcciones que hace tu equipo sobre los borradores durante las primeras semanas."),
 ],
}

# Estructura: frases del dueño + por qué se retrasa el cobro + comparación de alternativas en tabla + lo que no hace
D["servicios/agentes-de-ia/cobros-e-impagos"] = {
 "estructura": "frases-del-dueno + tabla-comparativa-de-alternativas + limites-del-recobro",
 "lead": "Reclamar una factura a un cliente con el que te llevas bien da apuro, así que lo dejas para el viernes, y el viernes para el mes que viene. Mientras, pagas tú a tus proveedores. Un agente de IA para reclamar cobros e impagos insiste con educación, entiende lo que le contestan y te pasa lo que requiere una llamada.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">El trabajo que nadie quiere hacer</p><h2>¿Por qué se te acumulan facturas vencidas si tus clientes no son malos pagadores?</h2></div>
<ul class="lista" style="font-size:18px;max-width:820px">
<li>«Me sabe mal llamarle otra vez, lleva años con nosotros.»</li>
<li>«Me dijo que pagaba el viernes. No recuerdo de qué semana.»</li>
<li>«No sé cuánto me deben en total hasta que hago la lista a mano.»</li>
<li>«Cuando por fin reclamo, me dice que la factura estaba mal y que nadie le contestó.»</li>
</ul>
<p style="max-width:820px;margin-top:18px">Se acumulan porque reclamar exige constancia y nadie tiene esa tarea como la primera de su día. La mayoría de los retrasos no son impagos de verdad: son olvidos, facturas que no llegaron a quien paga o desacuerdos pequeños que nadie resolvió.</p>
<h3 style="margin-top:28px">Cuatro maneras de reclamar, comparadas</h3>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Opción</th><th>Lo bueno</th><th>Dónde falla</th></tr></thead><tbody>
<tr><td>Llamar tú cuando te acuerdas</td><td>Trato personal</td><td>Irregular; depende de tu tiempo y de tu ánimo</td></tr>
<tr><td>Recordatorio automático del programa</td><td>Sale siempre en fecha</td><td>No lee la respuesta: sigue reclamando aunque te hayan contestado</td></tr>
<tr><td>Agente de IA de cobros</td><td>Constante y atento a lo que dice cada cliente</td><td>Necesita que las facturas y los cobros estén al día en tu programa</td></tr>
<tr><td>Empresa de recobro o abogado</td><td>Para deuda antigua o conflictiva</td><td>Llega tarde y tensa la relación; es otro servicio</td></tr>
</tbody></table></div>
<h3 style="margin-top:28px">Hasta dónde llega y dónde se detiene</h3>
<p style="max-width:820px">El agente se ocupa de la gestión amistosa: recordar, anotar, pedir justificantes y avisar. Fuera de eso:</p>
<ul class="lista" style="max-width:820px">
<li>No amenaza ni usa un tono que tú no usarías.</li>
<li>No negocia quitas ni condiciones que no hayas escrito.</li>
<li>No inicia reclamaciones judiciales ni te asesora sobre intereses de demora; eso corresponde a tu asesoría o a un abogado.</li>
</ul>
<p style="max-width:820px">Tampoco arregla un problema de origen: si el cliente no paga porque el trabajo quedó a medias, lo correcto es que alguien le llame.</p>
<p style="max-width:820px">Para ver de un vistazo qué clientes se retrasan, el complemento natural es el <a href="/servicios/software-de-gestion/cobros-impagos-y-semaforo-de-clientes">semáforo de cobros e impagos</a>, y para saber cómo afecta a tu caja, la <a href="/servicios/automatizacion-y-datos/prevision-de-tesoreria-y-control-de-costes">previsión de tesorería</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo insistir en un pago pendiente sin resultar agresivo con un cliente de muchos años?", "Con mensajes breves, educados y puntuales, que faciliten pagar y permitan contestar. Un agente de IA mantiene ese tono en cada recordatorio, detiene la reclamación si el cliente plantea un desacuerdo y te pasa el caso cuando hace falta una conversación personal."),
  ("¿Qué pasa si el cliente contesta algo que el agente no entiende?", "No insiste a ciegas. Marca la respuesta como pendiente de revisión, pausa los recordatorios de esa factura y avisa a la persona responsable con el hilo completo."),
  ("¿A partir de cuántas facturas al mes compensa automatizar la reclamación de cobros?", "Depende menos del número que del tiempo que hoy dedicas y de lo que tardas en cobrar. Si alguien pasa varias horas a la semana persiguiendo pagos, o si directamente no se reclama por falta de tiempo, suele compensar."),
 ],
}

# Estructura: cuatro alternativas en tarjetas + señales de que te hace falta + cuándo no
D["servicios/agentes-de-ia/departamento-de-ia-externalizado"] = {
 "estructura": "tarjetas-de-alternativas + senales + cuando-no",
 "lead": "Has visto demostraciones, tienes tres propuestas en el correo y media plantilla usa ya asistentes por su cuenta, pero nadie en la empresa tiene tiempo ni conocimientos para decidir por dónde empezar. Un departamento de IA externalizado para pymes pone a alguien al mando de ese tema sin contratar un perfil que no sabrías ni entrevistar.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">La IA sin dueño</p><h2>¿Quién se ocupa de la inteligencia artificial en una empresa que no tiene informático?</h2><p class="lead" style="margin-top:8px">Hoy, normalmente, nadie. O todos un poco, que viene a ser lo mismo.</p></div>
<div class="rejilla">
<div class="tarjeta"><h3>Encargárselo «al que sabe de ordenadores»</h3><p>Barato y rápido. Pero lo hará a ratos, sin método, y el día que se vaya nadie sabrá qué montó.</p></div>
<div class="tarjeta"><h3>Contratar a un especialista</h3><p>Tiene sentido con mucho volumen. En una pyme es difícil de seleccionar, caro de mantener y una sola persona no cubre estrategia, técnica y formación.</p></div>
<div class="tarjeta"><h3>Pedir un informe a una consultora</h3><p>Te ordena las ideas. El riesgo es quedarte con un documento que nadie ejecuta.</p></div>
<div class="tarjeta"><h3>Comprar herramientas sueltas</h3><p>Cada departamento paga la suya, no se hablan entre sí y nadie mira qué datos se meten en ellas.</p></div>
</div>
<p style="max-width:820px;margin-top:20px">Un equipo de IA externo cubre el hueco entre esas opciones: decide contigo, monta, enseña y sigue ahí cuando algo deja de funcionar.</p>
<h3 style="margin-top:28px">Señales de que te hace falta alguien al mando</h3>
<ul class="lista" style="max-width:820px">
<li>Pagas varias suscripciones de IA y no sabrías decir qué se hace con cada una.</li>
<li>Hubo una prueba que funcionó y se quedó en prueba.</li>
<li>Cada proveedor te recomienda justo lo que vende.</li>
<li>Te preocupa qué información de clientes está saliendo de la empresa.</li>
</ul>
<h3 style="margin-top:28px">Cuándo es demasiado para ti</h3>
<p style="max-width:820px">Si trabajas solo o sois tres, un servicio continuo te viene grande: empieza por una <a href="/servicios/formacion-ia/sesion-de-ia-1-a-1">sesión de IA 1 a 1</a> o por un único agente. Si lo que quieres es una foto de dónde aplicar la IA antes de comprometerte, encaja mejor una <a href="/servicios/consultoria-y-ayudas/auditoria-de-ia-para-pymes">auditoría de IA para pymes</a>. Y si ya tienes agentes montados y solo necesitas que no se rompan, basta el <a href="/servicios/agentes-de-ia/mantenimiento-de-agentes-y-automatizaciones">mantenimiento de agentes y automatizaciones</a>. Tampoco funciona si dirección no dedica un rato al mes: externalizar la ejecución es posible, externalizar las decisiones no.</p>
</div></section>""",
 "faq": [
  ("¿Cómo empezar con la IA en una pyme sin contratar a un experto?", "Eligiendo un proceso que se repita mucho, midiendo cuánto tiempo consume hoy y automatizándolo como prueba con un equipo externo. Si el resultado convence, ese mismo equipo puede encargarse de los siguientes procesos, de la formación y del mantenimiento."),
  ("¿Qué pasa con lo que se ha montado si dejo el servicio de IA externalizado?", "Los agentes, las automatizaciones y su documentación son de tu empresa. Conviene dejarlo por escrito desde el principio: qué se entrega, con qué accesos y cómo se traspasa a otro proveedor o a alguien de tu plantilla."),
 ],
}

# Estructura: escena de un martes + tabla de tres niveles de sensibilidad | segunda sección: preguntas para cualquier proveedor
D["servicios/agentes-de-ia/ia-con-los-datos-de-tu-empresa-sin-que-salgan-fuera"] = {
 "estructura": "escena-del-excel-pegado + tabla-niveles-de-sensibilidad + preguntas-al-proveedor-en-segunda-seccion",
 "lead": "Alguien de tu equipo tenía prisa, pegó la lista de clientes en un chat gratuito para que se la ordenase y siguió trabajando. No lo hizo con mala intención, y tú no lo sabes. Una IA privada con los datos de tu empresa bajo control existe para que eso deje de ser la opción más cómoda.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Lo que ya está pasando</p><h2>¿Sabes qué información de tu empresa se ha pegado esta semana en un chat de IA?</h2></div>
<p style="max-width:820px">Lo más probable es que no, y no por descuido tuyo: nadie pide permiso para ahorrarse una hora. Imagina un martes cualquiera. Administración pega un extracto para cuadrarlo, un comercial sube un contrato para que se lo resuman y alguien de recursos humanos pide ayuda para redactar una carta con nombre y apellidos. Tres personas resolviendo su trabajo, tres copias de datos en cuentas personales que la empresa no ve.</p>
<p style="max-width:820px">Prohibirlo sin dar alternativa rara vez funciona; la gente lo sigue haciendo desde el móvil. Lo que funciona es ofrecer algo igual de cómodo dentro de un entorno que sí controlas.</p>
<h3 style="margin-top:28px">No todos los datos merecen el mismo cuidado</h3>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Tipo de información</th><th>Ejemplos</th><th>Criterio razonable</th></tr></thead><tbody>
<tr><td>Pública o inocua</td><td>Textos de la web, catálogo, un correo sin datos de nadie</td><td>Se puede trabajar con cualquier asistente autorizado por la empresa</td></tr>
<tr><td>Interna</td><td>Tarifas de compra, procedimientos, informes de ventas</td><td>Solo en el entorno de empresa, con permisos por puesto</td></tr>
<tr><td>Sensible</td><td>Datos de salud, nóminas, expedientes, contratos confidenciales</td><td>Acceso muy restringido, revisión previa con quien lleve tu protección de datos, o fuera de la IA</td></tr>
</tbody></table></div>
</div></section>
<section class="sec sec-suave"><div class="w">
<h3>Qué preguntar a cualquier proveedor de IA, incluidos nosotros</h3>
<ol style="max-width:820px">
<li>¿Dónde se procesan y se guardan mis datos, y consta por contrato?</li>
<li>¿Se usan mis conversaciones para entrenar modelos de terceros?</li>
<li>¿Puedo limitar el acceso por persona y ver quién consultó qué?</li>
<li>¿Qué ocurre con la información si cancelo el servicio?</li>
<li>¿Quién de vuestro equipo puede ver mis datos y para qué?</li>
</ol>
<p style="max-width:820px">En nuestro caso la respuesta a la primera pregunta es corta: los datos los tienes tú, en tu propio servidor. La IA trabaja sobre ellos ahí y no se copian a máquinas nuestras, de modo que «sin que salgan fuera» describe dónde están, no una promesa de confianza. Cómo se monta ese equipo lo explicamos en <a href="/servicios/agentes-de-ia/ia-en-servidor-propio">IA en servidor propio o dedicado</a>. Aun así, ninguna tecnología te exime de tus obligaciones de protección de datos, y nosotros no somos asesoría jurídica. Las normas para la plantilla se fijan con una <a href="/servicios/formacion-ia/politica-de-uso-de-ia-para-empresas">política de uso de IA</a> y los controles del producto están en <a href="/servicios/pix/seguridad-y-control">seguridad y control de PIX</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo evitar que los empleados peguen datos de clientes en ChatGPT?", "Combinando tres cosas: una norma interna clara sobre qué datos no pueden salir, formación con ejemplos de su propio puesto y una herramienta de empresa igual de cómoda que la gratuita. Solo con la prohibición, el uso suele continuar a escondidas."),
  ("¿Una IA privada se equivoca menos que un chat público?", "No necesariamente. Que sea privada afecta a dónde están los datos y quién los ve, no a que acierte siempre. Responde mejor porque consulta tu información real, pero lo que produce debe revisarlo una persona antes de usarlo en algo importante."),
 ],
}

# Estructura: petición literal de un cliente (cita) + lo que un servidor no resuelve + cómo empezar sin cerrarse puertas
D["servicios/agentes-de-ia/ia-en-servidor-propio"] = {
 "estructura": "cita-de-clausula-de-cliente + lista-de-lo-que-no-resuelve + arranque-reversible",
 "lead": "Un cliente grande te envía un cuestionario de proveedores: dónde se alojan sus datos, quién accede, si se comparten recursos con otras empresas. Hasta ahora nadie te lo había preguntado y no sabes qué contestar sobre tus herramientas de inteligencia artificial. La IA en servidor propio o dedicado es una de las respuestas posibles, no siempre la necesaria.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Cuando te lo exigen por escrito</p><h2>¿Tu cliente te pide saber dónde están sus datos y no sabes qué responder?</h2></div>
<blockquote style="max-width:820px"><p>«El proveedor declarará la ubicación de los sistemas donde se trate la información del cliente y si dichos sistemas son compartidos con terceros.»</p><p><small>Ejemplo hipotético de cláusula en un cuestionario de homologación.</small></p></blockquote>
<p style="max-width:820px">Lo primero es saber qué usas hoy, porque muchas empresas descubren en ese momento que su equipo trabaja con varias herramientas de IA que nadie ha inventariado. Lo segundo es decidir si la exigencia se cumple con un servicio en la nube bien contratado o si de verdad hace falta un entorno reservado. Ingenierías, despachos, laboratorios y proveedores de industria son quienes más reciben este tipo de peticiones.</p>
<h3 style="margin-top:28px">Lo que un servidor dedicado no arregla por sí solo</h3>
<ul class="lista" style="max-width:820px">
<li><strong>Permisos mal puestos.</strong> Si todo el mundo ve todo, da igual dónde esté la máquina.</li>
<li><strong>Empleados que siguen usando chats gratuitos.</strong> El entorno aislado no impide copiar y pegar en otra pestaña.</li>
<li><strong>La calidad de las respuestas.</strong> La IA no acierta más por estar en un servidor reservado.</li>
<li><strong>Tus obligaciones legales.</strong> Ayuda a cumplir compromisos con clientes; no equivale a cumplir ninguna norma de forma automática.</li>
<li><strong>Las copias de seguridad.</strong> Hay que planificarlas igual; mira el <a href="/servicios/ciberseguridad-y-sistemas/copias-de-seguridad-y-plan-de-continuidad">plan de copias y continuidad</a>.</li>
</ul>
<h3 style="margin-top:28px">Empezar sin hipotecarte</h3>
<p style="max-width:820px">Un despliegue dedicado cuesta más y pide más mantenimiento, así que montarlo «por si acaso» no suele tener sentido. Una vía prudente tiene tres pasos:</p>
<ol style="max-width:820px">
<li>Arrancar con un proceso y datos poco delicados en el plan estándar.</li>
<li>Documentar desde el primer día qué fuentes se conectan y quién accede.</li>
<li>Dejar previsto el traslado para cuando un contrato o un tipo de dato lo requiera.</li>
</ol>
<p style="max-width:820px">Qué controles existen en ambos casos lo explica <a href="/servicios/pix/seguridad-y-control">seguridad y control de PIX</a>, y los criterios para decidir qué información entra están en <a href="/servicios/agentes-de-ia/ia-con-los-datos-de-tu-empresa-sin-que-salgan-fuera">IA privada con los datos de tu empresa</a>. En la auditoría inicial te diremos con franqueza si lo necesitas o si te bastaría con menos.</p>
</div></section>""",
 "faq": [
  ("¿Cómo responder a un cliente que me exige saber dónde se alojan sus datos cuando uso IA?", "Con un inventario de las herramientas que tratan su información, la ubicación y condiciones de cada una según contrato, y los permisos de acceso internos. Si alguna no cumple lo que pide, se sustituye o se pasa ese trabajo a un entorno dedicado."),
  ("¿Cuánto tarda en montarse una IA en un servidor dedicado?", "Depende de los requisitos de seguridad, del número de programas que haya que conectar y de dónde estén esos programas. Se concreta tras la auditoría, y lo habitual es poner en marcha primero un proceso y ampliar después."),
  ("¿Qué pasa si el servidor dedicado se cae?", "Los flujos se detienen hasta que se recupera, como en cualquier sistema. Por eso el proyecto incluye vigilancia, copias y un procedimiento de recuperación acordado, y conviene decidir de antemano qué procesos necesitan un plan alternativo manual."),
 ],
}

# Estructura: tarde de viernes con un pliego + cuenta con tus números + para quién no compensa
D["servicios/agentes-de-ia/licitaciones-publicas"] = {
 "estructura": "escena-de-viernes + cuenta-de-horas-por-pliego + lista-de-no-compensa",
 "lead": "Te enteras de un concurso que te encajaba cuando faltan cuatro días para el cierre, o dedicas una tarde entera a leer un pliego para descubrir en la página sesenta que no cumples la solvencia. Un agente de IA para licitaciones públicas vigila las convocatorias y te resume cada una antes de que inviertas horas.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Contratación pública para empresas pequeñas</p><h2>¿Por qué tantas pymes dejan de presentarse a concursos que podrían ganar?</h2></div>
<p style="max-width:820px">Porque enterarse y decidir consume un tiempo que no tienen. En una constructora, una empresa de limpieza, una ingeniería o un proveedor de suministros, quien prepara las ofertas suele ser la misma persona que lleva obras, clientes o la administración. Leer boletines y plataformas cada mañana es lo primero que se abandona.</p>
<h3 style="margin-top:28px">Calcula lo que te cuesta decidir</h3>
<ol style="max-width:820px">
<li>Anota cuántas convocatorias miraste el último trimestre, aunque fuera por encima.</li>
<li>Apunta a cuántas te presentaste finalmente.</li>
<li>Estima las horas de lectura de las descartadas: pliego administrativo, técnico y anexos.</li>
<li>Recuerda alguna que viste tarde o que perdiste por un documento caducado.</li>
</ol>
<p style="max-width:820px">La diferencia entre el primer número y el segundo es tiempo dedicado a concursos que no eran para ti. Ese es el tramo que más se reduce: no la redacción de la oferta, sino el filtro previo.</p>
<h3 style="margin-top:28px">A quién no le compensa</h3>
<ul class="lista" style="max-width:820px">
<li>A quien se presenta a una o dos licitaciones al año, siempre del mismo organismo.</li>
<li>A quien no tiene todavía la documentación administrativa básica en orden; primero toca eso.</li>
<li>A quien espera que la IA escriba la oferta ganadora: la propuesta técnica y el precio dependen de tu conocimiento del trabajo.</li>
</ul>
<p style="max-width:820px">Un aviso importante: un resumen es una ayuda para decidir, no un sustituto del pliego. La IA puede pasar por alto un requisito escondido en un anexo o interpretar mal una cláusula ambigua, así que quien firma la oferta debe leer los apartados clave del documento original antes de presentarla. Tampoco prestamos asesoramiento jurídico sobre contratación ni tramitamos por ti. Si además buscas ayudas, tenemos un servicio aparte de <a href="/servicios/consultoria-y-ayudas/vigilancia-de-subvenciones">vigilancia de subvenciones</a>; y para tener a mano certificados y escrituras, sirve la <a href="/servicios/migraciones-e-integraciones/digitalizacion-de-archivo-en-papel">digitalización del archivo en papel</a>. El agente se apoya en los <a href="/servicios/pix/flujos-de-trabajo">flujos de trabajo de PIX</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo enterarme a tiempo de las licitaciones públicas de mi sector?", "Definiendo unos criterios fijos de búsqueda (actividad, zona, importe mínimo y máximo) y revisando cada día las publicaciones con ellos. Un agente de IA hace esa revisión por ti y te avisa solo de las que encajan, con un resumen para decidir."),
  ("¿Me puedo fiar del resumen que hace la IA de un pliego?", "Sirve para descartar rápido y para saber dónde mirar, pero no reemplaza la lectura de los apartados decisivos. El resumen indica de qué parte del pliego sale cada dato, de forma que tu equipo puede comprobarlo en el documento original antes de presentarse."),
 ],
}

# Estructura: fallo ruidoso frente a fallo silencioso (tabla) + qué pedir a quien te lo montó + cuándo no hace falta contrato
D["servicios/agentes-de-ia/mantenimiento-de-agentes-y-automatizaciones"] = {
 "estructura": "tabla-fallo-ruidoso-o-silencioso + que-exigir-a-quien-lo-monto + sin-contrato",
 "lead": "Te montaron una automatización hace un año, funcionó bien y dejaste de mirarla. Un día descubres que el formulario lleva semanas sin pasar contactos al programa, y quien la hizo ya no contesta. El mantenimiento de agentes de IA y automatizaciones sirve para enterarte el mismo día, no por un cliente enfadado.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Lo que no avisa es lo que más cuesta</p><h2>¿Cómo sabes hoy que tus automatizaciones siguen funcionando?</h2></div>
<p style="max-width:820px">Si la respuesta es «porque nadie se ha quejado», no lo sabes. Hay averías que se ven al momento y otras que pasan desapercibidas durante semanas; las segundas son las peligrosas.</p>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Avería</th><th>¿Se nota sola?</th><th>Quién suele descubrirla</th></tr></thead><tbody>
<tr><td>El chat de la web deja de cargar</td><td>Sí, enseguida</td><td>Tú o alguien del equipo</td></tr>
<tr><td>Los pedidos de la tienda no llegan al programa</td><td>A medias</td><td>Almacén, cuando un cliente reclama</td></tr>
<tr><td>El asistente sigue dando la tarifa del año pasado</td><td>No</td><td>Un cliente, al ver la factura</td></tr>
<tr><td>Un recordatorio deja de enviarse</td><td>No</td><td>Nadie; solo suben las ausencias</td></tr>
<tr><td>Las respuestas empeoran poco a poco</td><td>No</td><td>Nadie, hasta que alguien lee una conversación</td></tr>
</tbody></table></div>
<h3 style="margin-top:28px">Qué deberías tener de quien te lo montó</h3>
<ul class="lista" style="max-width:820px">
<li>Un esquema de cada flujo: qué lo dispara, qué programas toca y qué hace si falla un paso.</li>
<li>Las cuentas y credenciales a nombre de tu empresa, no del proveedor ni de un empleado.</li>
<li>Un aviso automático cuando algo no se ejecuta.</li>
<li>El nombre de la persona a la que llamar y un plazo de respuesta por escrito.</li>
</ul>
<p style="max-width:820px">Si te falta algo de esa lista, estás a un cambio de contraseña de quedarte sin servicio. Recuperar esa documentación es lo primero que hacemos al hacernos cargo de automatizaciones heredadas, estén hechas con PIX o con otras plataformas.</p>
<h3 style="margin-top:28px">Si solo tienes una automatización sencilla</h3>
<p style="max-width:820px">Una única automatización sencilla y poco crítica puede vigilarla alguien de tu equipo con una revisión semanal de cinco minutos; no hace falta un servicio para eso. El mantenimiento tampoco vuelve infalible a un agente: reduce el tiempo que un fallo pasa oculto, que es lo que de verdad hace daño. Si lo que quieres es que alguien decida además qué automatizar después, eso es el <a href="/servicios/agentes-de-ia/departamento-de-ia-externalizado">departamento de IA externalizado</a>; para la página web existe un <a href="/servicios/webs/mantenimiento-mensual">mantenimiento web mensual</a> aparte, y las conexiones entre programas se tratan en <a href="/servicios/migraciones-e-integraciones/integraciones-por-api">integraciones por API</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo comprobar si una automatización lleva tiempo fallando sin que nadie lo sepa?", "Comparando lo que entra con lo que sale: formularios recibidos frente a contactos creados, pedidos de la tienda frente a pedidos en el programa, citas dadas frente a recordatorios enviados. Si los números no cuadran, hay un paso que no se está ejecutando."),
  ("¿Qué pasa si la persona que montó mis automatizaciones ya no está?", "Se puede retomar. Primero se recuperan los accesos y se documenta qué hace cada flujo; después se decide si conviene mantenerlo tal cual, corregirlo o rehacerlo. Si no hay forma de acceder a alguna cuenta, habrá que reconstruir esa parte."),
 ],
}

# Estructura: recorrido de un presupuesto en pasos numerados + decisiones que no se delegan (definiciones)
D["servicios/agentes-de-ia/presupuestos-automaticos"] = {
 "estructura": "recorrido-de-un-presupuesto-tardio + decisiones-no-delegables-en-definiciones",
 "lead": "Pasas el día en la obra, el taller o las visitas, y los presupuestos los haces de noche. Cuando por fin envías uno, el cliente ya ha aceptado el de otro que respondió antes. Con los presupuestos automáticos con IA la oferta queda preparada desde la consulta y a ti solo te toca revisarla.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">El que contesta primero juega con ventaja</p><h2>¿Cuántos trabajos pierdes por tardar en enviar el presupuesto?</h2><p class="lead" style="margin-top:8px">No hay estadística que valga: mira los que mandaste el mes pasado y cuántos días pasaron desde que te los pidieron.</p></div>
<blockquote style="max-width:820px"><p>«Buenas, ¿cuánto me costaría cambiar las ventanas del salón? Es un tercero.»</p></blockquote>
<h3>Lo que le pasa a una petición así cuando se hace a mano</h3>
<ol style="max-width:820px">
<li><strong>Llega la consulta</strong> por WhatsApp, a medias, sin medidas ni material.</li>
<li><strong>Le preguntas medidas</strong> cuando tienes un rato; contesta al día siguiente.</li>
<li><strong>Buscas la tarifa</strong> del proveedor, que ha cambiado, y el presupuesto parecido del año pasado.</li>
<li><strong>Lo montas</strong> en una hoja de cálculo copiando otro y cambiando cifras, con el riesgo de dejar una línea del anterior.</li>
<li><strong>Lo envías</strong> y te olvidas. Nadie vuelve a escribir al cliente.</li>
</ol>
<p style="max-width:820px">Cada paso tiene una espera, y la suma de esperas es la razón por la que el cliente se va. Un agente de presupuestos recorta las esperas de los pasos dos, tres y cinco; el cuarto lo deja hecho para que lo mires.</p>
<h3 style="margin-top:28px">Lo que no conviene delegar nunca</h3>
<dl style="max-width:820px">
<dt><strong>El precio de lo que no has visto</strong></dt><dd>Una reforma con sorpresas detrás del alicatado se presupuesta tras la visita. El agente puede dar una horquilla orientativa si tú lo autorizas, dejando claro que no es una oferta en firme.</dd>
<dt><strong>Los descuentos</strong></dt><dd>Aplica los que hayas escrito como regla. Todo lo demás espera tu aprobación.</dd>
<dt><strong>El último vistazo</strong></dt><dd>Un cálculo automático puede arrastrar una tarifa vieja o entender mal una medida. Lo que envías con tu nombre lo lees tú antes.</dd>
<dt><strong>Decir que no</strong></dt><dd>Hay trabajos que no te interesan. Rechazarlos con tacto es cosa tuya.</dd>
</dl>
<p style="max-width:820px">Funciona cuando tus precios se pueden explicar con reglas; si cada trabajo lo valoras «a ojo», primero hay que poner esas reglas por escrito, y ese ejercicio ya suele ordenar el negocio. Si prefieres que el cliente se calcule el precio él mismo en tu página, mira el <a href="/servicios/software-de-gestion/presupuestador-y-configurador-online">presupuestador y configurador online</a>; para que lo aceptado no haya que teclearlo de nuevo, los <a href="/servicios/software-de-gestion/presupuestos-que-pasan-a-pedido-y-factura">presupuestos que pasan a pedido y factura</a>. En obra, lo específico es <a href="/servicios/software-de-gestion/presupuestos-desde-mediciones">presupuestar desde mediciones</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo enviar presupuestos más rápido sin contratar a un administrativo?", "Dejando que un agente de IA recoja los datos que faltan, aplique tus tarifas y prepare el documento con tu plantilla. Tú lo revisas y lo apruebas desde el móvil, y el seguimiento posterior también queda automatizado."),
  ("¿Qué pasa si el agente calcula mal un presupuesto?", "Para eso existe tu aprobación antes del envío. Además se fijan topes: importes a partir de los cuales siempre revisas con detalle y tipos de trabajo que el agente solo prepara en borrador. Los errores detectados sirven para corregir la regla que los causó."),
  ("¿Cuánto trabajo lleva preparar mis tarifas para automatizar los presupuestos?", "Depende de cómo las tengas. Con una lista de precios, los extras habituales y los mínimos por escrito se empieza pronto. Si los precios están solo en tu cabeza, hay que dedicar unas sesiones a convertirlos en reglas, empezando por los trabajos más repetidos."),
 ],
}

# Estructura: semana de anotaciones antes de decidir + dónde debe callarse + cómo se presenta (cita)
D["servicios/agentes-de-ia/recepcionista-de-voz-y-atencion-fuera-de-horario"] = {
 "estructura": "semana-de-anotaciones + reglas-de-derivacion + cita-de-presentacion",
 "lead": "Con las manos en una caldera, con un paciente en el sillón o en mitad de una clase no se puede coger el teléfono. Quien llama no deja mensaje: marca el siguiente número de la lista. Una recepcionista virtual con IA atiende esas llamadas sin atender, resuelve lo sencillo y te deja el recado completo.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">El teléfono suena cuando peor te viene</p><h2>¿Qué pasa con las llamadas que no puedes coger mientras trabajas?</h2></div>
<p style="max-width:820px">La mayoría se pierde, porque casi nadie habla con un contestador. Y no es un problema solo de noches y festivos: en muchos negocios pequeños las llamadas perdidas se concentran en plena jornada, justo cuando hay más trabajo. Antes de pensar en soluciones conviene saber de qué tamaño es el tuyo.</p>
<h3 style="margin-top:28px">Una semana de anotaciones antes de decidir</h3>
<ol style="max-width:820px">
<li>Mira en el registro del teléfono cuántas llamadas entraron y cuántas quedaron sin contestar.</li>
<li>Apunta a qué horas se concentran: mediodía, primera hora, sábados.</li>
<li>De las que sí atendiste, marca cuáles eran siempre lo mismo (horario, precio orientativo, pedir o mover una cita).</li>
<li>Señala cuáles necesitaban de verdad hablar contigo.</li>
</ol>
<p style="max-width:820px">Si las perdidas son pocas y casi todas requerían tu criterio, un asistente telefónico te aportará poco. Si son muchas y repetitivas, es donde más se nota.</p>
<h3 style="margin-top:28px">Dónde tiene que callarse y pasar la llamada</h3>
<ul class="lista" style="max-width:820px">
<li>Ante cualquier cosa que suene a emergencia de salud o de seguridad: no valora, deriva según el protocolo que le hayas dado.</li>
<li>Cuando la persona se altera o pide hablar con alguien.</li>
<li>Si no entiende tras dos intentos: acentos marcados, ruido de fondo o mala cobertura le afectan más que a una persona.</li>
<li>En todo lo que implique un precio cerrado, un diagnóstico o un compromiso que no esté escrito en sus reglas.</li>
</ul>
<blockquote style="max-width:820px"><p>«Hola, soy el asistente automático de la clínica. Puedo darte cita, cambiarla o dejar un aviso para el equipo. ¿En qué te ayudo?»</p></blockquote>
<p style="max-width:820px">Así debería empezar: identificándose como automático desde la primera frase. Ocultarlo no trae nada bueno y hay personas, sobre todo mayores, que prefieren saberlo y pedir que les llamen. Antes de activarla se prueba con llamadas representativas de tu negocio, y si se graban o transcriben las conversaciones hay que informar de ello. La tecnología de voz, los números y los idiomas se explican en <a href="/servicios/pix/agentes-de-voz">agentes de voz de PIX</a>; si tus clientes escriben más que llaman, mira las <a href="/servicios/whatsapp-ia/citas-y-recordatorios-automaticos">citas y recordatorios por WhatsApp</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo atender las llamadas de mi negocio cuando estoy trabajando y no puedo coger el teléfono?", "Desviando a un asistente de voz las llamadas que no contestas en unos segundos. Responde lo habitual, gestiona la cita si hay agenda conectada o toma el recado con el motivo, y tú recibes un resumen para devolver solo las llamadas que lo necesitan."),
  ("¿Qué pasa si la recepcionista de IA no entiende a quien llama?", "Pide que lo repita y, si sigue sin entender, no improvisa: toma el nombre y el teléfono, avisa a tu equipo y, si lo has configurado así, transfiere la llamada a una persona."),
  ("¿Sustituye a la persona de recepción?", "No es el objetivo. Descarga las consultas repetidas y cubre las horas en que nadie puede descolgar. Lo que exige criterio, trato delicado o conocer al cliente sigue siendo trabajo de una persona."),
 ],
}

# Estructura: situación del dueño frente a la ficha + mito/realidad en lista de definiciones + reparto de quién firma
D["servicios/agentes-de-ia/respuesta-a-resenas-de-google"] = {
 "estructura": "dueno-frente-a-la-ficha + mitos-en-definiciones + quien-firma",
 "lead": "Tienes veinte opiniones sin contestar y una de una estrella que te escuece cada vez que la lees. Contestarla en caliente es mala idea; dejarla ahí, también. Responder reseñas de Google con IA y tu propio tono te prepara cada respuesta para que tú solo decidas si se publica.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Lo primero que lee quien aún no te conoce</p><h2>¿Hace falta contestar a todas las reseñas, también a las malas?</h2></div>
<p style="max-width:820px">Conviene, porque tu respuesta no la lee solo quien escribió la opinión: la lee todo el que está decidiendo si ir a tu restaurante, tu clínica o tu taller. Una crítica sin contestar parece dejadez; una contestada con calma dice más de ti que diez elogios.</p>
<p style="max-width:820px">El problema es el momento. Las reseñas llegan cuando estás trabajando, y las negativas llegan además con rabia. Escribir bien, sin ponerse a la defensiva y sin copiar la misma frase de siempre, pide un rato de cabeza fría que casi nunca tienes.</p>
<h3 style="margin-top:28px">Ideas equivocadas sobre contestar opiniones con IA</h3>
<dl style="max-width:820px">
<dt><strong>«Se notará que es un robot»</strong></dt><dd>Se nota cuando todas las respuestas son iguales. Si menciona lo que el cliente contó y usa tus expresiones, suena a ti. Aun así, léela antes.</dd>
<dt><strong>«Así borro las malas»</strong></dt><dd>No. Ni nosotros ni nadie puede retirar una opinión legítima. Solo se puede solicitar la revisión de las que incumplen las normas de Google, y decide Google.</dd>
<dt><strong>«Puede escribir reseñas buenas por mí»</strong></dt><dd>No lo hacemos. Las opiniones falsas son un engaño al consumidor y un riesgo para tu ficha.</dd>
<dt><strong>«Contestando subo en el mapa»</strong></dt><dd>Responder ayuda a la confianza y a la actividad de la ficha, pero no existe relación directa que podamos prometerte con la posición.</dd>
</dl>
<h3 style="margin-top:28px">Lo que debería pasar siempre por tus manos</h3>
<p style="max-width:820px">Una reseña que menciona un problema de salud, una intoxicación, un accidente, a un empleado con nombre o una amenaza legal no se contesta con un borrador automático: te avisa y esperas a tener los hechos. En sectores sanitarios, además, la respuesta no puede confirmar que esa persona es paciente tuya. Lo razonable es empezar aprobando tú cada contestación y, cuando compruebes que acierta el tono, dejar que las positivas sencillas salgan solas. Si tu ficha está incompleta, antes va <a href="/servicios/presencia-digital/google-business-profile">optimizar el perfil de Google Business</a>; y para aparecer en más búsquedas de tu zona, el <a href="/servicios/presencia-digital/seo-local-y-por-sectores">SEO local y por sectores</a>. Pedir opinión tras la visita se hace con <a href="/servicios/software-de-gestion/recordatorios-automaticos-por-whatsapp">mensajes automáticos por WhatsApp</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo responder a una reseña negativa de Google sin empeorar las cosas?", "Con una respuesta breve que agradezca el aviso, reconozca lo que se pueda reconocer sin discutir los detalles en público y ofrezca un contacto directo para resolverlo. La IA prepara ese borrador con tu tono; tú compruebas los hechos y decides si se publica."),
  ("¿Qué pasa si la IA contesta algo inadecuado a un cliente enfadado?", "Para evitarlo, las reseñas negativas y las que tratan temas delicados no se publican solas: quedan como borrador y te llega un aviso. Solo se automatiza por completo lo que tú autorices, normalmente los agradecimientos sencillos."),
 ],
}

# Estructura: quién hace hoy la primera lectura + tabla de reparto IA/abogado | segunda sección: preguntas antes de subir un contrato
D["servicios/agentes-de-ia/revision-de-contratos-para-despachos"] = {
 "estructura": "tabla-reparto-ia-abogado + checklist-antes-de-subir-un-contrato-en-segunda-seccion",
 "lead": "Son las ocho de la tarde y quedan tres contratos de cuarenta páginas por leer antes de la reunión de mañana. La primera lectura la hace quien puede, cansado, buscando lo de siempre. La revisión de contratos con IA para despachos de abogados adelanta ese repaso y señala dónde mirar; la valoración sigue siendo del letrado.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Horas que el cliente no siempre paga</p><h2>¿Quién hace hoy la primera lectura de cada contrato en tu despacho?</h2></div>
<p style="max-width:820px">Suele hacerla un abogado júnior o el propio socio a última hora, y es un trabajo de comparación más que de criterio: localizar partes, plazos, importes y en qué se aparta el texto del modelo habitual. Es justo la parte donde el cansancio provoca descuidos y donde menos valor jurídico se aporta.</p>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Tarea</th><th>La puede adelantar la IA</th><th>Es del abogado</th></tr></thead><tbody>
<tr><td>Localizar fechas, importes, partes y preavisos</td><td>Sí, con cita del párrafo</td><td>Comprobar en el original lo decisivo</td></tr>
<tr><td>Comparar con la plantilla del despacho</td><td>Sí, cláusula a cláusula</td><td>Decidir qué desviaciones se aceptan</td></tr>
<tr><td>Valorar si una cláusula es válida o abusiva</td><td>No</td><td>Siempre</td></tr>
<tr><td>Tener en cuenta lo que el cliente contó de palabra</td><td>No lo conoce</td><td>Siempre</td></tr>
<tr><td>Aplicar jurisprudencia o cambios normativos recientes</td><td>No es fiable para eso</td><td>Siempre</td></tr>
<tr><td>Firmar el informe y responder ante el cliente</td><td>No</td><td>Siempre</td></tr>
</tbody></table></div>
</div></section>
<section class="sec sec-suave"><div class="w">
<h3>Antes de subir el primer contrato de un cliente</h3>
<ol style="max-width:820px">
<li>¿El encargo profesional o el deber de secreto te permiten tratar ese documento con esta herramienta? Si dudas, consulta tus normas colegiales.</li>
<li>¿Sabes dónde se procesa el texto y quién puede acceder? Debe constar por contrato.</li>
<li>¿Has definido qué abogados ven qué asuntos?</li>
<li>¿Tiene el despacho plantillas y criterios por escrito con los que comparar? Sin ellos, el resultado es genérico.</li>
<li>¿Has probado con contratos ya revisados a mano, para ver qué se le escapa?</li>
</ol>
<p style="max-width:820px">La quinta pregunta importa más de lo que parece: un sistema así puede omitir una cláusula relevante o resumirla con un matiz equivocado, y lo hará con la misma seguridad con que acierta. Por eso se usa como apoyo a la lectura y nunca como filtro que decide qué se revisa y qué no. No es asesoramiento jurídico ni lo sustituye. Para asuntos con confidencialidad reforzada existe la <a href="/servicios/agentes-de-ia/ia-en-servidor-propio">IA en servidor dedicado</a>; lo que ocurre después de la firma se gestiona con <a href="/servicios/software-de-gestion/contratos-con-firma-online">contratos con firma online</a>, y hay más casos del sector en la <a href="/guias/software-a-medida-para-despachos">guía de software para despachos</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo usar la IA para revisar contratos sin comprometer el secreto profesional?", "Trabajando en un entorno de empresa con acceso limitado por asunto, condiciones de tratamiento documentadas por contrato y registro de cada consulta, y nunca en un chat gratuito personal. Cada despacho debe valorar además sus normas deontológicas y lo pactado con el cliente."),
  ("¿Qué pasa si la IA no detecta una cláusula problemática?", "Es un riesgo real y por eso la revisión del abogado no se elimina. El agente reduce el tiempo de localización y comparación, pero la responsabilidad profesional y la lectura de los puntos críticos siguen siendo de quien firma el informe."),
  ("¿Sirve la revisión de contratos con IA para una asesoría o el departamento legal de una empresa?", "Sí, siempre que revisen contratos parecidos de forma habitual y tengan un modelo propio con el que comparar. El planteamiento y los límites son los mismos: adelanta la primera lectura y deja la decisión a la persona responsable."),
 ],
}

# Estructura: frase de mostrador (cita) + cuenta con tus números + errores que queman al cliente + cuándo no
D["servicios/agentes-de-ia/venta-adicional-en-pedidos-y-reservas"] = {
 "estructura": "cita-de-mostrador + cuenta-de-extras-no-ofrecidos + errores-que-queman + cuando-no",
 "lead": "En el mostrador siempre preguntas si quieren algo más; en una reserva por la web o en un pedido por WhatsApp no lo pregunta nadie. El cliente se entera del desayuno, del tratamiento o del recambio cuando ya es tarde. La venta adicional automática en pedidos y reservas hace esa pregunta una vez y en el momento oportuno.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Lo que tu mejor empleado hace sin pensar</p><h2>¿Cuánto dejas de vender por no ofrecer el complemento a tiempo?</h2></div>
<p style="max-width:820px">No lo sabrás hasta que lo midas, y no hay cifra general que sirva para tu negocio. Lo que sí es común: cuanto más se vende por canales donde no hay una persona delante, menos se ofrece.</p>
<blockquote style="max-width:820px"><p>«¿Le pongo también el líquido de frenos, que le toca?» «Tenemos parking, ¿se lo reservo?» «Si viene con la niña, hay menú infantil.»</p></blockquote>
<h3 style="margin-top:28px">Una cuenta rápida</h3>
<ol style="max-width:820px">
<li>Elige un extra que ya vendes bien cuando lo ofreces en persona.</li>
<li>Mira cuántos pedidos o reservas del mes pasado entraron por web, WhatsApp o teléfono sin que nadie lo propusiera.</li>
<li>Aplica la proporción de clientes que suele aceptarlo en el mostrador, rebajada, porque por mensaje se acepta menos.</li>
<li>Multiplica por el margen del extra, no por su precio.</li>
</ol>
<h3 style="margin-top:28px">Errores que convierten una sugerencia en una molestia</h3>
<ul class="lista" style="max-width:820px">
<li>Ofrecer algo que no tiene que ver con lo comprado.</li>
<li>Insistir tras un «no, gracias».</li>
<li>Proponer un extra que no hay en stock o que no cabe en la agenda.</li>
<li>Marcar la casilla por defecto para que el cliente tenga que quitarla. Eso no es vender, es colarlo, y no lo configuramos.</li>
<li>Sugerir tratamientos de salud sin que un profesional los haya indicado.</li>
</ul>
<h3 style="margin-top:28px">Si vendes pocas cosas, quizá no lo necesitas</h3>
<p style="max-width:820px">Con un solo servicio y sin complementos claros no hay nada que ofrecer, y forzarlo perjudica. Tampoco compensa con pocos pedidos al mes: una frase bien puesta en el mensaje de confirmación hace el mismo papel. Y el agente puede equivocarse al interpretar el historial, así que las reglas empiezan siendo pocas y se revisan con los datos de aceptación. Si lo tuyo es fidelizar a quien ya compró, mira <a href="/servicios/software-de-gestion/fidelizacion-y-bonos">fidelización y bonos</a>; para recuperar a quien hace tiempo que no viene, la <a href="/servicios/whatsapp-ia/reactivacion-de-clientes-y-pacientes-inactivos">reactivación de clientes inactivos</a>; y si aún no recibes reservas en línea, las <a href="/servicios/software-de-gestion/reservas-de-mesas-salas-clases-o-servicios">reservas de mesas, salas, clases o servicios</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo aumentar el importe medio de cada pedido sin agobiar al cliente?", "Ofreciendo un único complemento relacionado con lo que acaba de pedir, justo al confirmar, y aceptando el no a la primera. Las reglas las defines tú y se revisan con los datos: lo que nadie acepta se retira."),
  ("¿Qué pasa si el agente ofrece un extra que ya no tengo disponible?", "No debería, porque consulta el stock o la agenda antes de proponer. Si esos datos no están actualizados en tu programa, el riesgo existe; en ese caso se limita la oferta a extras sin restricción de disponibilidad hasta que el dato sea fiable."),
 ],
}
