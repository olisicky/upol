<?php

class LoggedUserModel {
    private $db;
    
    public function __construct() {
        $this->db = new PDO('mysql:host=192.168.1.2;dbname=moje_db', 'test', 'heslo');
    }

    public function getUsers($limit = 10) {
        // získá 10 uživatelů z tabulky userLog
        $limit = (int) $limit; // zabezpečení proti SQL injection
        $query = $this->db->prepare("SELECT * FROM userLog ORDER BY timestamp DESC LIMIT $limit");
        $query->execute();
        return $query->fetchAll(PDO::FETCH_ASSOC);
    }

    public function logUser(string $name, string $lastname, string $email) {
        // zapsání uživatele do databáze pro logování
        $query = $this->db->prepare("INSERT INTO userLog (name, lastname, timestamp, email) VALUES (:param1, :param2, :param3, :param4)");
        $result = $query->execute(['param1' => $name, 'param2' => $lastname, 'param3' => date('Y-m-d H:i:s'), 'param4' => $email]);
    }

    public function getUserInfo(string $user) {
        // získá informace o uživateli, které jsou pak vypsány
        $query = $this->db->prepare("SELECT * FROM users WHERE email = ?");
        $query->execute([$user]);
        $userInfo = $query->fetch(PDO::FETCH_ASSOC);
        return [
            'name' => $userInfo['name'] ?? null,
            'lastname' => $userInfo['lastname'] ?? null,
            'email' => $userInfo['email'] ?? null,
        ];
    }
}