import os

DB_USER = os.environ("DB_USER")
DB_PASSWORD = os.environ("DB_PASSWORD")

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_USER_DATABASE_URI = f"mysql://{DB_USER}:{DB_PASSWORD}@localhost/recipe_db"
