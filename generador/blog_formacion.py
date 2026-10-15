# Artículos del blog sobre formación (octubre 2026). Mismo formato que blog.ARTICULOS
# (slug, titulo, descripcion, fecha, categoria, servicio_relacionado, cuerpo_html) + FAQS, ALT y FECHA ISO.
FECHA_ISO = "2026-10-15"

def _resp(t):
    return '<div class="respuesta" style="margin:0 0 28px"><p class="kicker" style="margin:0 0 6px">Respuesta corta</p><p style="margin:0">%s</p></div>' % t

ARTICULOS = [
("formacion-bonificada-para-empresas-fundae", "Formación bonificada para empresas: cómo usar el crédito de FUNDAE",
 "Qué es la formación bonificada, cuánto crédito tiene tu empresa según su plantilla, qué cursos se pueden bonificar (también los de IA) y los pasos para no perder la bonificación.",
 "15 oct 2026", "Formación", "formacion-ia", _resp(
 "La formación bonificada permite a las empresas recuperar el coste de formar a su plantilla descontándolo de las cotizaciones a la Seguridad Social. Cada empresa tiene un crédito anual que gestiona a través de FUNDAE; si no lo usa, normalmente lo pierde.") + """
<p>Casi todas las empresas con trabajadores en plantilla pagan cada mes una cuota de formación profesional en sus seguros sociales. La <b>bonificación de la formación</b> es la manera de recuperar ese dinero: formas a tu equipo y lo que cuesta el curso se descuenta después de lo que pagas a la Seguridad Social.</p>
<h2>¿Qué es FUNDAE y qué papel tiene?</h2>
<p>FUNDAE (Fundación Estatal para la Formación en el Empleo) es el organismo que gestiona la llamada <b>formación programada por las empresas</b>. Su plataforma es donde se comunica cada curso, se registra a los alumnos y se justifica la formación para poder aplicar la bonificación.</p>
<h2>¿Cuánto crédito de formación tiene mi empresa?</h2>
<p>El crédito se calcula a partir de lo que tu empresa cotizó por formación profesional el año anterior, aplicando un porcentaje según el tamaño de la plantilla:</p>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Plantilla</th><th>Bonificación sobre lo cotizado</th><th>Cofinanciación privada mínima</th></tr></thead><tbody>
<tr><td>1 a 5 personas</td><td>100 % (crédito mínimo de 420 € al año)</td><td>No se exige</td></tr>
<tr><td>6 a 9 personas</td><td>100 %</td><td>5 %</td></tr>
<tr><td>10 a 49 personas</td><td>75 %</td><td>10 %</td></tr>
<tr><td>50 a 249 personas</td><td>60 %</td><td>20 %</td></tr>
<tr><td>250 o más</td><td>50 %</td><td>40 %</td></tr></tbody></table></div>
<p>La <b>cofinanciación privada</b> es la parte del coste que tiene que poner la empresa. Se puede cubrir, por ejemplo, con el salario de las horas que los empleados forman dentro de su jornada.</p>
<h2>¿Se puede bonificar la formación en IA?</h2>
<p>Sí. La <b>formación en IA bonificada</b> funciona igual que cualquier otra: lo importante no es el tema, sino que el curso esté relacionado con la actividad de la empresa y se comunique y justifique en plazo. Un curso de ChatGPT para el equipo comercial, uno de Excel para administración o una <a href="../servicios/formacion-ia/cursos-de-formacion-a-medida-para-empresas.html">formación a medida para empresas</a> pueden entrar en el crédito.</p>
<h2>Pasos para bonificar un curso sin perder el dinero</h2>
<ol><li><b>Consulta tu crédito disponible</b> en la plataforma de FUNDAE o pídeselo a tu asesoría.</li>
<li><b>Decide quién lo gestiona:</b> la propia empresa o una entidad organizadora que lo tramita por ti.</li>
<li><b>Comunica el inicio antes de empezar</b> el curso, con la antelación mínima que marca la norma. Si se comunica tarde, no se puede bonificar.</li>
<li><b>Controla la asistencia</b> y guarda las evidencias: listas de firmas, conexiones si es online y evaluaciones.</li>
<li><b>Comunica la finalización</b> con los costes y aplica la bonificación en los seguros sociales dentro del plazo.</li></ol>
<h2>¿Y si mi empresa tiene menos de 50 trabajadores?</h2>
<p>Las empresas de menos de 50 personas pueden <b>reservar el crédito que no gasten</b> y acumularlo hasta dos ejercicios más, si lo comunican dentro del plazo que fija FUNDAE (habitualmente, antes del 30 de junio). Es útil para pymes que quieren hacer una formación más grande un año concreto.</p>
<h2>Errores habituales</h2>
<ul><li>Empezar el curso antes de comunicarlo.</li><li>No guardar las firmas o las evidencias de asistencia.</li><li>Pensar que el crédito se acumula siempre: sin reserva, el que no se usa en el año se pierde.</li><li>Elegir cursos genéricos que nadie aplica: bonificado o no, el tiempo del equipo cuesta.</li></ul>
<p class="mut" style="font-size:14px">Fuentes: <a href="https://www.boe.es/buscar/act.php?id=BOE-A-2015-9734" target="_blank" rel="noopener">Ley 30/2015 del sistema de formación profesional para el empleo</a> y <a href="https://factorial.es/blog/fundae-empresas-formaciones/" target="_blank" rel="noopener">guía de FUNDAE para empresas (Factorial, actualizada en 2026)</a>. Las cifras pueden cambiar: confírmalas en FUNDAE o con tu asesoría antes de planificar.</p>
"""),
("plan-de-formacion-para-empresas", "Plan de formación para empresas: cómo hacerlo en 6 pasos",
 "Cómo hacer un plan de formación anual para tu empresa: detectar necesidades, priorizar, elegir formato, calcular presupuesto y medir si ha servido.",
 "15 oct 2026", "Formación", "formacion-ia", _resp(
 "Un plan de formación para empresas es el documento que recoge qué tiene que aprender cada puesto durante el año, cómo, cuándo y con qué presupuesto. Se hace en seis pasos: detectar necesidades, priorizar, fijar objetivos, elegir formato, calendarizar con presupuesto y medir resultados.") + """
<p>Sin plan, la formación se reparte a golpe de oferta: un curso que llega por correo, otro que pide alguien porque le interesa. Con plan, cada hora de formación responde a un problema real del negocio.</p>
<h2>1. Detecta qué necesita cada puesto</h2>
<p>Habla con responsables y con quien hace el trabajo. Las mejores pistas están en los errores que se repiten, las tareas que dependen de una sola persona y las herramientas que se infrautilizan. Las <b>evaluaciones de desempeño</b> y las quejas de clientes también dan pistas.</p>
<h2>2. Prioriza por impacto</h2>
<p>No todo cabe en un año. Ordena las necesidades según lo que cuestan hoy (tiempo, errores, ventas perdidas) y por urgencia legal: la <a href="formacion-obligatoria-en-empresas.html">formación obligatoria</a> va primero.</p>
<h2>3. Escribe objetivos medibles</h2>
<p>«Mejorar en Excel» no se puede medir. «Que administración cierre el informe mensual en una mañana en lugar de dos días» sí. Cada acción formativa debe tener un objetivo así.</p>
<h2>4. Elige el formato adecuado</h2>
<ul><li><b>Formación a medida (in company):</b> para procesos y herramientas propias de tu empresa.</li><li><b>Curso abierto:</b> para conocimientos generales y pocas personas.</li><li><b>Online en directo o presencial:</b> según si el equipo está repartido o en el mismo sitio.</li><li><b>Acompañamiento en el puesto:</b> para quien entra nuevo o cambia de herramienta.</li></ul>
<h2>5. Calendariza y calcula el presupuesto</h2>
<p>Reparte las acciones por trimestres evitando los picos de trabajo. Al calcular el presupuesto, cuenta las horas del equipo además del precio del curso, y revisa cuánto puedes recuperar con la <a href="formacion-bonificada-para-empresas-fundae.html">formación bonificada de FUNDAE</a>.</p>
<h2>6. Mide si ha servido</h2>
<p>Vuelve a los objetivos del paso 3 a las pocas semanas de cada curso: ¿se usa lo aprendido?, ¿ha bajado el tiempo o los errores? Lo que no funcione, se cambia en el plan del año siguiente.</p>
<h2>Plantilla mínima de un plan de formación</h2>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Puesto</th><th>Necesidad</th><th>Objetivo medible</th><th>Formato</th><th>Fecha</th><th>Coste</th></tr></thead><tbody>
<tr><td>Administración</td><td>Informe mensual manual</td><td>Cerrarlo en media jornada</td><td>Curso de Excel a medida</td><td>Primer trimestre</td><td>Según presupuesto</td></tr>
<tr><td>Comercial</td><td>Propuestas lentas</td><td>Enviar propuesta en 24 h</td><td>Formación en IA aplicada</td><td>Segundo trimestre</td><td>Según presupuesto</td></tr></tbody></table></div>
<p>Si quieres, te ayudamos a montar el plan y a impartir las acciones que tienen que ver con herramientas, IA y procesos: mira nuestros <a href="../servicios/formacion-ia/cursos-de-formacion-a-medida-para-empresas.html">cursos de formación a medida para empresas</a>.</p>
"""),
("formacion-obligatoria-en-empresas", "Formación obligatoria en empresas: qué cursos tienes que dar en 2026",
 "Qué formación es obligatoria en una empresa en España: prevención de riesgos, igualdad y acoso, LGTBI, protección de datos, alimentos, IA y las 20 horas anuales del Estatuto.",
 "15 oct 2026", "Normativas", "formacion-ia", _resp(
 "En España, toda empresa con trabajadores debe dar formación en prevención de riesgos laborales. Según su tamaño y actividad, también puede tener que formar en igualdad y acoso, medidas LGTBI, protección de datos, manipulación de alimentos o uso de la IA. Además, cada trabajador con un año de antigüedad tiene derecho a 20 horas anuales de formación retribuida.") + """
<p>La formación obligatoria no es un trámite: es lo primero que piden en una inspección y lo que te protege si algo sale mal. Este es el resumen de las obligaciones más habituales.</p>
<h2>Prevención de riesgos laborales (todas las empresas)</h2>
<p>La Ley 31/1995 obliga a dar a cada trabajador formación <b>teórica y práctica, suficiente y adecuada</b> sobre los riesgos de su puesto: al contratarle, cuando cambian sus funciones o se introducen equipos o tecnologías nuevas. Debe impartirse <b>dentro de la jornada</b> (o descontando ese tiempo) y su coste nunca puede recaer en el trabajador.</p>
<h2>Igualdad y prevención del acoso</h2>
<p>Las empresas deben tener medidas contra el acoso sexual y por razón de sexo, y la formación y sensibilización de la plantilla es una de ellas. Las empresas de <b>50 o más personas</b> deben tener además un plan de igualdad, que suele incluir formación.</p>
<h2>Medidas LGTBI (más de 50 personas)</h2>
<p>El Real Decreto 1026/2024 obliga a las empresas de más de 50 personas trabajadoras a aplicar un conjunto de medidas para la igualdad y no discriminación de las personas LGTBI, entre ellas <b>formación dirigida a toda la plantilla</b>.</p>
<h2>Protección de datos</h2>
<p>El RGPD exige aplicar medidas para que quien trata datos personales lo haga de forma segura. La formación del personal que accede a datos de clientes o empleados es la forma habitual de demostrarlo.</p>
<h2>Manipulación de alimentos</h2>
<p>En hostelería, comercio de alimentación e industria alimentaria, quien manipula alimentos debe estar formado en higiene alimentaria según su actividad.</p>
<h2>Uso de la inteligencia artificial</h2>
<p>Desde el 2 de febrero de 2025, el Reglamento europeo de IA exige que las empresas que usan sistemas de IA garanticen un <b>nivel suficiente de alfabetización en IA</b> de su personal. Lo explicamos en detalle en <a href="formacion-ia-obligatoria-ai-act.html">formación en IA obligatoria por el AI Act</a>.</p>
<h2>Las 20 horas anuales de formación</h2>
<p>El Estatuto de los Trabajadores (art. 23.3) reconoce a quien lleva al menos un año en la empresa un permiso retribuido de <b>20 horas al año</b> de formación vinculada a su puesto, acumulables hasta cinco años. Si la empresa ya da esa formación por otra obligación legal, se puede computar.</p>
<h2>¿Puede la empresa obligarme a hacer un curso fuera del horario?</h2>
<p>La formación en prevención de riesgos debe hacerse en horario laboral o descontarse de la jornada. Para el resto, depende del convenio y del tipo de formación: lo razonable es que la formación que pide la empresa se haga dentro de la jornada o se compense.</p>
<p>Si quieres cubrir la parte de herramientas, datos e IA con una formación que además sea útil para el día a día, mira nuestra <a href="../servicios/formacion-ia.html">formación en IA para empresas</a>.</p>
<p class="mut" style="font-size:14px">Fuentes: <a href="https://www.boe.es/buscar/act.php?id=BOE-A-1995-24292" target="_blank" rel="noopener">Ley 31/1995 de Prevención de Riesgos Laborales</a>, <a href="https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430" target="_blank" rel="noopener">Estatuto de los Trabajadores</a>, <a href="https://www.boe.es/buscar/doc.php?id=BOE-A-2024-20402" target="_blank" rel="noopener">Real Decreto 1026/2024</a> y <a href="https://eur-lex.europa.eu/eli/reg/2024/1689/oj" target="_blank" rel="noopener">Reglamento (UE) 2024/1689</a>. Este artículo es informativo y no sustituye el asesoramiento laboral.</p>
"""),
("formacion-en-ia-desde-cero", "Formación en IA desde cero: qué curso elegir y cuánto cuesta",
 "Cómo empezar a formarte en inteligencia artificial sin conocimientos previos: tipos de cursos, opciones gratis, cuánto cuestan y cómo elegir el que de verdad te sirve.",
 "15 oct 2026", "Inteligencia artificial", "formacion-ia", _resp(
 "Para empezar en IA desde cero no hace falta saber programar. Lo más útil es un curso práctico que te enseñe a usar asistentes como ChatGPT, Gemini, Copilot o Claude en tus tareas reales. Hay opciones gratuitas para entender lo básico y formaciones de pago, individuales o para equipos, cuando quieres aplicarlo a tu trabajo.") + """
<p>La <b>formación en IA</b> se ha disparado y hay de todo: másteres técnicos, cursos rápidos, vídeos gratis y talleres para empresas. El primer paso es saber qué buscas.</p>
<h2>¿Qué tipos de formación en IA existen?</h2>
<ul><li><b>Formación de uso:</b> aprender a sacarle partido a las herramientas de IA en tu trabajo. Es la que necesita la mayoría.</li><li><b>Formación técnica:</b> programación, datos y modelos de IA. Para perfiles de desarrollo o ciencia de datos.</li><li><b>Formación estratégica:</b> para directivos que deciden dónde aplicar la IA en la empresa.</li><li><b>Formación normativa:</b> uso responsable, protección de datos y AI Act.</li></ul>
<h2>¿Qué diferencia hay entre la IA y ChatGPT?</h2>
<p>La inteligencia artificial es el campo completo; ChatGPT es una herramienta concreta de IA generativa, capaz de escribir, resumir o analizar texto. Gemini, Copilot y Claude son herramientas parecidas de otras empresas. Comparamos las cuatro en <a href="chatgpt-gemini-copilot-o-claude-para-empresas.html">qué IA usar en tu empresa</a>.</p>
<h2>¿Hay formación en IA gratis?</h2>
<p>Sí. Para entender los conceptos básicos hay cursos gratuitos de calidad, como <a href="https://www.elementsofai.com/es" target="_blank" rel="noopener">Elements of AI</a> (en español) o los módulos de <a href="https://learn.microsoft.com/es-es/training/" target="_blank" rel="noopener">Microsoft Learn</a>. Su límite: son generales y no se adaptan a tu negocio ni resuelven tus dudas concretas.</p>
<h2>¿Cuánto cuesta un curso de IA?</h2>
<p>Depende del formato. Los cursos grabados suelen ser los más baratos; las sesiones en directo, individuales o para equipos, cuestan más porque se adaptan a ti. Como referencia, nuestra <a href="../servicios/formacion-ia/sesion-de-ia-1-a-1.html">sesión de IA 1 a 1</a> cuesta desde 40 € la hora, y la formación para equipos se presupuesta según personas y horas. Si eres empresa, puedes recuperar parte con la <a href="formacion-bonificada-para-empresas-fundae.html">formación bonificada</a>.</p>
<h2>¿Cuál es el mejor curso de IA para principiantes?</h2>
<p>El que cumple estas cuatro condiciones:</p>
<ol><li><b>Es práctico:</b> sales sabiendo hacer algo, no solo entendiéndolo.</li><li><b>Usa tus tareas:</b> correos, propuestas, informes o atención al cliente de tu negocio.</li><li><b>Te dice qué no hacer:</b> qué datos no compartir y cómo revisar lo que la IA responde.</li><li><b>Tiene seguimiento:</b> alguien a quien preguntar cuando lo pones en práctica.</li></ol>
<h2>Un plan de 4 semanas para empezar</h2>
<ul><li><b>Semana 1:</b> un curso gratuito de conceptos básicos.</li><li><b>Semana 2:</b> elige un asistente y úsalo cada día para una tarea repetitiva.</li><li><b>Semana 3:</b> aprende a dar buenas instrucciones (contexto, ejemplo y formato).</li><li><b>Semana 4:</b> automatiza una tarea completa con ayuda, en una sesión práctica.</li></ul>
"""),
("chatgpt-gemini-copilot-o-claude-para-empresas", "ChatGPT, Gemini, Copilot o Claude: qué IA usar en tu empresa",
 "Comparativa práctica de los cuatro asistentes de IA más usados en empresas: en qué destaca cada uno, cómo encaja con tus herramientas y qué revisar sobre privacidad.",
 "15 oct 2026", "Inteligencia artificial", "formacion-ia", _resp(
 "No hay una IA mejor para todas las empresas. Lo que más pesa es con qué herramientas trabajas: si vives en Microsoft 365, Copilot encaja de forma natural; si usas Google Workspace, Gemini. ChatGPT y Claude son asistentes muy completos e independientes de tu paquete de oficina. Elige uno, forma al equipo en él y revisa las condiciones de privacidad del plan para empresas.") + """
<p>Es la pregunta que más nos hacen en las formaciones: <b>¿qué es mejor, ChatGPT o Gemini?</b>, ¿y Copilot?, ¿y Claude? Las cuatro son herramientas de IA generativa capaces de redactar, resumir, analizar documentos y ayudarte a pensar. Las diferencias están en cómo encajan con tu forma de trabajar.</p>
<h2>Las cuatro, en una tabla</h2>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Asistente</th><th>Empresa</th><th>Encaja mejor si…</th></tr></thead><tbody>
<tr><td>ChatGPT</td><td>OpenAI</td><td>Quieres un asistente generalista, muy conocido por el equipo, para redactar, analizar y crear asistentes propios.</td></tr>
<tr><td>Gemini</td><td>Google</td><td>Trabajas con Gmail, Drive, Docs y Sheets y quieres la IA dentro de esas herramientas.</td></tr>
<tr><td>Copilot</td><td>Microsoft</td><td>Tu empresa usa Outlook, Word, Excel y Teams (Microsoft 365).</td></tr>
<tr><td>Claude</td><td>Anthropic</td><td>Trabajas mucho con documentos largos, textos cuidados o análisis detallados.</td></tr></tbody></table></div>
<h2>Qué mirar antes de elegir</h2>
<ul><li><b>Tus herramientas actuales:</b> la IA que vive dentro de tu correo y tus documentos se usa más.</li><li><b>Privacidad de los datos:</b> usa los planes para empresas y revisa en su contrato si tus datos se usan para entrenar modelos y dónde se procesan.</li><li><b>Control de accesos:</b> poder dar y quitar usuarios cuando alguien entra o se va.</li><li><b>Coste por usuario:</b> no hace falta que todo el mundo tenga la versión de pago desde el primer día.</li></ul>
<h2>¿Puedo usar varias a la vez?</h2>
<p>Se puede, pero en una empresa pequeña suele ser mejor <b>elegir una como herramienta oficial</b>. Así la formación, las normas de uso y las instrucciones guardadas sirven para todos. Si alguien necesita otra para una tarea concreta, se valora caso a caso.</p>
<h2>La herramienta importa menos que la formación</h2>
<p>Un equipo bien formado saca partido a cualquiera de las cuatro; uno sin formación no aprovecha ninguna. Por eso en nuestra <a href="../servicios/formacion-ia.html">formación en IA para empresas</a> trabajamos con la herramienta que ya tengáis y la ajustamos a las tareas de cada área. Si estás empezando, lee antes <a href="formacion-en-ia-desde-cero.html">formación en IA desde cero</a>.</p>
<p class="mut" style="font-size:14px">Las funciones y los planes de estas herramientas cambian a menudo. Comprueba las condiciones vigentes en la web de cada proveedor antes de contratar.</p>
"""),
]

FAQS = {
"formacion-bonificada-para-empresas-fundae": [
 ("¿Qué es la formación bonificada?", "Es la formación que la empresa da a su plantilla y cuyo coste recupera descontándolo de las cotizaciones a la Seguridad Social, con el crédito anual que gestiona FUNDAE."),
 ("¿Cuánto se puede bonificar una empresa en formación?", "Depende de lo que cotizó por formación profesional el año anterior y de su tamaño: del 100 % en empresas de hasta 9 personas al 50 % en las de 250 o más. Las de 1 a 5 personas tienen un mínimo de 420 € al año."),
 ("¿Quién paga la formación de un trabajador?", "La empresa, que después puede recuperar el coste con su crédito de formación si cumple los requisitos de comunicación y justificación."),
 ("¿Se puede bonificar un curso de IA o de Excel?", "Sí, si está relacionado con la actividad de la empresa y se comunica a FUNDAE antes de empezar."),
],
"plan-de-formacion-para-empresas": [
 ("¿Qué es un plan de formación en una empresa?", "Es el documento que organiza la formación del año: qué necesita aprender cada puesto, con qué objetivo, en qué formato, cuándo y con qué presupuesto."),
 ("¿Qué tipos de formación existen en las empresas?", "Formación obligatoria por ley, formación técnica del puesto, formación en herramientas y procesos propios, formación de acogida para nuevos empleados y desarrollo de habilidades."),
 ("¿Cada cuánto se revisa el plan?", "Lo normal es hacerlo una vez al año y revisarlo a mitad de ejercicio para ajustar prioridades."),
],
"formacion-obligatoria-en-empresas": [
 ("¿Es obligatoria la formación en las empresas?", "Sí en varios casos: prevención de riesgos laborales en todas, y según tamaño y actividad, igualdad, LGTBI, protección de datos, manipulación de alimentos o alfabetización en IA."),
 ("¿Puede la empresa obligarme a hacer cursos de formación?", "Puede exigir la formación necesaria para el puesto y la obligatoria por ley. La de prevención de riesgos debe hacerse en horario laboral o descontarse de la jornada, y sin coste para el trabajador."),
 ("¿Los cursos de prevención de riesgos se hacen en horario laboral?", "Sí: la Ley 31/1995 establece que se impartan dentro de la jornada o, si no es posible, en otras horas descontando ese tiempo de la jornada."),
 ("¿Qué son las 20 horas de formación?", "Un permiso retribuido de 20 horas al año para formación vinculada al puesto, para trabajadores con al menos un año de antigüedad, acumulable hasta cinco años (art. 23.3 del Estatuto de los Trabajadores)."),
],
"formacion-en-ia-desde-cero": [
 ("¿Cuánto cuestan los cursos de IA?", "Hay cursos gratuitos de conceptos básicos y cursos de pago desde precios bajos si son grabados. Las sesiones en directo y personalizadas cuestan más; la nuestra individual es desde 40 € la hora."),
 ("¿Dónde hacer un curso de IA gratis?", "Elements of AI (en español) y Microsoft Learn ofrecen formación gratuita para entender lo básico."),
 ("¿Hace falta saber programar para aprender IA?", "No para usarla en el trabajo. Solo la formación técnica, orientada a crear modelos o aplicaciones, requiere programación."),
 ("¿Qué tipo de IA es ChatGPT?", "Es una IA generativa basada en un modelo de lenguaje: genera texto a partir de las instrucciones que le das."),
],
"chatgpt-gemini-copilot-o-claude-para-empresas": [
 ("¿Qué es mejor, ChatGPT o Gemini?", "Depende de tus herramientas: Gemini encaja mejor si trabajas con Google Workspace y ChatGPT es un asistente generalista independiente. Las dos sirven para la mayoría de tareas de oficina."),
 ("¿Cuáles son las IA más usadas en empresas?", "Entre las más extendidas están ChatGPT, Microsoft Copilot, Google Gemini y Claude."),
 ("¿Es seguro meter datos de la empresa en una IA?", "Usa planes para empresas, revisa si tus datos se usan para entrenar y define por escrito qué información no se comparte nunca."),
 ("¿Hace falta formar al equipo para usar estas herramientas?", "Sí. Sin formación se usan para poco y con riesgos; con formación práctica se convierten en ahorro real de tiempo."),
],
}

ALT = {
"formacion-bonificada-para-empresas-fundae": "Responsable de RRHH revisando en el portátil el crédito de formación bonificada de la empresa",
"plan-de-formacion-para-empresas": "Directora y responsable de equipo planificando el calendario anual de formación de la empresa",
"formacion-obligatoria-en-empresas": "Formadora impartiendo un curso obligatorio a un grupo de empleados en la sala de reuniones",
"formacion-en-ia-desde-cero": "Persona aprendiendo inteligencia artificial desde cero con un curso online en el portátil",
"chatgpt-gemini-copilot-o-claude-para-empresas": "Portátil, tablet y móvil con distintos asistentes de IA abiertos para compararlos",
}
