# Bloques «primero la persona» para páginas internas (plan del 15/11/2026).
# Se insertan entre la cabecera y el contenido que ya existía. No cambian URL, título, H1 ni metadescripción.

def _t(h, p):
    return '<div class="tarjeta"><h3>%s</h3><p>%s</p></div>' % (h, p)

def _d(h, p, c=""):
    return '<div class="tarjeta dolor%s"><h3>%s</h3><p>%s</p></div>' % (c, h, p)

# slug del hub -> html (rutas relativas a /servicios/)
HUB_ANTES = {
"autonomos": """<section class="sec sec-suave"><div class="w">
<div class="cab"><p class="kicker">¿En qué punto estás?</p><h2>Tanto si solo tienes la idea como si ya eres autónomo</h2><p class="lead" style="margin-top:8px">No es lo mismo estar pensando en empezar que llevar meses trabajando. Por eso lo primero es saber dónde estás.</p></div>
<div class="rejilla">
<div class="tarjeta" style="border-top:4px solid var(--burdeos)"><h3>Tengo una idea, pero todavía no me he dado de alta</h3><p>Te ayudamos a darle forma, a decidir qué necesitas de verdad para empezar y a preparar tu presencia profesional para el día que arranques. Sin gastar de más antes de tiempo.</p><a class="mas" href="../guias/como-emprender-un-negocio.html">Guía: cómo emprender un negocio →</a></div>
<div class="tarjeta" style="border-top:4px solid var(--ocre)"><h3>Ya soy autónomo y quiero avanzar</h3><p>Te ayudamos a que te encuentren, a ordenar clientes, presupuestos y facturas, y a quitarte de encima las tareas que repites cada semana.</p><a class="mas" href="autonomos/automatizacion-del-dia-a-dia.html">Automatización del día a día →</a></div>
</div></div></section>
<section class="sec"><div class="w">
<div class="cab"><p class="kicker">Lo que más preocupa al empezar</p><h2>Si te suena alguna de estas dudas, es normal</h2></div>
<div class="rejilla">"""
+ _d("«No sé por dónde empezar»", "Hay mil herramientas y consejos. Ordenamos contigo los primeros pasos y dejamos para más adelante lo que todavía no hace falta.")
+ _d("«Me da miedo invertir de más»", "Empiezas por lo imprescindible y con el precio por escrito antes de arrancar. Lo demás se añade cuando tenga sentido.", " d2")
+ _d("«Nadie me encuentra»", "Sin web ni ficha de Google es difícil que confíen en ti. Te dejamos una presencia profesional desde el primer día.", " d3")
+ """</div></div></section>
<section class="sec sec-suave"><div class="w">
<div class="cab"><p class="kicker">Así te ayudamos</p><h2>Cuatro apoyos para emprender con buen pie</h2></div>
<div class="rejilla">"""
+ _t("Presencia profesional", 'Identidad, <a href="webs.html">web</a> y <a href="presencia-digital.html">ficha de Google Business</a> para que te encuentren y te tomen en serio.')
+ _t("Organización inicial", 'Clientes, presupuestos y facturas en un <a href="software-de-gestion.html">programa de gestión</a> sencillo, en lugar de repartidos entre el móvil y el Excel.')
+ _t("Formación", 'Te enseñamos a usar lo que montamos y, si quieres, a aprovechar la IA en tu trabajo con <a href="formacion-ia.html">formación práctica</a>.')
+ _t("Acompañamiento", "Hablas siempre con la misma persona, que conoce tu proyecto y te orienta en cada paso.")
+ """</div>
<p class="mut" style="margin-top:22px;font-size:15px;max-width:820px">Importante: no somos gestoría ni asesoría. El alta de autónomo, la constitución de una sociedad y los trámites fiscales los lleva tu gestor. Nosotros nos ocupamos de la parte digital y de organización del negocio, y si lo necesitas te ayudamos a encontrar a ese profesional.</p>
<div class="botones" style="margin-top:22px"><a class="btn btn-p" href="../contacto.html?servicio=autonomos#diagnostico">Quiero saber por dónde empezar</a></div>
</div></section>""",
}

# Selector de /servicios/ (rutas relativas a /servicios/)
SELECTOR = """<section class="sec sec-suave" style="padding:56px 0"><div class="w">
<div class="cab" style="margin-bottom:26px"><p class="kicker">Empieza por tu necesidad</p><h2>¿Qué quieres resolver?</h2><p class="lead" style="margin-top:8px">No hace falta que sepas qué herramienta necesitas. Elige lo que más se parece a tu situación.</p></div>
<div class="rejilla">
<a class="tarjeta" href="autonomos.html"><h3>Empezar un negocio</h3><p>Tienes una idea o acabas de arrancar y quieres hacerlo con buen pie.</p><span class="mas">Emprendedores y autónomos →</span></a>
<a class="tarjeta" href="presencia-digital.html"><h3>Conseguir clientes</h3><p>Tu trabajo es bueno, pero te encuentran poco en Google y en redes.</p><span class="mas">Presencia digital →</span></a>
<a class="tarjeta" href="automatizacion-y-datos.html"><h3>Ahorrar tiempo</h3><p>Repites las mismas tareas cada semana y no te queda tiempo para lo importante.</p><span class="mas">Automatización →</span></a>
<a class="tarjeta" href="software-de-gestion.html"><h3>Organizar el negocio</h3><p>Clientes, presupuestos y facturas repartidos entre Excel, correo y WhatsApp.</p><span class="mas">Programa de gestión →</span></a>
<a class="tarjeta" href="../normativas.html"><h3>Cumplir requisitos</h3><p>Verifactu, registro de jornada o formación en IA: qué te afecta y desde cuándo.</p><span class="mas">Normativas →</span></a>
<a class="tarjeta" href="pequenas-empresas.html"><h3>Crecer</h3><p>El negocio funciona y quieres dar el siguiente paso sin perder el control.</p><span class="mas">Pequeñas empresas →</span></a>
</div>
<p style="margin-top:22px">¿No encaja ninguna? <a href="../contacto.html#diagnostico">Cuéntanos tu caso</a> y te orientamos. Debajo tienes el catálogo completo.</p>
</div></section>"""
