<?php
// Registro de consentimientos de cookies de studioemprende.com
// Guarda cada elección en un CSV fuera de la carpeta pública (si el servidor lo permite).
header('Content-Type: application/json; charset=utf-8');
header('X-Robots-Tag: noindex');
if ($_SERVER['REQUEST_METHOD'] !== 'POST') { http_response_code(405); echo '{"ok":false}'; exit; }
$raw = file_get_contents('php://input', false, null, 0, 4000);
$d = json_decode($raw, true);
if (!is_array($d)) { http_response_code(400); echo '{"ok":false}'; exit; }
$id = preg_replace('/[^a-z0-9]/i', '', substr((string)($d['id'] ?? ''), 0, 40));
$acc = in_array($d['accion'] ?? '', ['aceptar', 'rechazar', 'guardar'], true) ? $d['accion'] : '';
if ($id === '' || $acc === '') { http_response_code(400); echo '{"ok":false}'; exit; }
$ana = !empty($d['analitica']) ? 'si' : 'no';
$pub = !empty($d['publicidad']) ? 'si' : 'no';
$ver = preg_replace('/[^0-9a-z.\-]/i', '', substr((string)($d['version'] ?? ''), 0, 20));
$url = substr(filter_var((string)($d['url'] ?? ''), FILTER_SANITIZE_URL), 0, 200);
if (strpos($url, 'https://studioemprende.com') !== 0) { $url = ''; }
$ip = $_SERVER['REMOTE_ADDR'] ?? '';
if (filter_var($ip, FILTER_VALIDATE_IP, FILTER_FLAG_IPV4)) { $p = explode('.', $ip); $p[3] = '0'; $ip = implode('.', $p); }
elseif (filter_var($ip, FILTER_VALIDATE_IP, FILTER_FLAG_IPV6)) { $ip = implode(':', array_slice(explode(':', $ip), 0, 3)) . '::'; }
else { $ip = ''; }
$ua = substr(preg_replace('/[\r\n",;]/', ' ', $_SERVER['HTTP_USER_AGENT'] ?? ''), 0, 160);
date_default_timezone_set('Europe/Madrid');
$fila = [date('c'), $id, $acc, $ana, $pub, $ver, $url, $ip, $ua];
$dir = dirname(__DIR__) . '/registros-consentimiento';
if (!is_dir($dir) && !@mkdir($dir, 0750) ) { $dir = __DIR__ . '/_registros'; }
if (!is_dir($dir)) { @mkdir($dir, 0750); }
if (strpos($dir, '/_registros') !== false && !file_exists($dir . '/.htaccess')) { @file_put_contents($dir . '/.htaccess', "Require all denied\nDeny from all\n"); }
$f = $dir . '/consentimientos-' . date('Y') . '.csv';
$nuevo = !file_exists($f);
$h = @fopen($f, 'a');
if (!$h) { http_response_code(500); echo '{"ok":false}'; exit; }
flock($h, LOCK_EX);
if ($nuevo) { fputcsv($h, ['fecha', 'id_visitante', 'accion', 'analitica', 'publicidad', 'version_aviso', 'pagina', 'ip_anonimizada', 'navegador']); }
fputcsv($h, $fila);
flock($h, LOCK_UN); fclose($h);
echo '{"ok":true}';
