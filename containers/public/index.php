<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mailer</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <div class="container">
        <h2>Send Email</h2>
        <form action="send_email.php" method="POST">
            <label for="from">From:</label>
            <input type="email" id="from" name="from" required>
            
            <label for="to">To:</label>
            <input type="email" id="to" name="to" required>
            
            <label for="subject">Subject:</label>
            <input type="text" id="subject" name="subject" required>
            
            <label for="message">Message:</label>
            <textarea id="message" name="message" rows="6" required></textarea>
            
            <button type="submit">Send Email</button>
        </form>
    </div>
    <script src="assets/js/main.js"></script>
</body>
</html>
