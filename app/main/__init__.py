import logging

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from .config import config_by_name
from flask.app import Flask

db = SQLAlchemy()
flask_bcrypt = Bcrypt()

logging.basicConfig(
    # filename='app.log',
    level=logging.DEBUG,
    format='[%(asctime)s]-[%(filename)s:%(lineno)d]-[%(levelname)s]-%(message)s',
    datefmt="%Y-%m-%d %H:%M:%S %z"
)


def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)

    @app.errorhandler(Exception)
    def handle_exception(e):
        logging.error(f"Exception Handler::{e}", exc_info=True)
        return jsonify(message="Something went wrong"), 500

    return app
