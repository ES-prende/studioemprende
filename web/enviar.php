<?php
// Envío de los formularios de studioemprende.com (contacto, portada, partners, landings y descarga de guías).
// Comprueba el captcha de Cloudflare Turnstile en el servidor antes de enviar nada.
// La clave secreta NO está en el repositorio: el despliegue la escribe en _config.php desde un secreto de GitHub.
header('X-Robots-Tag: noindex');
header('Cache-Control: no-store');
date_default_timezone_set('Europe/Madrid');
const DOM = 'https://studioemprende.com';
const DESTINO = 'info@studioemprende.com';
const COPIA = 'socialstudioemprende@gmail.com';
const BREVO_GUIA = 'https://eb3e1314.sibforms.com/serve/MUIFAMdw3qIhp9c2iTigkpd39NskZ7GrXJ58_MDLag9Fx8wmcGOq-Ywh3cByLvLl5ck8GGD6eHGLBrKh_ZYMGxDDD9KBsnTl3Isg5I7oAQmwIdnrVkRMh_0yYMBQF_uiLBfol6FSHM9XxKw-5mi1JWtj6LyoZwNMNnb2gcko-YIH3jkx8Bm0rMr5Uug6vmCUkjog7O_JW6Ti3chr0A==';

$json = (($_POST['tipo'] ?? '') === 'guia');
function fin($ok, $msg = '', $codigo = 200) {
    global $json;
    if ($json) { http_response_code($codigo); header('Content-Type: application/json; charset=utf-8'); echo json_encode(['ok' => $ok, 'msg' => $msg]); exit; }
    if ($ok) { header('Location: ' . DOM . '/gracias', true, 303); exit; }
    http_response_code($codigo); header('Content-Type: text/html; charset=utf-8');
    echo '<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>No se ha podido enviar</title>'
       . '<body style="font-family:system-ui,sans-serif;max-width:560px;margin:80px auto;padding:0 20px;color:#1C1C1E"><h1 style="font-weight:500">No se ha podido enviar</h1><p>'
       . htmlspecialchars($msg) . '</p><p><a href="javascript:history.back()" style="color:#7A2638">Volver al formulario</a> · <a href="https://wa.me/34601869668" style="color:#7A2638">Escribirnos por WhatsApp</a></p></body></html>';
    exit;
}
function campo($k, $max = 200) { $v = trim((string)($_POST[$k] ?? '')); $v = str_replace(["\r", "\0"], '', $v); return mb_substr($v, 0, $max); }
function linea($v) { return trim(preg_replace('/[\r\n]+/', ' ', $v)); }

if ($_SERVER['REQUEST_METHOD'] !== 'POST') { fin(false, 'Método no permitido.', 405); }
$cfg = @include __DIR__ . '/_config.php';
$secreto = is_array($cfg) ? (string)($cfg['turnstile'] ?? '') : '';
if ($secreto === '') { fin(false, 'El formulario no está disponible en este momento. Escríbenos a ' . DESTINO . '.', 503); }

// Trampas para robots
if (campo('_honey') !== '' || campo('website') !== '' || campo('email_address_check') !== '') { fin(true); }

// Captcha
$token = campo('cf-turnstile-response', 2100);
if ($token === '') { fin(false, 'Marca la comprobación de seguridad antes de enviar.', 400); }
$ip = $_SERVER['HTTP_CF_CONNECTING_IP'] ?? ($_SERVER['REMOTE_ADDR'] ?? '');
$ctx = stream_context_create(['http' => ['method' => 'POST', 'timeout' => 8, 'header' => "Content-Type: application/x-www-form-urlencoded\r\n",
    'content' => http_build_query(['secret' => $secreto, 'response' => $token, 'remoteip' => $ip])]]);
$r = @file_get_contents('https://challenges.cloudflare.com/turnstile/v0/siteverify', false, $ctx);
$v = $r ? json_decode($r, true) : null;
if (!is_array($v) || empty($v['success'])) { fin(false, 'No hemos podido verificar la comprobación de seguridad. Recarga la página e inténtalo de nuevo.', 400); }

$nombre = linea(campo('nombre', 80) ?: campo('NOMBRE', 80));
$email = linea(campo('email', 120) ?: campo('EMAIL', 120));
if ($nombre === '' || !filter_var($email, FILTER_VALIDATE_EMAIL)) { fin(false, 'Revisa el nombre y el correo.', 400); }

// ---- Descarga de guía: se pasa a Brevo, que guarda el contacto y envía el correo ----
if ($json) {
    $d = ['NOMBRE' => $nombre, 'EMAIL' => $email, 'OPT_IN' => '1', 'locale' => 'es', 'html_type' => 'simple', 'email_address_check' => ''];
    $tel = preg_replace('/\D/', '', campo('SMS', 20));
    if (preg_match('/^[6789]\d{8}$/', $tel)) { $d['SMS'] = $tel; $d['SMS__COUNTRY_CODE'] = '+34'; }
    $ctx = stream_context_create(['http' => ['method' => 'POST', 'timeout' => 10, 'ignore_errors' => true,
        'header' => "Content-Type: application/x-www-form-urlencoded\r\n", 'content' => http_build_query($d)]]);
    $r = @file_get_contents(BREVO_GUIA, false, $ctx);
    $estado = 0; foreach (($http_response_header ?? []) as $h) { if (preg_match('#^HTTP/\S+ (\d+)#', $h, $m)) { $estado = (int)$m[1]; } }
    if ($r === false || $estado >= 400) { fin(false, 'No se ha podido enviar. Inténtalo de nuevo en un momento.', 502); }
    fin(true);
}

// ---- Formularios de contacto ----
if (empty($_POST['privacidad'])) { fin(false, 'Tienes que aceptar la política de privacidad.', 400); }
$msg = campo('mensaje', 2000);
if (preg_match_all('#https?://|www\.#i', $msg) > 1) { fin(false, 'Por seguridad, no incluyas más de un enlace en el mensaje.', 400); }
if (preg_match('/[\x{0400}-\x{04FF}\x{4E00}-\x{9FFF}]/u', $msg)) { fin(false, 'Escribe el mensaje en español o inglés.', 400); }
foreach (['viagra', 'casino', 'crypto', 'bitcoin', 'forex', 'seo services', 'backlinks', 'porn', 'betting', 'bit.ly'] as $p) { if (stripos($msg, $p) !== false) { fin(true); } }

$asunto = linea(campo('_subject', 120)) ?: 'Nuevo contacto desde studioemprende.com';
$etiquetas = ['nombre' => 'Nombre', 'email' => 'Email', 'telefono' => 'Teléfono', 'empresa' => 'Empresa', 'etapa' => 'En qué punto está', 'punto' => 'En qué punto está',
    'servicio' => 'Servicio', 'funcion' => 'Función', 'origen' => 'Origen', 'viene_de' => 'Viene de', 'mensaje' => 'Mensaje'];
$cuerpo = '';
foreach ($_POST as $k => $val) {
    if ($k[0] === '_' || in_array($k, ['cf-turnstile-response', 'website', 'privacidad', 'tipo'], true) || is_array($val)) { continue; }
    $val = campo($k, $k === 'mensaje' ? 2000 : 200); if ($val === '') { continue; }
    $cuerpo .= ($etiquetas[$k] ?? ucfirst(preg_replace('/[^a-z0-9_ ]/i', '', $k))) . ': ' . ($k === 'mensaje' ? "\n" . $val : linea($val)) . "\n";
}
$cuerpo .= "\nPágina: " . linea(mb_substr((string)($_SERVER['HTTP_REFERER'] ?? ''), 0, 200)) . "\nFecha: " . date('d/m/Y H:i') . "\n";
$cab = "From: Studio Emprende <" . DESTINO . ">\r\nReply-To: " . $email . "\r\nCc: " . COPIA . "\r\nMIME-Version: 1.0\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Transfer-Encoding: 8bit";
$ok = @mail(DESTINO, '=?UTF-8?B?' . base64_encode($asunto . ': ' . $nombre) . '?=', $cuerpo, $cab, '-f' . DESTINO);

// Copia de seguridad en el servidor, fuera de la carpeta pública si se puede
$dir = dirname(__DIR__) . '/registros-contacto';
if (!is_dir($dir) && !@mkdir($dir, 0750)) { $dir = __DIR__ . '/_registros'; }
if (!is_dir($dir)) { @mkdir($dir, 0750); }
if (strpos($dir, '/_registros') !== false && !file_exists($dir . '/.htaccess')) { @file_put_contents($dir . '/.htaccess', "Require all denied\nDeny from all\n"); }
$guardado = false;
if ($h = @fopen($dir . '/contactos-' . date('Y') . '.csv', 'a')) { flock($h, LOCK_EX); $guardado = fputcsv($h, [date('c'), $asunto, $nombre, $email, campo('telefono', 20), campo('empresa', 120), linea($msg), $ok ? 'enviado' : 'NO ENVIADO']) !== false; flock($h, LOCK_UN); fclose($h); }
if (!$ok && !$guardado) { fin(false, 'No se ha podido enviar el mensaje. Escríbenos a ' . DESTINO . ' o por WhatsApp.', 500); }

if ($ok) {
    @mail($email, '=?UTF-8?B?' . base64_encode('Hemos recibido tu mensaje · Studio Emprende') . '?=',
        "Hola, " . $nombre . ":\n\nHemos recibido tu mensaje en Studio Emprende. Te respondemos en menos de 24 horas laborables.\nSi es urgente, escríbenos por WhatsApp al 601 86 96 68.\n\nStudio Emprende\n" . DOM . "\n",
        "From: Studio Emprende <" . DESTINO . ">\r\nMIME-Version: 1.0\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Transfer-Encoding: 8bit", '-f' . DESTINO);
}
fin(true);
