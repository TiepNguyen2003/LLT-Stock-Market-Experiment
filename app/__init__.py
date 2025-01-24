from flask import Flask
from flask_wtf.csrf import CSRFProtect
from config import Config

from app.questionContent import QuestionContent
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from waitress import serve


DEFAULT_BALANCE = Config.DEFAULT_BALANCE


csrf = CSRFProtect()

db = SQLAlchemy()
migrate = Migrate(db)


def create_app():
        
    app = Flask(__name__)
    app.config.from_object(Config)

    # initializers
    csrf.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from app.experiment import experiment
    from app import models
    app.register_blueprint(experiment)    
    return app



