from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api

db = SQLAlchemy()
api = Api()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    app.url_map.strict_slashes = False

    api.init_app(app)

    # blueprint
    from .auth.v1 import version1 as version1_blueprint
    app.register_blueprint(version1_blueprint, url_prefix='/api/v1')

    db.init_app(app)

    return app