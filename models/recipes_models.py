from app import app


class Recipes(app.db.Model):
    __tablename__ = 'recipes'
    db = app.db

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    created_at = db.Column(db.Datetime, nullable=False)
    updated_at = db.Column(db.Datetime)
    name = db.Column(db.String(128), nullable=False)
    is_default = db.Column(db.Boolean, nullables=False)
    desc = db.Column(db.Text)
    instructions = db.Column(db.Text)
    image = db.Column(db.String(128))
    glassware_id = db.Column(db.BigInteger, db.ForeignKey('glassware.id'), nullable=False)
    created_by_user_id = db.Column(db.BigInteger)


class Glassware(app.db.Model):
    __tablename__ = 'glassware'
    db = app.db

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    image = db.Column(db.String(128))


class Ingredients(app.db.Model):
    __tablename__ = 'ingredients'
    db = app.db

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    image = db.Column(db.String(128))


class RecipeIngredient(app.db.Model):
    __tablename__ = 'recipe_ingredients'
    db = app.db

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    recipes_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    ingredients_id = db.Column(db.Integer, db.ForeignKey('ingredients.id'), nullable=False)


class Tags(app.db.Model):
    __tablename__ = 'tags'
    db = app.db

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    tag = db.Column(db.String(128), nullable=False)


class RecipesTags(app.db.Model):
    __tablename__ = 'recipe_tags'
    db = app.db

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    recipes_id = db.Column(db.BigInteger, db.ForeignKey('recipes.id'), nullable=False)
    tags_id = db.Column(db.BigInteger, db.ForeignKey('tags.id'), nullable=False)
