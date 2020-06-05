from flask import Flask, jsonify, current_app
from flask.json import jsonify
import os
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
  vectorizers = [requests.get(vectorizer).json() for vectorizer in json.loads(os.environ.get('DISPATCHER_VECTORIZERS'))]
  predictors = [requests.get(predictor).json() for predictor in json.loads(os.environ.get('DISPATCHER_PREDICTORS'))]
  models = json.loads(os.environ.get('DISPATCHER_MODELS'))
  return jsonify(vectorizers=vectorizers, predictors=predictors, models=models)