# Reescritura «dolores primero» · familia Apps móviles (noviembre 2026).
# Cada página sigue un recorrido distinto; la pregunta de fondo es siempre si la app hace falta de verdad.
D = {}

# Estructura: recorrido de un pedido hoy en cinco pasos + tabla de dos modos de uso + cuándo no compensa
D["servicios/apps-moviles/app-de-catalogo-y-pedidos-para-distribuidores"] = {
 "estructura": "recorrido-del-pedido-reescrito + tabla-comercial-o-cliente + cuando-no-compensa",
 "lead": "Los pedidos te llegan por audio de WhatsApp, por foto de una hoja garabateada y por llamada a las once de la noche, y cada mañana alguien los teclea en el programa antes de que salga el reparto. Una app de pedidos para distribuidores y comerciales hace que el pedido entre ya escrito.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">El pedido que se escribe tres veces</p><h2>¿Cuánto te cuesta reescribir cada pedido?</h2></div>
<p style="max-width:820px">Te cuesta el tiempo de quien lo pasa a limpio y, sobre todo, los errores que se cuelan por el camino. Sigue un pedido cualquiera desde que nace hasta que se carga en la furgoneta:</p>
<ol style="max-width:820px">
<li>El cliente lo dicta o lo apunta de memoria: «lo de siempre y dos cajas más de lo otro».</li>
<li>El comercial lo anota en su libreta o lo reenvía en una foto.</li>
<li>En la oficina alguien lo interpreta y lo teclea. Aquí «dos cajas» se convierte en «doce» o en un formato que ya no trabajas.</li>
<li>Almacén prepara lo que pone, no lo que el cliente quería.</li>
<li>El repartidor entrega, el cliente protesta y hay que hacer un abono y un segundo viaje.</li>
</ol>
<p style="max-width:820px">Para ponerle cifra, cuenta los abonos y las devoluciones del último mes que vinieron de un pedido mal entendido y súmales las horas diarias de teclear. El número es tuyo y dice si esto es una molestia o una fuga.</p>
<blockquote style="max-width:820px">«Mi administrativa entra una hora antes solo para pasar los pedidos de la noche.»</blockquote>
<h3 style="margin-top:28px">Dos formas de usarla: decide cuál es la tuya</h3>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th></th><th>La lleva el comercial</th><th>La usa el propio cliente</th></tr></thead><tbody>
<tr><td>Quién introduce el pedido</td><td>Tu vendedor, durante la visita</td><td>El comprador, cuando le viene bien</td></tr>
<tr><td>Encaja cuando…</td><td>La visita sirve para aconsejar y enseñar novedades</td><td>Los pedidos son repetitivos y el cliente sabe lo que quiere</td></tr>
<tr><td>Qué cambia en tu equipo</td><td>El comercial deja de ser un tomador de notas</td><td>La oficina deja de atender pedidos por teléfono</td></tr>
<tr><td>Resistencia habitual</td><td>«Con la libreta voy más rápido»</td><td>«Yo siempre he llamado»</td></tr>
</tbody></table></div>
<p style="max-width:820px;margin-top:18px">Con una docena de clientes que piden lo mismo cada semana, no necesitas una app: basta un pedido tipo que se repite. Y si tus compradores trabajan sentados delante de un ordenador, puede servirles mejor el <a href="/servicios/software-de-gestion/portal-de-pedidos-b2b">portal de pedidos B2B</a>. En ambos casos, lo que manda es que el <a href="/servicios/software-de-gestion/catalogo-y-tarifas">catálogo y las tarifas</a> estén bien en origen; y si pagas por ventas, que cada pedido alimente el cálculo de <a href="/servicios/software-de-gestion/comerciales-y-comisiones">comerciales y comisiones</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo hacer una app de pedidos para comerciales?", "Se parte del catálogo y las tarifas que ya tienes en el programa de gestión, se define qué ve cada comercial y cada cliente, y se conecta la app para que el pedido entre directamente en el sistema. Antes de programar nada se comprueba que esa conexión es posible."),
  ("¿Mis clientes de toda la vida se acostumbrarán a pedir por una app?", "No todos ni a la vez, y no hace falta. Lo habitual es empezar por quienes ya piden por mensaje, que notan la ventaja enseguida, y mantener el teléfono para el resto. El comercial puede introducir en la misma app los pedidos de quien prefiere dictarlos."),
 ],
}

# Estructura: lista de lo que se pierde por el camino + por qué no basta el grupo de WhatsApp + cómo lograr que el equipo la use
D["servicios/apps-moviles/app-interna-para-empleados-y-tecnicos"] = {
 "estructura": "lo-que-se-pierde-en-la-furgoneta + limites-del-grupo-de-mensajes + adopcion-por-el-equipo",
 "lead": "El técnico termina el aviso, apunta las horas en un papel que viaja una semana en la guantera y, cuando llega a la oficina, nadie entiende la letra ni sabe qué material se gastó. Una app para empleados y técnicos con partes, fichaje y tareas cierra el trabajo en el sitio.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Lo que no vuelve con el técnico</p><h2>¿Qué se pierde entre la furgoneta y la oficina?</h2></div>
<ul class="lista" style="max-width:820px">
<li>Horas trabajadas que no llegan a la factura porque el parte apareció tarde o no apareció.</li>
<li>Material usado que nadie cobró ni repuso en el almacén.</li>
<li>La firma del cliente, que era la prueba de que el trabajo se hizo.</li>
<li>Las fotos del antes y el después, repartidas en los móviles personales de cada uno.</li>
<li>El aviso que se dio de palabra y que el compañero del turno siguiente nunca recibió.</li>
</ul>
<blockquote style="max-width:820px">«Facturamos a final de mes con lo que nos acordamos. Seguro que nos dejamos cosas.»</blockquote>
<h3 style="margin-top:28px">Por qué el grupo de WhatsApp se queda corto</h3>
<p style="max-width:820px">Porque mezcla todo con todo. En el mismo hilo conviven la dirección del próximo servicio, la foto de una avería, un chiste y el aviso de que mañana hay inspección. Encontrar la semana que viene qué se hizo en casa de un cliente obliga a deslizar el dedo hacia arriba durante un cuarto de hora. Además, ese historial vive en los teléfonos de tus empleados, no en la empresa: cuando alguien se marcha, se lo lleva puesto.</p>
<h3 style="margin-top:28px">Lo difícil no es la app, es que se use</h3>
<p style="max-width:820px">Una herramienta para gente que trabaja con las manos tiene que pedir menos esfuerzo que el papel, o volverá el papel. Eso significa botones grandes, pocas pantallas y cero campos «por si acaso». Antes de diseñarla nos sentamos con dos o tres personas del equipo, no solo con gerencia, y les preguntamos qué les hace perder tiempo hoy. Si el primer día les ahorra una llamada a la oficina, la adoptan; si solo les añade trabajo para que otro tenga informes, la sortean.</p>
<p style="max-width:820px">No hace falta empezar con todo. Lo sensato es arrancar por el parte de trabajo y, cuando ruede, sumar lo demás. Si lo único que necesitas es registrar la jornada, te sobra una app a medida: mira el <a href="/servicios/fichador">fichador</a>. Si ya usas nuestro programa, los <a href="/servicios/software-de-gestion/ordenes-y-partes-de-trabajo-con-firma-y-fotos">partes de trabajo con firma y fotos</a> y la <a href="/servicios/software-de-gestion/app-para-tecnicos-de-campo">app para técnicos de campo</a> ya cubren el caso más común.</p>
</div></section>""",
 "faq": [
  ("¿Cómo consigo que los técnicos rellenen los partes de trabajo el mismo día?", "Haciendo que cerrar el parte sea el último paso natural del servicio y no una tarea aparte: materiales elegidos de una lista, fotos desde la cámara y firma del cliente en la pantalla. Si lleva menos de un par de minutos, se hace en el sitio."),
  ("¿Necesito una app a medida o me vale la que trae mi programa de gestión?", "Si la app de tu programa cubre partes, agenda y fotos tal como trabaja tu equipo, úsala. La app a medida compensa cuando tu proceso tiene pasos propios, como certificados, listas de comprobación o documentos específicos de tu sector, que una aplicación genérica no contempla."),
 ],
}

# Estructura: tabla función por función «¿hace falta app?» con alternativa + prueba de la pantalla de inicio + preguntas antes de decidir
D["servicios/apps-moviles/app-para-socios-alumnos-o-pacientes"] = {
 "estructura": "tabla-hace-falta-app-o-no + prueba-de-la-pantalla-de-inicio + preguntas-previas",
 "lead": "Alguien te ha dicho que tu gimnasio, tu academia o tu clínica necesita una app propia y no sabes si es verdad o una moda cara. Una app para socios, alumnos o pacientes con tu marca compensa cuando la misma persona vuelve cada semana; si no, puede que te baste con menos.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">«Me dijeron que necesitaba una app»</p><h2>¿De verdad necesita mi centro una aplicación propia?</h2></div>
<p style="max-width:820px">Solo si tus usuarios van a abrirla a menudo. Una app es una herramienta para relaciones frecuentes: el socio que reserva pista tres veces por semana, el padre que mira cada tarde si hay aviso del profesor. Para una visita al año es un estorbo en el teléfono que acabará borrada. Repasa lo que quieres ofrecer, función por función:</p>
<div class="tabla-wrap" style="margin-top:18px"><table class="tabla-norm"><thead><tr><th>Lo que quieres que puedan hacer</th><th>¿Hace falta app?</th><th>Alternativa más sencilla</th></tr></thead><tbody>
<tr><td>Reservar clase o pista cada semana</td><td>Sí, aquí brilla</td><td>—</td></tr>
<tr><td>Recibir avisos de última hora (clase anulada, cambio de sala)</td><td>Sí, por las notificaciones</td><td>Mensaje de WhatsApp al grupo afectado</td></tr>
<tr><td>Consultar horarios y tarifas</td><td>No</td><td>Una página web clara</td></tr>
<tr><td>Pedir cita un par de veces al año</td><td>No</td><td>Reserva desde la web o por mensaje</td></tr>
<tr><td>Pagar la cuota</td><td>Ayuda, pero no es imprescindible</td><td>Domiciliación o enlace de pago</td></tr>
<tr><td>Ver documentos personales (notas, informes, recibos)</td><td>Depende de la frecuencia</td><td>Área privada en la web</td></tr>
</tbody></table></div>
<h3 style="margin-top:28px">La prueba de la pantalla de inicio</h3>
<p style="max-width:820px">Piensa en tu usuario más fiel y pregúntate si pondría tu icono en la primera pantalla de su móvil, junto al banco y la mensajería. Si la respuesta es «sí, porque lo usa varias veces por semana», adelante. Si es «lo abriría cuando le toque renovar», lo que necesitas es otra cosa, y te saldrá mejor de precio y de mantenimiento.</p>
<ul class="lista" style="max-width:820px">
<li>¿Cuántas llamadas y mensajes a recepción desaparecerían si el usuario pudiera hacerlo solo?</li>
<li>¿Quién va a mantener al día horarios, grupos y avisos dentro de la app?</li>
<li>¿Tu programa actual permite conectarse, o habría que duplicar los datos?</li>
<li>¿Qué pasa con quien no quiera o no sepa instalarla?</li>
</ul>
<p style="max-width:820px">Si tras este repaso la app sigue teniendo sentido, el detalle de reservas, pagos y avisos está en la <a href="/servicios/apps-moviles/app-para-clientes-reservas-pedidos-fidelizacion-y-avisos">app para clientes</a>. Si no, casi siempre encaja una <a href="/servicios/webs/web-con-reservas-y-citas">web con reservas y citas</a> o las <a href="/servicios/whatsapp-ia/citas-y-recordatorios-automaticos">citas y recordatorios por WhatsApp</a>. Hay una reflexión más larga en el artículo sobre <a href="/blog/app-movil-para-mi-negocio">si tu negocio necesita una app móvil</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo sé si mi negocio necesita una app o le basta con una web?", "Mira con qué frecuencia vuelve cada usuario. Si reserva, consulta o paga varias veces al mes, la app le ahorra tiempo y la usará. Si acude de forma esporádica, una web con reserva y un recordatorio por mensaje cumplen sin obligarle a instalar nada."),
  ("¿Usarán la app los socios o pacientes de más edad?", "Una parte sí y otra no, y hay que contar con ello. Recepción sigue atendiendo a quien prefiere llamar o pasar por el mostrador, y registra la reserva en el mismo sistema para que todo quede en un único sitio."),
 ],
}

# Estructura: por qué una app deja de funcionar sola + señales de que ya vas tarde + qué pedir hoy a quien la hizo (lista numerada)
D["servicios/apps-moviles/mantenimiento-y-actualizaciones"] = {
 "estructura": "por-que-caduca-una-app + senales-de-ir-tarde + que-pedir-al-desarrollador",
 "lead": "La app funcionaba perfectamente hasta que un cliente estrenó móvil y dejó de abrirse; la empresa que la programó ha cerrado, o te propone rehacerla entera. El mantenimiento de apps móviles y sus actualizaciones existe para que te enteres de estas cosas antes que tus usuarios.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Nadie la tocó y aun así se rompió</p><h2>¿Por qué una app que iba bien deja de funcionar sola?</h2></div>
<p style="max-width:820px">Porque la app no cambia, pero todo lo que la rodea sí. El teléfono estrena sistema, la tienda endurece sus requisitos, el servicio que enviaba las notificaciones modifica sus condiciones o caduca un certificado. Una aplicación es como un local en un centro comercial: aunque tú no hagas obras, el edificio cambia las normas, y un día no te dejan levantar la persiana.</p>
<blockquote style="max-width:820px">«Nos enteramos por una reseña de una estrella: "desde la última actualización del móvil no abre".»</blockquote>
<h3 style="margin-top:28px">Cinco avisos de que la app está desatendida</h3>
<ul class="lista" style="max-width:820px">
<li>La última versión publicada tiene más de un año.</li>
<li>Recibes correos de Apple o de Google que nadie lee porque llegan a una cuenta antigua.</li>
<li>Las valoraciones recientes hablan de cierres inesperados o de que no deja iniciar sesión.</li>
<li>No sabes quién tiene acceso a las cuentas de las tiendas.</li>
<li>Los pedidos o reservas hechos desde la app llegan a veces sí y a veces no.</li>
</ul>
<p style="max-width:820px">Con dos de estos avisos, conviene revisar la app antes de que lo haga por ti una tienda retirándola.</p>
<h3 style="margin-top:28px">Lo que deberías pedir hoy a quien te la hizo</h3>
<ol style="max-width:820px">
<li>El código fuente completo, en un repositorio al que tengas acceso tú.</li>
<li>Ser propietario, no invitado, de las cuentas de desarrollador en las dos tiendas.</li>
<li>Las claves con las que se firman las versiones.</li>
<li>La lista de servicios externos de los que depende (notificaciones, mapas, pagos) y quién paga cada uno.</li>
<li>Unas instrucciones escritas para generar y publicar una versión nueva.</li>
</ol>
<p style="max-width:820px">Pedirlo cuando la relación es buena cuesta un correo; pedirlo cuando ya hay un problema puede costar la app. Si te falta alguno de los cinco y tu proveedor no responde, estás en un caso parecido al <a href="/servicios/migraciones-e-integraciones/rescate-de-software-antiguo">rescate de software antiguo</a>. Cómo se ordenan las cuentas y la titularidad lo explicamos en la <a href="/servicios/apps-moviles/publicacion-en-google-play-y-app-store">publicación en Google Play y App Store</a>. Y si dudas de si la app merece seguir viva, cuéntanoslo en el <a href="/contacto#diagnostico">diagnóstico gratuito</a>: a veces lo honesto es recomendar que se sustituya por una web.</p>
</div></section>""",
 "faq": [
  ("¿Qué pasa si la empresa que hizo mi app ha cerrado?", "Lo primero es comprobar qué conservas: código fuente, cuentas de las tiendas y claves de firma. Con eso otra empresa puede hacerse cargo. Si falta alguna pieza, se estudia qué se puede recuperar y qué habría que reconstruir."),
  ("¿Es mejor mantener una app antigua o rehacerla desde cero?", "Depende del estado del código y de si aún responde a lo que necesita el negocio. Si la base es razonable, mantener y mejorar por partes sale más a cuenta. Si está hecha con tecnología abandonada o nadie puede compilarla, rehacerla suele ser más seguro que parchearla."),
 ],
}

# Estructura: línea de tiempo real de una publicación en pasos + errores que retrasan un lanzamiento + cuándo no necesitas las tiendas
D["servicios/apps-moviles/publicacion-en-google-play-y-app-store"] = {
 "estructura": "linea-de-tiempo-de-publicacion + errores-que-retrasan + cuando-sobran-las-tiendas",
 "lead": "La app está terminada y crees que publicarla es pulsar un botón; dos semanas después sigues rellenando formularios de Apple, te piden un número de empresa que no sabías que existía y la revisión la ha devuelto por una captura. Publicar una app en Google Play y App Store tiene su propio calendario.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">El último tramo, que nadie presupuesta</p><h2>¿Cuánto se tarda de verdad en tener la app en las tiendas?</h2></div>
<ol style="max-width:820px">
<li>Semanas antes: abrir las cuentas de desarrollador a nombre de la empresa. Es lo más lento, porque la verificación depende de Apple y de Google, no de ti ni de nosotros.</li>
<li>Con la app aún en pruebas: preparar nombre, descripción, icono y capturas, y contestar los cuestionarios sobre qué datos recoge.</li>
<li>Con la versión final: enviarla a revisión en cada tienda.</li>
<li>Durante la revisión: responder a lo que pidan. Un rechazo no es un drama, es un paso frecuente que se resuelve y se reenvía.</li>
<li>Aprobada: publicar, a ser posible primero para un grupo reducido y después para todos.</li>
</ol>
<p style="max-width:820px">Por eso la respuesta honesta es «depende de las tiendas». Ningún proveedor serio puede fijarte el día exacto en que tu app estará disponible; lo que sí puede es empezar el primer paso mucho antes de que termine el desarrollo, que es donde se ganan o se pierden las semanas.</p>
<h3 style="margin-top:28px">Errores que retrasan un lanzamiento</h3>
<ul class="lista" style="max-width:820px">
<li>Anunciar la fecha en redes antes de tener la aprobación.</li>
<li>Abrir las cuentas con el correo personal de un empleado o, peor, a nombre de quien programa.</li>
<li>Pedir permisos del teléfono (ubicación, contactos, cámara) que la app no usa.</li>
<li>Enviar a revisión una versión sin un usuario de prueba para que el revisor pueda entrar.</li>
<li>Dejar la política de privacidad para el último día.</li>
</ul>
<h3 style="margin-top:28px">Y si resulta que no necesitas las tiendas</h3>
<p style="max-width:820px">Pasa más de lo que parece. Si la aplicación es para tu plantilla, hay vías de distribución privada que evitan la ficha pública. Y si lo que ofreces a tus clientes es consultar, reservar o pedir de vez en cuando, una web bien adaptada al móvil lo resuelve sin revisión ni cuentas de desarrollador: compáralo en la <a href="/servicios/webs/web-con-reservas-y-citas">web con reservas y citas</a>. Para el uso interno, mira la <a href="/servicios/apps-moviles/app-interna-para-empleados-y-tecnicos">app para empleados y técnicos</a>. Publicar tampoco es el final: desde ese día empieza el <a href="/servicios/apps-moviles/mantenimiento-y-actualizaciones">mantenimiento y las actualizaciones</a>, que conviene dejar acordado antes del lanzamiento.</p>
</div></section>""",
 "faq": [
  ("¿Puedo publicar yo mismo mi app en Google Play y App Store?", "Sí, las tiendas permiten que cualquier empresa lo haga. Requiere tiempo para abrir las cuentas, preparar la ficha, declarar el uso de datos y atender la revisión. Si la app la ha hecho un tercero, asegúrate de que las cuentas quedan a nombre de tu empresa."),
  ("¿Qué fecha de lanzamiento puedo anunciar para mi app?", "Lo prudente es no anunciar una fecha hasta que las dos tiendas hayan aprobado la versión. Si necesitas comunicarlo antes, deja un margen amplio, porque un rechazo en la revisión obliga a corregir y volver a enviar."),
 ],
}
