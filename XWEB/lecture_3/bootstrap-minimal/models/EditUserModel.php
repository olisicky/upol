<?php

class EditUserModel {
    private $db;
    private $user;
    
    public function __construct(string $userName){
        // prepare database and user (email) from login
        $this->user = $userName;
        $this->db = new PDO('mysql:host=192.168.1.2;dbname=moje_db', 'test', 'heslo');
    }

    public function getUser() {
        // verify the current user wheather he is an admin
        $query = $this->db->prepare("SELECT * FROM users WHERE email = ?");
        $query->execute([$this->user]);
        return $query->fetch(PDO::FETCH_ASSOC);
    }

    public function getUsers() {
        // based on the admin flag, call users for edit
        $userInfo = $this->getUser($this->user);
        $_SESSION['is_admin'] = $userInfo['admin'];
        
        if ($userInfo['admin']) {
            $query = $this->db->prepare("SELECT * FROM users");
            $query->execute();
            return $query->fetchAll(PDO::FETCH_ASSOC);
        }
        else {
            return [$userInfo];
        }

    }

    public function deleteUser(string $user) {
        $query = $this->db->prepare("DELETE FROM `users` WHERE email = ?");
        $query->execute([$user]);
    }

    public function deleteLogEntry(string $id) {
        $query = $this->db->prepare("DELETE FROM `userLog` WHERE id = ?");
        $query->execute([$id]);
    }

    public function addUser($data) {
        $query = $this->db->prepare("
            INSERT INTO users (name, lastname, email, phone, room, description, password, admin)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ");
        $query->execute([
            $data['name'],
            $data['lastname'], 
            $data['email'],
            $data['phone'],
            $data['room'] ?? '',
            $data['description'] ?? '',
            $data['pswd'],
            $data['admin'] ?? 0
        ]); 
    }

    public function update($data) {
        $query = $this->db->prepare("
            UPDATE users
            SET name = ?,
                lastname = ?,
                email = ?,
                phone = ?,
                room = ?,
                description = ?,
                password = ?,
                admin = ?
            WHERE email = ?
        ");
        $query->execute([
            $data['name'],
            $data['lastname'], 
            $data['email'],
            $data['phone'],
            $data['room'] ?? '',
            $data['description'] ?? '',
            $data['pswd'],
            $data['admin'] ?? 0,
            $data['original_email']
        ]); 
    }
}