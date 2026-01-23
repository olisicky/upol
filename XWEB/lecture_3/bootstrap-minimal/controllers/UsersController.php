<?php
require_once "BaseController.php";
require_once __DIR__ . "/../models/EditUserModel.php";

class UsersController extends BaseController {
    private $currentUserName;
    private $usersInfo;
    private $usersModel;

    public function __construct(string $page) {
        parent::__construct($page);
        $this->currentUserName = $_SESSION["user"] ?? 'Není přihlášen';
        $this->usersModel = new EditUserModel($this->currentUserName);
        $this->usersInfo = $this->usersModel->getUsers();

    }

    public function edit(string $page, string $data) {
        // indicate edit for a view of user which should create a form
        $_SESSION['edit_mode'] = true;
        $_SESSION['user_to_edit'] = $data;
        header('Location: /users');
        exit();

    }

    public function delete(string $page, string $data) {
        echo "Deleting user";
        $this->usersModel->deleteUser($data);
        if (!empty($_SERVER['HTTP_X_REQUESTED_WITH']) && 
            strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) == 'xmlhttprequest') {
            header('Content-Type: application/json');
            // tohle jsou reálně data, která posílám a mohu s nimi dál pracovat v JS
            echo json_encode(['success' => true, 'message' => "User $data deleted"]);
            exit();
        }

        header('Location: /users');
        exit();
    }

    public function deleteLog(string $page, string $data) {
        // Delete entry from log based in the ID passed in $data
        echo "Deleting log entry";
        $this->usersModel->deleteLogEntry($data);
        if (!empty($_SERVER['HTTP_X_REQUESTED_WITH']) && 
            strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) == 'xmlhttprequest') {
            header('Content-Type: application/json');
            // tohle jsou reálně data, která posílám a mohu s nimi dál pracovat v JS
            echo json_encode(['success' => true, 'message' => "Log entry $data deleted"]);
            exit();
        }

        header('Location: /users');
        exit();
    }

    public function add(string $page, string $data) {
        $_SESSION['add_user'] = true;
        header('Location: /users');
        exit();
    }

    public function getView(string $page) {
        // úprava getView, abych měl k dispozici i proměnné
        $currentUserName = $this->currentUserName;
        $usersInfo = $this->usersInfo;
        $edit = null;
        $userToEdit =null;
        $isAdmin = $_SESSION['is_admin'] ?? false;

        
        if (isset($_SESSION['edit_mode'])){
            $edit = $_SESSION['edit_mode'];
            $user = new EditUserModel($_SESSION['user_to_edit']);
            $userToEdit = $user->getUser();

        }
        elseif (isset($_SESSION['add_user'])) {
            echo "ano";
            $edit = $_SESSION['add_user'];
            $userToEdit = [
                'name' => '',
                'lastname' => '',
                'email' => '',
                'phone' => '',
                'room' => '',
                'description' => '',
                'password' => '',
                'admin' => 0
            ];
        }

        include "views/" . $page . ".php";
    }

    public function handlePost() {
        // úprava handle post, abych získal i informace z tlačítka pro úpravu (save_update)
        parent::handlePost();
        if ($_POST && array_key_exists('logout', $_POST)) {
            $this->logout();
        }

        if (isset($_POST['save_update']) && isset($_SESSION['edit_mode'])) {
            if (!isset($_SESSION['is_admin'])) {
                $_POST['admin'] = 0;
            }
            $_POST['original_email'] = $_SESSION['user_to_edit'];    // in case email is changed
            $this->usersModel->update($_POST);
            unset($_SESSION['edit_mode']);
            unset($_SESSION['user_to_edit']);
        }

        elseif (isset($_POST['save_update']) && isset($_SESSION['add_user'])) {
            $this->usersModel->addUser($_POST);
            unset($_SESSION['add_user']);
        }

    }
}