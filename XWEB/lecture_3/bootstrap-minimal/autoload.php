<?php
// Simple PSR-4 autoloader which maps used class names to file paths (dont have to load them)
spl_autoload_register(function($className) {
    $paths = [
        'controllers/' . $className . '.php',
        'models/' . $className . '.php',
        'views/' . $className . '.php'
    ];
    
    foreach($paths as $path) {
        if (file_exists($path)) {
            require_once $path;
            return;
        }
    }
});
?>