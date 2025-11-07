<!DOCTYPE html>
<html lang="cs">

<head>
  <title>Dashboard</title>
  <meta content="Ondřej Lisický" name="author" />
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="./bootstrap.css">
  <link rel="stylesheet" href="./bootstrap-icons.css">
</head>

<style>
/* some hacks for responsive sidebar */
.sidebar {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 100;
  padding: 48px 0 0; /* height of navbar */
}

.sidebar-sticky {
  height: calc(100vh - 48px);
  overflow-x: hidden;
  overflow-y: auto;
}
</style>

<body>

    <form method="post">
        <div class="container">
            <label for="user"><b>Username</b></label>
            <input type="text" placeholder="Enter Username" name="user" required>
            <label for="psw"><b>Password</b></label>
            <input type="password" placeholder="Enter Password" name="psw" required>
            <button type="submit">Login</button>
        </div>
    </form>
</body>