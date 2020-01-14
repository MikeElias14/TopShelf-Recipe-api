import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config


def create_app(test_config=None):
    # create and configure the app
    _app = Flask(__name__, instance_relative_config=True)
    _app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI=config.SQLALCHEMY_USER_DATABASE_URI
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        _app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        _app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(_app.instance_path)
    except OSError:
        pass

    # DB init
    _app.db = SQLAlchemy(_app)
    _app.migrate = Migrate(_app, _app.db)

    # Create User Routes
    from api.v1.user_api import user_bp
    _app.register_blueprint(user_bp)

    return _app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
