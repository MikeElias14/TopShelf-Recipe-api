from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import SQLALCHEMY_RECIPE_DATABASE_URI
from models.model import Glassware, Ingredients, Tags

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_RECIPE_DATABASE_URI

db = SQLAlchemy(app)

# Default glasses
default_glassware = [
    Glassware(id=1, name='Shot'),
    Glassware(id=2, name='Highball'),
    Glassware(id=3, name='Martini'),
    Glassware(id=4, name='Old Fashioned'),
    Glassware(id=5, name='Cosmopolitan'),
    Glassware(id=6, name='Hurricane'),
    Glassware(id=7, name='Margarita'),
    Glassware(id=8, name='Rocks'),
    Glassware(id=9, name='Red Wine'),
    Glassware(id=10, name='White Wine'),
    Glassware(id=11, name='Zombie'),
    Glassware(id=12, name='Sherry'),
    Glassware(id=13, name='Pitcher'),
    Glassware(id=14, name='Irish Coffee'),
    Glassware(id=15, name='Beer Stein'),
    Glassware(id=16, name='Pilsner'),
    Glassware(id=17, name='Flute'),
    Glassware(id=18, name='Boot'),
    Glassware(id=19, name='Goblet'),
    Glassware(id=20, name='Beer Mug'),
    Glassware(id=21, name='Cordial'),
    Glassware(id=22, name='Lowball')
]

# Default ingredients
default_ingredients = [
    Ingredients(id=1, name='Rum'),
    Ingredients(id=2, name='Gin'),
    Ingredients(id=3, name='Silver Tequila'),
    Ingredients(id=4, name='Gold Tequila'),
    Ingredients(id=5, name='Rye Whiskey')
]

# Default ingredients
default_tags = [
    Tags(id=1, tag='Sweet'),
    Tags(id=2, tag='Dry'),
    Tags(id=3, tag='Warm'),
    Tags(id=4, tag='Cold'),
    Tags(id=5, tag='Smokey'),
    Tags(id=6, tag='Bitter'),
    Tags(id=7, tag='Sour')
]

for glassware in default_glassware:
    new_glassware = db.session.query(Glassware).get(glassware.id)
    if new_glassware is None:
        db.session.add(glassware)
    elif new_glassware.name != glassware.name:
        new_glassware.name = glassware.name
    elif new_glassware.image != glassware.image:
        new_glassware.image = glassware.image

for ingredient in default_ingredients:
    new_ingredient = db.session.query(Ingredients).get(ingredient.id)
    if new_ingredient is None:
        db.session.add(ingredient)
    elif new_ingredient.name != ingredient.name:
        new_ingredient.name = ingredient.name

for tag in default_tags:
    new_tag = db.session.query(Tags).get(tag.id)
    if new_tag is None:
        db.session.add(tag)
    elif new_tag.tag != tag.tag:
        new_tag.tag = tag.tag

db.session.commit()
