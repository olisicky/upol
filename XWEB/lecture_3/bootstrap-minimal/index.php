<?php
if (session_status() === PHP_SESSION_NONE) {
  session_start();
}
require_once 'autoload.php';

$router = new Router();
$url_info = $router->getController($_SERVER['REQUEST_URI']);
$controller = new $url_info['controller']($url_info['page']);    // () volá index??

if ($_SERVER['REQUEST_METHOD'] === 'POST'){
  $controller->handlePost();
}

// Jenom pro AJAX GET requesty, jinak by se nic nevykreslilo
if ($_SERVER['REQUEST_METHOD'] === 'GET' &&
    !empty($_SERVER['HTTP_X_REQUESTED_WITH']) &&
    strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) == 'xmlhttprequest'){
  $controller->handleGet();
}

if ($url_info['method'] != null && method_exists($controller, $url_info['method'])) {
  $controller->{$url_info['method']}($url_info['page'], $url_info['data']);
  // tohle je pro ajax requesty - nechceme pak volat getView
  if (!empty($_SERVER['HTTP_X_REQUESTED_WITH']) && 
      strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) == 'xmlhttprequest') {
    exit();
  }
}
?>
<!DOCTYPE html>
<html lang="cs">

<head>
  <title>KMI/WEBA Webové aplikace</title>
  <meta content="Ondřej Lisický" name="author" />
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="./bootstrap.css">
  <link rel="stylesheet" href="./bootstrap-icons.css">
</head>

<body>
  <main>
    <?php
    // když se nastaví přes url nějaká specifická metoda, tak ji předáme controlleru
    if ($url_info['method'] == null || !method_exists($controller, $url_info['method'])) {
      $controller->getView($url_info['page']);
    }
    ?>
  </main>
  <script src="js/edit.js" defer></script>
  <script src="js/validation.js" defer></script>
</body>