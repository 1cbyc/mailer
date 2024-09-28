import os
from flask import Flask, render_template, request, flash, redirect, url_for
import smtplib
from email.message import EmailMessage
from email_validator import validate_email, EmailNotValidError
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = 'my_secret_key'

app.config['UPLOAD_FOLDER'] = './attachments/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def send_mail():
    if request.method == 'POST':
        try:
            sender = request.form['from']
            recipient = request.form['to']
            subject = request.form['subject']
            message_content = request.form['message']
            cc = request.form.get('cc', '')
            bcc = request.form.get('bcc', '')

            validate_email(sender)
            validate_email(recipient)

            # Constructing the email
            msg = EmailMessage()
            msg.set_content(message_content)
            msg.add_alternative(message_content, subtype='html')  # HTML message
            msg['Subject'] = subject
            msg['From'] = sender
            msg['To'] = recipient

            # Add CC, BCC if provided
            if cc:
                msg['Cc'] = cc
            if bcc:
                msg['Bcc'] = bcc

            # Handling attachments
            attachment = request.files.get('attachment')
            if attachment and allowed_file(attachment.filename):
                filename = secure_filename(attachment.filename)
                attachment.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'rb') as f:
                    file_data = f.read()
                    file_type = attachment.content_type
                    msg.add_attachment(file_data, maintype='application', subtype=file_type, filename=filename)

            # Sending the email
            with smtplib.SMTP(os.getenv('SMTP_SERVER'), int(os.getenv('SMTP_PORT'))) as server:
                server.starttls()
                server.login(os.getenv('SMTP_USERNAME'), os.getenv('SMTP_PASSWORD'))
                server.send_message(msg)

            flash('Email sent successfully!', 'success')
        except EmailNotValidError as e:
            flash(f"Invalid email address: {str(e)}", 'error')
        except Exception as e:
            flash(f"Failed to send email: {str(e)}", 'error')

        return redirect(url_for('send_mail'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
