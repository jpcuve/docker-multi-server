from flask import current_app, jsonify
import os
from flask.blueprints import Blueprint

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/')
def index():
  identifier = os.environ.get('VECTORIZER_IDENTIFIER')
  width = int(os.environ.get('VECTORIZER_WIDTH', '0'))
  constructor = os.environ.get('VECTORIZER_CONSTRUCTOR')
  return jsonify(identifier=identifier, width=width, constructor=constructor)
