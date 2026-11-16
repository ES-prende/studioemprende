# Reescritura «dolores primero» · familia Grandes empresas (noviembre 2026).
# Lector: responsable de área o de sistemas. Tono algo más sobrio, mismo enfoque de problema real. Sin precios.
D = {}

# Estructura: tabla «lo que dijo cada área tras el curso general / lo que necesitaba» + señales de que no caló + qué preparar antes de pedir propuesta
D["servicios/grandes-empresas/formacion-in-company-por-departamentos"] = {
 "estructura": "tabla-reaccion-de-cada-area-al-curso-general + senales-de-que-no-calo + que-preparar-antes-de-pedir-propuesta",
 "lead": "Se organizó una jornada de inteligencia artificial para toda la plantilla, la valoración fue buena y, dos meses después, casi nadie ha cambiado su forma de trabajar. Cada área salió con la misma duda: «¿y esto para lo mío?». La formación en IA in company por departamentos parte de esa pregunta.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Buena nota en la encuesta, ningún cambio en el puesto</p><h2>¿Por qué la formación general en IA no llega al trabajo diario?</h2></div>
<p style="max-width:820px">Porque enseña la herramienta y no la tarea. Un curso igual para todos tiene que quedarse en ejemplos neutros, y un ejemplo neutro no se parece al expediente, al pedido o a la reclamación que cada persona tiene delante el lunes. Quien no ve su propio trabajo en la pantalla concluye que aquello es interesante pero no va con él.</p>
<div class="tabla-wrap" style="margin-top:22px"><table class="tabla-norm"><thead><tr><th>Área</th><th>Lo que suele decir al salir</th><th>Lo que necesitaba ver</th></tr></thead><tbody>
<tr><td>Comercial</td><td>«Para escribir correos ya me apaño»</td><td>Cómo preparar una visita con el historial del cliente en diez minutos</td></tr>
<tr><td>Finanzas</td><td>«No puedo fiarme de un número que no sé de dónde sale»</td><td>Usos donde la IA propone y la persona comprueba, con sus propias conciliaciones</td></tr>
<tr><td>Personas</td><td>«Con datos de empleados, ni tocarlo»</td><td>Qué se puede hacer sin datos personales y qué no debe hacerse nunca</td></tr>
<tr><td>Operaciones</td><td>«Nosotros no estamos delante de un ordenador»</td><td>Casos con partes, incidencias y procedimientos desde el móvil</td></tr>
<tr><td>Mandos intermedios</td><td>«¿Y cómo sé qué puedo autorizar?»</td><td>Criterios para aprobar o frenar un uso en su equipo</td></tr>
</tbody></table></div>
<h3 style="margin-top:30px">Señales de que la formación anterior no caló</h3>
<ul class="lista" style="max-width:820px">
<li>Las licencias corporativas se usan mucho menos de lo que se paga.</li>
<li>La gente sigue recurriendo a cuentas personales porque «la de la empresa no sé para qué sirve».</li>
<li>Los mismos tres entusiastas resuelven las dudas de toda su planta.</li>
<li>Nadie sabría enumerar qué datos no deben introducirse.</li>
</ul>
<h3 style="margin-top:30px">Qué conviene tener a mano antes de pedir propuesta</h3>
<ol style="max-width:820px">
<li>El listado de áreas y el número aproximado de personas de cada una.</li>
<li>Las herramientas de IA que la empresa ha autorizado, y las que sabes que se usan sin autorizar.</li>
<li>La política de uso, si existe. Si no existe, conviene escribirla antes o a la vez.</li>
<li>Dos o tres tareas por área que consuman tiempo y sean repetitivas.</li>
</ol>
<p style="max-width:820px">Con eso se diseñan sesiones que cada equipo reconoce como suyas. No prometemos un porcentaje de adopción: depende de que los mandos den tiempo para practicar y de que las herramientas estén disponibles al día siguiente. Las reglas del juego se fijan con la <a href="/servicios/grandes-empresas/gobernanza-de-ia">gobernanza de IA</a>; la parte de alfabetización exigible la detallamos en la <a href="/servicios/formacion-ia/formacion-obligatoria-ai-act">formación en IA por el AI Act</a>, y para el comité de dirección existe una <a href="/servicios/formacion-ia/mentoria-para-directivos">mentoría para directivos</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo conseguir que los empleados usen de verdad la IA después de un curso?", "Formando con tareas reales de su puesto, dejando las herramientas disponibles desde el día siguiente y reservando tiempo para practicar. Ayuda que cada mando acuerde con su equipo uno o dos usos concretos y los revise al cabo de unas semanas."),
  ("¿Qué pasa si en la empresa hay niveles muy distintos de conocimiento de IA?", "Se hacen grupos por nivel dentro de cada área, con un diagnóstico previo breve. Quien empieza de cero necesita confianza y casos sencillos; quien ya la usa aprovecha mejor sesiones sobre automatización y límites."),
 ],
}

# Estructura: preguntas incómodas del comité (ol) + rejilla de tres reacciones habituales y su coste + por dónde empezar con poco
D["servicios/grandes-empresas/gobernanza-de-ia"] = {
 "estructura": "preguntas-incomodas-del-comite + rejilla-tres-reacciones-y-su-coste + empezar-con-poco",
 "lead": "Marketing ha contratado un generador de contenidos, atención al cliente prueba un chatbot y media plantilla usa asistentes con su cuenta personal. Cuando el comité pregunta quién ha autorizado todo eso, nadie tiene la respuesta completa. La gobernanza de IA en la empresa, con reglas y control, existe para poder darla.",
 "bloque": """<section class="sec sec-suave"><div class="w">
<div class="cab"><p class="kicker">Muchos usos, ningún mapa</p><h2>¿Quién decide qué IA se usa en la empresa y con qué datos?</h2></div>
<p style="max-width:820px">En muchas organizaciones, hoy, cada departamento por su cuenta. No hay mala fe: las herramientas son baratas, se contratan con una tarjeta y resuelven un problema inmediato. El responsable de sistemas se entera cuando alguien pide integrar algo; el área jurídica, cuando llega un contrato. Estas son las preguntas que antes o después llegan a la mesa de dirección.</p>
<ol style="max-width:820px">
<li>¿Cuántos sistemas de IA estamos usando y quién contrató cada uno?</li>
<li>¿En cuáles se introducen datos de clientes, de empleados o información confidencial?</li>
<li>¿Hay alguna decisión sobre personas en la que influya un sistema automático?</li>
<li>Si una respuesta generada causa un perjuicio, ¿quién responde internamente?</li>
<li>¿Podríamos reconstruir qué hizo un agente hace tres meses?</li>
</ol>
<p style="max-width:820px">Si para contestar hay que convocar a seis personas, falta gobierno, no tecnología.</p>
<h3 style="margin-top:30px">Tres reacciones habituales y lo que cuestan</h3>
<div class="rejilla">
<div class="tarjeta"><h3>Prohibirlo todo</h3><p>Tranquiliza un mes. Después el uso continúa, pero escondido y sin ningún control.</p></div>
<div class="tarjeta"><h3>Dejar hacer</h3><p>Avanza rápido hasta el primer incidente, y entonces se frena todo de golpe.</p></div>
<div class="tarjeta"><h3>Un comité que lo revisa todo</h3><p>Cada petición tarda semanas, los equipos dejan de preguntar y vuelven a contratar por su cuenta.</p></div>
</div>
<p style="max-width:820px;margin-top:20px">Una gobernanza útil se sitúa entre las tres: vía rápida para lo de bajo riesgo, revisión seria para lo que toca a personas o a datos sensibles, y un registro que permita saber qué hay.</p>
<h3 style="margin-top:30px">Se puede empezar con poco</h3>
<p style="max-width:820px">No hace falta un programa de un año para dar el primer paso. Un inventario honesto, una persona responsable por sistema y una lista corta de usos permitidos y vetados ya cambian la conversación con dirección. Lo demás se construye encima.</p>
<p style="max-width:820px">Este trabajo es organizativo y técnico; la interpretación jurídica de cada caso corresponde a tu asesoría legal, con la que nos coordinamos. Para la norma escrita que lee la plantilla, mira la <a href="/servicios/formacion-ia/politica-de-uso-de-ia-para-empresas">política de uso de IA</a>. Para comprobar que un agente respeta lo acordado antes de abrirlo, las <a href="/servicios/grandes-empresas/pruebas-de-agentes-ia">pruebas de agentes IA</a>. Y si la preocupación es que la información no salga de la casa, la <a href="/servicios/agentes-de-ia/ia-con-los-datos-de-tu-empresa-sin-que-salgan-fuera">IA con los datos de tu empresa sin que salgan fuera</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo hacer un inventario de los usos de IA en una empresa grande?", "Combinando tres fuentes: una encuesta breve a los responsables de área, la revisión de contratos y suscripciones, y el análisis de qué funciones de IA traen activadas los programas corporativos. Cada uso se anota con su finalidad, sus datos y su responsable."),
  ("¿Quién debe ser responsable de la IA en la empresa?", "Depende de la organización, pero suele funcionar un responsable global que coordina y un responsable de negocio por cada sistema. Sistemas, jurídico y protección de datos participan en la revisión de los usos de mayor riesgo."),
 ],
}

# Estructura: objeciones del responsable de sistemas con su respuesta (dl) + lo que no haríamos + cierre con enlaces
D["servicios/grandes-empresas/ia-conectada-a-erp-y-sistemas-antiguos"] = {
 "estructura": "objeciones-del-responsable-de-sistemas-en-glosario + lo-que-no-hariamos",
 "lead": "Negocio quiere un agente que consulte pedidos y stock «como en la demo», y el dato vive en un ERP con veinte años, tablas con nombres crípticos y una persona que lo entiende. El fabricante propone migrar primero. Conectar IA al ERP y a sistemas antiguos (legacy) es posible sin esa migración, con condiciones.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Entre la prisa de negocio y la prudencia de sistemas</p><h2>¿Se puede poner IA encima de un ERP antiguo sin arriesgar la operación?</h2></div>
<p style="max-width:820px">Se puede, si el sistema central se trata como lo que es: la pieza que no puede fallar. Quien lleva sistemas suele ser la única persona de la sala que ha visto lo que pasa cuando algo escribe mal en producción, y sus reservas merecen respuesta concreta, no entusiasmo. Estas son las más frecuentes.</p>
<dl style="max-width:820px">
<dt><strong>«No voy a dar acceso a la base de datos a algo que no controlo.»</strong></dt><dd>No se le da. El agente consulta a través de una capa intermedia con operaciones definidas y, al principio, solo de lectura.</dd>
<dt><strong>«El ERP ya va justo de rendimiento.»</strong></dt><dd>Las consultas se dirigen a una réplica o a extracciones programadas, no al sistema en vivo, cuando la carga lo aconseja.</dd>
<dt><strong>«Nadie sabe ya qué significa cada campo.»</strong></dt><dd>Es el trabajo previo más importante: documentar con quien lo conoce las tablas que se van a usar, y solo esas.</dd>
<dt><strong>«¿Y si se inventa un dato?»</strong></dt><dd>Las cifras se leen del sistema, no se generan. El modelo redacta y decide qué consultar; el número sale de la fuente y queda registrado.</dd>
<dt><strong>«Cuando cambiemos de ERP habrá que tirarlo.»</strong></dt><dd>La capa intermedia aísla al agente del sistema: al cambiar el ERP se rehace la conexión, no el agente.</dd>
<dt><strong>«Soporte del fabricante nos dirá que eso no está cubierto.»</strong></dt><dd>Por eso se revisa el contrato de mantenimiento antes y se eligen vías que el fabricante admite.</dd>
</dl>
<p style="max-width:820px;margin-top:18px">Con estas condiciones, el primer agente suele ser poco vistoso y muy útil: contesta preguntas sobre pedidos, existencias o estados que hoy alguien busca pantalla a pantalla.</p>
<h3 style="margin-top:30px">Lo que no haríamos</h3>
<ul class="lista" style="max-width:820px">
<li>Dar permisos de escritura el primer día, por mucho que apriete el calendario.</li>
<li>Conectar sin el visto bueno de la persona responsable del sistema.</li>
<li>Automatizar pantallas cuando existe una vía más estable, aunque sea más lenta de montar.</li>
<li>Prometer que no habrá incidencias: habrá ajustes, y por eso cada operación queda en un registro.</li>
</ul>
<p style="max-width:820px;margin-top:18px">Si los datos del ERP arrastran duplicados o códigos incoherentes, conviene pasar antes por la <a href="/servicios/grandes-empresas/preparacion-de-datos-para-ia">preparación de datos para IA</a>. Una forma prudente de empezar es acotar un caso en un <a href="/servicios/grandes-empresas/piloto-de-agente-ia-en-30-60-dias">piloto de agente de IA</a>. Y si la política interna impide que la información salga de vuestra infraestructura, existe la opción de <a href="/servicios/agentes-de-ia/ia-en-servidor-propio">IA en servidor propio</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo evitar que un agente de IA modifique datos del ERP por error?", "Empezando con acceso de solo lectura y, cuando se permita escribir, limitándolo a operaciones concretas con validaciones y aprobación humana. Cada acción queda registrada para poder revisarla y deshacerla."),
  ("¿Qué pasa con la conexión de IA si más adelante migramos de ERP?", "Si se ha construido con una capa intermedia, el agente no depende del sistema concreto. Al migrar se adapta esa capa al nuevo ERP y el resto, incluidas las reglas y las pruebas, se conserva."),
  ("¿Quién debe participar en un proyecto de IA sobre un sistema heredado?", "Como mínimo, la persona responsable del sistema, alguien de negocio que conozca el proceso y un responsable de seguridad o de datos. Sin el conocimiento de quien mantiene el sistema, el riesgo de interpretar mal un campo es alto."),
 ],
}

# Estructura: frase del cliente en una reunión (blockquote) + tabla de cuatro salidas posibles + qué mirar antes de firmar con cualquier proveedor de marca blanca
D["servicios/grandes-empresas/marca-blanca-para-consultoras"] = {
 "estructura": "frase-del-cliente-en-reunion + tabla-cuatro-salidas + que-mirar-antes-de-firmar",
 "lead": "Llevas años con un cliente al que conoces bien y en la última reunión te pregunta si «vosotros hacéis algo de inteligencia artificial». Tu consultora no tiene equipo técnico. Si dices que no, se lo preguntará a otro. La IA en marca blanca para consultoras y agencias te permite decir que sí sin improvisar.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">La pregunta que llega al final de la reunión</p><h2>Mis clientes me piden IA y no tengo equipo técnico: ¿qué opciones hay?</h2></div>
<blockquote style="max-width:820px"><p>«Oye, una cosa más: lo de los agentes de IA, ¿eso lo lleváis vosotros o tengo que buscar a alguien?»</p></blockquote>
<p style="max-width:820px;margin-top:18px">Quien pregunta así no quiere otro proveedor; quiere que lo resuelvas tú, que ya conoces su negocio. La respuesta que des en ese momento decide algo más que un proyecto: decide si sigues siendo su asesor de referencia o pasas a compartir la cuenta con otra firma.</p>
<h3 style="margin-top:30px">Cuatro salidas y lo que implica cada una</h3>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Opción</th><th>Ventaja</th><th>Riesgo</th></tr></thead><tbody>
<tr><td>Decir que no es vuestra especialidad</td><td>Honesto y sin compromiso</td><td>El cliente abre la puerta a un tercero que puede ofrecerle también lo vuestro</td></tr>
<tr><td>Contratar un perfil técnico</td><td>Capacidad propia</td><td>Coste fijo antes de tener cartera, y una sola persona no cubre diseño, desarrollo y soporte</td></tr>
<tr><td>Recomendar a un proveedor</td><td>Rápido</td><td>Pierdes visibilidad del proyecto y control sobre la calidad</td></tr>
<tr><td>Entregarlo con tu marca y un equipo detrás</td><td>Mantienes la relación y decides el alcance</td><td>Respondes ante el cliente: necesitas confiar en quien ejecuta</td></tr>
</tbody></table></div>
<p style="max-width:820px;margin-top:20px">La cuarta es la que tratamos aquí, y no vale para todas las firmas. Encaja cuando tu valor está en conocer el sector y el proceso del cliente; encaja peor si esperas vender algo que no vas a entender ni a supervisar.</p>
<h3 style="margin-top:30px">Qué mirar antes de firmar con cualquier proveedor de marca blanca</h3>
<ol style="max-width:820px">
<li><strong>Confidencialidad y no captación</strong>, por escrito y con nombre de cliente.</li>
<li><strong>Propiedad</strong> de lo desarrollado y qué ocurre si la relación termina.</li>
<li><strong>Quién atiende las incidencias</strong>, en qué plazo y por qué canal.</li>
<li><strong>Dónde se alojan los datos</strong> del cliente final y quién accede a ellos.</li>
<li><strong>Qué puedes prometer y qué no</strong>: pide por adelantado los límites de cada solución.</li>
</ol>
<p style="max-width:820px">Aplícanos la misma lista a nosotros. Y un límite que conviene decir pronto: no venderemos a tu cliente algo que no esté probado; si un caso no es viable, te lo diremos a ti antes de que lo ofrezcas.</p>
<p style="max-width:820px">Para acotar el primer proyecto con poco riesgo sirve el formato de <a href="/servicios/grandes-empresas/piloto-de-agente-ia-en-30-60-dias">piloto de 30 a 60 días</a>. Si tus clientes son despachos o asesorías, hay un producto pensado para ellos, el <a href="/servicios/software-especializado/portal-en-marca-blanca-para-gestorias">portal en marca blanca para gestorías</a>. Las condiciones de colaboración están en la página de <a href="/partners">partners</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo puede una consultora ofrecer servicios de IA sin contratar programadores?", "Apoyándose en un equipo técnico externo que trabaje bajo su marca. La consultora aporta el conocimiento del cliente y del sector, define el alcance y supervisa; el equipo construye y mantiene la solución."),
  ("¿Qué pasa si el cliente final descubre que hay un proveedor detrás?", "Depende de lo que hayas acordado con él. La subcontratación técnica es habitual en consultoría; muchos contratos la permiten si se mantiene la confidencialidad. Conviene revisar qué dice tu contrato con el cliente antes de empezar."),
 ],
}

# Estructura: tres causas por las que mueren los pilotos (h3 narrativos) + segunda sección con las respuestas que hay que tener antes de empezar
D["servicios/grandes-empresas/piloto-de-agente-ia-en-30-60-dias"] = {
 "estructura": "tres-causas-por-las-que-mueren-los-pilotos + segunda-seccion-respuestas-previas",
 "lead": "La empresa lleva un año haciendo pruebas de concepto con inteligencia artificial: demostraciones que gustan, presentaciones al comité y ningún proceso que funcione distinto. Dirección empieza a preguntar qué se ha sacado. Un piloto de agente de IA para empresas en 30-60 días está diseñado para acabar con una decisión.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">De la demostración al proceso</p><h2>¿Por qué las pruebas de IA no pasan de la prueba?</h2></div>
<p style="max-width:820px">Porque se plantean para enseñar que la tecnología funciona, y eso ya se sabe. Lo que una organización necesita averiguar es otra cosa: si funciona aquí, con estos datos, estas personas y este proceso, y si compensa. Los pilotos que se quedan en el cajón suelen fallar por una de estas tres razones.</p>
<h3 style="margin-top:26px">No había una cifra con la que comparar</h3>
<p style="max-width:820px">Se empezó sin medir cuánto tarda hoy la tarea ni cuántos errores tiene. Al terminar, unos opinan que ha ido bien y otros que no, y ninguna de las dos posturas se puede demostrar.</p>
<h3 style="margin-top:26px">Nadie de negocio lo sentía suyo</h3>
<p style="max-width:820px">Lo impulsó innovación o sistemas, y el área que debía usarlo lo vivió como un encargo ajeno. Sin un responsable del proceso que quiera el resultado, el agente se queda sin quien lo defienda.</p>
<h3 style="margin-top:26px">Se probó con datos de laboratorio</h3>
<p style="max-width:820px">Con diez documentos limpios todo sale bien. Con el archivo real, sus versiones duplicadas y sus excepciones, aparece el trabajo de verdad, y aparece tarde.</p>
</div></section>
<section class="sec sec-suave"><div class="w">
<h3>Cuatro respuestas que conviene tener antes del primer día</h3>
<ul class="lista" style="max-width:820px">
<li><strong>¿Qué proceso, exactamente?</strong> Uno, acotado, con volumen suficiente para medir en pocas semanas.</li>
<li><strong>¿Quién es su dueño?</strong> Una persona de negocio con nombre y con tiempo reservado.</li>
<li><strong>¿Qué número queremos mover y cuánto vale hoy?</strong> Tiempo por caso, casos resueltos sin intervención, errores.</li>
<li><strong>¿Qué haremos según el resultado?</strong> Decidir de antemano qué significa ampliar, ajustar o parar evita discutirlo después.</li>
</ul>
<p style="max-width:820px;margin-top:18px">Un piloto bien planteado puede terminar en «no compensa», y ese también es un buen resultado: se ha sabido en semanas y con un gasto acotado. Lo que no entregamos es una promesa de retorno antes de empezar; la estimación se hace con los datos del propio piloto. Si al definir el caso se ve que la documentación no está en condiciones, lo primero es la <a href="/servicios/grandes-empresas/preparacion-de-datos-para-ia">preparación de datos para IA</a>. Antes de abrir el agente a usuarios pasa por las <a href="/servicios/grandes-empresas/pruebas-de-agentes-ia">pruebas de agentes IA</a>, y cuando se decide escalar hace falta prever su <a href="/servicios/agentes-de-ia/mantenimiento-de-agentes-y-automatizaciones">mantenimiento</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo elegir el primer caso de uso de IA en una empresa?", "Buscando un proceso repetitivo, con volumen, con datos accesibles y con un responsable que quiera mejorarlo. Conviene evitar para empezar los procesos críticos o los que dependen de integraciones complejas."),
  ("¿Cómo justificar ante dirección la inversión en un agente de IA?", "Con una medición previa del proceso y los resultados del piloto sobre esa misma métrica, más el coste estimado de operar el agente a escala. Presentar ambos lados, incluido lo que no ha funcionado, da más credibilidad que una proyección optimista."),
 ],
}

# Estructura: situación hipotética + síntomas en lista + tabla de comprobación «pregunta / si la respuesta es no» + no hace falta ordenarlo todo
D["servicios/grandes-empresas/preparacion-de-datos-para-ia"] = {
 "estructura": "situacion-hipotetica + sintomas + tabla-de-comprobacion-previa + no-hace-falta-ordenarlo-todo",
 "lead": "El asistente interno contesta con seguridad y cita un procedimiento derogado hace dos años, porque seguía en la carpeta compartida junto al vigente. Nadie le dijo cuál era el bueno. La preparación de datos para IA en empresas grandes resuelve ese problema antes de que lo vea un empleado o un cliente.",
 "bloque": """<section class="sec sec-suave"><div class="w">
<div class="cab"><p class="kicker">El agente no se equivoca solo</p><h2>¿Por qué la IA responde mal si le hemos dado toda nuestra documentación?</h2></div>
<p style="max-width:820px">Precisamente por eso: porque se le ha dado toda. Imagina una empresa con varias sedes que conecta un asistente a su gestor documental. Dentro hay cuatro versiones de la misma tarifa, actas con datos personales, borradores que nunca se aprobaron y manuales de un sistema que ya no existe. El asistente no distingue lo vigente de lo antiguo; para él todo es texto igual de válido.</p>
<ul class="lista" style="max-width:820px">
<li>Da respuestas distintas a la misma pregunta según cómo se formule.</li>
<li>Cita documentos que el equipo sabe que están superados.</li>
<li>Muestra a una persona información de otra área que no debería ver.</li>
<li>Los usuarios dejan de fiarse a la segunda semana y vuelven a preguntar al compañero.</li>
</ul>
<h3 style="margin-top:30px">Comprobación previa: seis preguntas para el responsable de la información</h3>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Pregunta</th><th>Si la respuesta es «no»</th></tr></thead><tbody>
<tr><td>¿Sabemos dónde están las fuentes que el agente necesita?</td><td>Empieza por un inventario; puede haber repositorios que nadie recuerda</td></tr>
<tr><td>¿Cada documento tiene una versión vigente identificable?</td><td>Hay que marcarla o retirar las anteriores del alcance</td></tr>
<tr><td>¿Los permisos de las carpetas reflejan quién debe ver qué?</td><td>El agente heredará esos fallos y los hará visibles</td></tr>
<tr><td>¿Sabemos qué documentos contienen datos personales?</td><td>Conviene localizarlos y decidir si entran, se anonimizan o se excluyen</td></tr>
<tr><td>¿Alguien es dueño de mantener cada fuente?</td><td>Sin responsable, el orden dura lo que dure el proyecto</td></tr>
<tr><td>¿Los documentos escaneados son legibles como texto?</td><td>Hay que reconocer el texto antes de indexarlos</td></tr>
</tbody></table></div>
<p style="max-width:820px;margin-top:20px">Dos o tres respuestas negativas no impiden empezar; indican por dónde.</p>
<h3 style="margin-top:30px">No hace falta ordenar toda la empresa</h3>
<p style="max-width:820px">El error contrario al de «conectarlo todo» es querer un proyecto de calidad de datos de dos años antes de usar nada. Se prepara lo que necesita el primer caso de uso: un departamento, un tipo de documento, un conjunto de tablas. Lo aprendido ahí sirve de método para lo siguiente.</p>
<p style="max-width:820px">Tampoco es un trabajo puramente técnico. Decidir cuál es la versión buena de un procedimiento es una decisión de negocio; nosotros la preparamos y la documentamos, pero la toma quien responde del contenido. El marco de quién decide qué lo da la <a href="/servicios/grandes-empresas/gobernanza-de-ia">gobernanza de IA</a>. Si la fuente principal es un sistema central antiguo, mira <a href="/servicios/grandes-empresas/ia-conectada-a-erp-y-sistemas-antiguos">IA conectada a ERP y sistemas heredados</a>. Y si parte del conocimiento sigue en archivadores, la <a href="/servicios/migraciones-e-integraciones/digitalizacion-de-archivo-en-papel">digitalización de archivo en papel</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo evitar que un asistente de IA use documentos desactualizados?", "Retirando del alcance las versiones antiguas o marcando de forma explícita cuál está vigente, y asignando a alguien la tarea de mantenerlo. El agente debe citar el documento y la fecha de cada respuesta para que el usuario pueda comprobarlo."),
  ("¿Qué pasa si conectamos la IA a toda la documentación sin prepararla?", "Lo habitual es que mezcle versiones, dé respuestas contradictorias y pueda mostrar información a quien no tiene permiso para verla. La consecuencia práctica es que los usuarios pierden la confianza en la herramienta."),
 ],
}

# Estructura: cuatro preguntas del comité en rejilla + lo que una prueba no puede prometer + qué aportar para empezar (ol)
D["servicios/grandes-empresas/pruebas-de-agentes-ia"] = {
 "estructura": "rejilla-cuatro-preguntas-del-comite + lo-que-una-prueba-no-promete + que-aportar-para-empezar",
 "lead": "El agente está construido, la demostración interna salió bien y falta la firma de quien autoriza abrirlo a clientes. Esa persona pregunta qué pasa si alguien le pide algo indebido, y nadie tiene una respuesta mejor que «en las pruebas no ocurrió». Las pruebas de agentes IA antes de ponerlos en producción convierten esa frase en un informe.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Quién firma que puede salir</p><h2>¿Cómo sé que un agente de IA está listo para atender a clientes?</h2></div>
<p style="max-width:820px">No lo sabes por haberlo visto funcionar veinte veces. Una demostración enseña lo que el agente hace cuando se le pregunta lo previsto; lo que preocupa a quien responde del servicio es lo imprevisto. Antes de aprobar un despliegue, un comité razonable hará preguntas como estas, y conviene llegar con algo más que confianza.</p>
<div class="rejilla">
<div class="tarjeta"><h3>¿Qué hace cuando no sabe?</h3><p>Lo deseable es que lo diga y derive. Lo peligroso es que complete el hueco con algo verosímil.</p></div>
<div class="tarjeta"><h3>¿Puede hacer algo que no debería?</h3><p>Consultar datos de otro cliente, aplicar un descuento, cancelar un servicio sin verificar la identidad.</p></div>
<div class="tarjeta"><h3>¿Se le puede convencer para saltarse las reglas?</h3><p>Con insistencia, con un texto pegado en la conversación o haciéndose pasar por un empleado.</p></div>
<div class="tarjeta"><h3>¿Seguirá igual tras la próxima actualización?</h3><p>Un cambio en las instrucciones o en el modelo puede arreglar una cosa y estropear otra.</p></div>
</div>
<p style="max-width:820px;margin-top:20px">Cada pregunta se traduce en casos concretos que se lanzan al agente y cuyo resultado se anota. Lo que antes era una impresión pasa a ser una tabla: cuántos casos, cuántos correctos, cuáles fallan y con qué gravedad.</p>
<h3 style="margin-top:30px">Lo que una batería de pruebas no puede prometer</h3>
<p style="max-width:820px">Ninguna prueba demuestra que un agente no fallará. Demuestra cómo se comporta ante los casos que se han pensado, y reduce las sorpresas en proporción a lo bien elegidos que estén. Por eso el informe distingue lo comprobado de lo no cubierto, y por eso recomendamos abrir de forma gradual y con supervisión, aunque el resultado sea bueno. Tampoco evaluamos el cumplimiento legal del servicio; aportamos evidencia técnica para quien deba valorarlo.</p>
<h3 style="margin-top:30px">Qué aportar para empezar</h3>
<ol style="max-width:820px">
<li>Acceso al agente en un entorno que no sea el de producción.</li>
<li>La descripción de lo que debe y no debe hacer, tal como se aprobó.</li>
<li>Una muestra de conversaciones o peticiones reales, sin datos personales.</li>
<li>La lista de acciones que puede ejecutar en otros sistemas.</li>
<li>La persona que decidirá qué fallos bloquean la salida.</li>
</ol>
<p style="max-width:820px">Las reglas contra las que se prueba salen de la <a href="/servicios/grandes-empresas/gobernanza-de-ia">gobernanza de IA</a> de la organización. Si el agente aún no existe, el formato para construirlo y medirlo es el <a href="/servicios/grandes-empresas/piloto-de-agente-ia-en-30-60-dias">piloto en 30-60 días</a>. Una vez desplegado, las pruebas se repiten dentro del <a href="/servicios/agentes-de-ia/mantenimiento-de-agentes-y-automatizaciones">mantenimiento de agentes y automatizaciones</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo comprobar que un chatbot de IA no da información falsa a los clientes?", "Preparando un conjunto de preguntas con su respuesta correcta conocida, incluidas algunas que el agente no debería poder contestar, y comparando sus respuestas una a una. Se mide cuántas acierta, cuántas inventa y si reconoce cuándo no sabe."),
  ("¿Quién debe aprobar la puesta en producción de un agente de IA?", "El responsable del servicio o proceso afectado, con el informe de pruebas delante y, según el caso, la opinión de seguridad, protección de datos y jurídico. Conviene dejar por escrito qué fallos se consideran bloqueantes antes de empezar a probar."),
  ("¿Qué pasa si un agente de IA comete un error grave con un cliente?", "Se detiene la función afectada, se analiza la conversación con el registro, se corrige y se añade ese caso a la batería de pruebas para que no se repita. Tener previsto ese procedimiento forma parte de estar preparado para salir."),
 ],
}

# Estructura: frases que se oyen en la reunión de resultados + tabla «lo que ya mides / lo que no te cuenta» + límites en lista
D["servicios/grandes-empresas/voz-del-cliente-con-ia"] = {
 "estructura": "frases-de-la-reunion-de-resultados + tabla-lo-que-mides-y-lo-que-no-cuenta + limites-en-lista",
 "lead": "La nota de satisfacción ha bajado tres décimas y en la reunión cada área tiene su explicación: operaciones culpa a la web, producto a los plazos, atención al cliente a un cambio de tarifas. Los comentarios que lo aclararían son miles y nadie los ha leído. La voz del cliente con IA, que analiza reseñas y llamadas, los lee todos.",
 "bloque": """<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Sabes cuánto, no sabes por qué</p><h2>¿Por qué baja la satisfacción de los clientes si nadie ha cambiado nada?</h2></div>
<ul class="lista" style="font-size:18px;max-width:820px">
<li>«A mí la semana pasada un cliente me dijo que el problema es la aplicación.»</li>
<li>«Eso son cuatro que se quejan siempre; la mayoría está contenta.»</li>
<li>«El informe del trimestre dice que la entrega va bien.»</li>
<li>«Habría que leer los comentarios, pero son doce mil.»</li>
</ul>
<p style="max-width:820px;margin-top:18px">Cuando la discusión se apoya en anécdotas, gana quien cuenta la más reciente o quien tiene más peso en la sala. No porque nadie mienta, sino porque cada uno ha oído a los clientes que le tocan. La información para zanjarlo existe: está en el campo de texto libre de las encuestas, en los correos de soporte y en las llamadas grabadas. Se recoge con cuidado y casi nunca se lee entera.</p>
<h3 style="margin-top:30px">Lo que ya mides y lo que no te cuenta</h3>
<div class="tabla-wrap"><table class="tabla-norm"><thead><tr><th>Indicador que ya tienes</th><th>Lo que dice</th><th>Lo que deja fuera</th></tr></thead><tbody>
<tr><td>Nota media o índice de recomendación</td><td>Si la satisfacción sube o baja</td><td>El motivo, y si es el mismo en todas partes</td></tr>
<tr><td>Número de reclamaciones</td><td>Cuánta gente se toma la molestia de protestar</td><td>A los que se van sin decir nada</td></tr>
<tr><td>Estrellas en reseñas públicas</td><td>La imagen hacia fuera</td><td>Qué aspecto concreto repiten quienes puntúan bajo</td></tr>
<tr><td>Muestreo manual de comentarios</td><td>Ejemplos ilustrativos</td><td>El peso real de cada tema y su evolución</td></tr>
</tbody></table></div>
<p style="max-width:820px;margin-top:20px">Leer todos los comentarios y clasificarlos no sustituye a esos indicadores; los explica. Permite decir «los plazos de entrega concentran la mayor parte de las quejas de este mes y vienen sobre todo de una zona» en lugar de «creo que es la entrega».</p>
<h3 style="margin-top:30px">Límites que conviene conocer</h3>
<ul class="lista" style="max-width:820px">
<li>Refleja a quien opina, no a toda la clientela: los callados siguen sin aparecer.</li>
<li>Clasifica bien el grueso y duda en lo ambiguo; por eso cada conclusión enlaza a los textos originales.</li>
<li>Señala dónde mirar. Decidir qué se cambia sigue siendo trabajo de cada área.</li>
<li>Con transcripciones de llamadas, la calidad depende de la grabación.</li>
</ul>
<p style="max-width:820px;margin-top:18px">Para probarlo sin comprometer a toda la organización, se plantea como un <a href="/servicios/grandes-empresas/piloto-de-agente-ia-en-30-60-dias">piloto acotado</a> sobre un canal y un periodo. Si el objetivo es anticipar bajas con datos de comportamiento además de comentarios, lo complementa el análisis de <a href="/servicios/automatizacion-y-datos/clientes-en-riesgo-de-irse">clientes en riesgo de irse</a>. Y antes de cargar históricos de varios sistemas, revisa la <a href="/servicios/grandes-empresas/preparacion-de-datos-para-ia">preparación de datos para IA</a>.</p>
</div></section>""",
 "faq": [
  ("¿Cómo analizar miles de comentarios de clientes sin leerlos uno a uno?", "Con un sistema que lee cada comentario, lo asigna a uno o varios motivos y cuenta cuántos hay de cada tipo y cómo evolucionan. Una persona revisa una muestra para confirmar que la clasificación es correcta y ajusta las categorías."),
  ("¿Cómo saber por qué ha bajado la satisfacción o el NPS?", "Comparando los motivos que aparecen en los comentarios del periodo actual con los del anterior. Los temas que más crecen entre quienes puntúan bajo suelen explicar la caída, y los textos originales permiten comprobarlo."),
 ],
}
