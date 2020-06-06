from flask.app import Flask
import json
import os

def create_app():
  app = Flask(__name__)
  from . import api
  app.register_blueprint(api.bp)
  app.height = int(os.environ.get('PREDICTOR_HEIGHT', '0'))
  app.feature_type = os.environ.get('PREDICTOR_FEATURE_TYPE')
  app.logger.debug(f"Building predictor: {app.feature_type}")
  return app