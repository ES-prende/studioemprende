# Auditoría SEO · por qué no se indexaban y qué se ha corregido

Fecha: 26/10/2026. Datos: Search Console (rendimiento hasta el 24/10 y cobertura hasta el 19/10), rastreo en vivo de las 280 URLs no indexadas y auditoría on-page de la web construida. Las 111 indexadas no se han tocado (comprobado byte a byte).

## Resumen ejecutivo

La web no tenía ningún bloqueo técnico: todas las URLs no indexadas responden 200, son `index,follow`, tienen canonical propio y están en el sitemap. **Google las había descubierto pero había decidido no rastrearlas**, por cuatro motivos que se suman:

1. **Contenido de plantilla en el momento del descubrimiento (12-13/10).** Las 264 páginas de función se publicaron con el mismo bloque genérico («Cómo lo trabajamos… Analizamos cómo lo haces hoy…») y una entradilla automática. Google rastreó unas pocas, vio páginas casi idénticas y bajó la prioridad de todo el patrón de URL. Es el motivo principal.
2. **Dominio de dos semanas, sin enlaces externos y con 409 URLs de golpe.** Google asigna poco presupuesto de rastreo a un dominio nuevo sin autoridad; 400 URLs son muchas para ese presupuesto.
3. **Cambios de URL y de indexación en los primeros días.** El 12/10 se pasó de `.html` a URLs limpias con 301 y se borraron 23 páginas; el 15/10 hubo 14 minutos con `noindex` en 269 páginas de servicio. Cada cambio hace que Google espere.
4. **Cadenas de redirección en los hubs.** `/servicios/fichador.html` (la URL del primer sitemap) pasaba por dos 301 antes de llegar a `/servicios/fichador/` (tres desde http o www). Los 15 hubs de familia ni siquiera figuraban como descubiertos.

**Ya hay señales de que se está desatascando:** indexadas de 111 a 118 (17/10), «rastreadas sin indexar» de 3 a 2, y 8 páginas que no estaban indexadas reciben ya impresiones (el blog del agente de IA para WhatsApp, 54 impresiones en posición 40; el LMS; 5 guías y servicios). Las impresiones diarias han pasado de 35 a 226. Todo esto **antes** de que Google vea el contenido nuevo: la cobertura es del 19/10 y las ampliaciones empezaron el 20/10.

**Valoración:** la base técnica es buena y el contenido ya no es el problema. Lo que queda es tiempo de rastreo y autoridad externa (Bloque 5).

## Qué se ha corregido (solo páginas no indexadas)

| Causa | Corrección | Estado |
|---|---|---|
| Contenido de plantilla | Ejemplo aplicado propio, 2 FAQ nuevas, precio y plazo en 291 páginas; Anexo C reescrito; 1.346 palabras de mediana | Hecho |
| Canibalización | 29 grupos de intención enlazados entre sí; títulos y H1 diferenciados en 7 páginas | Hecho |
| Poco enlace interno | Mínimo 3 enlaces entrantes en cada página (salvo legales); malla por grupo; casos y temas | Hecho |
| Cadena de 301 en hubs | Regla en `.htaccess`: `.html`, `/index.html`, sin barra, http y www → URL final con barra **en un solo salto** | Hecho, a comprobar en vivo tras publicar |
| Hubs sin descubrir | Títulos y H1 de 8 hubs orientados a su búsqueda (fichador, alojamientos, automatización, ciberseguridad, consultoría, migraciones, relevo, startups) | Hecho |
| Sin señal de prioridad | Un sitemap por familia con el hub primero; `lastmod` real por página | Hecho |
| Autoridad cero | Kit de enlaces externos para Sandra | Pendiente (fuera de la web) |
| Recrawl | Cola diaria de envíos a Google (10/día) y Bing (100/día); IndexNow en cada despliegue | Pendiente de publicar |

## Oportunidades de keyword (consultas reales de Search Console)

| Consulta | Impr. | Pos. | Página que la ataca | Acción |
|---|--:|--:|---|---|
| agentes ia whatsapp (+ empresas, business api) | 36 | 22-82 | `/servicios/whatsapp-ia/` y `/blog/agente-de-ia-para-whatsapp` | Hub reorientado; blog ya indexado |
| crm para autónomos / crm autónomos | 31 | 65-67 | `/blog/crm-para-autonomos` (indexada) | Apoyada con el artículo nuevo de cuánto cuesta un CRM |
| erp para pymes: cuándo dejar de usar excel / dejar de usar excel para facturar | 25 | 64-85 | `/blog/que-es-un-erp-y-cuando-lo-necesito` | Título cambiado a la consulta exacta |
| calcular crédito fundae / cómo saber el crédito de formación / alta de cursos fundae | ~35 | 77-95 | — | **Artículo nuevo** `/blog/como-calcular-el-credito-de-formacion-fundae` |
| software para startups | 11 | 33 | `/servicios/startups-e-inversores/` | Título y H1 reorientados |
| hogar inteligente de lujo / tecnología viviendas de lujo | 16 | 15-21 | Páginas indexadas | Sin cambios (ya posicionan) |
| software / emprendedor / qué es software | 300+ | 50-78 | Guías indexadas | No atacar: términos genéricos imposibles sin autoridad |

## Checklist técnico

| Comprobación | Estado | Detalle |
|---|---|---|
| Respuesta HTTP de las no indexadas | Pass | 275 × 200; 4 duplicados con canonical a su versión principal; 1 × 301 (URL antigua) |
| `noindex` o `X-Robots-Tag` | Pass | Ninguno en páginas indexables |
| Canonical | Pass | Propio en todas, salvo los 4 duplicados previstos |
| robots.txt y sitemaps | Pass | Sin bloqueos; índice con 30 sitemaps hijos |
| Redirecciones | Pass (tras publicar) | Hubs en un solo salto |
| Enlaces rotos | Pass | 0 en toda la web |
| JSON-LD | Pass | Válido en todas; las FAQ del schema coinciden con las visibles |
| Títulos y metas | Pass | Únicos; sin truncar salvo legales (metas cortas en aviso legal, cookies y privacidad, sin impacto) |
| Imágenes | Pass | `alt`, `width` y `height` en todas; WebP en lo nuevo |
| Velocidad | Pass | 236 ms de TTFB, 64 KB, CLS 0 |

## Plan de acción

**Esta semana (tras publicar):**
1. Reenviar `sitemap.xml` en Search Console y Bing Webmaster Tools.
2. Comprobar en vivo que `/servicios/fichador.html` llega a `/servicios/fichador/` en un solo 301.
3. Empezar la cola de `seo/COLA-INDEXACION.md`: los 10 primeros días, hubs y páginas nuevas.
4. En Search Console → Indexación → Páginas → «Descubierta: actualmente sin indexar» → **Validar corrección**.

**Este trimestre:**
1. Enlaces externos (kit de Sandra): primero contratalux.com hacia el caso, después el Perfil de Empresa y LinkedIn.
2. Revisar cada semana en Search Console el paso de «Descubierta» a «Indexada», sección por sección gracias a los sitemaps por familia.
3. Proponer cambios en las indexadas solo con datos (ver `seo/PROPUESTAS-INDEXADAS.md`).

**Expectativa realista:** de 2 a 6 semanas para ver la mayoría de las páginas rastreadas tras publicar, y de 2 a 3 meses para posiciones estables. Sin enlaces externos irá más lento.
