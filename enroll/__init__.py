from flask import Flask,Request
from enroll.test import tests
def create_app():
    app = Flask(__name__)

    app.register_blueprint(tests)
    return app