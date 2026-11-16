"""Genera las imágenes y la guía PDF «Tu negocio en ChatGPT: Centro de empresas paso a paso».
   python3 seo/scripts/guia_chatgpt.py <captura-portada-openai.jpg> <captura-centro-empresas.jpg>
Datos: páginas oficiales de OpenAI consultadas el 16/11/2026."""
import os, sys
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader, simpleSplit
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLUG = "chatgpt-business-hub-centro-de-empresas"
P = os.path.join(R, "portadas")
BUR, OCRE, TINTA, FONDO, GRIS = "#7A2638", "#C9A961", "#1C1C1E", "#FAF7F4", "#5E5A57"
SUP = "/System/Library/Fonts/Supplemental/"
def f(n, s): return ImageFont.truetype(SUP + n, s)

# --- capturas reales, recortadas (sin datos de la cuenta) ---
a = Image.open(sys.argv[1]).convert("RGB"); a = a.crop((150, 0, 1310, 712))
b = Image.open(sys.argv[2]).convert("RGB"); b = b.crop((330, 130, 1400, 640))
a.save(os.path.join(P, SLUG + "-paso-1.jpg"), quality=88); b.save(os.path.join(P, SLUG + "-paso-2.jpg"), quality=88)

# --- portada del artículo ---
def portada(w, h):
    im = Image.new("RGB", (w, h), FONDO); d = ImageDraw.Draw(im)
    d.rectangle((0, 0, w, 14), fill=BUR)
    d.text((80, 90), "CHATGPT · CENTRO DE EMPRESAS", font=f("Arial Bold.ttf", 26), fill=OCRE)
    d.text((80, 150), "Tu negocio,", font=f("Georgia.ttf", 84), fill=TINTA)
    d.text((80, 250), "dentro de ChatGPT", font=f("Georgia.ttf", 84), fill=BUR)
    # ficha de empresa dibujada
    x, y = 80, 400
    d.rounded_rectangle((x, y, x + 620, y + 190), 22, fill="white", outline="#E4DCD4", width=2)
    d.ellipse((x + 30, y + 35, x + 110, y + 115), fill=BUR)
    d.text((x + 130, y + 38), "Tu empresa", font=f("Georgia.ttf", 40), fill=TINTA)
    d.ellipse((x + 365, y + 48, x + 397, y + 80), fill="#2F7DE1"); d.line((x + 373, y + 65, x + 379, y + 71, x + 390, y + 58), fill="white", width=4)
    d.text((x + 130, y + 92), "Perfil reclamado y verificado", font=f("Arial.ttf", 24), fill=GRIS)
    d.text((x + 30, y + 140), "Menciones · Clics a la web · Temas", font=f("Arial.ttf", 24), fill=GRIS)
    for i, (t, c) in enumerate((("1  Reclamar", BUR), ("2  Verificar", "#83503A"), ("3  Actualizar", "#8A6A1F"))):
        d.rounded_rectangle((780, 400 + i * 66, 1120, 452 + i * 66), 26, fill=c); d.text((806, 412 + i * 66), t, font=f("Arial Bold.ttf", 26), fill="white")
    d.text((80, h - 52), "studioemprende.com", font=f("Arial.ttf", 22), fill=GRIS)
    return im
g = portada(1200, 675)
g.save(os.path.join(P, SLUG + ".jpg"), quality=86); g.save(os.path.join(P, SLUG + ".webp"), quality=82)
s = g.resize((600, 338), Image.LANCZOS); s.save(os.path.join(P, SLUG + "-600.jpg"), quality=84); s.save(os.path.join(P, SLUG + "-600.webp"), quality=80)
g.crop((0, 22, 1200, 652)).save(os.path.join(P, "og", SLUG + ".jpg"), quality=86)

# --- guía en PDF, formato presentación (16:9) ---
pdfmetrics.registerFont(TTFont("G", SUP + "Georgia.ttf")); pdfmetrics.registerFont(TTFont("A", SUP + "Arial.ttf")); pdfmetrics.registerFont(TTFont("AB", SUP + "Arial Bold.ttf"))
W, H = 960, 540
out = os.path.join(R, "generador", "descargas", "guia-centro-de-empresas-chatgpt-7k2m9q.pdf")
c = canvas.Canvas(out, pagesize=(W, H)); c.setTitle("Tu negocio en ChatGPT: el Centro de empresas paso a paso"); c.setAuthor("Studio Emprende")
n = [0]
def base(kicker, titulo):
    n[0] += 1
    c.setFillColor(HexColor(FONDO)); c.rect(0, 0, W, H, fill=1, stroke=0); c.setFillColor(HexColor(BUR)); c.rect(0, H - 8, W, 8, fill=1, stroke=0)
    c.setFillColor(HexColor("#8A6A1F")); c.setFont("AB", 11); c.drawString(48, H - 46, kicker.upper())
    c.setFillColor(HexColor(TINTA)); c.setFont("G", 27); c.drawString(48, H - 82, titulo)
    c.setFillColor(HexColor(GRIS)); c.setFont("A", 9); c.drawString(48, 22, "Studio Emprende · studioemprende.com · Información de OpenAI consultada el 16/11/2026"); c.drawRightString(W - 48, 22, str(n[0]))
def texto(x, y, w, t, fn="A", sz=13.5, col=TINTA, lead=19):
    c.setFillColor(HexColor(col)); c.setFont(fn, sz)
    for l in simpleSplit(t, fn, sz, w): c.drawString(x, y, l); y -= lead
    return y
def lista(x, y, w, items, sz=13.5):
    for it in items:
        c.setFillColor(HexColor(BUR)); c.circle(x + 4, y + 4, 3, fill=1, stroke=0); y = texto(x + 16, y, w - 16, it, sz=sz) - 7
    return y
def enlace(x, y, etiqueta, url):
    c.setFont("AB", 13); wd = c.stringWidth(etiqueta, "AB", 13) + 28
    c.setFillColor(HexColor(BUR)); c.roundRect(x, y - 9, wd, 30, 15, fill=1, stroke=0); c.setFillColor(HexColor("#FFFFFF")); c.drawString(x + 14, y + 1, etiqueta)
    c.linkURL(url, (x, y - 9, x + wd, y + 21)); c.setFillColor(HexColor(GRIS)); c.setFont("A", 10); c.drawString(x + wd + 12, y + 2, url)
def img(path, x, y, w):
    im = Image.open(path); h = w * im.size[1] / im.size[0]
    c.setFillColor(HexColor("#FFFFFF")); c.setStrokeColor(HexColor("#E4DCD4")); c.roundRect(x - 6, y - 6, w + 12, h + 12, 8, fill=1, stroke=1); c.drawImage(ImageReader(path), x, y, w, h)

# 1 portada
c.setFillColor(HexColor(FONDO)); c.rect(0, 0, W, H, fill=1, stroke=0); c.setFillColor(HexColor(BUR)); c.rect(0, 0, 14, H, fill=1, stroke=0)
c.setFillColor(HexColor("#8A6A1F")); c.setFont("AB", 13); c.drawString(70, 400, "GUÍA PASO A PASO")
c.setFillColor(HexColor(TINTA)); c.setFont("G", 46); c.drawString(70, 340, "Tu negocio en ChatGPT"); c.setFillColor(HexColor(BUR)); c.drawString(70, 286, "El Centro de empresas")
texto(70, 240, 640, "Cómo reclamar el perfil de tu empresa, verificarlo y mantener tu información al día. Con los enlaces oficiales para ir haciéndolo mientras lees.", sz=16, col=GRIS, lead=23)
c.setFillColor(HexColor(GRIS)); c.setFont("A", 11); c.drawString(70, 60, "Studio Emprende · studioemprende.com · Versión del 16 de noviembre de 2026"); n[0] = 1; c.showPage()

base("Antes de empezar", "Qué necesitas tener a mano")
y = lista(48, 410, 520, ["Una cuenta de ChatGPT. Sirve la gratuita: el Centro de empresas se abre desde ella.", "Una web de tu negocio. OpenAI indica que, al principio, solo pueden reclamar su perfil los negocios con sitio web.", "Ser el dueño o estar autorizado para representar a la empresa.", "Acceso al correo de empresa o al panel del dominio (DNS), según el método de verificación que elijas.", "Para el segundo control (Persona): documento de identidad, datos registrales de la empresa y prueba de que la representas."])
c.setFillColor(HexColor("#FFFFFF")); c.setStrokeColor(HexColor("#E4DCD4")); c.roundRect(600, 190, 312, 220, 12, fill=1, stroke=1)
c.setFillColor(HexColor(BUR)); c.setFont("AB", 12); c.drawString(620, 382, "OJO SI TIENES LOCAL FÍSICO")
texto(620, 356, 272, "Según la ayuda de OpenAI, las tiendas y restaurantes locales solo pueden reclamar por ahora fichas que ya existan en Estados Unidos. Un negocio online con web sí puede ver la opción de añadirse.", sz=12.5, lead=17.5)
enlace(48, 70, "Crear cuenta de ChatGPT", "https://chatgpt.com"); c.showPage()

base("Paso 1", "Entra en la página oficial y pulsa «Reclama tu negocio»")
img(os.path.join(P, SLUG + "-paso-1.jpg"), 48, 110, 520)
texto(600, 410, 312, "La página de OpenAI explica el programa «Negocios en ChatGPT». El botón negro «Reclama tu negocio» te lleva al Centro de empresas (Business Hub).", lead=19)
texto(600, 300, 312, "También puedes abrirlo desde la barra lateral de ChatGPT, con la sesión iniciada.", col=GRIS)
enlace(48, 62, "Abrir la página oficial", "https://openai.com/es-ES/business/businesses-in-chatgpt/"); c.showPage()

base("Paso 2", "Busca tu empresa por su nombre")
img(os.path.join(P, SLUG + "-paso-2.jpg"), 48, 105, 500)
y = texto(580, 410, 332, "Con la sesión iniciada verás un buscador: «Buscar empresa». Escribe el nombre de tu negocio y elige la ficha que coincide.")
y = lista(580, y - 14, 332, ["Si no aparece y tu negocio es online, puede salir la opción de añadirlo.", "Si aparece «Contactar con soporte», la ficha está bloqueada: pide acceso desde ahí.", "Al continuar aceptas las condiciones de «Businesses in ChatGPT». Léelas antes."], sz=12.5)
enlace(48, 62, "Abrir el Centro de empresas", "https://chatgpt.com/business-hub"); c.showPage()

base("Paso 3", "Confirma la cuenta y elige cómo verificar")
texto(48, 420, 860, "Confirma con qué cuenta de ChatGPT vas a gestionar el perfil y elige uno de los métodos que te muestre la pantalla. No todos aparecen para todos los negocios.", lead=20)
for i, (t, d) in enumerate((("Correo de empresa", "Pulsa «Obtener código» e introduce el código que llega al correo asociado a tu negocio."), ("Dominio de la web", "Añade en el DNS de tu dominio el registro TXT que te muestra ChatGPT, tal cual, y pulsa «Verificar dominio». Puede tardar."), ("Teléfono de empresa", "SMS o llamada automática con un código. Solo se ofrece a algunos negocios."), ("Tienda Shopify", "«Conectar Shopify», revisa los permisos e inicia sesión en la tienda del negocio."))):
    x = 48 + i * 218
    c.setFillColor(HexColor("#FFFFFF")); c.setStrokeColor(HexColor("#E4DCD4")); c.roundRect(x, 150, 204, 200, 12, fill=1, stroke=1)
    c.setFillColor(HexColor(BUR)); c.setFont("AB", 13); c.drawString(x + 14, 322, t); texto(x + 14, 296, 176, d, sz=12, lead=16.5)
texto(48, 112, 860, "Si el dominio lo lleva otra persona (tu informático o quien te hizo la web), pásale el registro TXT para que lo añada. Los nombres de los botones pueden variar según el idioma de tu cuenta.", col=GRIS, sz=12.5)
c.showPage()

base("Paso 4", "Espera la aprobación y pasa la verificación de identidad")
y = lista(48, 415, 860, ["OpenAI revisa la solicitud y te responde por correo con la decisión o pidiendo más datos. Mientras tanto puedes cancelarla.", "Con la solicitud aprobada ya entras a tu empresa en el Centro de empresas, pero para publicar cambios, ver estadísticas o conectar un catálogo hace falta un segundo control: la verificación de identidad con Persona.", "Pulsa «Verificar con Persona» y sigue las instrucciones. Te pueden pedir documento de identidad, datos registrales y prueba de que representas a la empresa.", "El nombre, la dirección y el número fiscal deben coincidir con los registros oficiales de tu empresa.", "La insignia azul de verificado aparece cuando se aprueba la verificación con Persona, no antes."])
texto(48, y - 6, 860, "Importante: si usas Persona para crear un perfil nuevo, la aprobación de OpenAI lo publica automáticamente. Continúa solo cuando lo tengas listo.", fn="AB", sz=12.5, col=BUR)
c.showPage()

base("Paso 5", "Actualiza la información de tu negocio")
y = texto(48, 420, 420, "Abre tu perfil y revisa estos datos:", fn="AB")
lista(48, y - 8, 420, ["Web y descripción del negocio", "Categoría de producto o servicio", "Logotipo y foto de portada", "Política de envíos y de devoluciones", "Si vendes productos: catálogo en CSV o desde Shopify, con precios y disponibilidad"])
c.setFillColor(HexColor("#FFFFFF")); c.setStrokeColor(HexColor("#E4DCD4")); c.roundRect(500, 150, 412, 270, 12, fill=1, stroke=1)
c.setFillColor(HexColor(BUR)); c.setFont("AB", 12); c.drawString(520, 392, "LO QUE VERÁS EN ESTADÍSTICAS (28 DÍAS)")
lista(520, 364, 372, ["Menciones: veces que ChatGPT cita tu web. Nombrar la marca sin citar la web no cuenta.", "Clics hacia tu página.", "Temas de descubrimiento: asuntos de las respuestas donde apareces. No verás preguntas ni conversaciones de nadie.", "Un dato en blanco no significa cero: puede no haber llegado al mínimo."], sz=12)
texto(48, 112, 860, "OpenAI revisa y publica cada cambio; puede tardar en verse, y ChatGPT sigue usando también otras fuentes.", col=GRIS, sz=12.5)
c.showPage()

base("Para no llevarte sorpresas", "Lo que el Centro de empresas no hace")
lista(48, 415, 860, ["No garantiza que ChatGPT te recomiende más ni que vendas más: las respuestas siguen siendo independientes.", "La publicidad no influye en esas respuestas, y no necesitas cuenta de anuncios para reclamar tu perfil.", "Los agentes para empresas (un asistente que responde por tu negocio) solo están disponibles, de momento, para comercio electrónico y servicios online de Estados Unidos.", "Un perfil ya publicado no se puede borrar ni ocultar desde soporte; solo se eliminan los borradores.", "Cada marca se gestiona por separado: reclamar la marca principal no reclama sus locales."])
enlace(48, 108, "Ayuda oficial de OpenAI", "https://help.openai.com/en/articles/20001635-setting-up-your-business-on-chatgpt")
enlace(48, 62, "Política de Negocios en ChatGPT", "https://openai.com/policies/businesses-in-chatgpt/"); c.showPage()

base("Lista de comprobación", "Ve marcando cada paso")
yy = 410
for t in ["Tengo cuenta de ChatGPT y web del negocio", "He abierto chatgpt.com/business-hub y he buscado mi empresa", "He elegido método de verificación y lo he completado", "He recibido el correo de aprobación de OpenAI", "He pasado la verificación de identidad con Persona", "He revisado descripción, categoría, logo y políticas", "He apuntado una fecha para mirar las estadísticas dentro de un mes"]:
    c.setStrokeColor(HexColor(BUR)); c.setFillColor(HexColor("#FFFFFF")); c.roundRect(48, yy - 4, 18, 18, 4, fill=1, stroke=1); texto(80, yy, 800, t, sz=14); yy -= 36
texto(48, 122, 860, "¿Prefieres que lo hagamos contigo? En Studio Emprende preparamos la web y la información de tu negocio para que los asistentes de IA la entiendan bien.", col=GRIS, sz=12.5)
enlace(48, 58, "Pedir diagnóstico gratuito", "https://studioemprende.com/contacto#diagnostico"); c.showPage()
c.save(); print(out, n[0], "páginas")
