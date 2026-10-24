# SEO · registro de cambios

Trabajo sobre las instrucciones SEO del 24/10/2026 (datos de Search Console del 16/10/2026).
Rama: `seo-indexacion`. Nada se publica hasta fusionar en `main`.

## Regla de oro: cómo se garantiza que no se tocan las 111 indexadas

La web se genera entera con `generador/construir.py`, y cabecera, pie y estilos son comunes a todas las páginas. Por eso "no tocar" se comprueba byte a byte:

- `seo/huellas-anexo-a.json` guarda el SHA-256 de cada una de las 111 URLs del Anexo A.
- `python3 seo/scripts/proteger.py` falla si alguna ha cambiado. **Se ejecuta después de cada build y antes de cada commit.**
- Consecuencia práctica: no se cambia nada común (menú, pie, `estilos.css`). Lo nuevo va en bloques que solo se insertan en páginas que no están en el Anexo A, y en hojas de estilo aparte.

## Hecho

| Fecha | Bloque | Cambio | Commit |
|---|---|---|---|
| 24/10 | 1 | Tabla de priorización: 300 páginas en 12 tandas de 25, keyword principal por URL, 29 grupos de canibalización y qué le falta a cada una (`seo/PRIORIZACION.md`, `seo/priorizacion.csv`). | `279a80f` |
| 24/10 | 1 | Scripts de medición reutilizables (`seo/scripts/medir.py`, `seo/scripts/tabla.py`). | `279a80f` |
| 24/10 | 4 | Un sitemap por familia de servicio (24) más páginas, guías y blog. El hub de cada familia es la primera URL de su sitemap. Siguen siendo exactamente las mismas 410 URLs. | `dd625af` |
| 24/10 | 4 | 301 de `sitemap-funciones.xml` y `sitemap-servicios.xml` al índice `sitemap.xml`. El despliegue no borra archivos del servidor, así que sin esto quedarían allí con contenido viejo. | `dd625af` |
| 24/10 | — | Control de las 111 indexadas (`seo/scripts/proteger.py`). | `dd625af` |
| 24/10 | 3 · 3 bis | Sección nueva y plana `/casos/` (hub + `/casos/contratalux`), con sitemap propio `sitemap-casos.xml`. Caso real ContrataLux: 1.590 palabras, Article + VideoObject + 4 ImageObject + FAQPage + BreadcrumbList. Capturas WebP 1280×720 con `width`/`height`/`lazy`, clip de 20 s (734 KB, sin audio, `preload="none"`, póster WebP) y línea de tiempo SVG animada con `IntersectionObserver` y `prefers-reduced-motion`. Estilos y script propios (`casos.css`, `casos.js`), no se cargan en el resto de la web. | ver git log |
| 24/10 | 2 | Bloque "Caso real" con enlace a `/casos/contratalux` en 12 páginas no indexadas relacionadas (presencia digital, SEO programático, redes, dominios, correo, comisiones, cuadro de mando, software especializado, PIX, packs, sobre nosotros). | ver git log |
| 24/10 | 3 | Nota discreta en el caso: «Proyecto desarrollado para una empresa del mismo grupo». | `bb10637` |
| 24/10 | 1 · Anexo C | Reescritura a fondo de las 3 «rastreadas sin indexar»: **PIX inteligencia conectada** (nuevo ángulo «IA conectada a tu ERP y CRM», diferencia con IA privada, ejemplo real en ContrataLux, precio 90/145 €/mes, piloto de 4 semanas), **PIX casos por sector** (tabla de primer proceso y métrica por sector, caso real, 5 FAQ propias) y **LMS** (ángulo de formación obligatoria auditable, comparativa con Moodle y plataformas genéricas). | `5f3f11b` |
| 24/10 | 2 | Malla de los 29 grupos de intención: 93 páginas no indexadas enlazan a las de su grupo con su keyword como anchor (máx. 6). Enlaces contextuales hacia las 29 páginas que tenían menos de 3 entradas: ahora solo aviso legal y cookies tienen 2 (más el pie). Mediana de enlaces entrantes: de 5 a 6. | `048c0bb` |
| 24/10 | 3 | Hub `/servicios/whatsapp-ia/` orientado a «agentes de IA para WhatsApp» (consulta en posición 22,5): título, H1, qué hace y qué no, precio real y por dónde empezar. El nombre en los menús no cambia. | `46f054a` |
| 24/10 | 3 | Artículo nuevo **«Cuánto cuesta un CRM para autónomos en 2026»** (apoya a `/blog/crm-para-autonomos`, posición 67, sin tocarla): tres modelos de precio, costes ocultos, fórmula a 24 meses y precios reales de Studio Emprende. Portada propia en la paleta de marca. Los artículos nuevos van en `blog_nuevos.py` y **no entran en portada, índice del blog, mapa web ni "otros artículos"** de los posts indexados. | `34f88fc` |
| 24/10 | 3 | Sección `/temas/`: hub y 6 temas del blog (IA, gestión y CRM, normativas, formación, webs, emprender), con CollectionPage + ItemList y `sitemap-temas.xml`. | `43f4741` |
| 24/10 | 1 | Títulos y H1 diferenciados en 7 páginas canibalizadas: previsión de ventas, chatbot para página web, recordatorios de cobros y entregas, resumen semanal, control de costes, cobros pendientes y cubrir ausencias. | `8070313` |
| 24/10 | 6 | Cola de envío a indexación (`seo/COLA-INDEXACION.md`): 310 URLs, 31 días en Google (10/día) y 4 en Bing (100/día), empezando por lo nuevo y los hubs sin descubrir. | ver git log |
| 24/10 | 5 | Kit para Sandra (`seo/BLOQUE5-SANDRA.md`): datos NAP idénticos, textos corto, medio y largo, y orden de directorios y enlaces. | ver git log |

## Revisado y ya estaba bien (no se cambia)

- **http → https y www → sin www**: un solo 301, comprobado en vivo. También `.html` → URL limpia.
- **`lastmod` real**: ya se calcula por hash del contenido de cada página (`generador/fechas.json`). Si hoy todas marcan 20/10 es porque ese día cambió la plantilla común y se modificaron todas. A partir de ahora cada página tendrá su fecha según cambie.
- **IndexNow**: ya se avisa en cada despliegue (`generador/scripts/indexnow.py`). Condición: construir en local y commitear `web/` y `generador/fechas.json`, como se ha hecho siempre. Si se commitea sin construir, el aviso no detecta los cambios.
- **Velocidad**: 236 ms de TTFB, 64 KB transferidos, CLS 0, gzip y caché activos (medido en vivo el 24/10). **Cloudflare no hace falta por ahora.** La API pública de PageSpeed agotó su cuota diaria; conviene repetir la medición en pagespeed.web.dev.
- **404**: la web devuelve 404 real con página propia.
- **Huérfanas**: no hay ninguna. Todas las páginas del Anexo B reciben al menos un enlace desde el contenido de otra página (mediana 5; las indexadas, 8). Las que menos reciben están marcadas en la tabla.

## Descartado y por qué

- **Capa programática servicio × localidad (forgenex `/sevilla/`)**: descartada por ahora. El diagnóstico es que sobran URLs para un dominio de 2 semanas sin enlaces externos, y añadir 600 casi iguales lo agrava; Google suele tratarlas como páginas puerta. Además Studio Emprende es 100 % online. Se puede reconsiderar como servicio × sector, pocas páginas, cuando lo actual esté indexado.
- **Añadir los hubs al menú o al pie**: cambiaría las 111 indexadas. Va en la lista de propuestas.
- **Fusionar páginas canibalizadas**: prohibido por las instrucciones. Se diferencian por keyword y ángulo (ver tabla).

## Hallazgos importantes

1. **El contenido de las no indexadas ya es comparable al de las indexadas.** Mediana de 1.000 palabras y 6 FAQ, títulos y descripciones únicos, solapamiento de texto muy bajo (0,012). Se amplió el 15/10 y el 20/10, después de la última foto del índice (16/10), así que **Google todavía no ha visto la mayor parte**.
2. **Lo que de verdad les falta**: precio (solo el 7 % lo menciona), plazos (18 %), ejemplos concretos, algo visual y más enlaces entrantes.
3. **25 URLs del sitemap aún no las ha descubierto Google**, entre ellas 15 hubs de familia (`/servicios/fichador/`, `/servicios/whatsapp-ia/`...). Van primero en la cola de envío manual.
4. **La página "Precio del fichador por trabajador" no tiene precio.** No hay ningún precio del fichador en el generador.

## Pendiente

- [ ] Revisión de la tabla de priorización por parte de Sandra.
- [ ] Datos reales: precio del fichador y plazos por servicio. (Caso citable y capturas: hecho con ContrataLux.)
- [x] Anexo C reescrito.
- [ ] Bloque 1, tandas 1-13: añadir precio, plazo y ejemplo a cada página (pendiente de los datos de Sandra).
- [x] Bloque 2: malla de grupos de intención y enlaces hacia las páginas poco enlazadas.
- [x] Bloque 3: caso de éxito, CRM para autónomos (precio), agentes IA WhatsApp y temas del blog.
- [ ] Bloque 3: comparativas tipo «Holded vs …» (necesitan precios y funciones de terceros verificados en la fecha de publicación).
- [x] Bloque 3 bis: SVG animado, WebP y vídeo con póster en /casos/ (hoja y script propios).
- [ ] Bloque 3 bis: extender las ilustraciones SVG a los hubs no indexados.
- [ ] Tras fusionar: reenviar `sitemap.xml` en Search Console y Bing.
