<?php

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

class Mailer
{
    private $mailer;
    
    public function __construct($config)
    {
        $this->mailer = new PHPMailer(true);
        $this->configureMailer($config['smtp']);
    }

    private function configureMailer($smtpConfig)
    {
        $this->mailer->isSMTP();
        $this->mailer->Host = $smtpConfig['host'];
        $this->mailer->SMTPAuth = true;
        $this->mailer->Username = $smtpConfig['username'];
        $this->mailer->Password = $smtpConfig['password'];
        $this->mailer->SMTPSecure = 'tls';
        $this->mailer->Port = $smtpConfig['port'];
    }

    public function sendEmail($from, $to, $subject, $message)
    {
        try {
            $this->mailer->setFrom($from);
            $this->mailer->addAddress($to);
            $this->mailer->isHTML(false);
            $this->mailer->Subject = $subject;
            $this->mailer->Body = $message;

            $this->mailer->send();
            $this->logEmail($from, $to, $subject, "Success");

            return true;
        } catch (Exception $e) {
            $this->logEmail($from, $to, $subject, $e->getMessage());
            return false;
        }
    }

    private function logEmail($from, $to, $subject, $status)
    {
        $logMessage = date('Y-m-d H:i:s') . " | From: $from | To: $to | Subject: $subject | Status: $status\n";
        file_put_contents(__DIR__ . '/../logs/mail.log', $logMessage, FILE_APPEND);
    }
}
