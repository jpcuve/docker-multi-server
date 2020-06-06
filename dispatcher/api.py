from flask import current_app, jsonify
import os
from flask.blueprints import Blueprint
from pip._vendor import requests
import json
from .database import db
from dispatcher.database import get_vectorizer

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/')
def api_index():
  database = os.environ.get('DISPATCHER_DATABASE')
  return jsonify(
    vectorizers=current_app.vectorizers, 
    predictors=current_app.predictors, 
    models=current_app.models, 
    database=database)


@bp.route('/create-database')
def api_create_database():
  current_app.logger.debug(f"Creating database, db: {db}")
  db.create_all(app=current_app)
  for vectorizer in current_app.vectorizers:
    get_vectorizer(vectorizer.get('identifier'))
  return jsonify(status='OK')
