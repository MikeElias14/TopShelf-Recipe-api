from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import SQLALCHEMY_RECIPE_DATABASE_URI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_RECIPE_DATABASE_URI

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class Recipes(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime)
    name = db.Column(db.String(128), nullable=False)
    is_default = db.Column(db.Boolean, nullable=False)
    desc = db.Column(db.Text)
    instructions = db.Column(db.Text)
    image = db.Column(db.String(128))
    glassware_id = db.Column(db.BigInteger, db.ForeignKey('glassware.id'), nullable=False)
    created_by_user_id = db.Column(db.BigInteger)


class Glassware(db.Model):
    __tablename__ = 'glassware'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    image = db.Column(db.String(128))


class Ingredients(db.Model):
    __tablename__ = 'ingredients'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    image = db.Column(db.String(128))


class RecipeIngredient(db.Model):
    __tablename__ = 'recipe_ingredients'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    recipes_id = db.Column(db.BigInteger, db.ForeignKey('recipes.id'), nullable=False)
    ingredients_id = db.Column(db.BigInteger, db.ForeignKey('ingredients.id'), nullable=False)


class Tags(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    tag = db.Column(db.String(128), nullable=False)


class RecipesTags(db.Model):
    __tablename__ = 'recipe_tags'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    recipes_id = db.Column(db.BigInteger, db.ForeignKey('recipes.id'), nullable=False)
    tags_id = db.Column(db.BigInteger, db.ForeignKey('tags.id'), nullable=False)


if __name__ == '__main__':
    manager.run()
