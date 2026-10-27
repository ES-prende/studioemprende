# Temas del blog (/temas/): páginas de archivo que agrupan artículos, guías y servicios por asunto.
# Sección nueva y plana con su propio sitemap. El índice del blog (/blog/) está indexado y no se modifica.

TEMAS = [
 ("inteligencia-artificial", "Inteligencia artificial para pequeñas empresas",
  "Artículos sobre inteligencia artificial para pymes y autónomos: agentes, WhatsApp, automatización y por dónde empezar.",
  "La IA útil en un negocio pequeño no es la que escribe poemas, sino la que contesta el WhatsApp a las once de la noche, prepara el presupuesto o te avisa de una factura sin cobrar. Aquí reunimos lo que hemos escrito sobre cómo empezar, qué tareas automatizar primero, qué herramienta elegir y cuándo compensa frente a contratar.",
  ["como-empezar-a-usar-la-ia-en-tu-pequena-empresa", "tareas-que-puedes-automatizar", "que-puede-hacer-un-agente-de-ia", "agente-de-ia-para-whatsapp", "whatsapp-para-no-perder-clientes", "ia-o-contratar-personal-en-una-pequena-empresa", "chatgpt-gemini-copilot-o-claude-para-empresas", "formacion-en-ia-desde-cero", "kit-digital-ia", "piloto-ia-grandes-empresas"],
  [("Agentes de IA", "servicios/agentes-de-ia/index.html"), ("WhatsApp con IA", "servicios/whatsapp-ia/index.html"), ("PIX, nuestro agente", "servicios/pix/index.html")]),
 ("gestion-y-crm", "Gestión, CRM y programas para tu negocio",
  "Artículos sobre CRM, ERP, programas de gestión y cómo dejar el Excel: qué elegir, cuánto cuesta y cómo implantarlo.",
  "Si llevas clientes en una libreta, presupuestos en el correo y facturas en Excel, estos artículos son para ti. Explican qué es un CRM y un ERP sin tecnicismos, cuánto cuestan de verdad, cómo saber cuándo te hace falta uno y cómo pasar tus datos sin perder nada ni parar el negocio.",
  ["software-de-gestion-modular-con-automatizaciones", "cuanto-cuesta-un-crm-para-autonomos", "crm-para-autonomos", "crm-para-empresas-de-servicios", "que-es-un-erp-y-cuando-lo-necesito", "como-dejar-de-usar-excel-en-mi-empresa", "software-todo-en-uno-para-pequenas-empresas", "app-de-control-horario-para-pequenas-empresas", "app-movil-para-mi-negocio"],
  [("Programa de gestión", "servicios/software-de-gestion/index.html"), ("ERP para pymes", "servicios/erp-para-pymes/index.html"), ("Migraciones", "servicios/migraciones-e-integraciones/index.html")]),
 ("normativas-y-cumplimiento", "Normativas que afectan a tu negocio",
  "Verifactu, fichaje digital, AI Act, APPCC y registro de viajeros: qué dicen las normas, a quién afectan y cómo cumplirlas.",
  "Cada año llega alguna obligación nueva y casi nunca se explica en lenguaje normal. Estos artículos cuentan qué exige cada norma, desde cuándo, a quién afecta y qué tienes que tener preparado, con enlace a la fuente oficial. Para el calendario completo, consulta también la página de normativas.",
  ["que-es-verifactu-y-cuando-me-afecta", "es-obligatorio-el-fichaje-digital", "formacion-ia-obligatoria-ai-act", "formacion-obligatoria-en-empresas", "appcc-digital-hosteleria", "registro-de-viajeros-ses-hospedajes"],
  [("Normativas 2026-2027", "normativas.html"), ("Fichador", "servicios/fichador/index.html"), ("Ciberseguridad y cumplimiento", "servicios/ciberseguridad-y-sistemas/index.html")]),
 ("formacion-para-empresas", "Formación para empresas y equipos",
  "Cómo organizar la formación de tu equipo: obligatoria, bonificada con FUNDAE, en IA y para nuevas incorporaciones.",
  "Formar al equipo es obligatorio en algunos casos y rentable en casi todos, pero suele hacerse tarde y sin registro. Aquí explicamos qué formación es obligatoria, cómo bonificarla con FUNDAE, cómo montar un plan de formación en seis pasos y cómo empezar con la IA sin conocimientos previos.",
  ["como-calcular-el-credito-de-formacion-fundae", "plan-de-formacion-para-empresas", "formacion-bonificada-para-empresas-fundae", "formacion-obligatoria-en-empresas", "formacion-ia-obligatoria-ai-act", "formacion-en-ia-desde-cero"],
  [("Formación en IA", "servicios/formacion-ia/index.html"), ("Plataforma de formación interna", "servicios/software-especializado/plataforma-de-formacion-interna-lms.html")]),
 ("webs-y-visibilidad", "Webs y visibilidad en Google y en la IA",
  "Cómo conseguir una web que venda y aparecer en Google y en ChatGPT con un negocio pequeño.",
  "Tener web no basta: tiene que aparecer cuando te buscan y convencer cuando te encuentran. Estos artículos explican qué hace que una web venda, cómo salir en Google con una empresa pequeña y qué cambia ahora que mucha gente pregunta a ChatGPT o a Gemini antes de buscar.",
  ["web-que-vende", "como-aparecer-en-google-con-tu-pequena-empresa", "como-aparecer-en-chatgpt", "primeros-pasos-autonomo-digital"],
  [("Webs", "servicios/webs/index.html"), ("Presencia digital", "servicios/presencia-digital/index.html"), ("Caso real: ContrataLux", "casos/contratalux.html")]),
 ("emprender-y-crecer", "Emprender, crecer y proteger tu negocio",
  "Primeros pasos digitales, ahorrar horas, cobrar a tiempo, copias de seguridad y preparar el relevo del negocio.",
  "Lo que conviene resolver pronto para no tener sustos después: los primeros pasos digitales de un autónomo, cómo ahorrar horas en una pyme, cómo reducir impagos, cómo tener copias de seguridad que funcionen de verdad y cómo preparar el negocio para el día que otro tome el relevo.",
  ["primeros-pasos-autonomo-digital", "pyme-ahorrar-horas", "como-reducir-impagos", "copias-de-seguridad-que-funcionan", "departamento-tecnologico-externo", "relevo-generacional-preparar-mi-negocio", "mvp-startup", "casa-inteligente-de-lujo"],
  [("Autónomos", "servicios/autonomos/index.html"), ("Pequeñas empresas", "servicios/pequenas-empresas/index.html"), ("Tu departamento tecnológico", "servicios/departamento-tecnologico/index.html")]),
]


def html_tema(r, migas_html, tema, tarjetas_html, cta_html):
    slug, titulo, meta, intro, arts, servicios = tema
    serv = " · ".join('<a href="%s%s">%s</a>' % (r, h, t) for t, h in servicios)
    otros = "".join('<a class="pildora" href="%s.html">%s</a>' % (s, t) for s, t, *_ in TEMAS if s != slug)
    return """<section class="page-hero"><div class="w">{m}<p class="kicker">Tema del blog</p><h1>{t}</h1><p class="lead">{i}</p></div></section>
<section class="sec"><div class="w"><div class="cab"><p class="kicker">{n} artículos</p><h2>Lo que hemos escrito sobre este tema</h2></div><div class="rejilla">{c}</div>
<p style="margin-top:28px"><b style="font-weight:500">Servicios relacionados:</b> {s}</p></div></section>
<section class="sec sec-suave"><div class="w"><div class="cab"><p class="kicker">Más temas</p><h2>Otros temas del blog</h2></div><div class="pildoras">{o}</div></div></section>
{cta}""".format(m=migas_html, t=titulo, i=intro, n=len(arts), c=tarjetas_html, s=serv, o=otros, cta=cta_html)


def html_hub(r, migas_html, cta_html):
    tarjetas = "".join('<a class="tarjeta" href="%s.html"><span class="etiqueta">%d artículos</span><h3>%s</h3><p>%s</p><span class="mas">Ver el tema →</span></a>' % (s, len(a), t, m) for s, t, m, i, a, sv in TEMAS)
    return """<section class="page-hero"><div class="w">{m}<p class="kicker">Blog por temas</p><h1>Temas del blog: gestión, IA, webs, normativas y formación</h1>
<p class="lead">Todos nuestros artículos ordenados por asunto, para que encuentres lo que necesitas sin recorrer el blog entero.</p></div></section>
<section class="sec"><div class="w"><div class="rejilla">{t}</div></div></section>
{cta}""".format(m=migas_html, t=tarjetas, cta=cta_html)
