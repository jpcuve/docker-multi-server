from flask import current_app, jsonify
import os
from flask.blueprints import Blueprint
from pip._vendor import requests
import json

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/')
def index():
  vectorizers = [requests.get(vectorizer).json() for vectorizer in json.loads(os.environ.get('DISPATCHER_VECTORIZERS'))]
  predictors = [requests.get(predictor).json() for predictor in json.loads(os.environ.get('DISPATCHER_PREDICTORS'))]
  models = json.loads(os.environ.get('DISPATCHER_MODELS'))
  return jsonify(vectorizers=vectorizers, predictors=predictors, models=models)