import json
from controllers.convert_json import (
    ingredients_to_json,
    tags_to_json,
    glassware_to_json,
    recipes_to_json
)
from models.model import (
    RecipeIngredient,
    Recipes,
    RecipesTags,
    RecipeIngredient,
    Glassware,
    Ingredients,
    Tags
)


# Ingredients
def get_ingredients(ids):
    if not isinstance(ids, list):
        list(ids)
    query = Ingredients.query.filter(Ingredients.id.in_(ids)).all()

    result = ingredients_to_json(query)
    return result


def get_ingredients_page(page, per_page):
    query = Ingredients.query.order_by(Ingredients.id).paginate(int(page), int(per_page), error_out=False)

    result = ingredients_to_json(query.items)
    return result


# Tags
def get_tags(ids):
    if not isinstance(ids, list):
        list(ids)
    query = Ingredients.query.filter(Ingredients.id.in_(ids)).all()

    result = ingredients_to_json(query)
    return result


def get_tags_page(page, per_page):
    query = Tags.query.order_by(Tags.id).paginate(int(page), int(per_page), error_out=False)

    result = tags_to_json(query.items)
    return result


# Glassware
def get_glassware(ids):
    if not isinstance(ids, list):
        list(ids)
    query = Glassware.query.filter(Glassware.id.in_(ids)).all()

    result = glassware_to_json(query)
    return result


def get_glassware_page(page, per_page):
    query = Glassware.query.order_by(Glassware.id).paginate(int(page), int(per_page), error_out=False)

    result = glassware_to_json(query.items)
    return result


# Recipes
def get_recipes(recipe_ids):
    if not isinstance(recipe_ids, list):
        list(recipe_ids)
    query = Recipes.query.filter(Recipes.id.in_(recipe_ids)).all()

    return query

