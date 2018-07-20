from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ.get('EMAIL_USER'),
    "MAIL_PASSWORD": os.environ.get('EMAIL_PASSWORD')
}

app.config.update(mail_settings)
mail = Mail(app)


# Mail Info
def sendMailCustomer(mail_recipients, email_body):
    with mail.app.app_context():
        msg = Message(subject="Hello",
                      sender="contactlighteyesusa@gmail.com",
                      recipients=[mail_recipients],
                      body=email_body)
        mail.send(msg)


def sendMailCompany(subject, mail_recipients, email_body):
    with mail.app.app_context():
        msg = Message(subject=subject,
                      sender="contactlighteyesusa@gmail.com",
                      recipients=["lighteyesusa@gmail.com",
                                  "contactlighteyesusa@gmail.com"],
                      body=email_body)
        mail.send(msg)
