from mail import mail
from flask import Flask
from flask_mail import Mail, Message
import os


def sendMail():
    with mail.app.app_context():
        msg = Message(subject="Hello",
                      sender=mail.app.config.get("MAIL_USERNAME"),
                      recipients=["hayate58@gmail.com"],
                      body="Thank you for subscribing to our newsletter!")
        mail.send(msg)


sendMail()