# Brief de reescritura «dolores primero» (noviembre 2026)

Web: studioemprende.com (Studio Emprende · «Tu negocio, llave en mano»). Público: personas con una idea de negocio, autónomos y negocios que empiezan, y pymes que ya funcionan. Tono: cercano, de tú, español de España, frases claras, sin jerga ni anglicismos innecesarios.

## Qué hay que hacer
Reescribir, **una por una**, las páginas de la familia asignada. Cada página ya tiene contenido útil (título, H1, respuesta corta, secciones, FAQ): **eso se conserva**. Lo que se añade/cambia por página es una entrada en `generador/dolores_<familia>.py` (guiones bajos en el nombre, p. ej. `dolores_software_de_gestion.py`) con:

- `lead`: nueva entradilla (sustituye a la actual). Empieza por el **dolor o la situación concreta de la persona**, no por el producto. 35–60 palabras. Incluye la búsqueda principal de la página de forma natural.
- `bloque`: HTML propio de esa página, 260–420 palabras, que conecta con los problemas reales de quien busca eso y le explica cómo se resuelve. Se inserta justo después de la cabecera y la «respuesta corta».
- `faq`: 2 o 3 preguntas nuevas `(pregunta, respuesta)` tal como las buscaría una persona en Google o se las haría a un asistente de IA («¿cómo…?», «¿cuánto tarda…?», «¿qué pasa si…?»). No repetir las que la página ya tiene. Texto plano, sin HTML.
- `estructura`: etiqueta corta que describe el recorrido elegido (sirve al validador).
- `meta` (opcional): solo si la metadescripción actual es floja; máximo 155 caracteres.

**No se cambian** URL, título ni H1. No se toca ningún otro archivo.

Ejemplo real y formato exacto: `generador/dolores_whatsapp_ia.py`. Léelo entero antes de empezar.

## Método, página a página
1. Lee el texto actual: `python3 seo/scripts/texto_pagina.py servicios/<familia>/<slug>` (admite varias rutas). Lee también su ficha en el plan: `grep -n "<slug>" /Users/Oficina/Downloads/STUDIO_EMPRENDE_PLAN_UNICO_PARA_CLAUDE_2026-11-15.md` y lee esas ~12 líneas con `sed -n`. De la ficha interesa «Problema y diferenciación», «Pregunta AEO candidata» y «Prueba de valor»; la «entradilla propuesta» del plan es una plantilla repetida: **no la copies**. Si la página tiene borrador completo en el anexo del plan (líneas 3888–4313: 12 «REESCRITURA n»), aprovecha sus ideas.
2. Piensa quién busca esa página, qué le duele hoy (tiempo, dinero, miedo a una multa, clientes que se van, desorden, dependencia de una persona…) y qué palabras usa.
3. Escribe la entrada. **No repitas información que la página ya da**: el bloque aporta lo que falta (la situación de la persona, por qué ocurre, cómo saber si es su caso, qué cambia, límites, cuándo no compensa, cómo empezar).
4. Pasa a la siguiente. No generes las páginas con un bucle ni con una plantilla de texto: cada una se redacta a mano.

## Cada página, una estructura distinta
Google no debe ver páginas clónicas. Dentro de tu lote **no puede haber dos bloques con la misma secuencia de elementos HTML ni con el mismo planteamiento**. Combina y varía recursos como estos (son ideas, inventa más):
frases literales del dueño entre comillas · escena de un día concreto · tabla «hoy / después» · tabla por perfiles o por tamaño de negocio · cuenta con tus propios números (sin cifras inventadas) · lista de síntomas para reconocerse · preguntas para autodiagnosticarse · errores habituales y su coste · línea de tiempo de un proceso · «mito / realidad» · qué mirar antes de contratar · comparación de alternativas (hacerlo a mano, Excel, programa genérico, a medida) · cuándo NO te hace falta · lo que no hace o no le dejamos hacer · primeras dos semanas paso a paso · ejemplo hipotético de un sector concreto (etiquetado «Ejemplo hipotético») · glosario mínimo en lenguaje llano · qué pedirle a tu gestor/proveedor · señales de que ya vas tarde.
Varía también el número de apartados (1 H2 + 1–3 H3), su orden, y los sectores de los ejemplos (clínica, taller, reformas, academia, tienda, hostelería, despacho, distribuidora, inmobiliaria, alojamiento…). Los titulares (H2/H3) no pueden repetirse entre páginas ni empezar todos igual.

## SEO, GEO y AEO
- Muchas palabras clave, pero naturales: la búsqueda principal más variantes y sinónimos reales (cómo lo diría un autónomo, cómo lo diría un gerente), términos relacionados, sectores y casos de uso. Nada de listas de keywords ni relleno.
- Un H2 del bloque en forma de problema o pregunta real. Respuestas directas en la primera frase de cada apartado (para fragmentos y asistentes de IA).
- 2–4 enlaces internos por bloque hacia páginas que existen, con texto ancla descriptivo y **ruta absoluta sin .html** (p. ej. `/servicios/fichador/turnos-y-cuadrantes`, `/guias/erp-vs-crm`, `/contacto#diagnostico`, `/precios`). Comprueba que existen (`ls web/servicios/<familia>/`). Sin parámetros `?…`.
- Evita canibalizar: fichador = registro de jornada y turnos; software-de-gestion = programa modular y CRM; erp-para-pymes = implantación de ERP; agentes-de-ia = caso de uso de un agente; pix = producto PIX; whatsapp-ia = canal WhatsApp; webs = diseño y conversión; presencia-digital = Google, SEO y captación. Si otra página trata un tema, enlázala en vez de repetirlo.

## HTML permitido
- Páginas de servicio: el bloque es una o dos `<section class="sec">` (o `sec sec-suave`) con `<div class="w">…</div>`. Dentro: `<div class="cab"><p class="kicker">…</p><h2>…</h2><p class="lead">…</p></div>`, `<h3>`, `<p>`, `<ul class="lista">`, `<ol>`, `<div class="rejilla">` con `<div class="tarjeta"><h3>…</h3><p>…</p></div>`, `<div class="tabla-wrap"><table class="tabla-norm">…`, `<div class="respuesta">…</div>`, `<blockquote>`, `<dl>`. Nada de `<h1>`, `<script>`, `<style>` ni imágenes.
- Guías, blog y temas (`guias/…`, `blog/…`, `temas/…`): comprueba primero la estructura con `texto_pagina.py`. En guías y blog el bloque va **sin `<section>`**: solo `<h2>`, `<h3>`, `<p>`, `<ul>`, `<ol>`, tablas y `<blockquote>`, porque se inserta dentro del artículo antes del primer H2. Mantén el tono informativo; el servicio se menciona al final y sin presión.

## Líneas rojas
- Nada inventado: ni cifras de clientes, ni porcentajes, ni testimonios, ni casos reales. Los ejemplos se etiquetan «Ejemplo hipotético» o se formulan como «imagina…».
- Sin promesas absolutas: prohibido «garantizamos», «100 %», «sin errores», «nunca falla», «líder», «el mejor». No prometer posiciones en Google ni cumplimiento legal automático.
- **Sin precios** en páginas de programa de gestión, CRM o ERP (familias software-de-gestion y erp-para-pymes, y cualquier mención a CRM/ERP). En el resto solo puedes citar un precio si ya aparece en la página actual; ante la duda, no pongas precio y enlaza a `/precios`.
- Studio Emprende **no es gestoría ni asesoría**: no ofrece altas de autónomo, constitución de sociedades, impuestos ni asesoramiento legal o laboral. Normativa (Verifactu, registro de jornada, protección de datos, NIS2, Ley 11/2023…): solo lo que la página ya afirma; no añadas fechas, importes de sanciones ni obligaciones nuevas.
- El diagnóstico inicial es gratuito: se puede mencionar.
- No uses las expresiones «en la era digital», «en el mundo actual», «sin duda», «no es ningún secreto», ni empieces varias entradillas igual.

## Entrega y comprobación
- Escribe el archivo completo de una vez (Python válido, `D = {}` y una asignación `D["ruta/sin/.html"] = {...}` por página, con un comentario encima que resuma la estructura elegida). Las claves son la ruta sin dominio ni `.html`.
- Valida: `python3 seo/scripts/validar_dolores.py <familia>` (familia = segundo tramo de la ruta, o `guias`, `blog`, `temas`). Corrige hasta que tu familia dé 0 avisos y 0 páginas pendientes. Los avisos que mencionen páginas de otra familia también se corrigen por tu lado.
- **No ejecutes** `generador/construir.py`, no edites `generador/construir.py` ni archivos de otras familias, y no uses git. Hay otras personas trabajando a la vez en otras familias.
- Al terminar, informa: páginas hechas, resultado del validador y cualquier duda de contenido (afirmaciones de la página actual que te parezcan dudosas, solapes entre páginas).
