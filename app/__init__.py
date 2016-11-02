import os
from ConfigParser import ConfigParser
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask.ext.mail import Mail

basedir = os.path.abspath(os.path.dirname(__file__))
bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()
login_manager.session_protection = 'basic'
login_manager.login_view = 'main.login'
filename = 'E:/up.ini'
cf = ConfigParser()
cf.read(filename)


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SECRET_KEY'] = 'xxx'
    app.config['MAIL_SERVER'] = 'smtp.163.com'
    app.config['MAIL_USERNAME'] = cf.get('up', 'username')
    app.config['MAIL_PASSWORD'] = cf.get('up', 'passwd')
    app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[FLASKY]'
    app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin<flasky@163.com>'
    app.config.from_object()
    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app



