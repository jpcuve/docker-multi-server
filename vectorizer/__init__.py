from flask.app import Flask
import json
import os

def create_app():
  app = Flask(__name__)
  from . import api
  app.register_blueprint(api.bp)
  identifier = os.environ.get('VECTORIZER_IDENTIFIER')
  width = int(os.environ.get('VECTORIZER_WIDTH', '0'))
  constructor = os.environ.get('VECTORIZER_CONSTRUCTOR')
  app.logger.debug(f"Building vectorizer: {constructor}")
  return app