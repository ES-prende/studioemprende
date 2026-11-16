# Reescritura «dolores primero» · familia Migraciones e integraciones (noviembre 2026).
# Sin precios (se habla de ERP, CRM y programas de gestión). Cada página con su propio recorrido.
D = {}

# Estructura: viaje de un pedido tecleado varias veces (ol) + cuenta con tus números + por dónde empezar sin conectarlo todo
D["servicios/migraciones-e-integraciones/conectar-erp-tienda-crm-y-contabilidad"] = {
 "estructura": "viaje-de-un-pedido-tecleado-cuatro-veces + cuenta-con-tus-numeros + empezar-por-una-sola-conexion",
 "lead": "Entra un pedido por la web y alguien lo copia en el programa de gestión, otro actualiza el stock a mano, administración rehace la factura y a final de mes se le manda todo al gestor en un correo. Conectar el ERP con la tienda online, el CRM y la contabilidad acaba con ese teclear lo mismo cuatro veces.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">El mismo dato, escrito una y otra vez</p><h2>Tenemos tres programas y pasamos los datos a mano: ¿es normal?</h2></div>
<p style="max-width:820px">Es lo más corriente, y tiene una explicación sencilla: cada programa se compró en un momento distinto para resolver una cosa. Primero la facturación, luego la tienda, después algo para llevar a los clientes. Ninguno se eligió pensando en los otros, y el pegamento entre ellos acabó siendo una persona. Sigue un pedido cualquiera y cuenta las veces que se escribe.</p>
<ol style="max-width:820px">
<li><strong>En la tienda online.</strong> Lo teclea el cliente: nombre, dirección, productos.</li>
<li><strong>En el programa de gestión.</strong> Alguien lo copia para preparar el albarán. Si el cliente es nuevo, lo da de alta otra vez.</li>
<li><strong>En el almacén.</strong> Se descuenta el stock; la web sigue mostrando la cantidad antigua hasta que alguien la corrige.</li>
<li><strong>En el CRM o en la hoja de comerciales.</strong> Se apunta la venta para saber qué compra cada cliente.</li>
<li><strong>En la contabilidad.</strong> La factura viaja en PDF a la asesoría, que vuelve a introducirla.</li>
</ol>
<p style="max-width:820px">Cada copia es una ocasión para una errata, y las erratas no se quedan dentro: se convierten en un producto vendido que no estaba, un envío a una dirección vieja o una factura que no cuadra con el cobro.</p>
<h3 style="margin-top:30px">Haz la cuenta con tus propios números</h3>
<ul class="lista" style="max-width:820px">
<li>Pedidos o facturas a la semana, multiplicados por los minutos que cuesta copiar cada uno.</li>
<li>Veces al mes que hay que llamar a un cliente porque lo vendido no estaba en el almacén.</li>
<li>Horas de cierre mensual dedicadas a casar lo que dice un programa con lo que dice otro.</li>
</ul>
<p style="max-width:820px;margin-top:18px">Si la suma es pequeña, quizá no te compense conectar nada todavía, y lo decimos sin problema: con pocos pedidos, copiar a mano sale más barato que una integración.</p>
<h3 style="margin-top:30px">No hace falta conectarlo todo a la vez</h3>
<p style="max-width:820px">Lo sensato es empezar por la unión que más duele, que casi siempre es tienda y stock o facturas y asesoría, dejarla funcionando un mes y decidir después la siguiente. Antes de presupuestar comprobamos qué permite cada programa, porque no todos se dejan conectar igual.</p>
<p style="max-width:820px">La parte técnica de cómo hablan dos programas la explicamos en <a href="/servicios/migraciones-e-integraciones/integraciones-por-api">integraciones por API</a>. Si al revisar resulta que tienes demasiadas herramientas para lo mismo, puede ser mejor <a href="/servicios/migraciones-e-integraciones/unificar-varios-programas-en-uno">unificar varios programas en uno</a>. Y si dudas sobre qué hace cada tipo de programa, la guía <a href="/guias/erp-vs-crm">ERP frente a CRM</a> lo aclara.</p>
</div></section>""",
 "faq": [
  ("¿Cómo evitar pasar los pedidos de la tienda online al programa de gestión a mano?", "Conectando ambos para que cada pedido entre solo en el programa con su cliente, sus productos y su forma de pago. Se hace por API o mediante intercambio automático de archivos, según lo que permita cada herramienta."),
  ("¿Cuándo compensa conectar los programas de la empresa?", "Cuando el tiempo de copiar datos y corregir descuadres supera con claridad el coste de la conexión, o cuando los errores ya afectan a clientes: stock que no era real, facturas duplicadas o envíos equivocados."),
  ("¿Qué pasa si uno de mis programas no se puede conectar?", "Se buscan vías alternativas, como exportaciones programadas o lectura de archivos. Si tampoco es posible, se valora sustituir ese programa o dejarlo fuera de la conexión y automatizar el resto."),
 ],
}

# Estructura: escena de buscar un papel en el trastero + tabla «qué cajas sí y cuáles no» + qué preguntar a tu gestor antes de tirar nada
D["servicios/migraciones-e-integraciones/digitalizacion-de-archivo-en-papel"] = {
 "estructura": "escena-de-buscar-en-el-trastero + tabla-que-cajas-si-y-cuales-no + preguntas-para-tu-gestor",
 "lead": "Un cliente reclama y necesitas el contrato que firmó hace seis años. Sabes que está en el trastero, en alguna de las cuarenta cajas, y la persona que las ordenó ya se jubiló. La digitalización de archivo en papel para empresas sirve para que encontrarlo cueste diez segundos y no una mañana.",
 "bloque": """<section class="sec sec-suave"><div class="w">
<div class="cab"><p class="kicker">Lo tienes, pero no lo encuentras</p><h2>¿Merece la pena escanear todo el archivo en papel de la empresa?</h2></div>
<p style="max-width:820px">Todo, casi nunca. Una parte, casi siempre. El papel guardado tiene un coste que no aparece en ninguna factura: el del metro cuadrado que ocupa, el de la mañana que alguien pierde buscando y, sobre todo, el de no encontrar a tiempo el documento que te daba la razón.</p>
<p style="max-width:820px">También hay un riesgo más discreto. Si el archivo solo existe en un sitio, una humedad o una mudanza mal hecha se lo llevan sin posibilidad de copia. Y si solo lo entiende una persona, su orden se va con ella.</p>
<h3 style="margin-top:30px">Qué cajas sí y qué cajas no</h3>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Tipo de papel</th><th>Cada cuánto se consulta</th><th>Qué solemos recomendar</th></tr></thead><tbody>
<tr><td>Expedientes y contratos de clientes activos</td><td>A menudo</td><td>Digitalizar con sus datos y enlazarlos a la ficha del cliente</td></tr>
<tr><td>Garantías, certificados, planos, escrituras</td><td>Poco, pero cuando hace falta es urgente</td><td>Digitalizar y, además, conservar el original</td></tr>
<tr><td>Albaranes y facturas de años recientes</td><td>En reclamaciones e inspecciones</td><td>Escanear por lotes con fecha, proveedor e importe</td></tr>
<tr><td>Documentación de ejercicios muy antiguos</td><td>Casi nunca</td><td>Dejar en caja bien rotulada o valorar su destrucción con tu asesor</td></tr>
<tr><td>Copias, borradores y publicidad</td><td>Nunca</td><td>No gastar un minuto en escanearlo</td></tr>
</tbody></table></div>
<p style="max-width:820px;margin-top:20px">Hacer esta criba antes de empezar es lo que más abarata un proyecto: lo habitual es que una buena parte de las cajas no merezca pasar por el escáner.</p>
<h3 style="margin-top:30px">Antes de tirar un solo papel, pregunta a tu gestor</h3>
<ul class="lista" style="max-width:820px">
<li>¿Qué documentos debo conservar en original y durante cuánto tiempo?</li>
<li>¿Cuáles puedo guardar solo en digital?</li>
<li>¿Hay algo de este archivo que debería haberse destruido ya por contener datos personales?</li>
</ul>
<p style="max-width:820px;margin-top:18px">Nosotros no somos asesoría y no decidimos qué se puede eliminar: digitalizamos, ordenamos y dejamos el papel como estaba hasta que tú, con ese consejo, resuelvas qué hacer con él.</p>
<p style="max-width:820px">Si lo que te preocupa no es el archivo antiguo sino el papel que entra cada día, lo que buscas es la <a href="/servicios/automatizacion-y-datos/lectura-automatica-de-documentos-hacia-tu-programa">lectura automática de documentos</a>. Para que el equipo pregunte al archivo en lenguaje normal, mira el <a href="/servicios/agentes-de-ia/asistente-interno-de-procedimientos">asistente interno de procedimientos</a>. Y si el orden del archivo está en la cabeza de alguien que se va, el <a href="/servicios/relevo-y-continuidad/manual-de-operaciones-con-video-e-ia">manual de operaciones</a> ayuda a que no se pierda.</p>
</div></section>""",
 "faq": [
  ("¿Cómo organizar el archivo de una empresa para encontrar los documentos rápido?", "Con un criterio único de carpetas y nombres, y con los datos clave de cada documento (cliente, fecha, tipo, número) guardados como campos por los que se puede buscar. Si además el texto es legible por el buscador, se encuentra por cualquier palabra."),
  ("¿Qué pasa si se pierde o se moja el archivo en papel de la empresa?", "Lo que no tenga copia se pierde, y con ello la posibilidad de acreditar contratos, entregas o garantías. Digitalizar lo importante y guardarlo con copia de seguridad reduce ese riesgo, aunque algunos originales convenga conservarlos igualmente."),
 ],
}

# Estructura: frases del día a día + rejilla de cuatro alternativas comparadas + cuándo no hace falta + respuesta destacada
D["servicios/migraciones-e-integraciones/integraciones-por-api"] = {
 "estructura": "frases-del-dia-a-dia + rejilla-cuatro-alternativas + cuando-no-hace-falta-integrar",
 "lead": "Cada viernes alguien descarga un Excel de un programa, le cambia tres columnas y lo sube a otro. Si esa persona falta, no se hace. Si se equivoca de fila, nadie lo nota hasta que un cliente protesta. Una integración por API entre los programas de tu empresa hace ese traspaso sola y deja rastro de cada dato.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Exportar, retocar, importar</p><h2>¿Cómo hago que dos programas se pasen los datos sin copiarlos yo?</h2></div>
<ul class="lista" style="font-size:18px;max-width:820px">
<li>«El proveedor me dice que su programa "tiene API", pero no sé qué hago con eso.»</li>
<li>«Tenemos un Excel puente que solo sabe usar una persona.»</li>
<li>«Damos de alta al cliente en un sitio y se nos olvida en el otro.»</li>
<li>«Montamos un automatismo con una herramienta de internet y un día dejó de funcionar sin avisar.»</li>
</ul>
<p style="max-width:820px;margin-top:18px">Que un programa «tenga API» significa que el fabricante ha dejado una entrada preparada para que otros sistemas lean y escriban datos con permiso. Es una condición necesaria, no una solución: alguien tiene que decidir qué dato viaja, hacia dónde y qué ocurre cuando llega mal.</p>
<h3 style="margin-top:30px">Cuatro maneras de resolverlo, de menos a más</h3>
<div class="rejilla">
<div class="tarjeta"><h3>Seguir copiando</h3><p>Válido con poco volumen. Depende de una persona y no deja rastro de los errores.</p></div>
<div class="tarjeta"><h3>Exportar e importar ficheros</h3><p>Rápido de montar. Los datos van con retraso y cualquier cambio de formato lo rompe.</p></div>
<div class="tarjeta"><h3>Conector ya hecho</h3><p>Sirve cuando el caso es estándar. Se queda corto si tu proceso tiene excepciones.</p></div>
<div class="tarjeta"><h3>Integración a medida por API</h3><p>Se ajusta a tu forma de trabajar y avisa de los fallos. Requiere más análisis al principio.</p></div>
</div>
<h3 style="margin-top:30px">Cuándo no te hace falta una integración</h3>
<p style="max-width:820px">Si el traspaso ocurre una vez al mes y lleva diez minutos, automatizarlo es matar moscas a cañonazos. Tampoco conviene integrar dos programas cuando uno de ellos vas a cambiarlo pronto: primero se decide con qué te quedas. Y si el dato de origen ya está mal, una conexión solo conseguirá que el error llegue antes a más sitios; en ese caso se limpia primero.</p>
<div class="respuesta" style="max-width:820px;margin-top:20px"><p><strong>Qué preguntar a tu proveedor esta semana:</strong> si su programa tiene API, si está documentada, si tu plan la incluye y si permite escribir datos o solo leerlos. Con esas cuatro respuestas sabemos qué es posible. Si lo que quieres unir es todo el circuito de venta, mira <a href="/servicios/migraciones-e-integraciones/conectar-erp-tienda-crm-y-contabilidad">conectar ERP, tienda, CRM y contabilidad</a>. Si prefieres un programa que ya venga preparado para conectarse, están las <a href="/servicios/software-de-gestion/integraciones-por-api">integraciones del programa de gestión</a>. Y si el otro extremo es un programa viejo sin puerta de entrada, el <a href="/servicios/migraciones-e-integraciones/rescate-de-software-antiguo">rescate de software antiguo</a>.</p></div>
</div></section>""",
 "faq": [
  ("¿Cómo saber si mi programa tiene API?", "Busca en su web o en su ayuda un apartado de API, desarrolladores o integraciones, o pregúntalo al soporte. Conviene confirmar también si está incluida en tu plan y si permite escribir datos además de leerlos."),
  ("¿Qué pasa si una integración falla y no me entero?", "Si no hay vigilancia, los datos dejan de pasar en silencio y el descuadre aparece días después. Una integración bien hecha registra cada envío, reintenta los que fallan y avisa a una persona cuando algo no se ha podido entregar."),
 ],
}

# Estructura: miedos del dueño con su respuesta (dl) + las dos primeras semanas paso a paso + cuándo quedarte en Excel
D["servicios/migraciones-e-integraciones/migracion-de-excel-a-programa-de-gestion"] = {
 "estructura": "miedos-y-respuestas-en-glosario + dos-primeras-semanas + cuando-quedarte-en-excel",
 "lead": "La hoja de clientes tiene doce pestañas, colores que solo entiende quien la hizo y una fórmula que nadie se atreve a tocar. Funciona, hasta que esa persona se va de vacaciones o alguien guarda encima. Pasar de Excel a un programa de gestión sin perder datos asusta más por lo que puede romperse que por el programa.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">«Mejor no tocar, que así funciona»</p><h2>¿Qué puede salir mal al dejar Excel y cómo se evita?</h2></div>
<p style="max-width:820px">Sale mal cuando se hace de golpe y sin mirar dentro de las hojas. Quien lleva años con sus libros de cálculo tiene miedos concretos, y casi todos son sensatos. Estos son los que más oímos y lo que se hace con cada uno.</p>
<dl style="max-width:820px">
<dt><strong>«¿Y si se pierde algún cliente o alguna factura por el camino?»</strong></dt><dd>Se cuentan los registros antes y después, y se comparan totales por año. Lo que no cuadra se revisa fila a fila antes de dar nada por terminado.</dd>
<dt><strong>«Mi hoja hace cosas que ningún programa va a hacer.»</strong></dt><dd>A veces es verdad. Se revisa cada fórmula y cada truco: unos tienen equivalente, otros se configuran y alguno conviene dejarlo en Excel, conectado.</dd>
<dt><strong>«No podemos parar ni un día.»</strong></dt><dd>No se para. Se trabaja en paralelo un tiempo corto y el cambio se hace en una fecha tranquila, no en cierre de trimestre.</dd>
<dt><strong>«La persona que lleva el Excel se va a sentir desplazada.»</strong></dt><dd>Es quien mejor conoce los datos. Se la implica desde el primer día para revisar la carga; suele ser quien más gana.</dd>
<dt><strong>«¿Y si luego el programa no nos gusta?»</strong></dt><dd>Tus hojas originales se conservan intactas y el programa debe permitir exportar. Pregúntalo antes de firmar con cualquier proveedor.</dd>
</dl>
<h3 style="margin-top:30px">Qué ocurre en las dos primeras semanas</h3>
<ol style="max-width:820px">
<li><strong>Días 1 a 3.</strong> Nos enseñas las hojas tal como las usas, con sus rarezas. No las ordenes antes.</li>
<li><strong>Días 4 a 7.</strong> Te devolvemos una lista de lo encontrado: duplicados, huecos, formatos distintos y dudas que solo tú puedes resolver.</li>
<li><strong>Segunda semana.</strong> Primera carga de prueba con datos reales, para que busques a tres clientes que conozcas bien y compruebes que está todo.</li>
</ol>
<h3 style="margin-top:30px">Cuándo es razonable quedarte en Excel</h3>
<p style="max-width:820px">Si la hoja la usa una sola persona, tiene pocos cientos de filas y no se cruza con facturación ni con stock, cambiarla es complicarse. El salto compensa cuando varias personas editan a la vez, cuando hay versiones distintas del mismo archivo o cuando un error en una celda ya te ha costado dinero. Si lo que vas a implantar es un sistema completo, este mismo proceso está contado desde ese lado en la <a href="/servicios/erp-para-pymes/migracion-desde-excel-u-otro-programa">migración desde Excel dentro del ERP</a>. Para entender qué tipo de herramienta necesitas, lee <a href="/guias/que-es-un-software-de-gestion">qué es un software de gestión</a>; y si el equipo necesita soltura con el programa nuevo, hay <a href="/servicios/formacion-ia/formacion-de-empleados-en-un-programa-nuevo">formación de empleados en un programa nuevo</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo pasar mis clientes de Excel a un programa de gestión?", "Se revisa la hoja, se unifican formatos de nombre, teléfono y NIF, se eliminan duplicados y se importa al programa relacionando cada cliente con sus facturas o pedidos. Antes de darlo por bueno se comprueba una muestra a mano."),
  ("¿Cuánto tarda en estar funcionando el programa después de dejar Excel?", "Depende del número de hojas y de lo limpias que estén. Lo habitual es hacer primero una carga de prueba y convivir un periodo corto con ambos sistemas; el plazo concreto se fija por escrito tras revisar tus archivos."),
  ("¿Qué pasa con las fórmulas y macros de mis hojas de cálculo?", "Se analizan una a una. Las que calculan precios, márgenes o comisiones suelen convertirse en reglas del programa; las que son informes se sustituyen por listados, y las muy particulares pueden mantenerse en una hoja conectada a los datos."),
 ],
}

# Estructura: cita del dueño + tabla por etapas del deterioro (qué notas / qué se puede hacer aún) + segunda sección: lo que conviene hacer hoy aunque no decidas nada
D["servicios/migraciones-e-integraciones/rescate-de-software-antiguo"] = {
 "estructura": "cita-del-dueno + tabla-por-etapas-del-deterioro + que-hacer-hoy-sin-decidir-nada",
 "lead": "Hay un ordenador en la oficina que nadie puede apagar, actualizar ni cambiar de sitio porque dentro vive el programa de siempre, con veinte años de clientes y artículos. El rescate de software antiguo y programas obsoletos saca esos datos mientras el equipo todavía enciende, que es cuando resulta más sencillo.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">El ordenador que nadie se atreve a tocar</p><h2>¿Cuánto tiempo más puedo esperar con mi programa antiguo?</h2></div>
<blockquote style="max-width:820px"><p>«Mientras arranque, lo dejamos. El día que no arranque, ya veremos.»</p></blockquote>
<p style="max-width:820px;margin-top:18px">Es la decisión más frecuente y también la más cara, porque ese «ya veremos» llega sin fecha y con la empresa parada. Un programa obsoleto no avisa con un mensaje: va perdiendo capacidades poco a poco. Saber en qué etapa estás indica cuánto margen queda y qué se puede salvar.</p>
<div class="tabla-wrap" style="margin-top:22px"><table class="tabla-norm"><thead><tr><th>Etapa</th><th>Lo que notas</th><th>Lo que todavía se puede hacer</th></tr></thead><tbody>
<tr><td>1. Funciona, sin soporte</td><td>Nadie contesta si hay una duda; no hay versiones nuevas</td><td>Rescate ordenado, con el programa en marcha y sin prisa</td></tr>
<tr><td>2. Empieza a aislarse</td><td>No imprime en la impresora nueva, no exporta, no envía correos</td><td>Rescate completo; conviene no retrasarlo</td></tr>
<tr><td>3. Atado a una máquina</td><td>Solo funciona en un equipo viejo que no se puede sustituir</td><td>Copia íntegra del equipo y extracción de datos</td></tr>
<tr><td>4. Ya no arranca</td><td>Pantalla negra o error al abrir</td><td>Recuperación desde el disco o desde copias, con resultado incierto</td></tr>
</tbody></table></div>
</div></section>
<section class="sec sec-suave"><div class="w">
<h3>Lo que conviene hacer hoy, aunque no decidas nada</h3>
<ul class="lista" style="max-width:820px">
<li>Averiguar en qué carpeta guarda el programa sus datos y copiarla a otro sitio.</li>
<li>Apuntar el sistema operativo, la versión del programa y cualquier clave o licencia que pida al abrir.</li>
<li>Sacar en papel o en PDF los listados que más usas: clientes, artículos con precio, saldos pendientes.</li>
<li>No instalar nada nuevo en ese ordenador ni conectarlo a internet si no es imprescindible.</li>
</ul>
<p style="max-width:820px;margin-top:18px">Con eso ya has reducido la mayor parte del riesgo sin gastar nada. No todo se recupera siempre: si el formato es muy cerrado o el disco está dañado, puede que solo se salve una parte, y te lo diremos después de mirar, no antes. Si prefieres que el programa siga vivo un tiempo en lugar de sustituirlo ya, eso es <a href="/servicios/departamento-tecnologico/mantenemos-programas-abandonados-por-su-proveedor">mantener un programa abandonado por su proveedor</a>. Cuando lo antiguo es una colección de hojas de cálculo y no un programa, mira la <a href="/servicios/migraciones-e-integraciones/migracion-de-excel-a-programa-de-gestion">migración de Excel a un programa de gestión</a>. Para elegir destino, la guía de <a href="/guias/tipos-de-software">tipos de software</a> orienta.</p>
</div></section>""",
 "faq": [
  ("¿Cómo sacar los datos de un programa muy antiguo?", "Primero se hace una copia completa del equipo. Después se localizan los archivos donde el programa guarda la información y se leen con herramientas adecuadas a su formato, aunque el propio programa no tenga opción de exportar."),
  ("¿Qué pasa si se rompe el ordenador donde está instalado el programa antiguo?", "Si existe una copia del disco o de la carpeta de datos, se puede restaurar en otro equipo o extraer la información. Sin copia, la recuperación depende del estado del disco y no siempre es completa."),
 ],
}
