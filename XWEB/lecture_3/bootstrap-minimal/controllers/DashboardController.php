<?php
require_once "BaseController.php";
require_once __DIR__ . '/../models/LoggedUserModel.php';

class DashboardController extends BaseController {

    public $logins;

    public function __construct(string $page) {
        // přidání volání parent konstruktoru a nastavení loggins pro view
        parent::__construct($page);
        $logged = new LoggedUserModel();

        $this->logins = $logged->getUsers();
        $json_dat = json_encode($this->logins, JSON_HEX_TAG | JSON_HEX_APOS | JSON_HEX_AMP | JSON_HEX_QUOT);
    }

    function handleGet() {
        // use data grom GET request
        $logged = new LoggedUserModel();
        $this->logins = $logged->getUsers($_GET['limit'] ?? 10);
        $json_data = json_encode($this->logins, JSON_HEX_TAG | JSON_HEX_APOS | JSON_HEX_AMP | JSON_HEX_QUOT);
        error_log($json_data);
        // poslání dat pro react
        header('Content-Type: application/json');
        echo $json_data;
        exit();
    }

    
}
