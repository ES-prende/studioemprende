<?php
// Consulta protegida del registro de consentimientos (solo con contraseña)
const CLAVE_HASH = '$2y$10$iblijLwakRu...5NHd54euODcdUUw2yt2ygwqgdrnHeUHElc6guwm';
header('X-Robots-Tag: noindex, nofollow');
session_start();
if (isset($_POST['clave'])) { if (password_verify($_POST['clave'], CLAVE_HASH)) { $_SESSION['ok'] = 1; } else { sleep(2); $error = 1; } }
if (isset($_GET['salir'])) { session_destroy(); header('Location: registro-consentimientos.php'); exit; }
$dirs = [dirname(__DIR__) . '/registros-consentimiento', __DIR__ . '/_registros'];
$files = [];
foreach ($dirs as $d) { foreach (glob($d . '/consentimientos-*.csv') ?: [] as $f) { $files[basename($f)] = $f; } }
krsort($files);
if (!empty($_SESSION['ok']) && isset($_GET['descargar']) && isset($files[$_GET['descargar']])) {
  header('Content-Type: text/csv; charset=utf-8'); header('Content-Disposition: attachment; filename="' . basename($_GET['descargar']) . '"'); readfile($files[$_GET['descargar']]); exit;
}
?><!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>Registro de consentimientos</title>
<style>body{font-family:system-ui,sans-serif;background:#F7F2EC;color:#2a2224;margin:0;padding:24px}main{max-width:1100px;margin:0 auto;background:#fff;border-radius:14px;padding:24px}h1{color:#7A2638;font-size:24px}table{border-collapse:collapse;width:100%;font-size:13px}th,td{border-bottom:1px solid #eee;padding:6px 8px;text-align:left;vertical-align:top}th{background:#faf6f1}input,button{font:inherit;padding:8px 12px}button,.b{background:#7A2638;color:#fff;border:0;border-radius:8px;text-decoration:none;padding:8px 14px}.s{color:#7A2638}.wrap{overflow-x:auto}</style></head><body><main>
<h1>Registro de consentimientos de cookies</h1>
<?php if (empty($_SESSION['ok'])): ?>
<form method="post"><p>Introduce la contraseña para consultar el registro.</p><?php if (!empty($error)) echo '<p class="s">Contraseña incorrecta.</p>'; ?><input type="password" name="clave" autofocus required> <button>Entrar</button></form>
<?php else:
  $rows = []; $tot = ['aceptar' => 0, 'rechazar' => 0, 'guardar' => 0];
  foreach ($files as $f) { if (($h = fopen($f, 'r'))) { $head = fgetcsv($h); while (($r = fgetcsv($h)) !== false) { $rows[] = $r; if (isset($tot[$r[2]])) $tot[$r[2]]++; } fclose($h); } }
  usort($rows, function ($a, $b) { return strcmp($b[0], $a[0]); });
?>
<p>Total: <b><?= count($rows) ?></b> · Aceptar todas: <?= $tot['aceptar'] ?> · Rechazar: <?= $tot['rechazar'] ?> · Selección personalizada: <?= $tot['guardar'] ?></p>
<p><?php foreach ($files as $n => $f): ?><a class="b" href="?descargar=<?= urlencode($n) ?>">Descargar <?= htmlspecialchars($n) ?></a> <?php endforeach; ?> <a href="?salir=1" class="s">Salir</a></p>
<div class="wrap"><table><tr><th>Fecha</th><th>Visitante</th><th>Acción</th><th>Analítica</th><th>Publicidad</th><th>Versión</th><th>Página</th><th>IP (anonimizada)</th></tr>
<?php foreach (array_slice($rows, 0, 500) as $r): ?><tr><?php foreach (array_slice($r, 0, 8) as $c): ?><td><?= htmlspecialchars($c) ?></td><?php endforeach; ?></tr><?php endforeach; ?>
</table></div><p style="font-size:13px;color:#777">Se muestran los 500 últimos. Descarga el CSV para ver todos.</p>
<?php endif; ?></main></body></html>
