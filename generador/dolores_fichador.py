# Reescritura «dolores primero» · familia Fichador (noviembre 2026).
# 18 páginas de registro de jornada: cada una parte de una situación distinta y sigue un recorrido propio.
D = {}

# Estructura: mensajes que recibe la oficina a fin de mes (cita) + tabla «pregunta / dónde la resuelve solo» + cuándo aporta poco
D["servicios/fichador/acceso-del-trabajador-a-sus-registros"] = {
 "estructura": "mensajes-a-la-oficina + tabla-pregunta-y-donde-se-resuelve + cuando-aporta-poco",
 "lead": "«¿Me habéis contado la noche del sábado?», «¿cuántas horas llevo este mes?». Si en administración os pasáis la última semana contestando mensajes así, falta un sitio donde cada persona mire lo suyo. Con el portal del empleado, el trabajador consulta sus fichajes y sus registros de jornada sin preguntar a nadie.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">La última semana del mes, en administración</p><h2>¿Por qué todo el mundo pregunta por sus horas justo antes de la nómina?</h2></div>
<blockquote style="max-width:820px">«Yo ese día salí a las diez y pico, no a las nueve. Mira a ver, porque en la nómina no me cuadra.»</blockquote>
<p style="max-width:820px;margin-top:18px">Porque hasta ese momento nadie ha podido ver su propio registro. El dato existe, pero vive en la hoja del encargado, en una carpeta o en el ordenador de quien prepara las nóminas, y la única forma de comprobarlo es escribir a la oficina. Cuando la duda llega con tres semanas de retraso ya nadie recuerda bien aquel sábado, y lo que era un despiste se convierte en una discusión de «mi palabra contra la tuya». Un área personal de fichajes cambia el orden: primero mira el trabajador, y solo si algo no encaja interviene el responsable.</p>
<div class="tabla-wrap" style="margin-top:22px"><table class="tabla-norm"><thead><tr><th>Lo que pregunta la plantilla</th><th>Cómo se resuelve hoy</th><th>Con consulta desde el móvil</th></tr></thead><tbody>
<tr><td>«¿Cuántas horas llevo?»</td><td>Alguien de oficina lo busca y contesta</td><td>Lo ve en su saldo de la semana y del mes</td></tr>
<tr><td>«Ese día fiché mal»</td><td>Se avisa de palabra y a veces se olvida</td><td>Pide el cambio indicando el día y el motivo; decide el responsable</td></tr>
<tr><td>«¿Quién me ha tocado el fichaje?»</td><td>No hay forma de saberlo</td><td>La corrección aparece con su autor y su explicación</td></tr>
<tr><td>«Necesito un justificante de mis horas»</td><td>Hay que prepararlo a mano</td><td>Se descarga el periodo que haga falta</td></tr>
</tbody></table></div>
<h3 style="margin-top:30px">Cuándo te va a cambiar poco</h3>
<p style="max-width:820px">Si sois tres personas que entráis y salís juntas, la conversación en el pasillo ya hace este trabajo. Donde se nota es en plantillas con turnos, noches, fines de semana o gente repartida por varios locales: residencias, hostelería, limpieza, comercio con varias tiendas. Ahí conviene que el portal vaya acompañado de <a href="/servicios/fichador/registros-inalterables-con-historial">registros que guardan el rastro de cada cambio</a>, porque enseñar los datos solo genera confianza si nadie puede retocarlos a escondidas.</p>
<p style="max-width:820px">Y si además quieres que la nómina y los contratos estén en el mismo sitio, eso corresponde a la <a href="/servicios/software-de-gestion/documentacion-del-empleado">documentación del empleado</a>, que es otra pieza.</p>
</div></section>""",
 "faq": [
  ("¿Cómo puede un empleado consultar sus horas trabajadas sin pedirlas a la empresa?", "Entrando con su usuario en el área personal del fichador, desde el móvil o desde un navegador. Ahí ve cada día con su entrada, su salida y sus pausas, además del total acumulado frente a su contrato."),
  ("¿Qué hago si mis trabajadores no se fían del registro de jornada?", "Lo que más ayuda es que vean exactamente lo mismo que ve la empresa y que cada corrección muestre quién la hizo y por qué. La desconfianza suele venir de no poder comprobar el dato, no del dato en sí."),
 ],
}

# Estructura: escena del día 30 + línea de tiempo de un olvido (lista ordenada) + cuándo sobran los avisos
D["servicios/fichador/alertas-de-olvidos-y-retrasos"] = {
 "estructura": "escena-de-fin-de-mes + cronologia-de-un-olvido + cuando-sobran-los-avisos",
 "lead": "Día 30, las siete de la tarde: tienes delante cuarenta fichajes sin salida y vas llamando uno a uno para preguntar «¿tú a qué hora te fuiste el día 12?». Los avisos de fichaje olvidado y de retrasos hacen esa pregunta el mismo día, cuando la persona todavía se acuerda.",
 "bloque": """<section class="sec sec-suave"><div class="w">
<div class="cab"><p class="kicker">El problema no es el olvido, es cuándo lo descubres</p><h2>¿Qué pasa con un fichaje olvidado si nadie avisa a tiempo?</h2></div>
<p style="max-width:820px">Que acaba rellenándose de memoria, y un registro reconstruido de memoria vale poco. Olvidarse de marcar la salida es normal: se termina el turno, se cierra el local, suena el teléfono. Lo que estropea el control horario es la distancia entre el despiste y su arreglo.</p>
<p style="max-width:820px">Sigue el recorrido de un mismo olvido según haya o no recordatorio:</p>
<ol style="max-width:820px">
<li><strong>Martes, 14:10.</strong> Una dependienta termina y se va sin marcar la salida.</li>
<li><strong>Sin aviso:</strong> la jornada queda abierta. Nadie lo ve hasta el cierre del mes, y entonces se apunta «las dos, más o menos».</li>
<li><strong>Con aviso:</strong> a media tarde le llega un recordatorio al móvil. Contesta con la hora correcta y solicita el arreglo.</li>
<li><strong>Miércoles:</strong> el encargado solo encuentra en su resumen lo que sigue sin resolver, no la lista completa de despistes.</li>
<li><strong>Fin de mes:</strong> el listado para la asesoría sale sin huecos que tapar deprisa.</li>
</ol>
<p style="max-width:820px">Con los retrasos ocurre algo parecido. Enterarte tres semanas después de que alguien entra tarde cada lunes solo sirve para un reproche; saberlo esa misma mañana te deja cubrir el mostrador o preguntar qué ocurre. Para que la comparación funcione, el fichador necesita saber qué horario tocaba, y por eso las alertas se apoyan en los <a href="/servicios/fichador/turnos-y-cuadrantes">turnos y cuadrantes</a> de cada persona.</p>
<h3 style="margin-top:30px">Cuándo no merece la pena activarlos</h3>
<p style="max-width:820px">Con horarios muy flexibles, donde cada cual empieza cuando quiere, un aviso de «no has fichado a tu hora» molesta más de lo que ayuda: ahí basta el de jornada abierta demasiado tiempo. Tampoco conviene usarlos como vigilancia minuto a minuto, porque la plantilla termina silenciando las notificaciones. Si el equipo ya utiliza el <a href="/servicios/fichador/fichaje-por-whatsapp-o-con-pix">fichaje por WhatsApp</a>, el recordatorio llega a ese mismo chat y responder cuesta dos segundos.</p>
</div></section>""",
 "faq": [
  ("¿Cómo evitar que los trabajadores se olviden de fichar la salida?", "Con un recordatorio automático que salta cuando la jornada lleva abierta más tiempo del previsto. Llega al móvil o al chat del trabajador el mismo día, y él solicita la corrección con la hora real."),
  ("¿Qué pasa si un empleado se olvida de fichar muchas veces?", "Cada día incompleto queda señalado en el registro y aparece en el resumen del responsable, así que el patrón se ve pronto. Qué medidas tomar es una decisión de la empresa que conviene consultar con la asesoría laboral."),
 ],
}

# Estructura: excusas para aplazarlo en formato mito/realidad (lista de definiciones) + qué no entra en ese plazo
D["servicios/fichador/alta-en-24-48-horas"] = {
 "estructura": "mito-y-realidad-en-lista-de-definiciones + lo-que-no-entra-en-el-plazo",
 "lead": "Llevas meses diciendo «la semana que viene lo miramos» porque implantar un control horario suena a proyecto largo: instalar, configurar, explicarlo a todos. Con el alta rápida del fichador en 24-48 horas, tú envías la lista de la plantilla y nosotros dejamos el sistema preparado para empezar a fichar.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Lo que te frena no es el programa</p><h2>¿De verdad se puede poner en marcha un fichador en dos días?</h2></div>
<p style="max-width:820px">Sí, cuando la configuración no recae en ti. Lo que retrasa a la mayoría de negocios no es la tecnología, sino una serie de ideas que se dan por ciertas y que casi nunca lo son:</p>
<dl style="max-width:820px">
<dt><strong>«Tengo que ordenar antes los horarios de todo el mundo.»</strong></dt>
<dd>No hace falta tenerlos perfectos. Se arranca con el horario que hay hoy, aunque esté en una foto de la pizarra, y se afina con el uso.</dd>
<dt><strong>«Mi gente no se aclara con las aplicaciones.»</strong></dt>
<dd>Cada persona recibe su acceso con unas instrucciones de un minuto, y quien no quiera aplicación puede fichar en una tablet común o por mensaje.</dd>
<dt><strong>«Ahora estamos en plena temporada, mejor en invierno.»</strong></dt>
<dd>La temporada alta es justo cuando más horas se discuten. El arranque no exige cerrar ni reunir a la plantilla entera.</dd>
<dt><strong>«Si empiezo a mitad de mes, el registro queda cojo.»</strong></dt>
<dd>El registro digital empieza el día que se activa; lo anterior se conserva como lo llevaras hasta entonces.</dd>
<dt><strong>«Necesito a alguien de informática.»</strong></dt>
<dd>Basta una persona que conozca al equipo y los horarios para contestar dudas durante la puesta en marcha.</dd>
</dl>
<h3 style="margin-top:30px">Lo que ese plazo no incluye</h3>
<p style="max-width:820px">Conviene saberlo antes de contar los días. El plazo se mide en jornadas laborables y arranca cuando tenemos la información completa, no cuando pides presupuesto. Los lectores o tarjetas dependen del transporte, de modo que al principio se ficha por otro método. Y la conexión con tu programa de nóminas o con un ERP es un trabajo aparte, con su propio calendario.</p>
<p style="max-width:820px">Si prefieres verlo funcionar antes de decidir, empieza por la <a href="/servicios/fichador/prueba-gratuita">prueba gratuita</a>; si lo que te preocupa es quedarte atado, mira cómo funciona el contrato <a href="/servicios/fichador/sin-permanencia">sin permanencia</a>. Y si todavía dudas de qué método encaja con cada puesto, repasa las <a href="/servicios/fichador/movil-tablet-web-o-tarjeta-nfc">formas de fichar</a> disponibles.</p>
</div></section>""",
 "faq": [
  ("¿Cuánto se tarda en implantar un sistema de control horario en una pyme?", "Con la lista de trabajadores, centros y horarios en la mano, el fichador queda configurado en uno o dos días laborables. Lo que más alarga el proceso es reunir esa información, no la parte técnica."),
  ("¿Qué pasa si tengo una inspección y todavía no tengo fichador?", "Un alta rápida te permite empezar a registrar la jornada desde ya, pero no crea registros de días pasados. Cómo responder por el periodo anterior es algo que debes ver con tu asesoría laboral."),
 ],
}

# Estructura: preguntas de autodiagnóstico (lista) + qué se pierde por el camino + qué hacer con lo anterior
D["servicios/fichador/conservacion-durante-4-anos"] = {
 "estructura": "autodiagnostico-en-cinco-preguntas + por-donde-se-pierden-los-registros + que-hacer-con-lo-antiguo",
 "lead": "Haz la prueba: intenta encontrar ahora las horas de un camarero que trabajó contigo dos veranos atrás. Si la respuesta es «estarán en alguna caja del almacén», tienes un problema de archivo, no de fichaje. Conservar el registro de jornada durante 4 años exige poder localizarlo, no solo haberlo guardado.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Guardar no es lo mismo que encontrar</p><h2>¿Sabrías enseñar hoy un registro de hace tres años?</h2></div>
<p style="max-width:820px">La mayoría de negocios guardó en su día las hojas de fichaje; lo que falla es recuperarlas cuando alguien las pide. Antes de pensar en herramientas, contesta con sinceridad:</p>
<ul class="lista" style="max-width:820px">
<li>¿Quién sabe dónde están las hojas de años anteriores? ¿Sigue esa persona en la empresa?</li>
<li>Si cambiaste de asesoría, de local o de ordenador, ¿los registros viajaron contigo?</li>
<li>¿Puedes separar los de un solo trabajador sin revisar la carpeta entera?</li>
<li>¿Tienes los de quienes estuvieron una sola temporada y no volvieron?</li>
<li>Si mañana se estropea el portátil donde vive el Excel, ¿existe otra copia?</li>
</ul>
<h3 style="margin-top:28px">Por dónde se pierden de verdad</h3>
<p style="max-width:820px">Casi nunca por un incendio. Se pierden en momentos corrientes: una mudanza, una reforma, el encargado que se marcha con su libreta, una limpieza de archivadores «porque esto ya es viejo», un teléfono formateado. En hostelería, comercio estacional, agricultura o limpieza, con mucha rotación de personal, el volumen se multiplica y el papel deja de ser manejable mucho antes de cumplir el plazo. Un archivo digital de fichajes no depende de ninguna de esas circunstancias: los datos están fuera de tu local, con copias, y se filtran por persona, centro y fechas. Para que ese histórico sea creíble debe conservar también las correcciones, que es lo que resuelven los <a href="/servicios/fichador/registros-inalterables-con-historial">registros inalterables con historial</a>.</p>
<h3 style="margin-top:28px">Qué hacer con los años que ya tienes en papel</h3>
<p style="max-width:820px">Empezar con un fichador no borra el pasado. Lo sensato es localizar ahora lo que exista, juntarlo en un único sitio, anotar qué periodos faltan y comentarlo con tu asesoría laboral, que es quien puede valorar cada caso. A partir del día del alta, el archivo se construye solo. Si te inquieta depender de un proveedor durante tanto tiempo, revisa las condiciones del contrato <a href="/servicios/fichador/sin-permanencia">sin permanencia</a>: al marcharte te llevas la exportación completa. El día que te lo pidan, sacar el documento es cosa del <a href="/servicios/fichador/informe-para-inspeccion-en-un-clic">informe para Inspección</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cuántos años hay que guardar los registros de jornada de los trabajadores?", "Cuatro años, también los de quienes ya dejaron la empresa. Lo importante en la práctica es poder localizar el registro de una persona y un periodo concretos cuando alguien lo solicite."),
  ("¿Qué pasa si he perdido las hojas de fichaje de años anteriores?", "No se pueden reconstruir con fiabilidad. Reúne lo que conserves, identifica qué periodos faltan y consúltalo con tu asesoría laboral; desde que empiezas con un fichador digital, el archivo queda guardado con copias."),
 ],
}

# Estructura: frases del encargado + rejilla «encaja / encaja a medias / no encaja» + qué tiene que ser cierto para que valga
D["servicios/fichador/fichaje-por-whatsapp-o-con-pix"] = {
 "estructura": "frases-del-encargado + rejilla-encaja-o-no-encaja + condiciones-para-que-sea-fiable",
 "lead": "Compraste una aplicación de control horario y a los quince días solo la usaba la mitad: uno no tenía espacio en el móvil, otro olvidó la contraseña, otro «no se aclaraba». Fichar por WhatsApp aprovecha lo único que toda tu plantilla abre veinte veces al día, sin instalar nada nuevo.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Cuando el problema es que nadie quiere otra aplicación</p><h2>¿Tu equipo ficha de verdad o lo acabas apuntando tú?</h2></div>
<ul class="lista" style="font-size:18px;max-width:820px">
<li>«Les instalé la app uno por uno y la semana siguiente la mitad la había borrado.»</li>
<li>«Los de la cuadrilla me mandan un mensaje al grupo cuando llegan y luego lo paso yo a limpio.»</li>
<li>«Tengo gente mayor y gente que acaba de llegar al país; cada pantalla nueva es una barrera.»</li>
<li>«Cada lunes hay alguien que no recuerda su clave.»</li>
</ul>
<p style="max-width:820px;margin-top:18px">Cuanto más cuesta registrar la jornada, más olvidos y más apaños a posteriori. Un control horario sin app elimina ese paso: el trabajador escribe o manda un audio a un número de la empresa y recibe la confirmación. Pero la comodidad no basta, y este método no vale igual para todos.</p>
<div class="rejilla" style="margin-top:22px">
<div class="tarjeta"><h3>Encaja bien</h3><p>Hostelería, limpieza, reformas, reparto, ayuda a domicilio o comercio: equipos que se mueven, con móvil propio y cobertura normal.</p></div>
<div class="tarjeta"><h3>Encaja a medias</h3><p>Oficinas y teletrabajo, donde un botón en el navegador resulta igual de rápido, o plantillas que entran todas por una única puerta.</p></div>
<div class="tarjeta"><h3>No es el método adecuado</h3><p>Sótanos, fincas o naves sin señal: el mensaje no sale hasta que hay red. Ahí funciona mejor el <a href="/servicios/fichador/modo-sin-conexion-para-obras">modo sin conexión</a>. Tampoco sirve para quien no dispone de teléfono.</p></div>
</div>
<p style="max-width:820px;margin-top:22px">Para que un fichaje por chat sea algo más que un mensaje tienen que cumplirse tres cosas: que cada número esté asociado a una sola persona, que la hora la ponga el sistema y no quien escribe, y que cualquier corrección siga un procedimiento con rastro en lugar de editar o borrar el texto. Un grupo donde cada cual avisa de que ha llegado no cumple ninguna. Antes de activarlo conviene explicar a la plantilla qué se registra y ofrecer una alternativa a quien prefiera no usar su teléfono personal, como la tablet o la tarjeta que verás en <a href="/servicios/fichador/movil-tablet-web-o-tarjeta-nfc">formas de fichar</a>. Quién contesta al otro lado es <a href="/servicios/pix">PIX</a>, el agente de IA de Studio Emprende.</p>
</div></section>""",
 "faq": [
  ("¿Cómo fichar en el trabajo sin instalar ninguna aplicación?", "Enviando un mensaje o un audio por WhatsApp a un número de la empresa conectado al fichador. El sistema reconoce al trabajador por su teléfono, anota la hora de recepción y le devuelve la confirmación."),
  ("¿Es obligatorio que todos los empleados fichen por WhatsApp si la empresa lo activa?", "No. Es un método más, y en la misma empresa pueden convivir la aplicación, la tablet de la entrada, la web o la tarjeta. Conviene ofrecer alternativa a quien no quiera usar su móvil personal."),
  ("¿Sirve un grupo de WhatsApp como control horario?", "No es un registro fiable: los mensajes se pueden editar o borrar, no identifican de forma segura a cada persona y alguien tiene que pasarlos a mano. Hace falta un sistema que guarde el fichaje con la hora del servidor."),
 ],
}

# Estructura: tabla con los dos puntos de vista (trabajador / empresa) + pasos previos + cita de cómo explicarlo
D["servicios/fichador/geolocalizacion-con-aviso-al-trabajador"] = {
 "estructura": "tabla-dos-puntos-de-vista + como-plantearlo-al-equipo + cita-de-ejemplo",
 "lead": "Tus técnicos empiezan en casa del cliente y tú no tienes forma de saber si el fichaje de las ocho se hizo en el portal o desde el sofá. Pero tampoco quieres que nadie se sienta perseguido. El fichaje con geolocalización, con aviso previo al trabajador, resuelve lo primero sin caer en lo segundo.",
 "bloque": """<section class="sec sec-suave"><div class="w">
<div class="cab"><p class="kicker">Comprobar sin vigilar</p><h2>¿Cómo saber dónde se ficha sin que la plantilla se sienta controlada?</h2></div>
<p style="max-width:820px">Guardando un solo punto en el momento de fichar y contándolo antes con total claridad. El rechazo a la ubicación casi nunca nace del dato, sino de no saber qué se registra ni para qué. Ayuda poner sobre la mesa las dos posturas, porque ambas son razonables:</p>
<div class="tabla-wrap" style="margin-top:20px"><table class="tabla-norm"><thead><tr><th>Lo que teme quien ficha</th><th>Lo que necesita la empresa</th><th>Dónde se encuentran</th></tr></thead><tbody>
<tr><td>«Van a saber por dónde ando todo el día»</td><td>Confirmar que la jornada empezó en el lugar de trabajo</td><td>Una posición por fichaje, nada entre medias</td></tr>
<tr><td>«Me lo activan sin decírmelo»</td><td>Poder demostrar que avisó</td><td>Comunicación previa y mensaje en pantalla antes de confirmar</td></tr>
<tr><td>«Lo usarán contra mí por cualquier cosa»</td><td>Revisar solo lo que no cuadra</td><td>Zonas de trabajo: se mira lo que cae fuera, no todo</td></tr>
<tr><td>«¿Y en mi tiempo libre?»</td><td>Nada: fuera de la jornada no hay interés legítimo</td><td>Sin fichaje no se recoge ningún dato</td></tr>
</tbody></table></div>
<h3 style="margin-top:30px">Cómo plantearlo para que no levante ampollas</h3>
<p style="max-width:820px">Actívalo solo para quien trabaja fuera: instaladores, comerciales, limpieza en casa de clientes, reparto, mantenimiento. El personal de tienda u oficina puede fichar en un dispositivo fijo y no necesita ubicación. Explícalo en una reunión breve antes de encenderlo y deja que cada persona vea el punto guardado junto a sus propios fichajes, algo que permite el <a href="/servicios/fichador/acceso-del-trabajador-a-sus-registros">acceso del trabajador a sus registros</a>. Y pide a tu asesoría laboral o a tu responsable de protección de datos que revise el texto informativo: nosotros te damos una base, pero esa valoración no nos corresponde.</p>
<blockquote style="max-width:820px;margin-top:20px">«A partir del lunes, cuando fichéis desde el móvil se guardará el punto donde estáis en ese instante. No hay seguimiento durante la jornada, y cada uno puede ver su dato en la aplicación.»</blockquote>
<p style="max-width:820px;margin-top:16px">Una frase así, dicha antes y no después, evita la mayor parte de los recelos. Para equipos que además trabajan donde falla la señal, la posición se combina con el <a href="/servicios/fichador/modo-sin-conexion-para-obras">fichaje sin conexión</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo comprobar que un trabajador ficha desde el lugar de trabajo y no desde casa?", "Activando la ubicación en el momento del fichaje y definiendo una zona alrededor de la obra, la tienda o el domicilio del cliente. Los fichajes hechos fuera de esa zona quedan señalados para que el responsable los revise."),
  ("¿Hay que avisar a los empleados antes de activar la geolocalización en el fichaje?", "Sí. La empresa debe informar antes de qué dato se guarda, en qué momento y con qué finalidad. Te facilitamos un texto de partida para que lo revise tu asesoría laboral o tu responsable de protección de datos."),
 ],
}

# Estructura: cuenta con tus propios números (pasos) + síntomas de que se te escapan horas + límite del servicio
D["servicios/fichador/horas-extra"] = {
 "estructura": "cuenta-con-tus-numeros-en-pasos + sintomas-de-horas-sin-apuntar + limite-del-servicio",
 "lead": "Las horas de más casi nunca se apuntan el día que se hacen: se quedan en un pósit, en la memoria del encargado o en un «ya te lo compensaré». Tres meses después nadie sabe cuántas fueron. Un control de horas extra de los trabajadores las separa cada día, sin depender de que alguien se acuerde.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Antes de buscar herramienta, mide el agujero</p><h2>¿Cuántas horas extra se hacen en tu negocio y nadie apunta?</h2><p class="lead" style="margin-top:8px">No hay estadística que te lo diga. Sale de comparar dos papeles que ya tienes.</p></div>
<ol style="max-width:820px">
<li>Elige una semana normal del mes pasado, ni la más tranquila ni la peor.</li>
<li>Anota a qué hora se marchó realmente cada persona. Pregunta si hace falta: lo recordarán mejor que tú.</li>
<li>Resta la hora de salida que figura en su contrato o en el cuadrante.</li>
<li>Suma los minutos de toda la plantilla y multiplica por las semanas que tiene el año.</li>
</ol>
<p style="max-width:820px;margin-top:16px">Ese total es tuyo y de nadie más. En un sentido son horas que alguien podría reclamar; en el otro, tiempo que quizá ya estás pagando sin saber en qué se va. Las dos cosas se arreglan igual: dejando de calcular a ojo.</p>
<h3 style="margin-top:30px">Pistas de que el descontrol ya está ahí</h3>
<ul class="lista" style="max-width:820px">
<li>Las compensaciones se pactan de palabra: «el viernes sales antes y estamos en paz».</li>
<li>Cada encargado lleva la cuenta a su manera y ninguna coincide con la de la asesoría.</li>
<li>Siempre se quedan los mismos y nadie lo ha decidido así.</li>
<li>Los cierres de caja, las urgencias o las entregas de última hora alargan la jornada «solo hoy», pero todas las semanas.</li>
<li>Has tenido, o temes tener, una conversación incómoda sobre horas al despedirse alguien.</li>
</ul>
<p style="max-width:820px;margin-top:16px">Para que el cálculo salga bien hacen falta dos datos previos que suelen fallar: las <a href="/servicios/fichador/pausas-y-descansos">pausas registradas</a>, porque sin ellas cualquier jornada parece más larga de lo que fue, y el horario previsto en los <a href="/servicios/fichador/turnos-y-cuadrantes">turnos</a>. Con eso, las horas de más aparecen separadas y el responsable decide sobre ellas con la información delante. El fichador te da el dato; cómo se pagan, cómo se compensan y qué topes te aplican lo marca tu convenio y debes revisarlo con tu asesoría laboral, porque ese criterio no nos corresponde.</p>
<p style="max-width:820px">Si quieres ir un paso más allá y saber qué clientes o servicios se comen esas horas, eso es terreno de la <a href="/servicios/software-de-gestion/rentabilidad-por-cliente-servicio-y-empleado">rentabilidad por cliente, servicio y empleado</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo llevar el control de las horas extra de los empleados sin Excel?", "Con un fichador que compare cada día lo trabajado con la jornada del contrato y aparte la diferencia. El responsable valida esas horas y el resumen mensual por persona sale preparado para la asesoría."),
  ("¿Cómo sé si mis trabajadores hacen horas de más que no quedan registradas?", "Compara durante una semana la hora real de salida con la prevista. Si la diferencia se repite y no consta en ningún sitio, hay horas sin apuntar; registrarlas a diario es la única forma de conocer el volumen."),
 ],
}

# Estructura: escena del requerimiento en dos tiempos + tabla «con carpetas / con fichador» + advertencia honesta
D["servicios/fichador/informe-para-inspeccion-en-un-clic"] = {
 "estructura": "escena-del-requerimiento + tabla-carpetas-frente-a-fichador + advertencia-de-lo-que-no-arregla",
 "lead": "Llega una notificación un martes: quieren el registro de jornada de seis meses de una de tus tiendas y hay pocos días para entregarlo. Lo que ocurra a partir de ahí depende de dónde estén esos datos. El informe de registro de jornada para la Inspección de Trabajo debería ser una descarga, no una semana sin dormir.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">El día que te lo piden</p><h2>¿Cuánto tardarías hoy en reunir el registro horario de medio año?</h2></div>
<p style="max-width:820px">Si la respuesta sincera es «varios días», el riesgo no está en la visita, sino en tu archivo. Imagina la escena: buscas las hojas de marzo, faltan dos semanas de un trabajador, alguien firmó todas las casillas a la misma hora y el Excel del encargado no coincide con lo que tiene la gestoría. Entregas tarde, incompleto y con la sensación de haber dado una imagen peor que la realidad.</p>
<p style="max-width:820px">Con los fichajes guardados día a día, esa misma petición se resuelve eligiendo fechas, centro y personas. La diferencia se ve mejor por partes:</p>
<div class="tabla-wrap" style="margin-top:20px"><table class="tabla-norm"><thead><tr><th>Lo que hay que hacer</th><th>Con hojas y carpetas</th><th>Con el fichador</th></tr></thead><tbody>
<tr><td>Reunir el periodo</td><td>Localizar archivadores y pedir copias a cada local</td><td>Filtrar por fechas</td></tr>
<tr><td>Separar a quienes piden</td><td>Fotocopiar y ordenar persona por persona</td><td>Marcar trabajadores o centro</td></tr>
<tr><td>Explicar los cambios</td><td>Tachones sin autor ni fecha</td><td>Cada corrección aparece con quién, cuándo y por qué</td></tr>
<tr><td>Sumar horas</td><td>Calculadora y repaso manual</td><td>Totales ya calculados, con las horas de más aparte</td></tr>
<tr><td>Justificar los días sin fichaje</td><td>Buscar partes de baja y permisos</td><td>Las ausencias constan como tales</td></tr>
</tbody></table></div>
<p style="max-width:820px;margin-top:20px">Hay algo que conviene decir sin rodeos: un informe rápido no mejora un registro malo. Si durante meses no se fichó, o se rellenó a posteriori, el documento lo mostrará tal cual. Lo que el fichador hace es que, desde el día en que se usa, el dato sea completo y coherente; por eso importa tanto que los <a href="/servicios/fichador/registros-inalterables-con-historial">registros guarden su historial</a> y que el archivo cubra todo el <a href="/servicios/fichador/conservacion-durante-4-anos">plazo de conservación</a>. Cómo contestar a un requerimiento concreto es asunto de tu asesoría laboral; nosotros nos ocupamos de que tengas los datos listos. Si quieres saber qué se exige hoy, lo explicamos en <a href="/blog/es-obligatorio-el-fichaje-digital">¿es obligatorio el fichaje digital?</a></p>
</div></section>""",
 "faq": [
  ("¿Cómo preparar el registro de jornada si me lo pide un inspector de trabajo?", "Lee qué periodo, qué centro y qué trabajadores solicita, y genera el informe con esos mismos filtros. Si los fichajes están en un fichador digital sale en PDF o Excel en el momento; coméntalo con tu asesoría antes de enviarlo."),
  ("¿Puedo generar el informe de fichajes yo mismo o tengo que pedíroslo?", "Lo generas tú desde el panel, sin depender de nosotros: eliges fechas, centro y personas y descargas el documento. También puede programarse un envío periódico a la asesoría."),
 ],
}

# Estructura: tres situaciones concretas (un H3 por lugar de trabajo) con lo que falla y cómo queda
D["servicios/fichador/modo-sin-conexion-para-obras"] = {
 "estructura": "tres-lugares-sin-señal-uno-por-apartado",
 "lead": "En el sótano no entra la señal, en la finca tampoco, y la cuadrilla empieza a trabajar igual. El resultado es que se ficha «cuando se pueda», es decir, mal o nunca. Una app de fichaje sin conexión para obras y campo guarda la hora real en el teléfono y la envía cuando vuelve la red.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Donde no llega la cobertura, sí llega la jornada</p><h2>¿Cómo registrar la jornada donde el móvil no tiene señal?</h2><p class="lead" style="margin-top:8px">Dejando que el teléfono anote el fichaje por su cuenta y lo entregue más tarde. El problema cambia según el sitio, así que mejor verlo lugar por lugar.</p></div>
<h3 style="margin-top:26px">En la obra: subir a la calle para fichar</h3>
<p style="max-width:820px">Garajes, plantas bajo rasante, estructuras de hormigón. Para marcar la entrada hay que salir a buscar una raya de cobertura, y eso con el encofrado esperando no lo hace nadie. Al final el encargado apunta a todos «a las ocho» en una libreta. Con el fichaje guardado en el dispositivo, cada operario marca abajo, en el tajo, y el registro sube cuando sale a almorzar o al terminar. Una tablet en la caseta cumple la misma función para toda la cuadrilla.</p>
<h3 style="margin-top:26px">En el campo: jornadas que empiezan antes que la red</h3>
<p style="max-width:820px">Fincas, invernaderos, explotaciones ganaderas, trabajos forestales. Aquí además hay temporeros que cambian cada campaña y capataces que llevan las horas de memoria. Sin datos móviles el teléfono sigue sirviendo: anota la hora y, si lo has activado, el punto donde se fichó. Cuando el vehículo vuelve al pueblo o a la nave, todo se sincroniza sin tocar nada.</p>
<h3 style="margin-top:26px">En mantenimiento: entrar y salir de zonas ciegas varias veces al día</h3>
<p style="max-width:820px">Salas de máquinas, cuartos de contadores, ascensores, cubiertas, cámaras frigoríficas. El técnico no pasa el día entero sin señal, pero sí justo cuando empieza o acaba un aviso. Que el fichaje no dependa de ese instante evita huecos y llamadas a la oficina para «que me lo apuntes tú».</p>
<p style="max-width:820px;margin-top:22px">En los tres casos queda una señal visible de que el registro llegó más tarde, de modo que nadie tiene que fiarse a ciegas: el responsable sabe cuáles se hicieron sin red. Si lo que necesitas recoger en esos mismos lugares es el trabajo realizado, con fotos y firma del cliente, eso lo cubren las <a href="/servicios/software-de-gestion/ordenes-y-partes-de-trabajo-con-firma-y-fotos">órdenes y partes de trabajo</a>. Y si quieres confirmar que se fichó en la obra y no de camino, combínalo con la <a href="/servicios/fichador/geolocalizacion-con-aviso-al-trabajador">geolocalización con aviso al trabajador</a>. ¿No sabes si tu zona da problemas? Durante la <a href="/servicios/fichador/prueba-gratuita">prueba gratuita</a> se comprueba en una jornada.</p>
</div></section>""",
 "faq": [
  ("¿Cómo fichar en una obra donde no hay cobertura ni wifi?", "Con una aplicación que guarde el fichaje en el propio teléfono o en una tablet de la caseta. La hora queda anotada en el momento y se envía sola al recuperar la conexión, marcada como fichaje hecho sin red."),
  ("¿Qué control horario sirve para trabajadores del campo o temporeros?", "Uno que funcione sin datos móviles y que no obligue a cada persona a tener un teléfono moderno: aplicación con modo sin conexión para quien tenga móvil y una tablet compartida para el resto de la cuadrilla."),
 ],
}

# Estructura: rejilla de cuatro preguntas para elegir método + errores habituales al elegir (lista)
D["servicios/fichador/movil-tablet-web-o-tarjeta-nfc"] = {
 "estructura": "rejilla-de-preguntas-para-elegir + errores-al-elegir-metodo",
 "lead": "Elegiste un único sistema para todos y no le sirve a nadie: los de la nave no pueden llevar el teléfono encima, los comerciales nunca pasan por la entrada y en la oficina se olvidan. Poder fichar con móvil, tablet, web o tarjeta NFC evita obligar a puestos distintos a registrar igual.",
 "bloque": """<section class="sec sec-suave"><div class="w">
<div class="cab"><p class="kicker">No existe un método ideal; existe el de cada puesto</p><h2>¿Por qué fracasa un reloj de fichar que es igual para toda la empresa?</h2></div>
<p style="max-width:820px">Porque la jornada no empieza en el mismo sitio ni del mismo modo para todos. Un sistema de fichaje se abandona cuando marcar exige un rodeo: volver a la puerta, sacar un aparato que no llevas, recordar una clave. Cuatro preguntas bastan para acertar con cada grupo.</p>
<div class="rejilla" style="margin-top:20px">
<div class="tarjeta"><h3>¿Dónde arranca su día?</h3><p>Si es en un punto fijo, vale un dispositivo en la pared. Si es en la calle o en casa del cliente, tiene que ir en el bolsillo.</p></div>
<div class="tarjeta"><h3>¿Tiene las manos libres?</h3><p>Cocina, obrador, línea de producción o taller: guantes, harina, grasa. Acercar un llavero es viable; desbloquear una pantalla, no.</p></div>
<div class="tarjeta"><h3>¿Cuántos entran a la vez?</h3><p>Diez personas a la misma hora ante una sola tablet con PIN forman cola. Con poca gente no hay problema.</p></div>
<div class="tarjeta"><h3>¿Quiere usar su teléfono?</h3><p>Hay quien prefiere no mezclar lo personal con el trabajo. Ten prevista otra vía antes de que lo plantee.</p></div>
</div>
<h3 style="margin-top:30px">Tropiezos frecuentes al decidir</h3>
<ul class="lista" style="max-width:820px">
<li><strong>Comprar aparatos antes de probar.</strong> Empieza con lo que no cuesta nada (teléfono y navegador) y añade lectores solo donde se demuestre que hacen falta.</li>
<li><strong>Colocar el punto de fichaje después del vestuario.</strong> Se pierden minutos cada día y nacen discusiones sobre cuándo empieza la jornada.</li>
<li><strong>Dejar un PIN compartido «para ir rápido».</strong> En ese momento el registro deja de decir quién fichó.</li>
<li><strong>No prever la avería.</strong> Si la tablet se cae o el lector falla, tiene que existir un segundo método ya activado.</li>
<li><strong>Olvidar a los que rotan.</strong> Quien trabaja en dos locales necesita poder marcar en ambos sin gestiones.</li>
</ul>
<p style="max-width:820px;margin-top:16px">Todos los métodos alimentan un único registro por persona, así que mezclarlos no complica los informes. Si el equipo rechaza cualquier pantalla nueva, existe además el <a href="/servicios/fichador/fichaje-por-whatsapp-o-con-pix">fichaje por WhatsApp</a>; para gente repartida entre casa y varias sedes, mira <a href="/servicios/fichador/teletrabajo-y-varios-centros">teletrabajo y varios centros</a>. Lo que cuesta el terminal de pared está en <a href="/servicios/fichador/precio-por-trabajador-al-mes">precio por trabajador</a>.</p>
</div></section>""",
 "faq": [
  ("¿Qué sistema de fichaje es mejor para una empresa pequeña: app, tablet o tarjeta?", "Depende de dónde empiece la jornada cada persona. Con todos en un mismo local suele bastar una tablet en la entrada; si hay gente en la calle, la aplicación del móvil; la tarjeta compensa cuando entran muchos a la vez."),
  ("¿Cómo fichan los empleados que no pueden usar el móvil en su puesto?", "Con un dispositivo fijo situado donde empiezan a trabajar: una tablet con PIN o un lector al que acercan su tarjeta o llavero. El registro queda igual de completo que el de quien usa la aplicación."),
 ],
}

# Estructura: tabla de discusiones típicas y el dato que falta + pasos para introducirlo sin conflicto
D["servicios/fichador/pausas-y-descansos"] = {
 "estructura": "tabla-discusion-y-dato-que-falta + pasos-para-introducirlo-sin-conflicto",
 "lead": "«Yo solo salí diez minutos.» «Pues yo te vi media hora en la puerta.» Cuando el descanso no se anota, cada parte recuerda una cosa y las horas del mes ya no cuadran para nadie. El registro de pausas y descansos en la jornada sustituye esa discusión por un dato que ambos pueden consultar.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">El hueco que desordena todas las cuentas</p><h2>¿Por qué las horas trabajadas no cuadran aunque todos fichen la entrada y la salida?</h2></div>
<div class="tabla-wrap" style="margin-top:8px"><table class="tabla-norm"><thead><tr><th>La discusión</th><th>Lo que cree cada parte</th><th>El dato que faltaba</th></tr></thead><tbody>
<tr><td>El cigarro o el café</td><td>«Son cinco minutos» / «Son cinco minutos seis veces»</td><td>Cuántas salidas hubo y cuánto duraron</td></tr>
<tr><td>La comida en jornada partida</td><td>«Tardé una hora» / «Volviste a las cuatro y cuarto»</td><td>Hora de salida y de vuelta</td></tr>
<tr><td>El bocadillo</td><td>«Eso es tiempo de trabajo» / «Eso se descuenta»</td><td>Qué dice el convenio y cómo está configurado</td></tr>
<tr><td>El turno sin parar</td><td>«No pude descansar» / «Nadie te lo impidió»</td><td>Si el descanso existió o no ese día</td></tr>
</tbody></table></div>
<p style="max-width:820px;margin-top:20px">Porque entre la entrada y la salida hay tiempo que nadie ha anotado. Sin ese dato, quien trabaja de nueve a seis parece haber hecho nueve horas, y a partir de ahí todo sale torcido: las horas de más, el coste de cada servicio y la sensación de justicia dentro del equipo. Fíjate en que la tabla recoge quejas de los dos lados. Un sistema de pausas no es una herramienta contra la plantilla: también protege a quien nunca consigue parar en un turno de cocina o en una línea de producción, porque deja constancia de ello.</p>
<h3 style="margin-top:30px">Cómo introducirlo sin que parezca desconfianza</h3>
<ol style="max-width:820px">
<li><strong>Lee antes el convenio con tu asesoría.</strong> Qué descansos cuentan como trabajo no lo decidimos nosotros ni el programa.</li>
<li><strong>Explica el motivo.</strong> «Para que las horas salgan bien para todos» se entiende; «para saber cuánto fumáis», no.</li>
<li><strong>Empieza por la pausa larga.</strong> La comida es la que más distorsiona el cálculo; las salidas breves pueden esperar.</li>
<li><strong>Hazlo fácil.</strong> Un solo gesto en el mismo sitio donde ya se ficha, sin pantallas extra.</li>
<li><strong>Revisa el primer mes en común.</strong> Ajusta duraciones previstas y avisos con lo que haya ocurrido realmente.</li>
</ol>
<p style="max-width:820px;margin-top:16px">Hecho así, el tiempo efectivo se calcula solo y alimenta el <a href="/servicios/fichador/horas-extra">control de horas extra</a>. Los despistes al volver los cubren las <a href="/servicios/fichador/alertas-de-olvidos-y-retrasos">alertas de olvidos</a>. Y si tu duda es más general, sobre qué debe tener un programa de este tipo, tienes una guía en <a href="/blog/app-de-control-horario-para-pequenas-empresas">app de control horario para pequeñas empresas</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo controlar las pausas de los trabajadores sin crear mal ambiente?", "Explicando para qué sirve, empezando solo por la pausa de comida y dejando que cada persona vea su propio registro. Cuando el dato protege también al trabajador que no llega a descansar, deja de percibirse como vigilancia."),
  ("¿El tiempo del café o del cigarro cuenta como jornada de trabajo?", "Depende de tu convenio y de lo acordado en la empresa. El fichador registra la pausa y la trata como tiempo de trabajo o como descuento según lo configures; esa decisión debes tomarla con tu asesoría laboral."),
 ],
}

# Estructura: qué entra en la cuota (lista) + qué se paga aparte o no entra (lista) + cuándo no compensa
D["servicios/fichador/precio-por-trabajador-al-mes"] = {
 "estructura": "que-entra-en-la-cuota + que-queda-fuera + cuando-no-compensa",
 "lead": "Has pedido tres presupuestos de control horario y no hay manera de compararlos: uno cobra por tramos, otro añade «módulos», otro exige un año de contrato. Antes de mirar la cifra conviene saber qué estás comprando. El precio del fichador es de 8 € por empleado y mes, y aquí tienes qué cubre.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Comparar precios sin llevarse sorpresas</p><h2>¿Qué hay detrás de una tarifa de control horario?</h2></div>
<p style="max-width:820px">Detrás hay tres cosas que casi ningún anuncio enseña juntas: qué funciones entran, qué se cobra aparte y cuánto tiempo te comprometes. Dos ofertas con la misma cifra pueden costar muy distinto al cabo del año si una factura por tramos de usuarios que no llenas o añade suplementos que no viste al principio. Por eso lo desglosamos, y en el presupuesto cada opción aparece por separado.</p>
<h3 style="margin-top:26px">Lo que cubre la cuota por persona</h3>
<ul class="lista" style="max-width:820px">
<li>Fichar desde la aplicación del móvil, desde el navegador o en una tablet que ya tengas.</li>
<li>El panel del responsable y el área personal de cada trabajador.</li>
<li>El informe de jornada para la Inspección de Trabajo.</li>
<li>El archivo de los registros durante el plazo de conservación y su exportación.</li>
</ul>
<h3 style="margin-top:26px">Lo que va aparte o no forma parte del fichador</h3>
<ul class="lista" style="max-width:820px">
<li>El terminal físico para la entrada y las tarjetas o lectores, que son opcionales y se abonan una única vez.</li>
<li>El fichaje por chat con PIX, que puede llevar un coste añadido según el volumen de mensajes.</li>
<li>El IVA, que no está incluido en las cifras publicadas.</li>
<li>Conectar los fichajes con tu programa de nóminas u otro sistema: se presupuesta según el caso.</li>
<li>El asesoramiento laboral. No somos asesoría: te entregamos el dato ordenado y las decisiones sobre convenio o contratos las tomas con la tuya.</li>
</ul>
<p style="max-width:820px;margin-top:18px">Como pagas por quien ficha, la factura sube y baja con tu plantilla: en un negocio de temporada el invierno cuesta menos que el verano, y el ajuste llega con la cuota del mes siguiente. Tampoco hay compromiso de permanencia, algo que detallamos en <a href="/servicios/fichador/sin-permanencia">control horario sin permanencia</a>. Para plantillas grandes existe un precio de grupo que conviene consultar; todas las cifras actualizadas están en la <a href="/precios">página de precios</a>.</p>
<p style="max-width:820px">¿Cuándo no te compensa? Si trabajas solo, sin empleados, no hay plantilla cuya jornada registrar. Y si lo que buscas va más allá del horario (facturas, clientes, almacén), tiene más sentido valorar el fichador como una pieza dentro de un programa de gestión y pedir un <a href="/contacto#diagnostico">diagnóstico gratuito</a> antes de contratar nada suelto. Para salir de dudas sin gastar, empieza por la <a href="/servicios/fichador/prueba-gratuita">prueba gratuita</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cuánto cuesta un programa de control horario para una empresa pequeña?", "En Studio Emprende, 8 € por empleado y mes sin IVA y sin permanencia. Para saber tu cuota multiplica esa cifra por las personas que fichan; el terminal físico es opcional y se paga aparte, y el fichaje por WhatsApp puede tener un coste añadido."),
  ("¿Qué debo comparar entre presupuestos de control horario además del precio?", "Si se cobra por persona o por tramos, qué funciones llevan suplemento, si hay permanencia, quién hace la configuración y si te entregan tus datos al darte de baja. Esas cinco cosas cambian el coste real más que la cifra anunciada."),
 ],
}

# Estructura: tabla de plan de prueba por etapas + señales para decidir (lista) + qué no demuestra una prueba
D["servicios/fichador/prueba-gratuita"] = {
 "estructura": "plan-de-prueba-por-etapas-en-tabla + señales-para-decidir + lo-que-una-prueba-no-demuestra",
 "lead": "Ya te ha pasado: contratas un programa que en la demostración parecía perfecto y a las tres semanas nadie lo usa. Con el control horario el riesgo es mayor, porque depende de que fiche toda la plantilla cada día. Una prueba gratuita de app de fichaje con tu equipo real lo aclara antes de pagar.",
 "bloque": """<section class="sec sec-suave"><div class="w">
<div class="cab"><p class="kicker">Una demo la hace el vendedor; una prueba la hace tu gente</p><h2>¿Cómo saber si tu plantilla va a usar el fichador antes de contratarlo?</h2></div>
<div class="tabla-wrap" style="margin-top:8px"><table class="tabla-norm"><thead><tr><th>Etapa</th><th>Qué haces</th><th>Qué estás comprobando</th></tr></thead><tbody>
<tr><td>Arranque</td><td>Eliges a un grupo variado: alguien de oficina, alguien de calle y la persona más reacia a la tecnología</td><td>Si todos consiguen fichar el primer día sin ayuda</td></tr>
<tr><td>Uso normal</td><td>No recuerdas nada a nadie; dejas que ocurra lo que ocurriría cualquier semana</td><td>Cuántos olvidos aparecen y si los avisos los resuelven</td></tr>
<tr><td>Un imprevisto</td><td>Provocas un cambio de turno, una corrección y una ausencia</td><td>Si el encargado se maneja con las excepciones</td></tr>
<tr><td>Cierre</td><td>Descargas el informe del periodo y se lo enseñas a tu asesoría</td><td>Si el documento sirve tal cual, sin retocar</td></tr>
</tbody></table></div>
<h3 style="margin-top:30px">Tres señales para decidir con criterio</h3>
<ul class="lista" style="max-width:820px">
<li><strong>Buena señal:</strong> la persona que más se resistía ficha sola y el responsable deja de perseguir a nadie.</li>
<li><strong>Señal de ajuste:</strong> se ficha, pero con rodeos. Suele arreglarse cambiando el método de un puesto, no de herramienta.</li>
<li><strong>Mala señal:</strong> al terminar sigues teniendo que completar huecos a mano. Entonces no es para ti, y mejor saberlo ahora.</li>
</ul>
<p style="max-width:820px;margin-top:16px">Lo sabrás poniéndola a prueba en condiciones normales y no en las ideales. La tentación es probar con los dos empleados más ordenados durante una semana tranquila: sale bien y no demuestra nada. Lo que quieres ver es qué ocurre con el camarero que entra corriendo o con la operaria que no usa correo electrónico.</p>
<p style="max-width:820px">También conviene tener claro qué no te va a decir. Una prueba no revela cómo se comporta el sistema en tu mes de más trabajo si la haces en temporada baja, ni sustituye la conversación previa con la plantilla sobre por qué se empieza a fichar. Y no te compromete a nada: no hay permanencia ni cargos por haber probado. Si al acabar quieres seguir, la configuración ya está hecha y continúas con el <a href="/servicios/fichador/alta-en-24-48-horas">alta rápida</a>; la tarifa posterior está en <a href="/servicios/fichador/precio-por-trabajador-al-mes">precio por trabajador al mes</a>. Para probar formatos distintos en un mismo periodo, revisa antes las <a href="/servicios/fichador/movil-tablet-web-o-tarjeta-nfc">formas de fichar</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo probar un programa de control horario antes de comprarlo?", "Pide un periodo de prueba con tu plantilla real y úsalo en una semana normal, con un grupo variado de puestos. Comprueba que todos fichan sin ayuda, cómo se corrige un olvido y si el informe final le sirve a tu asesoría."),
  ("¿Qué pasa si mis empleados no quieren usar la app de fichar durante la prueba?", "Es justo lo que la prueba debe descubrir. Normalmente se resuelve asignando otro método a quien se resiste, como una tablet común o el chat, y explicando al equipo para qué se registra la jornada."),
 ],
}

# Estructura: cita de una situación incómoda + glosario llano (lista de definiciones) + a quién protege
D["servicios/fichador/registros-inalterables-con-historial"] = {
 "estructura": "cita-de-situacion-incomoda + glosario-en-lenguaje-llano + a-quien-protege",
 "lead": "Un encargado «arregla» las horas del viernes porque alguien olvidó fichar, y seis meses después nadie sabe qué casillas son originales y cuáles se retocaron. A partir de ahí todo el registro queda bajo sospecha. Un registro de jornada inalterable, con historial de cambios, permite corregir errores sin que se pierda la versión anterior.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Corregir no es el problema; no saber quién corrigió, sí</p><h2>¿Qué vale un registro horario que cualquiera puede retocar?</h2></div>
<blockquote style="max-width:820px">«En la hoja pone que salí a las seis. Yo sé que salí a las ocho y que alguien lo cambió, pero no puedo demostrarlo. Y la empresa tampoco puede demostrar lo contrario.»</blockquote>
<p style="max-width:820px;margin-top:18px">Muy poco, y para las dos partes. Una hoja de cálculo, un cuaderno o un programa donde se sobrescribe la celda no distinguen entre un arreglo honrado y una manipulación: ambos dejan el mismo resultado limpio. Eso perjudica al trabajador que reclama y también al empresario que ha hecho las cosas bien y no tiene cómo acreditarlo. La solución no es prohibir los cambios, porque los despistes existen, sino que cada cambio se sume al registro en vez de sustituirlo.</p>
<h3 style="margin-top:28px">Cuatro palabras que conviene entender</h3>
<dl style="max-width:820px">
<dt><strong>Inalterable</strong></dt><dd>El fichaje original no se borra ni se pisa. Permanece aunque después se rectifique.</dd>
<dt><strong>Trazabilidad</strong></dt><dd>Poder seguir el rastro de un dato: quién lo creó, quién lo modificó, en qué momento y con qué explicación.</dd>
<dt><strong>Hora del sistema</strong></dt><dd>La que pone el servidor al recibir el fichaje, no la que marque el reloj de un teléfono o escriba una persona.</dd>
<dt><strong>Corrección</strong></dt><dd>Una anotación nueva que convive con la anterior. No es un borrado: se ven las dos.</dd>
</dl>
<p style="max-width:820px;margin-top:18px">Con estas cuatro piezas, un fichaje auditable deja de depender de la buena fe de quien tiene la contraseña. El encargado sigue pudiendo resolver un olvido, pero su nombre queda junto al cambio; el empleado lo ve desde su <a href="/servicios/fichador/acceso-del-trabajador-a-sus-registros">área personal</a>; y si un día hay que entregar el <a href="/servicios/fichador/informe-para-inspeccion-en-un-clic">informe de jornada</a>, las rectificaciones aparecen explicadas en lugar de despertar dudas. Es, además, lo que da sentido a <a href="/servicios/fichador/conservacion-durante-4-anos">conservar los registros durante años</a>: guardar mucho tiempo un dato que pudo alterarse no sirve de gran cosa.</p>
<p style="max-width:820px">Un límite que no ocultamos: el historial acredita qué se registró y qué se cambió, no si lo registrado coincide con lo que pasó. Si alguien ficha y luego no trabaja, o trabaja sin fichar, ningún programa lo arregla por sí solo; para eso están la supervisión del responsable y los avisos.</p>
</div></section>""",
 "faq": [
  ("¿Cómo demostrar que un registro de jornada no ha sido manipulado?", "Con un sistema que conserve el fichaje original y añada cada corrección como una anotación aparte, con autor, fecha y motivo. Así cualquiera puede ver qué se registró al principio y qué se rectificó después."),
  ("¿Se pueden corregir los fichajes en un registro inalterable?", "Sí. Inalterable no significa que no se pueda rectificar un error, sino que la rectificación no borra lo anterior: quedan visibles el valor original, el nuevo y quién lo aprobó."),
 ],
}

# Estructura: qué mirar antes de firmar con cualquier proveedor (pasos) + lo que significa en la práctica + reverso honesto
D["servicios/fichador/sin-permanencia"] = {
 "estructura": "preguntas-antes-de-firmar-en-pasos + reverso-honesto-del-mes-a-mes",
 "lead": "Firmaste un año de un programa que dejó de servirte en marzo y lo sigues pagando en noviembre. O peor: quieres irte y te dicen que tus datos «no se pueden exportar». Un software de control horario sin permanencia solo es buena noticia si además puedes llevarte los registros al salir.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">La letra pequeña que nadie lee hasta que quiere irse</p><h2>¿Qué te ata de verdad a un programa de fichaje?</h2></div>
<p style="max-width:820px">Menos el contrato que los datos. Una cláusula de doce meses molesta; no poder recuperar los fichajes de tu plantilla te deja sin salida, porque esos registros tienes que seguir conservándolos aunque cambies de proveedor. Por eso «sin compromiso» es media respuesta, y conviene preguntar el resto.</p>
<h3 style="margin-top:26px">Cinco preguntas para hacer a cualquier proveedor, también a nosotros</h3>
<ol style="max-width:820px">
<li><strong>¿Hay periodo mínimo o renovación automática anual?</strong> Pide que te lo señalen en el documento, no de palabra.</li>
<li><strong>¿Puedo reducir usuarios cuando baje la plantilla?</strong> Si pagas por tramos, quizá no.</li>
<li><strong>¿En qué formato me entregáis los registros si me marcho?</strong> Un PDF de mil páginas no es lo mismo que una hoja que puedas filtrar.</li>
<li><strong>¿Se incluyen los de quienes ya no trabajan aquí y las correcciones?</strong> Son los que más se olvidan.</li>
<li><strong>¿Los aparatos son míos o alquilados?</strong> Un terminal en alquiler es una permanencia con otro nombre.</li>
</ol>
<h3 style="margin-top:26px">Lo que cambia en el día a día al pagar mes a mes</h3>
<p style="max-width:820px">Que el proveedor tiene que ganarse la renovación cada treinta días y que tú puedes adaptar el gasto a la realidad: un chiringuito que triplica personal en verano, una academia que cierra en agosto, una empresa de reformas con obras que empiezan y acaban. Pagas por las personas que fichan y la cuota se ajusta sola. Para un negocio que está empezando y no sabe cuánta gente tendrá en seis meses, esa flexibilidad vale más que un descuento por fidelidad.</p>
<p style="max-width:820px">También tiene su reverso, y preferimos decirlo. Sin compromiso por tu parte tampoco hay un precio blindado durante años por contrato, y cambiar de herramienta cada pocos meses desordena el archivo aunque exportes bien. La libertad de irse sirve para elegir con calma, no para ir saltando. Si aún estás decidiendo, la <a href="/servicios/fichador/prueba-gratuita">prueba gratuita</a> responde a casi todo sin pagar; el detalle de la cuota está en <a href="/servicios/fichador/precio-por-trabajador-al-mes">precio por trabajador al mes</a> y lo que ocurre con el archivo a largo plazo, en <a href="/servicios/fichador/conservacion-durante-4-anos">conservación durante 4 años</a>.</p>
</div></section>""",
 "faq": [
  ("¿Qué pasa con mis datos de fichaje si cambio de programa de control horario?", "Debes llevártelos, porque la obligación de conservarlos sigue siendo tuya. Con nosotros recibes una exportación completa al darte de baja; con cualquier otro proveedor, pregunta el formato antes de contratar."),
  ("¿Es mejor un control horario con contrato anual o mes a mes?", "Mes a mes te da margen si tu plantilla varía o si todavía no sabes si la herramienta encaja. El contrato anual puede ofrecer mejor tarifa a cambio de pagar aunque dejes de usarlo; compáralo con tu estacionalidad."),
 ],
}

# Estructura: dos secciones, una por problema (casa / varias sedes): lista de síntomas y tabla de quién ve qué
D["servicios/fichador/teletrabajo-y-varios-centros"] = {
 "estructura": "dos-secciones: sintomas-en-remoto + tabla-quien-ve-que-en-varias-sedes",
 "lead": "Con la mitad del equipo en casa y la otra mitad repartida en tres locales, saber quién está trabajando acaba siendo un rosario de mensajes: «¿estás?», «¿quién abre hoy en la otra tienda?». El control horario para teletrabajo y varios centros te da esa foto sin interrogar a nadie.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Cuando el equipo ya no cabe en una sola puerta</p><h2>¿Cómo registrar la jornada de quien trabaja desde casa sin convertirlo en vigilancia?</h2></div>
<p style="max-width:820px">Pidiendo únicamente lo que pedirías en la oficina: cuándo empieza, cuándo para y cuándo acaba. El fichaje en remoto se tuerce cuando se intenta suplir la falta de presencia con más control. Estas son las señales de que vas por ese camino:</p>
<ul class="lista" style="max-width:820px">
<li>Pides un «buenos días» en el chat del equipo y lo usas como prueba de entrada.</li>
<li>Quien está en casa siente que debe contestar al instante para demostrar que trabaja.</li>
<li>Nadie anota los días remotos, y a final de mes no sabes cuántos fueron.</li>
<li>Las jornadas se alargan por la noche sin que conste en ninguna parte.</li>
<li>Te has planteado instalar algo que mire la pantalla. No lo hacemos ni lo recomendamos.</li>
</ul>
<p style="max-width:820px">Un botón en el navegador al empezar y otro al terminar basta para tener el dato, con la jornada marcada como remota. Lo demás es confianza y objetivos, no fichaje.</p>
</div></section>
<section class="sec sec-suave"><div class="w">
<div class="cab"><h2>Varias tiendas, naves o delegaciones: ¿quién debería ver qué?</h2></div>
<p style="max-width:820px">Cada responsable, lo suyo; la dirección, el conjunto. Con dos o más centros de trabajo el desorden suele venir de que cada local lleva su hoja, con su criterio y sus festivos, y juntar la información exige perseguir a cada encargado.</p>
<div class="tabla-wrap" style="margin-top:18px"><table class="tabla-norm"><thead><tr><th>Quién</th><th>Qué necesita ver</th><th>Qué no le hace falta</th></tr></thead><tbody>
<tr><td>Encargado de un local</td><td>Su equipo de hoy, ausencias y fichajes pendientes</td><td>Los datos de otras sedes</td></tr>
<tr><td>Persona que rota</td><td>Dónde le toca y sus propias horas, sumadas</td><td>Los fichajes de los compañeros</td></tr>
<tr><td>Gerencia</td><td>Comparativa entre centros y totales</td><td>Aprobar cada corrección una por una</td></tr>
<tr><td>Asesoría</td><td>El resumen mensual por centro</td><td>Entrar en el panel a diario</td></tr>
</tbody></table></div>
<p style="max-width:820px;margin-top:18px">Este reparto es lo que permite crecer sin que el control de presencia multicentro se vuelva un trabajo a jornada completa. Para organizar quién cubre cada sede se usan los <a href="/servicios/fichador/turnos-y-cuadrantes">turnos y cuadrantes</a>, y los días libres que difieren entre localidades se llevan en <a href="/servicios/fichador/vacaciones-y-ausencias">vacaciones y ausencias</a>. Si parte de la plantilla empieza la jornada en la calle, valora además la <a href="/servicios/fichador/geolocalizacion-con-aviso-al-trabajador">ubicación en el momento de fichar</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo fichan los empleados que teletrabajan?", "Desde el navegador del ordenador o desde el móvil, con su usuario: marcan el inicio, las pausas y el final. La jornada queda identificada como trabajo a distancia y se suma al mismo registro que los días presenciales."),
  ("¿Cómo llevar el control horario de una empresa con varias tiendas o sedes?", "Con un único fichador donde cada centro tiene su calendario y su responsable. Cada encargado ve a su equipo, la dirección ve todos los centros juntos y quien rota entre locales conserva un solo registro."),
 ],
}

# Estructura: escena del domingo por la noche + síntomas del cuadrante en Excel + pasos para la primera publicación
D["servicios/fichador/turnos-y-cuadrantes"] = {
 "estructura": "escena-del-domingo-noche + sintomas-del-cuadrante-en-excel + pasos-primera-publicacion",
 "lead": "Domingo, once de la noche. Reenvías por tercera vez el Excel de la semana porque dos personas han pedido cambiar el martes, y alguien contesta: «¿cuál es el bueno?». Un cuadrante de turnos de trabajo online acaba con las versiones: hay un solo horario y todos lo miran en el móvil.",
 "bloque": """<section class="sec sec-suave"><div class="w">
<div class="cab"><p class="kicker">Si organizar los horarios te ocupa el fin de semana</p><h2>¿Por qué el cuadrante en Excel siempre acaba dando problemas?</h2></div>
<p style="max-width:820px">Porque una hoja de cálculo es una foto y un horario cambia a diario. En cuanto la envías, deja de estar al día: alguien se pone enfermo, otro pide un cambio, entra un pedido grande. Cada modificación obliga a rehacer, reenviar y confiar en que todo el mundo abra el archivo correcto.</p>
<p style="max-width:820px">Quien lleva el planning de un bar, una clínica, un gimnasio, una tienda o una residencia reconoce el patrón enseguida.</p>
<h3 style="margin-top:26px">Lo que suele ocurrir cada semana</h3>
<ul class="lista" style="max-width:820px">
<li>Circulan varias versiones y cada persona guarda una captura distinta.</li>
<li>Los cambios se pactan por mensaje entre compañeros y tú te enteras cuando alguien no aparece.</li>
<li>Descubres un turno sin cubrir el mismo día, a la hora de abrir.</li>
<li>Asignas trabajo a quien estaba de vacaciones porque el calendario de ausencias vive en otro archivo.</li>
<li>A la misma persona le tocan todos los sábados y nadie lo ha decidido: simplemente se copió la semana anterior.</li>
<li>Solo tú sabes montarlo. Si faltas, no hay horario.</li>
</ul>
<h3 style="margin-top:26px">Cómo pasar del archivo al calendario compartido sin parar</h3>
<ol style="max-width:820px">
<li>Vuelca los turnos tipo que ya usas, con sus nombres de siempre («mañana», «partido», «cierre»).</li>
<li>Monta una sola semana y publícala junto al Excel, para que el equipo compare.</li>
<li>Pide que los cambios se soliciten desde el móvil y deja de aceptarlos por mensaje.</li>
<li>A la tercera semana, retira la hoja. A partir de ahí copias y ajustas en lugar de empezar de cero.</li>
</ol>
<p style="max-width:820px;margin-top:16px">La ventaja de tener el planificador de horarios dentro del fichador es que lo previsto y lo ocurrido se comparan solos: si alguien no llega a su hora, saltan las <a href="/servicios/fichador/alertas-de-olvidos-y-retrasos">alertas de olvidos y retrasos</a>, y los días concedidos en <a href="/servicios/fichador/vacaciones-y-ausencias">vacaciones y ausencias</a> ya aparecen bloqueados al repartir. El programa no decide por ti qué descansos o límites te aplican: eso lo marca tu convenio y conviene revisarlo con tu asesoría. Y si lo que buscas es planificar personal junto con ventas, clientes y facturación, esa visión la da <a href="/servicios/software-de-gestion/turnos-vacaciones-y-ausencias">turnos, vacaciones y ausencias</a> dentro del programa de gestión.</p>
</div></section>""",
 "faq": [
  ("¿Cómo hacer un cuadrante de turnos sin Excel?", "Con un calendario online donde defines tus turnos tipo, los asignas a cada persona y publicas la semana. El equipo lo consulta en el móvil y recibe un aviso si algo cambia, de modo que solo existe una versión."),
  ("¿Cómo gestionar los cambios de turno entre compañeros sin perder el control?", "Haciendo que el cambio se solicite en la misma herramienta y quede pendiente hasta que el responsable lo apruebe. Así el cuadrante publicado siempre refleja quién trabaja de verdad y no lo que se acordó por mensaje."),
 ],
}

# Estructura: línea de tiempo de un año de vacaciones mal gestionado (pasos) + dos decisiones previas (un H3 cada una)
D["servicios/fichador/vacaciones-y-ausencias"] = {
 "estructura": "calendario-del-año-en-pasos + dos-decisiones-previas",
 "lead": "En mayo todos quieren la segunda quincena de agosto. Las peticiones llegan por mensaje, de palabra y en una nota pegada al monitor, y en julio descubres que has dicho que sí a tres personas del mismo turno. Una app para pedir vacaciones y gestionar ausencias pone todas las solicitudes en un único calendario.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">El lío no empieza en agosto, empieza en enero</p><h2>¿Por qué cada año se repite el mismo conflicto con los días libres?</h2></div>
<p style="max-width:820px">Porque se gestiona por goteo y sin una vista de conjunto. Nadie decide mal a propósito: cada «sí» parece razonable en el momento, y el choque solo se ve cuando se juntan todos. Así suele transcurrir un año sin herramienta:</p>
<ol style="max-width:820px">
<li><strong>Enero–marzo.</strong> Nadie pide nada. Los saldos del año anterior están en una hoja que solo entiende una persona.</li>
<li><strong>Abril–mayo.</strong> Llegan las solicitudes de verano por cinco canales distintos. Algunas se aprueban de palabra en un pasillo.</li>
<li><strong>Junio.</strong> Alguien pregunta cuántos días le quedan y la respuesta tarda una mañana.</li>
<li><strong>Julio–agosto.</strong> Aparece el solapamiento. Se negocia con prisas y alguien queda descontento.</li>
<li><strong>Octubre.</strong> Una baja médica deja un turno sin cubrir y nadie sabe quién tenía ya días concedidos.</li>
<li><strong>Diciembre.</strong> Media plantilla descubre que le sobran días y quiere cogerlos a la vez.</li>
</ol>
<h3 style="margin-top:28px">Primera decisión: cuáles son las reglas del juego</h3>
<p style="max-width:820px">Ningún programa fija cuántos días corresponden ni con qué criterio se reparten; eso viene de tu convenio y de lo que acuerdes con la plantilla, y si dudas, de tu asesoría laboral. Lo que hace el gestor de ausencias es aplicar tus reglas siempre igual: mínimos de personal por turno, fechas en las que no se concede nada, plazo para pedir el verano. Decidirlas una vez y por escrito ya rebaja la mitad de los roces.</p>
<h3 style="margin-top:28px">Segunda decisión: quién aprueba y viendo qué</h3>
<p style="max-width:820px">La persona que autoriza necesita ver, en la misma pantalla, quién más falta esas fechas. Con esa información aprobar deja de ser un acto de fe. Y el trabajador, al consultar su saldo desde el teléfono, ya no depende de que alguien busque el dato. Los días concedidos pasan al <a href="/servicios/fichador/turnos-y-cuadrantes">cuadrante de turnos</a> para que no se le asigne trabajo, y los avisos de fichaje no saltan en esas fechas. En empresas con varias sedes, cada una con sus festivos, encaja con <a href="/servicios/fichador/teletrabajo-y-varios-centros">teletrabajo y varios centros</a>. Si además quieres archivar justificantes, contratos y nóminas junto a cada ficha, mira la <a href="/servicios/software-de-gestion/documentacion-del-empleado">documentación del empleado</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo organizar las vacaciones de los empleados para que no coincidan todos?", "Fijando un mínimo de personas por turno y un plazo para pedir los días, y aprobando con el calendario de todo el equipo delante. La herramienta avisa cuando una solicitud deja un turno por debajo de ese mínimo."),
  ("¿Cómo llevar el control de los días de vacaciones que le quedan a cada trabajador?", "Con un saldo por persona que se descuenta solo al aprobar cada solicitud. El trabajador lo consulta desde el móvil y el responsable ve el de todo su equipo sin mantener una hoja aparte."),
 ],
}
