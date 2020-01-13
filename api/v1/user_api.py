import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
# from werkzeug.security import check_password_hash, generate_password_hash
# from flaskr.db import get_db

user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/hello', methods=["GET"])
def get_hello():
    return 'Hello, World!'
