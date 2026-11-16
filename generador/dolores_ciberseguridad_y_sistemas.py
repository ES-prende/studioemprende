# Reescritura «dolores primero» · familia Ciberseguridad y sistemas (noviembre 2026).
# Sin cifras de miedo ni obligaciones legales nuevas: solo lo que cada página ya afirma.
D = {}

# Estructura: escena del correo de compras con el cuestionario + tabla «te preguntan / quiere decir / respuesta honesta» + el error de marcar sí a todo
D["servicios/ciberseguridad-y-sistemas/adaptacion-a-nis2-para-proveedores"] = {
 "estructura": "escena-del-cuestionario-de-compras + tabla-pregunta-traducida-y-respuesta-honesta + error-de-marcar-si-a-todo",
 "lead": "Tu mejor cliente te envía un Excel con ochenta preguntas sobre ciberseguridad y un plazo de dos semanas. Si no lo devuelves, o lo devuelves mal, puedes dejar de ser proveedor homologado. La adaptación a NIS2 para proveedores te ayuda a contestar con verdad y a tener detrás lo que afirmas.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">El cuestionario que llega sin avisar</p><h2>Me piden cumplir requisitos de seguridad para seguir siendo proveedor: ¿por dónde empiezo?</h2></div>
<p style="max-width:820px">Empieza por leerlo entero antes de contestar nada. Lo envía el departamento de compras de una empresa grande, no un técnico, y se lo mandan igual a una ingeniería de cuatrocientas personas que a un taller de quince. Muchas preguntas no van contigo, otras usan palabras que no has oído nunca y unas pocas describen cosas que ya haces sin llamarlas así.</p>
<p style="max-width:820px">Quien lo recibe suele ser el gerente o la persona de administración, que no tiene a quién reenviarlo. El primer impulso es pasárselo al informático de confianza y que «ponga lo que haya que poner». Es comprensible, y es el origen de casi todos los problemas posteriores.</p>
<div class="tabla-wrap" style="margin-top:22px"><table class="tabla-norm"><thead><tr><th>Lo que pregunta</th><th>Lo que quiere saber en realidad</th><th>Una respuesta honesta posible</th></tr></thead><tbody>
<tr><td>«¿Dispone de una política de control de accesos?»</td><td>Si cada persona entra solo a lo que necesita y se le retira al marcharse</td><td>Sí, con un documento breve y la lista de usuarios revisada</td></tr>
<tr><td>«¿Realiza copias de seguridad verificadas?»</td><td>Si podrías seguir sirviéndole tras un incidente</td><td>Sí, con la fecha de la última restauración probada</td></tr>
<tr><td>«¿Tiene un procedimiento de gestión de incidentes?»</td><td>Si le avisarás, y a quién, cuando algo te pase</td><td>En implantación, con fecha prevista y un contacto designado</td></tr>
<tr><td>«¿Forma a su personal en seguridad?»</td><td>Si tu equipo distingue un correo fraudulento</td><td>Parcialmente: sesión anual, con registro de asistencia</td></tr>
</tbody></table></div>
<h3 style="margin-top:30px">El error que más caro sale: marcar «sí» a todo</h3>
<p style="max-width:820px">Un cuestionario firmado es una declaración ante tu cliente. Si afirmas que tienes algo y un día te piden la evidencia, o hay un incidente y resulta que no existía, el daño para la relación es mayor que haber contestado «todavía no». Una respuesta del tipo «no lo tenemos, lo tendremos en tal fecha» suele aceptarse mejor de lo que se cree, porque compras necesita ver que el riesgo está identificado y en manos de alguien.</p>
<h3 style="margin-top:30px">Ni sello ni certificado: los límites de este trabajo</h3>
<p style="max-width:820px">No es una certificación ni un sello, y no convierte a tu empresa en entidad obligada por la directiva. Tampoco es asesoramiento jurídico: si tu contrato incluye cláusulas de responsabilidad, léelas con tu abogado. Es trabajo técnico y documental para que lo que contestes sea cierto. Dos de las medidas que más se repiten las tienes explicadas en <a href="/servicios/ciberseguridad-y-sistemas/copias-de-seguridad-y-plan-de-continuidad">copias de seguridad y plan de continuidad</a> y en la <a href="/servicios/departamento-tecnologico/auditoria-de-accesos-y-licencias">auditoría de accesos y licencias</a>. El contexto de la norma está en nuestra página de <a href="/normativas">normativas</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo responder a un cuestionario de ciberseguridad de un cliente si soy una pyme?", "Leyéndolo entero, separando lo que ya cumples, lo que cumples a medias y lo que no tienes, y contestando cada punto con la verdad y una fecha cuando falte algo. Adjuntar evidencias sencillas, como un procedimiento o un registro, da más confianza que un sí sin respaldo."),
  ("¿Puedo perder un cliente por no cumplir sus requisitos de seguridad?", "Puede ocurrir si el cliente exige esos requisitos a toda su cadena de suministro y no ve voluntad de adaptarse. Lo habitual es que acepte un plan con plazos razonables cuando el proveedor demuestra que ha empezado."),
  ("¿Qué medidas de seguridad mínimas suele pedir una empresa grande a sus proveedores?", "Las más repetidas son control de accesos con doble factor, copias de seguridad probadas, equipos actualizados, un procedimiento para avisar de incidentes y formación básica del personal. Cada cliente añade las suyas según su sector."),
 ],
}

# Estructura: tres perfiles de uso de la IA en rejilla para reconocerse + lo que no vamos a decirte
D["servicios/ciberseguridad-y-sistemas/adaptacion-al-ai-act"] = {
 "estructura": "tres-perfiles-de-uso-para-reconocerse + lo-que-no-vamos-a-decirte",
 "lead": "En tu empresa ya se usa inteligencia artificial aunque nadie lo haya decidido: alguien redacta correos con ChatGPT, otro resume contratos, la web tiene un chatbot. Has oído que hay un reglamento europeo y no sabes si te toca hacer algo. La adaptación al AI Act para pymes que usan IA empieza por averiguarlo.",
 "bloque": """<section class="sec sec-suave"><div class="w">
<div class="cab"><p class="kicker">La IA entró sin pedir permiso</p><h2>Mi equipo usa ChatGPT en el trabajo: ¿tengo que hacer algo por el reglamento de IA?</h2></div>
<p style="max-width:820px">Depende de para qué se use, y esa es justo la información que casi ninguna pyme tiene. La norma no trata igual a quien pide ayuda para escribir un texto que a quien deja que un sistema puntúe candidatos. Antes de pensar en documentos conviene saber en cuál de estas tres situaciones se parece más tu empresa. Puedes estar en más de una.</p>
<div class="rejilla">
<div class="tarjeta"><h3>Usáis asistentes para trabajar más rápido</h3><p>Redactar, traducir, resumir, preparar una hoja de cálculo. Es el caso de la mayoría. Lo que toca es que el equipo sepa usarlos con criterio y qué datos no deben introducirse.</p></div>
<div class="tarjeta"><h3>La IA habla con vuestros clientes</h3><p>Un chatbot en la web, respuestas automáticas, imágenes o voces generadas en anuncios. Aquí entra además avisar con claridad de que se trata de un sistema automático o de contenido generado.</p></div>
<div class="tarjeta"><h3>La IA influye en decisiones sobre personas</h3><p>Filtrar currículos, evaluar empleados, valorar solvencia. Son usos que la norma mira con mucha más exigencia y que conviene revisar uno a uno antes de seguir.</p></div>
</div>
<p style="max-width:820px;margin-top:20px">Si no sabes en cuál estás, no te preocupes: es lo habitual. Las herramientas las contrata cada persona con su correo, algunas vienen ya dentro de programas que usabas antes y nadie lleva la cuenta. El inventario de usos es el primer entregable porque sin él todo lo demás son suposiciones.</p>
<h3 style="margin-top:30px">Lo que no vamos a decirte</h3>
<p style="max-width:820px">No te diremos que una plantilla descargada te deja «en regla», ni que por usar un asistente de texto necesitas un proyecto de meses. Tampoco prohibimos por sistema: dejar de usar la IA por miedo es otra forma de perder. Y no sustituimos a tu asesor jurídico; nuestro trabajo es técnico y organizativo, y te indicaremos qué puntos conviene que revise un abogado.</p>
<p style="max-width:820px">Lo que sí hacemos es ordenar. La parte formativa la tienes detallada en la <a href="/servicios/formacion-ia/formacion-obligatoria-ai-act">formación en IA por el AI Act</a> y las normas internas, en la <a href="/servicios/formacion-ia/politica-de-uso-de-ia-para-empresas">política de uso de IA para empresas</a>. Si antes de regular quieres saber dónde te aporta algo la IA, empieza por una <a href="/servicios/consultoria-y-ayudas/auditoria-de-ia-para-pymes">auditoría de IA para pymes</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo saber qué herramientas de IA se están usando en mi empresa?", "Preguntando al equipo sin ánimo de sancionar, revisando los cargos de suscripciones y mirando qué funciones de IA traen activadas los programas que ya usáis. Con eso se elabora un inventario de usos con su finalidad y su responsable."),
  ("¿Qué pasa si un empleado usa una IA gratuita con datos de clientes?", "Esos datos pueden quedar fuera del control de la empresa, según las condiciones del servicio. Lo razonable es fijar por escrito qué herramientas están permitidas y qué información no se introduce nunca, y explicárselo al equipo."),
 ],
}

# Estructura: preguntas que te hará tu distribuidor (ol) + glosario mínimo en lenguaje llano (dl)
D["servicios/ciberseguridad-y-sistemas/adaptacion-al-reglamento-de-ciberresiliencia"] = {
 "estructura": "preguntas-del-distribuidor-en-lista-ordenada + glosario-minimo-en-llano",
 "lead": "Fabricas un aparato que se conecta por wifi o vendes un programa que instalan tus clientes, sois pocos y nadie en la empresa se dedica a la seguridad. Un distribuidor empieza a preguntar si el producto cumplirá la nueva norma europea. La adaptación de productos al Reglamento de Ciberresiliencia convierte esa pregunta en una lista de tareas.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Para quien hace producto, no solo lo usa</p><h2>¿Mi producto conectado podrá seguir vendiéndose en Europa?</h2></div>
<p style="max-width:820px">Sí, si empiezas a preparar ahora lo que la norma pedirá de forma escalonada. Esta página no va dirigida a quien usa programas en su oficina, sino a quien los fabrica o los pone en el mercado: un termostato con aplicación, una báscula que envía datos, un software de gestión instalable, un sensor para naves.</p>
<p style="max-width:820px">El problema de un fabricante pequeño no suele ser la mala voluntad. Es que el producto se hizo para funcionar, con piezas de aquí y de allá, y nadie apuntó cuáles. Cuando un cliente pregunta, no hay de dónde sacar la respuesta.</p>
<h3 style="margin-top:30px">Cinco preguntas que acabará haciéndote un cliente o un distribuidor</h3>
<ol style="max-width:820px">
<li>¿Qué componentes de terceros lleva vuestro producto y en qué versión?</li>
<li>Si mañana se descubre un fallo en uno de ellos, ¿cómo os enteráis?</li>
<li>¿Cómo llega la corrección a los equipos que ya están instalados en casa de mis clientes?</li>
<li>¿Hasta cuándo vais a publicar actualizaciones de este modelo?</li>
<li>¿A quién escribe un investigador, o yo mismo, si encuentra una vulnerabilidad?</li>
</ol>
<p style="max-width:820px">Si puedes contestar a las cinco por escrito, tienes hecha buena parte del camino. Si no, cada una señala un trabajo concreto que se puede planificar por trimestres sin parar la producción.</p>
<h3 style="margin-top:30px">Cuatro términos que vas a oír, en cristiano</h3>
<dl style="max-width:820px">
<dt><strong>Producto con elementos digitales</strong></dt><dd>Cualquier programa o aparato que lleva software y puede conectarse a otro dispositivo o a una red.</dd>
<dt><strong>Lista de materiales del software</strong></dt><dd>El «escandallo» de tu programa: qué librerías y piezas lo componen. Es a tu producto lo que la lista de ingredientes a un alimento.</dd>
<dt><strong>Gestión de vulnerabilidades</strong></dt><dd>Tener a alguien pendiente de los fallos que se publican, decidir cuáles te afectan y corregirlos en un plazo.</dd>
<dt><strong>Periodo de soporte</strong></dt><dd>El tiempo durante el que te comprometes a seguir sacando arreglos para ese modelo.</dd>
</dl>
<p style="max-width:820px;margin-top:18px">No certificamos productos ni emitimos declaraciones de conformidad; preparamos contigo la parte técnica y documental y te decimos cuándo necesitas a un organismo o a un asesor legal. Si tu caso es el contrario, que no fabricas pero un cliente te pide requisitos de seguridad como empresa, lo tuyo es la <a href="/servicios/ciberseguridad-y-sistemas/adaptacion-a-nis2-para-proveedores">adaptación a NIS2 para proveedores</a>. El calendario general de normas lo mantenemos en <a href="/normativas">normativas</a> y puedes plantearnos tu producto en el <a href="/contacto#diagnostico">diagnóstico gratuito</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo saber qué librerías y componentes lleva mi software?", "Con herramientas que analizan el código y sus dependencias y generan una lista con nombre y versión de cada pieza. La primera vez requiere revisión manual; después se actualiza de forma automática con cada versión del producto."),
  ("¿Qué pasa si descubro una vulnerabilidad en un producto que ya he vendido?", "Hay que valorar su gravedad, preparar la corrección y hacerla llegar a los equipos instalados, además de informar a los clientes afectados. Tener ese proceso decidido de antemano evita improvisar cuando ocurre."),
 ],
}

# Estructura: ejercicio de quince minutos con el equipo (ol) + tabla por tipo de negocio + lo que un plan no evita
D["servicios/ciberseguridad-y-sistemas/copias-de-seguridad-y-plan-de-continuidad"] = {
 "estructura": "ejercicio-de-quince-minutos-con-el-equipo + tabla-por-tipo-de-negocio + lo-que-el-plan-no-evita",
 "lead": "Una tubería rota sobre el servidor, un portátil robado del coche o un archivo cifrado por un virus, y la pregunta es siempre la misma: ¿mañana podemos abrir? Unas copias de seguridad y un plan de continuidad de negocio sirven para tener la respuesta pensada antes, y no improvisarla con la oficina parada.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Pensarlo un día tranquilo</p><h2>Si mañana no arranca nada, ¿cuánto tardaría mi empresa en volver a trabajar?</h2></div>
<p style="max-width:820px">La mayoría de los negocios no lo sabe, porque nunca se lo ha planteado en voz alta. No hace falta un consultor para la primera aproximación. Reúne quince minutos a las personas que llevan administración, atención al cliente y producción, y haced este ejercicio con papel y bolígrafo.</p>
<ol style="max-width:820px">
<li>Imaginad que mañana a las ocho no hay ordenadores, ni servidor, ni internet en la oficina.</li>
<li>Que cada uno escriba lo primero que no podría hacer: facturar, ver la agenda, consultar un pedido, fichar.</li>
<li>Al lado, cuántas horas o días aguanta el negocio sin eso antes de perder dinero o clientes.</li>
<li>Por último, de qué fecha tendrían que ser los datos como muy tarde para poder continuar: ¿de ayer?, ¿de la semana pasada?</li>
<li>Comparad las hojas. Casi siempre hay sorpresas.</li>
</ol>
<h3 style="margin-top:30px">Lo imprescindible cambia mucho de un negocio a otro</h3>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Tipo de negocio</th><th>Lo que no puede faltar</th><th>Lo que puede esperar unos días</th></tr></thead><tbody>
<tr><td>Clínica o centro con citas</td><td>La agenda del día y las fichas de pacientes</td><td>La contabilidad y el archivo antiguo</td></tr>
<tr><td>Tienda online</td><td>La web, los pedidos en curso y el stock</td><td>Las estadísticas y el boletín</td></tr>
<tr><td>Asesoría o despacho</td><td>Los expedientes abiertos y los certificados</td><td>Los ejercicios cerrados</td></tr>
<tr><td>Taller o empresa de instalaciones</td><td>Los partes de trabajo y los teléfonos de clientes</td><td>Los presupuestos antiguos</td></tr>
</tbody></table></div>
<p style="max-width:820px;margin-top:20px">Con esas dos respuestas por cada sistema, cuánto puedes estar sin él y cuántos datos puedes permitirte rehacer, las copias dejan de ser «las que vienen por defecto» y se diseñan para lo que tu empresa necesita. Lo crítico se copia más a menudo y se recupera primero.</p>
<h3 style="margin-top:30px">Lo que un plan no evita</h3>
<p style="max-width:820px">No impide que ocurra un incidente ni promete que no se pierda nada. Reduce el tiempo de parada y acota la pérdida a lo que tú has decidido aceptar. Y solo vale si se mantiene: un plan escrito hace tres años, con personas que ya no están y programas que ya no se usan, da una tranquilidad falsa. Por eso se acompaña de una <a href="/servicios/departamento-tecnologico/prueba-mensual-de-copias-de-seguridad">prueba mensual de restauración</a>. Si parte del riesgo viene de tener todo en un servidor dentro de la oficina, valora una <a href="/servicios/ciberseguridad-y-sistemas/migracion-a-la-nube">migración a la nube</a>; y si son los propios equipos los que están al límite, la <a href="/servicios/ciberseguridad-y-sistemas/renovacion-de-equipos-y-fin-de-windows-10">renovación de equipos</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo hacer un plan de continuidad para una empresa pequeña?", "Lista los sistemas sin los que no puedes trabajar, decide cuánto tiempo puedes estar sin cada uno y cuántos datos puedes perder, y escribe quién hace qué si fallan. Con eso se ajustan las copias y se deja el plan en un sitio accesible fuera de la oficina."),
  ("¿Qué pasa si un virus cifra los archivos de la empresa?", "Se aísla el equipo afectado, se comprueba el alcance y se restaura desde una copia que el ataque no haya podido tocar. Por eso conviene tener al menos una copia desconectada o protegida contra borrado, y haber probado antes la restauración."),
  ("¿Dónde debo guardar el plan de continuidad?", "En un lugar al que puedas acceder aunque la oficina y sus sistemas no estén disponibles: impreso en casa de dos responsables y en un servicio en la nube independiente. Un plan guardado solo en el servidor que ha fallado no sirve."),
 ],
}

# Estructura: señales de que el servidor de la oficina ya frena (lista) + segunda sección con rejilla por persona el primer lunes + cuándo no migrar
D["servicios/ciberseguridad-y-sistemas/migracion-a-la-nube"] = {
 "estructura": "senales-de-que-el-servidor-frena + rejilla-por-persona-el-primer-lunes + cuando-no-migrar",
 "lead": "El servidor está en un cuartito, hace ruido, nadie sabe muy bien qué tiene dentro y solo se puede trabajar desde la oficina. Te gustaría quitarlo, pero te frena el miedo a que un lunes nadie encuentre sus archivos. Una migración a la nube para pymes sin perder datos se planifica justamente contra ese miedo.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">El aparato del cuartito</p><h2>¿Cuándo deja de tener sentido el servidor de la oficina?</h2></div>
<ul class="lista" style="max-width:820px">
<li>Para consultar un documento desde casa hay que llamar a alguien para que lo envíe por correo.</li>
<li>Existe una conexión remota, pero va tan lenta que nadie la usa.</li>
<li>Hay carpetas con nombres de personas que se fueron hace años y nadie se atreve a borrarlas.</li>
<li>Cuando se va la luz o se cae internet en la oficina, se paran también los que están fuera.</li>
<li>El servidor tiene más de seis o siete años y la única persona que lo entendía ya no viene.</li>
<li>Los comerciales llevan copias de todo en su portátil «por si acaso».</li>
</ul>
<p style="max-width:820px;margin-top:18px">Con dos o tres de estas señales, el servidor local ya te está costando tiempo cada semana. El miedo al cambio también tiene fundamento: una mudanza mal hecha deja enlaces rotos, permisos abiertos a quien no debe y archivos duplicados que nadie sabe cuál es el bueno. Por eso lo que se cuida no es la copia, que es lo fácil, sino el orden previo y el primer día.</p>
</div></section>
<section class="sec sec-suave"><div class="w">
<h3>Qué nota cada persona el primer lunes</h3>
<div class="rejilla">
<div class="tarjeta"><h3>Administración</h3><p>Abre las mismas carpetas con los mismos nombres. Cambia el icono desde el que entra, no dónde está cada cosa.</p></div>
<div class="tarjeta"><h3>Quien trabaja fuera</h3><p>Consulta y edita desde el portátil o el móvil sin conexión especial y sin llevar copias sueltas.</p></div>
<div class="tarjeta"><h3>Gerencia</h3><p>Sabe quién tiene acceso a qué y puede recuperar una versión anterior de un documento sin pedir ayuda.</p></div>
</div>
<h3 style="margin-top:30px">Cuándo es mejor no migrar, o no del todo</h3>
<p style="max-width:820px">Si tu conexión a internet es mala y no hay alternativa en la zona, si trabajas con archivos enormes que se abren decenas de veces al día, o si un programa antiguo solo funciona instalado en un equipo de la red, puede convenir una solución mixta: lo ligero en la nube y lo pesado en local. Lo decimos antes de empezar, no a mitad. Y llevar los datos fuera no elimina la necesidad de copia: sigue haciendo falta un <a href="/servicios/ciberseguridad-y-sistemas/copias-de-seguridad-y-plan-de-continuidad">plan de copias y continuidad</a>. Aprovecha la mudanza para revisar quién entra en cada carpeta con una <a href="/servicios/departamento-tecnologico/auditoria-de-accesos-y-licencias">auditoría de accesos</a>; si el problema es ese programa viejo que te ata al servidor, mira el <a href="/servicios/migraciones-e-integraciones/rescate-de-software-antiguo">rescate de software antiguo</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo pasar los archivos de la empresa a la nube sin perder nada?", "Haciendo primero un inventario de carpetas, limpiando duplicados, copiando en varias pasadas mientras se sigue trabajando y comparando al final el número y tamaño de archivos en origen y destino. El servidor antiguo se conserva un tiempo en solo lectura como respaldo."),
  ("¿Qué pasa si se cae internet y tengo todo en la nube?", "Los archivos sincronizados en el ordenador siguen disponibles y los cambios se suben al volver la conexión. Para lo demás conviene tener una línea de respaldo, por ejemplo móvil, si el negocio no puede parar."),
 ],
}

# Estructura: la pregunta que hace un cliente o una aseguradora (blockquote) + lo que hace quien ocupa ese papel y lo que no + cuándo basta con menos
D["servicios/ciberseguridad-y-sistemas/responsable-de-ciberseguridad-externalizado"] = {
 "estructura": "pregunta-del-cliente-o-la-aseguradora + lo-que-no-es-ese-papel + si-nadie-te-lo-exige",
 "lead": "En el formulario de un cliente, de la aseguradora o de una licitación aparece una casilla: «nombre de su responsable de seguridad de la información». En tu empresa no hay nadie con ese cargo y contratarlo a jornada completa no tiene sentido. Un responsable de ciberseguridad externo para pymes ocupa ese puesto las horas que hacen falta.",
 "bloque": """<section class="sec sec-suave"><div class="w">
<div class="cab"><p class="kicker">Una casilla en blanco</p><h2>¿Quién responde de la seguridad informática en mi empresa?</h2></div>
<blockquote style="max-width:820px"><p>«Indique el nombre, cargo y contacto de la persona responsable de la seguridad de la información en su organización.»</p></blockquote>
<p style="max-width:820px;margin-top:18px">En una pyme la respuesta sincera suele ser «nadie en concreto». El informático de mantenimiento arregla lo que se rompe, el gerente firma lo que le ponen delante y la persona de administración guarda las contraseñas. Cada uno hace su parte y nadie mira el conjunto ni decide qué es prioritario.</p>
<p style="max-width:820px">Eso funciona hasta que alguien de fuera pregunta, o hasta que pasa algo y hay que decidir en una hora si se apagan los equipos, a quién se avisa y qué se le dice a los clientes. En ese momento se echa en falta a una persona que ya lo tuviera pensado.</p>
<h3 style="margin-top:30px">Lo que este papel no es</h3>
<ul class="lista" style="max-width:820px">
<li><strong>No es un técnico que viene a arreglar ordenadores.</strong> Decide qué hay que proteger primero y comprueba que se hace; puede apoyarse en tu informático actual.</li>
<li><strong>No es un producto.</strong> Ningún antivirus ni cortafuegos sustituye a alguien que revise con calendario.</li>
<li><strong>No es un seguro.</strong> Reduce la probabilidad y el alcance de un incidente; no lo descarta.</li>
<li><strong>No es quien carga con la culpa.</strong> La responsabilidad última sigue siendo de la dirección, que decide con mejor información.</li>
</ul>
<h3 style="margin-top:30px">Si nadie te lo exige, quizá aún no lo necesitas</h3>
<p style="max-width:820px">Si nadie te pide acreditar nada, sois pocos y no manejáis datos delicados de terceros, puede bastar con las medidas básicas bien puestas: accesos revisados, copias probadas y equipos al día. Eso lo cubre <a href="/servicios/departamento-tecnologico">tu departamento tecnológico</a> sin necesidad de nombrar un responsable.</p>
<p style="max-width:820px">La figura compensa cuando hay clientes que auditan a sus proveedores, cuando una póliza lo exige o cuando el negocio depende de sistemas que no pueden parar. Si el detonante ha sido un cuestionario, empieza por la <a href="/servicios/ciberseguridad-y-sistemas/adaptacion-a-nis2-para-proveedores">adaptación a NIS2 para proveedores</a>; si es que temes que usen tu nombre para engañar a clientes, por la <a href="/servicios/departamento-tecnologico/vigilancia-de-suplantacion">vigilancia de suplantación</a>.</p>
</div></section>""",
 "faq": [
  ("¿A quién pongo como responsable de seguridad si no tengo departamento de informática?", "Puedes designar a una persona interna con apoyo externo o a un responsable externalizado que asuma las funciones. Lo importante es que exista alguien identificable, con tiempo asignado y capacidad de proponer medidas a la dirección."),
  ("¿Cómo saber si mi empresa necesita un responsable de ciberseguridad?", "Suele hacer falta cuando clientes o aseguradoras piden acreditar medidas de seguridad, cuando se manejan datos sensibles de terceros o cuando una parada de los sistemas detiene el negocio. Si no se da ninguno de esos casos, bastan unas medidas básicas bien mantenidas."),
 ],
}
