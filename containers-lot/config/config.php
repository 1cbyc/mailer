<?php

require_once __DIR__ . '/../vendor/autoload.php';

use Dotenv\Dotenv;

$dotenv = Dotenv::createImmutable(__DIR__ . '/../');
$dotenv->load();

return [
    'smtp' => [
        'host' => $_ENV['SMTP_HOST'],
        'username' => $_ENV['SMTP_USER'],
        'password' => $_ENV['SMTP_PASSWORD'],
        'port' => $_ENV['SMTP_PORT'],
    ]
];
