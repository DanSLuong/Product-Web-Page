from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ['EMAIL_USER'],
    "MAIL_PASSWORD": os.environ['EMAIL_PASSWORD']
}

app.config.update(mail_settings)
mail = Mail(app)


"""
if __name__ == '__main__':
    with app.app_context():
        # For email subscribe request
        msg = Message(subject="Hello",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=["<recipient email here>"],
                      body="Thank you for subscribing to our newsletter!")
        mail.send(msg)
        msg2 = Message(subject="New Subscriber",
                       sender=app.config.get("MAIL_USERNAME"),
                       recipients=[app.config.get("MAIL_USERNAME")],
                       body="Subscriber Email Request.")
        mail.send(msg2)

        # For contact request
        msg3 = Message(subject="Hello",
                       sender=app.config.get("MAIL_USERNAME"),
                       recipients=["<recipient email here>"],
                       body="Thank you reaching out to us! Our team will try to respond to you as soon as possible")
        mail.send(msg3)
        msg4 = Message(subject="Customer Inquery",
                       sender=app.config.get("MAIL_USERNAME"),
                       recipients=[app.config.get("MAIL_USERNAME")],
                       body="Customer Inquery text body!!!")
        mail.send(msg4)
"""