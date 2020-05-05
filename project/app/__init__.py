from flask import Flask
from flask_sqlalchemy import SQLAlchemy # ORM and related utils
import flask_login # help with login a user

db = SQLAlchemy()
login_manager = flask_login.LoginManager()

def create_app(test_config=None):
    from app import blueprints, commands
    app = Flask(__name__,
                instance_relative_config=True,
                static_folder='static',
                static_url_path='/assets/')
    app.config.from_pyfile('config.py')
    if test_config:
        app.config.update(test_config)
    db.init_app(app)
    login_manager.init_app(app)
    blueprints.init_app(app)
    commands.init_app(app)
    app.add_url_rule('/',endpoint='index') # appoint the entry
    return app
