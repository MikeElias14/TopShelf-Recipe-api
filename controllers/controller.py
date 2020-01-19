import json
from models.model import (
    RecipeIngredient,
    Recipes,
    RecipesTags,
    RecipeIngredient,
    Glassware,
    Ingredients,
    Tags
)


# Template this?
def ingredients_to_json(ingredients):
    result = []

    for ingredient in ingredients:
        info = dict(
            id=ingredient.id,
            image=ingredient.image,
            name=ingredient.name
        )
        result.append(info)
    return result


def get_ingredients(ingredient_ids):
    if not isinstance(ingredient_ids, list):
        list(ingredient_ids)
    query = Ingredients.query.filter(Ingredients.id.in_(ingredient_ids)).all()

    result = ingredients_to_json(query)
    return result


def get_ingredients_page(page, per_page):
    query = Ingredients.query.order_by(Ingredients.id).paginate(int(page), int(per_page), error_out=False)

    result = ingredients_to_json(query.items)
    return result


def get_tags(tag_ids):
    if not isinstance(tag_ids, list):
        list(tag_ids)
    query = Tags.query.filter(Tags.id.in_(tag_ids)).all()

    return query


def get_glassware(glassware_ids):
    if not isinstance(glassware_ids, list):
        list(glassware_ids)
    query = Glassware.query.filter(Glassware.id.in_(glassware_ids)).all()

    return query


def get_recipes(recipe_ids):
    if not isinstance(recipe_ids, list):
        list(recipe_ids)
    query = Recipes.query.filter(Recipes.id.in_(recipe_ids)).all()

    return query

