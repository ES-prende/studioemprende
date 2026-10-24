# Precio del fichador (dato de Studio Emprende, 24/10/2026). Precios sin IVA.
CUOTA = 8          # € por empleado y mes
CUOTA_GRUPO = 5    # € por empleado y mes, precio de grupo para plantillas grandes
TERMINAL = 300     # € pago único, terminal físico opcional

# Dónde se muestra: páginas no indexadas de la familia del fichador y relacionadas
DESTACADO = {"servicios/fichador", "servicios/fichador/precio-por-trabajador-al-mes"}
COMPACTO_EXTRA = {"blog/app-de-control-horario-para-pequenas-empresas",
                  "servicios/software-de-gestion/fichador-y-registro-de-jornada",
                  "servicios/pequenas-empresas/cumple-la-ley-verifactu-y-registro-de-jornada"}


def aplica(clave):
    return clave in DESTACADO or clave in COMPACTO_EXTRA or clave.startswith("servicios/fichador/")


def bloque(clave):
    if clave in DESTACADO:
        return """<section class="sec" style="padding-bottom:0"><div class="w"><div class="cab"><p class="kicker">Precio del fichador</p><h2>Cuánto cuesta el fichador</h2></div>
<div class="rejilla">
<div class="tarjeta pack dest"><span class="etiqueta">Cuota mensual</span><h3>Por empleado</h3><div class="precio">{c} €</div><span class="cuota">por empleado y mes · sin permanencia</span><p>Móvil, tablet, web, NFC o WhatsApp, informe para Inspección y conservación durante 4 años.</p></div>
<div class="tarjeta pack"><span class="etiqueta">Plantillas grandes</span><h3>Precio de grupo</h3><div class="precio">{g} €</div><span class="cuota">por empleado y mes</span><p>Para empresas con muchos trabajadores o varios centros. Te lo confirmamos con tu plantilla.</p></div>
<div class="tarjeta pack"><span class="etiqueta">Opcional</span><h3>Terminal físico</h3><div class="precio">{t} €</div><span class="cuota">pago único</span><p>Para fichar en la entrada del local u obra sin usar el móvil del trabajador.</p></div>
</div>
<p class="mut" style="margin-top:16px;font-size:14px">Precios sin IVA. Ejemplo: un negocio con 6 empleados paga 6 × {c} € = {e6} € al mes; si quiere terminal físico, {t} € una sola vez. <a href="/contacto?servicio=fichador#diagnostico">Pide el precio de grupo para tu plantilla</a>.</p>
</div></section>""".format(c=CUOTA, g=CUOTA_GRUPO, t=TERMINAL, e6=6 * CUOTA)
    return """<section class="sec" style="padding-top:0"><div class="w"><div class="tarjeta" style="flex-direction:row;flex-wrap:wrap;align-items:center;gap:14px 28px">
<span class="kicker" style="margin:0">Precio del fichador</span>
<span><b style="font-weight:500">{c} € por empleado y mes</b> · precio de grupo de {g} € para plantillas grandes · terminal físico opcional, {t} € pago único · sin permanencia. Precios sin IVA.</span>
<a class="mas" href="/servicios/fichador/precio-por-trabajador-al-mes">Ver el precio →</a></div></div></section>""".format(c=CUOTA, g=CUOTA_GRUPO, t=TERMINAL)


def ofertas(dom):
    url = dom + "/servicios/fichador/precio-por-trabajador-al-mes"
    srv = {"@id": dom + "/servicios/fichador/#servicio"}
    return [{"@type": "Offer", "@id": url + "#cuota", "name": "Fichador · cuota por empleado", "url": url, "availability": "https://schema.org/InStock",
             "seller": {"@id": dom + "/#org"}, "priceCurrency": "EUR", "price": str(CUOTA),
             "priceSpecification": {"@type": "UnitPriceSpecification", "price": str(CUOTA), "priceCurrency": "EUR", "valueAddedTaxIncluded": False,
                                    "unitText": "empleado y mes", "referenceQuantity": {"@type": "QuantitativeValue", "value": 1, "unitCode": "MON"}}},
            {"@type": "Offer", "@id": url + "#grupo", "name": "Fichador · precio de grupo por empleado", "url": url, "availability": "https://schema.org/InStock",
             "seller": {"@id": dom + "/#org"}, "priceCurrency": "EUR", "price": str(CUOTA_GRUPO),
             "priceSpecification": {"@type": "UnitPriceSpecification", "price": str(CUOTA_GRUPO), "priceCurrency": "EUR", "valueAddedTaxIncluded": False,
                                    "unitText": "empleado y mes, plantillas grandes", "referenceQuantity": {"@type": "QuantitativeValue", "value": 1, "unitCode": "MON"}}},
            {"@type": "Offer", "@id": url + "#terminal", "name": "Terminal físico de fichaje", "url": url, "availability": "https://schema.org/InStock",
             "seller": {"@id": dom + "/#org"}, "priceCurrency": "EUR", "price": str(TERMINAL),
             "priceSpecification": {"@type": "PriceSpecification", "price": str(TERMINAL), "priceCurrency": "EUR", "valueAddedTaxIncluded": False}}]
