from flask.app import Flask
import json
import os

def create_app():
  app = Flask(__name__)
  from . import api
  app.register_blueprint(api.bp)
  app.identifier = os.environ.get('VECTORIZER_IDENTIFIER')
  app.width = int(os.environ.get('VECTORIZER_WIDTH', '0'))
  app.constructor = os.environ.get('VECTORIZER_CONSTRUCTOR')
  app.logger.debug(f"Building vectorizer: {app.constructor}")
  return app