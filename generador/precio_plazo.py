# Precio y plazo por familia de servicio (Bloque 1). Solo datos publicados por Studio Emprende:
# packs (precios.html), PIX (implantacion-y-precios), formación 1 a 1 y diagnóstico gratuito. Precios sin IVA.
# Donde no hay precio público se dice claro: presupuesto cerrado tras el diagnóstico gratuito.

_PACK_GESTION = ("El programa de gestión va incluido en el pack <b style=\"font-weight:500\">Negocio en Marcha: 1.790 € + 40 €/mes</b> de soporte y mantenimiento. "
                 "Los módulos que no entren en el pack se presupuestan aparte, con precio cerrado.",
                 "De 3 a 4 semanas desde que nos pasas la información, con fecha cerrada al empezar. La migración de tus datos está incluida.")
_PIX = ("Con PIX, el agente de IA: <b style=\"font-weight:500\">desde 90 €/mes</b> para 3 personas o <b style=\"font-weight:500\">145 €/mes</b> para 5, sin permanencia ni cuota de alta. "
        "Más usuarios o integraciones a medida, con presupuesto aparte.",
        "Se empieza con un piloto de unas 4 semanas sobre un proceso concreto, con resultados medidos antes de ampliar.")
_WEB = ("<b style=\"font-weight:500\">Impulso Inicial, 990 €</b> (web One Page, Google Business y redes), <b style=\"font-weight:500\">Negocio en Marcha, 1.790 €</b> (web completa con blog y SEO) "
        "o <b style=\"font-weight:500\">Llave en Mano, 3.690 €</b> (web premium y embudo de ventas). Todos con 40 €/mes de soporte.",
        "De 2 a 3 semanas el Impulso Inicial, de 3 a 4 Negocio en Marcha y unos 2 meses Llave en Mano, desde que nos pasas la información.")
_FORMACION = ("Sesiones individuales <b style=\"font-weight:500\">desde 40 € la hora</b>. Los cursos para equipos se presupuestan según personas, horas y contenidos.",
              "Una sesión 1 a 1 se agenda en días. Un curso para el equipo, en cuanto acordamos el temario.")
_MEDIDA = ("Presupuesto <b style=\"font-weight:500\">cerrado</b> antes de empezar, después de un diagnóstico gratuito en el que vemos qué necesitas de verdad.",
           "Te damos las fases y las fechas por escrito en la propuesta, antes de que firmes nada.")

FAMILIA = {
    "software-de-gestion": _PACK_GESTION, "erp-para-pymes": _PACK_GESTION, "migraciones-e-integraciones": _PACK_GESTION,
    "automatizacion-y-datos": _PACK_GESTION, "pequenas-empresas": _PACK_GESTION, "autonomos": _WEB,
    "agentes-de-ia": _PIX, "whatsapp-ia": _PIX, "pix": _PIX,
    "webs": _WEB, "presencia-digital": _WEB,
    "formacion-ia": _FORMACION,
    "apps-moviles": _MEDIDA, "software-especializado": _MEDIDA, "ciberseguridad-y-sistemas": _MEDIDA,
    "departamento-tecnologico": _MEDIDA, "consultoria-y-ayudas": _MEDIDA, "grandes-empresas": _MEDIDA,
    "startups-e-inversores": _MEDIDA, "problemas-sin-resolver": _MEDIDA, "relevo-y-continuidad": _MEDIDA,
    "deluxe": _MEDIDA, "alojamientos-y-domotica": _MEDIDA,
}
# Páginas que ya tienen su propio precio en el contenido
EXCLUIR = {"servicios/pix/inteligencia-conectada", "servicios/pix/casos-por-sector",
           "servicios/consultoria-y-ayudas/diagnostico-de-digitalizacion-gratuito"}


def familia(clave):
    p = clave.split("/")
    return p[1] if len(p) >= 2 and p[0] == "servicios" and p[1] in FAMILIA else None


def bloque(clave):
    f = familia(clave)
    if not f or clave in EXCLUIR or f == "fichador":
        return ""
    precio, plazo = FAMILIA[f]
    return ('<section class="sec" style="padding-top:0"><div class="w"><div class="rejilla">'
            '<div class="tarjeta"><p class="kicker" style="margin:0">Precio</p><p>%s</p><a class="mas" href="/precios">Ver precios y packs →</a></div>'
            '<div class="tarjeta"><p class="kicker" style="margin:0">Plazo</p><p>%s</p><a class="mas" href="/contacto?servicio=%s#diagnostico">Pedir diagnóstico gratis →</a></div>'
            '</div></div></section>') % (precio, plazo, f)
