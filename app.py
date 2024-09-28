from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def send_mail():
    if request.method == 'POST':
        sender = request.form['from']
        recipient = request.form['to']
        subject = request.form['subject']
        message_content = request.form['message']

        msg = EmailMessage()
        msg.set_content(message_content)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipient

        try:
            with smtplib.SMTP('smtp.provider.com', 587) as server:
                server.starttls()
                server.login('my@mail.com', 'my')
                server.send_message(msg)
            return 'Email sent successfully!'
        except Exception as e:
            return f"Failed to send email: {str(e)}"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
