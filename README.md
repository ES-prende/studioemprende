# Studio Emprende · web

Web estática de **studioemprende.com** (387 páginas: servicios, funciones, guías, blog, sectores).

## Estructura

| Carpeta | Qué contiene |
|---|---|
| `web/` | La web ya construida. Es lo que se sube al hosting. |
| `generador/` | El programa que crea la web: textos y datos (`datos.py`, `blog.py`, `guias.py`, `guias2.py`, `sectores_*.py`), plantilla (`construir.py`) y estilos (`estilos.css`). |
| `marca/` | Logos, favicon e imágenes de marca. |
| `portadas/` | Imágenes de los artículos del blog. |
| `.github/workflows/deploy.yml` | Publica la web en IONOS automáticamente en cada cambio. |

## Cambiar algo

1. Edita el texto en `generador/` (por ejemplo, una guía en `guias2.py`).
2. Haz commit en la rama `main`.
3. GitHub reconstruye la web (páginas, sitemap, robots.txt, llms.txt, enlaces) y la sube sola a IONOS.

Para construirla en tu ordenador: `python3 generador/construir.py marca web portadas`

## Conectar con IONOS (una sola vez)

En IONOS: **Hosting → SFTP y SSH** → crea un usuario SFTP.
En GitHub: **Settings → Secrets and variables → Actions → New repository secret** y crea:

| Secreto | Valor |
|---|---|
| `SFTP_HOST` | Servidor SFTP que te da IONOS (p. ej. `access-xxxx.webspace-host.com`) |
| `SFTP_USER` | Usuario SFTP |
| `SFTP_PASSWORD` | Contraseña SFTP |
| `SFTP_PATH` | Carpeta de la web en el hosting (normalmente `/`) |

Después, en la pestaña **Actions**, ejecuta «Construir y publicar en IONOS» o haz cualquier commit.
