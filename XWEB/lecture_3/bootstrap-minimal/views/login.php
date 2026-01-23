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

<div class="alert alert-success m-2" role="alert" id="login_notification" style="display:none"></div>

<form method="post">
    <div class="container">
        <label for="user"><b>Username</b></label>
        <input type="text" placeholder="Enter Username" name="user" required>
        <label for="psw"><b>Password</b></label>
        <input type="password" placeholder="Enter Password" name="psw" required>
        <button type="submit" id="login_button">Login</button>
    </div>
</form>
