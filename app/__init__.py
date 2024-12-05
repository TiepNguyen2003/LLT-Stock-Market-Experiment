from flask import Flask
from flask_wtf.csrf import CSRFProtect
from settings.config import Config
from settings.questionContent import QuestionContent
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from waitress import serve
DEFAULT_BALANCE = Config.DEFAULT_BALANCE


app = Flask(__name__)


app.config.from_object(Config)


csrf = CSRFProtect()
csrf.init_app(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
