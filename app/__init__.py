from flask import Flask
from flask_wtf.csrf import CSRFProtect
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from waitress import serve


DEFAULT_BALANCE = Config.DEFAULT_BALANCE

FLASK_RUN_PORT=8000
FLASK_RUN_HOST="127.0.0.1"


csrf = CSRFProtect()

db = SQLAlchemy()
migrate = Migrate()


def create_app():
        
    app = Flask(__name__)
    app.config.from_object(Config)

    # initializers
    csrf.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from app.experimentRoute import experiment
    from app.models import models
    app.register_blueprint(experiment)    
    return app


