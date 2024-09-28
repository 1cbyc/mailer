<?php

function sanitizeInput($data)
{
    return htmlspecialchars(stripslashes(trim($data)));
}

function validateEmail($email)
{
    return filter_var($email, FILTER_VALIDATE_EMAIL);
}

function validateFields($from, $to, $subject, $message)
{
    return !empty($from) && !empty($to) && !empty($subject) && !empty($message);
}
