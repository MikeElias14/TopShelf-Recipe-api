import json
from flask import Blueprint, jsonify, request
import controllers.controller as db

tags_bp = Blueprint('tags', __name__, url_prefix='/tags')

#
# # Create One tag
# @tags_bp.route('', methods=["POST"])
# def create_tag():
#
#
# # Update One tag
# @tags_bp.route('', methods=["PUT"])
# def update_tag():
#
#
# # Delete One tag
# @tags_bp.route('', methods=["DELETE"])
# def delete_tag():


# Get One or More or All tags
@tags_bp.route('', methods=["GET"])
def get_tags():
    ids = request.args.get('ids')
    page = int(request.args.get('page'))
    per_page = int(request.args.get('per_page'))

    if ids is None and page is not None and per_page is not None:
        result = db.get_tags_page(page, per_page)
        code = 200  # TODO: Template these as var's in a config/defaults file
    elif ids is not None:
        result = db.get_tags(ids)
        code = 200
    else:
        result = 'error'
        code = 400

    return jsonify(result), code
