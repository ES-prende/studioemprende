# Página de programa de partners de Studio Emprende (partners.html)
TITULO = "Programa de partners para asesores y consultores"
META = "Hazte partner de Studio Emprende: ofrece a tus clientes webs, software de gestión, IA y formación con nuestro equipo técnico detrás. Para asesorías y consultores."

FAQS = [
 ("¿Quién puede ser partner de Studio Emprende?", "Asesorías, gestorías, consultores, coaches de emprendimiento, agencias, informáticos y entidades que acompañan a emprendedores y tienen clientes a los que ya prestan servicio."),
 ("¿Tengo que saber de tecnología para ser partner?", "No. Tú conoces a tu cliente y detectas lo que necesita; la implantación, las migraciones y el soporte técnico los hacemos nosotros."),
 ("¿Qué gano como partner?", "Depende del nivel y del tipo de colaboración. Te explicamos las condiciones en la primera conversación, antes de que te comprometas a nada."),
 ("¿Sigo siendo yo quien atiende a mi cliente?", "Sí. La relación con tu cliente es tuya; nosotros te tenemos al tanto de cada paso del proyecto."),
 ("¿Cómo se sube de nivel?", "Con el tiempo y los proyectos que hacemos juntos. Empiezas como Semilla y, a medida que la colaboración crece, pasas a Brote y a Árbol."),
]

def html(migas_html, faq_html, dom):
    return """<section class="page-hero"><div class="w">{m}<p class="kicker">Programa de partners</p><h1>Hazte partner de Studio Emprende</h1>
<p class="lead">Para asesorías, consultores y profesionales que acompañan a emprendedores y pymes: ofrece a tus clientes web, programa de gestión, IA y formación con nuestro equipo técnico detrás, sin dejar de ser su referente.</p>
<div class="botones" style="margin-top:24px"><a class="btn btn-p" href="#solicitud">Quiero ser partner</a><a class="btn btn-s" href="#niveles">Ver los niveles</a></div>
<div class="niveles-mini"><span>Semilla</span><span>Brote</span><span>Árbol</span></div></div></section>

<section class="sec" style="padding-bottom:0"><div class="w"><div class="respuesta"><p class="kicker" style="margin:0 0 6px">Respuesta corta</p><p style="margin:0">El programa de partners de Studio Emprende permite a asesorías, consultores y otros profesionales ofrecer a sus clientes todo lo digital que necesita un negocio (web con SEO, programa de gestión, agente de IA PIX, automatizaciones y formación) mientras nosotros nos encargamos de la parte técnica. Hay tres niveles: Semilla, Brote y Árbol.</p></div></div></section>

<section class="sec"><div class="w"><div class="cab"><p class="kicker">A quién va</p><h2>¿Para quién es el programa de partners?</h2></div><div class="rejilla">
<div class="tarjeta"><h3>Asesorías y gestorías</h3><p>Das de alta negocios cada semana. Tus clientes te preguntan por la web, la facturación con Verifactu o el fichaje, y ahora tienes a quién derivarlos con confianza.</p></div>
<div class="tarjeta"><h3>Consultores y coaches de emprendimiento</h3><p>Ayudas a definir el negocio; nosotros lo ponemos en marcha en digital con packs de precio cerrado.</p></div>
<div class="tarjeta"><h3>Agencias de diseño y marketing</h3><p>Haces la marca o las campañas y te falta la parte de software, automatizaciones o IA para cerrar el proyecto completo.</p></div>
<div class="tarjeta"><h3>Informáticos e instaladores</h3><p>Mantienes equipos y redes; sumas programa de gestión, fichador y agentes de IA a lo que ya ofreces.</p></div>
<div class="tarjeta"><h3>Incubadoras y asociaciones</h3><p>Acompañas a emprendedores y quieres darles un proveedor tecnológico serio, con precios claros desde el primer día.</p></div>
</div></div></section>

<section class="sec sec-suave"><div class="w"><div class="cab"><p class="kicker">Qué te llevas</p><h2>¿Qué ganas al ser partner de Studio Emprende?</h2></div><div class="rejilla">
<div class="tarjeta"><h3>Un catálogo completo para tus clientes</h3><p>Packs con precio cerrado, programa de gestión modular, el agente de IA PIX, webs con SEO, fichador y formación en IA. Un solo proveedor para todo lo digital.</p></div>
<div class="tarjeta"><h3>Equipo técnico detrás</h3><p>Implantación, migración de datos, integraciones y soporte los hacemos nosotros. Tú no tienes que contratar a nadie.</p></div>
<div class="tarjeta"><h3>Tu cliente sigue siendo tuyo</h3><p>Tú mantienes la relación. Te informamos de cada proyecto para que siempre sepas cómo va.</p></div>
<div class="tarjeta"><h3>Diagnóstico gratis para tus clientes</h3><p>Antes de proponer nada, revisamos el negocio de tu cliente y te damos una propuesta clara para presentársela.</p></div>
<div class="tarjeta"><h3>Formación para ti y tu equipo</h3><p>Sesiones sobre nuestras soluciones y sobre IA aplicada, para que sepas qué ofrecer y cuándo.</p></div>
<div class="tarjeta"><h3>Condiciones que crecen contigo</h3><p>Cuanto más colaboramos, más cercanía y mejores condiciones. Te las explicamos en la primera conversación.</p></div>
</div></div></section>

<section class="sec" id="niveles"><div class="w"><div class="cab"><p class="kicker">Niveles</p><h2>Tres niveles de partner</h2></div><div class="rejilla">
<div class="tarjeta nivel"><p class="kicker" style="margin:0 0 6px">Nivel 1</p><h3>Semilla</h3><p>El punto de partida. Te damos el material para presentar nuestras soluciones y acompañamos de cerca tus primeros clientes.</p></div>
<div class="tarjeta nivel"><p class="kicker" style="margin:0 0 6px">Nivel 2</p><h3>Brote</h3><p>Cuando ya trabajamos juntos con varios clientes. Interlocutor directo en nuestro equipo y prioridad en diagnósticos y propuestas.</p></div>
<div class="tarjeta nivel"><p class="kicker" style="margin:0 0 6px">Nivel 3</p><h3>Árbol</h3><p>Para relaciones estables. Planificación conjunta, acompañamiento en proyectos grandes y presencia como partner destacado.</p></div>
</div></div></section>

<section class="sec sec-suave"><div class="w lateral"><div class="lateral-main"><div class="cab"><p class="kicker">Qué pedimos</p><h2>Requisitos para ser partner</h2></div>
<ul class="lista"><li>Tener clientes a los que ya prestas servicio o una red de emprendedores.</li><li>Recomendar solo lo que el cliente necesita, sin prometer de más.</li><li>Trabajar con clientes en España.</li><li>Ganas de construir una relación a largo plazo.</li></ul></div>
<aside class="lateral-aside"><h3>¿Tienes dudas?</h3><p style="color:#C9C1BB">Escríbenos y te contamos cómo encaja el programa con lo que haces.</p><a class="btn btn-claro" href="https://wa.me/34601869668?text=Hola%2C%20quiero%20informaci%C3%B3n%20del%20programa%20de%20partners" target="_blank" rel="noopener">Hablar por WhatsApp</a></aside></div></section>

<section class="sec"><div class="w"><div class="cab"><p class="kicker">Cómo funciona</p><h2>Cómo hacerse partner en cuatro pasos</h2></div><div class="rejilla">
<div class="tarjeta"><h3>1. Envías la solicitud</h3><p>Nos cuentas a qué te dedicas y qué tipo de clientes tienes.</p></div>
<div class="tarjeta"><h3>2. Hablamos</h3><p>Una conversación para conocernos, ver encaje y explicarte las condiciones.</p></div>
<div class="tarjeta"><h3>3. Alta como partner</h3><p>Empiezas en el nivel Semilla con el material y el contacto de tu interlocutor.</p></div>
<div class="tarjeta"><h3>4. Primer cliente juntos</h3><p>Hacemos el diagnóstico de tu primer cliente y te acompañamos en toda la propuesta.</p></div>
</div></div></section>

<section class="sec sec-suave" id="solicitud"><div class="w lateral"><div class="lateral-main">
<div class="cab"><h2>Solicita ser partner</h2><p class="lead" style="margin-top:8px">Cuéntanos tu actividad y tus clientes. Te respondemos en menos de 24 horas laborables.</p></div>
<form class="form" data-contacto action="https://formsubmit.co/info@studioemprende.com" method="post">
<input type="hidden" name="_subject" value="Solicitud de partner desde studioemprende.com">
<input type="hidden" name="_cc" value="socialstudioemprende@gmail.com">
<input type="hidden" name="_template" value="table">
<input type="hidden" name="_next" value="{dom}/gracias.html">
<input type="hidden" name="_captcha" value="true">
<input type="hidden" name="_blacklist" value="viagra, casino, crypto, bitcoin, forex, loan, seo services, backlinks, porn, betting, http://, https://bit.ly">
<input type="hidden" name="_autoresponse" value="Hola, hemos recibido tu solicitud para ser partner de Studio Emprende. Te escribimos en menos de 24 horas laborables para hablar.">
<input type="hidden" name="_t" id="_t" value="">
<div aria-hidden="true" style="position:absolute;left:-10000px;top:auto;width:1px;height:1px;overflow:hidden"><label>No rellenar<input type="text" name="_honey" tabindex="-1" autocomplete="off"></label><label>Web<input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
<p class="form-aviso" id="form-aviso" role="alert" hidden></p>
<div class="dos"><div class="campo"><label for="nombre">Nombre</label><input id="nombre" name="nombre" autocomplete="name" required minlength="2" maxlength="80"></div>
<div class="campo"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" required maxlength="120"></div></div>
<div class="dos"><div class="campo"><label for="telefono">Teléfono (opcional)</label><input id="telefono" name="telefono" type="tel" autocomplete="tel" inputmode="tel" maxlength="20"></div>
<div class="campo"><label for="empresa">Empresa (opcional)</label><input id="empresa" name="empresa" autocomplete="organization" maxlength="120"></div></div>
<div class="dos"><div class="campo"><label for="perfil">¿A qué te dedicas?</label><select id="perfil" name="perfil" required><option value="">Elige una opción</option><option>Asesoría o gestoría</option><option>Consultoría o coaching de emprendimiento</option><option>Agencia de diseño, marketing o webs</option><option>Informática o instalaciones</option><option>Incubadora, aceleradora o asociación</option><option>Otro</option></select></div>
<div class="campo"><label for="clientes">¿Cuántos clientes atiendes?</label><select id="clientes" name="clientes"><option value="">Prefiero no decirlo</option><option>Menos de 10</option><option>Entre 10 y 50</option><option>Entre 50 y 200</option><option>Más de 200</option></select></div></div>
<div class="campo"><label for="mensaje">Cuéntanos tu actividad y qué necesitan tus clientes</label><textarea id="mensaje" name="mensaje" rows="5" maxlength="2000"></textarea></div>
<label style="display:flex;gap:10px;font-size:14px;align-items:flex-start"><input type="checkbox" name="privacidad" required style="margin-top:4px"> He leído y acepto la <a href="privacidad.html">política de privacidad</a>.</label>
<div><button class="btn btn-p" type="submit">Enviar solicitud</button></div>
</form></div>
<aside class="lateral-aside"><h3>Otras formas de contacto</h3><p style="color:#C9C1BB"><a style="color:#fff" href="mailto:info@studioemprende.com">info@studioemprende.com</a><br><a style="color:#fff" href="https://wa.me/34601869668" target="_blank" rel="noopener">WhatsApp 601 86 96 68</a></p></aside></div></section>

<section class="sec"><div class="w"><div class="cab"><h2>Preguntas frecuentes</h2></div>{faq}</div></section>""".format(m=migas_html, faq=faq_html, dom=dom)
