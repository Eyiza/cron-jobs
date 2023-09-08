import os
from flask_mail import Mail, Message

mail = Mail()

def init_app(app):
    mail.init_app(app)


def send_email(to, subject, template, sender):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=sender
    )
    mail.send(msg)