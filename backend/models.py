from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Card(db.Model):
    __tablename__ = 'cards'
    imgpath = db.Column(db.String(100), nullable=True)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    furigana = db.Column(db.String(30), nullable=False)
    birthday = db.Column(db.DateTime, nullable=False)
    favourite = db.Column(db.String(30), nullable=False)
    skills = db.Column(db.String(30), nullable=False)

def init_db(app):
    db.init_app(app)
    db.create_all()

def get_all():
    return Card.query.order_by(Card.id).all()

def insert(dictionary):
    card = Card(imgpath=dictionary['imgpath'],
                name=dictionary['name'],
                id=1,
                furigana=dictionary['furigana'],
                birthday=dictionary['birthday'] ,
                favourite=dictionary['favourite'],
                skills=dictionary['skills'])
    db.session.add(card)
    db.session.commit()

def update(dictionary):
    newcard=Card.query.get(1)
    newcard.imgpath=dictionary['imgpath']
    newcard.name=dictionary['name']
    newcard.furigana=dictionary['furigana']
    newcard.birthday=dictionary['birthday']
    newcard.favourite=dictionary['favourite']
    newcard.skills=dictionary['skills']
    # newcard.update({
    # 'imgpath':dictionary['imgpath'],
    # 'name':dictionary['name'],
    # 'furigana':dictionary['furigana'],
    # 'birthday':dictionary['birthday'] ,
    # 'favourite':dictionary['favourite'],
    # 'skills':dictionary['skills']
    # })
    db.session.commit()

def print_card():
    contents = Card.query.all()
    for content in contents:
        print('%d, %s %s %s' % (content.id, content.imgpath, content.name, content.furigana))
        user_info = {'name':content.name,'furigana':content.furigana,'birthday':content.birthday,'favourite':content.favourite,'skills':content.skills}
    return user_info