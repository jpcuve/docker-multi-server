from flask import current_app, jsonify
import os
from flask.blueprints import Blueprint

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/')
def index():
  return jsonify(
    height=current_app.height, 
    feature_type=current_app.feature_type)
