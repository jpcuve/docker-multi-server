from flask import current_app, jsonify
import os
from flask.blueprints import Blueprint

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/')
def index():
  height = int(os.environ.get('PREDICTOR_HEIGHT', '0'))
  typ = os.environ.get('PREDICTOR_TYPE')
  return jsonify(height=height, type=typ)
