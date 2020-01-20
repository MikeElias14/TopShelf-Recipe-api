import json
from flask import Blueprint, jsonify, request
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


# Get One or More or All ingredients
@ingredients_bp.route('', methods=["GET"])
def get_ingredients():
    ids = request.args.get('ids')
    page = int(request.args.get('page'))
    per_page = int(request.args.get('per_page'))

    if ids is None and page is not None and per_page is not None:
        result = db.get_ingredients_page(page, per_page)
        code = 200  # TODO: Template these as var's in a config/defaults file
    elif ids is not None:
        result = db.get_ingredients(ids)
        code = 200
    else:
        result = 'error'
        code = 400

    return jsonify(result), code
