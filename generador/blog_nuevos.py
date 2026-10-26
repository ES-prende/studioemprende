# Artículos nuevos (desde el 24/10/2026). Se publican con la misma plantilla que el resto del blog, pero NO entran
# en la portada, el índice del blog, el mapa web ni los "otros artículos" de los posts existentes: esas páginas están
# indexadas y no se modifican. Se enlazan desde los temas (/temas/), páginas no indexadas y su sitemap.
from blog_formacion import _resp

ARTICULOS = [
("como-calcular-el-credito-de-formacion-fundae", "Cómo calcular el crédito de formación FUNDAE de tu empresa",
 "Cómo saber cuánto crédito de formación bonificada tiene tu empresa en FUNDAE: la fórmula, los porcentajes según plantilla, el mínimo de 420 € y un ejemplo paso a paso.",
 "26 oct 2026", "Formación", "formacion-ia", _resp(
 "El crédito de formación de FUNDAE se calcula aplicando un porcentaje a lo que tu empresa cotizó por formación profesional el año anterior: el 100 % si tienes de 6 a 9 trabajadores, el 75 % de 10 a 49, el 60 % de 50 a 249 y el 50 % a partir de 250. Las empresas de 1 a 5 trabajadores tienen un crédito mínimo de 420 € al año. El dato exacto lo consultas en la aplicación de Formación Programada de FUNDAE.") + """
<p>Casi todas las empresas tienen un crédito para formar a su equipo que se descuenta de los seguros sociales, y muchas no lo usan porque no saben cuánto es. Esta guía explica de dónde sale, cómo calcularlo tú y qué cubre de verdad.</p>
<p>Si todavía no sabes qué es la formación bonificada ni cómo funciona, empieza por la guía de <a href="/blog/formacion-bonificada-para-empresas-fundae">formación bonificada para empresas con FUNDAE</a>. Aquí vamos a los números.</p>
<h2>De dónde sale el crédito de formación</h2>
<p>Cada mes, en las cotizaciones a la Seguridad Social, se paga una <b>cuota de formación profesional</b> del 0,70 % de la base de cotización: el 0,60 % lo pone la empresa y el 0,10 % el trabajador. Una parte de lo cotizado el año anterior vuelve a la empresa como crédito para formar a su plantilla al año siguiente. Cuánta parte depende del tamaño de la empresa.</p>
<h2>Porcentaje según el tamaño de la plantilla</h2>
<table><thead><tr><th>Plantilla media</th><th>Crédito</th></tr></thead><tbody>
<tr><td>De 1 a 5 trabajadores</td><td>Mínimo de 420 € al año</td></tr>
<tr><td>De 6 a 9 trabajadores</td><td>100 % de lo cotizado por formación profesional</td></tr>
<tr><td>De 10 a 49 trabajadores</td><td>75 %</td></tr>
<tr><td>De 50 a 249 trabajadores</td><td>60 %</td></tr>
<tr><td>250 trabajadores o más</td><td>50 %</td></tr>
</tbody></table>
<p>Los porcentajes se fijan cada año en los Presupuestos Generales del Estado. Antes de planificar, comprueba los vigentes en la web de <a href="https://www.fundae.es" rel="noopener" target="_blank">FUNDAE</a>.</p>
<h2>Cómo calcularlo paso a paso</h2>
<ol>
<li><b>Busca lo cotizado por formación profesional el año anterior.</b> Lo tienes en los recibos de liquidación de cotizaciones o te lo da tu gestoría.</li>
<li><b>Mira tu plantilla media</b> de ese año para saber en qué tramo estás.</li>
<li><b>Aplica el porcentaje del tramo.</b> Si te sale menos de 420 € y tienes hasta 5 trabajadores, tu crédito es 420 €.</li>
</ol>
<p><b>Ejemplo:</b> una empresa con una plantilla media de 20 personas cotizó el año pasado 6.000 € por formación profesional. Está en el tramo de 10 a 49 trabajadores, así que su crédito para este año es 6.000 × 75 % = <b>4.500 €</b>.</p>
<p>Un autónomo con dos empleados que cotizó 300 € tiene igualmente un crédito de 420 €, porque es el mínimo para empresas de hasta 5 trabajadores.</p>
<h2>Cómo consultar el crédito exacto</h2>
<p>FUNDAE calcula el crédito de cada empresa con los datos de la Seguridad Social. Para verlo tienes que acceder a la aplicación de Formación Programada de su web, con certificado digital, o pedírselo a tu gestoría o a la entidad que te organice la formación.</p>
<h2>Qué cubre y qué no</h2>
<ul>
<li><b>No cubre cualquier precio.</b> El importe bonificable de cada curso tiene un máximo por hora y participante según la modalidad, así que un curso caro puede no quedar bonificado del todo.</li>
<li><b>Salvo las microempresas, la empresa suele aportar una parte</b> del coste de la formación con fondos propios (la cofinanciación privada), que depende del tamaño de la plantilla.</li>
<li><b>El crédito es anual.</b> Lo que no se usa en el año se pierde, aunque las empresas de menos de 50 trabajadores pueden acumularlo en determinados casos si lo comunican en plazo. Pregunta a tu gestoría por tu caso.</li>
<li><b>Hay que comunicar la formación antes de empezar</b> y justificarla al terminar para poder aplicar la bonificación en los seguros sociales.</li>
</ul>
<h2>Qué formación conviene hacer con el crédito</h2>
<p>La que tu equipo vaya a usar el lunes siguiente: el programa de gestión que acabáis de implantar, hojas de cálculo que se usan cada día o el uso de la inteligencia artificial en el trabajo, que el AI Act exige a las empresas que usan IA. Si quieres un curso pensado con tus herramientas y tus casos reales, mira los <a href="/servicios/formacion-ia/cursos-de-formacion-a-medida-para-empresas">cursos de formación a medida para empresas</a>.</p>
"""),
("cuanto-cuesta-un-crm-para-autonomos", "Cuánto cuesta un CRM para autónomos en 2026",
 "Precio de un CRM para autónomos en 2026: qué ofrecen los gratuitos, cómo se paga una suscripción, cuánto cuesta uno implantado y los costes ocultos que conviene mirar antes.",
 "24 oct 2026", "Gestión", "autonomos", _resp(
 "Un CRM para autónomos puede costar cero euros, una cuota mensual por usuario o un pago de implantación más una cuota de soporte. El gratuito sirve para empezar con pocos contactos; la suscripción encaja si te vale una herramienta estándar; el implantado compensa cuando necesitas que el CRM se conecte con tu facturación, tu WhatsApp y tu forma de trabajar. En un CRM implantado, pide siempre un presupuesto cerrado que incluya migración, formación e integraciones.") + """
<p>«¿Cuánto cuesta un CRM?» tiene tres respuestas distintas según el tipo de CRM, y compararlas por la cuota mensual engaña: lo caro de un CRM casi nunca es la cuota, sino lo que no incluye. Esta guía separa los tres modelos, dice qué pagas en cada uno y te deja una fórmula para comparar con tus números.</p>
<p>Si todavía estás decidiendo qué funciones necesitas, empieza por la guía de <a href="/blog/crm-para-autonomos">CRM para autónomos y freelancers: cuál elegir y qué debe tener</a>. Aquí hablamos solo de dinero.</p>
<h2>Los tres modelos de precio de un CRM</h2>
<table><thead><tr><th>Modelo</th><th>Qué pagas</th><th>Encaja si…</th><th>Ojo con…</th></tr></thead><tbody>
<tr><td>CRM gratuito</td><td>Nada, a cambio de límites de contactos, usuarios o funciones</td><td>Estás empezando y tienes pocos clientes</td><td>La exportación de datos, el soporte y dónde se guardan</td></tr>
<tr><td>Suscripción (SaaS)</td><td>Una cuota por usuario y mes, que sube con cada plan</td><td>Te vale una herramienta estándar tal como viene</td><td>Las funciones que solo están en el plan superior</td></tr>
<tr><td>CRM implantado a medida</td><td>Un pago de implantación y una cuota de soporte</td><td>Necesitas que se conecte con facturación, WhatsApp o tu web</td><td>Que el presupuesto sea cerrado y los datos sean tuyos</td></tr>
</tbody></table>
<h2>¿Merece la pena un CRM gratis para un autónomo?</h2>
<p>Para empezar, sí. Un CRM gratuito ordena tus contactos y tus oportunidades mejor que una hoja de cálculo. El problema llega cuando creces: los planes gratuitos limitan el número de contactos, de usuarios o de automatizaciones, y algunos no permiten exportar todo o lo complican. Antes de meter tus clientes, comprueba tres cosas:</p>
<ul><li>Si puedes exportar todos tus datos en un formato estándar, sin pagar.</li><li>Dónde se guardan los datos y si el proveedor firma un contrato de encargado de tratamiento, como exige el RGPD.</li><li>Qué pasa con tus datos si dejas de usarlo.</li></ul>
<h2>¿Cuánto se paga por un CRM de suscripción?</h2>
<p>Los CRM de suscripción cobran por usuario y mes, y casi siempre tienen tres o cuatro planes. Los de entrada son asequibles para una persona, pero las funciones que suele necesitar un autónomo que crece, como automatizaciones, informes o integraciones, están en los planes intermedios. Los precios cambian a menudo, así que consulta siempre la tarifa vigente en la web de cada proveedor y fíjate en si el precio es con permanencia anual o mes a mes.</p>
<p>Lo que la cuota no suele incluir: la migración de tus datos, la configuración inicial, la formación y la conexión con tu programa de facturación. Si no lo haces tú, alguien te lo cobrará aparte.</p>
<h2>¿Cuánto cuesta un CRM implantado a medida?</h2>
<p>Aquí pagas por tener el CRM montado con tus etapas de venta, tus plantillas, tu facturación y tus canales, y por que alguien lo mantenga. El precio depende de los módulos, de las integraciones y de cuántos datos hay que migrar, así que lo serio es pedir un <b>presupuesto cerrado</b> que diga qué incluye y qué no. Antes de firmar, comprueba que el presupuesto detalla:</p>
<ul>
<li>El pago inicial de implantación y la cuota mensual de soporte, por separado.</li>
<li>Si la migración de tus datos y la formación están incluidas.</li>
<li>Qué integraciones entran (facturación, web, WhatsApp) y cuáles se pagan aparte.</li>
<li>Que los datos son tuyos y cómo te los llevas si cambias de proveedor.</li>
</ul>
<p>Un CRM sectorial, pensado para un tipo de negocio concreto, suele salir más rentable que adaptar uno genérico. Un ejemplo es el que desarrollamos para asesorías energéticas: <a href="/casos/contratalux">caso ContrataLux</a>.</p>
<h2>Los costes que no aparecen en la cuota</h2>
<ol>
<li><b>Migración</b>: pasar tus clientes desde Excel u otro programa. Si lo haces a mano, cuéntalo en horas.</li>
<li><b>Formación</b>: el CRM que nadie usa es el más caro. Cuenta el tiempo de aprenderlo.</li>
<li><b>Integraciones</b>: conectar con tu facturación, tu web o WhatsApp. En WhatsApp, además, Meta cobra los mensajes de plantilla enviados fuera de una conversación abierta.</li>
<li><b>Usuarios extra</b>: el día que entra un colaborador, la cuota por usuario se multiplica.</li>
<li><b>Salida</b>: lo que cuesta llevarte tus datos si cambias de proveedor.</li>
</ol>
<h2>Cómo comparar con tus números</h2>
<p>Haz la cuenta a dos años, no a un mes:</p>
<p><b>Coste a 24 meses = alta o implantación + (cuota mensual × usuarios × 24) + migración + formación + integraciones</b></p>
<p>Y ponle al lado las horas que te ahorra: si el CRM te quita dos horas a la semana de buscar en WhatsApp y perseguir presupuestos, son más de 200 horas en dos años. Multiplícalas por lo que vale tu hora y verás cuál de los tres modelos te sale realmente más barato.</p>
<p>Si ya usas otro programa y quieres cambiar, la <a href="/servicios/migraciones-e-integraciones/migracion-desde-holded-clientify-hubspot-y-otros">migración desde Holded, Clientify, HubSpot y otros</a> está incluida al implantar el nuestro. Y si quieres que te hagamos la cuenta con tu caso, el <a href="/servicios/consultoria-y-ayudas/diagnostico-de-digitalizacion-gratuito">diagnóstico es gratuito</a>.</p>
"""),
]

FAQS = {
 "como-calcular-el-credito-de-formacion-fundae": [
  ("¿Cómo sé cuánto crédito FUNDAE tiene mi empresa?", "Entrando en la aplicación de Formación Programada de FUNDAE con certificado digital, o pidiéndoselo a tu gestoría. El cálculo aproximado es lo cotizado por formación profesional el año anterior por el porcentaje de tu tramo de plantilla."),
  ("¿Un autónomo sin empleados tiene crédito de formación?", "No. El crédito va ligado a la cotización por formación profesional de los trabajadores por cuenta ajena. Con al menos un empleado, la empresa tiene un mínimo de 420 € al año."),
  ("¿Qué pasa si no gasto el crédito este año?", "En general se pierde al terminar el año. Las empresas de menos de 50 trabajadores pueden acumularlo en determinados casos si lo comunican en plazo; consulta tu situación con tu gestoría."),
  ("¿Puedo bonificar un curso hecho a medida para mi equipo?", "Sí, si se comunica a FUNDAE antes de empezar y cumple los requisitos de duración, asistencia y justificación. El importe bonificable tiene un máximo por hora y participante."),
 ],
 "cuanto-cuesta-un-crm-para-autonomos": [
  ("¿Hay algún CRM gratis que sirva de verdad a un autónomo?", "Sí, para empezar con pocos contactos. Antes de elegirlo, comprueba que puedes exportar todos tus datos sin coste y dónde se guardan."),
  ("¿Cuánto cuesta un CRM con facturación incluida?", "Depende del modelo y de lo que haya que conectar. En un CRM implantado, pide un presupuesto cerrado que separe la implantación de la cuota mensual y diga si incluye migración y formación."),
  ("¿Qué es más barato a largo plazo, suscripción o a medida?", "Haz la cuenta a 24 meses sumando cuotas, usuarios, migración, formación e integraciones. Con un solo usuario y pocas necesidades suele ganar la suscripción; si necesitas integraciones y que alguien lo mantenga, el implantado se acerca o compensa."),
  ("¿Puedo cambiar de CRM sin perder mis clientes?", "Sí, si tu CRM actual permite exportar los datos. La migración desde Excel, Holded, Clientify, HubSpot y otros está incluida al implantar nuestro programa de gestión."),
 ],
}

ALT = {"como-calcular-el-credito-de-formacion-fundae": "Ilustración con la fórmula del crédito de formación: cotización por porcentaje según plantilla", "cuanto-cuesta-un-crm-para-autonomos": "Ilustración con tres etiquetas de precio de CRM: gratis, suscripción y a medida"}

RESUMEN = {"como-calcular-el-credito-de-formacion-fundae": "Crédito FUNDAE = lo cotizado por formación profesional el año anterior × el porcentaje de tu tramo (100 %, 75 %, 60 % o 50 %). De 1 a 5 trabajadores, mínimo de 420 € al año.", "cuanto-cuesta-un-crm-para-autonomos": "Un CRM para autónomos puede ser gratuito, de suscripción por usuario y mes o implantado a medida. Compáralos a 24 meses sumando cuotas, usuarios, migración, formación e integraciones, no solo por la cuota."}
