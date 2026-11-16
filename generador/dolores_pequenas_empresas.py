# Reescritura «dolores primero» · familia Pequeñas empresas (noviembre 2026).
# Siete páginas, siete recorridos: cuenta propia, mitos, glosario, perfiles, señales, inventario y tropiezos.
D = {}

# Estructura: cuenta con tus propios números (lista numerada) + tabla de cuatro maneras de facturar + qué se deja con revisión
D["servicios/pequenas-empresas/ahorra-horas-programa-de-gestion-y-facturas-automaticas"] = {
 "estructura": "cuenta-de-horas-propias + tabla-cuatro-maneras-de-facturar + revision-humana",
 "lead": "Si el viernes por la tarde alguien de tu empresa sigue pasando albaranes a facturas y copiando el mismo cliente de un documento a otro, el fallo no es de la persona, sino del método. Un programa de gestión con facturas automáticas hace ese traslado y os deja solo la revisión.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Antes de mirar ningún programa</p><h2>¿Cuántas horas al mes se os van en teclear facturas?</h2><p class="lead" style="margin-top:8px">Sácalo con vuestros datos; se tarda menos que en hacer una factura.</p></div>
<ol style="max-width:820px">
<li>Cuenta las facturas que emitisteis el mes pasado.</li>
<li>Cronometra tres de principio a fin: buscar el albarán o el parte, copiar los datos, generar el PDF, enviarlo y anotarlo.</li>
<li>Multiplica el tiempo medio por el número de facturas.</li>
<li>Añade las que hubo que rehacer por un error de copia: un precio antiguo, un albarán olvidado, un cliente equivocado.</li>
</ol>
<p style="max-width:820px;margin-top:18px">Ese resultado es vuestro y no una media del sector. Si sale una mañana al mes, quizá no os haga falta cambiar nada. Si sale una semana entera de una persona, la facturación automática se paga sola en tiempo recuperado, y además deja de depender de que esa persona no falte a final de mes.</p>
<h3 style="margin-top:30px">Cuatro maneras de facturar y dónde se rompe cada una</h3>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Cómo facturáis</th><th>Va bien cuando</th><th>Empieza a fallar cuando</th></tr></thead><tbody>
<tr><td>Plantilla de Word o PDF</td><td>Hay pocas facturas y pocos clientes</td><td>Toca numerar, buscar una antigua o rectificar</td></tr>
<tr><td>Hoja de Excel con fórmulas</td><td>Una persona la domina y la lleva sola</td><td>Esa persona falta o dos abren el archivo a la vez</td></tr>
<tr><td>Programa de facturación genérico</td><td>Vendéis siempre lo mismo al mismo precio</td><td>Aparecen partes, cuotas, tarifas por cliente o albaranes agrupados</td></tr>
<tr><td>Software de gestión adaptado</td><td>El dato nace en el presupuesto o en el parte y llega solo a la factura</td><td>Nadie revisa: automatizar no elimina el visto bueno</td></tr>
</tbody></table></div>
<h3 style="margin-top:30px">Automático no quiere decir sin control</h3>
<p style="max-width:820px">Lo prudente es arrancar con todas las facturas en borrador y que alguien las apruebe en bloque. Con las semanas, la revisión se limita a las excepciones: el cliente con precio especial, el trabajo que se alargó, la cuota que este mes no toca. El detalle de cada pieza está en <a href="/servicios/software-de-gestion/presupuestos-que-pasan-a-pedido-y-factura">presupuestos que pasan a pedido y factura</a> y en <a href="/servicios/software-de-gestion/bonos-cuotas-y-suscripciones">cuotas y suscripciones</a>. Si hoy vivís en hojas de cálculo, el paso previo es la <a href="/servicios/migraciones-e-integraciones/migracion-de-excel-a-programa-de-gestion">migración de Excel a un programa de gestión</a>, que se hace por partes para no parar la actividad.</p>
</div></section>""",
 "faq": [
  ("¿Cómo dejar de pasar albaranes a facturas a mano?", "Haciendo que el albarán y la factura salgan del mismo dato. Cuando el pedido o el parte se cierra en el programa, la factura se genera con esas líneas y solo hay que aprobarla. También puede agrupar todos los albaranes del mes de un cliente en una sola."),
  ("¿Merece la pena un programa de gestión si hago pocas facturas al mes?", "No siempre. Con pocas facturas y clientes fijos, una plantilla ordenada puede bastar. Empieza a compensar cuando hay cuotas, precios distintos por cliente o varias personas tocando los mismos datos, y los errores de copia se repiten."),
  ("¿Cuánto se tarda en empezar a facturar con un programa nuevo?", "Depende sobre todo de cómo estén tus datos de clientes, artículos y precios. Antes de empezar recibes las fases y las fechas por escrito, y lo habitual es poner en marcha primero la facturación y dejar el resto para después."),
 ],
}

# Estructura: tres mitos frente a realidad (tarjetas) + seis preguntas de autodiagnóstico + orden de actuación
D["servicios/pequenas-empresas/cobra-antes-cobros-y-tesoreria"] = {
 "estructura": "mito-realidad-en-tarjetas + seis-preguntas-de-autodiagnostico + ver-acortar-poner-reglas",
 "lead": "Tienes trabajo, facturas bien y aun así a final de mes miras la cuenta con el estómago encogido, porque las nóminas salen antes de que los clientes paguen. Cobrar antes y controlar la tesorería de tu pyme empieza por saber qué día entra cada importe, no por reclamar más fuerte.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Vender no es lo mismo que cobrar</p><h2>¿Por qué falta dinero en la cuenta si el negocio va bien?</h2></div>
<p style="max-width:820px">Porque el beneficio se mide en facturas y la caja se mide en fechas. Una empresa puede ganar dinero sobre el papel y no llegar a fin de mes si paga a proveedores y plantilla antes de cobrar a sus clientes. Alrededor de este problema de liquidez circulan tres ideas que lo empeoran.</p>
<div class="rejilla">
<div class="tarjeta"><h3>«Si reclamo, pierdo al cliente»</h3><p>Lo que molesta es el aviso brusco tras meses de silencio. Un recordatorio breve antes del vencimiento se lee como buena organización.</p></div>
<div class="tarjeta"><h3>«La tesorería ya la lleva la gestoría»</h3><p>La gestoría trabaja con lo que ya ha pasado. La previsión de las próximas semanas depende de lo que solo sabes tú: qué vas a facturar y quién te ha prometido pagar.</p></div>
<div class="tarjeta"><h3>«Con mirar el banco cada mañana basta»</h3><p>El saldo de hoy no avisa de que el día 20 coinciden las nóminas, un impuesto y la factura grande de un proveedor.</p></div>
</div>
<h3 style="margin-top:30px">Seis preguntas para saber si es tu caso</h3>
<ul class="lista" style="max-width:820px">
<li>¿Sabes ahora mismo, sin abrir nada, cuánto te deben y desde cuándo?</li>
<li>¿Pasan más de dos días entre terminar un trabajo y enviar su factura?</li>
<li>¿Quien reclama es la misma persona que vende, y por eso lo va dejando?</li>
<li>¿Te has enterado de algún impago por casualidad?</li>
<li>¿Has tirado de la póliza o de tus ahorros en un mes en el que había facturas vencidas sin cobrar?</li>
<li>¿Decides las compras mirando el saldo y no lo que ya está comprometido?</li>
</ul>
<p style="max-width:820px">Con dos respuestas afirmativas, el problema no son tus clientes, sino el método. El orden que solemos proponer es sencillo: primero ver, con una <a href="/servicios/software-de-gestion/prevision-de-tesoreria">previsión de tesorería</a>; después acortar el plazo de cobro con <a href="/servicios/problemas-sin-resolver/cobro-facil-con-enlaces-de-pago">enlaces de pago en cada factura</a>; y, si hay clientes que se retrasan por costumbre, poner reglas con un <a href="/servicios/problemas-sin-resolver/sistema-anti-impagos">sistema anti-impagos</a>. Ninguna herramienta asegura que te paguen: lo que cambia es que te enteras antes y decides con margen. La financiación y la negociación con el banco siguen siendo cosa tuya y de tu asesor.</p>
</div></section>""",
 "faq": [
  ("¿Por qué mi empresa tiene beneficios pero no tiene dinero en el banco?", "Porque el beneficio cuenta lo facturado y la caja cuenta lo cobrado. Si pagas gastos y nóminas antes de que tus clientes te paguen, el dinero falta aunque las cuentas salgan en positivo. Se corrige facturando antes, facilitando el pago y previendo las semanas ajustadas."),
  ("¿Cómo mejorar la liquidez de una pequeña empresa sin pedir un préstamo?", "Acortando el tiempo entre el trabajo hecho y el cobro: señal al aceptar, factura el mismo día, forma de pago sencilla y recordatorio antes del vencimiento. No sustituye a la financiación cuando hace falta, pero reduce las veces que tienes que recurrir a ella."),
 ],
}

# Estructura: glosario llano de cuatro términos + preguntas para la gestoría + preguntas para el proveedor del programa
D["servicios/pequenas-empresas/cumple-la-ley-verifactu-y-registro-de-jornada"] = {
 "estructura": "glosario-llano + que-preguntar-a-la-gestoria + que-preguntar-al-proveedor",
 "lead": "Cada pocos meses alguien te reenvía una noticia sobre multas, facturas con QR o fichaje digital, y ya no distingues qué es obligatorio hoy y qué es un rumor. En una pequeña empresa, Verifactu y el registro de jornada se resuelven mejor con calma, un calendario claro y un solo programa.",
 "bloque": """<section class="sec sec-suave"><div class="w">
<div class="cab"><p class="kicker">Entre titulares y cadenas de WhatsApp</p><h2>¿Qué tengo que hacer de verdad y qué es ruido?</h2></div>
<p style="max-width:820px">El miedo a una sanción empuja a dos errores opuestos: comprar con prisa el primer programa que promete «cumplir la ley» o no hacer nada hasta la víspera. Ninguno es necesario. Son dos obligaciones diferentes, con calendarios diferentes, que tienes resumidos más arriba. Lo que suele faltar no es información, sino entender los términos y saber a quién preguntar cada cosa.</p>
<h3 style="margin-top:28px">Cuatro palabras que conviene tener claras</h3>
<dl style="max-width:820px">
<dt><strong>Registro de jornada</strong></dt><dd>Anotar cada día a qué hora empieza y a qué hora termina cada persona. Lo que se pide es un registro fiable, no un aparato concreto.</dd>
<dt><strong>Fichaje digital</strong></dt><dd>Hacer ese registro con una aplicación en vez de con una hoja. Es una manera de cumplir, más cómoda de conservar y de enseñar si te lo piden.</dd>
<dt><strong>Verifactu</strong></dt><dd>Una forma de facturar en la que el programa deja un rastro de cada factura que no se puede alterar después. Afecta al software de facturación, no a tu manera de vender.</dd>
<dt><strong>Registro encadenado</strong></dt><dd>Cada factura queda enlazada con la anterior, así que no se puede borrar o colar una en medio sin que se note.</dd>
</dl>
<h3 style="margin-top:28px">Qué preguntarle a tu gestoría</h3>
<ul class="lista" style="max-width:820px">
<li>¿Desde qué fecha me afecta Verifactu según mi forma jurídica, y ha cambiado el plazo?</li>
<li>¿Mi convenio dice algo particular sobre pausas, turnos u horas extra que deba reflejar el registro?</li>
<li>¿Cómo prefieres recibir las facturas y los informes de jornada?</li>
</ul>
<h3 style="margin-top:28px">Qué preguntarle a quien te vende el programa</h3>
<ul class="lista" style="max-width:820px">
<li>¿Quién lo actualiza cuando cambie la norma y qué me cuesta?</li>
<li>¿Puedo exportar mis facturas y mis fichajes si un día me voy?</li>
<li>¿Qué ocurre si en la obra o en el almacén no hay cobertura?</li>
</ul>
<p style="max-width:820px">Nosotros ponemos la herramienta y la mantenemos al día; la interpretación de tu caso corresponde a tu asesoría laboral y fiscal, y ningún programa la sustituye. Cada parte tiene su página: el <a href="/servicios/fichador">fichador y control horario</a> y la <a href="/servicios/software-de-gestion/facturacion-con-verifactu">facturación con Verifactu</a>. El resto de normas que pueden tocarte están ordenadas en <a href="/normativas">normativas para empresas</a>.</p>
</div></section>""",
 "faq": [
  ("¿Es mejor un solo programa para facturar y fichar o dos separados?", "Con uno solo tienes un único acceso, un único soporte y los datos de empleados y clientes en el mismo sitio. Dos programas separados funcionan igual de bien si ya los tienes y cumplen; no hace falta cambiarlos solo por unificarlos."),
  ("¿Qué hago si mis empleados no quieren fichar con el móvil?", "Ofrecer otra vía: una tablet en la entrada o una tarjeta. Ayuda explicar para qué sirve el registro y que cada persona puede consultar sus propios fichajes, porque el rechazo suele venir de sentirse vigilado más que de la herramienta."),
  ("¿Cómo sé si mi programa actual está preparado para Verifactu?", "Pregúntaselo al proveedor por escrito: si la versión que usas estará adaptada, desde cuándo y si tiene coste. Con esa respuesta y la de tu gestoría sobre tu fecha decides si esperas, actualizas o cambias, sin prisas de última hora."),
 ],
}

# Estructura: tabla por tipo de negocio rural + orden recomendado en cuatro pasos + objeción «no hay nadie cerca»
D["servicios/pequenas-empresas/digitalizacion-de-negocios-rurales"] = {
 "estructura": "tabla-por-tipo-de-negocio-rural + orden-en-cuatro-pasos + objecion-sin-tecnico-cerca",
 "lead": "En el pueblo te conocen por tu nombre, pero quien viene de fuera te busca en el móvil y, si no apareces, pasa de largo. La digitalización de negocios rurales consiste en que te encuentren, puedan reservar o encargar a distancia y tú no pierdas el trato de siempre.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">De puertas afuera</p><h2>¿Cómo vendo a quien no pasa por delante de mi puerta?</h2></div>
<p style="max-width:820px">Haciéndote visible donde esa persona mira y dándole una forma de pedirte algo sin depender de que cojas el teléfono. Digitalizar un negocio de pueblo no significa convertirlo en una tienda fría de internet. Los negocios rurales rara vez fallan por el producto: fallan porque fuera nadie sabe que existen. El primer paso cambia según lo que tengas entre manos.</p>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Tu negocio</th><th>Lo que suele frenarlo</th><th>Primer paso sensato</th></tr></thead><tbody>
<tr><td>Casa rural, restaurante o empresa de actividades</td><td>Reservas por teléfono mientras limpias, cocinas o guías un grupo</td><td>Ficha de Google completa y reserva online con confirmación</td></tr>
<tr><td>Tienda, obrador o productor de queso, miel, aceite o embutido</td><td>Solo compra quien pasa por allí</td><td>Catálogo corto con pedido por WhatsApp, antes de pensar en tienda online</td></tr>
<tr><td>Oficio con furgoneta: fontanería, electricidad, taller agrícola</td><td>Avisos en una libreta y facturas a fin de mes</td><td>Partes y facturas desde el móvil, aunque no haya señal</td></tr>
<tr><td>Explotación agrícola o ganadera</td><td>Papeles repartidos entre casa, cooperativa y gestoría</td><td>Documentos y vencimientos reunidos en un único sitio</td></tr>
</tbody></table></div>
<h3 style="margin-top:30px">El orden que recomendamos</h3>
<ol style="max-width:820px">
<li><strong>Que te encuentren.</strong> Una <a href="/servicios/presencia-digital/google-business-profile">ficha de Google Business Profile</a> con fotos, horario y zona es lo que más rinde por lo que cuesta.</li>
<li><strong>Que puedan pedirte sin llamarte.</strong> WhatsApp ordenado o una reserva sencilla.</li>
<li><strong>Que la gestión viaje contigo.</strong> Un programa que se usa en el móvil, en la ruta o en la nave.</li>
<li><strong>Solo después,</strong> una web más completa o una tienda online, si los pasos anteriores han traído demanda.</li>
</ol>
<h3 style="margin-top:30px">«Aquí no hay nadie que entienda de ordenadores»</h3>
<p style="max-width:820px">Es la objeción que más oímos y la más comprensible. Por eso todo se monta y se atiende en remoto, con videollamadas cortas, y se elige lo que no te exige mantenimiento. Si tu clientela es del pueblo y no quieres crecer hacia fuera, puede que te baste la ficha de Google, y así te lo diremos. Para alojamientos hay un apartado propio de <a href="/servicios/alojamientos-y-domotica">alojamientos y domótica</a>; y si prefieres intentarlo por tu cuenta, empieza por la guía <a href="/guias/como-crear-una-pagina-web">cómo crear una página web</a>.</p>
</div></section>""",
 "faq": [
  ("¿Por dónde empiezo a digitalizar un negocio de pueblo con poco presupuesto?", "Por lo que te hace visible: la ficha de Google con fotos, horario y teléfono, y un WhatsApp de empresa con respuestas preparadas. Con eso ya puedes recibir encargos de fuera. La web, la reserva online o el programa de gestión vienen después, según lo que te pidan."),
  ("¿Cómo consigo que mi casa rural o mi tienda aparezca en Google Maps?", "Creando y verificando la ficha de tu negocio en Google Business Profile, con dirección, categoría correcta, fotos reales y horario al día. Las reseñas de clientes ayudan. Nadie puede prometerte un puesto concreto en el mapa, pero sin ficha no apareces."),
 ],
}

# Estructura: señales de que se escapan clientes + voz o WhatsApp según cómo entra el trabajo + primeras dos semanas
D["servicios/pequenas-empresas/no-pierdas-clientes-whatsapp-ia-y-recepcionista-de-voz"] = {
 "estructura": "senales-de-clientes-que-se-escapan + elegir-voz-o-whatsapp + primeras-dos-semanas",
 "lead": "El teléfono suena mientras estás subido a una escalera, con un cliente delante o conduciendo, y esa llamada perdida casi nunca vuelve. Atender WhatsApp y llamadas con IA en tu pyme significa que alguien responde siempre, toma el recado completo y te pasa solo lo que necesita de ti.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Señales de que ya se te están escapando</p><h2>¿Cuántos clientes llaman una vez y no lo vuelven a intentar?</h2></div>
<ul class="lista" style="max-width:820px">
<li>En hora punta, la lista de llamadas perdidas del móvil es más larga que la de atendidas.</li>
<li>Devuelves llamadas a última hora y te contestan «ya lo he arreglado con otro».</li>
<li>En WhatsApp hay conversaciones que acaban en una pregunta del cliente sin respuesta.</li>
<li>Los lunes amaneces con mensajes del fin de semana que pedían algo «para hoy».</li>
<li>Quien coge el teléfono es también quien cobra, despacha o repara.</li>
</ul>
<p style="max-width:820px;margin-top:18px">Con una sola de estas señales que se repita cada semana ya merece la pena mirarlo. Para no perder clientes por no contestar no hace falta contratar a alguien de recepción, y tampoco dejarlo todo en manos de una máquina.</p>
<h3 style="margin-top:30px">Voz o WhatsApp: empieza por donde te entra el trabajo</h3>
<p style="max-width:820px">Si tus clientes llaman —urgencias, talleres, reformas, clínicas con pacientes mayores—, lo primero es la <a href="/servicios/agentes-de-ia/recepcionista-de-voz-y-atencion-fuera-de-horario">recepcionista de voz para fuera de horario</a>. Si escriben —estética, academias, tiendas, alojamientos—, empieza por el <a href="/servicios/whatsapp-ia/asistente-de-ia-para-whatsapp">asistente de IA para WhatsApp</a>. Poner en marcha los dos a la vez rara vez es buena idea: se aprende más afinando uno y sumando el otro cuando el primero ya funciona.</p>
<p style="max-width:820px">Y si recibes pocas consultas al día y las atiendes bien, no lo necesitas. Te bastará un mensaje de ausencia bien escrito y devolver las llamadas a una hora fija.</p>
<h3 style="margin-top:30px">Quince días de arranque, por orden</h3>
<ol style="max-width:820px">
<li>Recogemos las preguntas reales de tu historial de mensajes y cómo las contestas tú.</li>
<li>Escribimos contigo lo que puede decir y lo que debe pasar siempre a una persona.</li>
<li>Lo probamos en interno, llamando y escribiendo como lo haría un cliente difícil.</li>
<li>Arranca solo fuera de horario y cada mañana repasas lo que ha atendido.</li>
<li>Si te convence, se amplía a las horas de más trabajo. Si no, se ajusta o se retira.</li>
</ol>
<p style="max-width:820px">Antes de nada comprobamos tu caso en el <a href="/contacto#diagnostico">diagnóstico gratuito</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo atender el teléfono de mi negocio cuando estoy trabajando?", "Desviando las llamadas que no puedes coger a una recepcionista de voz con IA que saluda con el nombre de tu negocio, resuelve lo habitual, toma los datos y te deja un resumen. Las urgentes pueden pasarte al móvil según las reglas que marques."),
  ("¿Es mejor contratar a una recepcionista o usar un asistente con IA?", "Depende del volumen y del tipo de consulta. Una persona aporta criterio y trato en casos complejos; la IA cubre las horas sin nadie y los picos de trabajo. Muchas pequeñas empresas combinan ambas: el equipo atiende lo delicado y la IA lo repetitivo."),
 ],
}

# Estructura: escena del día que algo falla + inventario en tabla + cuándo no compensa + qué exigir por escrito
D["servicios/pequenas-empresas/todo-incluido-por-cuota-mensual"] = {
 "estructura": "el-dia-que-algo-falla + inventario-en-tabla + cuando-no-compensa + que-exigir-por-escrito",
 "lead": "El dominio lo registró un sobrino, la web la hizo una agencia que ya no contesta, el programa lo instaló un informático que viene cuando puede y las copias nadie sabe si se hacen. Con la tecnología por una cuota mensual fija, tu pyme pone todo eso bajo un mismo responsable.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">El día que algo deja de funcionar</p><h2>¿A quién llamas cuando se cae la web o no abre el programa?</h2></div>
<p style="max-width:820px">Si la respuesta es «depende» o «no lo sé», ahí está el problema, más que en el dinero. En muchas pequeñas empresas la informática se ha ido comprando a trozos durante años, cada trozo a una persona distinta, y nadie conserva la foto completa. Mientras todo marcha no se nota. El día que caduca un dominio o se estropea el ordenador del despacho empieza una cadena de llamadas en la que cada proveedor señala al siguiente.</p>
<p style="max-width:820px">Antes de pensar en cuotas, haz inventario. Media hora y una hoja.</p>
<h3 style="margin-top:28px">Tu inventario digital en una tabla</h3>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Qué tienes</th><th>A nombre de quién</th><th>Cuándo se renueva</th><th>Quién responde si falla</th></tr></thead><tbody>
<tr><td>Dominio y correo</td><td>Debería ser la empresa, no quien lo registró</td><td>Fecha y tarjeta con la que se paga</td><td>Nombre y teléfono</td></tr>
<tr><td>Página web</td><td>Quién guarda las claves de administración</td><td>Alojamiento y mantenimiento</td><td>Quién hace los cambios</td></tr>
<tr><td>Programa de gestión</td><td>Titular de la licencia y de los datos</td><td>Mensual, anual o pago único</td><td>Soporte: horario y canal</td></tr>
<tr><td>Copias de seguridad</td><td>Dónde se guardan</td><td>Última vez que se probó a restaurar</td><td>Quién sabría recuperarlas</td></tr>
</tbody></table></div>
<p style="max-width:820px;margin-top:16px">Las casillas que no sepas rellenar son tu riesgo real. Si son varias, te interesa leer cómo se resuelven los <a href="/servicios/departamento-tecnologico/dominios-y-renovaciones">dominios y renovaciones</a> y qué supone tener <a href="/servicios/departamento-tecnologico/soporte-con-un-unico-interlocutor">soporte con un único interlocutor</a>.</p>
<h3 style="margin-top:28px">Cuándo no te compensa una cuota</h3>
<ul class="lista" style="max-width:820px">
<li>Si solo tienes una web sencilla y un correo, y ya hay alguien de confianza que responde.</li>
<li>Si lo que necesitas es un proyecto puntual, como una web nueva: mejor un precio cerrado.</li>
<li>Si en la plantilla hay una persona que sabe y tiene horas para mantenerlo.</li>
</ul>
<h3 style="margin-top:28px">Lo que debe quedar por escrito</h3>
<p style="max-width:820px">Un pago mensual sin letra clara es otra factura suelta. Pide la lista de lo que cubre, lo que se presupuesta aparte, el plazo de respuesta y qué te llevas si te marchas: dominio, contenidos y datos a nombre de tu empresa. Los importes orientativos están en la <a href="/precios">página de precios</a>.</p>
</div></section>""",
 "faq": [
  ("¿Qué es mejor para una pyme, pagar la tecnología por cuota mensual o comprarla de una vez?", "La cuota reparte el gasto e incluye mantenimiento y soporte, así que encaja cuando no tienes a nadie que se ocupe. Comprar de una vez sale a cuenta si tu necesidad es puntual o cuentas con alguien interno que lo mantenga. Compara el coste a tres años, no el del primer mes."),
  ("¿Qué pasa con mi web y mis datos si dejo de pagar la cuota?", "Tiene que estar escrito en el contrato antes de firmar. Nuestra forma de trabajar es que el dominio, los contenidos y los datos estén a nombre de tu empresa y puedas llevártelos; exige lo mismo a cualquier proveedor."),
 ],
}

# Estructura: cuatro tropiezos que cuestan ventas (lista numerada) + semana tipo en tabla + cuándo las redes no son tu canal
D["servicios/pequenas-empresas/vende-mas-en-redes"] = {
 "estructura": "cuatro-tropiezos + semana-tipo-en-tabla + cuando-las-redes-no-son-tu-canal",
 "lead": "Publicas cuando te acuerdas, la foto recibe veinte «me gusta» de familiares y compañeros del gremio, y en la caja no se nota. Vender más en redes sociales siendo pequeña empresa no va de seguidores: va de que quien te ve sepa qué haces, cuánto cuesta más o menos y cómo pedírtelo.",
 "bloque": """<section class="sec sec-suave"><div class="w">
<div class="cab"><p class="kicker">Mucho esfuerzo, pocas ventas</p><h2>¿Por qué mis publicaciones tienen «me gusta» pero no traen clientes?</h2></div>
<p style="max-width:820px">Casi siempre porque la publicación enseña algo bonito y no dice qué hacer después. Quien la ve no sabe si trabajas en su zona, si puede permitírselo ni dónde escribirte. Conseguir clientes por Instagram, Facebook o TikTok depende menos del algoritmo que de cuatro detalles muy terrenales.</p>
<h3 style="margin-top:28px">Cuatro tropiezos que cuestan ventas</h3>
<ol style="max-width:820px">
<li><strong>Publicar sin precio ni referencia.</strong> Mucha gente no pregunta por miedo a que sea caro. Un «desde» o una horquilla filtra y anima.</li>
<li><strong>Querer estar en todas las redes.</strong> Una cuenta bien atendida vende más que cuatro a medias.</li>
<li><strong>Contestar los mensajes al día siguiente.</strong> El interés caduca en horas. Si no llegas, un <a href="/servicios/whatsapp-ia/asistente-de-ia-para-whatsapp">asistente en WhatsApp</a> puede dar la primera respuesta.</li>
<li><strong>No apuntar de dónde llega cada cliente.</strong> Sin ese dato sigues dedicando horas a ciegas.</li>
</ol>
<h3 style="margin-top:28px">Una semana que cabe en tu agenda</h3>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Día</th><th>Qué se publica</th><th>Lo que pones tú</th></tr></thead><tbody>
<tr><td>Lunes</td><td>Un trabajo terminado, con la zona y un precio orientativo</td><td>La foto al acabar</td></tr>
<tr><td>Miércoles</td><td>Un vídeo corto que responde a una duda de mostrador</td><td>Grabarte contestándola como lo harías en persona</td></tr>
<tr><td>Viernes</td><td>El hueco libre o la oferta de la semana, con botón a WhatsApp</td><td>Un audio con los datos</td></tr>
</tbody></table></div>
<p style="max-width:820px;margin-top:16px">Lo demás —textos, recortes, programación— se prepara con ayuda de inteligencia artificial y tú lo apruebas antes de que salga. Cómo funciona está en <a href="/servicios/presencia-digital/automatizacion-de-redes-sociales">automatización de redes sociales</a> y en <a href="/servicios/presencia-digital/videos-y-anuncios-con-ia">vídeos y anuncios con IA</a>.</p>
<p style="max-width:820px">Un aviso honesto: las redes no son el canal de todo el mundo. Si vendes a otras empresas con decisiones lentas, o tu cliente te busca en Google el día que tiene una avería, te rendirá más el <a href="/servicios/presencia-digital/seo-local-y-por-sectores">SEO local</a>. No prometemos ventas ni seguidores; sí medir cuántos mensajes llegan y de dónde, para que decidas con datos si seguir.</p>
</div></section>""",
 "faq": [
  ("¿Cómo conseguir clientes por Instagram si tengo un negocio local?", "Enseñando trabajos reales con la zona y un precio orientativo, y poniendo en cada publicación una forma directa de escribirte. Usa la ubicación y etiquetas de tu ciudad, y responde pronto: en un negocio local vende más la rapidez que el número de seguidores."),
  ("¿Cuánto tardan las redes sociales en traer ventas a un negocio pequeño?", "No hay un plazo fijo. Depende del sector, de la constancia y de lo fácil que sea pedirte algo. Lo que sí puedes medir desde el primer mes es cuántos mensajes y reservas llegan desde cada red; si tras varios meses de constancia no llega ninguno, toca cambiar de enfoque o de canal."),
 ],
}
