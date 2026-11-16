# Reescritura «dolores primero» · artículos de blog (noviembre 2026).
# El bloque va SIN <section> porque se inserta dentro del artículo, antes del primer H2.
D = {}

# Estructura: cuándo Excel deja de bastar + frase de oficina + tabla de tres etapas + lo que no conviene hacer + cuándo esperar
D["blog/que-es-un-erp-y-cuando-lo-necesito"] = {
 "estructura": "frase-de-oficina + tabla-de-tres-etapas + lo-que-no-conviene-hacer + cuando-esperar",
 "lead": "El Excel de pedidos lo abre una persona y los demás esperan. Hay tres versiones del mismo archivo, ninguna es la buena, y el viernes alguien dedica la tarde a cuadrarlas. Si te preguntas qué es un ERP y cuándo lo necesita una pyme, seguramente ya has notado que la hoja de cálculo se ha quedado corta.",
 "bloque": """<h2>¿En qué momento Excel deja de ser suficiente para llevar una empresa?</h2>
<p>Deja de serlo cuando más de una persona necesita el mismo dato a la vez y ese dato cambia varias veces al día. Hasta entonces la hoja de cálculo es una herramienta excelente. El problema no es Excel: es pedirle que haga de sistema compartido.</p>
<blockquote>«¿Cuál es el archivo bueno, el del escritorio o el que me mandaste ayer?»</blockquote>
<p>Si esa pregunta se oye en tu oficina cada semana, estás en el punto de cambio. Si no, quizá te baste con ordenar lo que tienes.</p>
<h3>Tres etapas y lo que pide cada una</h3>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Etapa</th><th>Cómo se nota</th><th>Qué suele hacer falta</th></tr></thead><tbody>
<tr><td>Trabajas solo o sois dos</td><td>Todo está en tu cabeza y en un par de hojas</td><td>Orden y copias de seguridad; nada más</td></tr>
<tr><td>Varias personas tocan pedidos, compras o facturas</td><td>Se pisan cambios y se duplican datos</td><td>Un programa de gestión compartido, con los módulos justos</td></tr>
<tr><td>Hay almacén, producción o varias sedes</td><td>Las decisiones dependen de datos que tardan días</td><td>Un ERP implantado por fases</td></tr>
</tbody></table></div>
<h3>Lo que conviene no hacer</h3>
<ul>
<li>Comprar el programa más completo «para no quedarnos cortos». Se paga lo que no se usa y abruma al equipo.</li>
<li>Pasar todas las hojas al programa tal cual. Muchas existen solo para tapar un hueco que el sistema ya cubre.</li>
<li>Cambiarlo todo el mismo día. Mejor un área que funcione, y luego la siguiente.</li>
<li>Decidirlo sin contar con quien lo va a usar.</li>
</ul>
<h3>Cuándo esperar</h3>
<p>Si tu empresa está cambiando de modelo, de local o de socios, espera a que se asiente. Un ERP fija una forma de trabajar; conviene que sea la que vas a tener, no la que estás dejando.</p>
<p>Para dar el paso con calma tienes <a href="/blog/como-dejar-de-usar-excel-en-mi-empresa">cómo dejar de usar Excel en tu empresa</a> y, si ya lo has decidido, la <a href="/servicios/erp-para-pymes/migracion-desde-excel-u-otro-programa">migración desde Excel u otro programa</a>. La diferencia con el programa comercial la explicamos en <a href="/guias/erp-vs-crm">ERP y CRM</a>.</p>""",
 "faq": [
  ("¿Cuándo dejar de usar Excel y pasar a un ERP?", "Cuando varias personas necesitan el mismo dato a la vez, aparecen versiones distintas del mismo archivo o alguien dedica horas cada semana a cuadrar hojas. Si trabajas solo y el volumen es bajo, Excel bien ordenado sigue siendo válido."),
  ("¿Qué diferencia hay entre un programa de facturación y un ERP?", "El programa de facturación emite facturas y controla cobros. El ERP une además compras, existencias, pedidos, producción o proyectos, de modo que una venta actualiza todo lo demás sin volver a teclear."),
 ],
}

# Estructura: tareas que empiezan por «acuérdate de» + localizarlas en media hora + una regla escrita + qué no automatizar
D["blog/software-de-gestion-modular-con-automatizaciones"] = {
 "estructura": "tareas-acuerdate-de + localizarlas-en-media-hora + regla-escrita-con-revision-humana + que-no-automatizar",
 "lead": "Cada lunes alguien copia los pedidos de la semana, avisa a los clientes con factura vencida y prepara el mismo informe de siempre. Si esa persona falta, no se hace. Un software de gestión modular con automatizaciones sirve para que esas tareas repetidas ocurran solas, y para que seas tú quien decide cuáles.",
 "bloque": """<h2>¿Qué tareas de la oficina se repiten cada semana y dependen de una sola persona?</h2>
<p>Casi todas las que empiezan por «acuérdate de…». Avisar, copiar, recordar, pasar un dato de un sitio a otro. No requieren criterio, pero sí que alguien esté disponible, y por eso fallan en vacaciones, en bajas y en semanas de mucho trabajo.</p>
<h3>Cómo localizar las tuyas en media hora</h3>
<ol>
<li>Pide a cada persona que apunte lo que hace siempre igual, cada día o cada semana.</li>
<li>Marca las que siguen una regla clara: «si pasa esto, hago aquello».</li>
<li>Descarta las que necesitan valorar un caso: esas siguen siendo de una persona.</li>
<li>Ordena las que quedan por tiempo que consumen y por lo que cuesta un olvido.</li>
</ol>
<p>La primera de la lista es tu candidata. Empieza por una sola.</p>
<h3>Una regla escrita, de principio a fin</h3>
<p>Ejemplo hipotético: una empresa de mantenimiento de ascensores quiere dejar de perseguir facturas vencidas. La regla, en sus propias palabras, sería: «cuando una factura lleve diez días vencida, envía un recordatorio amable al cliente; si a los veinte sigue sin pagarse, avisa a administración y no mandes nada más». La primera parte la ejecuta el programa. La segunda la decide una persona, que conoce al cliente y sabe si conviene llamar.</p>
<h3>Lo que no conviene automatizar</h3>
<ul>
<li>Lo que hoy se hace de tres maneras distintas: primero hay que ponerse de acuerdo.</li>
<li>Decisiones con dinero o con trato delicado, salvo como aviso.</li>
<li>Lo que ocurre dos veces al año: no compensa.</li>
<li>Cualquier cosa cuyo resultado nadie vaya a revisar las primeras semanas.</li>
</ul>
<blockquote>Una automatización bien puesta no quita a nadie de en medio: quita los «se me pasó».</blockquote>
<p>Que el programa sea modular importa aquí por una razón práctica: activas solo la parte donde está esa tarea (ventas, facturas, agenda) y las reglas trabajan con datos que ya están dentro. Tienes más ideas en <a href="/blog/tareas-que-puedes-automatizar">tareas que puedes automatizar</a> y el detalle de cobros en <a href="/servicios/software-de-gestion/cobros-impagos-y-semaforo-de-clientes">cobros, impagos y semáforo de clientes</a>. El conjunto está en <a href="/servicios/software-de-gestion">software de gestión modular</a>.</p>""",
 "faq": [
  ("¿Qué tareas administrativas se pueden automatizar en una pequeña empresa?", "Las que siguen una regla clara y se repiten: recordatorios de cobro, avisos de cita, informes periódicos, altas de clientes desde un formulario o el paso de presupuesto a factura. Las que requieren valorar un caso deben seguir en manos de una persona."),
  ("¿Cómo saber si necesito un software de gestión modular o me basta con el que tengo?", "Mira si tu programa actual te deja activar solo lo que usas y crear tus propias reglas. Si para cada cambio dependes del fabricante o acabas con hojas de cálculo paralelas, uno modular te dará más margen."),
 ],
}
