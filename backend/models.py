from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Card(db.Model):
    __tablename__ = 'cards'
    imgpath = db.Column(db.String(100), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    furigana = db.Column(db.String(30), nullable=False)
    birthday = db.Column(db.DateTime, nullable=False)
    favourite = db.Column(db.String(30), nullable=False)
    skills = db.Column(db.String(30), nullable=False)

class SpamModel(db.Model):
    __tablename__ = 'spam_table'

    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    note = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

def init_db(app):
    db.init_app(app)
    db.create_all()

def get_all():
    return SpamModel.query.order_by(SpamModel.pk).all()

def insert(name, note):
    model = SpamModel(name=name, note=note)
    db.session.add(model)
    db.session.commit()