# Reescritura «dolores primero» · familia la IA empresarial (noviembre 2026).
# Aquí se habla de capacidades del producto; los casos de uso concretos viven en /servicios/agentes-de-ia/… y se enlazan.
D = {}

# Estructura: síntomas de «tarea automatizada, proceso roto» + tabla tarea suelta frente a flujo + cuándo un flujo es demasiado
D["servicios/pix/flujos-de-trabajo"] = {
 "estructura": "sintomas-de-proceso-a-trozos + tabla-tarea-suelta-vs-flujo + cuando-es-demasiado",
 "lead": "Tienes un formulario que envía un correo, una plantilla para los presupuestos y un recordatorio automático, y aun así alguien copia datos de un sitio a otro todas las mañanas. Lo automatizado son tareas sueltas; el hueco entre ellas lo sigue rellenando una persona. Automatizar procesos completos con IA consiste en cerrar esos huecos.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Automatizaciones que no se hablan</p><h2>¿Por qué sigues haciendo trabajo manual si ya tienes cosas automatizadas?</h2></div>
<p style="max-width:820px">Porque cada herramienta resuelve su trozo y nadie se ocupa del recorrido entero. Se reconoce por detalles como estos:</p>
<ul class="lista" style="max-width:820px">
<li>El aviso llega, pero después hay que abrir tres programas para actuar.</li>
<li>Un paso depende de que alguien «se acuerde de darle al botón».</li>
<li>Cuando falta un dato, el proceso se queda parado sin que nadie se entere.</li>
<li>Para saber en qué punto está un asunto hay que preguntar a dos personas.</li>
<li>Las aprobaciones se dan por mensaje y luego no se encuentran.</li>
</ul>
<h3 style="margin-top:28px">Una tarea automática y un flujo no son lo mismo</h3>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th></th><th>Tarea automatizada</th><th>Flujo completo en la IA empresarial</th></tr></thead><tbody>
<tr><td>Alcance</td><td>Un paso: enviar, copiar, recordar</td><td>Desde lo que lo origina hasta el resultado registrado</td></tr>
<tr><td>Si falta información</td><td>Falla o envía algo incompleto</td><td>La pide, espera y continúa, o avisa a quien corresponde</td></tr>
<tr><td>Decisiones</td><td>No las contempla</td><td>Se detiene en los puntos de aprobación que hayas marcado</td></tr>
<tr><td>Seguimiento</td><td>Hay que mirar herramienta por herramienta</td><td>Cada caso muestra en qué paso está y quién lo tiene</td></tr>
<tr><td>Cuando cambia el negocio</td><td>Se rompe en silencio</td><td>Se ajusta el paso afectado; el resto sigue igual</td></tr>
</tbody></table></div>
<p style="max-width:820px;margin-top:18px">La diferencia práctica es que la IA interpreta lo que llega (un correo escrito de cualquier manera, un documento, una nota de voz) y decide qué paso toca, algo que las reglas fijas no hacen. Esa misma flexibilidad es su punto débil: puede interpretar mal. Por eso cada flujo lleva puntos de control humano y deja rastro de lo que hizo.</p>
<h3 style="margin-top:28px">Cuándo un flujo es matar moscas a cañonazos</h3>
<p style="max-width:820px">Si el proceso ocurre dos veces al mes, si cada caso es distinto del anterior o si ni siquiera en tu equipo os ponéis de acuerdo en cómo se hace, no lo automatices todavía: escríbelo primero. Tampoco tiene sentido encadenar pasos sobre datos que no son fiables. Lo habitual es empezar por un solo recorrido, medirlo durante unas semanas y ampliar después. Ejemplos ya desarrollados: <a href="/servicios/agentes-de-ia/presupuestos-automaticos">presupuestos automáticos con IA</a> y <a href="/servicios/agentes-de-ia/agentes-que-gestionan-pedidos-presupuestos-o-incidencias-de-principio-">agentes que gestionan pedidos e incidencias</a>. Con qué programas puede trabajar cada paso lo tienes en <a href="/servicios/pix/integraciones">integraciones de la IA empresarial</a>, y qué acciones exigen tu aprobación, en <a href="/servicios/pix/seguridad-y-control">seguridad y control</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo automatizar un proceso entero de mi empresa y no solo una tarea?", "Dibujando primero el recorrido completo: qué lo inicia, qué datos necesita cada paso, quién aprueba y dónde queda registrado el resultado. Con ese mapa, la IA empresarial encadena los pasos, pide lo que falta y se detiene donde has decidido que intervenga una persona."),
  ("¿Qué pasa si la IA toma una decisión equivocada en mitad de un flujo?", "Las acciones sensibles no se ejecutan sin aprobación, y todo lo que hace queda registrado con el dato en que se basó. Si un paso sale mal, se puede ver dónde, corregir el caso y ajustar la instrucción para que no se repita."),
  ("¿Cuánto se tarda en poner en marcha el primer flujo de trabajo con la IA empresarial?", "El primer flujo suele plantearse como un piloto de unas cuatro semanas. La mayor parte del tiempo se va en acordar cómo es el proceso y en conectar los programas, no en la configuración de la IA."),
 ],
}

# Estructura: tres perfiles en tarjetas según lo que ya usan + preguntas previas a cada conexión (definiciones)
D["servicios/pix/integraciones"] = {
 "estructura": "tarjetas-por-punto-de-partida + preguntas-previas-en-definiciones",
 "lead": "El cliente está en el CRM, sus correos en Outlook, el presupuesto en una hoja de cálculo y lo que te dijo por WhatsApp, en tu móvil. Para contestarle abres cuatro ventanas. Las integraciones de la IA empresarial con Gmail, Outlook, WhatsApp, CRM y API sirven para que un asistente consulte todo eso por ti, con los permisos que marques.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Cuatro programas, cuatro verdades</p><h2>¿Tus programas no se hablan y eres tú quien hace de cable?</h2><p class="lead" style="margin-top:8px">Copiar un dato de una pantalla a otra no es trabajar: es suplir una conexión que falta.</p></div>
<div class="rejilla">
<div class="tarjeta"><h3>Trabajas con correo, calendario y hojas de cálculo</h3><p>Es el punto de partida más común en autónomos y negocios pequeños. Se conecta primero la cuenta de Google o de Microsoft y con eso ya hay agenda, documentos y bandeja.</p></div>
<div class="tarjeta"><h3>Tienes un CRM o un programa de facturación</h3><p>La pregunta es si permite conexiones. Si es de los habituales, suele bastar con autorizarlo; si es sectorial, hay que mirar su documentación.</p></div>
<div class="tarjeta"><h3>Usas un programa antiguo o hecho a medida</h3><p>Aquí no hay respuesta rápida. A veces existe una API, a veces solo exportaciones de archivos y a veces nada, y hay que decírtelo antes de presupuestar.</p></div>
</div>
<h3 style="margin-top:30px">Lo que conviene preguntarse antes de conectar cada herramienta</h3>
<dl style="max-width:820px">
<dt><strong>¿Leer o también escribir?</strong></dt><dd>Consultar un calendario es inocuo; crear, modificar o borrar citas no. Se empieza por lectura y se amplía con casos probados.</dd>
<dt><strong>¿Con qué usuario entra?</strong></dt><dd>Mejor una cuenta propia y con permisos recortados que la del gerente con acceso a todo.</dd>
<dt><strong>¿Qué datos personales hay ahí?</strong></dt><dd>Si el programa guarda datos de clientes, pacientes o empleados, la conexión debe encajar con tu documentación de protección de datos. Eso se revisa contigo antes.</dd>
<dt><strong>¿Qué pasa si el otro programa cambia?</strong></dt><dd>Las conexiones se rompen cuando un fabricante actualiza su servicio. No es raro y no depende de nosotros; por eso se vigilan.</dd>
<dt><strong>¿De verdad hace falta?</strong></dt><dd>Cada integración añade mantenimiento. Conectar por conectar complica más que ayuda.</dd>
</dl>
<p style="max-width:820px">Que una herramienta aparezca en la lista de compatibles significa que la conexión existe, no que cualquier cosa sea posible con ella: lo que se puede hacer depende de lo que cada fabricante permite y del plan que tengas contratado. Por eso comprobamos tu caso concreto antes de darte un precio. Si lo que necesitas es unir programas entre sí sin asistente de por medio, ese trabajo es <a href="/servicios/migraciones-e-integraciones/conectar-erp-tienda-crm-y-contabilidad">conectar ERP, tienda, CRM y contabilidad</a>; si estás pensando en dejar de tener tantos, <a href="/servicios/migraciones-e-integraciones/unificar-varios-programas-en-uno">unificar varios programas en uno</a>. Un uso típico de estas conexiones es <a href="/servicios/agentes-de-ia/clasificacion-y-respuesta-de-correos">clasificar y responder correos con IA</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo saber si mi programa de gestión se puede conectar con un asistente de IA?", "Buscando en su documentación o preguntando al fabricante si ofrece una API o, al menos, exportación e importación de datos. Con el nombre del programa y la versión lo comprobamos nosotros en el diagnóstico, antes de presupuestar."),
  ("¿Qué pasa si una integración de la IA empresarial deja de funcionar tras una actualización?", "El flujo afectado se detiene y salta un aviso. Se revisa qué cambió en el programa conectado y se adapta la conexión; mientras tanto, los pasos que dependen de ella quedan en espera o se hacen a mano."),
 ],
}

# Estructura: miedos en frases literales + preguntas para exigir a cualquier agente + lo que el control no cubre
D["servicios/pix/seguridad-y-control"] = {
 "estructura": "miedos-en-primera-persona + preguntas-exigibles-numeradas + lo-que-no-cubre",
 "lead": "Te gustaría que una IA respondiese correos y moviese datos por ti, pero te frena una idea muy sensata: ¿y si manda algo que no debe, o ve lo que no le toca? La seguridad y el control humano en un agente de IA deciden si puedes delegar tranquilo o si acabarás revisándolo todo dos veces.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Desconfiar es lo razonable</p><h2>¿Qué te impide dejar que un agente de IA actúe en tu empresa?</h2></div>
<ul class="lista" style="font-size:18px;max-width:820px">
<li>«No quiero que conteste a un cliente importante sin que yo lo vea.»</li>
<li>«¿Y si un empleado le pregunta por las nóminas de los demás?»</li>
<li>«He leído que estas IA se inventan cosas.»</li>
<li>«Si algo sale mal, ¿cómo sé qué hizo y por qué?»</li>
</ul>
<p style="max-width:820px;margin-top:18px">Son las preguntas correctas. Un agente que actúa en tus programas no es un chat de consulta: puede enviar, modificar y borrar. La confianza no viene de que el proveedor te diga que es seguro, sino de que puedas comprobar qué tiene permitido.</p>
<h3 style="margin-top:28px">Seis cosas que deberías poder exigir a cualquier agente, no solo a la IA empresarial</h3>
<ol style="max-width:820px">
<li>Una lista clara de a qué programas y carpetas accede, y poder recortarla.</li>
<li>Diferenciar entre lo que puede leer y lo que puede cambiar.</li>
<li>Que las acciones delicadas (pagos, envíos masivos, borrados, respuestas a reclamaciones) esperen a una persona.</li>
<li>Un historial de cada acción con fecha, usuario que la pidió y datos utilizados.</li>
<li>Un botón para pararlo todo.</li>
<li>Condiciones de tratamiento de datos por escrito, no en un folleto.</li>
</ol>
<h3 style="margin-top:28px">Lo que ningún panel de control hace por ti</h3>
<p style="max-width:820px">Los permisos y las aprobaciones reducen el riesgo; no lo eliminan. Una IA puede redactar con aplomo un dato incorrecto, y si quien aprueba pulsa «aceptar» sin leer, el control humano es decorativo. También hay límites que no son técnicos: una contraseña compartida entre compañeros, un administrador que nadie sustituye en vacaciones o permisos que se dieron «de momento» y nunca se retiraron.</p>
<p style="max-width:820px">Por eso recomendamos empezar con poco: un proceso, acceso de lectura, aprobación para todo lo que salga de la empresa y una revisión mensual de qué se ha concedido. Los permisos se amplían cuando los casos reales lo justifican. Si tu preocupación es dónde residen los datos, mira la <a href="/servicios/agentes-de-ia/ia-en-servidor-propio">IA en servidor propio o dedicado</a>; para las normas que debe seguir la plantilla, la <a href="/servicios/formacion-ia/politica-de-uso-de-ia-para-empresas">política de uso de IA para empresas</a>; y si necesitas a alguien que vigile la seguridad de todos tus sistemas, existe el <a href="/servicios/ciberseguridad-y-sistemas/responsable-de-ciberseguridad-externalizado">responsable de ciberseguridad externalizado</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo dejar que una IA trabaje con mis datos sin perder el control de lo que hace?", "Dándole acceso solo a lo imprescindible, separando lectura de escritura, exigiendo aprobación humana para las acciones sensibles y revisando el registro de actividad. Se empieza con permisos mínimos y se amplían a medida que se comprueba cómo responde."),
  ("¿Quién responde si el agente de IA comete un error con un cliente?", "Ante el cliente responde tu empresa, igual que si el error lo cometiera un empleado. Por eso importa decidir qué puede hacer solo el agente y qué necesita revisión, y conservar el registro que permite ver qué ocurrió y corregirlo."),
  ("¿Cuánto trabajo le supone al administrador supervisar la IA empresarial?", "Al principio más, porque conviene revisar a diario lo que se aprueba y cómo responde. Una vez estable, suele bastar con atender las aprobaciones pendientes y repasar permisos y actividad de forma periódica."),
 ],
}
