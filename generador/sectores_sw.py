# Sectores y subsectores para la guía "software a medida por sectores".
# (sector, [(subsector, qué se suele desarrollar)])
S = "../servicios/"
def a(ruta, txt): return '<a href="%s%s.html">%s</a>' % (S, ruta, txt)

SECTORES_SW = [
("Industria y fabricación", [
  ("Metal y calderería", "órdenes de fabricación, hojas de ruta por máquina y control de horas por pedido."),
  ("Alimentación y bebidas", "trazabilidad de lotes, caducidades, " + a("software-especializado/appcc-digital-para-hosteleria-y-alimentacion", "APPCC digital") + " y etiquetado."),
  ("Química y plásticos", "fichas de seguridad, recetas de producción y control de calidad por lote."),
  ("Madera y mueble", "configurador de producto a medida, despiece y planificación de taller."),
  ("Textil y confección", "tallas y colores por artículo, pedidos de temporada y control de talleres externos."),
  ("Artes gráficas e imprenta", "presupuestador por tirada y acabados, y seguimiento de cada trabajo en máquina."),
  ("Industria auxiliar y automoción", "planificación ajustada a pedidos del cliente, " + a("software-especializado/gestion-de-calidad-iso-sin-papel", "calidad ISO sin papel") + " y " + a("software-especializado/huella-de-carbono-para-proveedores", "huella de carbono") + " para grandes clientes."),
]),
("Construcción y reformas", [
  ("Constructoras", a("software-de-gestion/obras-y-proyectos-presupuesto-frente-a-real", "obras con presupuesto frente a real") + ", certificaciones y " + a("software-especializado/coordinacion-de-actividades-empresariales-cae", "CAE") + " con subcontratas."),
  ("Empresas de reformas", a("software-de-gestion/presupuestos-desde-mediciones", "presupuestos desde mediciones") + ", fotos de antes y después y cobros por hitos."),
  ("Instaladores eléctricos, fontanería y climatización", a("software-de-gestion/ordenes-y-partes-de-trabajo-con-firma-y-fotos", "partes de trabajo con firma") + ", " + a("software-de-gestion/mantenimientos-programados", "mantenimientos programados") + " y agente de voz para urgencias."),
  ("Carpintería de aluminio y PVC", "presupuestos por medidas y perfiles, pedidos a proveedor y seguimiento de instalación."),
  ("Telecomunicaciones y fibra óptica", "órdenes por zona, materiales por técnico y certificación de instalaciones."),
  ("Promotoras", "seguimiento de compradores, cambios de acabados y postventa con incidencias."),
]),
("Inmobiliario", [
  ("Agencias inmobiliarias", "cartera conectada a portales, cruces automáticos con compradores y " + a("agentes-de-ia/agente-inmobiliario", "agente inmobiliario con IA") + "."),
  ("Administradores de fincas", "comunidades, derramas, incidencias con fotos y portal para vecinos."),
  ("Gestión de alquileres", "contratos, cobros mensuales, avisos de impago y liquidación a propietarios."),
  ("Alquiler vacacional", a("alojamientos-y-domotica/check-in-online-con-firma", "check-in online") + ", " + a("alojamientos-y-domotica/cerradura-con-codigo-por-reserva", "cerraduras con código") + " y " + a("alojamientos-y-domotica/envio-automatico-a-ses-hospedajes", "envío a SES.Hospedajes") + "."),
]),
("Despachos y servicios profesionales", [
  ("Abogados", "expedientes, plazos procesales y " + a("agentes-de-ia/revision-de-contratos-para-despachos", "revisión de contratos con IA") + "."),
  ("Gestorías y asesorías", a("agentes-de-ia/agente-documental-para-gestorias", "lectura automática de documentos") + ", calendario fiscal de clientes y " + a("software-especializado/portal-en-marca-blanca-para-gestorias", "portal con tu marca") + "."),
  ("Arquitectura e ingeniería", "proyectos por fases, horas por proyecto y control de visados y entregables."),
  ("Consultoras", "propuestas, horas imputadas, rentabilidad por cliente y base de conocimiento interna."),
  ("Asesorías energéticas", "comparador de tarifas, contratos de suministro, comisiones y renovaciones."),
  ("Corredurías de seguros", a("software-especializado/tarificador-para-corredurias", "tarificador") + ", pólizas, siniestros y renovaciones."),
]),
("Salud y bienestar", [
  ("Clínicas dentales", "agenda por gabinete, presupuestos de tratamiento y financiación, y recordatorios por WhatsApp."),
  ("Fisioterapia y rehabilitación", "bonos de sesiones, historial de evolución y reserva online."),
  ("Psicología", "agenda, notas de sesión con acceso restringido y videoconsulta."),
  ("Medicina estética", "consentimientos firmados online, fotos de seguimiento y venta de tratamientos."),
  ("Oftalmología y ópticas", "conexión de equipos de diagnóstico, graduaciones y pedidos a laboratorio."),
  ("Veterinarias", "ficha por mascota, vacunas con avisos automáticos y venta de productos."),
  ("Farmacias y parafarmacias", "encargos, fidelización y control de stock de parafarmacia."),
  ("Centros de estética y peluquerías", "agenda por profesional, bonos, comisiones y reservas online."),
]),
("Hostelería y restauración", [
  ("Restaurantes", a("software-de-gestion/tpv", "TPV") + ", reservas, escandallos y " + a("presencia-digital/menus-digitales-para-hosteleria", "carta digital") + "."),
  ("Bares y cafeterías", "comandas rápidas, cierre de caja y control de mermas."),
  ("Catering y colectividades", "menús por evento, alérgenos, compras y logística de entrega."),
  ("Hoteles y hostales", "reservas, housekeeping, upselling y registro de viajeros."),
  ("Ocio nocturno", "control de aforo, listas, reservados y venta anticipada."),
]),
("Comercio y retail", [
  ("Tiendas de barrio", "TPV con Verifactu, fidelización y pedidos por WhatsApp."),
  ("Moda y calzado", "tallas y colores, rebajas, cambios y tienda online conectada al stock."),
  ("Alimentación y supermercados", "caducidades, básculas, pedidos a proveedor y reparto a domicilio."),
  ("Ferreterías y suministros", "catálogos grandes, tarifas por cliente y venta a profesionales."),
  ("Comercio electrónico", a("software-de-gestion/tienda-online-conectada", "tienda conectada") + " a facturación, devoluciones y marketplaces."),
  ("Franquicias", "panel central con ventas de cada local, pedidos a central y manuales de operación."),
]),
("Distribución, transporte y logística", [
  ("Mayoristas y distribuidores", a("software-especializado/portal-de-pedidos-b2b", "portal de pedidos B2B") + " y " + a("apps-moviles/app-de-catalogo-y-pedidos-para-distribuidores", "app para comerciales") + "."),
  ("Transporte de mercancías", a("software-de-gestion/planificacion-de-rutas", "rutas") + ", albaranes con firma y " + a("software-de-gestion/gestion-de-flotas", "flota") + "."),
  ("Mensajería y última milla", "asignación de repartos, prueba de entrega con foto y avisos al destinatario."),
  ("Almacenes y operadores logísticos", "ubicaciones, preparación de pedidos y lectura de códigos; ver " + '<a href="erp-para-logistica-y-almacen.html">gestión de almacenes</a>' + "."),
  ("Logística de frío", "registro de temperaturas, alertas y trazabilidad por lote."),
]),
("Automoción y movilidad", [
  ("Talleres mecánicos", "órdenes de reparación, ficha de vehículo por matrícula, recambios y avisos de ITV o revisión."),
  ("Concesionarios y compraventa", "stock de vehículos, tasaciones, financiación y postventa."),
  ("Alquiler de vehículos", "reservas, contratos, daños con fotos y disponibilidad de flota."),
  ("Recambios", "catálogo por referencia y vehículo, pedidos de taller y devoluciones."),
]),
("Agricultura, ganadería y agroalimentación", [
  ("Explotaciones agrícolas", "cuaderno de campo digital, tratamientos y costes por parcela."),
  ("Cooperativas", "entradas de socios, liquidaciones y trazabilidad hasta el cliente."),
  ("Ganadería", "registro de animales, sanidad, alimentación y producción."),
  ("Bodegas y almazaras", "control de depósitos, embotellado, lotes y venta directa online."),
]),
("Educación y formación", [
  ("Academias", "matrículas, cuotas, asistencia y comunicación con familias."),
  ("Autoescuelas", "clases prácticas por profesor y vehículo, tests y seguimiento de alumnos."),
  ("Centros de formación para empresas", a("software-especializado/plataforma-de-formacion-interna-lms", "plataforma de formación") + ", diplomas y gestión de bonificaciones."),
  ("Escuelas infantiles", "agenda diaria para familias, comedor y recibos domiciliados."),
]),
("Deporte y ocio", [
  ("Gimnasios y centros deportivos", "socios, cuotas, control de acceso y reserva de clases."),
  ("Clubes y escuelas deportivas", "fichas de jugadores, equipos, cuotas y comunicaciones."),
  ("Actividades y turismo activo", "reservas por horario, guías asignados y venta online."),
  ("Organización de eventos y bodas", "presupuestos, proveedores, invitados y cronograma del evento."),
]),
("Turismo y viajes", [
  ("Agencias de viajes", "presupuestos de viaje, reservas con proveedores y documentación al cliente."),
  ("Receptivo y excursiones", "conexión con plataformas de reservas, asignación de guías y vehículos."),
]),
("Servicios a empresas y particulares", [
  ("Limpieza", "rutas de personal, " + a("fichador/geolocalizacion-con-aviso-al-trabajador", "fichaje con ubicación") + " y control de calidad por cliente."),
  ("Mantenimiento y servicio técnico", a("software-de-gestion/app-para-tecnicos-de-campo", "app para técnicos de campo") + " y contratos de mantenimiento."),
  ("Seguridad y vigilancia", "cuadrantes, rondas registradas e incidencias."),
  ("Jardinería y piscinas", "visitas periódicas, productos usados y facturación recurrente."),
  ("Lavanderías y tintorerías", "seguimiento de prendas, avisos de recogida y suscripciones."),
]),
("Social, asistencial y asociaciones", [
  ("Residencias y centros de día", "planes de atención, medicación, turnos de personal y comunicación con familias."),
  ("Ayuda a domicilio", "rutas de cuidadores, fichaje en domicilio y partes de servicio."),
  ("ONG y asociaciones", "socios, cuotas, donaciones, voluntariado y justificación de subvenciones."),
]),
("Energía y medio ambiente", [
  ("Instaladores de placas solares", "estudios de ahorro, presupuestos, legalización y mantenimiento."),
  ("Gestión de residuos", "recogidas programadas, pesajes, documentación de traslado y facturación por servicio."),
  ("Eficiencia energética", "auditorías, informes y seguimiento de consumos con sensores."),
]),
("Tecnología, medios y startups", [
  ("Empresas de software y SaaS", "panel de clientes, suscripciones y " + a("startups-e-inversores/metricas-para-inversores", "métricas para inversores") + "."),
  ("Agencias de marketing y productoras", "proyectos, horas, aprobaciones del cliente y facturación por entregable."),
  ("Startups", a("startups-e-inversores/mvp-en-6-12-semanas", "MVP") + " y " + a("startups-e-inversores/cto-externalizado", "CTO externalizado") + "."),
]),
]
