from flask import Flask
# from flask_mail import Mail
# from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from .config import config

# mail = Mail()
# moment = Moment()
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    # mail.init_app(app)
    # moment.init_app(app)
    db.init_app(app)
    # attach routes and custom error pages here

    # Define os modelos de contas do banco de dados
    from .models import contas

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

