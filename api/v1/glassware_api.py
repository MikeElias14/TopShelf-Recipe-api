import json
from flask import Blueprint, jsonify, request
import controllers.controller as db

glassware_bp = Blueprint('glassware', __name__, url_prefix='/glassware')

#
# # Create One glass
# @glassware_bp.route('', methods=["POST"])
# def create_glass():
#
#
# # Update One glass
# @glassware_bp.route('', methods=["PUT"])
# def update_glass():
#
#
# # Delete One glass
# @glassware_bp.route('', methods=["DELETE"])
# def delete_glass():


# Get One or More or All glassware
@glassware_bp.route('', methods=["GET"])
def get_glassware():
    ids = request.args.get('ids')
    page = int(request.args.get('page'))
    per_page = int(request.args.get('per_page'))

    if ids is None and page is not None and per_page is not None:
        result = db.get_glassware_page(page, per_page)
        code = 200  # TODO: Template these as var's in a config/defaults file
    elif ids is not None:
        result = db.get_glassware(ids)
        code = 200
    else:
        result = 'error'
        code = 400

    return jsonify(result), code
