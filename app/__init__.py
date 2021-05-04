from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from .auth.v1 import version1 as v1 

from config import app_config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    app.url_map.strict_slashes = False

    app.config.from_pyfile('config.py')
    app.register_blueprint(v1)

    # blueprint
    from .auth.v1 import version1 as version1_blueprint
    app.register_blueprint(version1_blueprint, url_prefix='api/v1')

    db.init_app(app)

    return app