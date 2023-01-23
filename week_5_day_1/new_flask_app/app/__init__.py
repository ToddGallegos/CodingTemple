from flask import Flask
from config import Config
from .models import db, User, Pokemon
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

# app.config.update(
#     FLASK_APP = 'run.py',
#     FLASK_ENV = 'development',
#     SECRET_KEY = '8675309',
#     SQLALCHEMY_DATABASE_URI = 'postgresql://vrsxstzu:PbuyR4zLQGjEGpb2lU0XKRfNqBgzyFKs@kashin.db.elephantsql.com/vrsxstzu',
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
# )

db.init_app(app)
migrate = Migrate(app, db)

from . import routes
from . import models