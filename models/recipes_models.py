from app import app


class Recipes(app.db.Model):
    __tablename__ = 'recipes'
    db = app.db

    created_at = db.Column(db.Datetime)
    updated_at = db.Column(db.Datetime)
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    instructions = db.Column(db.Text, nullable=True)
    glassware = db.Column(db.Integer, db.ForeignKey('glassware.id'), nullable=False)
    image = db.Column(db.String(128))


class Glassware(app.db.Model):
    __tablename__ = 'glassware'
    db = app.db

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.String(128, nullable=False)


class Ingredients(app.db.Model):
    __tablename__ = 'ingredients'
    db = app.db

    created_at = db.Column(db.Datetime)
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)


class RecipeIngredient(app.db.Model):
    __tablename__ = 'recipe_ingredients'
    db = app.db

    created_at = db.Column(db.Datetime)
    updated_at = db.Column(db.Datetime)
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.id'), nullable=False)
