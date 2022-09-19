from flask import Flask
from flask_cors import CORS


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)

    CORS(app=app)
    return app
