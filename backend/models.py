from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
db = SQLAlchemy()

class Card(db.Model):
    __tablename__ = 'cards'
    imgpath = db.Column(db.String(100), nullable=True)
    id = db.Column(db.String(40), primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    furigana = db.Column(db.String(30), nullable=True)
    birthday = db.Column(db.DateTime, nullable=True)
    favourite = db.Column(db.String(30), nullable=True)
    skills = db.Column(db.String(30), nullable=True)
    card_code = db.Column(db.String(30), nullable=True)

    #gallerys = relationship("Gallery", backref="cards")
class Gallery(db.Model):
    __tablename__ = 'gallerys'
    dummy = db.Column(db.Integer, autoincrement=True,primary_key=True)
    id = db.Column(db.String(40), ForeignKey('cards.id'))
    store_id = db.Column(db.String(40), nullable=True)

    card = relationship("Card",backref=('gallerys'))  

def init_db(app):
    db.init_app(app)
    db.create_all()

def get_all():
    return Card.query.order_by(Card.id).all()

def insert(dictionary):
    card = Card(imgpath=dictionary['imgpath'],
                name=dictionary['name'],
                id=dictionary['id']['uID'],
                furigana=dictionary['furigana'],
                birthday=dictionary['birthday'] ,
                favourite=dictionary['favourite'],
                skills=dictionary['skills'])
    db.session.add(card)
    db.session.commit()

def update(dictionary):
    newcard=Card.query.filter(Card.id==dictionary['id']).first()
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

def makecode(dictionary):
    user_card=Card.query.filter(Card.id==dictionary['id']).first()
    user_card.card_code=dictionary['card_code']
    db.session.commit()

def print_card(id):
    print(id)
    print(Card.query.filter(Card.id == id).scalar())
    content= Card.query.filter(Card.id==id).first()
    user_info = {'name':content.name,'furigana':content.furigana,'birthday':content.birthday,'favourite':content.favourite,'skills':content.skills}
    return user_info

def addGallery(dictionary):
    user_card=Card.query.filter(Card.card_code==dictionary['card_code']).first()
    addID=user_card.id
    print(dictionary['id'])
    addcard=Gallery(id=dictionary['id']['uID'],
                    store_id=addID)
    db.session.add(addcard)
    db.session.commit()
    return user_card.name
