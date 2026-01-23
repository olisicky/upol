<?php
require_once "BaseController.php";
require_once __DIR__ . "/../models/LoggedUserModel.php";
class LoginController extends BaseController {

    public function __construct(string $page) {
        parent::__construct($page);

        if ($this->isLoggedIn()) {
            if ($page == 'login') {
                header("Location: /dashboard");
                exit();
            }
        } else {
            if ($page != 'login') {
                header("Location: /login");
                exit();
            }
        }
    }

    public function isLoggedIn() {
        return isset($_SESSION["user"]) && isset($_SESSION["password"]);
    }

    public function handlePost() {
        parent::handlePost();
        // podívám se na hodnoty v superglobální $_POST
        if ($_POST && array_key_exists('logout', $_POST)) {
            $this->logout();
        }

        if ($_POST && array_key_exists('user', $_POST) && array_key_exists('psw', $_POST)) {
            require_once __DIR__ . "/../models/UserModel.php";
            $userModel = new UserModel();
            $verification = $userModel->verifyUser($_POST['user'], $_POST['psw']);
            if ($verification['isValid']) {
                $this->handleLogin($verification['isAdmin']);
            }
            else {
                echo "<p style='color:red;'>Neplatné uživatelské jméno nebo heslo.</p>";
            }
        }
    }

    private function handleLogin($admin) {
        // získám uživatelské jméno a heslo z formuláře a uložím je do session
        $user = isset($_POST['user']) ? $_POST['user'] : '';
        $password = isset($_POST['psw']) ? $_POST['psw'] : '';
        
        $_SESSION["user"] = $user;
        $_SESSION["password"] = $password;
        $_SESSION["isAdmin"] = $admin;

        require_once __DIR__ . "/../models/LoggedUserModel.php";
        $logged = new LoggedUserModel();
        $info = $logged->getUserInfo($_SESSION['user']);
        $logged->logUser($info["name"], $info['lastname'], $info['email']);
        
        header("Location: /dashboard");
        exit();
        return true;
    }
}
?>