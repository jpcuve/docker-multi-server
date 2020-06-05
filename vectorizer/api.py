from flask import Flask, current_app, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
  name = os.environ.get('VECTORIZER_NAME', 'gorilla')
  return jsonify(status=f'OK from vectorizer: {name}')
