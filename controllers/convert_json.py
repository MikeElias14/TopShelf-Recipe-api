
# TODO: Tempalte the xxxx_to_json's in terms of the model, not like this


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


def tags_to_json(tags):
    result = []

    for tag in tags:
        info = dict(
            id=tag.id,
            tag=tag.name
        )
        result.append(info)
    return result


def glassware_to_json(glassware):
    result = []

    for glass in glassware:
        info = dict(
            id=glass.id,
            image=glass.image,
            name=glass.name
        )
        result.append(info)
    return result


def recipes_to_json(recipes):
    result = []

    for recipe in recipes:
        info = dict(
            id=recipe.id,
            image=recipe.image,
            name=recipe.name
        )
        result.append(info)
    return result
