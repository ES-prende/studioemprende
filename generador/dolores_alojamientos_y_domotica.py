# Reescritura «dolores primero» · familia alojamientos y domótica (noviembre 2026).
# Diez páginas para propietarios y gestores de pisos turísticos, casas rurales y pequeños hoteles (y dos para el hogar propio).
# Cada una sigue un recorrido distinto; ninguna repite secuencia ni titulares.
D = {}

# Estructura: cita de un sábado de cambios + tres fallos típicos de coordinación, cada uno con su apartado
D["servicios/alojamientos-y-domotica/aviso-automatico-a-limpieza"] = {
 "estructura": "tres-fallos-de-coordinacion-cada-uno-con-apartado",
 "lead": "El huésped llega a las cuatro y la casa sigue con las sábanas de ayer, porque el mensaje a la limpiadora se quedó sin enviar entre una reserva y otra. Con el aviso automático al equipo de limpieza tras cada salida, la tarea sale sola del calendario con su hora límite y deja de depender de tu memoria.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Cambios de huésped en el mismo día</p><h2>¿Por qué se descoordina la limpieza si «siempre se ha hecho por WhatsApp»?</h2><p class="lead" style="margin-top:8px">Porque el grupo de mensajes funciona con tres viviendas y un mes tranquilo. En temporada alta se rompe por tres sitios.</p></div>
<blockquote style="max-width:820px;font-size:18px">«¿La de la calle Mayor está hecha? Entran en una hora y no me contesta nadie.»</blockquote>
<h3 style="margin-top:26px">El aviso que no se envió</h3>
<p style="max-width:820px">Entra una reserva de última hora para esta noche mientras atiendes otra cosa. Tú lo sabes, la plataforma lo sabe, la persona que limpia no. Cuando el viajero escribe desde el portal ya no hay margen. Coordinar la limpieza de apartamentos turísticos a mano significa que cada reserva nueva genera una tarea para ti antes que para nadie.</p>
<h3 style="margin-top:26px">El cambio que nadie trasladó</h3>
<p style="max-width:820px">Concedes una salida tardía por amabilidad y olvidas avisar. La limpiadora llega a su hora, encuentra a la familia desayunando, espera en el rellano y se le descuadra el resto de la ruta. Lo mismo ocurre con una cancelación: alguien se desplaza para preparar una casa que va a quedarse vacía.</p>
<h3 style="margin-top:26px">La casa «lista» que no lo estaba</h3>
<p style="max-width:820px">Nadie confirmó que se terminó, faltaba un juego de toallas para la quinta persona y el mando del aire no aparecía. Te enteras por la reseña. Sin una confirmación al acabar, con su lista de comprobación, das por hecha una tarea que no has visto.</p>
<p style="max-width:820px;margin-top:22px">Los tres fallos tienen el mismo origen: la información vive en el calendario y hay que copiarla a mano para quien limpia. Cuando la tarea nace de la reserva, se mueve con ella y se cierra con una confirmación, tú solo intervienes si algo se sale de lo previsto. Para que funcione hace falta que las reservas de todos los canales estén en un <a href="/servicios/alojamientos-y-domotica/calendario-unificado-con-airbnb-booking-y-web-propia">calendario unificado</a>; si además quieres que el personal entre sin recoger llaves, se combina con la <a href="/servicios/alojamientos-y-domotica/cerradura-con-codigo-por-reserva">cerradura con código</a>. Con una sola vivienda que limpias tú, no lo necesitas. A partir de varias casas, o en cuanto trabaja contigo alguien externo, cuéntanos cómo os organizáis en el <a href="/contacto#diagnostico">diagnóstico gratuito</a> y vemos qué parte merece automatizarse.</p>
</div></section>""",
 "faq": [
  ("¿Cómo coordinar la limpieza de varios pisos turísticos sin estar pendiente del móvil?", "Haciendo que cada salida genere su tarea sin intervención tuya, con la hora límite marcada por la siguiente entrada, y que quien limpia la confirme al terminar. Solo recibes avisos cuando algo no se confirma o hay una incidencia."),
  ("¿Qué pasa si entra una reserva de última hora para el mismo día?", "La tarea se crea en ese momento y llega al equipo con la hora de entrada del nuevo huésped. Si no hay margen suficiente, lo ves antes de aceptar o puedes fijar un tiempo mínimo entre salida y entrada para que no se venda esa noche."),
 ],
}

# Estructura: tabla según número de alojamientos y canales + lo que cuesta un overbooking en lista + cierre sobre comisiones
D["servicios/alojamientos-y-domotica/calendario-unificado-con-airbnb-booking-y-web-propia"] = {
 "estructura": "tabla-por-tamano-de-cartera + coste-de-una-doble-reserva-en-lista",
 "lead": "Dos familias con la misma reserva para el puente, una por Booking y otra por Airbnb, y un solo apartamento: toca recolocar a una, pagar la diferencia y asumir la mala reseña. Un calendario unificado de Airbnb, Booking y tu web cierra las fechas en todos los canales cuando entra la primera.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Vender en varios portales a la vez</p><h2>¿Cómo evitar la doble reserva sin renunciar a ningún canal?</h2></div>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Tu situación</th><th>Dónde está el riesgo</th><th>Qué necesitas de verdad</th></tr></thead><tbody>
<tr><td>Una vivienda en dos portales</td><td>Reservas de última hora que coinciden en minutos</td><td>Sincronización básica y un margen mínimo de antelación</td></tr>
<tr><td>De tres a diez apartamentos</td><td>Bloqueos manuales que se olvidan en algún canal</td><td>Una vista por alojamiento y bloqueos que se propaguen solos</td></tr>
<tr><td>Casa rural que también vende por teléfono</td><td>La reserva de palabra que no llega a ningún portal</td><td>Poder anotar la reserva directa y que cierre el resto</td></tr>
<tr><td>Hostal o pequeño hotel con habitaciones iguales</td><td>Vender más habitaciones de un tipo de las que hay</td><td>Cupos por tipo de habitación, no solo fechas</td></tr>
<tr><td>Gestor con viviendas de varios propietarios</td><td>Usos propios del dueño que nadie comunicó</td><td>Que el propietario bloquee sus fechas desde su acceso</td></tr>
</tbody></table></div>
<p style="max-width:820px;margin-top:20px">Un gestor de canales para alojamientos pequeños no tiene por qué ser una herramienta de gran hotel. Lo importante es que resuelva tu fila de la tabla y que alguien te explique antes qué retardo tiene cada conexión, para que ajustes tus reglas en las fechas de más demanda.</p>
<h3 style="margin-top:30px">Lo que te cuesta un overbooking, sin poner cifras por ti</h3>
<ul class="lista" style="max-width:820px">
<li>La noche en otro alojamiento para el viajero que se queda sin casa, casi siempre más cara y pagada por ti.</li>
<li>Las horas al teléfono buscando alternativa en plena temporada.</li>
<li>La penalización o la pérdida de visibilidad que aplique el portal por cancelar.</li>
<li>Una reseña negativa que seguirá ahí cuando el huésped ya se haya olvidado.</li>
</ul>
<p style="max-width:820px">Con que te haya pasado una vez, ya sabes cuánto suma. Tener todas las reservas juntas también deja ver qué parte de tus ingresos se va en comisiones y qué clientes repiten: a esos puedes ofrecerles la reserva directa en tu web la próxima vez. La reserva unificada alimenta además el <a href="/servicios/alojamientos-y-domotica/check-in-online-con-firma">check-in online con firma</a> y el <a href="/servicios/alojamientos-y-domotica/aviso-automatico-a-limpieza">aviso a limpieza</a>, y si gestionas para terceros, el <a href="/servicios/alojamientos-y-domotica/panel-de-propietarios">panel de propietarios</a> lee del mismo calendario.</p>
</div></section>""",
 "faq": [
  ("¿Cómo sincronizar los calendarios de Airbnb y Booking para que no se pisen las reservas?", "Conectando ambos a un calendario central que, al recibir una reserva por un canal, cierra esas noches en los demás. Según el volumen se hace por intercambio de calendarios o por conexión directa, que actualiza con menos retardo."),
  ("¿Qué pasa si entran dos reservas a la vez para las mismas fechas?", "Es poco frecuente, pero puede ocurrir mientras un portal todavía no ha recibido el bloqueo. Para reducirlo se usan conexiones más rápidas en temporada alta y reglas como estancias mínimas o un tiempo de antelación para reservar."),
  ("¿Necesito tener web propia para usar un calendario unificado?", "No. Puedes empezar solo con los portales y añadir la reserva directa más adelante. La web propia interesa cuando tienes huéspedes que repiten o te buscan por tu nombre y quieres ahorrarte la comisión en esas estancias."),
 ],
}

# Estructura: escena de una llegada de madrugada en dos párrafos + cita + pasos para que no dependa de ti
D["servicios/alojamientos-y-domotica/cerradura-con-codigo-por-reserva"] = {
 "estructura": "escena-de-madrugada + cita-del-anfitrion + pasos-para-dejar-de-ir-a-la-puerta",
 "lead": "El vuelo se retrasa, el huésped aterriza a la una y media y tú llevas desde las once esperando en el coche con las llaves en el bolsillo. Mañana madrugas. Una cerradura inteligente con código por reserva le abre a él a la hora que llegue y deja de abrirle cuando termina su estancia.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Entregar llaves a cualquier hora</p><h2>¿Cuántas noches has esperado a un huésped que llegaba tarde?</h2></div>
<p style="max-width:820px">La entrega de llaves en mano parece un detalle de buen anfitrión hasta que gestionas más de una vivienda o tienes otro trabajo. Entonces se convierte en la parte que más te ata: no puedes aceptar llegadas nocturnas sin sacrificar la tuya, dependes de un familiar cuando sales de viaje y un atasco del viajero te descuadra la tarde entera.</p>
<p style="max-width:820px">Las soluciones caseras tienen su precio. El cajetín con combinación en la fachada se queda con el mismo número durante meses y lo conocen todos los que han pasado por allí. La llave bajo el felpudo o en el bar de abajo funciona hasta el día que no. Y cada copia que se pierde obliga a cambiar el bombín.</p>
<blockquote style="max-width:820px;font-size:18px">«No sé cuántas copias de la llave hay por ahí. Limpieza tiene una, el fontanero se llevó otra y la del último inquilino nunca volvió.»</blockquote>
<h3 style="margin-top:30px">Para dejar de ir a la puerta, en este orden</h3>
<ol style="max-width:820px">
<li><strong>Mira tu acceso completo, no solo la puerta del piso.</strong> Si hay portal comunitario o verja, hay que resolver también ese tramo; en algunas comunidades exige hablarlo antes.</li>
<li><strong>Decide qué condición libera el código.</strong> Lo habitual es que el viajero lo reciba cuando ha completado el <a href="/servicios/alojamientos-y-domotica/check-in-online-con-firma">check-in online</a>, no antes.</li>
<li><strong>Prepara el plan para cuando algo falle.</strong> Una llave física de emergencia custodiada y un teléfono al que llamar; la apertura sin llaves reduce los desplazamientos, no los elimina del todo.</li>
<li><strong>Da a cada persona de tu equipo su propia clave.</strong> Así sabes quién entró y puedes retirarla el día que deje de trabajar contigo.</li>
<li><strong>Explícaselo al huésped con una foto.</strong> Un mensaje con la imagen del teclado y dos líneas evita la mayoría de las llamadas.</li>
</ol>
<p style="max-width:820px">Si las dudas del viajero al llegar son muchas (dónde aparcar, cómo va la vitrocerámica), las puede resolver el <a href="/servicios/alojamientos-y-domotica/asistente-del-huesped-por-whatsapp-24-7">asistente del huésped por WhatsApp</a>. El acceso autónomo a un apartamento turístico encaja peor cuando tu valor es precisamente recibir en persona, como en algunas casas rurales con encanto: en ese caso puede servirte solo como respaldo para las llegadas fuera de hora.</p>
</div></section>""",
 "faq": [
  ("¿Cómo dar acceso a un huésped que llega de madrugada sin ir a entregarle las llaves?", "Con una cerradura electrónica que admita códigos temporales. El viajero recibe su clave por mensaje al completar el registro y entra cuando llegue; tú ves en el móvil que ha abierto y no tienes que desplazarte."),
  ("¿Qué pasa si un huésped anterior conserva el código de la puerta?", "No le sirve. Cada clave está ligada a las fechas de una reserva y deja de funcionar a la hora de salida. A diferencia de una llave o de un cajetín con combinación fija, no hay nada que devolver ni que cambiar."),
 ],
}

# Estructura: tabla de dudas frecuentes del anfitrión (creencia / lo que ocurre) + qué hacer con el huésped que no lo rellena + cuándo mantener la recepción
D["servicios/alojamientos-y-domotica/check-in-online-con-firma"] = {
 "estructura": "tabla-creencia-frente-a-practica + huesped-que-no-rellena + cuando-mantener-recepcion",
 "lead": "Son las diez de la noche, la familia lleva seis horas de coche y tú les pides los documentos uno a uno en el portal, apuntando números a mano mientras los niños se duermen de pie. Con el check-in online con firma para pisos turísticos, esos datos ya están rellenos y firmados antes de que arranquen.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Registro de viajeros sin papeles en la puerta</p><h2>¿Se puede registrar al huésped antes de que llegue?</h2><p class="lead" style="margin-top:8px">Sí: rellena y firma desde su móvil días antes. Lo que frena a muchos anfitriones son estas cuatro ideas.</p></div>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Lo que se suele pensar</th><th>Lo que pasa en la práctica</th></tr></thead><tbody>
<tr><td>«Mis huéspedes son mayores, no sabrán hacerlo»</td><td>Es un enlace que se abre desde el mismo mensaje de la reserva; quien ha reservado por un portal sabe rellenar un formulario. Para el resto, siempre puedes completarlo tú con ellos</td></tr>
<tr><td>«Les va a parecer frío»</td><td>Lo frío es hacer cola con las maletas. El trámite hecho de antemano deja la llegada para lo agradable: enseñar la casa o, simplemente, descansar</td></tr>
<tr><td>«Seguro que se equivocan con los datos»</td><td>El formulario marca los campos que faltan y pide un documento por viajero; hay menos errores que copiando a mano con prisa</td></tr>
<tr><td>«Si no les veo, no sé quién entra»</td><td>Queda la foto del documento y una firma por cada adulto, asociadas a la reserva, y puedes condicionar el acceso a que esté completo</td></tr>
</tbody></table></div>
<h3 style="margin-top:30px">¿Y el que no lo rellena?</h3>
<p style="max-width:820px">Siempre hay alguno. Lo razonable es escalonar la insistencia:</p>
<ol style="max-width:820px">
<li>Recordatorio automático la víspera, con el enlace otra vez.</li>
<li>Un mensaje tuyo, personal, la mañana de la llegada.</li>
<li>Si aparece sin hacerlo, se completa en la puerta con ese mismo enlace en su teléfono.</li>
</ol>
<p style="max-width:820px">Lo que conviene evitar es entregar el acceso sin el registro hecho, porque luego es difícil conseguirlo. Cuando la entrada es autónoma, se enlaza con la <a href="/servicios/alojamientos-y-domotica/cerradura-con-codigo-por-reserva">cerradura con código por reserva</a> para que la clave solo se envíe con el check-in terminado.</p>
<h3 style="margin-top:30px">Cuándo mantener una recepción en persona</h3>
<p style="max-width:820px">El registro digital de huéspedes no obliga a desaparecer. En un hotel pequeño o una casa rural donde la bienvenida forma parte de la experiencia, puede usarse solo para adelantar el papeleo y dedicar el encuentro a lo que importa. En una vivienda de uso turístico gestionada a distancia, en cambio, es lo que hace posible no estar. La comunicación del parte a las autoridades es un paso distinto, que tratamos en el <a href="/servicios/alojamientos-y-domotica/envio-automatico-a-ses-hospedajes">envío automático a SES.HOSPEDAJES</a>. Si quieres revisar tu caso, el <a href="/contacto#diagnostico">diagnóstico es gratuito</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo hacer el check-in de un apartamento turístico sin estar presente?", "Enviando al huésped un enlace tras la reserva para que introduzca los datos de cada viajero, adjunte su documento y firme en la pantalla. Con el registro completo, el acceso puede darse mediante un código sin entrega de llaves."),
  ("¿Cuánto tarda un huésped en completar el check-in online?", "Unos minutos por persona si tiene el documento a mano. En grupos, cada acompañante puede rellenar lo suyo desde su propio teléfono, de modo que quien reservó no tiene que reunir los datos de todos."),
 ],
}

# Estructura: preguntas sueltas para reconocerse + tabla por perfil (propietario, gestor, estancia larga, casa rural) + cierre de cuándo no
D["servicios/alojamientos-y-domotica/consumo-por-estancia"] = {
 "estructura": "preguntas-para-reconocerse + tabla-por-perfil-de-alojamiento + que-hacer-con-el-dato-y-cuando-no-medir",
 "lead": "Llega la factura de la luz de agosto y es el doble que la de julio con las mismas noches ocupadas. ¿Fue el aire puesto con las ventanas abiertas, la depuradora o un termo averiado? Sin medir el consumo de luz y agua por estancia en tu piso turístico, solo puedes suponerlo.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Suministros incluidos en el precio</p><h2>¿Sabes cuánto te cuesta de luz y agua cada reserva?</h2></div>
<ul class="lista" style="font-size:18px;max-width:820px">
<li>¿Has puesto el mismo precio en enero que en mayo sin saber cuánto gasta la calefacción?</li>
<li>¿Algún huésped dejó el aire acondicionado encendido los cuatro días, también mientras estaba en la playa?</li>
<li>¿Repartes la factura de suministros entre propietarios «a ojo» y alguno protesta?</li>
<li>¿Has descubierto una cisterna que perdía agua solo al ver el recibo?</li>
<li>¿Alquilas por meses en temporada baja con «gastos incluidos» y te da miedo el resultado?</li>
</ul>
<p style="max-width:820px;margin-top:18px">Si has dicho que sí a dos, el problema no es el huésped: es que la factura llega una vez al mes, mezclada, y no dice qué estancia gastó qué. Un medidor en el cuadro eléctrico y, si quieres, otro en la entrada de agua reparten ese gasto por fechas de reserva.</p>
<h3 style="margin-top:30px">Para qué lo usa cada tipo de alojamiento</h3>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Perfil</th><th>Duda que resuelve</th><th>Decisión que permite</th></tr></thead><tbody>
<tr><td>Propietario con un piso</td><td>Si su tarifa de invierno cubre la climatización</td><td>Ajustar precio o estancia mínima en los meses fríos</td></tr>
<tr><td>Gestor de varias viviendas</td><td>Qué suministros corresponden a cada dueño</td><td>Liquidar con lecturas, sin discusiones</td></tr>
<tr><td>Alquiler de temporada o media estancia</td><td>Si el inquilino supera lo razonable</td><td>Pactar un consumo incluido y avisar antes de pasarse</td></tr>
<tr><td>Casa rural con piscina o jacuzzi</td><td>Cuánto pesa cada equipo en la factura</td><td>Programar horarios o cobrar el extra como servicio</td></tr>
</tbody></table></div>
<h3 style="margin-top:30px">El medidor no ahorra; lo que haces con el dato, sí</h3>
<p style="max-width:820px">Medir no baja el consumo por sí solo. Lo baja lo que haces después: apagar el clima al quedar vacía la casa con <a href="/servicios/alojamientos-y-domotica/clima-y-luces-automaticas">clima y luces automáticas</a>, reparar lo que gotea o cambiar una tarifa. Si te basta con saber si hay agua corriendo cuando no debería, quizá solo necesites un <a href="/servicios/alojamientos-y-domotica/detector-de-fugas-y-humo">detector de fugas</a>.</p>
<p style="max-width:820px">Y si tu factura es pequeña y estable todo el año, el control del gasto energético por reserva no te aportará gran cosa: mejor invertir en otra parte. Para trasladar los suministros a cada dueño, las lecturas pasan al <a href="/servicios/alojamientos-y-domotica/panel-de-propietarios">panel de propietarios</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo saber cuánta luz gasta cada huésped en un apartamento turístico?", "Con un medidor de energía en el cuadro eléctrico que registra el consumo de forma continua. El sistema cruza esas lecturas con las fechas de entrada y salida de cada reserva y te da los kilovatios hora de esa estancia."),
  ("¿Qué pasa si descubro que una estancia ha gastado muchísimo más que las demás?", "Primero conviene mirar si hubo consumo con la casa vacía, que suele indicar avería u olvido. Si fue uso del huésped, te sirve para ajustar normas, automatizar el apagado del clima o revisar el precio de esa temporada."),
 ],
}

# Estructura: repaso guiado en pasos numerados + el día que te lo piden + nota de prudencia normativa
D["servicios/alojamientos-y-domotica/control-de-nrua-y-licencias"] = {
 "estructura": "repaso-guiado-numerado + dia-en-que-te-lo-piden + nota-de-prudencia-normativa",
 "lead": "Tienes el número de inscripción de cada vivienda en un correo de hace años, el seguro en otro y el anuncio de Booking con un dígito cambiado desde no sabes cuándo. Mientras nadie pregunta, no pasa nada. El control de licencias turísticas y número de registro junta todo en una ficha por vivienda y avisa de lo que caduca.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Papeles de cada vivienda de uso turístico</p><h2>¿Tienes a mano el número de registro y los documentos de cada alojamiento?</h2><p class="lead" style="margin-top:8px">Haz este repaso con una vivienda cualquiera de tu cartera. Si te atascas en algún paso, ya sabes dónde está el hueco.</p></div>
<ol style="max-width:820px">
<li>Localiza la resolución o el justificante de inscripción en el registro turístico de tu comunidad. ¿Cuánto has tardado?</li>
<li>Abre el anuncio en cada portal y en tu web. ¿El número que aparece es exactamente el mismo, sin espacios ni letras de más?</li>
<li>Busca la póliza de responsabilidad civil vigente. ¿Sabes qué día vence?</li>
<li>Comprueba si guardas los certificados que te pidieron al dar de alta la vivienda y si alguno tiene caducidad.</li>
<li>Si la vivienda es de un tercero, ¿tienes su autorización o contrato de gestión firmado y localizable?</li>
</ol>
<h3 style="margin-top:30px">El día que alguien lo pide</h3>
<p style="max-width:820px">Puede ser un portal que revisa los anuncios, una inspección, el administrador de la comunidad, la aseguradora tras un daño o un propietario que quiere vender y necesita demostrar que todo está en orden. En todos los casos la pregunta llega con prisa y la respuesta está repartida. Para una gestora con viviendas en varios municipios, llevar las licencias de pisos turísticos en una hoja compartida aguanta hasta que alguien borra una fila o deja de actualizarla.</p>
<p style="max-width:820px">La ficha por vivienda no hace ningún trámite por ti ni interpreta la norma: guarda, relaciona y recuerda. Tú sigues decidiendo qué exige tu comunidad autónoma y tu ayuntamiento, con tu asesor si lo tienes. Lo que cambia es que, cuando una regla se modifica, sabes en minutos a qué viviendas afecta y qué documento hay que renovar en cada una. Las novedades las resumimos en la página de <a href="/normativas">normativas</a>, y la comunicación de los datos de los viajeros es un asunto aparte, explicado en el <a href="/servicios/alojamientos-y-domotica/envio-automatico-a-ses-hospedajes">envío a SES.HOSPEDAJES</a>. Si gestionas para otros dueños, pueden aportar ellos mismos sus papeles desde el <a href="/servicios/alojamientos-y-domotica/panel-de-propietarios">panel de propietarios</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo comprobar que el número de registro de mi anuncio en Airbnb o Booking es el correcto?", "Comparándolo con el que figura en la resolución de inscripción de tu comunidad autónoma. La ficha guarda ambos, el oficial y el publicado en cada canal, para que una diferencia de un carácter salte a la vista."),
  ("¿Qué pasa si se me caduca el seguro o un certificado de una vivienda turística?", "Las consecuencias dependen de tu póliza y de la normativa de tu comunidad, así que conviene no llegar a ese punto. El sistema avisa con antelación de cada vencimiento para que renueves con margen y adjuntes el documento nuevo."),
 ],
}

# Estructura: tabla-cronología de una fuga sin nadie en casa + dónde empezar si solo pones tres sensores + párrafo de límites
D["servicios/alojamientos-y-domotica/detector-de-fugas-y-humo"] = {
 "estructura": "cronologia-de-una-fuga-en-tabla + tres-sensores-para-empezar + tres-decisiones-previas",
 "lead": "Te llama el vecino de abajo: le cae agua por el techo del baño y tu piso lleva vacío desde el domingo. Estás a tres horas en coche y no sabes si cerraste la llave de paso. Un detector de fugas de agua y humo con aviso al móvil te lo habría dicho con el primer charco.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Viviendas que pasan días sin nadie</p><h2>¿Cuánto tarda en enterarse alguien de una fuga en una casa vacía?</h2></div>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Momento</th><th>Sin sensores</th><th>Con detector conectado</th></tr></thead><tbody>
<tr><td>Minuto cero: revienta el latiguillo de la lavadora</td><td>Nadie lo sabe</td><td>El sensor toca agua y manda la alerta</td></tr>
<tr><td>Primeros minutos</td><td>El agua corre por la cocina</td><td>Si hay electroválvula, se corta la entrada general</td></tr>
<tr><td>Primera hora</td><td>Empapa rodapiés y llega al pasillo</td><td>La persona avisada confirma y manda a alguien con llave o código</td></tr>
<tr><td>Horas después</td><td>Cala al piso inferior; llama el vecino o el administrador</td><td>Suelo seco, latiguillo cambiado</td></tr>
<tr><td>Días después</td><td>Parte al seguro, peritos, reservas canceladas</td><td>Queda una anotación con hora y sensor</td></tr>
</tbody></table></div>
<p style="max-width:820px;margin-top:20px">La columna central no es una exageración: es lo que cuenta cualquier propietario al que le ha tocado. Con el humo ocurre algo parecido; un detector que solo pita dentro de una vivienda sin nadie no avisa a quien puede hacer algo.</p>
<h3 style="margin-top:30px">Si solo fueras a poner tres sensores</h3>
<ul class="lista" style="max-width:820px">
<li><strong>Bajo la lavadora o el lavavajillas,</strong> donde están las mangueras que más fallan.</li>
<li><strong>Junto al termo o la caldera,</strong> porque sus pérdidas son lentas y silenciosas.</li>
<li><strong>Un detector de humo en el pasillo,</strong> entre la cocina y los dormitorios.</li>
</ul>
<h3 style="margin-top:30px">Lo que un aviso no resuelve por sí solo</h3>
<p style="max-width:820px">Una alarma de inundación en el móvil sirve si alguien puede actuar. Antes de instalar nada conviene tomar tres decisiones:</p>
<ol style="max-width:820px">
<li>Quién recibe la alerta cuando tú no puedes atenderla.</li>
<li>Cómo entra esa persona en la vivienda.</li>
<li>Si quieres que el agua se corte sola o prefieres decidirlo en cada caso.</li>
</ol>
<p style="max-width:820px">Sin ese plan, el sensor solo te da la mala noticia antes. En un piso turístico, la entrada de quien acude se resuelve con un código temporal de la <a href="/servicios/alojamientos-y-domotica/cerradura-con-codigo-por-reserva">cerradura inteligente</a>; en tu propia casa, estos sensores forman parte del <a href="/servicios/alojamientos-y-domotica/hogar-inteligente-y-modo-vacaciones">modo vacaciones</a>. Si tienes varias viviendas cerradas buena parte del año, mira también la <a href="/servicios/deluxe/gestion-de-varias-propiedades">gestión de varias propiedades</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo enterarme de una fuga de agua en mi piso cuando no estoy?", "Colocando sensores de agua en el suelo junto a los puntos de riesgo, conectados a internet. Cuando uno se moja, recibes una alerta en el móvil y también la reciben las personas que hayas designado para acudir."),
  ("¿Qué pasa si salta la alarma de fuga y no puedo ir hasta la vivienda?", "Por eso se define una lista de contactos en orden: un vecino, mantenimiento, el gestor. Si además hay electroválvula en la entrada general, el suministro se corta sin esperar a nadie y el daño queda limitado."),
  ("¿Cuántos sensores de fugas hacen falta en un apartamento?", "Depende de cuántos puntos de agua tenga. Como mínimo, uno por electrodoméstico con toma de agua y otro junto al termo. En viviendas con dos baños o cocina separada conviene añadir alguno bajo los lavabos."),
 ],
}

# Estructura: tres tarjetas con las preocupaciones del viaje + lista de lo que no promete + qué deja de hacer el vecino
D["servicios/alojamientos-y-domotica/hogar-inteligente-y-modo-vacaciones"] = {
 "estructura": "preocupaciones-del-viaje-en-tarjetas + lo-que-no-promete + adios-al-favor-del-vecino",
 "lead": "Vas ya por la autovía y empieza la ronda de dudas: ¿cerré la ventana del baño?, ¿apagué el termo?, ¿se notará mucho que no hay nadie con las persianas bajadas tres semanas? Un hogar inteligente con modo vacaciones para tu casa responde a esas preguntas desde el móvil, sin dar la vuelta.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Para tu vivienda, no para un alquiler</p><h2>¿Qué te quita el sueño cuando dejas la casa cerrada?</h2><p class="lead" style="margin-top:8px">Casi siempre son las mismas tres cosas, y ninguna necesita una instalación de película.</p></div>
<div class="rejilla">
<div class="tarjeta"><h3>«Que se note que no estamos»</h3><p>Persianas bajadas a todas horas y ni una luz por la noche. Las luces y las persianas que se mueven con horarios cambiantes dan a la vivienda aspecto de habitada.</p></div>
<div class="tarjeta"><h3>«Que pase algo y no nos enteremos»</h3><p>Una fuga, un cortocircuito, una puerta que alguien abre. Los sensores avisan al teléfono en el momento, estés donde estés.</p></div>
<div class="tarjeta"><h3>«Que me haya dejado algo encendido»</h3><p>La plancha, el aire, el termo. Lo compruebas en la aplicación y lo apagas a distancia, en vez de llamar a tu cuñado.</p></div>
</div>
<h3 style="margin-top:30px">Lo que un modo vacaciones no promete</h3>
<ul class="lista" style="max-width:820px">
<li>No es una alarma conectada a una central receptora ni la sustituye; si ya tienes una, conviven.</li>
<li>No impide que entre quien esté decidido a hacerlo: simular presencia disuade, y los sensores te avisan pronto.</li>
<li>Depende de la conexión a internet y de la corriente; por eso se configura qué ocurre y quién se entera si alguna de las dos cae.</li>
</ul>
<h3 style="margin-top:30px">El favor que ya no tienes que pedir</h3>
<p style="max-width:820px">Hasta ahora la domótica de muchas familias en verano se llama vecino: sube persianas, recoge el correo, riega y echa un vistazo. Funciona mientras él no se va también de vacaciones. Con la casa conectada, esa persona pasa a ser un respaldo para lo que requiere manos, como regar unas macetas delicadas, y entra con un permiso temporal que no dispara las alertas. Lo demás lo ves tú.</p>
<p style="max-width:820px">Se puede empezar con poco y crecer. Para muchos hogares lo prioritario son los <a href="/servicios/alojamientos-y-domotica/detector-de-fugas-y-humo">detectores de fugas y humo</a>; si en casa vive una persona mayor, la misma base sirve para la <a href="/servicios/alojamientos-y-domotica/teleasistencia-para-mayores">teleasistencia</a>, y quien busca una automatización completa de una vivienda grande tiene la <a href="/servicios/deluxe/villa-o-casa-inteligente-de-lujo">casa inteligente de alta gama</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo vigilar mi casa desde el móvil cuando me voy de vacaciones?", "Con sensores de apertura, agua y humo conectados a un concentrador, y luces o persianas controlables a distancia. Antes de salir activas una escena y, desde entonces, la aplicación te muestra el estado y te avisa si algo cambia."),
  ("¿Cuánto se tarda en instalar un modo vacaciones en un piso normal?", "Un equipo básico sin obra, con sensores inalámbricos y algunos enchufes o interruptores conectados, suele quedar instalado y explicado en una visita. Motorizar persianas o añadir una electroválvula de agua requiere algo más de trabajo."),
 ],
}

# Estructura: lo que pregunta el propietario cada mes en lista + dos párrafos sobre confianza + qué preparar antes
D["servicios/alojamientos-y-domotica/panel-de-propietarios"] = {
 "estructura": "preguntas-mensuales-del-dueno + confianza-como-producto + preparativos-numerados",
 "lead": "Cada día 5 te escriben los mismos propietarios: cuánto ha hecho el piso, por qué este mes se liquida menos, de dónde sale ese gasto de lavandería. Contestas uno a uno rebuscando en tu Excel. Un panel de propietarios para gestores de pisos turísticos les enseña esas respuestas antes de que pregunten.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Gestoras y administradores de viviendas de terceros</p><h2>¿Cuántas horas al mes dedicas a explicar liquidaciones?</h2></div>
<ul class="lista" style="font-size:18px;max-width:820px">
<li>«¿Está alquilado el puente o lo puedo usar yo?»</li>
<li>«El mes pasado hubo más noches y he cobrado menos, ¿cómo puede ser?»</li>
<li>«¿Esta reparación quién la autorizó?»</li>
<li>«Mi gestor me pide los ingresos del año para la renta, ¿me los mandas?»</li>
</ul>
<p style="max-width:820px;margin-top:18px">Ninguna de esas preguntas es una queja. Son la señal de que el dueño no ve lo que tú ves. Y cuando alguien confía su casa a un tercero y no ve, tiende a pensar mal: que el calendario podría estar más lleno, que los gastos están inflados, que otra empresa de gestión de alquiler vacacional lo haría mejor.</p>
<p style="max-width:820px">En este negocio la transparencia es parte de lo que vendes. Un área privada para propietarios, con su ocupación, cada estancia desglosada y los justificantes de cada gasto, cambia la conversación: el dueño deja de pedir explicaciones y empieza a preguntar cómo mejorar el rendimiento. Para ti significa menos mensajes, liquidaciones que no se montan a mano y un argumento serio cuando vas a captar una vivienda nueva frente a quien solo ofrece un PDF mensual.</p>
<h3 style="margin-top:30px">Qué conviene tener resuelto antes de abrirlo</h3>
<ol style="max-width:820px">
<li>Las condiciones de cada contrato de gestión por escrito: honorario, quién paga la limpieza, a partir de qué importe se pide permiso para una reparación.</li>
<li>Todas las reservas en un mismo sitio; si aún repasas portal por portal, empieza por el <a href="/servicios/alojamientos-y-domotica/calendario-unificado-con-airbnb-booking-y-web-propia">calendario unificado</a>.</li>
<li>La costumbre de adjuntar la factura o el tique a cada gasto en el momento, no a fin de mes.</li>
<li>Decidir qué no se muestra: los datos personales de los huéspedes no tienen por qué verlos los dueños.</li>
</ol>
<p style="max-width:820px">Con dos o tres propietarios que además son conocidos, un informe mensual cuidado puede bastar. La liquidación a propietarios en línea compensa cuando la cartera crece, cuando hay dueños que viven fuera o cuando quieres repercutir suministros con datos del <a href="/servicios/alojamientos-y-domotica/consumo-por-estancia">consumo por estancia</a>. Los documentos de cada vivienda se llevan en el <a href="/servicios/alojamientos-y-domotica/control-de-nrua-y-licencias">control de licencias</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo dar a los propietarios acceso a las reservas de su vivienda sin enseñarles datos de los huéspedes?", "Con un acceso propio para cada dueño que muestra las noches ocupadas, los importes y los gastos de su inmueble, pero no nombres ni documentos de los viajeros. Cada propietario entra con su usuario y solo ve lo suyo."),
  ("¿Qué pasa si un propietario no está de acuerdo con un gasto de la liquidación?", "Puede verlo con su justificante adjunto y comentarlo contigo antes del cierre. Como el criterio de reparto está definido en su contrato de gestión y aplicado igual todos los meses, la conversación parte de datos y no de impresiones."),
 ],
}

# Estructura: dos secciones; primera con la llamada del vecino en prosa, segunda con glosario mínimo y encaje con las normas de la casa
D["servicios/alojamientos-y-domotica/sensor-de-ruido-sin-camaras"] = {
 "estructura": "llamada-del-vecino-en-prosa + seccion-aparte-glosario-llano + normas-de-la-casa",
 "lead": "A las dos de la madrugada te llama el presidente de la comunidad: hay fiesta en tu piso y es la tercera vez este trimestre. No sabes si es verdad, si son tus huéspedes ni desde cuándo dura. Un sensor de ruido para pisos turísticos, sin cámaras, te avisa a ti antes que al vecino.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Convivencia con la comunidad de vecinos</p><h2>¿Cómo saber si hay una fiesta en tu apartamento sin vigilar a nadie?</h2></div>
<p style="max-width:820px">Midiendo solo el volumen. Al propietario de un alojamiento turístico el ruido le llega siempre tarde y de segunda mano: una queja por la mañana, una nota en el ascensor, un punto en el orden del día de la junta. Para entonces el grupo ya se ha ido y solo queda tu palabra contra la de la vecina del tercero.</p>
<p style="max-width:820px">Lo que está en juego no es una noche. Es la relación con una comunidad que puede ponerte muy difícil seguir alquilando, y la reputación del anuncio si un vecino acaba llamando a la policía. Tampoco quieres pasarte de frenada: una cámara en el salón o un micrófono que grabe son una intromisión que ningún huésped debería aceptar, y que tú no quieres tener que justificar.</p>
</div></section>
<section class="sec sec-suave"><div class="w">
<h3>Cuatro términos que conviene tener claros</h3>
<dl style="max-width:820px">
<dt><strong>Decibelios</strong></dt><dd>La unidad con la que se expresa el nivel sonoro. El aparato registra ese número, no palabras ni voces reconocibles.</dd>
<dt><strong>Umbral</strong></dt><dd>El nivel a partir del cual consideras que hay un problema. Se fija por franjas: más alto de día, más bajo en horario de descanso.</dd>
<dt><strong>Duración</strong></dt><dd>Los minutos seguidos que debe mantenerse el exceso para avisar. Evita que salte por un portazo o una carcajada.</dd>
<dt><strong>Escalado</strong></dt><dd>El orden de los avisos: primero un mensaje al huésped, después otro más firme y, si continúa, la alerta a ti o a quien esté de guardia.</dd>
</dl>
<h3 style="margin-top:30px">Dilo antes: el medidor en las normas de la casa</h3>
<p style="max-width:820px">El control de ruido en viviendas turísticas funciona mejor como disuasión que como castigo. Indica en el anuncio y en las normas que hay un medidor de nivel sonoro, que no graba, y a partir de qué hora se pide silencio; el viajero puede aceptarlas al hacer el <a href="/servicios/alojamientos-y-domotica/check-in-online-con-firma">check-in online con firma</a>. La mayoría de los grupos baja el volumen con el primer mensaje, que puede enviar el <a href="/servicios/alojamientos-y-domotica/asistente-del-huesped-por-whatsapp-24-7">asistente del huésped por WhatsApp</a>. El sensor no cuenta personas ni sustituye tu criterio al aceptar reservas; te da un dato a tiempo y un historial que enseñar si la comunidad pregunta. Si quieres valorar tu caso, hablamos en el <a href="/contacto#diagnostico">diagnóstico</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo evitar fiestas en un piso turístico sin poner cámaras?", "Con un medidor de nivel sonoro que avisa cuando el ruido supera un límite durante varios minutos. Se anuncia en las normas de la casa, lo que ya disuade, y envía un mensaje al huésped antes de que la molestia llegue a los vecinos."),
  ("¿Qué pasa si el huésped ignora los avisos de ruido?", "El aviso pasa a ti o a la persona de guardia, que puede llamar o acercarse. Queda además un registro con horas y niveles de esa reserva, útil si después hay que explicar lo ocurrido a la comunidad o reclamar al portal."),
 ],
}
