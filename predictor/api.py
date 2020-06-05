from flask import Flask
from flask.json import jsonify

app = Flask(__name__)

@app.route('/')
def index():
  return jsonify(status='OK from predictor')