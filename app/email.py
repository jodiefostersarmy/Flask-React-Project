from flask_mail import Message
from flask import render_template
from app import mail, app
from threading import Thread

# there are some issues with the email, and with the python client.

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender, recipients, text_body, html_body)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)
    Thread(target=send_async_email, args=(app, msg)).start()

def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email(
        '[Microblog] Reset Your Password',
        sender=app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('email/reset_password.txt', user=user, token=token),
        html_body=render_template('email/reset_password.html', user=user, token=token)
    )

# this can utilise cc and bcc, just check the docs:
# https://pythonhosted.org/Flask-Mail/

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)
