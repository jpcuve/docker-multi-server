from flask import Flask
from flask.json import jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
  height = int(os.environ.get('PREDICTOR_HEIGHT', '0'))
  typ = os.environ.get('PREDICTOR_TYPE')
  return jsonify(height=height, type=typ)
