<?php

class Router {

    public function getController(string $url) {
        // oddělení URL na části pro získání controlleru, metody a dat (parametry v ?)
        $parsed = parse_url($url);
        $path = $parsed['path'] ?? '/';

        $request_uri = explode('/', trim($path, '/'));
        $page = $request_uri[0] ?: 'login';
        $method = $request_uri[1] ?? null;
        $data = $request_uri[2] ?? null;
        $controller = ucfirst($page) . "Controller";

        return [
            'page' => $page,
            'controller' => $controller,
            'method' => $method,
            'data' => $data
        ];
    }
}

?>