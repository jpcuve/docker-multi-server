import datetime
import logging
from collections import Counter
from typing import Dict, List, Tuple
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

logger = logging.getLogger(__file__)


class Image(db.Model):
    __tablename__ = 'images'
    __table_args__ = {'sqlite_autoincrement': True}
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column('created', db.DateTime, nullable=False,
                        default=datetime.datetime.utcnow())
    identifier = db.Column(db.String(64), nullable=False,
                           unique=True, index=True)
    width = db.Column(db.Integer, nullable=False, default=0)
    height = db.Column(db.Integer, nullable=False, default=0)
    crc32 = db.Column(db.BigInteger, nullable=False, default=0)
    nice_classes = db.Column(db.BigInteger, nullable=False, default=0)


class Vectorizer(db.Model):
    __tablename__ = 'vectorizers'
    __table_args__ = {'sqlite_autoincrement': True}
    id = db.Column(db.Integer, primary_key=True)
    identifier = db.Column(db.String(256), nullable=False,
                           unique=True, index=True)


class Vector(db.Model):
    __tablename__ = 'vectors'
    __table_args__ = (
        db.UniqueConstraint('image_id', 'vectorizer_id'),
        {
            'sqlite_autoincrement': True,
        }
    )
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.LargeBinary(), nullable=False)
    image_id = db.Column(db.Integer, db.ForeignKey('images.id'))
    image = db.relationship(
        'Image', backref=db.backref('vectors', lazy='dynamic'))
    vectorizer_id = db.Column(db.Integer, db.ForeignKey('vectorizers.id'))
    vectorizer = db.relationship(
        'Vectorizer', backref=db.backref('vectors', lazy='dynamic'))


def get_vectorizer(vectorizer_identifier: str) -> Vectorizer:
    try:
        return next(vt for vt in db.session.query(Vectorizer).filter(Vectorizer.identifier == vectorizer_identifier))
    except StopIteration:
        vt = Vectorizer(identifier=vectorizer_identifier)
        db.session.add(vt)
        db.session.commit()
        return vt
