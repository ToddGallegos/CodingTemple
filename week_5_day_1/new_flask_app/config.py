import os

basedir = os.path.abspath(os.path.dirname(__name__))

class Config():
    FLASK_APP = os.environ.get('FLASK_APP')
    print(os.environ.get('FLASK_ENV'))
    FLASK_ENV = os.environ.get('FLASK_ENV')
    print(os.environ.get('SECRET_KEY'))
    SECRET_KEY = os.environ.get('SECRET_KEY')
    print(os.environ.get('DATABASE_URL'))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False