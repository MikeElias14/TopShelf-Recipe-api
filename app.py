import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

# Define db then connect later
db = SQLAlchemy()


def create_app(test_config=None):
    # create and configure the app
    _app = Flask(__name__, instance_relative_config=True)
    _app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI=config.SQLALCHEMY_RECIPE_DATABASE_URI
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

    # Connect to DB
    db.init_app(_app)

    # Create Routes
    # Recipes
    from api.v1.recipes_api import recipes_bp
    _app.register_blueprint(recipes_bp)

    # Ingredients
    from api.v1.ingredients_api import ingredients_bp
    _app.register_blueprint(ingredients_bp)

    # Tags
    from api.v1.tags_api import tags_bp
    _app.register_blueprint(tags_bp)

    # Glassware
    from api.v1.glassware_api import glassware_bp
    _app.register_blueprint(glassware_bp)

    return _app


app = create_app()
app.run(debug=True)
