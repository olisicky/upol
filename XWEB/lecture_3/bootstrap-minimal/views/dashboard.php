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

<header class="navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0 shadow">
  <button class="navbar-toggler d-md-none collapsed m-2 b-0" type="button" data-bs-toggle="collapse"
    data-bs-target="#sidebarMenu" aria-controls="sidebarMenu" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <a class="navbar-brand col-md-3 col-lg-2 me-0 px-3 fs-6" href="#">simple administration</a>
  <div>
    <?php echo "Hello world"; ?>
  </div>
  <div class="navbar-nav">
    <div class="nav-item text-nowrap">
      <!-- <a class="nav-link px-3" href="/login">logout</a> -->
      <form method="POST">
        <button class="btn btn-link" type="submit" name="logout">logout</button>
      </form>
    </div>
  </div>
</header>

<div class="container-fluid">
  <div class="row">
    <nav id="sidebarMenu" class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse">
      <div class="position-sticky pt-3 sidebar-sticky">
        <ul class="nav flex-column">
          <li class="nav-item">
            <a href="/dashboard" class="nav-link active" aria-current="page">
              <span class="icon">
                <i class="bi bi-easel"></i>
              </span>
              Dashboard
            </a>
          </li>
          <li>
            <a href="/items" class="nav-link link-dark">
              <span class="icon">
                <i class="bi bi-card-list"></i>
              </span>
              Items
            </a>
          </li>
          <li>
            <a href="/others" class="nav-link link-dark">
              <span class="icon">
                <i class="bi bi-box"></i>
              </span>
              Others
            </a>
          </li>
          <li>
            <a href="/users" class="nav-link link-dark">
              <span class="icon">
                <i class="bi bi-person-circle"></i>
              </span>
              Users
            </a>
          </li>
        </ul>
      </div>
    </nav>

    <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4 pt-3 pb-3">
      <h1 class="pb-3 border-bottom">Dashboard</h1>
      <div id="react-dashboard"></div>
      <!-- <script>
        const USER_DATA = <?php echo json_encode($json_data); ?>;
      </script> -->
    </main>
  </div>
</div>

<script src="./bootstrap.js"></script>
<!-- Použití reactu bez build kroku -->
<script crossorigin src="https://unpkg.com/react@18/umd/react.development.js"></script>
<script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
<script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
<script src="../components/dashboard.jsx" type="text/babel"></script>