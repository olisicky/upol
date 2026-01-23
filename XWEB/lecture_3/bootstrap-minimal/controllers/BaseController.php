<?php
class BaseController {
    public function __construct(string $page) {
        if (session_status() === PHP_SESSION_NONE) {
            session_start();
        }
        $this->handleJsonInput();
    }

    private function handleJsonInput() {
        // Převedení JSON vstupu na pole $_POST, abych nemusel měnit stávající logiku zpracování POST
        $contentType = $_SERVER['CONTENT_TYPE'] ?? '';
        
        if (strpos($contentType, 'application/json') !== false) {
            $input = file_get_contents('php://input');
            $jsonData = json_decode($input, true);
            
            if ($jsonData && is_array($jsonData)) {
                // Převést JSON data do $_POST
                $_POST = array_merge($_POST, $jsonData);
            }
        }
    }

    public function handlePost() {
        // Základní post, který mi bude handlovat logout ve všech controllerech.
        // Jakmile mám pak specifický post, tak je potřeba přepsat a brát v potaz i ten logout
        if ($_POST && array_key_exists('logout', $_POST)) {
            $this->logout();
        }
    }
    public function getView(string $page) {
        // základní getView, který mi bude ve všech controllerech includovat příslušný view
        include "views/" . $page . ".php";
    }
    public function logout() {
        // jednoduchá funkce pro odhlášení uživatele
        session_unset();
        session_destroy();
        header("Location: /login");
        exit();
    }

    public function handleGet() {
        echo "Base GET method called";
    }
}
?>