<?php

require_once __DIR__ . '/../config/config.php';
require_once __DIR__ . '/../src/Mailer.php';
require_once __DIR__ . '/../src/functions.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $from = sanitizeInput($_POST['from']);
    $to = sanitizeInput($_POST['to']);
    $subject = sanitizeInput($_POST['subject']);
    $message = sanitizeInput($_POST['message']);

    if (!validateEmail($from) || !validateEmail($to)) {
        echo "Invalid email format.";
        exit;
    }

    if (!validateFields($from, $to, $subject, $message)) {
        echo "All fields are required.";
        exit;
    }

    $config = include __DIR__ . '/../config/config.php';
    $mailer = new Mailer($config);

    if ($mailer->sendEmail($from, $to, $subject, $message)) {
        echo "Email sent successfully!";
    } else {
        echo "Failed to send the email.";
    }
}
?>
