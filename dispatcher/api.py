from flask import Flask, jsonify, current_app
from flask.json import jsonify
import os
import requests

app = Flask(__name__)

@app.route('/')
def index():
  env_vectorizers = os.environ.get('DISPATCHER_VECTORIZERS')
  vectorizers = []
  if env_vectorizers is not None:
    for vectorizer in env_vectorizers.split(','):
      res = requests.get(vectorizer)
      if res.ok:
        vectorizers.append(res.json())
  env_predictors = os.environ.get('DISPATCHER_PREDICTORS')
  predictors = []
  if env_predictors is not None:
    for predictor in env_predictors.split(','):
      res = requests.get(predictor)
      if res.ok:
        predictors.append(res.json())
  return jsonify(vectorizers=vectorizers, predictors=predictors)