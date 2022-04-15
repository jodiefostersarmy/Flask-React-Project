import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # Secret keys are useful to generate signatures or tokens
    # Flask-WTF use it to protect web forms against a nasty attack called Cross-Site Request Forgery (CSRF)
    # during development, the hardcoded string can be used
    # during production, we will rely solely on the secret key and not provide a hardcoded string

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False