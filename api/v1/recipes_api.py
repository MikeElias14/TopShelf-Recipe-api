from flask import Blueprint
from controllers.recipes_controller import


recipes_bp = Blueprint('recipes', __name__, url_prefix='/user')

# Create One Recipe
@recipes_bp.route('/create', methods=["POST"])
def create_recipe():
    
# Update One Recipe
@recipes_bp.route('/update', methods=["PUT"])
def update_recipe():
    
# Delete One Recipe
@recipes_bp.route('/delete', methods=["DELETE"])
def delete_recipe():
    
# Get One or More Recipes
@recipes_bp.route('/get', methods=["GET"])
def get_recipe():
