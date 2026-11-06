# Propuestas SEO · 6/11/2026

Datos: Search Console (cobertura y rendimiento a 6/11, últimos 3 meses) y PageSpeed del 6/11.

## 1. Errores de Search Console y estado

| Aviso | Páginas | Qué es | Acción |
|---|--:|---|---|
| Descubierta: actualmente sin indexar | 284 | Google las conoce pero aún no las ha rastreado. No es un fallo técnico. | Validación ya iniciada. Esperar; seguir la cola diaria. |
| Rastreada: actualmente sin indexar | 2 | Las dos páginas de PIX (inteligencia conectada y casos por sector), reescritas el 24/10. | Pulsar **Validar corrección** (no está iniciada). Pedir indexación de las dos. |
| Página con redirección | 1 | `http://studioemprende.com/` → `https://`. Es correcto. | Ninguna. |
| PageSpeed: `main.js` sin caché | — | El servidor lo sirve como `text/javascript` y la regla de caché solo cubría `application/javascript`. | **Corregido** (7 días, comprobado en vivo). |

Evolución: indexadas 111 → 125; impresiones diarias de 35 a ~280; posición media de 65 a 42. 22 páginas que no estaban en la lista original ya reciben impresiones y quedan protegidas (141 en total).

## 2. Mejoras que tocan la plantilla común (necesitan tu permiso)

Cambian todas las páginas, también las indexadas, aunque no tocan títulos, textos ni URLs.

| Cambio | Efecto |
|---|---|
| Texto del enlace del aviso de cookies: «Más información» → «Más información sobre cookies» | SEO de Lighthouse de 92 a 100 |
| Cargar Google Tag Manager después de la primera interacción o a los 3 s | LCP en móvil de 4,2 s a ~2,5 s; rendimiento móvil de 81 a 90+ |

## 3. Artículos nuevos (consultas reales sin página propia)

Ordenados por impresiones. Ninguno pisa a una página indexada: atacan una intención distinta y enlazan a la guía existente.

| Artículo propuesto | Consultas que lo piden | Impr. | Pos. actual |
|---|---|--:|--:|
| Cómo solicitar la bonificación de FUNDAE paso a paso (y qué hacer si es urgente) | fundae como solicitar, bonificación fundae urgente, crédito formativo como solicitar, consultoría fundae presupuesto, empresa bonificada | ~150 | 50-70 |
| Ejemplos de ERP para pymes por sector | ejemplos erp, erp ejemplos, que es un erp ejemplos, tipos de erp, siglas erp | ~120 | 75-85 |
| Préstamos y ayudas ENISA para jóvenes emprendedores | préstamos para jóvenes emprendedores, financiación jóvenes emprendedores, enisa jóvenes emprendedores | ~50 | 43-92 |
| Cuánto cuesta mantener una página web al año | cuanto cuesta mantener una pagina web, precio paginas web | ~20 | 96 |
| SaaS o software a medida: cuál elegir | saas, saas erp, software para startups | ~45 | 36-80 |
| Cómo implantar IA en una empresa pequeña: plan de 30 días | implementar ia empresa pequeña, curso ia coste | ~15 | 75-84 |
| Integrar Holded con HubSpot (y cuándo conviene unificar) | integración holded hubspot | 6 | 91 |
| Programa de gestión para centros deportivos y de ocio | programa gestión centro deportivo, gestion centros de ocio | ~8 | 22-80 |

Ya hay artículos nuevos posicionando bien: el de crédito FUNDAE está en posición 19 en dos semanas.

## 4. Especificar mejor los servicios

Hoy los servicios están repartidos en 24 familias y 264 fichas. Quien llega no ve en un solo sitio qué haces, para quién, cuánto tarda y cuánto cuesta.

1. **Página nueva «Catálogo de servicios»** (`/catalogo-de-servicios`): una tabla por familia con qué incluye, para quién es, plazo y precio. Sin precios en CRM, programa de gestión y ERP. Schema `OfferCatalog` con cada servicio. Se enlaza desde páginas no indexadas y temas.
2. **Páginas de servicio por sector, pocas y con datos** (máximo 6): instaladores, clínicas, despachos, alojamientos turísticos, comercio y formación. Cada una con el paquete típico de módulos, un ejemplo y FAQ propias. Solo cuando la mayoría de las 284 actuales estén indexadas.
3. **Comparativas** «Studio Emprende vs Holded / Clientify / Odoo»: necesitan precios y funciones de terceros verificados el día de publicar.
4. **Plazos de implantación** de los servicios a medida: hoy dicen «fases y fechas en la propuesta». Con un rango real (por ejemplo, «CRM básico en 3-5 semanas») la ficha gana concreción. Falta el dato.

## 5. Lo que tienes que hacer tú en Search Console

1. Indexación → Páginas → «Rastreada: actualmente sin indexar» → **Validar corrección**.
2. Inspeccionar URL y pedir indexación: `/servicios/pix/inteligencia-conectada`, `/servicios/pix/casos-por-sector` y `/blog/software-de-gestion-modular-con-automatizaciones`.
3. Seguir la cola de `seo/COLA-INDEXACION.md` (10 URLs al día).
4. Enlace desde contratalux.com a `https://studioemprende.com/casos/contratalux`: es el enlace externo más fácil de conseguir.
