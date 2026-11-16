# Reescritura «dolores primero» · familia Problemas que nadie resuelve (noviembre 2026).
# Diez páginas con diez recorridos distintos. Studio Emprende no es gestoría ni despacho: en todas queda dicho dónde acaba la herramienta.
D = {}

# Estructura: por qué cada trámite empieza de cero + tabla «quién hace qué» + para quién no merece la pena
D["servicios/problemas-sin-resolver/agente-de-tramites"] = {
 "estructura": "por-que-se-empieza-de-cero + tabla-quien-hace-que + para-quien-no-merece-la-pena",
 "lead": "Para pedir una licencia te reclaman la escritura, el seguro, un certificado que caducó la semana pasada y un formulario que ya rellenaste casi igual el año anterior. Un agente de IA para trámites y papeleo de empresa reúne todo eso y deja el borrador listo para que tú o tu gestoría lo reviséis.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">El papeleo que nadie tiene tiempo de hacer bien</p><h2>¿Por qué cada trámite te obliga a empezar de cero?</h2></div>
<p style="max-width:820px">Porque la información de tu empresa está repartida. La escritura, en un cajón; el último certificado, en el correo de alguien; la póliza, en la carpeta de la gestoría; y los datos que siempre piden, en tu cabeza. Cada solicitud vuelve a exigir lo mismo en otro formato, y quien la prepara suele ser el dueño, fuera de horas y con miedo a dejarse algo. No es un trabajo difícil: es tedioso, repetido y con fecha límite.</p>
<p style="max-width:820px">El agente no decide ni presenta. Ordena y prepara. Conviene tener claro ese reparto antes de contratar nada.</p>
<h3 style="margin-top:28px">Quién hace qué en una gestión con la Administración</h3>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Paso</th><th>El agente de IA</th><th>Tú o tu gestoría</th></tr></thead><tbody>
<tr><td>Saber qué piden</td><td>Lee el formulario o las bases y lista los documentos exigidos</td><td>Confirmáis que es el trámite que corresponde</td></tr>
<tr><td>Reunir documentos</td><td>Localiza los que ya existen y marca los caducados o ausentes</td><td>Solicitáis los que faltan</td></tr>
<tr><td>Rellenar</td><td>Prepara el borrador con los datos de la empresa</td><td>Revisáis cada campo y corregís</td></tr>
<tr><td>Firmar y presentar</td><td>No lo hace</td><td>Siempre una persona, con su certificado</td></tr>
<tr><td>Seguir el plazo</td><td>Recuerda fechas y lo que queda pendiente</td><td>Decidís cómo responder</td></tr>
</tbody></table></div>
<h3 style="margin-top:28px">Para quién no merece la pena</h3>
<p style="max-width:820px">Si haces dos gestiones al año y tu gestoría ya las lleva de principio a fin, automatizar los trámites de la empresa no te aporta nada. Compensa cuando el papeleo es recurrente: negocios que piden permisos a menudo, que entregan la misma documentación a muchos clientes, que tienen varias sedes o que se presentan a concursos (para eso hay un agente específico de <a href="/servicios/agentes-de-ia/licitaciones-publicas">licitaciones públicas</a>). Tampoco sustituye a tu asesor: no interpreta la normativa ni te dice si te conviene solicitar algo. Si lo que te quita el sueño son las fechas, lo complementan el <a href="/servicios/problemas-sin-resolver/calendario-de-obligaciones">calendario de obligaciones</a> y el <a href="/servicios/problemas-sin-resolver/buzon-de-notificaciones-vigilado">buzón de notificaciones vigilado</a>.</p>
</div></section>""",
 "faq": [
  ("¿Puede una IA rellenar formularios de la Administración por mí?", "Puede preparar el borrador con los datos y documentos de tu empresa y decirte qué falta. Revisarlo, firmarlo y presentarlo sigue siendo cosa tuya o de tu gestoría: el agente no usa tu certificado ni envía nada por su cuenta."),
  ("¿Cómo organizar la documentación de mi empresa para no buscarla en cada trámite?", "Reuniéndola en un único archivo ordenado por tipo —escrituras, seguros, certificados, licencias— y anotando la fecha de caducidad de cada documento. Así sabes qué está vigente y qué hay que renovar antes de que te lo pidan."),
 ],
}

# Estructura: la frase «yo no he recibido nada» (cita) + cómo se pierde un aviso + tres preguntas incómodas + hasta dónde llegamos
D["servicios/problemas-sin-resolver/buzon-de-notificaciones-vigilado"] = {
 "estructura": "cita-yo-no-he-recibido-nada + como-se-pierde-un-aviso + tres-preguntas-incomodas + hasta-donde-llegamos",
 "lead": "Te enteras de que Hacienda te había escrito cuando llega el recargo: el aviso fue a un correo que ya nadie abre y la carta electrónica venció sin que la leyeras. Con las notificaciones electrónicas de Hacienda vigiladas, cada comunicación llega a tiempo a quien tiene que responder.",
 "bloque": """<section class="sec sec-suave"><div class="w">
<div class="cab"><p class="kicker">La carta que nadie vio</p><h2>¿Cómo es posible que te notifiquen algo y no te enteres?</h2></div>
<blockquote style="max-width:820px">«Yo no he recibido nada.»</blockquote>
<p style="max-width:820px">Es lo primero que se dice cuando aparece el recargo, y suele ser verdad a medias: la notificación se envió, pero a un buzón electrónico que nadie abría. Ocurre así. Un día diste de alta la empresa en una sede electrónica con el correo de quien llevaba entonces la administración. Esa persona se marchó, o la dirección se llenó de publicidad, o el aviso cayó en la carpeta de no deseados. El plazo corre igual y tú sigues trabajando sin saberlo. No hay mala fe por ninguna parte: hay un buzón sin dueño.</p>
<p style="max-width:820px">Los más expuestos son los autónomos que pasan el día fuera, las sociedades pequeñas sin nadie en administración y quienes tienen varias empresas, cada una con sus buzones.</p>
<h3 style="margin-top:28px">Tres preguntas incómodas</h3>
<ul class="lista" style="max-width:820px">
<li>¿Qué dirección de correo figura como contacto en cada sede electrónica, y quién la lee de verdad?</li>
<li>¿Quién tiene el certificado digital y qué pasa cuando esa persona está de vacaciones o de baja?</li>
<li>Si tu gestoría recibe los avisos, ¿en cuánto tiempo te los traslada y por qué canal?</li>
</ul>
<p style="max-width:820px">Si alguna no tiene una respuesta clara, ya sabes por dónde puede llegar el susto.</p>
<h3 style="margin-top:28px">Lo que hacemos y lo que queda para tu gestoría</h3>
<p style="max-width:820px">Vigilamos, avisamos y resumimos. No contestamos requerimientos ni presentamos escritos: eso es trabajo de tu gestoría o de tu abogado, y lo habitual es que reciban el mismo aviso que tú, como explicamos en la <a href="/servicios/software-de-gestion/conexion-con-tu-asesoria">conexión con tu asesoría</a>. Tampoco podemos evitar que una administración te reclame algo; lo que evitamos es que el plazo pase sin que nadie lo haya visto.</p>
<p style="max-width:820px">Si además de las notificaciones quieres tener controlados impuestos, renovaciones y revisiones, el siguiente paso es el <a href="/servicios/problemas-sin-resolver/calendario-de-obligaciones">calendario de obligaciones con avisos</a>. Y si no sabes en qué sedes está dada de alta tu empresa, lo vemos contigo en el <a href="/contacto#diagnostico">diagnóstico gratuito</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo sé si tengo notificaciones pendientes de Hacienda?", "Entrando con tu certificado digital en la Dirección Electrónica Habilitada única y en las sedes donde tu empresa esté dada de alta. La dificultad es acordarse de hacerlo cada pocos días; el buzón vigilado lo comprueba y te avisa en cuanto aparece algo."),
  ("¿Quién debe revisar las notificaciones electrónicas, la empresa o la gestoría?", "Depende de lo que hayáis acordado: muchas gestorías lo hacen si las autorizas, pero conviene dejarlo por escrito. Como las consecuencias recaen sobre la empresa, lo más seguro es que el aviso llegue a las dos partes a la vez."),
 ],
}

# Estructura: cuatro sitios donde viven hoy tus fechas (tarjetas) + primera versión en una tarde + límite: no decidimos tus obligaciones
D["servicios/problemas-sin-resolver/calendario-de-obligaciones"] = {
 "estructura": "cuatro-sitios-donde-viven-las-fechas + primera-version-en-una-tarde + quien-valida-la-lista",
 "lead": "La ITV de la furgoneta, el seguro de responsabilidad civil, la revisión de los extintores, el dominio de la web y el trimestre caen en la misma quincena y te acuerdas de dos. Un calendario de obligaciones fiscales y legales saca esas fechas de tu cabeza y avisa con margen a quien le toca.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Fechas que solo existen en tu memoria</p><h2>¿Dónde están apuntados hoy los plazos de tu empresa?</h2><p class="lead" style="margin-top:8px">En cuatro sitios distintos que no se hablan entre sí. Por eso alguno se escapa.</p></div>
<div class="rejilla">
<div class="tarjeta"><h3>En la gestoría</h3><p>Lleva los impuestos y te pide los papeles con el tiempo justo. Lo que no es fiscal ni laboral no está en su lista.</p></div>
<div class="tarjeta"><h3>En tu cabeza</h3><p>Renovaciones, licencias, contratos con proveedores. Funciona hasta la semana en que enfermas o el trabajo te desborda.</p></div>
<div class="tarjeta"><h3>En una pegatina</h3><p>La del extintor, la de la caldera, la del vehículo. Nadie la mira hasta que la fecha ya ha pasado.</p></div>
<div class="tarjeta"><h3>En el correo de un proveedor</h3><p>El aviso de que caduca el dominio o el certificado llega a una dirección que quizá ya no usas.</p></div>
</div>
<p style="max-width:820px;margin-top:18px">Si te reconoces en más de una, es lo habitual: casi ninguna pequeña empresa tiene una agenda única de vencimientos.</p>
<h3 style="margin-top:30px">Monta la primera versión en una tarde</h3>
<ol style="max-width:820px">
<li>Pide a tu asesoría la lista de modelos que te presenta y sus fechas.</li>
<li>Recorre el local con el móvil y fotografía cada etiqueta de revisión.</li>
<li>Abre pólizas, contratos y facturas anuales, y apunta el vencimiento y el preaviso de cada uno.</li>
<li>Pon un nombre al lado de cada fecha. Un aviso sin responsable es ruido.</li>
</ol>
<p style="max-width:820px">Con eso ya tienes un control de vencimientos de empresa, aunque sea en una hoja. Lo que añade el servicio es que deje de depender de que alguien abra esa hoja: los avisos salen solos, suben a dirección si nadie los atiende y cada justificante queda guardado junto a su fecha.</p>
<p style="max-width:820px">Un límite que conviene dejar claro: nosotros no decidimos qué obligaciones tiene tu negocio. Esa lista la validan tu gestoría y los técnicos que hacen cada revisión; el calendario la recuerda y deja constancia. Para las comunicaciones oficiales que no tienen fecha conocida existe el <a href="/servicios/problemas-sin-resolver/buzon-de-notificaciones-vigilado">buzón de notificaciones vigilado</a>; las renovaciones técnicas las tratamos en <a href="/servicios/departamento-tecnologico/dominios-y-renovaciones">dominios y renovaciones</a>, y el repaso de normas que pueden afectarte está en <a href="/normativas">normativas para empresas</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo llevar el control de los vencimientos de una empresa sin que se pase ninguno?", "Reuniendo todas las fechas en un solo calendario, asignando cada una a una persona y programando al menos dos avisos: uno con tiempo para preparar y otro cerca del día. Lo que más falla no es la lista, sino que nadie se sienta responsable de cada plazo."),
  ("¿Sirve una hoja de Excel como calendario de obligaciones?", "Sirve para empezar y para ver todo junto. Su punto débil es que no avisa: alguien tiene que acordarse de abrirla. Cuando las fechas son muchas o dependen de varias personas, compensa pasar a un sistema que envíe los avisos por sí mismo."),
 ],
}

# Estructura: tabla «lo que oyes / lo que pasa / con enlace» + cuándo aporta poco + tres decisiones previas
D["servicios/problemas-sin-resolver/cobro-facil-con-enlaces-de-pago"] = {
 "estructura": "tabla-lo-que-oyes-lo-que-pasa + cuando-aporta-poco + tres-decisiones-previas",
 "lead": "«Mándame el número de cuenta», «mañana te hago la transferencia», «se me pasó, perdona». Casi nunca hay mala intención: pagar una factura da pereza y se va dejando. Los enlaces de pago para cobrar facturas al momento convierten ese «luego» en un botón que el cliente pulsa desde su móvil.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">No es que no quieran pagar</p><h2>¿Por qué un cliente contento tarda semanas en pagarte?</h2></div>
<p style="max-width:820px">Porque pagarte le exige más pasos de los que parece, y cada paso es una ocasión de dejarlo para luego. Las frases te sonarán.</p>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Lo que oyes</th><th>Lo que suele estar pasando</th><th>Con un enlace de pago</th></tr></thead><tbody>
<tr><td>«Pásame el IBAN otra vez»</td><td>El correo con la factura está enterrado entre otros cien</td><td>El botón de pagar va en cada mensaje que le envías</td></tr>
<tr><td>«Esta noche te lo hago desde casa»</td><td>Una transferencia exige abrir el banco, copiar la cuenta y escribir el concepto</td><td>Paga desde el móvil en el mismo momento en que lo lee</td></tr>
<tr><td>«¿Cuánto era al final?»</td><td>No recuerda el importe ni qué factura es</td><td>El enlace ya lleva el importe y el concepto</td></tr>
<tr><td>«Creo que ya te lo pagué»</td><td>Ni él ni tú lo tenéis claro</td><td>El pago queda anotado en la factura al instante</td></tr>
</tbody></table></div>
<p style="max-width:820px;margin-top:18px">Cobrar con tarjeta a distancia, por correo o por WhatsApp, elimina la fricción, que es la causa más corriente del retraso entre particulares y negocios pequeños. No convierte en buen pagador a quien no piensa pagar: para eso hacen falta otras medidas, como un <a href="/servicios/problemas-sin-resolver/sistema-anti-impagos">sistema anti-impagos</a>.</p>
<h3 style="margin-top:28px">Cuándo un enlace de pago aporta poco</h3>
<ul class="lista" style="max-width:820px">
<li>Si tus clientes son empresas grandes que pagan por transferencia en fechas fijas, con su propio circuito de aprobación.</li>
<li>Si los importes son altos y la comisión de la pasarela pesa: compara antes con la transferencia o con las <a href="/servicios/software-de-gestion/remesas-y-domiciliaciones">remesas y domiciliaciones</a>.</li>
<li>Si ya cobras todo en el mostrador con datáfono.</li>
</ul>
<h3 style="margin-top:28px">Tres decisiones antes de activarlo</h3>
<p style="max-width:820px">La primera, con qué pasarela: pregunta la comisión por operación y cuánto tarda en abonarte el dinero. La segunda, en qué documentos aparecerá el enlace: la señal del presupuesto, la factura, el recordatorio o los tres. La tercera, si tu programa actual puede anotar el cobro sin intervención; esto lo comprobamos nosotros antes de darte presupuesto. Cuando lo que quieres es ordenar el ciclo completo y no solo el momento del pago, la página de referencia es <a href="/servicios/pequenas-empresas/cobra-antes-cobros-y-tesoreria">cobrar antes y controlar la tesorería</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo cobrar una factura por WhatsApp?", "Enviando al cliente un enlace de pago asociado a esa factura. Lo abre en el móvil, paga con tarjeta en una pasarela segura y recibe el justificante. En tu programa la factura pasa a cobrada sin que tengas que revisar el banco."),
  ("¿Qué comisión tiene cobrar con un enlace de pago?", "La fija la pasarela de pago que elijas, no nosotros, y suele aplicarse a cada operación. Pídela por escrito antes de decidir y compárala con el tiempo que hoy dedicas a perseguir y cuadrar transferencias."),
 ],
}

# Estructura: separar tareas mecánicas de tareas de criterio + tabla de tres columnas + prueba de una semana con rayas
D["servicios/problemas-sin-resolver/empleado-digital"] = {
 "estructura": "mecanico-frente-a-criterio + tabla-encargar-revisar-reservar + prueba-de-una-semana",
 "lead": "Llevas meses con la oferta publicada y no encuentras a nadie para administración, o lo encuentras y no te salen las cuentas de una jornada completa. Entretanto, los correos y los pedidos se acumulan. Un empleado digital con IA para tareas de oficina cubre la parte repetitiva bajo la supervisión de tu equipo.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">El puesto que no consigues cubrir</p><h2>¿Qué hago con el trabajo de oficina que nadie tiene tiempo de hacer?</h2></div>
<p style="max-width:820px">Lo primero, separarlo en tareas, porque un puesto de oficina no es una sola cosa. Dentro hay trabajo mecánico —pasar un pedido, registrar una factura, contestar el horario— y trabajo de criterio: calmar a un cliente, negociar una entrega, notar que algo no cuadra. Un asistente virtual con inteligencia artificial sirve para lo primero. Quien te prometa lo segundo te está vendiendo humo.</p>
<h3 style="margin-top:28px">Qué se le puede encargar y qué no</h3>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Se lo puedes encargar</th><th>Solo con revisión de una persona</th><th>Sigue siendo de tu equipo</th></tr></thead><tbody>
<tr><td>Contestar preguntas frecuentes y dar cita</td><td>Borradores de presupuesto</td><td>Reclamaciones y clientes enfadados</td></tr>
<tr><td>Pasar al programa los pedidos que llegan por correo o WhatsApp</td><td>Registro de facturas de proveedores</td><td>Decidir precios, descuentos o plazos</td></tr>
<tr><td>Avisar de existencias bajas o confirmar una entrega</td><td>Respuestas a correos que se salen de lo habitual</td><td>Todo lo que comprometa dinero o tenga efecto legal</td></tr>
</tbody></table></div>
<p style="max-width:820px;margin-top:16px">La columna central es la que más se olvida. Al principio casi todo pasa por ella; con los meses, lo que el agente hace bien de forma repetida puede soltarse, y lo demás se queda donde está.</p>
<h3 style="margin-top:28px">La prueba de una semana</h3>
<ol style="max-width:820px">
<li>Durante cinco días, quien hoy hace ese trabajo apunta cada tarea con una raya: qué era y si necesitó pensar.</li>
<li>El viernes, separa las que se repiten idénticas de las que cambian cada vez.</li>
<li>Si las repetidas son un goteo que no llena media jornada, no necesitas un empleado digital: basta con <a href="/servicios/automatizacion-y-datos/automatizacion-de-administracion-facturas-y-cobros">automatizar una o dos tareas de administración</a>.</li>
<li>Si ocupan buena parte de un puesto, entonces sí tiene sentido definirlo como tal, con sus funciones y su supervisor.</li>
</ol>
<p style="max-width:820px">Un agente así no sustituye a una persona ni es una razón para prescindir de nadie: descarga a quien ya tienes para que atienda lo que sí necesita cabeza. Funciona sobre <a href="/servicios/pix/asistente-empresarial">PIX, nuestro asistente empresarial</a>, y como cualquier puesto necesita seguimiento; por eso existe el <a href="/servicios/agentes-de-ia/mantenimiento-de-agentes-y-automatizaciones">mantenimiento de agentes y automatizaciones</a>.</p>
</div></section>""",
 "faq": [
  ("¿Qué puede hacer un empleado digital con IA en una oficina?", "Tareas repetitivas con reglas claras: contestar consultas habituales, agendar citas, pasar pedidos al programa, registrar documentos o preparar borradores. Lo que exige criterio, negociación o una decisión con dinero de por medio lo deriva a una persona."),
  ("¿Un empleado digital sustituye a un administrativo?", "No. Asume la parte mecánica del puesto y deja a la persona el trato con clientes, las excepciones y la supervisión. En empresas donde nadie llega a todo, permite que el trabajo atrasado salga sin ampliar plantilla de inmediato."),
  ("¿Qué diferencia hay entre un chatbot y un empleado digital?", "Un chatbot responde preguntas. Un empleado digital, además, hace la gestión dentro de tus herramientas: crea la cita, da de alta el pedido o registra la factura, con permisos limitados y alguien que revisa sus excepciones."),
 ],
}

# Estructura: prueba con tu factura impagada más antigua (lista de comprobación) + tres momentos en que se gana la prueba (definiciones) + si la deuda ya existe
D["servicios/problemas-sin-resolver/expediente-de-reclamacion-listo"] = {
 "estructura": "comprobacion-con-tu-factura-mas-antigua + tres-momentos-de-la-prueba + si-la-deuda-ya-existe",
 "lead": "Decides por fin reclamar esa factura y el abogado te pide el presupuesto aceptado, los albaranes firmados y los avisos que enviaste. Buscas en correos, capturas de WhatsApp y carpetas, y falta justo lo importante. Tener el expediente de reclamación de deuda preparado te ahorra esa búsqueda.",
 "bloque": """<section class="sec sec-suave"><div class="w">
<div class="cab"><p class="kicker">Cuando toca reclamar en serio</p><h2>¿Reunirías hoy todos los papeles de una deuda en menos de una hora?</h2></div>
<p style="max-width:820px">La mayoría de las pequeñas empresas no, y no por desorden, sino porque cada prueba nació en un sitio distinto. El sí del cliente fue un audio, el albarán lo firmó un encargado en papel, la factura salió del programa y los recordatorios, del móvil del comercial. Mientras el cliente paga, no importa. Cuando deja de pagar, reconstruirlo lleva días, y esos días retrasan la decisión de reclamar.</p>
<h3 style="margin-top:28px">Haz la prueba con tu factura impagada más antigua</h3>
<ul class="lista" style="max-width:820px">
<li>¿Tienes por escrito que el cliente aceptó el encargo y el precio?</li>
<li>¿Puedes enseñar que entregaste o hiciste el trabajo, con fecha y firma o foto?</li>
<li>¿Coinciden los importes de presupuesto, albarán y factura, o hubo cambios de palabra?</li>
<li>¿Guardas cada aviso con su fecha y la respuesta, si la hubo?</li>
<li>¿Sabes quién de tu equipo habló con el cliente y qué se dijo?</li>
</ul>
<p style="max-width:820px">Cada «no» es un hueco que tu abogado tendrá que valorar. A nosotros no nos corresponde decirte cuánto pesa cada documento: eso es criterio jurídico. Lo que sí podemos hacer es que el hueco no llegue a producirse.</p>
<h3 style="margin-top:28px">Tres momentos en los que se gana o se pierde la prueba</h3>
<dl style="max-width:820px">
<dt><strong>Al aceptar el encargo</strong></dt><dd>Que el sí quede registrado: una aceptación desde el propio presupuesto o un <a href="/servicios/software-de-gestion/contratos-con-firma-online">contrato con firma online</a>.</dd>
<dt><strong>Al entregar</strong></dt><dd>Un <a href="/servicios/software-de-gestion/ordenes-y-partes-de-trabajo-con-firma-y-fotos">parte de trabajo con firma y fotos</a> hecho en el móvil, delante del cliente.</dd>
<dt><strong>Al vencer la factura</strong></dt><dd>Recordatorios enviados desde el programa y no desde un teléfono personal, para que queden fechados y juntos.</dd>
</dl>
<h3 style="margin-top:28px">Si la deuda ya existe</h3>
<p style="max-width:820px">También se puede preparar la documentación para reclamar un impago a posteriori, con lo que haya: se escanea, se ordena por fecha y se señala lo que falta, para que tu abogado o tu asesoría decidan con todo delante. Y para que haya menos expedientes que montar, conviene saber antes a quién se le sirve: de eso se ocupa el <a href="/servicios/problemas-sin-resolver/semaforo-de-clientes-morosos">semáforo de clientes morosos</a>.</p>
</div></section>""",
 "faq": [
  ("¿Qué hago si no tengo el albarán firmado de un trabajo que no me han pagado?", "Reúne cualquier otro rastro de que el trabajo se hizo: correos, fotos, mensajes, pagos parciales o pedidos posteriores, y enséñaselo a tu abogado, que es quien valora si basta. De ahora en adelante, recoge la firma en el móvil al terminar cada servicio."),
  ("¿Cuándo conviene pasar una factura impagada a un abogado?", "Es una decisión tuya y de tu asesor, y depende del importe, de la relación con el cliente y de lo que haya respondido. Tener el historial y los documentos ordenados te permite tomarla antes y con menos coste de preparación."),
 ],
}

# Estructura: lo que cuesta cada incorporación (sin cifras) + tabla de la primera semana antes/después + empezar con cinco preguntas
D["servicios/problemas-sin-resolver/formacion-rapida-de-nuevos-empleados"] = {
 "estructura": "coste-de-cada-incorporacion + tabla-primera-semana-antes-despues + empezar-con-cinco-preguntas",
 "lead": "Entra una persona nueva en plena temporada y la formación consiste en ponerla al lado de quien más sabe, que justo es quien menos tiempo tiene. A las tres semanas se defiende y a los dos meses se marcha. Formar rápido a un empleado nuevo con vídeos e IA corta ese círculo.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Enseñar lo mismo cada temporada</p><h2>¿Cuánto te cuesta cada persona nueva antes de que rinda?</h2></div>
<p style="max-width:820px">Bastante más de lo que marca su nómina. Durante los primeros días hay dos personas haciendo el trabajo de una: la que aprende y la que deja lo suyo para explicar. Si el negocio tiene rotación —hostelería, comercio, limpieza, campañas agrícolas—, esa explicación se repite varias veces al año y cada vez sale un poco distinta, según quién la dé.</p>
<p style="max-width:820px">No te damos una cifra, porque la cuenta es tuya: las horas que tu mejor empleado dedica a enseñar, por las incorporaciones del año, más los errores de las primeras semanas. Comandas mal tomadas, devoluciones mal hechas, partes incompletos.</p>
<h3 style="margin-top:28px">La primera semana, antes y después</h3>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Momento</th><th>Aprendiendo «a la sombra»</th><th>Con vídeos cortos y asistente</th></tr></thead><tbody>
<tr><td>Antes de empezar</td><td>Llega sin saber nada del local</td><td>Ha visto en el móvil lo básico: horarios, uniforme, caja</td></tr>
<tr><td>Primer día</td><td>Sigue a un compañero que va con prisa</td><td>Hace tareas sencillas y consulta el paso exacto cuando duda</td></tr>
<tr><td>Tercer día</td><td>Pregunta lo mismo a tres personas y recibe tres versiones</td><td>Pregunta al asistente y recibe la versión de la casa</td></tr>
<tr><td>Fin de la semana</td><td>Nadie sabe con certeza qué domina</td><td>Su responsable ha marcado lo que ya hace bien y lo que falta</td></tr>
</tbody></table></div>
<h3 style="margin-top:28px">Cómo empezar sin grabar un curso entero</h3>
<ol style="max-width:820px">
<li>Apunta las cinco preguntas que más repiten los recién llegados.</li>
<li>Graba la respuesta a cada una con el móvil, en el puesto y sin guion.</li>
<li>Pruébalo con la siguiente incorporación y anota qué volvió a preguntar.</li>
<li>Graba eso. El material crece con las dudas reales, no con un temario.</li>
</ol>
<p style="max-width:820px">Hay cosas que un vídeo no enseña. El trato con el cliente y la reacción ante un imprevisto se aprenden con alguien al lado; lo que se libera es el tiempo de ese alguien para enseñar justo eso.</p>
<h3 style="margin-top:28px">Según lo que necesites, quizá busques otra cosa</h3>
<ul class="lista" style="max-width:820px">
<li>Para dejar documentado el negocio entero, no solo la acogida: <a href="/servicios/relevo-y-continuidad/manual-de-operaciones-con-video-e-ia">manual de operaciones grabado en vídeo</a>.</li>
<li>Para un itinerario con contenidos y calendario: <a href="/servicios/formacion-ia/plan-de-formacion-para-nuevos-empleados">plan de formación para nuevos empleados</a>.</li>
<li>Para las consultas de cada día de toda la plantilla: <a href="/servicios/agentes-de-ia/asistente-interno-de-procedimientos">asistente interno de procedimientos</a>.</li>
</ul>
</div></section>""",
 "faq": [
  ("¿Cómo formar a un camarero o a un dependiente nuevo en pocos días?", "Enseñándole primero las pocas tareas que hará desde el primer turno, con un vídeo corto por tarea que pueda volver a ver, y dejando lo demás para cuando las domine. Una lista de la primera semana ayuda a que su responsable sepa en qué punto está."),
  ("¿Qué hago si el empleado nuevo no lee los manuales?", "Es lo normal: casi nadie lee un manual largo. Funciona mejor que pueda preguntar en el momento, desde el móvil, y reciba la respuesta concreta con el fragmento de vídeo que la explica."),
 ],
}

# Estructura: frases que se oyen en ventas (cita) + ejemplo hipotético de tres clientes en tarjetas + el color informa, no decide
D["servicios/problemas-sin-resolver/semaforo-de-clientes-morosos"] = {
 "estructura": "frases-de-ventas + ejemplo-hipotetico-tres-colores + el-color-informa-no-decide",
 "lead": "Hay un cliente simpático, de toda la vida, que siempre acaba pagando… a los cuatro meses. Y otro seco y exigente que paga el mismo día. La memoria confunde quién es quién. Un semáforo de clientes morosos lo aclara con sus fechas reales de pago antes de servirle otro pedido.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">La impresión no es un dato</p><h2>¿Cómo saber si un cliente paga tarde antes de volver a venderle?</h2></div>
<p style="max-width:820px">Mirando cuántos días tardó de verdad en sus últimas facturas, no lo bien que te cae. Parece evidente, pero en una pyme ese dato vive en administración y la venta la cierra otra persona, que lo que oye es esto:</p>
<blockquote style="max-width:820px">«A este sírvele, que es de confianza.»<br>«Ya pagará, siempre paga.»<br>«No le voy a decir que no por una factura.»</blockquote>
<h3 style="margin-top:28px">Tres clientes, tres colores</h3>
<p style="max-width:820px"><strong>Ejemplo hipotético</strong> de un almacén de materiales de construcción.</p>
<div class="rejilla">
<div class="tarjeta"><h3>Verde: el reformista del barrio</h3><p>Compra poco y a menudo, y paga en plazo desde hace años. Se le sirve sin preguntar.</p></div>
<div class="tarjeta"><h3>Ámbar: la constructora mediana</h3><p>Compra mucho y cada mes se retrasa un poco más. Nadie lo había notado porque «al final paga». El comercial recibe un aviso y los pedidos grandes salen con señal.</p></div>
<div class="tarjeta"><h3>Rojo: el que vuelve tras un año</h3><p>Dejó dos recibos devueltos y reaparece con un encargo urgente. En el mostrador ven la alerta y cobran por adelantado.</p></div>
</div>
<h3 style="margin-top:28px">El color informa, no decide</h3>
<p style="max-width:820px">Un control de morosidad de clientes como este no está para castigar a nadie ni para romper una relación por un retraso puntual. Sirve para que la conversación ocurra a tiempo y con datos: pedir una señal, acortar el plazo, llamar antes de que la deuda crezca. Qué se hace con cada color lo marcas tú, y siempre puedes saltarte la regla con un cliente concreto dejando anotado el motivo.</p>
<p style="max-width:820px">Tiene dos límites. Con un cliente nuevo no hay historial, así que el color todavía no dice nada. Y si atiendes a una docena de clientes y los cobros los ves tú cada semana, no lo necesitas: empieza a ser útil cuando vende más de una persona o la cartera ya no te cabe en la cabeza. El funcionamiento dentro del programa está en <a href="/servicios/software-de-gestion/cobros-impagos-y-semaforo-de-clientes">cobros, impagos y semáforo de clientes</a>; las reglas que se disparan con cada color, en el <a href="/servicios/problemas-sin-resolver/sistema-anti-impagos">sistema anti-impagos</a>; y lo que ocurre cuando ya hay que reclamar, en el <a href="/servicios/problemas-sin-resolver/expediente-de-reclamacion-listo">expediente de reclamación</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo detectar a un cliente moroso antes de que la deuda crezca?", "Midiendo en cada factura cuántos días pasan entre el vencimiento y el cobro, y fijándote en la tendencia. Un cliente que cada mes tarda algo más es una señal más útil que un retraso aislado, y se ve mucho antes de que la deuda sea grande."),
  ("¿Qué hago con un buen cliente que empieza a pagar tarde?", "Hablar pronto y con el dato en la mano. Suele haber una explicación —un cambio de persona, un problema de caja— y es más fácil pactar una señal o un plazo distinto cuando la deuda es pequeña que cuando ya se han acumulado varias facturas."),
 ],
}

# Estructura: cómo nace un impago en cinco silencios (lista numerada) + estados de una factura (definiciones) + cómo sabrás si funciona
D["servicios/problemas-sin-resolver/sistema-anti-impagos"] = {
 "estructura": "cinco-silencios-que-acaban-en-impago + estados-de-la-factura + como-sabras-si-funciona",
 "lead": "Cuando por fin llamas para reclamar, la factura lleva tres meses vencida, el cliente ya no recuerda el trabajo y a ti te da apuro insistir. Un sistema anti-impagos para autónomos y pymes actúa mucho antes: ordena los vencimientos, avisa a tiempo y te reserva las decisiones delicadas.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">El impago no empieza el día que reclamas</p><h2>¿En qué momento se convierte una factura en un problema?</h2></div>
<p style="max-width:820px">Mucho antes de la primera llamada incómoda. Casi ningún impago nace de un cliente que decide no pagar: nace de pequeños silencios encadenados.</p>
<ol style="max-width:820px">
<li>La factura se envía a un correo genérico y nadie confirma que ha llegado.</li>
<li>Vence, y nadie lo mira porque esa semana hay mucho trabajo.</li>
<li>Ventas da por hecho que administración ya ha llamado; administración cree que lo hará el comercial, que es quien tiene la relación.</li>
<li>Pasa un mes. Reclamar ahora resulta violento, así que se espera «a ver si entra».</li>
<li>Llega un pedido nuevo de ese mismo cliente y se sirve.</li>
</ol>
<h3 style="margin-top:28px">Antes de programar avisos, define las excepciones</h3>
<p style="max-width:820px">Reducir los impagos de clientes no consiste en mandar más mensajes, sino en mandar el adecuado según lo que esté ocurriendo. Para eso cada factura necesita un estado claro.</p>
<dl style="max-width:820px">
<dt><strong>Próxima a vencer</strong></dt><dd>Recordatorio cordial con los datos de pago.</dd>
<dt><strong>Vencida</strong></dt><dd>Segundo aviso, y alguien de tu equipo mira el contexto antes del tercero.</dd>
<dt><strong>En revisión</strong></dt><dd>El cliente ha comunicado un error o una incidencia. Los avisos se detienen hasta resolverla.</dd>
<dt><strong>Con promesa de pago</strong></dt><dd>Hay una fecha comprometida. Silencio hasta ese día.</dd>
<dt><strong>Para reclamación formal</strong></dt><dd>Lo decides tú con tu abogado o tu asesoría. Aquí el sistema solo aporta el historial.</dd>
</dl>
<h3 style="margin-top:28px">Cómo sabrás si está funcionando</h3>
<ul class="lista" style="max-width:820px">
<li>Baja la antigüedad media de lo que tienes pendiente, medida con tus propios datos.</li>
<li>Te enteras de cada vencimiento la misma semana, no al cerrar el trimestre.</li>
<li>Ya no se sirve a ciegas a quien debe: lo avisa el <a href="/servicios/problemas-sin-resolver/semaforo-de-clientes-morosos">semáforo de clientes</a>.</li>
<li>Las conversaciones difíciles ocurren antes y duran menos.</li>
</ul>
<p style="max-width:820px">Lo que no hará: asegurar que todos paguen, sustituir a un abogado ni decidir por ti cuánto riesgo asumes con cada cliente. Si quieres que una IA redacte y envíe los recordatorios con tu tono, eso lo cubre el <a href="/servicios/agentes-de-ia/cobros-e-impagos">agente de cobros e impagos</a>; y si lo que falla es la comodidad del pago, empieza por los <a href="/servicios/problemas-sin-resolver/cobro-facil-con-enlaces-de-pago">enlaces de pago</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo reducir los impagos de clientes en una pyme?", "Actuando antes del vencimiento: condiciones claras en el presupuesto, factura enviada el mismo día, recordatorio previo y un responsable que revise cada semana lo pendiente. La mayoría de los retrasos se resuelven con orden; los pocos que no, se detectan pronto y se reclaman con todo documentado."),
  ("¿Reclamar un pago por WhatsApp o por correo estropea la relación con el cliente?", "No si el mensaje es breve, educado y llega a tiempo. Lo que deteriora la relación es el silencio largo seguido de un aviso brusco. Un recordatorio antes de la fecha, con los datos para pagar, suele agradecerse."),
  ("¿Cuándo no necesito un sistema anti-impagos?", "Si cobras al contado o en el momento de entregar, o si tienes pocos clientes y revisas tú los cobros cada semana, te basta con una lista de facturas pendientes. Compensa cuando hay pago aplazado, cuotas o varias personas vendiendo."),
 ],
}

# Estructura: escena de las siete y diez + tres formas de llevar el cuadrante + acuerdos previos con la plantilla
D["servicios/problemas-sin-resolver/turnos-y-ausencias-integrados"] = {
 "estructura": "escena-siete-y-diez + tres-formas-de-llevar-el-cuadrante + acuerdos-previos-con-la-plantilla",
 "lead": "A las siete y diez te escribe una empleada: tiene fiebre y no puede ir. Abres el cuadrante, miras quién libra, llamas a tres personas y, mientras, la primera cita ya está esperando. Cubrir ausencias de empleados sin rehacer el cuadrante es posible cuando turnos, fichaje y agenda están conectados.",
 "bloque": """<section class="sec sec-suave"><div class="w">
<div class="cab"><p class="kicker">Siete y diez de la mañana</p><h2>¿Quién cubre el turno cuando alguien avisa a última hora?</h2></div>
<p style="max-width:820px">Hoy, quien tú consigas localizar. Lo difícil de una baja imprevista no es la baja, que es inevitable, sino que la información para resolverla está en sitios distintos: el cuadrante en una hoja colgada o en Excel, las vacaciones en un grupo de WhatsApp, las citas en la agenda y quién sabe hacer cada cosa, en tu memoria. Te toca cruzarlo a ti, deprisa y con el teléfono en la mano.</p>
<h3 style="margin-top:28px">Tres formas de llevar el cuadrante y qué pasa cuando falta alguien</h3>
<ul class="lista" style="max-width:820px">
<li><strong>En papel o en la pizarra.</strong> Lo ve quien está en el local. Un cambio se tacha y quien libra no se entera.</li>
<li><strong>En una hoja de cálculo compartida.</strong> Queda ordenado, pero no sabe quién ha fichado, quién está de vacaciones ni qué citas dependen de ese turno.</li>
<li><strong>Unido al fichaje y a la agenda.</strong> Al marcar la ausencia aparecen los servicios afectados y las personas disponibles que saben hacerlos.</li>
</ul>
<p style="max-width:820px">Con las dos primeras, además, casi siempre acabas llamando a la misma persona, la que nunca dice que no. A la larga, eso también tiene un precio.</p>
<h3 style="margin-top:28px">Lo que conviene acordar con la plantilla antes de activarlo</h3>
<ol style="max-width:820px">
<li>Por qué canal y hasta qué hora se avisa de una ausencia.</li>
<li>Quién puede aceptar una sustitución y cómo se reparten, para que no recaigan siempre en los mismos.</li>
<li>Qué se hace con las horas de más, según lo que diga vuestro convenio.</li>
<li>Quién decide cuando el sistema no encuentra a nadie.</li>
</ol>
<p style="max-width:820px">El programa propone y el responsable decide. No conoce la situación personal de cada uno ni reemplaza la conversación con el equipo, y todo lo relativo a descansos y jornadas debe ajustarse a vuestro convenio con el criterio de tu asesoría laboral. En plantillas de tres o cuatro personas que se organizan hablando, no hace falta. Si lo que buscas es solo planificar, tienes <a href="/servicios/fichador/turnos-y-cuadrantes">turnos y cuadrantes</a> y <a href="/servicios/fichador/vacaciones-y-ausencias">vacaciones y ausencias</a> dentro del fichador; y para avisar a los clientes cuya cita se mueve, las <a href="/servicios/whatsapp-ia/citas-y-recordatorios-automaticos">citas y recordatorios por WhatsApp</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo cubrir una baja de última hora sin llamar a toda la plantilla?", "Con un cuadrante que sepa quién está libre, quién ha fichado y quién tiene la cualificación para ese puesto. Al registrar la ausencia propone candidatos y envía la petición solo a ellos; el primero que acepta queda asignado y el resto recibe el aviso de que ya está cubierto."),
  ("¿Qué programa sirve para organizar turnos y vacaciones en una empresa pequeña?", "Uno que reúna en el mismo sitio el cuadrante, las solicitudes de vacaciones y el registro de jornada, y que cada empleado pueda consultar desde el móvil. Si además trabajas con cita o con rutas, conviene que esté conectado a la agenda para ver qué servicios afecta cada ausencia."),
 ],
}
