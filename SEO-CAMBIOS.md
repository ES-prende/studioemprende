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
- [ ] Datos reales: precio del fichador, plazos por servicio, casos de clientes citables y capturas del programa.
- [ ] Bloque 1, tandas 1-12 (reescritura del Anexo C primero).
- [ ] Bloque 2: enlaces contextuales cruzados entre familias y desde los grupos de canibalización.
- [ ] Bloque 3: "CRM para autónomos" (precio), "agentes IA WhatsApp", páginas de precio y comparativas, casos de éxito (solo con datos reales), categorías del blog.
- [ ] Bloque 3 bis: SVG animados en hoja de estilos aparte, solo fuera del Anexo A.
- [ ] Tras fusionar: reenviar `sitemap.xml` en Search Console y Bing.
