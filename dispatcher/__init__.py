from flask.app import Flask
import json
import os
from pip._vendor import requests

def create_app():
  app = Flask(__name__)
  app.config.from_object(os.environ.get('DISPATCHER_CONFIG_CLASS'))
  from . import api
  app.register_blueprint(api.bp)
  from .database import db
  db.init_app(app)
  app.vectorizers = [requests.get(vectorizer).json() for vectorizer in json.loads(os.environ.get('DISPATCHER_VECTORIZERS'))]
  app.predictors = [requests.get(predictor).json() for predictor in json.loads(os.environ.get('DISPATCHER_PREDICTORS'))]
  app.models = json.loads(os.environ.get('DISPATCHER_MODELS'))
  app.logger.debug(f"Building dispatcher: {app.models}")
  return app