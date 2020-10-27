from flask import Flask,Request
from .test import tests
def create_app():
    app = Flask(__name__)

    app.register_blueprint(tests)
    return app