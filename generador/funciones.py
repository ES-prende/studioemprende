# Páginas de función con contenido propio (se indexan). Las que no estén aquí usan la plantilla genérica y van con noindex.
# Clave: "seccion/slug". Cada página ataca una búsqueda distinta y no repite lo que ya cuentan los artículos del blog.
FECHA = "2026-10-15"

PAGINAS = {
"software-de-gestion/facturacion-con-verifactu": {
 "titulo": "Programa de facturación con Verifactu",
 "meta": "Programa de facturación preparado para Verifactu: registro encadenado, código QR en cada factura y envío a Hacienda, dentro de tu programa de gestión.",
 "h1": "Programa de facturación con Verifactu, dentro de tu gestión",
 "lead": "Un programa de facturación con Verifactu que no es una pieza suelta: las facturas salen de tus presupuestos y pedidos y quedan registradas como exige Hacienda.",
 "respuesta": "Un programa de facturación adaptado a Verifactu genera un registro de cada factura encadenado con el anterior, imprime un código QR que el cliente puede verificar en la Agencia Tributaria y, si eliges la modalidad VERI*FACTU, envía los registros a Hacienda de forma automática. Nuestro programa lo hace sin pasos extra.",
 "secciones": [
  ("¿Qué hace el programa por ti?", "Se encarga de que cada factura cumpla Verifactu sin que cambies tu forma de facturar: deja el registro encadenado, pone el QR, remite los datos a Hacienda si eliges esa modalidad y corrige errores con rectificativas.", [
    ("Registro encadenado", "Cada factura genera su registro con una huella vinculada a la anterior, de modo que no se puede borrar ni alterar sin dejar rastro."),
    ("Código QR en la factura", "El QR se añade solo en el PDF y en el ticket, listo para que tu cliente lo compruebe."),
    ("Envío a la Agencia Tributaria", "En modalidad VERI*FACTU, los registros se remiten automáticamente; tú no tienes que entrar en ninguna sede."),
    ("Rectificativas y anulaciones correctas", "Si te equivocas, el programa genera la rectificativa en lugar de dejarte borrar."),
  ]),
  ("¿Cuándo tienes que tenerlo?", "Las fechas vigentes son el 1 de enero de 2027 para sociedades y el 1 de julio de 2027 para el resto, aunque Hacienda ha anunciado un aplazamiento a octubre de 2028 pendiente de publicarse en el BOE. Lo explicamos al detalle en el artículo «Qué es Verifactu y cuándo te afecta».", []),
 ],
 "faqs": [
  ("¿Sirve mi programa de facturación actual para Verifactu?", "Solo si su fabricante lo ha adaptado y declara que cumple. Si no lo hace, tendrás que cambiar de programa antes de la fecha que te corresponda."),
  ("¿Puedo seguir facturando en Excel o Word con Verifactu?", "No como sistema de facturación: Verifactu exige un software que genere y conserve los registros de cada factura."),
  ("¿Puedo importar mis clientes y facturas anteriores?", "Sí. Importamos tus datos para que sigas la numeración y tengas el histórico en el mismo programa."),
 ],
 "rel": [("../../blog/que-es-verifactu-y-cuando-me-afecta.html", "Qué es Verifactu y cuándo te afecta"), ("factura-electronica-b2b.html", "Factura electrónica B2B"), ("cobros-impagos-y-semaforo-de-clientes.html", "Cobros e impagos")],
},
"software-de-gestion/factura-electronica-b2b": {
 "titulo": "Factura electrónica B2B obligatoria: programa preparado",
 "meta": "Envía y recibe la factura electrónica B2B obligatoria desde tu programa de gestión, con estado de pago informado. Calendario: 2027 y 2028 según facturación.",
 "h1": "Factura electrónica B2B: emítela y recíbela desde tu programa",
 "lead": "La factura electrónica B2B será obligatoria entre empresas y autónomos. Con nuestro programa de gestión las envías, las recibes y comunicas su estado de pago sin cambiar de herramienta.",
 "respuesta": "La factura electrónica B2B obligatoria no es un PDF por correo: es un archivo estructurado que se intercambia por plataformas autorizadas o por la solución pública de la Agencia Tributaria, y en el que además hay que informar de cuándo se paga. Será obligatoria desde el 6 de octubre de 2027 para quien facture más de 8 millones de euros y desde el 6 de octubre de 2028 para el resto.",
 "secciones": [
  ("¿En qué se diferencia de lo que haces hoy?", "Cambian tres cosas respecto al PDF que mandas por correo: el formato del archivo, que leerá el programa de tu cliente; el canal de envío, que debe estar autorizado; y la obligación de comunicar cuándo se paga.", [
    ("Archivo estructurado, no PDF", "La factura viaja en un formato que el programa del cliente lee sin que nadie teclee nada."),
    ("Envío por canal autorizado", "Plataformas de intercambio o la solución pública de la AEAT, en lugar del correo electrónico."),
    ("Estado de pago", "Hay que informar de cuándo se cobra o se paga cada factura, lo que ayuda a vigilar la morosidad."),
  ]),
  ("¿Cómo lo resolvemos?", "Lo resolvemos dentro de tu propio programa: la factura que ya emites sale también en formato electrónico, las de tus proveedores entran sin teclearlas y el estado de cobro o pago se comunica al registrarlo.", [
    ("Emisión desde la misma factura", "La factura que ya generas (con Verifactu) se envía también en formato electrónico."),
    ("Recepción automática", "Las facturas de proveedores entran en el programa sin teclearlas."),
    ("Estado de cobro sincronizado", "Al marcar un cobro, el estado se comunica; al recibir un pago, se refleja en tu tesorería."),
  ]),
 ],
 "faqs": [
  ("¿Qué empresas están obligadas a la factura electrónica B2B?", "Todas las empresas y autónomos en sus operaciones con otras empresas y profesionales: primero quienes facturan más de 8 millones de euros (6/10/2027) y después el resto (6/10/2028)."),
  ("¿Verifactu y factura electrónica son lo mismo?", "No. Verifactu controla cómo se registran tus facturas; la factura electrónica B2B regula cómo se envían y reciben entre empresas. Hay que cumplir las dos."),
  ("¿Afecta a las facturas a particulares?", "No: la obligación es para operaciones entre empresas y profesionales."),
 ],
 "rel": [("facturacion-con-verifactu.html", "Programa de facturación con Verifactu"), ("../../normativas.html", "Normativas y plazos"), ("prevision-de-tesoreria.html", "Previsión de tesorería")],
},
"software-de-gestion/cobros-impagos-y-semaforo-de-clientes": {
 "titulo": "Control de cobros e impagos con semáforo de clientes",
 "meta": "Controla cobros e impagos con un semáforo por cliente: avisos antes y después del vencimiento, recordatorios por WhatsApp y bloqueo de nuevos pedidos si hay deuda.",
 "h1": "Control de cobros e impagos: el semáforo de tus clientes",
 "lead": "Controlar los cobros y los impagos no debería depender de revisar el banco cada mañana. El semáforo te dice de un vistazo quién paga bien, quién se retrasa y a quién no conviene servir.",
 "respuesta": "Un control de cobros con semáforo clasifica a cada cliente en verde (paga a tiempo), ámbar (se retrasa) o rojo (tiene deuda vencida), envía recordatorios automáticos antes y después del vencimiento y avisa al equipo antes de aceptar un pedido nuevo de un cliente en rojo.",
 "secciones": [
  ("¿Cómo funciona el semáforo?", "El semáforo pinta a cada cliente según cómo paga: verde si cumple los plazos, ámbar si empieza a retrasarse o roza su límite de riesgo y rojo cuando acumula facturas vencidas sin pagar.", [
    ("Verde", "Paga en plazo. Se le sirve sin restricciones."),
    ("Ámbar", "Acumula retrasos o se acerca a su límite de riesgo. Recibe recordatorios y el comercial lo ve en su ficha."),
    ("Rojo", "Tiene facturas vencidas. El programa avisa antes de preparar un nuevo pedido o presupuesto."),
  ]),
  ("Recordatorios que cobran solos", "Los avisos de cobro salen sin que nadie los escriba: uno cordial antes de que venza la factura, otros escalonados por correo y WhatsApp si se retrasa, y se detienen en cuanto el banco confirma el pago.", [
    ("Antes del vencimiento", "Un aviso amable unos días antes evita la mayoría de retrasos."),
    ("Después del vencimiento", "Recordatorios escalonados por correo y WhatsApp, con enlace de pago."),
    ("Al conciliar el banco", "Cuando entra el pago, la factura se marca como cobrada y los avisos se detienen."),
  ]),
 ],
 "faqs": [
  ("¿Se puede poner un límite de riesgo por cliente?", "Sí. Defines un importe máximo de deuda y el programa avisa cuando un pedido lo superaría."),
  ("¿Los recordatorios suenan agresivos?", "No: los textos los ajustamos contigo y empiezan con un tono cordial; tú decides cuándo se endurecen."),
  ("¿Cómo se entera el programa de que me han pagado?", "Al conciliar el extracto del banco: cada cobro se casa con su factura y el semáforo se actualiza."),
 ],
 "rel": [("../../blog/como-reducir-impagos.html", "Cómo reducir los impagos"), ("prevision-de-tesoreria.html", "Previsión de tesorería"), ("remesas-y-domiciliaciones.html", "Remesas y domiciliaciones")],
},
"software-de-gestion/prevision-de-tesoreria": {
 "titulo": "Previsión de tesorería automática para pymes",
 "meta": "Previsión de tesorería automática a 13 semanas: cobros pendientes, pagos, nóminas e impuestos en una sola vista para anticiparte a los meses flojos.",
 "h1": "Previsión de tesorería automática: sabe hoy cómo irá tu caja",
 "lead": "La previsión de tesorería te dice cuánto dinero tendrás en las próximas semanas a partir de lo que ya está en tu programa: facturas por cobrar, pagos a proveedores, nóminas e impuestos.",
 "respuesta": "Una previsión de tesorería automática suma tu saldo actual, los cobros pendientes según su vencimiento y los pagos previstos (proveedores, nóminas, impuestos y cuotas) y te muestra semana a semana cuánto dinero tendrás. Así ves con tiempo cuándo faltará caja y puedes adelantar cobros o aplazar compras.",
 "secciones": [
  ("¿De dónde salen los datos?", "La previsión se construye con lo que ya registras en el programa: las facturas emitidas con su vencimiento, los pagos comprometidos a proveedores, nóminas y préstamos, y una estimación de los impuestos del trimestre.", [
    ("Cobros", "Facturas emitidas con su fecha de vencimiento y el historial de puntualidad de cada cliente."),
    ("Pagos", "Facturas de proveedores, remesas, nóminas, cuotas de préstamos y suscripciones."),
    ("Impuestos", "Estimación de IVA y retenciones de cada trimestre a partir de tu facturación."),
  ]),
  ("¿Qué decisiones te ayuda a tomar?", "Te ayuda a decidir con semanas de margen qué cobros conviene reclamar antes, qué pagos puedes mover sin ahogar la caja y si necesitas pedir una póliza al banco antes de que sea urgente.", [
    ("Adelantar cobros", "Detectas qué clientes conviene recordar antes de una semana floja."),
    ("Ordenar pagos", "Ves qué pagos puedes mover sin tensar la caja."),
    ("Pedir financiación con tiempo", "Si hace falta una póliza, la pides antes de necesitarla, no la víspera."),
  ]),
 ],
 "faqs": [
  ("¿A cuánto tiempo se hace la previsión?", "Lo habitual es mirar 13 semanas, un trimestre, con detalle semanal; se puede ampliar a 12 meses con menos detalle."),
  ("¿Tengo que meter los datos a mano?", "No. La previsión se alimenta de las facturas, pedidos y pagos que ya están en el programa; solo añades lo extraordinario."),
  ("¿Sirve para presentar al banco?", "Sí: se exporta en un informe claro que suele pedirse al solicitar financiación."),
 ],
 "rel": [("cobros-impagos-y-semaforo-de-clientes.html", "Cobros e impagos"), ("cuadro-de-mando-en-tiempo-real.html", "Cuadro de mando en tiempo real"), ("conexion-con-tu-asesoria.html", "Conexión con tu asesoría")],
},
"software-de-gestion/agenda-y-citas-online": {
 "titulo": "Agenda y citas online conectadas a tu gestión",
 "meta": "Agenda de citas online conectada a la ficha del cliente: reservas desde la web, WhatsApp y Google, recordatorios automáticos y cobro de señal para evitar ausencias.",
 "h1": "Agenda y citas online que se rellenan solas",
 "lead": "Una agenda de citas online conectada a tu gestión: tus clientes reservan cuando quieren y cada cita queda en su ficha, con su historial y su factura.",
 "respuesta": "Una agenda de citas online permite que el cliente reserve solo desde la web, WhatsApp o tu ficha de Google según tu disponibilidad real, le envía recordatorios para que no falte y guarda cada cita en su ficha. Conectada al programa de gestión, la cita genera después la factura sin volver a teclear.",
 "secciones": [
  ("¿Desde dónde reservan tus clientes?", "Tus clientes pueden reservar desde tres puntos que acaban en la misma agenda: el botón de tu web, una conversación de WhatsApp con el asistente y el enlace de tu perfil de Google Business.", [
    ("Tu web", "Un botón de reserva que muestra solo los huecos libres de cada profesional o sala."),
    ("WhatsApp", "El asistente propone horas y confirma la cita en la conversación."),
    ("Google", "El enlace de reserva en tu perfil de Google Business lleva a la misma agenda."),
  ]),
  ("¿Qué evita las ausencias?", "Las ausencias bajan cuando el cliente recibe un recordatorio con opción de confirmar o cambiar, cuando deja una señal en servicios largos y cuando los huecos cancelados pasan solos a la lista de espera.", [
    ("Recordatorio el día antes", "Con opción de confirmar o cambiar la cita en un toque."),
    ("Señal o pago por adelantado", "Para servicios largos o clientes que ya han faltado."),
    ("Lista de espera", "Si alguien cancela, el hueco se ofrece automáticamente a otro cliente."),
  ]),
 ],
 "faqs": [
  ("¿Puedo tener varias agendas, una por profesional o sala?", "Sí, cada profesional, sala o recurso tiene su agenda y el cliente ve solo lo disponible."),
  ("¿Puedo ver las citas en mi calendario de siempre?", "Se puede sincronizar con calendarios como Google Calendar u Outlook; lo dejamos configurado en la puesta en marcha."),
  ("¿Puedo bloquear horas para trabajo interno?", "Sí, marcas bloques no reservables y la agenda online los respeta."),
 ],
 "rel": [("recordatorios-automaticos-por-whatsapp.html", "Recordatorios automáticos por WhatsApp"), ("../../blog/crm-para-empresas-de-servicios.html", "CRM para empresas de servicios"), ("bonos-cuotas-y-suscripciones.html", "Bonos, cuotas y suscripciones")],
},
"software-de-gestion/captacion-de-leads-desde-web-whatsapp-y-anuncios": {
 "titulo": "Captación de leads desde web, WhatsApp y anuncios",
 "meta": "Recoge en un solo CRM los contactos que llegan por la web, WhatsApp y anuncios de Meta o Google, respóndelos al momento y mide qué canal te trae clientes.",
 "h1": "Captación de leads: todos los contactos en un mismo sitio",
 "lead": "La captación de leads falla menos por falta de contactos que por contactos que se pierden. Aquí cada solicitud de la web, WhatsApp o tus anuncios entra en el CRM y se responde al momento.",
 "respuesta": "Un sistema de captación de leads recoge automáticamente los contactos que llegan por formularios web, WhatsApp y anuncios (Meta o Google), los crea en el CRM con su origen, envía una primera respuesta inmediata y asigna el seguimiento a una persona. Así ningún interesado se enfría y sabes qué canal te trae clientes de verdad.",
 "secciones": [
  ("¿De dónde entran los contactos?", "Entran desde los formularios de tu web, los mensajes nuevos de WhatsApp y los formularios de los anuncios de Meta y Google, y cada uno se guarda en el CRM con el canal del que procede.", [
    ("Formularios de la web", "Cada envío crea el contacto con la página desde la que llegó."),
    ("WhatsApp", "Los mensajes nuevos se registran como oportunidad, con la conversación guardada."),
    ("Anuncios de Meta y Google", "Los formularios de los anuncios se vuelcan al CRM sin descargar hojas de cálculo."),
  ]),
  ("¿Qué pasa en los primeros cinco minutos?", "En esos primeros minutos el contacto recibe una respuesta automática, queda asignado a la persona que corresponde por servicio o zona y, si nadie lo atiende dentro del plazo fijado, el programa lanza un aviso.", [
    ("Respuesta inmediata", "Un mensaje automático confirma que lo has recibido y, si quieres, propone una cita."),
    ("Asignación", "El contacto se asigna a quien toca según el servicio o la zona."),
    ("Seguimiento", "Si nadie lo atiende en el plazo que fijes, el programa avisa."),
  ]),
  ("¿Qué canal te trae clientes?", "Cada contacto guarda su origen y su campaña. El informe te dice cuántos contactos, presupuestos y ventas sale de cada canal, para invertir donde funciona.", []),
 ],
 "faqs": [
  ("¿Qué es un lead?", "Un contacto que ha mostrado interés en lo que vendes, por ejemplo al rellenar un formulario o escribirte por WhatsApp, pero que todavía no es cliente."),
  ("¿Puedo conectar los formularios de Facebook e Instagram Ads?", "Sí, se conectan para que los contactos de los anuncios de Meta entren en el CRM sin descargar archivos."),
  ("¿Cumple la protección de datos?", "Sí, si los formularios recogen el consentimiento; guardamos el origen y la aceptación de cada contacto."),
 ],
 "rel": [("embudo-de-ventas-y-oportunidades.html", "Embudo de ventas y oportunidades"), ("../../blog/agente-de-ia-para-whatsapp.html", "Agente de IA para WhatsApp"), ("campanas-de-email-y-whatsapp.html", "Campañas de email y WhatsApp")],
},
}

def html(key, c, migas_html, faq_html, sec_titulo):
    secs = ""
    for i, (h2, intro, items) in enumerate(c["secciones"]):
        suave = " sec-suave" if i % 2 == 0 else ""
        tarj = "".join('<div class="tarjeta"><h3>%s</h3><p>%s</p></div>' % (a, b) for a, b in items)
        secs += '<section class="sec%s"><div class="w"><div class="cab"><h2>%s</h2></div>%s%s</div></section>' % (
            suave, h2, ('<p class="lead" style="max-width:760px;margin-bottom:20px">%s</p>' % intro) if intro else "", ('<div class="rejilla">%s</div>' % tarj) if tarj else "")
    seccion, slug = key.split("/")
    rel = "".join('<li><a style="color:#fff" href="%s">%s</a></li>' % (h, t) for h, t in c["rel"])
    return """<section class="page-hero"><div class="w">{m}<p class="kicker">{st}</p><h1>{h1}</h1><p class="lead">{lead}</p>
<div class="botones" style="margin-top:24px"><a class="btn btn-p" href="../../contacto.html?servicio={sec}&amp;funcion={sl}#diagnostico">Quiero esto en mi negocio</a><a class="btn btn-s" href="../{sec}.html">Ver {stl}</a></div></div></section>
<section class="sec" style="padding-bottom:0"><div class="w"><div class="respuesta"><p class="kicker" style="margin:0 0 6px">Respuesta corta</p><p style="margin:0">{resp}</p></div></div></section>
{secs}
<section class="sec"><div class="w lateral"><div class="lateral-main"><div class="cab"><h2>Preguntas frecuentes</h2></div>{faq}</div><aside class="lateral-aside"><h3>Relacionado</h3><ul class="lista lista-enl" style="margin:8px 0 18px">{rel}</ul><a class="btn btn-claro" href="../../contacto.html?servicio={sec}&amp;funcion={sl}#diagnostico">Pedir información</a></aside></div></section>""".format(
        m=migas_html, st=sec_titulo, h1=c["h1"], lead=c["lead"], sec=seccion, sl=slug, stl=sec_titulo if sec_titulo.split()[0] in ("WhatsApp", "PIX", "CRM", "ERP", "IA") or sec_titulo[:2].isupper() else sec_titulo[0].lower() + sec_titulo[1:], resp=c["respuesta"], secs=secs, faq=faq_html, rel=rel)

# Lotes de páginas de función reescritas (octubre 2026)
import importlib as _il
for _n in range(1, 11):
    PAGINAS.update(_il.import_module("funciones_lote_%d" % _n).PAGINAS)
