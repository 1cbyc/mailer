<?php
$to = "recipient@example.com"; // Replace with the recipient email address
$subject = "Test Email"; // Replace with the email subject
$message = "This is a test email sent from PHP."; // Replace with the email message
$headers = "From: sender@example.com"; // Replace with the sender email address

// Send the email
if(mail($to, $subject, $message, $headers)){
    echo "Email sent successfully.";
} else{
    echo "Email sending failed.";
}
?>
