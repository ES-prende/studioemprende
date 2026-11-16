# Reescritura «dolores primero» · guías (noviembre 2026).
# Páginas informativas: el bloque parte de la duda o el miedo de quien busca, orienta de forma neutral
# y solo al final menciona el servicio. Va SIN <section> porque se inserta dentro del artículo.
# Cada guía tiene su propio recorrido; no se repite estructura ni frases entre ellas.
D = {}

# Estructura: orden de decisiones numerado + lo que puede esperar + dos señales de avance
D["guias/como-iniciar-un-negocio-online"] = {
 "estructura": "orden-de-decisiones-numerado + lo-que-puede-esperar + senales-de-avance",
 "lead": "Tienes una idea, algo de ahorro y veinte pestañas abiertas con consejos que se contradicen: que si primero la web, que si el alta, que si las redes. Para iniciar un negocio online en España sin gastar antes de tiempo, lo que importa es el orden de las decisiones, y eso es lo que aclara esta guía.",
 "bloque": """<h2>¿Qué hago primero si quiero montar un negocio por internet y parto de cero?</h2>
<p>Lo primero no es el dominio ni el logotipo: es comprobar que alguien pagaría por lo que quieres vender. Casi todo el dinero que se pierde al empezar a vender por internet se va en construir cosas (tienda, fotos, anuncios) antes de haber hablado con un solo comprador.</p>
<p>Este orden evita ese tropiezo. No sustituye a los pasos formales que tienes más abajo: te ayuda a decidir en qué momento merece la pena darlos.</p>
<ol>
<li><strong>Escribe una frase de cliente.</strong> «Ayudo a [quién] que necesita [qué] y hoy lo resuelve con [alternativa].» Si no puedes rellenarla, todavía no hay negocio, hay una ilusión.</li>
<li><strong>Enséñasela a diez personas de ese perfil.</strong> No a tu familia. Apunta qué preguntan y qué les frena: son tus futuros textos de venta.</li>
<li><strong>Vende una vez a mano.</strong> Por mensaje, en un grupo, en un mercadillo o con un formulario sencillo. Un primer pedido real enseña más que un mes de planificación.</li>
<li><strong>Haz números con ese pedido.</strong> Lo que te costó el producto, el envío, tu tiempo y la comisión del cobro. Si no queda margen con uno, no quedará con cien.</li>
<li><strong>Ahora sí, monta lo imprescindible.</strong> Una web clara, una forma de cobrar y una manera de que te encuentren.</li>
</ol>
<h3>Lo que puede esperar sin que pase nada</h3>
<p>Al principio sobran casi siempre la aplicación móvil, el programa de puntos, las cinco redes sociales a la vez y el catálogo de doscientas referencias. También puede esperar la automatización: mientras recibas pocos mensajes al día, contestarlos tú es la mejor forma de aprender qué quiere tu cliente.</p>
<h3>Dos señales de que vas por buen camino</h3>
<p>La primera, que un desconocido te compra sin que tengas que convencerle durante media hora. La segunda, que repite o te recomienda. Si aún estás eligiendo qué vender, compara opciones con los criterios de <a href="/guias/ideas-de-negocio-en-espana">ideas de negocio en España</a>; si ya lo tienes claro y toca construir, sigue con <a href="/guias/crear-pagina-web-para-vender">crear una página web para vender</a>. Y si prefieres que alguien mire tu caso contigo, en el <a href="/contacto#diagnostico">diagnóstico gratuito</a> te decimos qué parte digital necesitas ya y cuál conviene aplazar. Para el alta y los impuestos, quien debe orientarte es tu asesoría.</p>""",
 "faq": [
  ("¿Necesito una tienda online para empezar a vender por internet?", "No siempre. Depende de si vendes productos con precio fijo, servicios a presupuesto, formación o reservas. Para las primeras ventas suele bastar una página clara con una forma sencilla de pedir y de pagar; la tienda completa llega cuando ya sabes qué se vende."),
  ("¿Qué es lo primero que debo hacer si tengo una idea para vender por internet?", "Comprobar que hay gente dispuesta a pagar. Habla con posibles clientes, ofrece una versión sencilla y consigue un primer pedido antes de invertir en web, logotipo o anuncios."),
  ("¿Puedo empezar a vender online mientras sigo trabajando por cuenta ajena?", "Muchas personas prueban su idea así, dedicándole unas horas a la semana. Consulta con una asesoría las obligaciones que te correspondan desde la primera venta, porque dependen de tu situación."),
 ],
}

# Estructura: tabla «qué vendes / cómo decide / qué necesita la web» + prueba del móvil prestado + síntomas
D["guias/crear-pagina-web-para-vender"] = {
 "estructura": "tabla-por-tipo-de-venta + prueba-del-movil-prestado + sintomas-que-no-son-trafico",
 "lead": "Has montado la tienda, entran visitas y casi nadie compra; o todavía no la tienes y te da miedo pagar por algo que luego no venda. Crear una página web para vender online empieza por saber cómo compra tu cliente: no es lo mismo un carrito que una reserva o una petición de presupuesto.",
 "bloque": """<h2>¿Por qué una web bonita no vende y qué tipo de web necesitas tú?</h2>
<p>Una web vende cuando el visitante entiende en segundos qué ofreces y puede terminar la compra sin tropezar. El diseño ayuda, pero lo decisivo es que el camino hasta pagar, reservar o pedir precio encaje con la forma de comprar de tu cliente. Antes de elegir plataforma, sitúate en esta tabla.</p>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Qué vendes</th><th>Cómo decide tu cliente</th><th>Lo que la web necesita</th><th>Lo que te puedes ahorrar</th></tr></thead><tbody>
<tr><td>Productos con precio fijo (ropa, vino, cerámica)</td><td>Compara y compra en el momento</td><td>Fichas, carrito, pago y envíos</td><td>Un blog extenso el primer día</td></tr>
<tr><td>Servicios con cita (fisioterapia, clases, estética)</td><td>Busca un hueco que le venga bien</td><td>Calendario con horas reales y confirmación</td><td>Carrito y gastos de envío</td></tr>
<tr><td>Trabajos a presupuesto (reformas, instalaciones, eventos)</td><td>Pide precio a dos o tres</td><td>Formulario corto, fotos de trabajos y respuesta rápida</td><td>Pasarela de pago</td></tr>
<tr><td>Formación o contenidos</td><td>Quiere probar antes</td><td>Una muestra y acceso tras el pago</td><td>Almacén e inventario</td></tr>
</tbody></table></div>
<h3>La prueba del móvil prestado</h3>
<p>Pídele a alguien que no conozca tu negocio que compre desde su teléfono mientras tú miras en silencio. Fíjate dónde duda, qué busca y no encuentra y en qué paso abandona. Diez minutos así descubren más fallos que cualquier informe.</p>
<h3>Síntomas de que el problema no es el tráfico</h3>
<ul>
<li>Te escriben para preguntar cosas que ya están en la web: están, pero no se ven.</li>
<li>Añaden al carrito y desaparecen al conocer los gastos de envío.</li>
<li>Llegan pedidos y tienes que copiarlos a mano en tu programa de facturas.</li>
<li>No sabes de dónde vino tu último cliente.</li>
</ul>
<p>Si te reconoces en los dos primeros, repasa el contenido con <a href="/blog/web-que-vende">qué tiene que tener una web que vende</a>. Si es el tercero, lo que falta es una <a href="/servicios/software-de-gestion/tienda-online-conectada">tienda online conectada con tu gestión</a>. Y si todavía no sabes cuánto reservar para el proyecto, la guía de <a href="/guias/cuanto-cuesta-una-pagina-web">cuánto cuesta una página web</a> te orienta.</p>""",
 "faq": [
  ("¿Qué es mejor para empezar, una tienda online propia o vender por Instagram y WhatsApp?", "Para probar si hay demanda, las redes y el WhatsApp son suficientes. La web propia compensa cuando los pedidos se repiten y quieres dejar de gestionarlos a mano, tener tus propios datos de clientes y no depender de una sola plataforma."),
  ("¿Puedo vender servicios con cita desde mi web sin montar una tienda online?", "Sí. Una web de servicios necesita un calendario con disponibilidad real y, si quieres, el cobro de una señal. No hace falta carrito ni gestión de envíos."),
  ("¿Por qué mi tienda online tiene visitas pero no vende?", "Lo habitual es que el visitante no entienda rápido la oferta, se encuentre costes inesperados al final o no se fíe. Observa a una persona comprando desde su móvil y revisa en qué paso abandona."),
 ],
}

# Estructura: cinco preguntas para reconocerse + qué llevar preparado al asesor + frase literal
D["guias/emprendedor-de-responsabilidad-limitada"] = {
 "estructura": "preguntas-para-reconocerse + que-llevar-al-asesor + frase-literal-del-autonomo",
 "lead": "Eres autónomo, tienes un piso en propiedad y te quita el sueño una pregunta: si el negocio va mal, ¿pueden ir a por mi casa? El emprendedor de responsabilidad limitada existe para ese miedo concreto, pero no le sirve a todo el mundo. Así puedes saber si es tu caso antes de ir al registro.",
 "bloque": """<h2>¿Me pueden quitar la casa por una deuda del negocio? Cómo saber si el ERL es para ti</h2>
<p>La figura del ERL responde a un miedo muy concreto: perder la vivienda habitual por deudas de la actividad. Si ese no es tu riesgo principal, probablemente no te compense la carga que trae consigo. Antes de leer los requisitos, contesta con sinceridad a estas preguntas.</p>
<h3>Cinco preguntas antes de pedir cita</h3>
<ul>
<li><strong>¿La vivienda en la que vives es tuya?</strong> Si vives de alquiler, la figura apenas te aporta.</li>
<li><strong>¿De dónde puede venirte una deuda grande en tu oficio?</strong> Material comprado a crédito, un cliente que no paga, un daño a un tercero. Cada origen tiene un remedio distinto.</li>
<li><strong>¿Has firmado avales personales?</strong> Lo que has avalado sigue respondiendo con tu patrimonio.</li>
<li><strong>¿Estás dispuesto a llevar una contabilidad más completa y a presentar cuentas cada año?</strong> Es la contrapartida, y supone más trabajo de asesoría.</li>
<li><strong>¿Piensas tener socios o buscar inversión?</strong> Entonces te interesa mirar ya la sociedad limitada.</li>
</ul>
<h3>Lo que conviene llevar preparado a tu asesor</h3>
<p>Studio Emprende no es una gestoría ni un despacho, así que la decisión y el trámite corresponden a tu asesor o a un notario. Lo que sí puedes hacer es llegar con los deberes hechos: una lista de tus bienes, tus deudas actuales con proveedores y bancos, los avales firmados y el seguro de responsabilidad civil que tengas. Con eso la conversación es más corta y la respuesta, mucho más precisa.</p>
<blockquote>«No quiero montar una sociedad, solo dormir tranquilo sabiendo que mi casa no depende de un mal año.» Si esta frase podría ser tuya, el resto de la guía está escrito para ti.</blockquote>
<p>Si al final te inclinas por la sociedad, tienes los pasos en <a href="/guias/como-registrar-una-empresa-en-espana">cómo registrar una empresa en España</a>. Y sea cual sea la forma que elijas, tener facturas y cobros ordenados desde el primer día evita que el cierre de cuentas se convierta en un drama: para eso sirve la <a href="/servicios/software-de-gestion/conexion-con-tu-asesoria">conexión de tu programa con la asesoría</a>.</p>""",
 "faq": [
  ("¿Cómo sé si me compensa ser emprendedor de responsabilidad limitada?", "Suele compensar si eres autónomo, tu principal patrimonio es la vivienda habitual en propiedad y tu actividad puede generar deudas importantes. Si vives de alquiler, tienes avales firmados o piensas tener socios, hay opciones que encajan mejor."),
  ("¿Quién me puede asesorar para hacerme ERL?", "Tu asesoría o gestoría y un notario. Son quienes pueden revisar tu situación, confirmar los límites vigentes y tramitar la inscripción. Studio Emprende no presta ese servicio; ayudamos con la parte digital del negocio."),
 ],
}

# Estructura: creencias frecuentes en lista de definiciones + la pregunta que decide + prueba de un mes
D["guias/erp-gratis-y-open-source"] = {
 "estructura": "creencias-y-realidad-en-dl + pregunta-que-decide + prueba-honesta-de-un-mes",
 "lead": "El presupuesto no da para licencias y alguien te ha dicho que hay ERP gratis que hacen lo mismo. Puede ser verdad, o puede que dentro de un año tengas un programa a medio instalar y la empresa otra vez en Excel. Antes de descargar un ERP open source, mira bien qué estás aceptando.",
 "bloque": """<h2>«Si es gratis, ¿dónde está la trampa?» Lo que se suele creer de un ERP de código abierto</h2>
<p>No hay trampa, hay un reparto distinto: no pagas por usar el programa, pero el trabajo de ponerlo en marcha y mantenerlo pasa a ser tuyo. Estas son las ideas que más confunden a quien busca un ERP gratuito para su pyme.</p>
<dl>
<dt>«Gratis quiere decir que no me va a costar nada»</dt><dd>La licencia no se paga. El servidor, las copias de seguridad, las horas de configuración y las de quien lo mantenga, sí; en dinero o en tiempo tuyo.</dd>
<dt>«Lo instalo un fin de semana»</dt><dd>Instalarlo es rápido. Lo lento es cargar clientes, artículos y tarifas, adaptar los documentos a tu forma de trabajar y enseñar al equipo.</dd>
<dt>«Si no me convence, lo quito y listo»</dt><dd>Para entonces ya habrá datos dentro. Pregunta antes cómo se exportan y en qué formato.</dd>
<dt>«Como es de código abierto, cualquiera me lo arregla»</dt><dd>Cualquiera que lo conozca bien. Comprueba que hay profesionales cerca que trabajen con esa herramienta concreta.</dd>
</dl>
<h3>¿Tienes a alguien que se haga cargo?</h3>
<p>Esta es la pregunta que decide. Si en la empresa hay una persona con conocimientos técnicos y horas reservadas para ello, un ERP libre puede darte mucha libertad. Si esa persona eres tú, y además vendes, compras y atiendes, lo normal es que el mantenimiento se quede siempre para mañana.</p>
<h3>Una prueba honesta de un mes</h3>
<ol>
<li>Elige un solo proceso, por ejemplo presupuestos y facturas.</li>
<li>Trabaja con datos reales, no con la empresa de demostración.</li>
<li>Apunta cada hora que dedicas a configurarlo o a buscar soluciones en foros.</li>
<li>Al terminar, haz una copia de seguridad y prueba a restaurarla.</li>
</ol>
<p>Si la cuenta de horas te parece asumible, adelante. Si no, compara con un programa que incluya soporte: en <a href="/guias/mejores-erp-para-pymes">cómo elegir ERP para una pyme</a> tienes los criterios, y en <a href="/servicios/erp-para-pymes/pagas-solo-los-modulos-que-usas">pagar solo los módulos que usas</a>, la vía intermedia. Ante la duda, pide una <a href="/servicios/consultoria-y-ayudas/segunda-opinion-tecnologica">segunda opinión tecnológica</a> antes de decidir.</p>""",
 "faq": [
  ("¿Merece la pena un ERP gratis para una empresa pequeña?", "Merece la pena si alguien de la empresa puede instalarlo, adaptarlo y mantenerlo con horas reservadas. Si nadie puede hacerse cargo, el ahorro de la licencia se pierde en tiempo y en errores."),
  ("¿Qué pasa si la persona que instaló el ERP open source se va de la empresa?", "Que el programa sigue funcionando hasta que hay que actualizarlo o algo falla, y entonces nadie sabe cómo estaba montado. Pide siempre que la instalación quede documentada y que haya una segunda persona o un proveedor capaz de mantenerla."),
 ],
}

# Estructura: frase del almacén + recorrido numerado de un error + tabla «lo que te pasa / lo que suele bastar»
D["guias/erp-para-logistica-y-almacen"] = {
 "estructura": "frase-del-almacen + recorrido-de-un-error + tabla-dolor-y-remedio",
 "lead": "El programa dice que quedan doce unidades y en la estantería hay tres. Alguien vendió lo que no había, el pedido sale incompleto y el cliente llama. Si te suena, el fallo no es de las personas: un software de gestión de almacenes o un ERP logístico sirve para que el dato y la estantería coincidan.",
 "bloque": """<h2>¿Por qué el stock del ordenador nunca coincide con el del almacén?</h2>
<p>Porque la mercancía se mueve más rápido que las anotaciones. Cada vez que algo entra, cambia de sitio o sale sin que quede registrado en ese mismo momento, el dato del programa envejece. No hace falta un gran descuido: basta con apuntarlo «luego».</p>
<blockquote>«Eso lo sabe Paco, que lleva aquí veinte años.» Cuando la ubicación de la mercancía vive en la cabeza de una persona, el almacén se para el día que esa persona falta.</blockquote>
<h3>El recorrido de un error, paso a paso</h3>
<ol>
<li>Llega un palé y se deja en el pasillo porque el muelle está lleno. Nadie lo da de entrada.</li>
<li>Ventas consulta el programa, ve cero y le dice al cliente que no hay.</li>
<li>Compras, que ve lo mismo, pide más al proveedor.</li>
<li>Dos días después aparece el palé. Ahora sobra género y falta espacio.</li>
<li>En el recuento de fin de año se ajusta la diferencia y nadie sabe de dónde vino.</li>
</ol>
<p>Ningún paso es grave por separado. Juntos suponen una venta perdida, una compra innecesaria y dinero parado en la estantería.</p>
<h3>Qué te hace falta según lo que te duele</h3>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Lo que te pasa</th><th>Lo que suele bastar</th></tr></thead><tbody>
<tr><td>Ventas, compras y almacén miran cifras distintas</td><td>Un ERP con módulo de almacén, para que todos lean el mismo dato</td></tr>
<tr><td>Se tarda en encontrar la mercancía o se prepara mal</td><td>Ubicaciones y lectura de códigos; con mucho volumen, un WMS</td></tr>
<tr><td>Caducan productos o se mezclan partidas</td><td>Control de lotes y de fechas</td></tr>
<tr><td>Hay varias naves o tiendas</td><td>Existencias por almacén y traspasos registrados</td></tr>
</tbody></table></div>
<p>Empieza por lo que no cuesta dinero: ordenar y etiquetar antes de comprar nada. Después, mira <a href="/servicios/software-de-gestion/inventario-en-varios-almacenes">inventario en varios almacenes</a>, <a href="/servicios/software-de-gestion/lotes-trazabilidad-y-caducidades">lotes, trazabilidad y caducidades</a> o, si lo tuyo es el reparto, la guía de <a href="/guias/software-a-medida-para-logistica">software para distribución y logística</a>.</p>""",
 "faq": [
  ("¿Cómo saber cuánto stock tengo de verdad sin parar el almacén?", "Con recuentos por zonas: cada día o cada semana se cuenta una parte pequeña y se corrige la diferencia en el momento. Así no hace falta cerrar para un inventario general y los errores se detectan cuando aún se recuerda su causa."),
  ("¿Puedo llevar el almacén con Excel o necesito un programa?", "Con pocas referencias y una sola persona que entra y saca mercancía, Excel aguanta. Deja de servir cuando varias personas mueven género a la vez o cuando ventas necesita consultar las existencias sin preguntar."),
 ],
}

# Estructura: seguir un pedido tramo a tramo (tabla) + tres resultados posibles + cuándo no hace falta ninguno
D["guias/erp-vs-crm"] = {
 "estructura": "seguir-un-pedido-tramo-a-tramo + tres-resultados + cuando-no-hace-falta-ninguno",
 "lead": "Sabes que necesitas poner orden, pero no si el desorden empieza en las ventas o en lo que ocurre después de vender. Nadie te explica la diferencia entre ERP y CRM con un caso como el tuyo. La forma más rápida de salir de dudas es seguir un pedido de principio a fin.",
 "bloque": """<h2>No sé si necesito un ERP o un CRM: sigue un pedido y lo verás</h2>
<p>Olvida las siglas un momento y coge el último trabajo que has cobrado. Recorre su camino, desde que esa persona preguntó por primera vez hasta que el dinero entró en el banco, y marca en qué tramo se perdió tiempo o información. Ahí está tu respuesta.</p>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Tramo</th><th>Pregunta que debes hacerte</th><th>Si falla aquí, mira</th></tr></thead><tbody>
<tr><td>Primer contacto</td><td>¿Sabes cuántos preguntaron el mes pasado y cuántos se quedaron sin respuesta?</td><td>CRM</td></tr>
<tr><td>Presupuesto</td><td>¿Alguien hace seguimiento de los que no contestan?</td><td>CRM</td></tr>
<tr><td>Pedido aceptado</td><td>¿Hay que volver a teclearlo en otro programa?</td><td>La conexión entre ambos</td></tr>
<tr><td>Preparación o servicio</td><td>¿Sabes si hay material, hueco o personal antes de comprometer una fecha?</td><td>ERP</td></tr>
<tr><td>Factura</td><td>¿Sale del pedido o se rehace a mano?</td><td>ERP</td></tr>
<tr><td>Cobro</td><td>¿El comercial sabe si ese cliente debe dinero cuando vuelve a llamar?</td><td>La conexión entre ambos</td></tr>
</tbody></table></div>
<h3>Tres resultados posibles</h3>
<ul>
<li><strong>Las marcas están arriba.</strong> Pierdes ventas antes de cerrarlas. Empieza por la parte comercial.</li>
<li><strong>Están abajo.</strong> Vendes bien, pero servir y facturar te desborda. Empieza por la operación.</li>
<li><strong>Están en los saltos.</strong> Cada parte funciona, pero no se hablan. No necesitas otro programa: necesitas unirlos.</li>
</ul>
<h3>Cuándo no necesitas ninguno de los dos todavía</h3>
<p>Si trabajas solo, con pocos clientes al mes y un único servicio, una buena hoja de cálculo y una agenda ordenada aguantan bastante. La señal para cambiar llega cuando contratas a la primera persona o cuando te descubres buscando un mismo dato en tres sitios. Si tu caso es el primero, tienes más detalle en <a href="/blog/crm-para-autonomos">CRM para autónomos</a>; si es el segundo, en <a href="/guias/que-es-un-erp">qué es un ERP</a>. Y para el tercero existe la opción de <a href="/servicios/migraciones-e-integraciones/conectar-erp-tienda-crm-y-contabilidad">conectar los programas que ya usas</a> sin cambiar ninguno.</p>""",
 "faq": [
  ("¿Qué es mejor para una pyme, un ERP o un CRM?", "Depende de dónde pierdas más tiempo o dinero. Si se te escapan clientes antes de cerrar la venta, empieza por un CRM. Si vendes bien pero preparar, servir y facturar es un caos, empieza por el ERP."),
  ("¿Necesito un ERP si soy autónomo?", "No por el hecho de serlo. Un autónomo con pocos clientes y un solo servicio suele arreglarse con facturación y una agenda ordenada. El ERP empieza a tener sentido cuando hay stock, varias personas o procesos que se pisan."),
 ],
}

# Estructura: cuenta de la necesidad en cuatro líneas + cuándo no buscar inversor + lo que depende de ti
D["guias/financiacion-para-emprendedores"] = {
 "estructura": "cuenta-en-cuatro-lineas + cuando-no-buscar-inversor + preparacion-antes-de-la-reunion",
 "lead": "Te falta dinero para arrancar o para dar el siguiente paso y no sabes a qué puerta llamar primero: el banco, una ayuda pública, un inversor o tu propia familia. Antes de repasar las vías de financiación para emprendedores, conviene tener claro cuánto necesitas, para qué y qué estás dispuesto a ceder a cambio.",
 "bloque": """<h2>¿Cuánto dinero necesito de verdad y para qué?</h2>
<p>La mayoría de quienes buscan financiación para su proyecto empiezan por el «dónde» cuando todavía no han resuelto el «cuánto» ni el «para qué». Quien presta o invierte lo nota en la primera reunión.</p>
<p>Estas cuentas se hacen en una tarde y cambian la conversación. Hazlas con tus cifras, no con medias sacadas de internet.</p>
<h3>Tu necesidad en cuatro líneas</h3>
<ol>
<li>Lo que cuesta llegar al primer cliente que paga: producto mínimo, web, material.</li>
<li>Lo que gastas cada mes aunque no vendas nada, incluido lo que necesitas para vivir.</li>
<li>Los meses que calculas hasta cubrir gastos, con un margen por si se alarga.</li>
<li>Lo que ya tienes: ahorros, equipo propio, clientes apalabrados.</li>
</ol>
<p>Lo que falta sale de sumar la primera línea a la segunda multiplicada por la tercera, y restar la cuarta. A menudo resulta bastante menos de lo que se pensaba pedir, y con una cifra menor se abren puertas más sencillas.</p>
<h3>Cuándo no te conviene buscar un inversor</h3>
<ul>
<li>Si tu negocio es un servicio local que crecerá poco a poco: quien invierte espera multiplicar lo que pone.</li>
<li>Si no quieres dar explicaciones ni compartir decisiones.</li>
<li>Si todavía no has vendido nada y podrías hacerlo con poco gasto: vende primero, negocia después.</li>
<li>Si lo que necesitas es cubrir un bache de tesorería, que es un problema distinto.</li>
</ul>
<h3>Lo que sí depende de ti antes de la primera reunión</h3>
<p>Tener los números a mano y poder enseñarlos sin improvisar: ventas por mes, lo que cuesta captar un cliente y cuánto tiempo se queda. Si aún no hay producto, un prototipo que se pueda tocar pesa más que cuarenta diapositivas; por eso muchos equipos empiezan por un <a href="/servicios/startups-e-inversores/mvp-en-6-12-semanas">producto mínimo viable</a> y unas <a href="/servicios/startups-e-inversores/metricas-para-inversores">métricas preparadas para inversores</a>. Las condiciones de cada préstamo o ayuda cambian: confírmalas siempre en la web del organismo o con tu asesoría, que es a quien corresponde esa parte. Si antes quieres ordenar la idea, vuelve a <a href="/guias/como-emprender-un-negocio">cómo emprender un negocio</a>.</p>""",
 "faq": [
  ("¿Cómo calcular cuánta financiación necesito para empezar mi negocio?", "Suma lo que cuesta llegar al primer cliente y los gastos fijos de los meses que tardarás en cubrirlos, con un margen de seguridad, y resta lo que ya tienes. Esa cifra, y no una redonda, es la que conviene llevar a un banco o a un inversor."),
  ("¿Qué hago si no consigo financiación para mi proyecto?", "Reduce el arranque: una versión más pequeña del producto, venta anticipada a los primeros clientes o empezar compaginándolo con otro trabajo. Un proyecto que ya vende, aunque sea poco, encuentra financiación con más facilidad."),
 ],
}

# Estructura: lista de síntomas + tabla «un trabajo, una herramienta» + regla de los treinta días
D["guias/herramientas-para-emprendedores"] = {
 "estructura": "sintomas-de-exceso + tabla-un-trabajo-una-herramienta + regla-de-treinta-dias",
 "lead": "Te has apuntado a una aplicación para las tareas, otra para las facturas, otra para los clientes y tres más que ya no recuerdas, y aun así sigues buscando cosas en el correo. Las herramientas digitales para emprendedores ayudan cuando son pocas y cada una tiene un trabajo claro que hacer.",
 "bloque": """<h2>¿Por qué con tantas aplicaciones sigo igual de desorganizado?</h2>
<p>Porque una herramienta ordena solo lo que tú ya has decidido cómo hacer. Si no hay una manera fija de apuntar un cliente nuevo o de dar por terminada una tarea, cada aplicación añade otro sitio donde mirar. Antes de comparar marcas, comprueba si te pasa esto.</p>
<ul>
<li>Apuntas lo mismo en dos sitios «por si acaso».</li>
<li>Pagas suscripciones que no has abierto en un mes.</li>
<li>Para saber cuánto te debe un cliente tienes que consultar más de una pantalla.</li>
<li>Probaste tres gestores de tareas y volviste a la libreta.</li>
<li>Cuando alguien te ayuda, tardas más en explicarle dónde está todo que en hacerlo tú.</li>
</ul>
<h3>Un trabajo, una herramienta</h3>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Trabajo</th><th>Qué necesitas que haga</th><th>Señal de que sobra o falta</th></tr></thead><tbody>
<tr><td>Saber a quién vender</td><td>Guardar contactos y lo último que hablasteis</td><td>Falta si dependes de tu memoria</td></tr>
<tr><td>Cobrar</td><td>Emitir facturas y ver cuáles están pendientes</td><td>Sobra una si facturas en dos programas</td></tr>
<tr><td>No olvidar nada</td><td>Una única lista de tareas con fecha</td><td>Sobra si tienes listas en tres sitios</td></tr>
<tr><td>Guardar documentos</td><td>Una carpeta compartida con nombres claros</td><td>Falta si acabas buscando en el correo</td></tr>
<tr><td>Cuentas e impuestos</td><td>Lo que acuerdes con tu asesoría</td><td>Pregúntale qué formato prefiere recibir</td></tr>
</tbody></table></div>
<h3>La regla de los treinta días</h3>
<p>Antes de contratar algo nuevo, hazlo a mano durante un mes: con papel, con una hoja de cálculo o con lo que ya tienes. Si al terminar sigues haciéndolo y te lleva tiempo, merece una herramienta. Si lo abandonaste, no era una necesidad y te has ahorrado la cuota.</p>
<p>Cuando varias de esas tareas empiezan a pisarse, suele compensar un único programa que las reúna; lo explicamos en <a href="/guias/que-es-un-software-de-gestion">qué es un software de gestión</a>. Y si acabas de darte de alta, en <a href="/blog/primeros-pasos-autonomo-digital">primeros pasos digitales para un nuevo autónomo</a> tienes el mínimo para empezar, o el <a href="/servicios/autonomos/kit-de-arranque-web-google-business-y-facturacion">kit de arranque</a> si prefieres recibirlo ya montado.</p>""",
 "faq": [
  ("¿Cómo elegir entre una herramienta gratuita y una de pago?", "Mira qué pasa con tus datos y con el límite de uso. Una gratuita vale mientras puedas exportar tu información y no dependas de ella para cobrar. Pasa a una de pago cuando un fallo o un límite te cueste más que la cuota."),
  ("¿Qué hago si ya tengo demasiadas aplicaciones y quiero simplificar?", "Haz una lista de todas, anota para qué usas cada una y cuándo la abriste por última vez. Quédate con una por trabajo, exporta los datos del resto y da de baja lo que sobre."),
 ],
}

# Estructura: definición de viabilidad + prueba de cuatro semanas + señales para replantear + ejemplo hipotético
D["guias/ideas-de-negocio-en-espana"] = {
 "estructura": "prueba-de-cuatro-semanas + senales-para-replantear + ejemplo-hipotetico-a-granel",
 "lead": "Llevas meses dándole vueltas: tienes una idea, o tres, y ninguna certeza de que alguna funcione. Dejar un sueldo o tocar los ahorros asusta, y las listas de ideas de negocio en España no te dicen cuál encaja contigo. Lo que sí puedes hacer es poner la tuya a prueba con poco gasto.",
 "bloque": """<h2>Tengo una idea de negocio y no sé si es viable: cómo comprobarlo sin jugarte los ahorros</h2>
<p>Una idea es viable cuando hay personas con un problema, dispuestas a pagar por resolverlo, a las que puedes llegar y atender dejando margen. Ninguna lista te lo va a confirmar; lo confirma una prueba pequeña y barata, hecha antes de alquilar un local o dejar tu trabajo.</p>
<h3>La prueba de las cuatro semanas</h3>
<ol>
<li><strong>Semana 1.</strong> Describe a tu cliente con nombre y situación, no con «todo el mundo». Busca dónde está: un barrio, un gremio, un grupo.</li>
<li><strong>Semana 2.</strong> Habla con quince. Pregunta cómo lo resuelven hoy y qué les cuesta. No vendas todavía: escucha.</li>
<li><strong>Semana 3.</strong> Ofrece una versión sencilla y ponle precio. Un «qué buena idea» no cuenta; cuenta un «¿cuándo puedes empezar?».</li>
<li><strong>Semana 4.</strong> Haz el trabajo para los primeros y apunta horas y gastos reales.</li>
</ol>
<h3>Señales de que conviene replantearla</h3>
<ul>
<li>Tienes que explicar el problema antes de que lo reconozcan.</li>
<li>Todos dicen que les gusta y nadie reserva.</li>
<li>Solo salen las cuentas si trabajas gratis.</li>
<li>Dependes de un único cliente o de un único proveedor.</li>
<li>Ya hay quien lo hace bien y no sabes decir en qué serías distinto.</li>
</ul>
<p>Ninguna de estas señales obliga a abandonar; indican qué cambiar: el cliente, el precio o la forma de entregarlo.</p>
<blockquote>Ejemplo hipotético: imagina a alguien que quiere abrir una tienda de productos a granel. Antes de buscar local, monta un puesto dos sábados en un mercado y ofrece reparto semanal en su barrio. Si se apuntan veinte vecinos, tiene clientes y datos; si se apuntan dos, ha gastado poco y ha aprendido mucho.</blockquote>
<p>Cuando la prueba salga bien, el siguiente paso es ordenar el arranque con <a href="/guias/como-emprender-un-negocio">cómo emprender un negocio</a> y, si vas a vender por internet, con <a href="/guias/como-iniciar-un-negocio-online">cómo iniciar un negocio online</a>. Y si quieres contrastarla con alguien de fuera, cuéntanosla en el <a href="/contacto#diagnostico">diagnóstico gratuito</a>: te diremos con franqueza qué parte digital le hace falta y cuál no.</p>""",
 "faq": [
  ("¿Cómo saber si mi idea de negocio es viable antes de invertir?", "Poniéndola a prueba a pequeña escala: habla con posibles clientes, ofrece una versión sencilla con precio y comprueba si alguien paga. Un primer cliente real vale más que cualquier estudio hecho desde casa."),
  ("¿Qué hago si alguien ya tiene la misma idea de negocio que yo?", "Es buena señal: indica que hay demanda. Lo que debes encontrar es en qué vas a ser distinto, ya sea la zona, el tipo de cliente, el trato o la rapidez. Copiar lo mismo y competir solo en precio rara vez sale bien."),
 ],
}

# Estructura: qué llevar escrito a la demo + frase un año después + tres miedos + cuándo aplazar
D["guias/mejores-erp-para-pymes"] = {
 "estructura": "deberes-antes-de-la-demo + frase-un-ano-despues + tres-miedos + cuando-aplazar",
 "lead": "Has visto tres demostraciones, todas parecían hacerlo todo y sigues sin saber cuál elegir. Mientras tanto, el miedo no cambia: pagar una implantación larga y que el equipo acabe volviendo a Excel. Para acertar con un ERP para tu pyme hay que mirar antes tu empresa que el catálogo del proveedor.",
 "bloque": """<h2>¿Por qué ninguna comparativa de ERP te dice cuál elegir?</h2>
<p>Porque comparan programas entre sí y tú necesitas compararlos con tu empresa. Dos pymes del mismo tamaño pueden necesitar cosas opuestas: una vive de servir pedidos rápido y otra de controlar obras que duran meses. Antes de volver a mirar marcas, prepara tu parte.</p>
<h3>Lo que debes llevar escrito a la demostración</h3>
<ol>
<li>El recorrido de un pedido normal, con quién interviene en cada paso.</li>
<li>Los tres casos raros que más guerra dan: la devolución parcial, el cliente con tarifa propia, la entrega en dos veces.</li>
<li>Los informes que hoy montas a mano cada mes.</li>
<li>Los programas que no vas a cambiar y con los que tendrá que entenderse.</li>
</ol>
<p>Pide que te enseñen esos casos con tus datos, no con la empresa de ejemplo. Si el comercial responde «eso se puede hacer» sin mostrarlo, apúntalo como pendiente, no como resuelto.</p>
<blockquote>«Nos enseñaron un programa precioso. Lo que no vimos fue cómo se hacía un albarán de los nuestros.» Es lo que se oye un año después de una elección precipitada.</blockquote>
<h3>Tres miedos razonables y cómo reducirlos</h3>
<ul>
<li><strong>Que el equipo no lo use.</strong> Implica desde el principio a quien lo va a manejar cada día, no solo a dirección.</li>
<li><strong>Que se alargue sin fin.</strong> Exige un calendario por fases, con algo funcionando pronto.</li>
<li><strong>Quedarte atado.</strong> Pregunta por escrito cómo te llevas tus datos si un día cambias.</li>
</ul>
<h3>Cuándo aplazar la decisión</h3>
<p>Si estás en plena campaña, cambiando de local o sin nadie que pueda dedicar horas al proyecto, espera. Un ERP implantado con prisas da peor resultado que uno implantado tres meses más tarde.</p>
<p>Para la parte de método tienes el <a href="/servicios/erp-para-pymes/analisis-de-tus-procesos-y-eleccion-de-modulos">análisis de procesos y elección de módulos</a> y la <a href="/servicios/erp-para-pymes/implantacion-por-fases-para-no-parar-el-negocio">implantación por fases</a>. Si ya tienes una oferta sobre la mesa y dudas, pide una <a href="/servicios/consultoria-y-ayudas/segunda-opinion-tecnologica">segunda opinión tecnológica</a> antes de firmar.</p>""",
 "faq": [
  ("¿Qué debo preparar antes de pedir una demo de ERP?", "El recorrido de un pedido normal, tus casos más complicados, los informes que hoy haces a mano y la lista de programas que quieres conservar. Con eso la demostración se hace sobre tu realidad y no sobre un ejemplo genérico."),
  ("¿Qué hago si mi equipo no quiere cambiar de programa?", "Averigua qué teme perder: suele ser un atajo o un dato que el programa nuevo no parece tener. Inclúyeles en las pruebas, empieza por un área pequeña y deja que vean un resultado antes de extenderlo."),
 ],
}

# Estructura: síntomas de parcheo + cuándo no hace falta + tabla de alternativas antes de programar
D["guias/software-a-medida"] = {
 "estructura": "sintomas-de-parcheo + cuando-no-hace-falta + tabla-de-caminos-alternativos",
 "lead": "Tu programa hace casi todo lo que necesitas, y ese «casi» lo cubres con un Excel paralelo, notas adhesivas y una persona que se sabe los trucos. Si te preguntas si el software a medida es para ti o un lujo de empresa grande, la respuesta está en cuánto te cuestan hoy esos parches.",
 "bloque": """<h2>¿Cómo sé si necesito software a medida o me vale un programa estándar?</h2>
<p>Necesitas algo hecho para ti cuando adaptar tu forma de trabajar al programa te hace perder lo que te distingue, o cuando los parches ya consumen más horas que el propio trabajo. Si un programa estándar cubre lo tuyo sin rodeos, quédate con él: es más rápido de poner en marcha.</p>
<ul>
<li>Exportas a Excel cada semana para hacer lo que el programa no hace.</li>
<li>Hay un paso que solo sabe hacer una persona, y cuando falta se para.</li>
<li>Usas un campo de «observaciones» para guardar datos importantes.</li>
<li>Has pedido un cambio al fabricante y la respuesta fue «está en la lista».</li>
<li>Tu presupuesto, tu tarifa o tu forma de planificar no caben en las pantallas.</li>
</ul>
<h3>Cuándo un programa estándar es la opción sensata</h3>
<p>Si acabas de empezar y aún estás descubriendo cómo trabajas, no encargues nada a medida: programarías un proceso que cambiará en pocos meses. Tampoco si tu necesidad es común a todo tu sector y ya existe un programa especializado que la resuelve. Lo sensato es hacer a medida solo la parte que te diferencia y dejar lo corriente (facturas, contabilidad, correo) en herramientas probadas.</p>
<h3>Cuatro caminos, del más ligero al más ambicioso</h3>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Camino</th><th>Te conviene si</th><th>Vigila</th></tr></thead><tbody>
<tr><td>Configurar mejor lo que ya tienes</td><td>El programa lo permite y nadie lo ha explorado</td><td>Que no acabe en más parches</td></tr>
<tr><td>Conectar dos programas</td><td>Cada uno hace bien su parte, pero no se pasan datos</td><td>Quién mantiene la conexión</td></tr>
<tr><td>Base modular con una pieza propia</td><td>Lo común te vale y solo una parte es especial</td><td>Que la pieza quede documentada</td></tr>
<tr><td>Desarrollo completo</td><td>Tu proceso es el negocio y nada se le parece</td><td>Alcance cerrado y entregas por partes</td></tr>
</tbody></table></div>
<p>Si decides seguir adelante, prepara la petición con <a href="/guias/como-pedir-presupuesto-de-software-a-medida">cómo pedir presupuesto de software a medida</a> y repasa las fases en <a href="/guias/desarrollo-de-software-a-medida">desarrollo de software a medida</a>. Para ver casos por actividad, tienes el <a href="/guias/software-a-medida-por-sectores">software a medida por sectores</a>.</p>""",
 "faq": [
  ("¿Cómo saber si me compensa un software a medida o adaptar el programa que ya tengo?", "Cuenta las horas semanales que se van en rodeos: exportar, copiar, corregir. Si son pocas, configura mejor lo que tienes. Si son muchas y afectan a lo que te distingue de la competencia, una pieza a medida suele compensar."),
  ("¿Es mejor un software a medida o seguir con Excel en una empresa pequeña?", "Excel sirve mientras lo use una persona y el volumen sea bajo. Cuando varias personas necesitan el mismo dato o un error en la hoja te cuesta un cliente, toca pasar a un programa, que no siempre tiene que ser a medida."),
 ],
}

# Estructura: dependencia de secretaría + frase literal + tabla «quién pregunta qué» + reglas por escribir
D["guias/software-a-medida-para-academias"] = {
 "estructura": "dependencia-de-secretaria + frase-literal + tabla-quien-pregunta-que + reglas-por-escribir",
 "lead": "En septiembre la secretaría no da abasto: matrículas por WhatsApp, recibos devueltos, padres que preguntan el horario y un grupo que se llena sin que nadie avise. El software a medida para academias tiene sentido cuando el programa genérico no entiende de cursos, grupos y cuotas como los tuyos.",
 "bloque": """<h2>¿Por qué tu academia depende de una sola persona en secretaría?</h2>
<p>Porque la información está repartida entre su cabeza, una hoja de cálculo y el móvil del centro. Ella sabe qué alumno paga en dos plazos, quién tiene descuento por hermano y a qué familia hay que avisar por la tarde. El día que enferma en plena campaña de matrícula, nadie más puede cobrar ni contestar.</p>
<blockquote>«El programa me deja apuntar alumnos, pero no sabe que el grupo de los martes comparte aula con el de refuerzo.»</blockquote>
<p>Esa es la frontera: los programas genéricos manejan fichas y recibos; lo que no suelen conocer son tus reglas. Y las reglas cambian mucho entre una academia de idiomas, una autoescuela, un centro de oposiciones y una escuela infantil.</p>
<h3>Lo que cada persona debería poder ver sin preguntar</h3>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Quién</th><th>Hoy pregunta</th><th>Debería verlo sin ayuda</th></tr></thead><tbody>
<tr><td>Dirección</td><td>¿Cuántas bajas llevamos este trimestre?</td><td>Altas, bajas y plazas libres por grupo</td></tr>
<tr><td>Secretaría</td><td>¿Este recibo se devolvió o no llegó a pasarse?</td><td>Estado de cada cuota y avisos pendientes</td></tr>
<tr><td>Profesorado</td><td>¿Quién viene hoy y quién recupera clase?</td><td>Lista del grupo y faltas desde el móvil</td></tr>
<tr><td>Familias y alumnos</td><td>¿A qué hora es el examen?</td><td>Horario, avisos y pagos en su propio acceso</td></tr>
</tbody></table></div>
<h3>Reglas que conviene escribir antes de pedir nada</h3>
<ul>
<li>Cómo se cobra: mensualidad, bono de clases, curso completo, matrícula aparte.</li>
<li>Qué pasa con una falta: se recupera, se pierde o caduca.</li>
<li>Cuándo un grupo se desdobla o se cierra.</li>
<li>Quién puede aplicar un descuento y con qué límite.</li>
</ul>
<p>Con esas cuatro respuestas por escrito sabrás si te vale un programa de gestión de academias corriente o si hay algo propio que programar. Para los cobros, mira <a href="/servicios/software-de-gestion/bonos-cuotas-y-suscripciones">bonos, cuotas y suscripciones</a> y <a href="/servicios/software-de-gestion/remesas-y-domiciliaciones">remesas y domiciliaciones</a>; para los horarios, <a href="/servicios/software-de-gestion/reservas-de-mesas-salas-clases-o-servicios">reservas de clases y salas</a>.</p>""",
 "faq": [
  ("¿Cómo gestionar las matrículas de una academia sin hojas de Excel?", "Con un formulario de inscripción que cree la ficha del alumno, lo asigne a su grupo y genere la cuota que le corresponde. Así secretaría revisa en lugar de teclear y la plaza se descuenta sola."),
  ("¿Merece la pena un programa a medida para una academia con pocos alumnos?", "Normalmente no. Con pocos grupos y cuotas sencillas, un programa estándar de academias es suficiente. Lo propio compensa cuando tus reglas de cobro, recuperaciones o grupos no caben en ninguno."),
 ],
}

# Estructura: del dato que nace en la parcela + tabla «hoy / en el momento» + exigencias del campo + cuándo basta una app
D["guias/software-a-medida-para-agricultura"] = {
 "estructura": "dato-que-nace-en-la-parcela + tabla-hoy-frente-a-en-el-momento + exigencias-del-campo + cuando-basta-una-app",
 "lead": "Acabas la jornada a las diez de la noche y todavía falta apuntar el tratamiento de hoy, las horas de la cuadrilla y los kilos que entraron. Cuando llega una inspección o el comprador pide la trazabilidad, toca reconstruirlo de memoria. Ahí empieza a tener sentido un software a medida para agricultura y ganadería.",
 "bloque": """<h2>¿Por qué el papeleo del campo siempre se hace tarde y de memoria?</h2>
<p>Porque el dato nace en la parcela y se apunta en la cocina. Entre un sitio y otro pasan horas, a veces días, y por el camino se pierden la dosis exacta, la hora o el nombre de quien lo aplicó. No es falta de interés: en plena campaña nadie se sienta delante de un ordenador.</p>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Momento</th><th>Cómo se hace hoy</th><th>Con el registro hecho en el momento</th></tr></thead><tbody>
<tr><td>Tratamiento o abonado</td><td>Se apunta de noche, si uno se acuerda</td><td>Se marca en el móvil al terminar, con parcela y producto</td></tr>
<tr><td>Recolección</td><td>Vales de papel por cuadrilla</td><td>Kilos por parcela y por persona al pesar</td></tr>
<tr><td>Entrada en cooperativa, bodega o almazara</td><td>Báscula por un lado, liquidación por otro</td><td>El peso y la calidad pasan solos a la cuenta del socio</td></tr>
<tr><td>Venta</td><td>Se busca el lote en carpetas</td><td>Se sabe de qué parcela salió cada partida</td></tr>
</tbody></table></div>
<h3>Lo que el campo exige a un programa y una oficina no</h3>
<ul>
<li>Funcionar sin señal y enviar los datos al recuperarla.</li>
<li>Botones grandes, pocos pasos y que se pueda usar con guantes o a pleno sol.</li>
<li>Hablar en tus unidades: fanegas, cajas, cántaras, cabezas.</li>
<li>Aguantar la estacionalidad: tres meses de locura y nueve de calma.</li>
<li>Varias personas apuntando a la vez sin pisarse.</li>
</ul>
<h3>Cuándo te vale una aplicación de cuaderno de campo ya hecha</h3>
<p>Si llevas una explotación con pocos cultivos y solo quieres tener el cuaderno al día, una aplicación estándar suele bastar y es lo primero que deberías probar. Lo propio empieza a compensar cuando hay liquidaciones a socios, varias fincas con costes separados, transformación (vino, aceite, queso) o un cliente que te exige su propio formato de trazabilidad.</p>
<p>Para esa parte, mira cómo funcionan los <a href="/servicios/software-de-gestion/lotes-trazabilidad-y-caducidades">lotes y la trazabilidad</a> y la <a href="/servicios/software-de-gestion/app-para-tecnicos-de-campo">aplicación para trabajo de campo</a>. Qué registros son obligatorios en tu caso te lo confirma tu técnico o tu cooperativa; el programa solo consigue que apuntarlos no dependa de la memoria.</p>""",
 "faq": [
  ("¿Merece la pena digitalizar una explotación agrícola pequeña?", "Sí cuando el papeleo te quita horas de descanso o un comprador te pide registros que hoy reconstruyes a mano. Para una finca pequeña suele bastar una aplicación sencilla de cuaderno de campo, sin desarrollos propios."),
  ("¿Cómo apuntar los tratamientos y labores sin esperar a llegar a casa?", "Desde el móvil, al terminar cada labor, eligiendo parcela y producto en una lista ya preparada. Si no hay señal, el dato se guarda en el teléfono y se envía más tarde."),
 ],
}

# Estructura: seis preguntas de autodiagnóstico + dónde se quedan cortos los genéricos + qué exigir + límite en cita
D["guias/software-a-medida-para-clinicas"] = {
 "estructura": "seis-preguntas-con-recepcion + limites-del-generico-por-especialidad + que-exigir + lo-que-no-decide",
 "lead": "La agenda llena en el papel y la sala medio vacía: dos pacientes no han venido, recepción lleva la mañana al teléfono y tú sigues sin saber cuántos presupuestos te han aceptado este mes. Antes de buscar software a medida para clínicas, conviene saber qué te falla y si un programa del sector ya lo resuelve.",
 "bloque": """<h2>¿Tu clínica necesita un programa distinto o usar mejor el que tiene?</h2>
<p>La mayoría de clínicas no necesitan empezar de cero: necesitan saber qué parte de su día no cabe en el programa actual. Contesta a estas preguntas con recepción delante, que es quien conoce los rodeos.</p>
<ol>
<li>¿Cuántas veces al día se apunta lo mismo en la agenda y en otro sitio?</li>
<li>¿Puede un paciente pedir o cambiar su cita sin llamar?</li>
<li>¿Sabes cuántos huecos quedaron vacíos la semana pasada y por qué?</li>
<li>¿El historial de una persona está entero en una pantalla, o hay parte en papel y parte en el equipo de diagnóstico?</li>
<li>¿Cada profesional ve solo lo que le corresponde?</li>
<li>Si mañana abrieras una segunda consulta, ¿el programa te seguiría?</li>
</ol>
<p>Si has dudado en una o dos, seguramente basta con configurar mejor lo que tienes. Si son cuatro o más, el programa se ha quedado pequeño.</p>
<h3>Dónde suelen quedarse cortos los programas genéricos</h3>
<p>En lo que distingue a cada especialidad. Un dentista trabaja con planes de tratamiento largos y presupuestos por fases; un fisioterapeuta, con bonos de sesiones y cabinas; un psicólogo necesita discreción extrema y pocas pantallas; una óptica o una veterinaria añaden producto y almacén. Un programa pensado para «clínicas» en general obliga a todos a dar rodeos.</p>
<h3>Lo que debes exigir antes de contratar a nadie</h3>
<ul>
<li>Que te enseñen quién puede ver cada dato y cómo queda anotado quién entró.</li>
<li>Dónde se alojan los datos y cómo se hacen las copias.</li>
<li>Cómo se saca el historial si cambias de proveedor.</li>
<li>Que la persona de recepción pruebe una mañana real antes de firmar.</li>
</ul>
<blockquote>Un programa de clínica ordena, recuerda y avisa. No diagnostica, no decide tratamientos y no sustituye el criterio de quien atiende.</blockquote>
<p>Para empezar por lo que más se nota, mira la <a href="/servicios/software-de-gestion/agenda-y-citas-online">agenda con citas online</a> y los <a href="/servicios/software-de-gestion/recordatorios-automaticos-por-whatsapp">recordatorios automáticos</a>. Las obligaciones sobre datos de salud las tienes más abajo en esta guía, y debe validarlas quien te asesore en protección de datos.</p>""",
 "faq": [
  ("¿Cómo saber si el programa de mi clínica se ha quedado pequeño?", "Cuando recepción apunta lo mismo en dos sitios, parte del historial sigue en papel, no puedes saber cuántas citas se perdieron o abrir una segunda consulta obligaría a duplicarlo todo. Una o dos señales se arreglan configurando; varias indican cambio."),
  ("¿Qué es mejor para una clínica, un programa del sector o uno a medida?", "Empieza mirando los programas de tu especialidad: suelen cubrir agenda, historial y cobros. Lo hecho a medida compensa cuando combinas varias especialidades, tienes varios centros o trabajas de una forma que esos programas no contemplan."),
 ],
}

# Estructura: cuenta con la última obra cerrada + tabla de descuidos y lo que arrastran + cuadrilla pequeña
D["guias/software-a-medida-para-construccion"] = {
 "estructura": "cuenta-con-tu-ultima-obra + tabla-descuidos-y-consecuencias + caso-cuadrilla-pequena",
 "lead": "Terminas la obra, haces cuentas y el beneficio que había en el presupuesto no aparece. Entre los extras que nadie apuntó, el material que se pidió dos veces y las horas de más, el margen se fue sin avisar. El software a medida para construcción y reformas sirve para ver esa fuga con la obra todavía abierta.",
 "bloque": """<h2>¿Dónde se pierde el margen entre el presupuesto y el final de la obra?</h2>
<p>Se pierde en lo que no queda escrito el mismo día. Un cambio que el cliente pide de palabra, un viaje extra al almacén, media jornada esperando a otro gremio. Nada de eso figura en el presupuesto y casi nunca llega a la factura.</p>
<h3>Haz la cuenta con tu última obra cerrada</h3>
<ol>
<li>Coge el presupuesto aceptado y suma las partidas.</li>
<li>Suma las facturas de material y de subcontratas de esa obra.</li>
<li>Calcula las horas reales de tu gente, no las previstas.</li>
<li>Anota los extras que hiciste y cuáles llegaste a cobrar.</li>
</ol>
<p>Compara el primer número con los otros tres y tendrás tu margen de verdad. Si te ha costado más de una tarde reunir esos datos, ya tienes el diagnóstico: la información existe, pero dispersa entre albaranes, mensajes y la memoria del encargado.</p>
<h3>Cuatro descuidos corrientes y lo que arrastran</h3>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Descuido</th><th>Lo que provoca</th></tr></thead><tbody>
<tr><td>Extras acordados de palabra</td><td>Discusión al cobrar o trabajo regalado</td></tr>
<tr><td>Partes en papel, entregados el viernes</td><td>Horas que se olvidan o se redondean</td></tr>
<tr><td>Pedidos de material por teléfono</td><td>Nadie sabe a qué obra cargar cada albarán</td></tr>
<tr><td>Certificaciones hechas a ojo</td><td>Se cobra tarde y de menos</td></tr>
</tbody></table></div>
<h3>¿Y si solo somos tres?</h3>
<p>Entonces no necesitas un gran sistema. Una cuadrilla pequeña gana mucho solo con dos cosas: presupuestos que salgan de las mediciones sin rehacerlos y partes diarios desde el móvil con foto. Lo demás puede esperar a que crezcas.</p>
<p>Tienes el detalle en <a href="/servicios/software-de-gestion/presupuestos-desde-mediciones">presupuestos desde mediciones</a>, <a href="/servicios/software-de-gestion/obras-y-proyectos-presupuesto-frente-a-real">presupuesto frente a coste real por obra</a> y <a href="/servicios/software-de-gestion/ordenes-y-partes-de-trabajo-con-firma-y-fotos">partes de trabajo con firma y fotos</a>. Si en tus obras no hay cobertura, el registro de jornada puede hacerse con el <a href="/servicios/fichador/modo-sin-conexion-para-obras">modo sin conexión</a>.</p>""",
 "faq": [
  ("¿Cómo saber si una reforma me ha dejado beneficio?", "Compara lo presupuestado con lo gastado de verdad en material, subcontratas y horas propias, y suma los extras que no cobraste. Si reunir esos datos te lleva más de una tarde, el problema es que están dispersos."),
  ("¿Qué programa necesita un autónomo de reformas que trabaja solo o con un ayudante?", "Uno sencillo que haga presupuestos rápidos, guarde fotos y cambios acordados con el cliente y saque la factura del presupuesto. No hace falta un sistema de control de obra completo."),
 ],
}

# Estructura: caja llena y poco margen + escena de un viernes + tabla de creencias + tres números + por dónde no empezar
D["guias/software-a-medida-para-hosteleria"] = {
 "estructura": "escena-de-un-viernes + tabla-se-piensa-frente-a-pasa + tres-numeros-semanales + por-donde-no-empezar",
 "lead": "Sábado noche, comedor lleno y buena caja. El lunes miras la cuenta y no entiendes por qué queda tan poco. Entre compras, personal y lo que se tira, el dinero se escapa por sitios que el TPV no enseña. De eso trata el software a medida para hostelería: de ver lo que ocurre detrás de la barra.",
 "bloque": """<h2>¿Por qué mi restaurante llena y aun así no gano dinero?</h2>
<p>Porque llenar mide las ventas, no lo que queda. Lo que queda depende de tres cosas que casi ningún local mira a diario: lo que cuesta de verdad cada plato, las horas de personal que has puesto para servirlo y lo que acaba en el cubo.</p>
<p>Piensa en un viernes cualquiera. Se compra de más «por si acaso», el cocinero cambia la ración a ojo, entran dos extras que no hacían falta y la carta sigue con los precios de hace un año. Ninguna decisión parece grave, y juntas se comen el margen.</p>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Lo que se suele pensar</th><th>Lo que suele pasar</th></tr></thead><tbody>
<tr><td>«El plato que más vendo es el que más me deja»</td><td>A menudo es el de margen más corto; el rentable está escondido en la carta</td></tr>
<tr><td>«Con el TPV ya lo controlo todo»</td><td>El TPV sabe lo que cobras, no lo que gastas en producirlo</td></tr>
<tr><td>«El problema es que la gente no rinde»</td><td>Suele ser el cuadrante: sobran manos el martes y faltan el domingo</td></tr>
<tr><td>«Eso es para cadenas»</td><td>Un bar con seis mesas también pierde dinero en compras y mermas</td></tr>
</tbody></table></div>
<h3>Tres números que deberías poder ver cada semana</h3>
<ul>
<li>Coste de materia prima sobre ventas, por familia de platos.</li>
<li>Coste de personal sobre ventas, por turno.</li>
<li>Lo que se tiró y por qué: caducado, mal elaborado, devuelto.</li>
</ul>
<h3>Por dónde no empezar</h3>
<p>No empieces por cambiarlo todo en agosto, ni por la aplicación para clientes, ni por la pantalla más vistosa. Empieza por lo que ya tienes: si tu caja permite sacar ventas por plato y por hora, con eso y tus facturas de proveedores ya puedes hacer la primera cuenta a mano. El programa viene después, para que no dependa de que alguien se acuerde.</p>
<p>La caja la tratamos aparte en la guía de <a href="/guias/software-tpv-para-hosteleria">software TPV para hostelería</a>. Para el resto, mira <a href="/servicios/software-de-gestion/pedidos-a-proveedores">pedidos a proveedores</a>, <a href="/servicios/fichador/turnos-y-cuadrantes">turnos y cuadrantes</a> y el <a href="/servicios/software-especializado/appcc-digital-para-hosteleria-y-alimentacion">APPCC digital</a> si aún llevas las temperaturas en papel.</p>""",
 "faq": [
  ("¿Por qué mi bar factura mucho y gana poco?", "Lo más frecuente es una combinación de compras sin control, raciones que no coinciden con el precio de carta y horas de personal mal repartidas entre turnos. Mirar cada semana materia prima, personal y mermas sobre ventas enseña cuál pesa más."),
  ("¿Hace falta un programa a medida para un bar pequeño?", "Casi nunca. Un bar pequeño necesita una buena caja, un control sencillo de compras y un cuadrante claro. Lo hecho a medida compensa con varios locales, catering, eventos o una forma de trabajar que los programas de hostelería no recogen."),
 ],
}

# Estructura: frases del gerente de planta + tabla «con qué trabajas / hasta dónde llega» + señales de ir tarde + un solo dato
D["guias/software-a-medida-para-industria"] = {
 "estructura": "frases-del-gerente-de-planta + tabla-con-que-trabajas + senales-de-ir-tarde + medir-un-solo-dato",
 "lead": "El cliente llama para saber cómo va su pedido y tienes que bajar a la planta a preguntarlo. Nadie sabe con certeza cuánto costó fabricar el último lote y la planificación vive en una pizarra. Si esa es tu fábrica, el software a medida para industria no empieza por las máquinas, sino por el dato que hoy te falta.",
 "bloque": """<h2>«Baja a preguntar cómo va»: cuando la información de la fábrica solo está en la planta</h2>
<ul>
<li>«No sé si este pedido lo he vendido ganando o perdiendo.»</li>
<li>«El jefe de taller se va de vacaciones y cruzamos los dedos.»</li>
<li>«Planifico en una hoja que solo entiendo yo.»</li>
<li>«Cuando un cliente reclama, tardamos un día en saber de qué bobina salió.»</li>
<li>«Las horas se apuntan a final de turno, más o menos.»</li>
</ul>
<p>Si has dicho alguna de estas frases, el problema no es de máquinas ni de gente: falta un registro que se haga mientras se trabaja y no después.</p>
<h3>¿Qué tienes ya y qué le falta?</h3>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Con qué trabajas</th><th>Hasta dónde llega</th><th>Dónde se queda corto</th></tr></thead><tbody>
<tr><td>Pizarra, papel y Excel</td><td>Planta pequeña, pocos pedidos a la vez</td><td>No deja histórico ni avisa de retrasos</td></tr>
<tr><td>ERP generalista</td><td>Compras, existencias y facturas</td><td>No sabe qué pasa dentro de cada orden</td></tr>
<tr><td>Programa de producción de catálogo</td><td>Órdenes, tiempos y máquinas</td><td>Te obliga a fabricar como él dice</td></tr>
<tr><td>Pieza a medida unida a tu ERP</td><td>Tu proceso real, con tus pasos</td><td>Hay que definirla bien y mantenerla</td></tr>
</tbody></table></div>
<h3>Señales de que ya vas tarde</h3>
<ol>
<li>Aceptas plazos sin conocer la carga real de la planta.</li>
<li>Repites un trabajo y nadie encuentra cómo se hizo la vez anterior.</li>
<li>Una auditoría o un cliente grande te pide registros que no tienes.</li>
<li>El margen baja y no sabes en qué producto.</li>
</ol>
<h3>Lo primero no es comprar nada</h3>
<p>Lo primero es elegir un solo dato y medirlo bien durante un mes: por ejemplo, las horas reales por orden en una sección. Con eso sabrás si tus presupuestos se parecen a la realidad y tendrás un argumento sólido para decidir qué programa necesitas, o si te basta con ajustar el que tienes.</p>
<p>Cuando llegue el momento, mira la <a href="/servicios/software-especializado/planificacion-de-produccion">planificación de producción</a>, la <a href="/servicios/software-especializado/gestion-de-calidad-iso-sin-papel">gestión de calidad sin papel</a> y la parte de <a href="/servicios/erp-para-pymes/produccion-obras-o-servicios-segun-tu-sector">producción dentro del ERP</a>.</p>""",
 "faq": [
  ("¿Por dónde empiezo a digitalizar una fábrica pequeña?", "Por un único dato que hoy no tengas y que te cueste dinero no conocer, como las horas reales por orden de fabricación. Mídelo en una sección durante un mes antes de pensar en cambiar de programa."),
  ("¿Qué diferencia hay entre un ERP y un programa de control de producción?", "El ERP lleva compras, existencias, ventas y facturas. El control de producción sigue lo que pasa dentro de la planta: qué orden está en qué máquina, cuánto tiempo lleva y con qué material. Lo habitual es que trabajen unidos."),
 ],
}

# Estructura: línea de tiempo de un contacto + tabla por actividad + cuándo no compensa
D["guias/software-a-medida-para-inmobiliarias"] = {
 "estructura": "linea-de-tiempo-de-un-contacto + tabla-por-actividad-inmobiliaria + cuando-no-compensa",
 "lead": "Un comprador escribe el sábado a las nueve de la noche por un piso del portal. El lunes le llamas y ya ha visitado otro con la agencia de enfrente. Entre portales, WhatsApp, llaves y propietarios que piden novedades, el día se va en contestar. Para eso se plantea un software a medida para inmobiliarias.",
 "bloque": """<h2>¿Qué le pasa a un contacto desde que escribe hasta que visita el piso?</h2>
<p>Le pasa que espera, y mientras espera sigue buscando. Sigue el camino de un interesado cualquiera en tu agencia y mira dónde se enfría.</p>
<ol>
<li><strong>Sábado, 21:00.</strong> Pregunta por un anuncio. El correo del portal llega a una bandeja que nadie mira hasta el lunes.</li>
<li><strong>Lunes, 10:30.</strong> Un agente le llama. No lo coge. Se apunta en un papel «volver a llamar».</li>
<li><strong>Martes.</strong> Contesta por WhatsApp al móvil personal del agente. La conversación ya no está en ningún sitio de la agencia.</li>
<li><strong>Jueves.</strong> Visita. Nadie anota qué le gustó, cuánto puede pagar ni qué zona prefiere.</li>
<li><strong>Un mes después.</strong> Entra un piso que le encajaría. Nadie se acuerda de él.</li>
</ol>
<p>En cinco pasos hay cuatro fugas, y ninguna se debe a mala voluntad. Se deben a que cada dato cae en un sitio distinto.</p>
<h3>Lo que cambia según a qué te dediques</h3>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Tu actividad</th><th>Lo que más tiempo se lleva</th><th>Lo primero que conviene ordenar</th></tr></thead><tbody>
<tr><td>Compraventa</td><td>Contestar y cualificar interesados</td><td>Entrada única de contactos y seguimiento</td></tr>
<tr><td>Alquiler de larga duración</td><td>Recibos, incidencias y renovaciones</td><td>Cobros y avisos de vencimiento</td></tr>
<tr><td>Administración de fincas</td><td>Llamadas de vecinos y proveedores</td><td>Registro de incidencias con estado visible</td></tr>
<tr><td>Alquiler vacacional</td><td>Entradas, salidas y limpieza</td><td>Calendario único y avisos automáticos</td></tr>
</tbody></table></div>
<h3>Cuándo no te compensa</h3>
<p>Si llevas veinte inmuebles tú solo y contestas en el día, un buen programa inmobiliario de catálogo y disciplina te bastan. Lo propio empieza a tener sentido con varios agentes, varias oficinas o un modo de repartir comisiones y captaciones que ningún programa estándar refleja.</p>
<p>Si el cuello de botella es la primera respuesta, mira el <a href="/servicios/agentes-de-ia/agente-inmobiliario">agente inmobiliario con IA</a> y la <a href="/servicios/software-de-gestion/captacion-de-leads-desde-web-whatsapp-y-anuncios">captación de contactos en una sola bandeja</a>; para viviendas turísticas, el <a href="/servicios/alojamientos-y-domotica/calendario-unificado-con-airbnb-booking-y-web-propia">calendario unificado</a>.</p>""",
 "faq": [
  ("¿Cómo evitar que se pierdan los contactos que llegan de los portales inmobiliarios?", "Haciendo que todos entren en un mismo sitio, sea cual sea el portal o el canal, con aviso inmediato al agente y una tarea de seguimiento. Lo que se pierde no es el contacto, sino el recuerdo de volver a llamarle."),
  ("¿Qué programa le basta a una inmobiliaria pequeña con uno o dos agentes?", "Un programa inmobiliario estándar que publique en portales, guarde la ficha de cada interesado y recuerde los seguimientos. El desarrollo propio se reserva para agencias con más equipo o reglas internas particulares."),
 ],
}

# Estructura: tropiezos en lista de definiciones + dos primeras semanas sin comprar + lo que no arregla un programa
D["guias/software-a-medida-para-logistica"] = {
 "estructura": "tropiezos-de-reparto-en-dl + dos-semanas-sin-comprar + lo-que-no-arregla-un-programa",
 "lead": "La furgoneta vuelve con dos entregas sin hacer, un albarán sin firmar y un cliente que jura que pidió otra cosa. En la oficina, alguien pasa la mañana contestando «¿por dónde va lo mío?». En reparto, esos fallos pequeños son el margen, y ahí tiene trabajo un software a medida para distribución y logística.",
 "bloque": """<h2>¿Cuánto te cuesta cada entrega que sale mal?</h2>
<p>Más de lo que parece, porque el coste no está en la factura sino alrededor: el segundo viaje, la llamada, el abono, la mercancía que vuelve y hay que recolocar. Estos son los tropiezos que más se repiten en un mayorista o en una empresa de reparto.</p>
<dl>
<dt>Pedido tomado por teléfono y apuntado a mano</dt><dd>Una referencia mal entendida es una devolución segura, y nadie puede demostrar qué se pidió.</dd>
<dt>Preparación sin comprobar</dt><dd>Sale una caja de menos; el cliente lo descubre al abrir y retiene el pago hasta que se aclare.</dd>
<dt>Ruta decidida por costumbre</dt><dd>Kilómetros y horas de más, y clientes que reciben siempre a última hora.</dd>
<dt>Albarán en papel</dt><dd>Se moja, se pierde o llega a la oficina una semana después. Hasta entonces no se factura.</dd>
<dt>Cliente ausente</dt><dd>El viaje se paga dos veces y la mercancía ocupa sitio en el muelle.</dd>
</dl>
<h3>Las dos primeras semanas, sin comprar nada</h3>
<ol>
<li><strong>Días 1 a 5.</strong> Apunta cada incidencia en una hoja común: qué pasó, con qué cliente, quién la detectó.</li>
<li><strong>Días 6 a 10.</strong> Agrúpalas. Verás que dos o tres causas explican casi todas.</li>
<li><strong>Días 11 a 14.</strong> Elige la más frecuente y arréglala con lo que tengas: una comprobación al cargar, una foto del albarán, un mensaje de aviso antes de salir.</li>
</ol>
<p>Con esa lista en la mano ya no pedirás «un programa de logística», sino la solución a un problema concreto, y cualquier proveedor tendrá que hablarte en esos términos.</p>
<h3>Lo que no arregla ningún programa</h3>
<p>Un almacén sin ordenar, tarifas que cada comercial aplica a su manera o clientes sin dirección de entrega correcta. Eso se limpia antes; si no, el programa reproducirá el desorden más deprisa.</p>
<p>Cuando toque, estas son las piezas habituales: <a href="/servicios/software-de-gestion/portal-de-pedidos-b2b">portal de pedidos para tus clientes</a>, <a href="/servicios/software-de-gestion/planificacion-de-rutas">planificación de rutas</a> y <a href="/servicios/software-de-gestion/gestion-de-flotas">gestión de flotas</a>. El detalle del almacén está en la guía de <a href="/guias/erp-para-logistica-y-almacen">software de gestión de almacenes</a>.</p>""",
 "faq": [
  ("¿Cómo reducir las entregas fallidas en una empresa de reparto?", "Avisando al cliente antes de salir, confirmando la franja de entrega y comprobando la carga con el pedido delante. Registrar el motivo de cada entrega fallida durante unas semanas enseña cuál de las tres medidas hace más falta."),
  ("¿Qué programa necesita un mayorista pequeño con una o dos furgonetas?", "Uno que recoja los pedidos sin tener que apuntarlos a mano, saque la hoja de carga y permita firmar el albarán en el móvil. La planificación de rutas compleja suele hacer falta más adelante, con más vehículos."),
 ],
}

# Estructura: por qué se va el tiempo en copiar + frase literal + tabla de cuatro maneras de trabajar + prueba del grupo + lo que sigue siendo humano
D["guias/software-a-medida-para-turismo"] = {
 "estructura": "tiempo-perdido-en-copiar + tabla-cuatro-maneras-de-trabajar + prueba-del-grupo-de-cuarenta + criterio-humano",
 "lead": "Un cliente pide un viaje a medida y tardas dos días en mandarle el presupuesto, porque hay que consultar tres proveedores, copiar precios y maquetar el documento. Cuando lo recibe, ya ha reservado por su cuenta. El software a medida para agencias de viajes ataca ese retraso y los errores de copiar datos.",
 "bloque": """<h2>¿Por qué tardas dos días en enviar un presupuesto de viaje?</h2>
<p>Porque montar un viaje es juntar piezas que viven en sitios distintos: el vuelo en una plataforma, el hotel en otra, el traslado en un correo y la excursión en la cabeza de quien la organizó la última vez. El tiempo no se va en pensar el viaje, se va en copiar.</p>
<blockquote>«Cambió la fecha de salida y tuve que rehacer el documento entero, a las once de la noche.»</blockquote>
<p>Y copiar tiene un segundo coste: el error. Un nombre que no coincide con el pasaporte, un precio antiguo, un traslado que nadie confirmó.</p>
<h3>Cuatro maneras de trabajar y hasta dónde aguanta cada una</h3>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Forma de trabajar</th><th>Funciona si</th><th>Se rompe cuando</th></tr></thead><tbody>
<tr><td>Correo, procesador de textos y hoja de cálculo</td><td>Pocos viajes al mes, muy artesanales</td><td>Coinciden varias salidas o falta la persona que lo lleva</td></tr>
<tr><td>Programa de agencia de catálogo</td><td>Vendes sobre todo paquetes de mayorista</td><td>Tu producto es propio y no cabe en sus plantillas</td></tr>
<tr><td>Plataformas de reservas sueltas</td><td>Cada una hace bien lo suyo</td><td>Hay que pasar los datos de una a otra a mano</td></tr>
<tr><td>Conexión a medida entre lo que ya usas</td><td>Tienes producto propio y volumen</td><td>No se ha definido qué dato manda sobre cuál</td></tr>
</tbody></table></div>
<h3>La prueba del grupo de cuarenta</h3>
<p>Imagina que mañana entra un grupo de cuarenta personas con dos hoteles, guía en dos idiomas y un cambio de vuelo a última hora. Pregúntate quién se entera del cambio, cómo se avisa a los viajeros y cuántos documentos hay que tocar. Si la respuesta es «depende de quién esté ese día», ahí tienes tu punto débil.</p>
<h3>Lo que debe seguir en manos de una persona</h3>
<ul>
<li>Elegir proveedor cuando hay dudas de calidad.</li>
<li>Resolver una incidencia en destino.</li>
<li>Decidir qué se le ofrece a un cliente que no sabe lo que quiere.</li>
</ul>
<p>El programa quita el copiar y el perseguir; el criterio sigue siendo tuyo. Para lo primero, mira las <a href="/servicios/software-de-gestion/integraciones-por-api">integraciones por API</a> y el <a href="/servicios/software-de-gestion/presupuestador-y-configurador-online">presupuestador online</a>. Si atiendes muchas consultas repetidas, un <a href="/servicios/whatsapp-ia/asistente-de-ia-para-whatsapp">asistente en WhatsApp</a> puede dar la primera respuesta.</p>""",
 "faq": [
  ("¿Qué programa usa una agencia de viajes pequeña que hace viajes a medida?", "Muchas trabajan con correo y hojas de cálculo, y funciona con pocos viajes al mes. Cuando el volumen crece, lo útil es una herramienta que monte el presupuesto con plantillas y reutilice los datos del viajero en todos los documentos."),
  ("¿Qué pasa si un proveedor de reservas no permite conectarse con mi programa?", "Se busca la alternativa menos mala: importar sus ficheros, leer sus correos de confirmación o mantener ese proveedor fuera de la conexión. Conviene comprobarlo antes de encargar nada, porque condiciona todo el proyecto."),
 ],
}

# Estructura: quién responde cuando falla + tabla «tu situación / suele encajar» + preguntas que nadie hace + decisión programa a programa
D["guias/software-libre-y-software-propietario"] = {
 "estructura": "quien-responde-cuando-falla + tabla-situacion-y-encaje + preguntas-que-nadie-hace + decidir-programa-a-programa",
 "lead": "Te han dicho que con software libre te ahorras las licencias, y también que si algo falla no hay a quién llamar. Las dos cosas pueden ser ciertas. Para decidir entre software libre y software propietario en tu empresa, la pregunta útil no es cuál gana, sino quién responde cuando deja de funcionar.",
 "bloque": """<h2>¿A quién llamo si falla? La pregunta que decide entre libre y propietario</h2>
<p>Lo que distingue de verdad a un programa de otro, para una empresa, es quién se hace responsable de que siga funcionando. Con uno propietario, pagas a un fabricante para que lo haga. Con uno libre, eliges tú: una persona de tu equipo, una empresa de soporte o nadie. La tercera opción es la que acaba mal.</p>
<h3>Sitúa tu caso</h3>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Tu situación</th><th>Suele encajar</th><th>Motivo</th></tr></thead><tbody>
<tr><td>Sin nadie técnico y con poco tiempo</td><td>Propietario con soporte, o libre con contrato de mantenimiento</td><td>Necesitas un teléfono al que llamar</td></tr>
<tr><td>Hay alguien que sabe y le gusta</td><td>Libre</td><td>Aprovechas la libertad de adaptarlo</td></tr>
<tr><td>Dependes de un formato que te exige un cliente o la administración</td><td>El que ese formato pida</td><td>La compatibilidad manda</td></tr>
<tr><td>Te preocupa quedar atado a un fabricante</td><td>Libre, o propietario con salida de datos clara</td><td>Lo que importa es poder irte</td></tr>
<tr><td>Datos delicados que no quieres fuera</td><td>Cualquiera que puedas alojar donde tú decidas</td><td>Mira dónde se guardan, no la licencia</td></tr>
</tbody></table></div>
<h3>Cosas que casi nadie pregunta y luego pesan</h3>
<ul>
<li>¿Puedo sacar todos mis datos en un formato que abra otro programa?</li>
<li>Si dejo de pagar, ¿pierdo el acceso o solo las actualizaciones?</li>
<li>¿Quién corrige un fallo de seguridad, y en cuánto tiempo?</li>
<li>¿Sigue vivo el proyecto? Mira cuándo se publicó la última versión.</li>
<li>¿Hay más de un proveedor capaz de darme soporte?</li>
</ul>
<p>Estas preguntas valen igual para los dos mundos. Un programa libre abandonado te ata tanto como uno cerrado cuyo fabricante cambia las condiciones.</p>
<h3>Una decisión por programa, no por empresa</h3>
<p>No tienes que elegir bando. Lo habitual es mezclar: herramientas libres donde el riesgo es bajo y el ahorro claro, y herramientas de pago donde un parón te cuesta ventas. Empieza por la lista de lo que usas, ordénala por lo que te dolería que fallara y decide una a una.</p>
<p>Si la duda es con el programa de gestión, tienes el caso concreto en <a href="/guias/erp-gratis-y-open-source">ERP gratis y open source</a>; si es con programas por suscripción, en <a href="/guias/que-es-saas-software-como-servicio">qué es el SaaS</a>. Y si heredaste un programa que ya nadie mantiene, existe el <a href="/servicios/migraciones-e-integraciones/rescate-de-software-antiguo">rescate de software antiguo</a>.</p>""",
 "faq": [
  ("¿Quién da soporte técnico al software libre en una empresa?", "Quien tú decidas: una persona de tu equipo, una empresa especializada en ese programa o la propia comunidad a través de foros. Para algo de lo que depende tu facturación, conviene tener un contrato de soporte y no fiarlo todo a los foros."),
  ("¿Cómo saber si un programa me deja atado al proveedor?", "Comprueba si puedes exportar todos tus datos en un formato abierto, qué ocurre con el acceso si dejas de pagar y si existe más de una empresa capaz de mantenerlo. Si las tres respuestas son malas, estás atado, sea libre o propietario."),
 ],
}

# Estructura: tabla «motivo / ¿justifica el cambio?» + lo que le importa a cada persona del local + el día del cambio
D["guias/software-tpv-para-hosteleria"] = {
 "estructura": "tabla-motivos-para-cambiar + lo-que-importa-a-cada-persona-del-local + el-dia-del-cambio",
 "lead": "Hora punta, la terraza llena, y el camarero vuelve a la barra porque la comanda no ha salido en cocina. Dos mesas esperan la cuenta y la pantalla se ha quedado pensando. Si vas a cambiar de software TPV para hostelería, que la elección no la decida el vendedor, sino un servicio como ese.",
 "bloque": """<h2>¿Cambio de TPV o aguanto con el que tengo?</h2>
<p>Cambia cuando el programa de caja te hace perder ventas o tiempo cada día, no porque sea viejo. Un TPV antiguo que el equipo domina puede rendir más que uno nuevo que nadie entiende en pleno servicio. Estas son las razones de peso, y las que no lo son.</p>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Motivo</th><th>¿Justifica el cambio?</th></tr></thead><tbody>
<tr><td>Se cuelga o va lento con el local lleno</td><td>Sí: cada minuto parado son mesas sin cobrar</td></tr>
<tr><td>No se adapta a las obligaciones de facturación que explica esta guía</td><td>Sí, pero pregunta antes al fabricante si lo va a actualizar</td></tr>
<tr><td>No saca las ventas por plato ni por hora</td><td>Sí, si quieres decidir con datos</td></tr>
<tr><td>Depende de un técnico que ya no contesta</td><td>Sí: es un riesgo aunque hoy funcione</td></tr>
<tr><td>«Es feo» o «el de al lado tiene otro»</td><td>No</td></tr>
<tr><td>Te ofrecen uno gratis</td><td>No por sí solo: mira qué entregas a cambio</td></tr>
</tbody></table></div>
<h3>Lo que le importa a cada persona del local</h3>
<ul>
<li><strong>A quien sirve mesas:</strong> que marcar una comanda sean pocos toques y que se pueda corregir sin llamar al encargado.</li>
<li><strong>A cocina:</strong> que el pedido llegue claro, con las notas («sin cebolla», «poco hecho») bien visibles.</li>
<li><strong>A quien cierra:</strong> que el arqueo cuadre sin calculadora.</li>
<li><strong>A ti:</strong> saber qué se vendió, a qué hora y con qué margen.</li>
<li><strong>A tu asesoría:</strong> recibir los datos sin que nadie los pase a mano.</li>
</ul>
<p>Si eliges pensando solo en tus informes, el equipo lo sufrirá; si eliges solo por la rapidez en sala, te quedarás sin información.</p>
<h3>El día del cambio</h3>
<ol>
<li>Elige una semana tranquila, nunca vísperas de fiesta.</li>
<li>Carga la carta y los precios con antelación y revísalos con alguien de sala.</li>
<li>Haz un servicio de prueba con el equipo, con comandas inventadas.</li>
<li>Mantén el sistema anterior disponible los primeros días.</li>
<li>Al cerrar la primera semana, pregunta a cada persona qué le sobra y qué echa de menos.</li>
</ol>
<p>Si además de la caja quieres unir reservas, compras y personal, eso lo tratamos en <a href="/guias/software-a-medida-para-hosteleria">software a medida para hostelería</a>. El módulo de caja está en <a href="/servicios/software-de-gestion/tpv">TPV conectado a tu gestión</a> y la carta, en <a href="/servicios/presencia-digital/menus-digitales-para-hosteleria">menús digitales para hostelería</a>.</p>""",
 "faq": [
  ("¿Cuándo merece la pena cambiar el TPV de un bar?", "Cuando se cuelga en hora punta, no se va a adaptar a las obligaciones de facturación, no te da las ventas por producto o depende de alguien que ya no lo mantiene. Que sea antiguo o poco vistoso no es motivo suficiente."),
  ("¿Cómo cambiar de TPV en un restaurante sin que el servicio se resienta?", "Preparando la carta y los precios con antelación, haciendo un servicio de prueba con el equipo y eligiendo una semana tranquila. Conviene mantener el sistema anterior a mano los primeros días por si hay que consultar algo."),
 ],
}

# Estructura: para qué sirve la clasificación + glosario en llano + confusiones que salen caras + tres preguntas + nota para estudiantes
D["guias/tipos-de-software"] = {
 "estructura": "glosario-en-llano + confusiones-que-salen-caras + tres-preguntas-por-programa + nota-para-estudiantes",
 "lead": "Buscas los tipos de software porque te lo piden en clase, o porque en tu empresa alguien ha dicho «necesitamos un software» y nadie sabe de qué clase. En los dos casos la clasificación sirve de poco si no la conectas con algo real. Aquí va traducida a decisiones de un negocio.",
 "bloque": """<h2>¿De qué me sirve conocer los tipos de software si solo quiero que mi empresa funcione?</h2>
<p>Te sirve para saber qué estás comprando, a quién reclamar cuando falla y qué puedes cambiar sin tocar lo demás. La teoría distingue familias; en el día a día lo útil es saber qué papel juega cada programa en tu negocio.</p>
<h3>La clasificación, dicha en llano</h3>
<dl>
<dt>Software de sistema</dt><dd>Lo que hace que el ordenador, el móvil o la caja arranquen. Casi nunca lo eliges: viene con el aparato. Lo que sí te toca es mantenerlo actualizado.</dd>
<dt>Software de aplicación</dt><dd>Con lo que trabajas: el correo, la hoja de cálculo, el programa de facturas, la agenda. Aquí están casi todas tus decisiones y casi todo tu gasto.</dd>
<dt>Software de programación</dt><dd>Las herramientas de quien fabrica programas. Solo te afecta si encargas algo propio: conviene saber con qué se hizo, por si mañana lo mantiene otro.</dd>
</dl>
<h3>Cuatro confusiones que salen caras</h3>
<ul>
<li>Creer que «la nube» es un tipo de programa. Es dónde funciona, no qué hace.</li>
<li>Pensar que una aplicación del móvil y un programa de ordenador son cosas distintas: muchas veces son dos puertas al mismo sistema.</li>
<li>Comprar un programa nuevo para algo que el que ya tienes hace, pero nadie ha configurado.</li>
<li>Culpar al programa de gestión cuando lo que falla es el sistema operativo sin actualizar, o al revés.</li>
</ul>
<h3>Tres preguntas ante cualquier programa de tu negocio</h3>
<ol>
<li>¿Qué trabajo hace exactamente y quién lo usa?</li>
<li>¿Dónde están los datos y quién puede sacarlos?</li>
<li>¿Quién lo actualiza y qué pasa si deja de hacerlo?</li>
</ol>
<p>Si no sabes responder a alguna, ya tienes tarea antes de comprar nada más.</p>
<h3>Si estás estudiando</h3>
<p>Quédate con la idea de capas: el sistema sostiene a las aplicaciones, y las herramientas de programación sirven para crear ambos. Los ejemplos de más abajo te valen para un trabajo o un examen.</p>
<p>Para seguir, <a href="/guias/que-es-un-software">qué es un software</a> explica el concepto desde cero y la <a href="/guias/diferencia-entre-hardware-y-software">diferencia entre hardware y software</a>, la otra mitad. Si lo que buscas es ordenar tu empresa, ve directo a <a href="/guias/que-es-un-software-de-gestion">qué es un software de gestión</a>.</p>""",
 "faq": [
  ("¿Qué tipo de software necesita una pequeña empresa?", "Sobre todo software de aplicación: correo, ofimática, un programa para facturar y llevar clientes y, según el sector, uno específico de su actividad. El software de sistema ya viene con los equipos; lo importante es tenerlo actualizado."),
  ("¿La nube es un tipo de software?", "No. La nube describe dónde funciona un programa: en servidores a los que accedes por internet en lugar de en tu ordenador. Un mismo tipo de programa, por ejemplo de facturación, puede existir instalado o en la nube."),
 ],
}
