from flask.app import Flask
import json
import os
from pip._vendor import requests

def create_app():
  app = Flask(__name__)
  from . import api
  app.register_blueprint(api.bp)
  vectorizers = [requests.get(vectorizer).json() for vectorizer in json.loads(os.environ.get('DISPATCHER_VECTORIZERS'))]
  predictors = [requests.get(predictor).json() for predictor in json.loads(os.environ.get('DISPATCHER_PREDICTORS'))]
  models = json.loads(os.environ.get('DISPATCHER_MODELS'))
  app.logger.debug(f"Building dispatcher: {models}")
  return app