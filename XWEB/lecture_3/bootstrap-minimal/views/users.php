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
  <div class="navbar-nav">
    <div class="nav-item text-nowrap">
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
            <a href="/dashboard" class="nav-link link-dark" aria-current="page">
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
            <a href="/users" class="nav-link active">
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
      <h2>Users page</h2>
      <div class="alert alert-success m-2" role="alert" id="save_notification" style="display:none"></div>

      <p>Přihlášeným uživatelem je, <?php echo $currentUserName; ?></p>

      <table>
        <thread>
          <tr>
            <th>Jméno a Příjmení</th>
            <th style="width: 150px;">Akce</th>
          </tr>
        </thread>
        <tbody>
            <?php foreach ($usersInfo as $user): ?>
            <tr>
                <td>
                    <?php echo $user['name'] . ' ' . $user['lastname']; ?>
                </td>
                <td>
                  <a href="/users/edit/<?php echo $user['email'];?>">
                      <button type="button" class="edit_button" data-email="<?php echo $user['email']; ?>">Edit</button>
                  </a>
                  <?php if ($isAdmin): ?>
                    <!-- <a href="/users/delete/<?php echo $user['email'];?>"> -->
                      <!-- přesměrování tady pomocí JS ! -->
                        <button type="button" class="delete_button" data-email="<?php echo $user['email']; ?>">Delete</button>
                    <!-- </a> -->
                  <?php endif; ?>
                </td>
            </tr>
            <?php endforeach; ?>
            
            <?php if (empty($usersInfo)): ?>
            <tr>
                <td colspan="2">Nebyly nalezeny žádné záznamy uživatelů.</td>
            </tr>
            <?php endif; ?>
        </tbody>
      </table>

      <a href="/users/add/empty">
        <button type="button">Add</button>
      </a>
      <?php if ($edit !== null): ?>

          <hr>
          
          <h2>Upravit uživatele:</h2>
          
          <form method="POST" id="edit_form"> 
              <input type="hidden" name="email" value="<?php echo $userToEdit['email']; ?>">
              
              <label for="name">Jméno:</label>
              <input type="text" name="name" 
                    value="<?php echo $userToEdit['name']; ?>" required><br>
              <label for="last_name">Příjmení:</label>
              <input type="text" name="lastname" 
                    value="<?php echo $userToEdit['lastname']; ?>" required><br>
              <label for="email">Email:</label>
              <input type="text" name="email" 
                    value="<?php echo $userToEdit['email']; ?>" required><br>
              <label for="pswd">Password:</label>
              <input type="text" name="pswd" 
                    value="<?php echo $userToEdit['password']; ?>" required><br>
              <label for="phone">Phone:</label>
              <input type="text" name="phone" 
                    value="<?php echo $userToEdit['phone']; ?>" required><br>
              <label for="room">Room:</label>
              <input type="text" name="room" 
                  value="<?php echo $userToEdit['room']; ?>" required><br>
              <label for="description">Description:</label>
              <input type="text" name="description" 
                  value="<?php echo $userToEdit['description']; ?>" required><br>
              <?php if ($isAdmin): ?>
                <label for="admin">Admin:</label>
                <input type="text" name="admin" 
                    value="<?php echo $userToEdit['admin']; ?>" required><br>      
                <?php endif; ?>

              <button type="submit" name="save_update" id="edit_yes">Uložit změny</button>
          </form>
          
      <?php endif; ?>
    
    <dialog id="confirm_edit">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Opravdu si přejete upravit uživatele <?php echo $userToEdit['email']; ?>?</h5>
            <button onclick="close_dialog('confirm_edit')" type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <p>Potvrzením dojde k nevratné úpravě údajů. </p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-primary" id="confirm_edit_btn">Uložit změny</button>
            <button type="button" class="btn btn-secondary" id="edit_no" data-dismiss="modal">Zavřít</button>
          </div>
        </div>
      </div>
    </dialog>

    <dialog id="ask_delete">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Opravdu si přejete odstranit uživatele?</h5>
            <button onclick="close_dialog('ask_delete')" type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <p>Potvrzením dojde k odstranění uživatele.</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-primary" id="confirm_delete_btn">Uložit změny</button>
            <button type="button" class="btn btn-secondary" id="delete_no" data-dismiss="modal">Zavřít</button>
          </div>
        </div>
      </div>
    </dialog>

    </main>
  </div>
</div>

<script src="./bootstrap.js"></script>
