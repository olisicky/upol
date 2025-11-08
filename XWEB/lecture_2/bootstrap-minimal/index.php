<?php
if (session_status() === PHP_SESSION_NONE) {
  session_start();
}
// Získání hodnoty parametru 'page' z URL, výchozí hodnota je 'dashboard'. Pro případ, kdy používám page proměnnou v url!
# $page = $_GET['page'] ?? 'dashboard';

# tohle je pro případ, kdy mám pěknější url, ale musím parsovat REQUEST_URI
$request_uri = explode('/', trim($_SERVER['REQUEST_URI'], '/'));
$page = $request_uri[0] ?: 'login';    # pokud prázdné, tak login
$path = "pages/" . $page . ".php";

if ($_POST && array_key_exists('logout', $_POST)) {
    session_unset();
    session_destroy();
    header("Location: /login");
    exit();
}


if ($_POST && array_key_exists('user', $_POST)) {
  $user = isset($_POST['user']) ? $_POST['user'] : '';
  $password = isset($_POST['psw']) ? $_POST['psw'] : '';
  $_SESSION["user"]=$user;
  $_SESSION["password"]=$password;
  header("Location: /dashboard");
  exit();
}


if ($page != 'login' && (!isset($_SESSION["user"]) || !isset($_SESSION["password"]))){
    header("Location: /login");
    exit();
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
      if (file_exists($path)) {
        include($path);
      } else {
        echo "<h2>404 Page not found</h2>";
      }
    ?>
  </main>
</body>