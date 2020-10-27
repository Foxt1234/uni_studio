import os
from flask import Flask,Request
from flask_bootstrap import Bootstrap
from .test import tests
from .fileservice.app import app as fileserviceapp
from .utils.dir_helper import join_upload_dir
def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    app.register_blueprint(tests)
    app.register_blueprint(fileserviceapp)
    app.config['SECRET_KEY'] = 'hard to guess string'
    app.config['UPLOAD_FOLDER'] = join_upload_dir('data/')
    #os.path.join(os.getcwd(),'studio/fileservice/data/')
    app.config['THUMBNAIL_FOLDER'] = join_upload_dir('data/thumbnail/')#'data/thumbnail/'
    app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024
    return app