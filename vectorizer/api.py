from flask import current_app, jsonify
import os
from flask.blueprints import Blueprint

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/')
def index():
  return jsonify(
    identifier=current_app.identifier, 
    width=current_app.width, 
    constructor=current_app.constructor)
