<?php

class UserModel {
    private $db;
    
    public function __construct() {
        $this->db = new PDO('mysql:host=192.168.1.2;dbname=moje_db', 'test', 'heslo');
    }

    public function verifyUser(string $userName, string $password) {
        // verifikace hesla proti databázi. Kontrola jenom na stejnost stringu, nemám
        // to teď v databázi hashováno
        $query = $this->db->prepare("SELECT * FROM users WHERE email = ?");
        $query->execute([$userName]);
        $user = $query->fetch(PDO::FETCH_ASSOC);
        return [
            'db_pass' => $user['password'] ?? null,
            'given_pass' => $password,
            'isValid' => $user !== false && ($password == $user['password']),
            'isAdmin' => $user['admin'] ?? false
        ];
    }
}