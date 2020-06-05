from flask.app import Flask
import json
import os

def create_app():
  app = Flask(__name__)
  from . import api
  app.register_blueprint(api.bp)
  height = int(os.environ.get('PREDICTOR_HEIGHT', '0'))
  typ = os.environ.get('PREDICTOR_TYPE')
  app.logger.debug(f"Building predictor: {typ}")
  return app