# Reescritura «dolores primero» · familia software de gestión (noviembre 2026).
# 34 páginas, cada una con su recorrido propio. Sin precios en toda la familia (programa de gestión y CRM).
D = {}

# Estructura: escena en la recepción de un centro de fisioterapia + cinco preguntas de autodiagnóstico + lo que no cambia (teléfono)
D["servicios/software-de-gestion/agenda-y-citas-online"] = {
 "estructura": "escena-en-recepcion + cinco-preguntas-de-autodiagnostico + lo-que-no-cambia",
 "lead": "Suena el teléfono mientras atiendes, apuntas la cita en un papel y por la tarde aparecen dos personas a la misma hora. Una agenda de citas online para tu negocio deja que cada cliente reserve solo en los huecos que de verdad tienes y guarda la visita en su ficha.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Una mañana cualquiera en recepción</p><h2>¿Cuántas veces dejas a un cliente a medias para coger una cita por teléfono?</h2></div>
<p style="max-width:820px">Imagina un centro de fisioterapia a las diez y cuarto. Hay un paciente en camilla, otro esperando para pagar y el teléfono suena por tercera vez: alguien quiere cambiar su sesión del jueves. La cita se mueve en la libreta, pero no en el calendario del móvil del otro fisio. El jueves habrá un hueco vacío y el viernes, dos personas en la misma sala.</p>
<p style="max-width:820px">El fallo no está en el teléfono ni en quien lo coge. Está en que la agenda vive en tres sitios a la vez (la libreta, el WhatsApp y la memoria de alguien) y cada cambio obliga a actualizar los tres.</p>
<h3 style="margin-top:28px">Cinco preguntas para saber si la agenda ya se te ha quedado pequeña</h3>
<ol style="max-width:820px">
<li>¿Te piden hora por WhatsApp a deshoras y contestas al día siguiente?</li>
<li>¿Has tenido este mes dos citas pisadas o un hueco que nadie llenó?</li>
<li>¿Solo una persona del equipo sabe «leer» la agenda?</li>
<li>¿Llamas para confirmar y la mitad no coge?</li>
<li>¿Al cobrar tienes que buscar qué servicio se hizo y a quién?</li>
</ol>
<p style="max-width:820px">Con dos respuestas afirmativas, el sistema de citas actual te está costando horas de mostrador y visitas perdidas. Con cuatro, además te está costando clientes.</p>
<h3 style="margin-top:28px">Lo que no tiene por qué cambiar</h3>
<p style="max-width:820px">Poner un calendario de reservas online no significa dejar de atender llamadas. Quien prefiere telefonear lo sigue haciendo y tu equipo anota esa cita en la misma agenda, con lo que el hueco desaparece también de la web. Tampoco hace falta implantar un programa entero para empezar: se puede arrancar solo con las citas y sumar después bonos o facturación. Si lo tuyo son plazas con aforo, como clases o mesas, encaja mejor el <a href="/servicios/software-de-gestion/reservas-de-mesas-salas-clases-o-servicios">sistema de reservas</a>; si quieres que el chat proponga las horas, mira las <a href="/servicios/whatsapp-ia/citas-y-recordatorios-automaticos">citas por WhatsApp</a>; y si aún no tienes página, la <a href="/servicios/webs/web-con-reservas-y-citas">web con reservas</a> resuelve las dos cosas.</p>
</div></section>""",
 "faq": [
  ("¿Cómo poner una agenda de citas online en mi negocio si ahora lo apunto todo en papel?", "Empieza por escribir qué servicios das, cuánto dura cada uno y en qué horario trabaja cada profesional. Con esa lista se configura la agenda, se cargan las citas que ya tienes dadas y durante unos días conviven el papel y la pantalla hasta que el equipo se fía."),
  ("¿Puedo seguir dando citas por teléfono con una agenda online?", "Sí. La reserva online es una puerta más, no la única. Las citas que entran por teléfono o en el mostrador las anota tu equipo en la misma agenda, de modo que el hueco deja de ofrecerse en la web en ese momento."),
  ("¿Qué pasa si un cliente no encuentra hueco en la agenda online?", "Puede apuntarse a la lista de espera o dejar un aviso para que le llaméis. Lo importante es decidir de antemano qué se le ofrece, para que no se vaya sin respuesta a buscar otro sitio."),
 ],
}

# Estructura: cita con frases del equipo + tabla de lo que se pierde entre la calle y la oficina + cuándo una app no arregla nada
D["servicios/software-de-gestion/app-movil"] = {
 "estructura": "cita-con-frases-del-equipo + tabla-calle-oficina + cuando-una-app-no-arregla-nada",
 "lead": "«Luego lo paso cuando llegue a la oficina» es la frase con la que se pierden pedidos, horas y notas de visita. Con la app móvil del programa de gestión tu equipo consulta y registra desde el teléfono, en la calle, lo mismo que verías en el ordenador.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Lo que se queda por el camino</p><h2>¿Por qué lo que pasa en la calle llega tarde, o no llega, a la oficina?</h2></div>
<blockquote style="max-width:820px">«Me lo dijo el cliente en la visita, pero no lo apunté.»<br>«Te mando una foto del albarán por WhatsApp y lo metes tú.»<br>«No sé si ese piso sigue disponible, llamo a la oficina y te digo.»</blockquote>
<p style="max-width:820px">Detrás de estas frases hay siempre lo mismo: el dato nace lejos del ordenador y alguien tiene que volver a escribirlo horas después. En ese traslado se pierde una parte, y la que llega obliga a administración a perseguir a los compañeros para completar lo que falta.</p>
<div class="tabla-wrap" style="margin-top:20px"><table class="tabla-norm"><thead><tr><th>Lo que ocurre fuera</th><th>Dónde se queda hoy</th><th>Con el programa en el móvil</th></tr></thead><tbody>
<tr><td>Un cliente pide algo durante la visita</td><td>En una nota del teléfono personal</td><td>Se crea el pedido o la tarea delante de él</td></tr>
<tr><td>Hay que saber si debe facturas antes de servirle</td><td>En una llamada a la oficina</td><td>Se consulta en su ficha, sin molestar a nadie</td></tr>
<tr><td>Se acaba un trabajo a las siete de la tarde</td><td>En la memoria, hasta el día siguiente</td><td>Queda anotado al terminar, con su hora</td></tr>
<tr><td>Alguien necesita un día libre</td><td>En un mensaje al encargado</td><td>Solicitud registrada y visible para quien aprueba</td></tr>
</tbody></table></div>
<h3 style="margin-top:28px">Cuándo una aplicación para el equipo no te arregla nada</h3>
<p style="max-width:820px">Si todo tu equipo trabaja sentado frente a una pantalla, la versión móvil aporta poco. Y si el programa de la oficina está desordenado (clientes duplicados, artículos sin precio), llevarlo en el bolsillo solo enseña el mismo desorden en pequeño: primero se ordena y luego se reparte. Tampoco conviene dar acceso a todo el mundo a la vez; funciona mejor empezar por un perfil, por ejemplo los comerciales con la <a href="/servicios/software-de-gestion/ficha-de-cliente-360">ficha de cliente</a>, y ampliar. Para cuadrillas que cierran partes en casa del cliente hay una versión específica, la <a href="/servicios/software-de-gestion/app-para-tecnicos-de-campo">app para técnicos de campo</a>, y si lo que necesitas no existe en ningún módulo, se valora una <a href="/servicios/apps-moviles/app-interna-para-empleados-y-tecnicos">app interna a medida</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo saber si mi equipo necesita la app móvil del programa de gestión?", "Si parte de la plantilla pasa la jornada fuera (visitas, repartos, obras, tiendas) y la oficina recibe llamadas para consultar datos o teclea después lo que otros anotaron, la necesita. Si todos trabajan en el mismo local con un ordenador delante, puede esperar."),
  ("¿Por dónde se empieza a usar el programa desde el móvil?", "Por una sola tarea que hoy duela: consultar la ficha del cliente antes de una visita, anotar un pedido o fichar. Cuando esa tarea se hace sin pensar, se añade la siguiente. Repartir todas las funciones el primer día suele acabar en que nadie usa ninguna."),
 ],
}

# Estructura: objeciones del dueño en lista de definiciones + qué preguntar antes de elegir programa
D["servicios/software-de-gestion/app-para-tecnicos-de-campo"] = {
 "estructura": "objeciones-en-lista-de-definiciones + preguntas-antes-de-elegir",
 "lead": "Tus técnicos pasan el día en la carretera y tú lo pasas al teléfono: dónde estás, qué te falta, cuándo acabas. Una app para técnicos de campo con partes y rutas les pone en el móvil el aviso, la dirección y el historial, y a la oficina le devuelve el trabajo cerrado.",
 "bloque": """<section class="sec sec-suave"><div class="w">
<div class="cab"><p class="kicker">Las pegas de siempre</p><h2>«Mis técnicos no van a usar una app»: ¿seguro?</h2><p class="lead" style="margin-top:8px">Es la objeción que más oímos en empresas de instalación, reparación y asistencia técnica. Casi nunca es un problema de edad ni de ganas.</p></div>
<dl style="max-width:820px">
<dt><strong>«Son de la vieja escuela, lo suyo es el talonario.»</strong></dt>
<dd>El talonario se rechaza menos de lo que parece cuando la alternativa quita trabajo: no hay que volver a la oficina a entregar papeles ni descifrar la letra de nadie. Si la pantalla pide más casillas que el papel, entonces sí la abandonan, y con razón.</dd>
<dt><strong>«Van a pensar que es para vigilarles.»</strong></dt>
<dd>Lo piensan si nadie les explica para qué sirve. Conviene decir con claridad qué se registra, quién lo ve y para qué, y enseñarles lo que ganan ellos: el historial del equipo antes de llamar al timbre y menos llamadas de la oficina.</dd>
<dt><strong>«Perderán más tiempo tecleando que trabajando.»</strong></dt>
<dd>Un parte bien planteado se rellena con toques, no con redacciones: materiales elegidos de una lista, fotos y firma. Lo que se escribe a mano es la excepción.</dd>
<dt><strong>«Con el grupo de WhatsApp nos apañamos.»</strong></dt>
<dd>Hasta que hay que facturar y alguien tiene que reconstruir, mensaje a mensaje, qué se hizo en cada casa. El chat avisa; no guarda historial por cliente ni prepara la factura.</dd>
</dl>
<h3 style="margin-top:28px">Qué preguntar antes de elegir un programa para tu servicio técnico</h3>
<ul class="lista" style="max-width:820px">
<li>¿El parte se adapta a mis trabajos o tengo que adaptarme yo a su formulario?</li>
<li>¿Quién reasigna un aviso urgente y cómo se entera el técnico?</li>
<li>¿El material gastado sale de mi almacén o de la furgoneta sin que nadie lo teclee?</li>
<li>¿Qué ocurre con los avisos periódicos? Si vives de contratos, necesitas <a href="/servicios/software-de-gestion/mantenimientos-programados">mantenimientos programados</a>.</li>
<li>¿Puedo probarlo con dos técnicos durante unas semanas antes de extenderlo?</li>
</ul>
<p style="max-width:820px">Si hoy tu cuello de botella es el documento que firma el cliente, empieza por los <a href="/servicios/software-de-gestion/ordenes-y-partes-de-trabajo-con-firma-y-fotos">partes de trabajo con firma y fotos</a>; si es el orden de las visitas, por la <a href="/servicios/software-de-gestion/planificacion-de-rutas">planificación de rutas</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo conseguir que los técnicos usen la app en vez del parte en papel?", "Contando con ellos desde el principio. Dos técnicos prueban el parte digital en trabajos reales, se quitan las casillas que sobran y solo entonces se extiende al resto. Cuando ven que ya no tienen que pasar por la oficina a entregar papeles, la adopción deja de ser un problema."),
  ("¿Cuántos técnicos hacen falta para que compense un programa de asistencia técnica?", "No depende tanto del número como del desorden. Con dos o tres técnicos que hacen varios avisos al día ya se nota en la facturación y en las segundas visitas evitadas. Un único profesional que factura al terminar cada trabajo puede arreglarse con menos."),
 ],
}

# Estructura: escena de fin de mes en un centro de pilates + tres cuentas en tarjetas + lista de dónde se tuerce a mano
D["servicios/software-de-gestion/bonos-cuotas-y-suscripciones"] = {
 "estructura": "escena-fin-de-mes + tres-cuentas-en-tarjetas + donde-se-tuerce-a-mano",
 "lead": "El bono de diez sesiones apuntado en una cartulina, la cuota que este mes no se pasó y la socia que jura que le quedaban dos clases. La gestión de bonos, cuotas y suscripciones de clientes lleva esa cuenta por ti: saldo, cobro y renovación en la ficha de cada persona.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Fin de mes en un centro de pilates</p><h2>¿Sabes cuánto has cobrado por adelantado y cuánto te queda por dar?</h2></div>
<p style="max-width:820px">Imagina el día 30 en un estudio con ciento y pico alumnas. Hay que pasar las cuotas, pero antes alguien revisa a mano quién se dio de baja, quién pidió congelar por una lesión y quién pagó en efectivo. Mientras tanto, en recepción se discute con una clienta si su bono tenía ocho sesiones o diez. Nadie miente: simplemente no hay un sitio donde mirarlo.</p>
<h3 style="margin-top:26px">Tres cuentas que puedes hacer hoy con tus propios datos</h3>
<div class="rejilla">
<div class="tarjeta"><h3>Sesiones vendidas y no dadas</h3><p>Suma lo que queda en los bonos abiertos. Es trabajo que ya has cobrado y todavía debes.</p></div>
<div class="tarjeta"><h3>Cuotas que tocaban y no entraron</h3><p>Compara los socios activos del mes con los recibos cobrados. La diferencia suele sorprender.</p></div>
<div class="tarjeta"><h3>Bonos a punto de caducar</h3><p>Cada uno es una conversación incómoda si nadie avisó antes al cliente.</p></div>
</div>
<p style="max-width:820px;margin-top:18px">Si tardas más de una tarde en obtener esas tres cifras, el control de abonos y mensualidades depende de la memoria del equipo.</p>
<h3 style="margin-top:26px">Dónde se tuerce cuando se lleva a mano</h3>
<ul class="lista" style="max-width:820px">
<li>La sesión se da, pero no se tacha: el bono dura más de lo que se pagó.</li>
<li>La baja se comunica de palabra y el recibo se sigue girando; después llega la devolución y el enfado.</li>
<li>Las subidas de tarifa se aplican a unos socios y a otros no.</li>
<li>Quien lleva la hoja de cálculo se va de vacaciones y nadie se atreve a tocarla.</li>
</ul>
<p style="max-width:820px">Un programa de cuotas y membresías no evita que un cliente deje de pagar ni decide por ti las condiciones: ordena lo que tú hayas fijado y te lo enseña a tiempo. Si cobras por banco, se apoya en las <a href="/servicios/software-de-gestion/remesas-y-domiciliaciones">remesas y domiciliaciones</a>; si las sesiones se reservan, en la <a href="/servicios/software-de-gestion/agenda-y-citas-online">agenda de citas</a>; y si lo que buscas es premiar a quien repite, eso es <a href="/servicios/software-de-gestion/fidelizacion-y-bonos">fidelización</a>, otra herramienta.</p>
</div></section>""",
 "faq": [
  ("¿Cómo llevar el control de los bonos de sesiones sin hojas de cálculo?", "Asociando cada bono a la ficha del cliente y descontando la sesión en el momento en que se da o se reserva. Así el saldo lo ve recepción, lo ve el profesional y lo ve el propio cliente, y deja de depender de una cartulina o de una celda."),
  ("¿Qué diferencia hay entre gestionar cuotas y tener un programa de fidelización?", "Las cuotas y los bonos son servicios que el cliente ya ha pagado o paga de forma periódica: hay que controlar saldo y cobro. La fidelización premia con puntos o regalos a quien vuelve. Se complementan, pero resuelven problemas distintos."),
  ("¿Cuánto tarda en ponerse en marcha un sistema de cuotas si ya tengo socios activos?", "Depende sobre todo de lo ordenados que estén los datos de partida: quién está activo, con qué tarifa y qué saldo tiene cada bono. Con esa lista clara, la carga inicial es rápida; el plazo concreto se da por escrito en la propuesta."),
 ],
}

# Estructura: tabla de alternativas para avisar a los clientes + lo que no hacemos + caso de pocos clientes
D["servicios/software-de-gestion/campanas-de-email-y-whatsapp"] = {
 "estructura": "tabla-de-alternativas-de-envio + lo-que-no-hacemos + caso-de-pocos-clientes",
 "lead": "Tienes cientos de clientes en el programa y, cuando quieres avisarles de algo, acabas copiando teléfonos a una lista de difusión. Las campañas de email y WhatsApp desde tu CRM salen de esos mismos datos: eliges a quién, escribes una vez y ves quién respondió.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Cuatro maneras de avisar a tus clientes</p><h2>¿Por qué tus envíos acaban en una lista de difusión que casi nadie contesta?</h2><p class="lead" style="margin-top:8px">Porque es lo que hay a mano. El problema no es el mensaje, sino que sale sin saber a quién le interesa ni qué pasó después.</p></div>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Cómo lo haces</th><th>Lo que suele pasar</th><th>Cuándo basta</th></tr></thead><tbody>
<tr><td>Lista de difusión del WhatsApp del negocio</td><td>Solo llega a quien te tiene guardado en contactos; todos reciben lo mismo y las respuestas se pierden entre chats</td><td>Avisos puntuales a un grupo pequeño</td></tr>
<tr><td>Exportar clientes a Excel y subirlos a una herramienta de boletines</td><td>La lista envejece el mismo día: bajas, clientes nuevos y compras recientes no están</td><td>Un boletín ocasional, si alguien mantiene la lista</td></tr>
<tr><td>Publicar en redes y esperar</td><td>Lo ve quien pasa por allí, no quien te compró</td><td>Novedades generales, no ofertas a clientes</td></tr>
<tr><td>Campaña lanzada desde el CRM</td><td>Se filtra por lo que cada cliente compró o dejó de comprar, y cada respuesta vuelve a su ficha</td><td>Cuando quieres repetirlo cada mes sin rehacer la lista</td></tr>
</tbody></table></div>
<h3 style="margin-top:28px">Lo que no hacemos en una campaña</h3>
<ul class="lista" style="max-width:820px">
<li>No cargamos bases de datos compradas ni teléfonos sacados de internet.</li>
<li>No se escribe a quien no ha dado permiso para recibir publicidad, por mucho que sea cliente.</li>
<li>No montamos envíos diarios: un negocio local que escribe demasiado consigue bajas, no ventas.</li>
<li>No prometemos un número de ventas por envío; sí te enseñamos qué ha movido cada mensaje.</li>
</ul>
<h3 style="margin-top:28px">¿Y si tengo pocos clientes?</h3>
<p style="max-width:820px">Con unas pocas decenas de clientes, escribir a cada uno en persona funciona mejor que cualquier envío masivo. El marketing por correo y mensajería empieza a compensar cuando ya no recuerdas de memoria quién compró qué. Antes de enviar nada conviene tener al día la <a href="/servicios/software-de-gestion/ficha-de-cliente-360">ficha de cada cliente</a>; para recuperar a quien dejó de venir existe un servicio específico de <a href="/servicios/whatsapp-ia/reactivacion-de-clientes-y-pacientes-inactivos">reactivación de clientes inactivos</a>; y si quieres dar un motivo para volver, combínalo con un <a href="/servicios/software-de-gestion/fidelizacion-y-bonos">programa de puntos</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo enviar un mensaje a todos mis clientes sin escribir uno por uno?", "Seleccionando en el CRM el grupo al que va dirigido, redactando el texto una vez con el nombre de cada cliente como campo y programando el envío por email, por WhatsApp o por ambos. Solo lo reciben quienes han aceptado comunicaciones comerciales."),
  ("¿Puedo hacer campañas si mis clientes están en un Excel y no en un CRM?", "Antes hay que pasarlos al programa y limpiarlos: duplicados, teléfonos antiguos y, sobre todo, quién ha dado su consentimiento. Sin ese paso la campaña sale, pero no sabrás qué funcionó ni podrás repetirla sin rehacer el trabajo."),
 ],
}

# Estructura: prueba de cliente misterioso en cuatro pasos + tres fugas en tarjetas
D["servicios/software-de-gestion/captacion-de-leads-desde-web-whatsapp-y-anuncios"] = {
 "estructura": "prueba-de-cliente-misterioso + tres-fugas-en-tarjetas",
 "lead": "Entra un formulario de la web, un mensaje por WhatsApp y dos contactos de un anuncio, y el lunes nadie sabe quién contestó a quién. La captación de leads desde web, WhatsApp y anuncios en un único CRM apunta a cada interesado con su origen y con un responsable.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Una prueba de diez minutos</p><h2>¿Qué le pasa a un interesado cuando te escribe? Compruébalo tú mismo</h2></div>
<p style="max-width:820px">Antes de invertir más en publicidad, haz de cliente misterioso de tu propio negocio. No cuesta nada y enseña más que cualquier informe.</p>
<ol style="max-width:820px">
<li><strong>Rellena tu formulario web</strong> con un correo que no conozca tu equipo. Apunta la hora.</li>
<li><strong>Escribe al WhatsApp de la empresa</strong> desde otro número, un viernes a media tarde.</li>
<li><strong>Pide a un amigo que conteste a uno de tus anuncios</strong> de Instagram, Facebook o Google.</li>
<li><strong>Espera y anota:</strong> cuánto tardó cada respuesta, quién la dio y si alguien le preguntó de dónde venía.</li>
</ol>
<h3 style="margin-top:28px">Las tres fugas que suele destapar la prueba</h3>
<div class="rejilla">
<div class="tarjeta"><h3>El aviso cae donde nadie mira</h3><p>El formulario envía a un buzón genérico o a la bandeja de quien ya no lleva ese tema. El contacto existe, pero no lo ve nadie.</p></div>
<div class="tarjeta"><h3>Cada canal tiene su dueño</h3><p>La web la mira administración, el WhatsApp lo lleva quien tiene el móvil y los anuncios los ve la agencia. Nadie tiene la lista completa de clientes potenciales.</p></div>
<div class="tarjeta"><h3>Nadie apunta de dónde vino</h3><p>Sin el origen de cada solicitud, a final de mes no sabes si el dinero de los anuncios trajo ventas o solo curiosos.</p></div>
</div>
<p style="max-width:820px;margin-top:18px">Centralizar los contactos comerciales no consiste en comprar otra herramienta, sino en que todas las entradas desemboquen en el mismo sitio y salgan de allí con nombre y fecha. A partir de ahí, cada oportunidad avanza por el <a href="/servicios/software-de-gestion/embudo-de-ventas-y-oportunidades">embudo de ventas</a> y las llamadas pendientes se organizan con el <a href="/servicios/software-de-gestion/seguimiento-comercial-y-tareas">seguimiento comercial</a>. Si el punto débil es la página donde aterriza el anuncio, eso se trabaja con una <a href="/servicios/webs/landing-pages-para-campanas">landing para campañas</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo centralizar los leads de la web y de WhatsApp en un CRM?", "Conectando cada entrada (formulario, número de WhatsApp de empresa y formularios de anuncios) al programa para que cree el contacto automáticamente, con su origen. Después se define quién recibe cada tipo de solicitud y en cuánto tiempo debe atenderla."),
  ("¿Qué hago con los contactos antiguos repartidos entre correos y móviles?", "Lo razonable es pasar al CRM solo los que siguen vivos: presupuestos abiertos y solicitudes de los últimos meses. Intentar recuperar todo el histórico retrasa el arranque y aporta poco."),
  ("¿Merece la pena un sistema de captación si recibo pocas solicitudes al mes?", "Si te llegan pocas y las atiendes tú mismo en el día, probablemente no. Empieza a compensar cuando entran por varios canales, las atiende más de una persona o inviertes en anuncios y necesitas saber qué te devuelven."),
 ],
}

# Estructura: frases que se oyen en la oficina + tabla «lo resuelve el programa / lo decides tú» + pocos artículos
D["servicios/software-de-gestion/catalogo-y-tarifas"] = {
 "estructura": "frases-de-oficina + tabla-programa-frente-a-decision-tuya + caso-pocos-articulos",
 "lead": "«¿A cuánto se lo dejamos a este cliente?» Si la respuesta depende de quién coja el teléfono, tienes un problema de precios, no de vendedores. Un catálogo de productos con tarifas de precios por cliente hace que presupuestos, pedidos y mostrador partan del mismo dato.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Lo que se oye en la oficina</p><h2>Cuando la lista de precios está en la cabeza de una persona</h2></div>
<ul class="lista" style="font-size:18px;max-width:820px">
<li>«Pregúntale a Carmen, que es la que sabe lo que se le cobra a cada uno.»</li>
<li>«Le pasé la tarifa del año pasado sin darme cuenta.»</li>
<li>«El proveedor subió en enero y nosotros seguimos vendiendo al precio de antes.»</li>
<li>«Ese descuento se lo prometió un comercial que ya no trabaja aquí.»</li>
</ul>
<p style="max-width:820px;margin-top:16px">Ninguna de estas situaciones es un despiste aislado. Aparecen cuando las condiciones comerciales viven repartidas entre una hoja de cálculo, un PDF antiguo y la memoria de quien lleva más años. Mientras esa persona está, el negocio funciona; el día que falta, cada pedido se convierte en una consulta.</p>
<h3 style="margin-top:28px">Qué pone el programa y qué sigues decidiendo tú</h3>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Lo resuelve el módulo</th><th>Sigue siendo decisión tuya</th></tr></thead><tbody>
<tr><td>Que el mismo artículo salga al mismo importe en presupuesto, pedido, mostrador y web</td><td>Qué tarifa merece cada cliente y por qué</td></tr>
<tr><td>Avisar cuando una venta deja un margen por debajo del que marcaste</td><td>Hasta dónde se puede bajar para cerrar una operación</td></tr>
<tr><td>Aplicar una subida a toda una familia de una vez</td><td>Cuándo subir y cuánto repercutir del aumento del proveedor</td></tr>
<tr><td>Guardar los acuerdos particulares con fecha</td><td>Revisarlos cuando dejan de tener sentido</td></tr>
</tbody></table></div>
<h3 style="margin-top:28px">¿Compensa con pocos artículos?</h3>
<p style="max-width:820px">Con una veintena de referencias y un precio único, una lista bien cuidada es suficiente. La gestión de tarifas empieza a hacer falta cuando vendes a distintos tipos de cliente, cuando tus costes cambian varias veces al año o cuando más de una persona da precios. En ese punto, el catálogo alimenta los <a href="/servicios/software-de-gestion/presupuestos-que-pasan-a-pedido-y-factura">presupuestos que pasan a pedido y factura</a>, el <a href="/servicios/software-de-gestion/tpv">TPV</a> y, si vendes a profesionales, el <a href="/servicios/software-de-gestion/portal-de-pedidos-b2b">portal de pedidos B2B</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo evitar que cada vendedor dé un precio distinto al mismo cliente?", "Asignando a cada cliente su tarifa en el programa y haciendo que todos los documentos tomen el precio de ahí. El vendedor ya no consulta una lista ni tira de memoria: el importe aparece solo y, si quiere cambiarlo, queda constancia de quién lo hizo."),
  ("¿Qué necesito tener preparado para montar mis tarifas en un programa?", "Un listado de artículos sin duplicados, el coste actual de cada uno y los tipos de cliente a los que vendes con sus condiciones. Los acuerdos especiales, aunque hoy sean de palabra, conviene escribirlos antes de cargarlos."),
 ],
}

# Estructura: cuatro causas del retraso en tarjetas + cuenta de lo que tienes en la calle + límites
D["servicios/software-de-gestion/cobros-impagos-y-semaforo-de-clientes"] = {
 "estructura": "cuatro-causas-en-tarjetas + cuenta-del-dinero-en-la-calle + limites",
 "lead": "Has hecho el trabajo, has enviado la factura y pasan las semanas sin que entre el dinero; reclamar te da apuro y, además, no tienes tiempo. Un programa para controlar cobros pendientes y vencimientos te dice cada mañana quién te debe, desde cuándo y a quién toca escribir.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Antes de culpar al cliente</p><h2>¿Por qué te pagan tarde si el trabajo está bien hecho?</h2><p class="lead" style="margin-top:8px">La mayoría de los retrasos no vienen de clientes que no quieren pagar, sino de facturas que nadie siguió.</p></div>
<blockquote style="max-width:820px">«Me da más apuro reclamar lo que me deben que trabajar gratis.»</blockquote>
<div class="rejilla">
<div class="tarjeta"><h3>La factura llegó a quien no paga</h3><p>Se envió al contacto de siempre y no a contabilidad. Sigue en una bandeja de entrada.</p></div>
<div class="tarjeta"><h3>Venció y nadie dijo nada</h3><p>Sin un aviso el mismo día, el cliente entiende que no corre prisa.</p></div>
<div class="tarjeta"><h3>Cobra antes quien insiste</h3><p>Cuando el cliente va justo de caja, paga primero al proveedor que le llama.</p></div>
<div class="tarjeta"><h3>Hay una pega que no te han contado</h3><p>Un albarán sin firmar, un importe que no cuadra. Hasta que alguien pregunta, la factura queda parada.</p></div>
</div>
<h3 style="margin-top:28px">Haz la cuenta de lo que tienes en la calle</h3>
<ol style="max-width:820px">
<li>Suma todas las facturas emitidas y no cobradas.</li>
<li>Separa las que ya han pasado su fecha de vencimiento.</li>
<li>Apunta cuántas de esas vencidas han recibido algún recordatorio tuyo.</li>
</ol>
<p style="max-width:820px">Si el tercer número es bajo, tu problema de morosidad es en buena parte un problema de seguimiento, y eso sí tiene arreglo con un control de facturas pendientes que avise solo.</p>
<p style="max-width:820px">Conviene saber también lo que esta herramienta no hace: no cobra por ti, no sustituye una reclamación formal cuando el cliente se niega a pagar y no decide a quién dejas de servir. Te da la información a tiempo para que lo decidas tú. Para ver cómo afectan esos retrasos a tu caja, enlaza con la <a href="/servicios/software-de-gestion/prevision-de-tesoreria">previsión de tesorería</a>; si cobras recibos periódicos, con las <a href="/servicios/software-de-gestion/remesas-y-domiciliaciones">remesas y domiciliaciones</a>; y si quieres que un asistente lleve la conversación de cobro, mira el <a href="/servicios/agentes-de-ia/cobros-e-impagos">agente de cobros e impagos</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo llevar el control de las facturas pendientes de cobro?", "Con un listado único, ordenado por fecha de vencimiento, que se actualice cuando entra cada pago. En un programa de gestión ese listado sale de las propias facturas, así que no hay que mantener una hoja aparte ni acordarse de tachar."),
  ("¿Cómo reclamar una factura vencida sin estropear la relación con el cliente?", "Pronto y con naturalidad. Un aviso amable al día siguiente del vencimiento, con la factura adjunta y los datos de pago, se recibe como un recordatorio. El mismo mensaje dos meses después se recibe como un reproche."),
 ],
}

# Estructura: tabla de las tres sillas (comercial, administración, gerencia) + reglas en un folio + caso de un solo vendedor
D["servicios/software-de-gestion/comerciales-y-comisiones"] = {
 "estructura": "tabla-de-tres-puntos-de-vista + reglas-en-un-folio + caso-un-solo-vendedor",
 "lead": "Llega fin de mes y el cálculo de comisiones se convierte en dos días de hojas de cálculo, correos cruzados y un vendedor convencido de que le falta dinero. Un software de comisiones para comerciales y agentes aplica las reglas pactadas a cada factura y enseña el detalle a quien cobra.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Tres sillas, un mismo problema</p><h2>¿Quién sufre cuando los incentivos de ventas se calculan a mano?</h2></div>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Quién</th><th>Lo que vive cada mes</th><th>Lo que necesitaría</th></tr></thead><tbody>
<tr><td>El comercial</td><td>Recibe una cifra sin desglose y lleva su propia cuenta paralela «por si acaso»</td><td>Ver, operación a operación, de dónde sale su liquidación</td></tr>
<tr><td>Administración</td><td>Cruza facturas, cobros y devoluciones con una hoja llena de excepciones que solo entiende quien la creó</td><td>Que el cálculo salga de los mismos datos con los que ya factura</td></tr>
<tr><td>Gerencia</td><td>Arbitra discusiones y paga variables sin saber si premian lo que le interesa vender</td><td>Reglas escritas y un resumen de lo que cuesta cada venta</td></tr>
</tbody></table></div>
<p style="max-width:820px;margin-top:18px">La desconfianza no nace de que alguien calcule mal, sino de que nadie puede comprobarlo. Cuando la retribución variable es opaca, el vendedor dedica tiempo a auditar su nómina en lugar de a vender.</p>
<h3 style="margin-top:28px">Antes de automatizar nada, escribe tus reglas en un folio</h3>
<p style="max-width:820px">Un programa aplica reglas; no las inventa. Si hoy no caben en una página, el primer trabajo es ese:</p>
<ol style="max-width:820px">
<li>Sobre qué se calcula el porcentaje y a partir de qué momento se considera ganado.</li>
<li>Qué ocurre si el cliente devuelve, no paga o paga con meses de retraso.</li>
<li>A quién pertenece un cliente cuando intervienen dos personas.</li>
<li>Qué se hace con las operaciones que no encajan en ningún caso.</li>
</ol>
<h3 style="margin-top:28px">Con un solo vendedor y un porcentaje fijo</h3>
<p style="max-width:820px">No te hace falta un módulo: una multiplicación al mes lo resuelve. La liquidación automática compensa con varios comerciales, agentes externos, tramos u objetivos. Y funciona mejor cuando ya registras la actividad en el <a href="/servicios/software-de-gestion/seguimiento-comercial-y-tareas">seguimiento comercial</a> y las operaciones en el <a href="/servicios/software-de-gestion/embudo-de-ventas-y-oportunidades">embudo de oportunidades</a>. Si además quieres fijar metas a personas que no venden, eso corresponde a <a href="/servicios/software-de-gestion/productividad-y-objetivos">productividad y objetivos</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo calcular las comisiones de los comerciales sin Excel?", "Definiendo las reglas una vez en el programa (base, porcentaje, tramos y condiciones) y dejando que se apliquen a cada factura conforme se emite o se cobra. A final de mes la liquidación ya está hecha y cada vendedor puede revisar su detalle."),
  ("¿Qué pasa si mis reglas de comisión tienen muchas excepciones?", "Se revisan una a una antes de configurar nada. Algunas se convierten en regla, otras se eliminan porque ya nadie recuerda su motivo y unas pocas quedan como ajuste manual con nota. Lo que no conviene es trasladar el caos tal cual al programa."),
 ],
}

# Estructura: escena del cierre de trimestre + cita del mensaje de la gestoría + preguntas para tu gestor + dónde acaba nuestro trabajo
D["servicios/software-de-gestion/conexion-con-tu-asesoria"] = {
 "estructura": "escena-cierre-de-trimestre + cita-del-gestor + preguntas-para-tu-gestor + limite-no-somos-asesoria",
 "lead": "Última semana del trimestre: la gestoría te pide las facturas que faltan, tú buscas tickets en la guantera y alguien reenvía los PDF uno a uno. Conectar tu programa de gestión con la asesoría convierte esa carrera en una entrega ordenada que sale al cerrar el periodo.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Cada tres meses, la misma carrera</p><h2>¿Por qué el cierre de trimestre siempre te pilla con papeles sueltos?</h2></div>
<p style="max-width:820px">Porque durante el trimestre nadie tiene el encargo de reunirlos. Las facturas de venta están en el programa o en una carpeta; las de compra, en el correo de tres personas; los tickets, donde cayeron. El último día alguien lo junta todo deprisa y lo manda como puede.</p>
<blockquote style="max-width:820px">«Me falta la factura de marzo del proveedor de siempre y dos tickets de gasolina. ¿Me los puedes pasar hoy?»</blockquote>
<p style="max-width:820px">Ese mensaje, a dos días del plazo, es incómodo para ti y también para tu gestor, que tiene decenas de clientes en la misma situación. Trabajar con prisas es el origen de casi todos los gastos que se quedan sin registrar.</p>
<h3 style="margin-top:28px">Qué preguntarle a tu gestor antes de conectar nada</h3>
<ul class="lista" style="max-width:820px">
<li>¿Con qué programa de contabilidad trabajáis y qué ficheros admite?</li>
<li>¿Preferís entrar vosotros a consultar o recibir un paquete cada mes?</li>
<li>¿Qué datos de cada factura necesitáis sí o sí para no tener que preguntarme?</li>
<li>¿Qué documentos os llegan hoy tarde o incompletos?</li>
<li>¿Quién será vuestra persona de contacto cuando algo no cuadre?</li>
</ul>
<p style="max-width:820px">Con esas cinco respuestas se decide el método. Sin ellas se corre el riesgo de montar un envío de facturas a la gestoría que al despacho no le sirve.</p>
<h3 style="margin-top:28px">Dónde acaba nuestro trabajo</h3>
<p style="max-width:820px">Studio Emprende no es una gestoría ni una asesoría fiscal: no presentamos impuestos ni llevamos tu contabilidad. Nuestro papel termina cuando los datos salen de tu programa completos y en el formato acordado; lo que se hace con ellos lo decide tu asesor. Para que las compras entren sin teclear, se combina con la <a href="/servicios/software-de-gestion/lectura-automatica-de-facturas-de-proveedores">lectura automática de facturas de proveedores</a>; para las ventas, con la <a href="/servicios/software-de-gestion/facturacion-con-verifactu">facturación con Verifactu</a>. Si lo que estás valorando es un sistema completo, lo explicamos en <a href="/servicios/erp-para-pymes/contabilidad-o-conexion-con-tu-asesoria">contabilidad o conexión con tu asesoría en un ERP</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo enviar las facturas a mi gestoría sin reenviar correos uno a uno?", "Registrando ventas, compras y gastos en el programa a medida que ocurren y dejando que sea el programa quien prepare la entrega: un acceso de consulta para el despacho o un fichero periódico con todo el periodo. Tú solo revisas que no falte nada antes de cerrar."),
  ("¿Quién revisa que los datos que recibe la asesoría están bien?", "La revisión contable sigue siendo de tu asesor. Lo que cambia es que le llega la información completa y ordenada, y que las dudas se resuelven sobre un documento concreto en vez de en una cadena de correos."),
 ],
}

# Estructura: glosario mínimo en lenguaje llano + tabla «cada cifra es tan reciente como su último apunte»
D["servicios/software-de-gestion/cuadro-de-mando-en-tiempo-real"] = {
 "estructura": "glosario-llano + tabla-frescura-del-dato",
 "lead": "El informe del lunes ya está viejo el jueves, y para saber cómo va el mes tienes que pedírselo a alguien que lo saca de un Excel. Un cuadro de mando en tiempo real para tu negocio lee los datos del programa y te los enseña en una pantalla, sin intermediarios.",
 "bloque": """<section class="sec sec-suave"><div class="w">
<div class="cab"><p class="kicker">Palabras claras</p><h2>¿Qué significa de verdad «tiempo real» en un panel de negocio?</h2></div>
<p style="max-width:820px">Significa que la pantalla cambia en cuanto alguien registra algo en el programa, no que adivine lo que todavía nadie ha apuntado. Parece un matiz, pero es la diferencia entre fiarse del panel y dejar de mirarlo. Estos son los términos que conviene tener claros antes de pedir un dashboard:</p>
<dl style="max-width:820px">
<dt><strong>Indicador (o KPI)</strong></dt><dd>Un número que resume algo que te importa: lo vendido esta semana, lo que te deben, los trabajos abiertos. Si no lleva a ninguna decisión, sobra.</dd>
<dt><strong>Fuente del dato</strong></dt><dd>El sitio del que sale la cifra: facturas, tickets, partes, almacén. Un indicador sin fuente clara acaba en discusión.</dd>
<dt><strong>Desglose</strong></dt><dd>Poder pulsar el total y ver qué lo compone. Sin esto, el panel plantea preguntas que no deja responder.</dd>
<dt><strong>Umbral</strong></dt><dd>El valor a partir del cual quieres que te avisen, para no tener que estar mirando.</dd>
</dl>
<h3 style="margin-top:28px">Cada cifra es tan reciente como su último apunte</h3>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Lo que miras</th><th>Se mueve cuando…</th><th>Si se registra tarde…</th></tr></thead><tbody>
<tr><td>Ventas</td><td>Se emite la factura o el ticket</td><td>Un trabajo acabado y sin facturar no aparece</td></tr>
<tr><td>Pendiente de cobro</td><td>Se anota el pago recibido</td><td>Verás como deudor a quien ya pagó</td></tr>
<tr><td>Existencias</td><td>Se da entrada o salida a la mercancía</td><td>El aviso de mínimo llega con el estante ya vacío</td></tr>
<tr><td>Trabajos en curso</td><td>El equipo abre o cierra el parte</td><td>La carga de trabajo parece mayor o menor de lo que es</td></tr>
</tbody></table></div>
<p style="max-width:820px;margin-top:18px">Por eso un panel de control empresarial no se arregla con gráficos más bonitos, sino con hábitos de registro. Cuando esos hábitos existen, la dirección deja de esperar al cierre mensual. Si prefieres que los números te lleguen sin abrir nada, está el <a href="/servicios/software-de-gestion/informe-semanal-automatico-por-whatsapp-o-voz">resumen semanal en el móvil</a>; para saber qué deja margen, la <a href="/servicios/software-de-gestion/rentabilidad-por-cliente-servicio-y-empleado">rentabilidad por cliente y servicio</a>; y si tus datos están repartidos entre varios programas, el <a href="/servicios/automatizacion-y-datos/cuadro-de-mando-de-direccion">cuadro de mando de dirección</a> los reúne.</p>
</div></section>""",
 "faq": [
  ("¿Cómo ver los resultados de mi negocio en un dashboard sin depender de Excel?", "Haciendo que el panel lea directamente del programa donde ya facturas, cobras y registras trabajos. Así nadie exporta ni pega datos: la cifra se recalcula con cada apunte y puedes abrirla desde el ordenador o el móvil."),
  ("¿Qué diferencia hay entre un cuadro de mando y el informe mensual de siempre?", "El informe mensual es una foto que alguien prepara cuando el mes ya ha terminado. El cuadro de mando es la misma información viva, consultable cualquier día, lo que permite corregir a mitad de mes en lugar de lamentarlo después."),
 ],
}

# Estructura: tres momentos de apuro en tarjetas + la persona que sabe dónde está todo + lista de lo que el módulo no hace
D["servicios/software-de-gestion/documentacion-del-empleado"] = {
 "estructura": "tres-momentos-de-apuro-en-tarjetas + dependencia-de-una-persona + lista-de-lo-que-no-hace",
 "lead": "Un trabajador te pide su contrato para el banco, una contrata exige un certificado de formación y una auditoría quiere ver un documento firmado: los tres papeles están «en alguna carpeta». La gestión documental de empleados reúne contratos y nóminas en un expediente digital por persona.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Tres momentos de apuro</p><h2>¿Dónde está ese papel cuando alguien te lo pide con prisa?</h2></div>
<div class="rejilla">
<div class="tarjeta"><h3>Lo pide el propio trabajador</h3><p>Necesita sus últimas nóminas o su contrato para un alquiler o un préstamo, y los necesita esta semana. Alguien deja lo que está haciendo para buscarlos y escanearlos.</p></div>
<div class="tarjeta"><h3>Lo pide un cliente o una contrata</h3><p>Antes de dejar entrar a tu operario en su obra o su fábrica, quieren ver su formación al día. Si el curso caducó hace un mes, te enteras en la puerta.</p></div>
<div class="tarjeta"><h3>Lo pide quien viene a revisar</h3><p>Una auditoría o una inspección solicita un documento con la firma del empleado. Existe, pero nadie recuerda en qué archivador.</p></div>
</div>
<p style="max-width:820px;margin-top:18px">En casi todas las pymes el archivo de personal funciona gracias a una persona que sabe dónde está cada cosa. Es un buen sistema hasta que esa persona enferma, cambia de puesto o se jubila. Entonces se descubre que los expedientes laborales no estaban ordenados: estaban memorizados.</p>
<p style="max-width:820px">Pasar a un expediente digital del trabajador no va de escanear por escanear. Va de que cada documento tenga dueño, fecha y, si caduca, un aviso antes de que caduque.</p>
<h3 style="margin-top:28px">Lo que este módulo no hace</h3>
<ul class="lista" style="max-width:820px">
<li>No confecciona nóminas ni redacta contratos: eso sigue siendo cosa de tu gestoría o de tu asesor laboral.</li>
<li>No decide cuánto tiempo hay que conservar cada papel; guarda lo que tu asesor te indique.</li>
<li>No sustituye al servicio de prevención ni valida por sí solo que un certificado sea el exigido.</li>
</ul>
<p style="max-width:820px">Lo que sí hace es dejar de depender de un archivador. Para los documentos que requieren firma se apoya en los <a href="/servicios/software-de-gestion/contratos-con-firma-online">contratos con firma online</a>; para la llegada de personal nuevo, en el <a href="/servicios/software-de-gestion/onboarding-con-ia">onboarding guiado</a>; y los permisos y días libres se llevan en <a href="/servicios/software-de-gestion/turnos-vacaciones-y-ausencias">turnos, vacaciones y ausencias</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo organizar la documentación de los empleados en una empresa pequeña?", "Con una carpeta por persona y la misma estructura para todos: contrato y anexos, nóminas, formación, reconocimientos y entregas de material. Lo importante es que cada documento tenga fecha y que alguien reciba aviso cuando uno caduca."),
  ("¿Tiene sentido digitalizar los expedientes si somos menos de diez personas?", "Depende de la rotación y de lo que te pidan terceros. Con plantilla estable y pocos documentos, una carpeta ordenada puede bastar. Si contratas por temporadas o tus clientes exigen certificados antes de cada trabajo, compensa aunque seáis pocos."),
 ],
}

# Estructura: tabla de costumbres y lo que provocan + tres preguntas + cuándo no compensa
D["servicios/software-de-gestion/etiquetas-codigos-de-barras-y-qr"] = {
 "estructura": "tabla-costumbres-y-consecuencias + tres-preguntas + cuando-no-compensa-etiquetar",
 "lead": "Teclear referencias a mano en la caja, cobrar un producto por otro que se le parece y contar el almacén con boli y papel son tres costumbres que salen caras. Un programa para imprimir etiquetas con código de barras identifica cada artículo con una lectura, sin escribir nada.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Lo que cuesta no tener códigos</p><h2>¿Cuántos descuadres de tu tienda o tu almacén empiezan con alguien tecleando una referencia?</h2></div>
<p style="max-width:820px">Más de los que parece. Cada vez que una persona busca un artículo por su nombre o copia un número de memoria, hay una posibilidad de elegir el de al lado. El error no se ve en el momento: aparece semanas después, cuando el inventario no cuadra y ya nadie sabe por qué.</p>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Costumbre</th><th>Qué provoca</th><th>Cómo lo notas</th></tr></thead><tbody>
<tr><td>Buscar el producto por nombre al cobrar</td><td>Se vende la variante equivocada (otro color, otra medida)</td><td>Dos artículos descuadrados a la vez: uno sobra y otro falta</td></tr>
<tr><td>Rotular precios a mano</td><td>El estante marca un importe y la caja otro</td><td>Discusiones en el mostrador y rebajas improvisadas</td></tr>
<tr><td>Inventariar con un listado impreso</td><td>Baldas contadas dos veces o ninguna</td><td>Un día de cierre para obtener cifras de las que nadie se fía</td></tr>
<tr><td>Herramientas y equipos sin identificar</td><td>No se sabe quién tiene qué ni cuándo se revisó</td><td>Se compra o se alquila lo que ya estaba en la nave</td></tr>
</tbody></table></div>
<h3 style="margin-top:28px">Tres preguntas para saber si te hace falta etiquetar</h3>
<ol style="max-width:820px">
<li>¿Tienes artículos que se parecen tanto que solo los distingue quien lleva años?</li>
<li>¿Un empleado nuevo tarda semanas en cobrar o preparar pedidos con soltura?</li>
<li>¿El recuento anual te obliga a cerrar o a venir en festivo?</li>
</ol>
<p style="max-width:820px">Un sí a cualquiera de las tres indica que el etiquetado de productos te ahorraría tiempo desde el primer mes.</p>
<h3 style="margin-top:28px">Cuándo no merece la pena</h3>
<p style="max-width:820px">Si fabricas piezas únicas por encargo o vendes un puñado de servicios, un sistema de códigos añade trabajo sin quitar ninguno. Tampoco conviene etiquetarlo todo de golpe: se empieza por lo que más rota y se amplía cuando el equipo ya lee sin pensar. El lector es solo la puerta de entrada; el orden lo pone lo que hay detrás, sea el <a href="/servicios/software-de-gestion/inventario-en-varios-almacenes">inventario por ubicaciones</a>, el <a href="/servicios/software-de-gestion/tpv">punto de venta</a> o, en alimentación y cosmética, el control de <a href="/servicios/software-de-gestion/lotes-trazabilidad-y-caducidades">lotes y caducidades</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo saber si mi negocio necesita un sistema de etiquetas y lectores?", "Fíjate en dónde se producen los errores. Si vienen de confundir artículos parecidos, de precios mal marcados o de recuentos que no cuadran, identificar cada producto con un código los reduce de raíz. Si tus fallos son de otro tipo, no es la prioridad."),
  ("¿Se puede empezar a usar códigos de barras sin cerrar la tienda?", "Sí. Lo habitual es etiquetar por familias, empezando por la que más se vende, mientras el resto sigue como hasta ahora. Durante un tiempo conviven artículos con código y sin él, y el programa admite las dos formas de localizarlos."),
 ],
}

# Estructura: cuatro malentendidos en tarjetas + preguntas numeradas para el proveedor del programa + aviso de que no somos asesoría
D["servicios/software-de-gestion/factura-electronica-b2b"] = {
 "estructura": "cuatro-malentendidos-en-tarjetas + preguntas-al-proveedor-del-programa + aviso-no-asesoria",
 "lead": "Has oído que el PDF por correo tiene los días contados y no sabes si tu programa actual servirá ni qué tienes que pedirle. Para la factura electrónica B2B obligatoria necesitas un programa preparado para emitir, recibir e informar del pago; aquí lo aclaramos sin alarmismo.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Sin alarmismo</p><h2>¿Qué se suele entender mal de la facturación electrónica entre empresas?</h2><p class="lead" style="margin-top:8px">Cuatro frases que oímos a autónomos y pymes, y lo que hay detrás de cada una.</p></div>
<div class="rejilla">
<div class="tarjeta"><h3>«Ya mando mis facturas por email, así que cumplo»</h3><p>Un PDF adjunto es un documento para que lo lea una persona. Lo que pide la norma es un fichero de datos que lea el programa de tu cliente, enviado por un canal autorizado.</p></div>
<div class="tarjeta"><h3>«Con Verifactu ya lo tengo resuelto»</h3><p>Son dos obligaciones distintas. Una afecta a cómo registras lo que facturas; la otra, a cómo lo intercambias con otras empresas.</p></div>
<div class="tarjeta"><h3>«Vendo a particulares, no va conmigo»</h3><p>Al emitir, puede que no. Pero tus proveedores sí te facturan como empresa o profesional, y tendrás que poder recibir sus e-facturas.</p></div>
<div class="tarjeta"><h3>«Queda mucho, ya lo miraré»</h3><p>La parte técnica es rápida; lo lento es ordenar datos de clientes, hábitos de cobro y acuerdos con proveedores. Eso no depende de la fecha.</p></div>
</div>
<h3 style="margin-top:28px">Cinco preguntas para quien te vende el programa de facturación</h3>
<ol style="max-width:820px">
<li>¿Va a emitir en formato estructurado, y por qué vía lo enviará?</li>
<li>¿Podrá recibir las facturas de mis proveedores sin que yo las teclee?</li>
<li>¿Cómo se comunica el estado de pago: a mano o al registrar el cobro?</li>
<li>¿Para cuándo estará disponible y cómo lo podré probar antes?</li>
<li>¿Qué pasa con mi histórico si al final tengo que cambiar de herramienta?</li>
</ol>
<p style="max-width:820px">Si no obtienes respuestas claras, es una señal para ir mirando alternativas con calma y no en el último trimestre.</p>
<p style="max-width:820px">Una aclaración necesaria: no somos asesoría fiscal. Las fechas y los obligados están recogidos más abajo y en la página de <a href="/normativas">normativas y plazos</a>, y tu caso concreto conviene confirmarlo con tu gestor. Lo nuestro es la herramienta: que la misma factura que ya haces con <a href="/servicios/software-de-gestion/facturacion-con-verifactu">Verifactu</a> salga también en electrónico y que tu despacho reciba los datos por la <a href="/servicios/software-de-gestion/conexion-con-tu-asesoria">conexión con la asesoría</a>. Si lo que estás eligiendo es un sistema completo, lo tratamos en <a href="/servicios/erp-para-pymes/facturacion-con-verifactu-y-factura-electronica-b2b">ERP con Verifactu y factura electrónica</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo saber si mi programa de facturación está preparado para la factura electrónica B2B?", "Pregunta a tu proveedor tres cosas: si generará el fichero estructurado, por qué canal lo enviará y recibirá, y cómo informará del estado de pago. Si la respuesta es vaga o remite a «una futura versión» sin fecha, pide un compromiso por escrito."),
  ("¿Tengo que cambiar de programa para emitir facturas electrónicas a otras empresas?", "No necesariamente. Si tu herramienta actual va a incorporar emisión, recepción y estado de pago, puedes seguir con ella. El cambio solo tiene sentido si no lo hará o si ya tenías otros motivos para cambiar."),
  ("¿Cuándo conviene empezar a prepararse para la facturación electrónica obligatoria?", "Cuanto antes en lo que no depende del calendario: datos fiscales de clientes revisados, cobros bien registrados y proveedores consultados. La parte del programa se activa cuando toque, pero llegar con los datos ordenados evita las prisas."),
 ],
}

# Estructura: tabla por situación «fichador suelto o integrado» + escena del doble apunte + lo que no cambia
D["servicios/software-de-gestion/fichador-y-registro-de-jornada"] = {
 "estructura": "tabla-por-situacion-suelto-o-integrado + escena-del-doble-apunte + lo-que-no-cambia-al-integrar",
 "lead": "Fichas en una aplicación, apuntas las horas de cada obra en otra y a final de mes alguien intenta que las dos cuadren. Con el registro de jornada y el fichaje conectado a tu gestión, la hora que marca el trabajador sirve también para saber qué cuesta cada trabajo.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Dos caminos</p><h2>¿Fichador suelto o dentro del programa? Depende de para qué quieras las horas</h2></div>
<p style="max-width:820px">Si solo necesitas dejar constancia de la entrada y la salida, un control horario independiente es suficiente y más sencillo. Si además esas horas tienen que acabar en una factura, en el coste de una obra o en una nómina con extras, integrarlo te ahorra apuntarlas dos veces.</p>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Tu situación</th><th>Lo que te conviene</th><th>Dónde lo explicamos</th></tr></thead><tbody>
<tr><td>Quieres cumplir con el registro horario y nada más</td><td>Un fichador sencillo, sin más módulos</td><td><a href="/servicios/fichador">Fichador y control horario</a></td></tr>
<tr><td>Facturas por horas o repartes mano de obra entre trabajos</td><td>Que fichaje y partes compartan datos</td><td>Esta página</td></tr>
<tr><td>Pagas extras o llevas bolsa de horas</td><td>Reglas de cálculo y un resumen para la gestoría</td><td><a href="/servicios/fichador/horas-extra">Horas extra</a></td></tr>
<tr><td>Trabajas con turnos rotativos</td><td>Un cuadrante que se compare con lo fichado</td><td><a href="/servicios/software-de-gestion/turnos-vacaciones-y-ausencias">Turnos, vacaciones y ausencias</a></td></tr>
</tbody></table></div>
<h3 style="margin-top:28px">El doble apunte, la señal más clara</h3>
<p style="max-width:820px">Imagina una empresa de montaje de cocinas. El operario marca su entrada a las ocho en el móvil y, por la tarde, escribe en una hoja: «tres horas en la calle Mayor, cuatro en el chalé». El lunes, administración copia esa hoja en el programa para imputar las horas a cada pedido. Son los mismos minutos, registrados tres veces por dos personas, y nunca suman igual. Cuando el fichaje vive dentro de la gestión, el operario indica en qué trabajo está y el resto se calcula.</p>
<h3 style="margin-top:28px">Lo que no cambia por integrarlo</h3>
<p style="max-width:820px">La obligación de registrar la jornada es la misma con una herramienta u otra, y el trabajador tiene que saber qué se anota y para qué. Integrar el fichaje no convierte el programa en un sistema de vigilancia ni resuelve por sí solo un conflicto laboral: aporta un registro ordenado. Los detalles del registro (pausas, correcciones, conservación) están tratados en las páginas del fichador para no repetirlos aquí; lo específico de esta opción es que las horas alimentan después la <a href="/servicios/software-de-gestion/rentabilidad-por-cliente-servicio-y-empleado">rentabilidad por cliente y servicio</a>.</p>
</div></section>""",
 "faq": [
  ("¿Qué ventaja tiene fichar dentro del programa de gestión en lugar de con una app aparte?", "Que las horas se apuntan una sola vez. El mismo registro sirve para el control de jornada, para imputar la mano de obra a cada trabajo y para calcular extras, sin copiar datos de una herramienta a otra ni cuadrar hojas a final de mes."),
  ("¿Puedo empezar con un fichador sencillo y conectarlo más adelante a la gestión?", "Es un planteamiento razonable cuando la urgencia es el registro horario y el resto puede esperar. En el diagnóstico revisamos qué datos convendría recoger desde el primer día para que el paso posterior no obligue a empezar de cero."),
 ],
}

# Estructura: recorrido del cliente en cuatro etapas (lista numerada) + cita del dueño + antes de regalar nada
D["servicios/software-de-gestion/fidelizacion-y-bonos"] = {
 "estructura": "recorrido-del-cliente-en-cuatro-etapas + cita-del-dueno + antes-de-regalar-nada",
 "lead": "El cliente salió contento, dijo que volvería y no ha vuelto: no pasó nada malo, simplemente no tuvo un motivo para acordarse de ti. Un programa de fidelización de clientes con puntos y bonos le da ese motivo y te enseña quién repite y quién se está alejando.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">El recorrido de un cliente</p><h2>¿Por qué no vuelve el cliente que quedó contento?</h2></div>
<p style="max-width:820px">Porque estar satisfecho no es lo mismo que tener costumbre. Entre una compra y la siguiente pasan semanas en las que tu negocio compite con la pereza, con el local que pilla más cerca y con la oferta que le acaba de llegar al móvil.</p>
<h3 style="margin-top:26px">De la primera visita a la quinta: dónde se cae</h3>
<ol style="max-width:820px">
<li><strong>Primera compra.</strong> Paga, da las gracias y se va. No sabes cómo se llama ni cómo volver a contactarle.</li>
<li><strong>Segunda, si hay suerte.</strong> Vuelve porque pasaba por la calle. Para ti sigue siendo un desconocido.</li>
<li><strong>El hueco.</strong> Pasan dos meses. Tú no lo notas, porque nadie echa de menos a quien no tiene registrado.</li>
<li><strong>La vuelta o el adiós.</strong> O algo le recuerda que existes, o ya ha cogido la costumbre de ir a otro sitio.</li>
</ol>
<p style="max-width:820px">Una tarjeta de puntos o un club de clientes actúa en los pasos uno y tres: da una razón para identificarse y permite detectar la ausencia a tiempo.</p>
<blockquote style="max-width:820px">«Tengo clientes de toda la vida, pero no sabría decirte cuántos son ni cuándo vino cada uno por última vez.»</blockquote>
<h3 style="margin-top:26px">Antes de regalar nada, mira esto</h3>
<p style="max-width:820px">Premiar a ciegas sale caro. Si no conoces cada cuánto vuelve un cliente normal, cualquier recompensa acaba yendo a quienes habrían venido igual. Por eso lo primero es registrar las ventas con nombre, aunque sea desde el <a href="/servicios/software-de-gestion/tpv">TPV</a>, y solo después decidir el premio. Hay negocios donde un sistema de recompensas tiene poco recorrido: quien reforma un baño no repite al mes siguiente, y ahí funciona mejor incentivar la recomendación. Y recuerda que acumular saldo no basta si nadie avisa: los mensajes salen con las <a href="/servicios/software-de-gestion/campanas-de-email-y-whatsapp">campañas de email y WhatsApp</a>. Para servicios que se pagan por adelantado, lo adecuado son los <a href="/servicios/software-de-gestion/bonos-cuotas-y-suscripciones">bonos y cuotas</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo conseguir que los clientes vuelvan a mi negocio?", "Primero, sabiendo quiénes son: sin un registro de quién compra y cuándo no puedes echar de menos a nadie. Después, dándoles un motivo concreto para regresar (saldo acumulado, un detalle, un aviso oportuno) y contactando con quien lleva demasiado tiempo sin aparecer."),
  ("¿Sirve una tarjeta de puntos si mis clientes compran muy de vez en cuando?", "Poco. Los puntos funcionan con compras frecuentes: cafeterías, peluquerías, tiendas de alimentación, estética. Si tu cliente te necesita una vez cada varios años, rinde más premiar que te recomiende o mantener el contacto con avisos útiles."),
 ],
}

# Estructura: tres lunes distintos en tarjetas + lista de límites + enlaces de continuidad
D["servicios/software-de-gestion/informe-semanal-automatico-por-whatsapp-o-voz"] = {
 "estructura": "tres-lunes-en-tarjetas + lista-de-limites-del-resumen",
 "lead": "Diriges el negocio desde la furgoneta, el quirófano o la barra, y abrir el programa para revisar números es lo último que haces cada semana. El resumen semanal del negocio en el móvil te llega desde tu programa, en texto o en audio, con lo que ha cambiado.",
 "bloque": """<section class="sec sec-suave"><div class="w">
<div class="cab"><p class="kicker">Tres lunes distintos</p><h2>¿Cómo empiezas la semana: a ciegas, pidiendo datos o con ellos ya leídos?</h2></div>
<div class="rejilla">
<div class="tarjeta"><h3>El lunes sin datos</h3><p>Arrancas con la sensación de que la semana pasada «fue floja» o «fue buena». Decides con esa impresión y con el saldo del banco. Las sorpresas llegan a final de mes, cuando ya no tienen arreglo.</p></div>
<div class="tarjeta"><h3>El lunes de «pásame las ventas»</h3><p>Pides los números a administración. Alguien dedica la mañana a exportar, sumar y enviarte una hoja que abres el miércoles. Tienes información, pero cuesta horas de otra persona y llega tarde.</p></div>
<div class="tarjeta"><h3>El lunes con el resumen en el bolsillo</h3><p>A la hora que elegiste suena el móvil. Un minuto de audio mientras conduces o cinco líneas de texto: qué se vendió, quién no ha pagado, qué se sale de lo habitual. Llegas al trabajo sabiendo por dónde empezar.</p></div>
</div>
<p style="max-width:820px;margin-top:18px">La diferencia entre el segundo lunes y el tercero no es la información, que es la misma, sino quién hace el esfuerzo de prepararla. Un informe de gestión automático tiene sentido para quien dirige y no dispone de un rato tranquilo delante del ordenador.</p>
<h3 style="margin-top:28px">Lo que conviene saber antes de pedirlo</h3>
<ul class="lista" style="max-width:820px">
<li>Resume lo que está registrado. Si el viernes quedaron trabajos sin facturar, el parte de novedades no los contará.</li>
<li>Señala cambios, no los explica del todo: te dice que un cliente ha dejado de comprar, no por qué.</li>
<li>No reemplaza la revisión de fondo que haces con tu asesor cada trimestre.</li>
<li>Las primeras semanas hay que afinarlo: quitar lo que no miras y añadir lo que echas en falta.</li>
</ul>
<p style="max-width:820px">Cuando una cifra del resumen te llame la atención y quieras el detalle, lo tienes en el <a href="/servicios/software-de-gestion/cuadro-de-mando-en-tiempo-real">cuadro de mando</a>. El asistente que lo redacta es <a href="/servicios/pix">IA empresarial</a>, al que también puedes preguntar por escrito. Y si tus datos viven en otros programas que no son el nuestro, existe la versión independiente del <a href="/servicios/automatizacion-y-datos/informe-semanal-por-whatsapp-o-voz">informe semanal por WhatsApp o voz</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo recibir un resumen de mi negocio en el móvil sin entrar al programa?", "Se elige qué datos interesan, a quién se envían y qué día y a qué hora. A partir de ahí el programa prepara el resumen con lo registrado esa semana y lo manda por WhatsApp como texto, como nota de voz o de las dos formas."),
  ("¿Qué pasa si esa semana faltan datos por registrar?", "El resumen reflejará solo lo que haya en el programa, así que las cifras saldrán más bajas de lo real. Por eso conviene acordar con el equipo un día de cierre semanal (por ejemplo, facturar y cerrar partes antes del envío) para que el informe sea fiable."),
 ],
}

# Estructura: diálogo de la llamada entre tiendas + lista de lo que esconde + primeras dos semanas paso a paso
D["servicios/software-de-gestion/inventario-en-varios-almacenes"] = {
 "estructura": "dialogo-de-la-llamada + lo-que-esconde + primeras-dos-semanas",
 "lead": "«¿Te queda de esto en la otra tienda?» Si la respuesta exige una llamada y a alguien yendo a mirar la estantería, tu stock no está controlado: está repartido. Un programa de inventario para varios almacenes te dice qué hay en cada local, nave o furgoneta sin preguntar a nadie.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">La llamada de todos los días</p><h2>¿Cuánto tiempo pierde tu equipo preguntando qué hay en el otro almacén?</h2></div>
<blockquote style="max-width:820px">—¿Os queda esmalte blanco satinado de cuatro litros?<br>—Creo que había un par de botes. Espera, que voy a mirar.<br>—Date prisa, que tengo al cliente delante.</blockquote>
<p style="max-width:820px">La conversación dura tres minutos y ocupa a dos personas. Si el compañero no coge el teléfono, el cliente se marcha con un «llámeme cuando lo sepa». Multiplica esa escena por las veces que ocurre en una semana y tendrás una idea de lo que cuesta no ver las existencias de cada punto de venta.</p>
<h3 style="margin-top:26px">Lo que esa llamada esconde</h3>
<ul class="lista" style="max-width:820px">
<li><strong>Mercancía duplicada «por si acaso».</strong> Como nadie se fía de lo que hay en la otra sede, cada una guarda de todo.</li>
<li><strong>Ventas que no se hacen.</strong> El artículo estaba a diez kilómetros, pero en el mostrador se dijo que no quedaba.</li>
<li><strong>Compras innecesarias.</strong> Se pide al proveedor lo que dormía en una estantería de la nave.</li>
<li><strong>Furgonetas convertidas en almacenes secretos.</strong> Lo que se carga y no se usa desaparece de las cuentas.</li>
</ul>
<h3 style="margin-top:26px">Las dos primeras semanas, paso a paso</h3>
<ol style="max-width:820px">
<li>Haz la lista de ubicaciones reales, incluidas trastiendas y vehículos.</li>
<li>Cuenta primero solo lo que más se mueve; el resto puede esperar.</li>
<li>Pon una regla que entienda todo el mundo: nada cambia de sitio sin un traspaso.</li>
<li>Nombra a una persona responsable por ubicación.</li>
<li>A los quince días, compara lo que dice la pantalla con lo que hay en tres estanterías elegidas al azar.</li>
</ol>
<p style="max-width:820px">Si en esa comprobación las cifras coinciden, el control de existencias multialmacén ya está funcionando y puedes ampliar al resto de artículos. Si no, el fallo casi siempre está en el punto tres. Para leer en lugar de teclear, se apoya en las <a href="/servicios/software-de-gestion/etiquetas-codigos-de-barras-y-qr">etiquetas con código de barras</a>; lo que falte se repone con los <a href="/servicios/software-de-gestion/pedidos-a-proveedores">pedidos a proveedores</a>; y la guía de <a href="/guias/erp-para-logistica-y-almacen">ERP para logística y almacén</a> da una visión más amplia.</p>
</div></section>""",
 "faq": [
  ("¿Cómo controlar el stock de dos tiendas y un almacén a la vez?", "Tratando cada sitio como una ubicación dentro del mismo programa. Las ventas descuentan de la tienda donde se hacen, las compras entran donde se reciben y lo que viaja de un lugar a otro se registra como traspaso. Así cualquier empleado ve qué hay en cada punto."),
  ("¿Hay que cerrar unos días para empezar a llevar el inventario por ubicaciones?", "No es necesario. Se puede arrancar con un recuento parcial de los artículos de más movimiento y completar el resto por zonas en las semanas siguientes, sin interrumpir la venta."),
 ],
}

# Estructura: simulacro de retirada con cronómetro + tabla de mínimos por actividad + aviso sobre normativa
D["servicios/software-de-gestion/lotes-trazabilidad-y-caducidades"] = {
 "estructura": "simulacro-con-cronometro + tabla-minimos-por-actividad + aviso-normativa",
 "lead": "Un proveedor te avisa de que una partida ha salido mal y necesitas saber, ya, a qué clientes se la serviste; con albaranes en papel eso son horas, si es que se consigue. Un software de trazabilidad por lotes y caducidades responde con una búsqueda y evita vender lo caducado.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Un simulacro con cronómetro</p><h2>Si mañana hubiera que retirar un producto, ¿cuánto tardarías en saber quién lo tiene?</h2><p class="lead" style="margin-top:8px">No hace falta esperar a que ocurra. Puedes ensayarlo esta semana con lo que tienes ahora.</p></div>
<ol style="max-width:820px">
<li>Elige un producto que recibiste hace unas tres semanas.</li>
<li>Localiza el albarán de entrada y anota el número de lote y el proveedor.</li>
<li>Intenta listar a quién se vendió o en qué elaboraciones se usó.</li>
<li>Para el cronómetro cuando tengas la lista completa, o cuando te rindas.</li>
</ol>
<p style="max-width:820px">Si has tardado minutos, tu sistema de seguimiento funciona, sea cual sea. Si has tardado una mañana o no has podido terminar, ya sabes lo que pasaría en una alerta real, con el teléfono sonando y la mercancía todavía en casa del cliente.</p>
<h3 style="margin-top:28px">Lo mínimo que conviene anotar según tu actividad</h3>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Actividad</th><th>Registro imprescindible</th><th>Lo que suele faltar</th></tr></thead><tbody>
<tr><td>Obrador o cocina que elabora</td><td>El lote de cada materia prima que entra en la receta</td><td>La relación entre ingrediente y producto terminado</td></tr>
<tr><td>Distribuidora o mayorista</td><td>Qué lote sale en cada albarán</td><td>Las devoluciones, que vuelven sin identificar</td></tr>
<tr><td>Tienda con producto fresco</td><td>La fecha de caducidad de cada entrada</td><td>Una lista de lo que vence esta semana</td></tr>
<tr><td>Taller o industria con componentes</td><td>Lote o número de serie de la pieza montada</td><td>En qué equipo acabó instalada</td></tr>
</tbody></table></div>
<p style="max-width:820px;margin-top:18px">El control de fechas de vencimiento tiene además un efecto que se nota en la cuenta de resultados: se tira menos, porque sale antes lo que antes caduca y las rebajas se hacen a tiempo.</p>
<p style="max-width:820px">Qué estás obligado a registrar exactamente lo marca la normativa de tu sector y, si lo tienes, tu responsable de calidad; nosotros ponemos la herramienta para que ese registro no dependa de papeles. En hostelería y alimentación se completa con el <a href="/servicios/software-especializado/appcc-digital-para-hosteleria-y-alimentacion">APPCC digital</a>, y en cualquier almacén gana rapidez con las <a href="/servicios/software-de-gestion/etiquetas-codigos-de-barras-y-qr">etiquetas con código</a> y el <a href="/servicios/software-de-gestion/inventario-en-varios-almacenes">inventario por ubicaciones</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo llevar la trazabilidad de los productos en una empresa pequeña?", "Anotando el lote en dos momentos: cuando la mercancía entra y cuando sale hacia el cliente o hacia una elaboración. Con esos dos apuntes enlazados ya se puede reconstruir el camino en ambos sentidos. Un programa lo hace sin duplicar trabajo porque usa los albaranes que ya registras."),
  ("¿Cuánto trabajo añade registrar los lotes en el día a día?", "Unos segundos por entrada si se lee la etiqueta del proveedor, algo más si hay que teclear. En la salida, el programa propone el lote que toca. Las primeras semanas se nota; después forma parte de recibir y preparar pedidos."),
 ],
}

# Estructura: cita del cliente que reclama + consecuencias + cuatro cosas que mirar antes de contratar (tarjetas) + cuándo vale el calendario del móvil
D["servicios/software-de-gestion/mantenimientos-programados"] = {
 "estructura": "cita-del-cliente-que-reclama + cuatro-criterios-en-tarjetas + cuando-vale-el-calendario",
 "lead": "El cliente llama enfadado porque este año nadie ha pasado a revisar su caldera, y tiene razón: la visita estaba en una hoja que solo abría un compañero. Un software de mantenimiento preventivo programado crea cada revisión en su fecha y te avisa de las que se quedan sin hacer.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Lo que firmaste y lo que hiciste</p><h2>¿Cuántas revisiones de tus contratos se quedan cada año sin hacer?</h2></div>
<blockquote style="max-width:820px">«Pago la cuota todos los meses y aquí no ha venido nadie desde el verano pasado.»</blockquote>
<p style="max-width:820px">Si no sabes contestar a la pregunta del titular, ese es el problema. Una empresa de climatización, ascensores, extintores o piscinas vive de contratos que prometen visitas periódicas. Cuando una se salta, no suena ninguna alarma: el cliente sigue pagando hasta que tiene una avería, repasa los papeles y descubre que la revisión de primavera nunca se hizo.</p>
<p style="max-width:820px">A partir de ahí pierdes dos veces. Pierdes la renovación, porque ya no confía, y pierdes la discusión sobre quién paga la reparación, porque no puedes enseñar un parte firmado.</p>
<h3 style="margin-top:28px">Cuatro cosas que mirar antes de contratar un programa de mantenimiento</h3>
<div class="rejilla">
<div class="tarjeta"><h3>Que parta del contrato, no de la agenda</h3><p>Las visitas deben nacer de lo pactado con cada cliente. Si hay que crearlas a mano, se seguirán olvidando.</p></div>
<div class="tarjeta"><h3>Que enseñe lo no hecho</h3><p>Importa menos el calendario de la semana que el listado de revisiones vencidas y sin cerrar.</p></div>
<div class="tarjeta"><h3>Que guarde la prueba</h3><p>Fecha, técnico, comprobaciones y firma. Es lo que enseñarás cuando alguien dude.</p></div>
<div class="tarjeta"><h3>Que avise de las renovaciones</h3><p>Un contrato que vence sin que nadie llame es un cliente que se va en silencio.</p></div>
</div>
<h3 style="margin-top:28px">Cuándo te vale con el calendario del móvil</h3>
<p style="max-width:820px">Con una veintena de clientes y un único técnico, unas citas repetidas en el calendario cumplen. El plan de mantenimiento informatizado compensa cuando los contratos se cuentan por decenas, cuando hay varias personas saliendo a la calle o cuando tus clientes te exigen justificantes. En ese caso, el técnico cierra cada visita desde la <a href="/servicios/software-de-gestion/app-para-tecnicos-de-campo">app de campo</a> y las cuotas se giran con las <a href="/servicios/software-de-gestion/remesas-y-domiciliaciones">remesas</a>. Si lo que mantienes son instalaciones sujetas a inspección, mira también el <a href="/servicios/software-especializado/registro-de-mantenimientos-obligatorios">registro de mantenimientos obligatorios</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo organizar las revisiones periódicas de muchos clientes sin que se olvide ninguna?", "Dando de alta cada contrato con su periodicidad y dejando que el programa genere la orden cuando toca. Lo decisivo es revisar cada semana el listado de visitas vencidas: ahí aparecen las que se han quedado atrás antes de que el cliente las reclame."),
  ("¿Sirve también para el mantenimiento de mis propias máquinas?", "El planteamiento es el mismo: cada equipo con su periodicidad, su lista de comprobaciones y su historial. Cambia que no hay contrato ni cuota que facturar. En el diagnóstico vemos si te basta con este módulo o necesitas algo más específico de planta."),
 ],
}

# Estructura: tabla-línea de tiempo de un extra que nadie apuntó + lo que el programa no puede saber
D["servicios/software-de-gestion/obras-y-proyectos-presupuesto-frente-a-real"] = {
 "estructura": "linea-de-tiempo-del-extra-no-apuntado + lo-que-el-programa-no-puede-saber",
 "lead": "La reforma parecía buena sobre el papel y, al sumar materiales, horas y los cambios que pidió el cliente a mitad de trabajo, apenas ha dejado nada. Con un control de obras que compara presupuesto frente a coste real ves la desviación cuando aún puedes corregirla o cobrarla.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">El extra que nadie apuntó</p><h2>¿Cómo controlar las desviaciones de una obra cuando el cliente cambia cosas sobre la marcha?</h2><p class="lead" style="margin-top:8px">Apuntando cada cambio el día que se pide, con su coste, antes de ejecutarlo. Parece obvio y casi nadie lo hace, porque en la obra no hay dónde apuntarlo.</p></div>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Momento</th><th>Lo que suele ocurrir</th><th>Lo que debería quedar escrito</th></tr></thead><tbody>
<tr><td>El cliente dice «ya que estáis, moved ese enchufe»</td><td>El oficial lo hace de buena fe y sigue con lo suyo</td><td>Un trabajo adicional, descrito, valorado y aceptado por el cliente</td></tr>
<tr><td>Falta material y se compra en el almacén del barrio</td><td>El ticket acaba en la guantera</td><td>La compra, asignada a esa obra el mismo día</td></tr>
<tr><td>Una partida se alarga dos jornadas</td><td>Nadie lo comenta hasta la liquidación</td><td>Las horas de más, visibles esa misma semana</td></tr>
<tr><td>Se entrega el trabajo</td><td>Se factura lo presupuestado al principio</td><td>Una factura que incluye lo ampliado, con su conformidad</td></tr>
</tbody></table></div>
<p style="max-width:820px;margin-top:18px">Ninguno de esos cuatro momentos es grave por separado. Juntos explican por qué tantas empresas de reformas, instalaciones y carpintería trabajan mucho y ganan poco: el sobrecoste existe, pero se descubre cuando ya está pagado. El seguimiento económico de un proyecto sirve precisamente para que la mala noticia llegue pronto, que es cuando todavía tiene solución.</p>
<h3 style="margin-top:28px">Lo que el programa no puede saber</h3>
<p style="max-width:820px">Un sistema de control de costes compara lo previsto con lo anotado. Si las horas no se imputan a cada obra, si las facturas de material se registran «a gastos generales» o si los extras se pactan de palabra, la pantalla mostrará un margen que no existe. Por eso la implantación empieza por tres hábitos y no por los informes: las horas, con los <a href="/servicios/software-de-gestion/ordenes-y-partes-de-trabajo-con-firma-y-fotos">partes de trabajo firmados</a>; las compras, imputadas al recibirlas; y los cambios, por escrito. Tampoco arregla un presupuesto que nació corto: eso se trabaja antes, con los <a href="/servicios/software-de-gestion/presupuestos-desde-mediciones">presupuestos desde mediciones</a>. Para una visión general del sector, consulta la guía de <a href="/guias/software-a-medida-para-construccion">software para construcción</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo cobrar los extras de una obra sin discutir con el cliente?", "Registrando cada ampliación en el momento en que se pide, con descripción e importe, y obteniendo su conformidad antes de hacerla. Cuando llega la factura final, el cliente reconoce lo que aceptó y no hay nada que negociar de memoria."),
  ("¿Cuándo debo revisar si una obra se está desviando?", "Cada semana, mientras está en curso. Una revisión mensual llega tarde en trabajos que duran pocas semanas. Basta con mirar qué partidas han consumido más de lo previsto para su grado de avance y decidir qué hacer con ellas."),
 ],
}

# Estructura: cuenta de horas de acogida (lista numerada simple) + lo que no hace el asistente + si incorporas a alguien cada dos años
D["servicios/software-de-gestion/onboarding-con-ia"] = {
 "estructura": "cuenta-de-horas-de-acogida + lo-que-no-hace-el-asistente + caso-pocas-incorporaciones",
 "lead": "Cada vez que entra alguien nuevo, tu persona más veterana deja su trabajo para explicar lo mismo que explicó hace tres meses, y aun así la mitad se olvida. Un onboarding de empleados con IA ofrece una acogida guiada: pasos claros por puesto y un asistente que responde con tus manuales.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Lo que cuesta enseñar</p><h2>¿Cuántas horas de tu mejor empleado se van en acoger a cada incorporación?</h2></div>
<p style="max-width:820px">Casi nadie lo ha calculado, porque no aparece en ninguna factura. Se nota en otra parte: en el encargado que no llega a lo suyo durante dos semanas y en el recién llegado que pregunta lo mismo a tres personas y recibe tres respuestas.</p>
<ol style="max-width:820px">
<li>Cuenta las personas que entraron el último año, incluidos refuerzos de temporada y sustituciones.</li>
<li>Estima las horas que alguien con experiencia dedicó a cada una durante sus primeros días.</li>
<li>Anota cuántas de esas personas siguen en la empresa.</li>
</ol>
<p style="max-width:820px">Las dos primeras cifras te dicen cuánto tiempo cualificado gastas en repetir explicaciones. La tercera, cuánto de ese esfuerzo se marchó por la puerta. En hostelería, ayuda a domicilio, comercio o logística, donde la rotación es alta, la suma suele justificar por sí sola un plan de bienvenida ordenado.</p>
<h3 style="margin-top:28px">Lo que no le dejamos hacer al asistente</h3>
<ul class="lista" style="max-width:820px">
<li>Contestar de memoria: se configura para responder con tus documentos y, si algo no está en ellos, decirlo y remitir al responsable.</li>
<li>Interpretar el contrato, el convenio o una nómina. Esas dudas van a una persona.</li>
<li>Evaluar al trabajador o decidir si supera el periodo de prueba.</li>
<li>Sustituir el recibimiento: el primer día alguien le enseña el sitio y le presenta al equipo.</li>
</ul>
<h3 style="margin-top:28px">Si incorporas a una persona cada dos años</h3>
<p style="max-width:820px">Entonces te basta una lista impresa y una buena conversación. El proceso de incorporación con inteligencia artificial compensa cuando las entradas se repiten y los procedimientos ya están escritos, aunque sea en documentos sueltos. Si aún no lo están, ese es el primer paso, y te servirá igualmente para el <a href="/servicios/agentes-de-ia/asistente-interno-de-procedimientos">asistente interno de procedimientos</a> que consulta toda la plantilla. Los papeles que firma el nuevo se archivan en la <a href="/servicios/software-de-gestion/documentacion-del-empleado">documentación del empleado</a>, y para cursos con evaluación existe la <a href="/servicios/software-especializado/plataforma-de-formacion-interna-lms">plataforma de formación interna</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo hacer la acogida de un empleado nuevo sin departamento de recursos humanos?", "Con una lista de pasos por puesto que cualquiera pueda seguir: qué firma, qué accesos recibe, a quién acompaña y qué debe saber hacer al final de la primera semana. El programa reparte esas tareas y avisa si alguna se retrasa, de modo que no dependa de quién esté libre ese día."),
  ("¿Se siente peor atendido un trabajador nuevo si le responde una IA?", "No, si la IA resuelve lo práctico y las personas hacen el resto. Poder preguntar sin apuro dónde se guarda algo o cómo se pide un día libre quita vergüenza al recién llegado. Lo que no debe faltar es alguien de carne y hueso que le reciba y le pregunte cómo va."),
 ],
}

# Estructura: comprobación con el mes pasado (tres pasos) + glosario de cuatro palabras que se confunden
D["servicios/software-de-gestion/ordenes-y-partes-de-trabajo-con-firma-y-fotos"] = {
 "estructura": "comprobacion-con-el-mes-pasado + glosario-de-cuatro-palabras",
 "lead": "El viernes aparece en la furgoneta un taco de hojas arrugadas, dos sin firmar y una de un servicio de hace tres semanas que nadie cobró. Un programa de partes de trabajo con firma y fotos hace que cada intervención llegue a la oficina el mismo día, completa y legible.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Del talonario a la factura</p><h2>¿Cuántos trabajos terminados se te quedan sin facturar?</h2></div>
<p style="max-width:820px">Es la fuga de dinero más silenciosa en fontanería, electricidad, climatización, cerrajería o limpieza. El servicio se prestó y el cliente quedó conforme, pero el justificante no llegó a administración o llegó ilegible, y nadie emite una factura de algo que no consta.</p>
<h3 style="margin-top:26px">Compruébalo con el mes pasado</h3>
<ol style="max-width:820px">
<li>Reúne todas las hojas de servicio del mes, también las que siguen en los vehículos.</li>
<li>Busca la factura que corresponde a cada una.</li>
<li>Anota cuántos días pasaron, de media, entre el trabajo y el cobro.</li>
</ol>
<p style="max-width:820px">Las hojas sin factura son ingresos perdidos. Los días de espera son dinero tuyo que financia a tus clientes. Las dos cifras bajan cuando el albarán de servicio digital viaja solo a la oficina en el momento de la firma.</p>
<h3 style="margin-top:26px">Cuatro palabras que se confunden</h3>
<dl style="max-width:820px">
<dt><strong>Orden de trabajo</strong></dt><dd>El encargo antes de hacerse: a quién, dónde, qué hay que hacer y quién va. La crea la oficina.</dd>
<dt><strong>Parte de trabajo</strong></dt><dd>El relato de lo que se hizo de verdad: tiempo, materiales, observaciones. Lo rellena quien ejecuta.</dd>
<dt><strong>Albarán</strong></dt><dd>El documento que acredita una entrega de mercancía. En servicios, muchas empresas llaman así al propio parte.</dd>
<dt><strong>Conforme</strong></dt><dd>La firma con la que el cliente acepta lo realizado. Sin ella, cualquier reclamación posterior es tu palabra contra la suya.</dd>
</dl>
<p style="max-width:820px">Tener claros estos cuatro documentos ayuda a decidir qué necesitas. Si tu equipo pasa la jornada entre avisos y además hay que organizarle el día, la herramienta completa es la <a href="/servicios/software-de-gestion/app-para-tecnicos-de-campo">app para técnicos de campo</a>. Si los trabajos nacen de un presupuesto aceptado, enlaza con los <a href="/servicios/software-de-gestion/presupuestos-que-pasan-a-pedido-y-factura">presupuestos que pasan a pedido y factura</a>. Y las horas que recoge cada parte son la base para calcular la <a href="/servicios/software-de-gestion/rentabilidad-por-cliente-servicio-y-empleado">rentabilidad por cliente y servicio</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo dejar de perder partes de trabajo en papel?", "Haciendo que el parte se rellene y se firme en el móvil. En cuanto el operario lo cierra, la oficina lo tiene y el cliente recibe su copia, así que ya no hay hojas que transportar, descifrar ni buscar en la furgoneta."),
  ("¿Sirve un programa de partes si trabajo solo o con un ayudante?", "Puede servir, sobre todo para facturar el mismo día y conservar fotos y firmas por si hay una reclamación. Si haces pocos trabajos a la semana y los facturas al momento, la mejora será pequeña y quizá no compense todavía."),
 ],
}

# Estructura: tabla de cuatro formas de pedir + tres preguntas para la semana que falte esa persona + cuándo vale lo que tienes
D["servicios/software-de-gestion/pedidos-a-proveedores"] = {
 "estructura": "tabla-cuatro-formas-de-pedir + preguntas-si-falta-la-persona-que-pide + cuando-vale-lo-que-tienes",
 "lead": "En tu negocio hay una persona que «sabe pedir»: cuánto, a quién y qué día reparte cada uno. Funciona hasta que se va de vacaciones. La gestión de pedidos a proveedores y compras saca ese conocimiento de su cabeza y lo convierte en propuestas que cualquiera puede revisar.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Cuatro formas de comprar</p><h2>¿Qué pasa con tus compras el día que falta quien las hace?</h2></div>
<p style="max-width:820px">En la mayoría de pequeños negocios, el aprovisionamiento es un oficio que nadie ha escrito. Quien lo lleva conoce de memoria los días de reparto, el pedido mínimo de cada casa y qué se agota antes de un puente. Es valioso, y también frágil.</p>
<blockquote style="max-width:820px">«Eso pregúntaselo a Antonio, que es el que pide. Vuelve el día quince.»</blockquote>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Cómo se pide</th><th>Funciona mientras…</th><th>Se rompe cuando…</th></tr></thead><tbody>
<tr><td>De memoria, dando una vuelta por el almacén</td><td>Hay pocos artículos y siempre compra la misma persona</td><td>Esa persona falta o el surtido crece</td></tr>
<tr><td>Por teléfono o WhatsApp con cada comercial</td><td>Los encargos son pequeños y de confianza</td><td>Hay que demostrar qué se encargó y a qué precio</td></tr>
<tr><td>Con una hoja de mínimos</td><td>Alguien la actualiza a diario</td><td>Las ventas dejan de anotarse un par de días</td></tr>
<tr><td>Con propuestas que genera el programa</td><td>Entradas y salidas se registran</td><td>Los datos de partida (mínimos, plazos) están sin revisar</td></tr>
</tbody></table></div>
<h3 style="margin-top:28px">Tres preguntas para la próxima semana que esa persona libre</h3>
<ol style="max-width:820px">
<li>¿Quién sabría qué encargar el lunes, y en qué se basaría?</li>
<li>¿Dónde está escrito el precio que se acordó con cada proveedor?</li>
<li>Cuando llegue el camión, ¿cómo comprobaría alguien que viene todo lo solicitado?</li>
</ol>
<p style="max-width:820px">Si las tres respuestas son «habría que llamarle», tu sistema de reposición depende de un móvil encendido en la playa.</p>
<h3 style="margin-top:28px">Cuándo te vale con lo que tienes</h3>
<p style="max-width:820px">Un negocio con dos o tres suministradores y entregas fijas no necesita un módulo de compras: una rutina semanal clara es suficiente. Empieza a compensar cuando trabajas con muchas referencias, cuando el género tiene caducidad o cuando un faltante te hace perder ventas. Para que las propuestas sean fiables hace falta que el <a href="/servicios/software-de-gestion/inventario-en-varios-almacenes">inventario</a> esté al día; si la demanda cambia mucho con la temporada, ayuda la <a href="/servicios/software-de-gestion/prevision-de-stock-con-ia">previsión de stock con IA</a>; y las facturas que llegan después pueden entrar solas con la <a href="/servicios/software-de-gestion/lectura-automatica-de-facturas-de-proveedores">lectura automática</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo organizar las compras a proveedores en un negocio pequeño?", "Escribiendo lo que hoy se sabe de memoria: qué artículos se compran a quién, con qué plazo llega cada uno y cuál es la cantidad por debajo de la cual hay que reponer. Con esos datos en el programa, la lista de lo que toca encargar sale sola y cualquiera puede revisarla."),
  ("¿Qué datos tengo que mantener al día para que el programa proponga bien los pedidos?", "Tres: las existencias reales, el stock mínimo de cada artículo y el plazo de entrega de su proveedor. Si alguno está desfasado, la propuesta fallará por exceso o por defecto, así que conviene repasarlos al menos cada cambio de temporada."),
 ],
}

# Estructura: frases del cliente sin respuesta + tres preguntas de un minuto en tarjetas + decisiones que siguen siendo de una persona
D["servicios/software-de-gestion/postventa-garantias-e-incidencias"] = {
 "estructura": "frases-del-cliente-sin-respuesta + tres-preguntas-de-un-minuto + decisiones-humanas",
 "lead": "Vendiste, instalaste y cobraste; tres meses después el cliente escribe que algo falla, el mensaje lo ve quien no era y pasa una semana sin respuesta. Un software de postventa para garantías e incidencias da a cada reclamación un responsable, un plazo y un final.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Lo que dice el cliente cuando nadie le contesta</p><h2>¿Por qué una avería pequeña acaba en una mala reseña?</h2></div>
<p style="max-width:820px">Por el silencio, no por la avería. Quien compra una cocina, una caldera o un ordenador entiende que algo pueda fallar. Lo que no perdona es tener que perseguir a la empresa para que le hagan caso.</p>
<ul class="lista" style="font-size:18px;max-width:820px">
<li>«Lo dije hace dos semanas y nadie me ha llamado.»</li>
<li>«He explicado lo mismo a tres personas distintas.»</li>
<li>«Me aseguraron que lo cubría la garantía y ahora me lo quieren cobrar.»</li>
</ul>
<p style="max-width:820px;margin-top:16px">Las tres quejas tienen el mismo origen: el aviso entró por un canal cualquiera (el móvil de un montador, el correo general, una llamada) y se quedó allí. No hay mala fe, hay un servicio posventa que funciona de memoria.</p>
<h3 style="margin-top:28px">Tres cosas que tu equipo debería poder contestar en un minuto</h3>
<div class="rejilla">
<div class="tarjeta"><h3>¿Cuántas reclamaciones hay abiertas hoy?</h3><p>Si para saberlo hay que preguntar a varios compañeros, alguna está olvidada.</p></div>
<div class="tarjeta"><h3>¿Quién lleva cada una y desde cuándo?</h3><p>Un caso sin nombre al lado no es de nadie.</p></div>
<div class="tarjeta"><h3>¿Esto está cubierto o no?</h3><p>La respuesta depende de la fecha de compra, y esa fecha debería estar a un clic, no en un archivador.</p></div>
</div>
<h3 style="margin-top:28px">Decisiones que siguen siendo de una persona</h3>
<p style="max-width:820px">Un gestor de reclamaciones ordena y avisa, pero no juzga. Valorar si un daño viene de un defecto o de un mal uso, decidir un gesto comercial con un buen cliente o resolver una discrepancia sobre lo pactado requiere criterio, y a veces el consejo de tu asesor. Lo que el programa aporta es que esa decisión se tome con el historial delante y dentro de plazo. La visita de reparación se documenta con los <a href="/servicios/software-de-gestion/ordenes-y-partes-de-trabajo-con-firma-y-fotos">partes de trabajo</a>, todo queda en la <a href="/servicios/software-de-gestion/ficha-de-cliente-360">ficha del cliente</a> y, si quieres que él mismo consulte cómo va su caso, se le da acceso al <a href="/servicios/software-de-gestion/portal-del-cliente-y-del-proveedor">portal del cliente</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo gestionar las reclamaciones de clientes en una empresa pequeña?", "Con una única lista donde entra todo, llegue por donde llegue, y tres datos obligatorios en cada caso: quién lo lleva, en qué estado está y cuándo vence el plazo que te has marcado. Lo demás (fotos, piezas, visitas) se añade sobre esa base."),
  ("¿Cuándo compensa un programa de incidencias frente a una hoja compartida?", "Cuando las reclamaciones dejan de caber en la cabeza de una persona: varios técnicos, productos con periodos de cobertura distintos o clientes que preguntan por el estado de su caso. Con pocas incidencias al mes y un único responsable, una hoja bien llevada puede ser suficiente."),
 ],
}

# Estructura: escena del presupuesto de los domingos + tabla incluye / no incluye + si haces pocos presupuestos
D["servicios/software-de-gestion/presupuestos-desde-mediciones"] = {
 "estructura": "escena-presupuesto-de-domingo + tabla-incluye-no-incluye + caso-pocos-presupuestos",
 "lead": "Visitas la vivienda el martes, mides con prisa y el precio sale el domingo por la noche, después de pelearte con la calculadora; para entonces el cliente ya tiene otras dos ofertas. Un programa de presupuestos con mediciones para reformas convierte las medidas en partidas valoradas el mismo día.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">El presupuesto de los domingos</p><h2>¿Cuántas obras pierdes por tardar una semana en dar precio?</h2></div>
<p style="max-width:820px">Imagina a un reformista que hace cuatro visitas entre lunes y jueves. De cada una vuelve con medidas en una libreta, fotos en el móvil y una idea aproximada de lo que quiere el cliente. Durante el día está en obra; los presupuestos se quedan para el fin de semana. El domingo abre la hoja de cálculo, copia una oferta antigua, cambia cantidades y cruza los dedos para no haber olvidado el rodapié.</p>
<p style="max-width:820px">Ese método tiene tres costes que no aparecen en ninguna factura:</p>
<ul class="lista" style="max-width:820px">
<li><strong>Llega tarde.</strong> Cuando el interesado lo recibe, ya ha comparado y a veces ya ha decidido.</li>
<li><strong>Llega con riesgo.</strong> Una multiplicación mal hecha se convierte en semanas trabajando a pérdidas.</li>
<li><strong>Depende de una persona.</strong> Solo sabe presupuestar el dueño, que es quien menos tiempo tiene.</li>
</ul>
<h3 style="margin-top:28px">Qué pone el programa y qué sigue en tus manos</h3>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Incluye</th><th>No incluye</th></tr></thead><tbody>
<tr><td>Calcular superficies, metros lineales y unidades a partir de lo que anotas</td><td>Medir por ti: la visita y la cinta métrica siguen siendo tuyas</td></tr>
<tr><td>Valorar cada partida con tus precios unitarios</td><td>Una lista de precios ya hecha: se construye con los tuyos</td></tr>
<tr><td>Enseñarte coste y beneficio antes de enviar</td><td>Decidir qué margen quieres o cuánto descuento aceptas</td></tr>
<tr><td>Dejar un documento claro, listo para el cliente</td><td>El proyecto técnico, cuando el trabajo lo requiere</td></tr>
</tbody></table></div>
<h3 style="margin-top:28px">¿Y si hago pocos presupuestos al mes?</h3>
<p style="max-width:820px">Con dos o tres ofertas mensuales de trabajos muy distintos entre sí, la hoja de cálculo aguanta. El cálculo de presupuestos de obra automatizado compensa cuando repites tipos de trabajo (baños, cocinas, pintura, suelos), cuando quieres que otra persona pueda preparar ofertas con tus criterios o cuando ya has perdido dinero por un error de cantidades. Una vez aceptada, la oferta sirve de referencia para comparar <a href="/servicios/software-de-gestion/obras-y-proyectos-presupuesto-frente-a-real">presupuesto frente a coste real</a> y avanza hacia <a href="/servicios/software-de-gestion/presupuestos-que-pasan-a-pedido-y-factura">pedido y factura</a> sin reescribirla. Si lo que buscas es que el cliente se calcule un precio orientativo desde tu web, eso es un <a href="/servicios/software-especializado/presupuestador-y-configurador-online">presupuestador online</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo hacer presupuestos de reformas más rápido sin equivocarme en las cantidades?", "Separando lo que mides de lo que calculas. Tú introduces las dimensiones de cada estancia y el programa obtiene metros y unidades con fórmulas fijas, les aplica tus precios y suma. Al no rehacer operaciones a mano cada vez, desaparecen los errores de copia."),
  ("¿Puede preparar los presupuestos otra persona que no sea el dueño?", "Sí, y es una de las razones para ordenar el proceso. Con las partidas y los precios definidos, un encargado o alguien de oficina puede montar la oferta a partir de las medidas, y tú solo revisas el margen antes de enviarla."),
 ],
}

# Estructura: mitos y realidad en tabla de dos columnas + tres comprobaciones previas + tienda pequeña
D["servicios/software-de-gestion/prevision-de-stock-con-ia"] = {
 "estructura": "mitos-y-realidad-sobre-la-ia + tres-comprobaciones-numeradas + caso-tienda-pequena",
 "lead": "Se te agota justo lo que más sale y te sobra lo que compraste «por si acaso»: las dos cosas a la vez, cada temporada. La previsión de stock con IA para comprar mejor estima cuánto vas a necesitar de cada artículo y te propone el pedido; la decisión final sigue siendo tuya.",
 "bloque": """<section class="sec sec-suave"><div class="w">
<div class="cab"><p class="kicker">Expectativas en su sitio</p><h2>¿Puede una inteligencia artificial saber lo que vas a vender?</h2></div>
<p style="max-width:820px">No lo sabe: lo estima a partir de lo que ya vendiste. Acierta más que la intuición en lo repetitivo, porque no se cansa de mirar cientos de referencias, y acierta menos en lo excepcional, porque no puede conocer lo que nunca ha ocurrido.</p>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Lo que se suele creer</th><th>Lo que ocurre en la práctica</th></tr></thead><tbody>
<tr><td>«Con instalarla, ya acierta»</td><td>Aprende de tus ventas. Si estaban mal registradas, aprenderá mal</td></tr>
<tr><td>«Sirve igual para todo el catálogo»</td><td>Funciona mejor con artículos de salida regular que con los que se venden dos veces al año</td></tr>
<tr><td>«Sustituye a quien compra»</td><td>Le quita horas de cálculo; el criterio sobre proveedores, ofertas y novedades sigue siendo suyo</td></tr>
<tr><td>«Elimina las roturas de stock»</td><td>Las reduce. Un proveedor que falla o una moda repentina seguirán pillándote por sorpresa</td></tr>
</tbody></table></div>
<h3 style="margin-top:28px">Antes de pensar en algoritmos, tres comprobaciones</h3>
<p style="max-width:820px">Si alguna falla, el primer trabajo es arreglarla, y resulta más barato y más útil que cualquier modelo predictivo.</p>
<ol style="max-width:820px">
<li><strong>¿Cada venta lleva su artículo?</strong> Si en caja se cobra mucho como «varios», no hay histórico del que aprender.</li>
<li><strong>¿El stock de la pantalla coincide con el del estante?</strong> Una estimación de demanda sobre existencias falsas propone compras absurdas.</li>
<li><strong>¿Tienes apuntado cuánto tarda cada proveedor?</strong> Sin ese plazo, el sistema no sabe con qué antelación avisarte.</li>
</ol>
<h3 style="margin-top:28px">Si tu tienda es pequeña</h3>
<p style="max-width:820px">Con un centenar de artículos y una demanda estable, un mínimo y un máximo por referencia resuelven casi todo, y eso ya lo hace el módulo de <a href="/servicios/software-de-gestion/pedidos-a-proveedores">pedidos a proveedores</a>. El pronóstico de ventas con inteligencia artificial compensa con catálogos amplios, estacionalidad marcada o varios puntos de venta, apoyado en un <a href="/servicios/software-de-gestion/inventario-en-varios-almacenes">inventario</a> fiable. Y si tus datos de venta están en otro programa o en una tienda online ajena, se puede plantear como proyecto independiente de <a href="/servicios/automatizacion-y-datos/prevision-de-ventas-y-stock">previsión de ventas y stock</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo prever el stock de una tienda con IA?", "El sistema analiza las ventas pasadas de cada artículo, detecta sus temporadas y tendencias y calcula cuánto se venderá en las próximas semanas. Con el plazo de cada proveedor, propone qué pedir y cuándo. Tú revisas la propuesta y corriges lo que sepas que va a cambiar."),
  ("¿Qué pasa si la previsión se equivoca?", "Se equivocará a veces, como cualquier estimación. Por eso se revisa antes de comprar y se compara después con lo que realmente ocurrió, para ir ajustando. Lo razonable es exigirle que falle menos que el método anterior, no que acierte siempre."),
 ],
}

# Estructura: por qué falta caja + síntomas del día a día + cita del dueño + lo que siempre decide una persona
D["servicios/software-de-gestion/prevision-de-tesoreria"] = {
 "estructura": "beneficio-no-es-caja + sintomas-del-dia-a-dia + cita + lo-que-decide-una-persona",
 "lead": "Vendes más que hace un año y, aun así, hay semanas en las que miras la cuenta antes de pagar las nóminas. No es mala gestión: vender y cobrar no ocurren el mismo día. Una previsión de tesorería automática para pymes te enseña ese desfase con semanas de antelación.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Ganar dinero y no tenerlo</p><h2>¿Por qué falta caja si el negocio va bien?</h2></div>
<p style="max-width:820px">Porque el beneficio se calcula con lo que facturas y la liquidez depende de lo que ya has cobrado. Entre una cosa y otra hay un hueco de treinta, sesenta o noventa días en el que tú sí pagas: sueldos, alquiler, proveedores, impuestos. Cuanto más creces, más grande es ese hueco, y por eso las empresas que venden mucho también pueden ahogarse.</p>
<h3 style="margin-top:26px">Cómo se nota en el día a día</h3>
<ul class="lista" style="max-width:820px">
<li>Abres la aplicación del banco varias veces el mismo día.</li>
<li>Retrasas un pago a un proveedor «hasta que entre lo de fulano».</li>
<li>Los trimestres de impuestos y las pagas extra te pillan cada año por sorpresa, aunque caen siempre en la misma fecha.</li>
<li>Rechazas un pedido grande porque no puedes adelantar el material.</li>
<li>Usas la póliza de crédito como si fuera parte del saldo.</li>
</ul>
<blockquote style="max-width:820px">«Este mes hemos facturado más que nunca y he tenido que tirar de la póliza para pagar el trimestre.»</blockquote>
<p style="max-width:820px">Ninguno de estos síntomas se cura vendiendo más. Se cura viendo antes: un plan de caja que proyecte entradas y salidas permite mover una compra, reclamar un cobro o hablar con el banco cuando todavía hay margen para elegir.</p>
<h3 style="margin-top:26px">Lo que siempre decide una persona</h3>
<p style="max-width:820px">Una proyección de flujo de caja es un cálculo con supuestos: que los clientes pagarán en su fecha, que no habrá gastos imprevistos. Unas semanas se cumplen y otras no. El programa suma y avisa, pero qué pago se aplaza, a qué cliente se aprieta o si conviene financiarse son decisiones tuyas, y las de más calado merecen la opinión de tu asesor; nosotros no damos consejo financiero. Para que la previsión parta de datos reales conviene tener al día el <a href="/servicios/software-de-gestion/cobros-impagos-y-semaforo-de-clientes">control de cobros</a> y, si giras recibos, las <a href="/servicios/software-de-gestion/remesas-y-domiciliaciones">remesas</a>. Si tus cifras están repartidas entre varios programas y bancos, existe un servicio aparte de <a href="/servicios/automatizacion-y-datos/prevision-de-tesoreria-y-control-de-costes">previsión de tesorería y control de costes</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo saber si voy a tener dinero para pagar el mes que viene?", "Sumando al saldo de hoy lo que esperas cobrar, con su fecha, y restando lo que tienes que pagar, con la suya. Hecho semana a semana, ese cálculo muestra en qué momento el saldo baja demasiado. Un programa lo mantiene actualizado con cada factura que emites o recibes."),
  ("¿Qué diferencia hay entre beneficio y tesorería?", "El beneficio es lo que ganas sobre el papel: ventas menos gastos del periodo. La tesorería es el dinero disponible en un momento dado. Una empresa puede tener beneficios y quedarse sin efectivo si cobra tarde y paga pronto."),
 ],
}

# Estructura: dos miedos frente a frente (dos tarjetas) + cuatro comprobaciones antes de poner objetivos + equipos de dos o tres
D["servicios/software-de-gestion/productividad-y-objetivos"] = {
 "estructura": "dos-miedos-frente-a-frente + cuatro-comprobaciones + equipos-muy-pequenos",
 "lead": "Tienes la sensación de que unos tiran del carro y otros se dejan llevar, pero no podrías demostrarlo, y sacar el tema sin datos solo crea mal ambiente. Un programa de objetivos y productividad del equipo pone sobre la mesa cifras que salen del trabajo ya registrado.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Dos miedos frente a frente</p><h2>¿Se puede medir el trabajo del equipo sin que parezca desconfianza?</h2><p class="lead" style="margin-top:8px">Sí, cuando se mide lo que se produce y cada persona ve sus cifras antes que nadie. El recelo aparece cuando los números se usan por sorpresa.</p></div>
<div class="rejilla">
<div class="tarjeta"><h3>Lo que teme quien dirige</h3><p>Que el esfuerzo esté mal repartido y no enterarse. Que subir un sueldo o dar un incentivo sea injusto por falta de datos. Que plantear metas se entienda como un reproche y el buen ambiente se resienta.</p></div>
<div class="tarjeta"><h3>Lo que teme quien trabaja</h3><p>Que le midan por algo que no depende de él. Que se compare su cifra con la de un compañero que tiene clientes más fáciles. Que el indicador se convierta en excusa para apretar y nunca para reconocer.</p></div>
</div>
<p style="max-width:820px;margin-top:18px">Los dos miedos son razonables, y un sistema de evaluación del desempeño solo funciona si responde a ambos: datos que nadie tenga que rellenar aposta, metas que la persona pueda alcanzar con su propio trabajo y transparencia sobre quién ve qué.</p>
<h3 style="margin-top:28px">Cuatro comprobaciones antes de fijar la primera meta</h3>
<ol style="max-width:820px">
<li>¿El trabajo queda ya anotado en algún sitio (partes, ventas, tareas) o habría que pedir informes nuevos?</li>
<li>¿Sabrías explicar cada objetivo en una frase y decir de dónde sale la cifra?</li>
<li>¿Alcanzarlo depende de la persona, o de factores que no controla?</li>
<li>¿Tienes decidido qué harás cuando alguien se quede corto, y cuando alguien lo supere?</li>
</ol>
<p style="max-width:820px">Si la cuarta pregunta no tiene respuesta, espera: una meta sin consecuencias pensadas desgasta más que no tener ninguna.</p>
<h3 style="margin-top:28px">En un equipo de dos o tres</h3>
<p style="max-width:820px">No necesitas un panel de rendimiento: lo ves todo cada día y una conversación sincera vale más. El seguimiento de metas por empleado empieza a compensar cuando hay varios centros, turnos o mandos intermedios que deben tratar igual a personas distintas. Para el equipo de ventas, lo natural es unirlo a <a href="/servicios/software-de-gestion/comerciales-y-comisiones">comerciales y comisiones</a>; para la visión de conjunto, al <a href="/servicios/software-de-gestion/cuadro-de-mando-en-tiempo-real">cuadro de mando</a>. Y si lo que te preocupa es el margen y no la actividad, la herramienta es la <a href="/servicios/software-de-gestion/rentabilidad-por-cliente-servicio-y-empleado">rentabilidad por cliente, servicio y empleado</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo medir la productividad de los empleados sin controlarles cada minuto?", "Midiendo resultados en lugar de presencia: trabajos cerrados, ventas, tareas entregadas en plazo, incidencias resueltas. Son datos que ya genera la actividad normal en el programa, de modo que no hacen falta capturas de pantalla ni registros de teclado."),
  ("¿Conviene explicar al equipo que se van a medir objetivos antes de empezar?", "Sí, siempre. Contar qué se mide, de dónde sale cada cifra, quién la ve y para qué se usará evita la mayor parte de los recelos. Los sistemas que se implantan sin explicación suelen acabar con datos maquillados o con la plantilla en contra."),
 ],
}

# Estructura: tabla de avisos que no se dan (más allá de la cita) + tres condiciones para no molestar + desvío a citas
D["servicios/software-de-gestion/recordatorios-automaticos-por-whatsapp"] = {
 "estructura": "tabla-de-avisos-que-no-se-dan + tres-condiciones-en-tarjetas + desvio-a-citas",
 "lead": "La prenda lleva un mes lista y nadie viene a por ella, el presupuesto caduca mañana y la revisión anual se pasó hace dos semanas: avisar de todo eso a mano es un trabajo que nunca toca. Los recordatorios por WhatsApp de cobros, recogidas y entregas salen solos desde tu programa.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Más allá de la cita</p><h2>¿Qué avisos se quedan sin dar en tu negocio porque nadie tiene tiempo?</h2></div>
<p style="max-width:820px">Casi todos los que no son urgentes. En un taller, una tintorería, una óptica o una empresa de reparto, llamar al cliente para decirle que su encargo está terminado es la tarea que siempre se deja para luego. Y sin embargo cada uno de esos mensajes mueve dinero o libera espacio.</p>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Lo que habría que comunicar</th><th>Si no se comunica…</th><th>Dato que lo dispara</th></tr></thead><tbody>
<tr><td>«Tu pedido o tu reparación ya está»</td><td>Ocupa sitio en el local y el cobro se retrasa</td><td>El trabajo pasa a estado terminado</td></tr>
<tr><td>«Mañana vamos a entregar o a instalar»</td><td>No hay nadie en casa y el viaje se repite</td><td>La fecha de entrega asignada</td></tr>
<tr><td>«Tu factura vence esta semana»</td><td>Se paga tarde, a menudo por simple olvido</td><td>El vencimiento del documento</td></tr>
<tr><td>«Ya toca la revisión»</td><td>El cliente la hace en otro sitio o no la hace</td><td>La fecha de la última visita</td></tr>
<tr><td>«Te queda una sesión en el bono»</td><td>El bono se agota y nadie propone renovarlo</td><td>El saldo de sesiones</td></tr>
</tbody></table></div>
<p style="max-width:820px;margin-top:18px">La idea es que el aviso no dependa de que alguien se acuerde, sino de un dato que ya está en la gestión. La notificación automática al cliente sale cuando ese dato cambia.</p>
<h3 style="margin-top:28px">Tres condiciones para que un aviso no moleste</h3>
<div class="rejilla">
<div class="tarjeta"><h3>Que hable de algo que ya espera</h3><p>Su prenda, su entrega, su factura. Eso es gestión; una oferta es publicidad y necesita su permiso aparte.</p></div>
<div class="tarjeta"><h3>Que llegue una vez y a tiempo</h3><p>Tres mensajes para lo mismo convierten un servicio en una molestia.</p></div>
<div class="tarjeta"><h3>Que se pueda contestar</h3><p>Si responde «pasa mi hermana a recogerlo», alguien o algo tiene que leerlo.</p></div>
</div>
<h3 style="margin-top:28px">Si lo que quieres recordar son citas</h3>
<p style="max-width:820px">Entonces esta página te vale, pero hay dos más específicas: la <a href="/servicios/software-de-gestion/agenda-y-citas-online">agenda y citas online</a>, donde nace la reserva, y las <a href="/servicios/whatsapp-ia/citas-y-recordatorios-automaticos">citas y recordatorios con asistente de WhatsApp</a>, si prefieres que el cliente pueda conversar para cambiar la hora. Y cuando el aviso de pago no basta y hay que escalar, el seguimiento se lleva desde el <a href="/servicios/software-de-gestion/cobros-impagos-y-semaforo-de-clientes">semáforo de cobros</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo avisar automáticamente a un cliente de que su pedido está listo para recoger?", "Vinculando el mensaje al cambio de estado en el programa. Cuando alguien marca el encargo como terminado, sale un WhatsApp con el texto que hayas definido: qué está listo, dónde recogerlo y en qué horario. Si pasan los días sin que venga, puede salir un segundo aviso."),
  ("¿Se puede recordar un pago pendiente por WhatsApp sin resultar brusco?", "Sí, cuidando el momento y el tono. Un mensaje breve unos días antes del vencimiento, con el importe y la forma de pago, se percibe como una ayuda. Conviene reservar los textos más firmes para cuando ya ha pasado la fecha y dejar los casos delicados a una persona."),
 ],
}

# Estructura: cuatro preguntas incómodas + tres acuerdos previos en lista de definiciones + qué sale de datos incompletos
D["servicios/software-de-gestion/rentabilidad-por-cliente-servicio-y-empleado"] = {
 "estructura": "cuatro-preguntas-incomodas + tres-acuerdos-previos + datos-incompletos",
 "lead": "Trabajas más que nunca, facturas más que nunca y a final de año queda lo mismo o menos. Algún cliente, algún servicio o algún desplazamiento se está comiendo lo que ganan los demás. La rentabilidad por cliente, servicio y empleado te dice cuál, con tus propios datos.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Preguntas incómodas</p><h2>¿A qué cliente le dirías que no si supieras lo que te cuesta?</h2></div>
<p style="max-width:820px">Todo negocio de servicios tiene alguno. Suele ser el que más llama, el que siempre pide «un favorcito» y el que nadie se atreve a revisar porque factura mucho. Responde a estas cuatro preguntas sin mirar ningún papel:</p>
<ol style="max-width:820px">
<li>¿Qué cliente consume más horas de teléfono y de visitas, y qué lugar ocupa por facturación?</li>
<li>¿Qué tipo de trabajo presupuestas siempre con miedo a quedarte corto?</li>
<li>¿Cuántas horas de la semana pasada no se le cobraron a nadie?</li>
<li>¿Qué encargo aceptas «por no perder la cuenta», aunque sospechas que no sale?</li>
</ol>
<p style="max-width:820px">Si has contestado de intuición, estás decidiendo precios, contrataciones y a quién dedicas tu mejor gente sin conocer el margen por trabajo. No es raro: la contabilidad dice cuánto ganó la empresa, no con quién.</p>
<h3 style="margin-top:28px">Tres acuerdos que hay que tomar antes de calcular nada</h3>
<dl style="max-width:820px">
<dt><strong>Qué vale una hora</strong></dt><dd>No es el sueldo dividido entre las horas del mes. Hay que decidir qué costes se cargan a cada perfil y revisarlo una vez al año.</dd>
<dt><strong>Qué se hace con los kilómetros</strong></dt><dd>El tiempo de ida y vuelta, ¿es coste del cliente o del negocio? La respuesta cambia por completo el resultado de los clientes lejanos.</dd>
<dt><strong>Cómo se reparte lo que es de todos</strong></dt><dd>Alquiler, oficina, vehículos. Cualquier criterio es discutible; lo importante es elegir uno y mantenerlo para poder comparar.</dd>
</dl>
<h3 style="margin-top:28px">Qué sale cuando los datos están incompletos</h3>
<p style="max-width:820px">Un análisis de márgenes es tan bueno como lo que se apunta. Si la mitad de las horas no se imputan, los clientes parecerán más rentables de lo que son; si el material sale del almacén sin registrar, también. Por eso este módulo se apoya en dos fuentes: las horas, que vienen del <a href="/servicios/software-de-gestion/fichador-y-registro-de-jornada">fichaje conectado a la gestión</a> o de los <a href="/servicios/software-de-gestion/ordenes-y-partes-de-trabajo-con-firma-y-fotos">partes de trabajo</a>, y las compras asignadas a cada encargo. En empresas que trabajan por proyecto, el mismo cálculo se sigue obra a obra en <a href="/servicios/software-de-gestion/obras-y-proyectos-presupuesto-frente-a-real">presupuesto frente a real</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo saber qué clientes me dejan dinero y cuáles no?", "Restando a lo que factura cada cliente lo que cuesta atenderle: horas de tu equipo, material, desplazamientos y la parte de gastos generales que le asignes. Con esos datos registrados en el programa, el margen de cada uno se calcula solo y puedes ordenarlos de mayor a menor."),
  ("¿Cuánto tiempo de datos hace falta para fiarse de las cifras de rentabilidad?", "El suficiente para cubrir un ciclo normal de tu actividad. Con un solo mes, una avería o un pedido excepcional distorsionan el resultado. Lo sensato es mirar las primeras cifras como orientación y tomar decisiones de precio cuando la tendencia se repite varios meses."),
 ],
}

# Estructura: un sábado hora a hora (tabla, ejemplo hipotético de restaurante) + errores de planteamiento + sin reserva o una sola persona
D["servicios/software-de-gestion/reservas-de-mesas-salas-clases-o-servicios"] = {
 "estructura": "sabado-hora-a-hora + errores-de-planteamiento + cuando-no-hace-falta-reservar",
 "lead": "Sábado, nueve y media de la noche: la mesa de ocho no aparece, el teléfono suena en pleno servicio y en Instagram hay tres mensajes pidiendo sitio que nadie ha visto. Un software de reservas para mesas, salas y clases ordena todo eso en un único plano de disponibilidad.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Un sábado, hora a hora</p><h2>¿Cuántas reservas se te escapan mientras estás atendiendo?</h2><p class="lead" style="margin-top:8px">Ejemplo hipotético de un restaurante de barrio. Cambia «mesa» por «plaza de yoga» o «sala de reuniones» y la historia es la misma.</p></div>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Hora</th><th>Lo que ocurre hoy</th><th>Con un sistema de reservas</th></tr></thead><tbody>
<tr><td>12:30</td><td>Llaman durante la preparación del servicio. Nadie puede coger</td><td>La persona reserva desde la web y recibe su confirmación</td></tr>
<tr><td>17:00</td><td>Tres mensajes en redes sociales pidiendo mesa; se leen a las ocho</td><td>El enlace del perfil lleva al mismo plano de mesas</td></tr>
<tr><td>21:30</td><td>El grupo de ocho no se presenta y no hay a quién ofrecer el hueco</td><td>Había confirmado o dejado señal; si anula, se avisa a la lista de espera</td></tr>
<tr><td>23:45</td><td>Se apunta en la libreta una petición para mañana, con letra de cansancio</td><td>Queda registrada con nombre, teléfono y número de comensales</td></tr>
</tbody></table></div>
<blockquote style="max-width:820px;margin-top:18px">«Llamé dos veces y no lo cogía nadie, así que reservamos en otro sitio.»</blockquote>
<p style="max-width:820px">Lo que se pierde no es solo la mesa vacía. Es el cliente que llamó dos veces y acabó cenando en otro sitio, y el que escribió por la tarde y nunca supo si tenía sitio.</p>
<h3 style="margin-top:28px">Errores de planteamiento que salen caros</h3>
<ul class="lista" style="max-width:820px">
<li>Abrir todo el aforo a la misma hora y colapsar la cocina o la recepción.</li>
<li>Pedir señal a todo el mundo, también a los habituales, que se molestan con razón.</li>
<li>No decidir cuánto se espera a quien llega tarde antes de liberar su plaza.</li>
<li>Mantener la libreta «por si acaso»: dos sistemas a la vez producen reservas dobles.</li>
</ul>
<h3 style="margin-top:28px">Si trabajas sin reserva o atiende una sola persona</h3>
<p style="max-width:820px">Un bar de menú del día que llena por orden de llegada no necesita un gestor de reservas online. Y si lo que organizas es el tiempo de un profesional (un fisio, una asesora, un peluquero), lo tuyo es una <a href="/servicios/software-de-gestion/agenda-y-citas-online">agenda de citas</a>, no un control de aforo. Esta herramienta compensa cuando hay plazas limitadas que se disputan varias personas: turnos de comedor, pistas, aulas, cabinas. En centros con abonos, la plaza se descuenta del <a href="/servicios/software-de-gestion/bonos-cuotas-y-suscripciones">bono o la cuota</a>, y buena parte de las peticiones llegan desde tu <a href="/servicios/presencia-digital/google-business-profile">ficha de Google</a>, que conviene tener cuidada.</p>
</div></section>""",
 "faq": [
  ("¿Cómo pasar de la libreta de reservas a un sistema online sin perder las que ya tengo?", "Cargando en el sistema todas las reservas futuras antes de abrirlo al público y fijando un día a partir del cual la libreta deja de usarse. Durante la transición, el equipo anota en la pantalla también las que entren por teléfono."),
  ("¿Quién atiende las reservas por teléfono cuando ya hay un sistema online?", "El mismo equipo, pero con menos llamadas y con una herramienta mejor: en lugar de hojear una libreta, ven de un vistazo qué queda libre y lo anotan en el mismo plano que usa la web, de modo que nunca se ofrece dos veces la misma plaza."),
 ],
}

# Estructura: excusas para no llamar (cita) + cuenta del último trimestre + insistir no es agobiar + lo que se lleva un comercial al irse
D["servicios/software-de-gestion/seguimiento-comercial-y-tareas"] = {
 "estructura": "excusas-para-no-llamar + cuenta-del-ultimo-trimestre + insistir-no-es-agobiar + cartera-que-se-va",
 "lead": "Enviaste la oferta hace diez días, quedaste en llamar y entre unas cosas y otras no lo has hecho; cuando por fin marcas, ya se lo han dado a otro. El seguimiento comercial con tareas en un CRM pone cada llamada pendiente en la lista de alguien, con fecha, para que no se enfríe.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Lo que nos decimos para no llamar</p><h2>¿Cuántas ofertas enviadas siguen esperando una llamada tuya?</h2></div>
<blockquote style="max-width:820px">«Si le interesa, ya llamará.»<br>«No quiero parecer pesado.»<br>«Esta semana sin falta le escribo.»</blockquote>
<p style="max-width:820px">Las tres frases son humanas y las tres cuestan ventas. Quien pide precio a varias empresas suele quedarse con la que le resuelve la última duda, no necesariamente con la más barata. Si esa duda surge el día doce y tú no has vuelto a dar señales, la resuelve otro.</p>
<h3 style="margin-top:26px">Haz recuento del último trimestre</h3>
<ol style="max-width:820px">
<li>Cuenta las propuestas que enviaste.</li>
<li>Separa las que tuvieron una respuesta clara, sea sí o sea no.</li>
<li>De las que quedan, apunta cuántas recibieron al menos un contacto tuyo después del envío.</li>
</ol>
<p style="max-width:820px">Lo que sobra en el tercer paso son operaciones que no perdiste: las abandonaste. Es la bolsa de ventas más fácil de recuperar, porque el trabajo caro (visitar, medir, preparar la oferta) ya está hecho.</p>
<h3 style="margin-top:26px">Insistir no es agobiar</h3>
<p style="max-width:820px">La diferencia está en lo que aportas. Llamar para preguntar «¿has visto ya el presupuesto?» incomoda. Llamar para aclarar un punto, proponer una alternativa o avisar de una fecha es un servicio. Una buena gestión de contactos comerciales no multiplica las llamadas: se asegura de que la siguiente tenga fecha y motivo, y de que alguien cierre el tema cuando el cliente dice que no.</p>
<h3 style="margin-top:26px">Lo que se lleva un vendedor cuando se va</h3>
<p style="max-width:820px">Si las conversaciones viven en su móvil y en su libreta, se lleva la cartera entera: quién estaba a punto de firmar, qué se prometió, cuándo había que volver a llamar. Con la agenda comercial dentro del programa, quien le sustituye abre la ficha y continúa. Las oportunidades se ordenan por fase en el <a href="/servicios/software-de-gestion/embudo-de-ventas-y-oportunidades">embudo de ventas</a>, los contactos nuevos entran desde la <a href="/servicios/software-de-gestion/captacion-de-leads-desde-web-whatsapp-y-anuncios">captación de leads</a> y, si dudas entre herramientas, la guía <a href="/guias/erp-vs-crm">ERP frente a CRM</a> aclara qué hace cada una.</p>
</div></section>""",
 "faq": [
  ("¿Cómo hacer el seguimiento de los presupuestos enviados sin que se me pase ninguno?", "Creando una tarea con fecha en el mismo momento en que envías la oferta, y otra nueva cada vez que cierras la anterior, hasta que el cliente decida. En un CRM esa cadena se genera sola y cada mañana ves a quién toca llamar."),
  ("¿Necesito un CRM si soy autónomo y llevo yo solo las ventas?", "Depende de cuántas conversaciones tengas abiertas a la vez. Con cuatro o cinco, una agenda basta. Cuando pasan de una docena, o cuando un proyecto tarda semanas en decidirse, la memoria empieza a fallar y un sistema de tareas te devuelve ventas que se estaban escapando."),
 ],
}

# Estructura: tabla por situación «conectar o seguir a mano» + qué revisar antes de pedir presupuesto + enlaces de continuidad
D["servicios/software-de-gestion/tienda-online-conectada"] = {
 "estructura": "tabla-conectar-o-seguir-a-mano + revision-antes-de-pedir-presupuesto + por-donde-seguir",
 "lead": "Vendes en la web un artículo que se acabó ayer en el local, copias cada pedido a mano en el programa y cambias los precios en dos sitios. Una tienda online conectada con stock y facturación trabaja con los mismos datos que tu mostrador, sin duplicar tareas.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">No todos los comercios lo necesitan igual</p><h2>¿Conectar el ecommerce con el programa o seguir pasando pedidos a mano?</h2></div>
<p style="max-width:820px">Depende de dos cosas: cuántos pedidos entran por internet y si comparten existencias con la venta en persona. Integrar cuesta un esfuerzo inicial, y hay situaciones en las que todavía no se recupera.</p>
<blockquote style="max-width:820px">«Los lunes me paso la primera hora copiando los pedidos del fin de semana y rezando para que quede género.»</blockquote>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Tu situación</th><th>Lo que suele bastar</th><th>Lo que ganarías integrando</th></tr></thead><tbody>
<tr><td>Algún pedido web a la semana y almacén holgado</td><td>Pasarlos al programa una vez al día</td><td>Poco, de momento</td></tr>
<tr><td>Pedidos diarios y el mismo género que en el local</td><td>Sincronizar existencias cuanto antes</td><td>Dejar de vender lo que ya no tienes y de pedir disculpas</td></tr>
<tr><td>Surtido amplio con cambios de precio frecuentes</td><td>Un único catálogo para los dos canales</td><td>No mantener dos listas ni dos descripciones</td></tr>
<tr><td>Vendes también en plataformas de terceros</td><td>Un solo origen para existencias y pedidos</td><td>Saber qué canal deja margen y cuál solo volumen</td></tr>
</tbody></table></div>
<p style="max-width:820px;margin-top:18px">La señal más fiable es el tiempo: si alguien dedica un rato cada día a copiar datos de la web al programa y a corregir existencias, ese rato ya tiene un coste mayor que la integración.</p>
<h3 style="margin-top:28px">Qué revisar antes de pedir presupuesto</h3>
<ul class="lista" style="max-width:820px">
<li><strong>En qué plataforma está tu tienda</strong> y si permite conectarse con otros programas. Lo comprobamos antes de proponerte nada.</li>
<li><strong>Si las referencias coinciden.</strong> El mismo producto con un código en la web y otro en el local es el origen de casi todos los descuadres.</li>
<li><strong>Quién manda en el precio.</strong> Hay que elegir un único sitio donde se cambia; el otro obedece.</li>
<li><strong>Qué pasa con cambios y devoluciones,</strong> que son los que deshacen el stock si nadie los registra.</li>
<li><strong>Cuánto género reservas</strong> para no vender en línea la última unidad que un cliente tiene en la mano.</li>
</ul>
<h3 style="margin-top:28px">Por dónde seguir según tu punto de partida</h3>
<p style="max-width:820px">Si aún no vendes por internet o tu web actual se ha quedado corta, el punto de partida es el <a href="/servicios/webs/tienda-online">diseño de la tienda online</a>. En el local, la otra mitad de la sincronización es el <a href="/servicios/software-de-gestion/tpv">TPV</a>, y con varios puntos de venta, el <a href="/servicios/software-de-gestion/inventario-en-varios-almacenes">inventario por ubicaciones</a>. Cuando hay más piezas que encajar (contabilidad, CRM, transportistas), lo tratamos como proyecto de <a href="/servicios/migraciones-e-integraciones/conectar-erp-tienda-crm-y-contabilidad">integración entre programas</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo sincronizar el stock de mi tienda física con la tienda online?", "Haciendo que las dos lean y escriban en el mismo inventario. Cada venta, sea en el mostrador o en la web, descuenta de una única cifra, y la web muestra lo disponible en ese momento. Para lograrlo, los artículos deben tener la misma referencia en ambos lados."),
  ("¿A partir de cuántos pedidos compensa conectar la tienda online al programa de gestión?", "No hay un número fijo. Compensa cuando copiar pedidos y corregir existencias ocupa un rato todos los días, o cuando ya has tenido que anular ventas por falta de género. Con pedidos esporádicos y stock de sobra, puede esperar."),
 ],
}
