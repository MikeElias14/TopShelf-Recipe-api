import json
from flask import Blueprint, jsonify
import controllers.controller as db

ingredients_bp = Blueprint('ingredients', __name__, url_prefix='/ingredients')

#
# # Create One ingredient
# @ingredients_bp.route('', methods=["POST"])
# def create_ingredient():
#
#
# # Update One ingredient
# @ingredients_bp.route('', methods=["PUT"])
# def update_ingredient():
#
#
# # Delete One ingredient
# @ingredients_bp.route('', methods=["DELETE"])
# def delete_ingredient():


# Get One or More ingredients
@ingredients_bp.route('', methods=["GET"])
def get_ingredients():
    ingredients = db.get_ingredients([1, 2, 3, 4])

    return jsonify(ingredients), 200
