import os
from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.message import EmailMessage
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './attachments/uploaded_files'
app.secret_key = 'your_secret_key'  # Required for flashing messages

# Define allowed file extensions for attachments
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'docx'}

# Helper function to check for allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def send_mail():
    if request.method == 'POST':
        # Fetch email data from form
        sender = request.form['from']
        recipient = request.form['to']
        subject = request.form['subject']
        message_content = request.form['message']
        cc = request.form.get('cc', '')
        bcc = request.form.get('bcc', '')
        reply_to = request.form.get('reply_to', '')
        headers = {}

        # Handling attachment (optional)
        attachment = request.files['attachment']
        filename = None
        if attachment and allowed_file(attachment.filename):
            filename = secure_filename(attachment.filename)
            attachment.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Constructing the email
        msg = EmailMessage()
        msg.set_content(message_content)
        msg.add_alternative(message_content, subtype='html')
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipient

        if cc:
            msg['Cc'] = cc
        if bcc:
            headers['Bcc'] = bcc
        if reply_to:
            msg['Reply-To'] = reply_to

        if filename:
            with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'rb') as f:
                file_data = f.read()
                file_type = attachment.content_type
                msg.add_attachment(file_data, maintype='application', subtype=file_type, filename=filename)

        try:
            with smtplib.SMTP('smtp.myprovider.com', 587) as server:
                server.starttls()
                server.login('my@email.com', 'my_password')
                server.send_message(msg)
            flash('Email sent successfully!', 'success')
            return redirect(url_for('send_mail'))
        except Exception as e:
            flash(f"Failed to send email: {str(e)}", 'error')
            return redirect(url_for('send_mail'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
