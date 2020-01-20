from flask import Blueprint
import controllers.controller as db


recipes_bp = Blueprint('recipes', __name__, url_prefix='/recipes')

# # Create One Recipe
# @recipes_bp.route('/create', methods=["POST"])
# def create_recipe():
#
# # Update One Recipe
# @recipes_bp.route('/update', methods=["PUT"])
# def update_recipe():
#
# # Delete One Recipe
# @recipes_bp.route('/delete', methods=["DELETE"])
# def delete_recipe():
#
# # Get One or More Recipes
# @recipes_bp.route('/get', methods=["GET"])
# def get_recipes():
