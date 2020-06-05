from flask import Flask, current_app, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
  identifier = os.environ.get('VECTORIZER_IDENTIFIER')
  width = int(os.environ.get('VECTORIZER_WIDTH', '0'))
  constructor = os.environ.get('VECTORIZER_CONSTRUCTOR')
  return jsonify(identifier=identifier, width=width, constructor=constructor)
