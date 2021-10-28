from flask import Blueprint,request, jsonify
from flask_restful import Api, Resource
from models import get_all,insert,update,print_card,makecode,addGallery
from models import Card,Gallery
from werkzeug.utils import secure_filename # ファイル名をチェックする関数
from tempfile import mkstemp
from flask import send_from_directory # 画像のダウンロード
import os
from datetime import datetime



api_bp = Blueprint('api', __name__, url_prefix='/api')


@api_bp.route('/spam', methods=['GET'])
def getUserList():

    res = "aaa"

    return jsonify(res), 200
@api_bp.route('/spam', methods=['POST'])
def createCard():

    req = request.json



    return jsonify(req), 200


@api_bp.route('/design', methods=['POST'])
def create():
    json=request.json
    name = json[0]['name']
    furigana = json[0]['furigana']
    birthday = json[0]['birthday']
    birthday = datetime.strptime(birthday, '%Y-%m-%d')
    favourite = json[0]['favourite']
    skills = json[0]['skills']
    uID =json[0]['uID']
    print(uID)
    dictionary={'imgpath': "aaa",'name':name,'furigana':furigana,'id':uID,
                'birthday':birthday,'favourite':favourite,'skills':skills}
    if Card.query.filter(Card.id == dictionary['id']).scalar() != None:
        update(dictionary)
        print("update!")
    else :
        insert(dictionary)
        print("insert!")
    card = Card.query.filter(Card.id==dictionary['id']).first()
    response_json={'name':card.name,'furigana':card.furigana,'birthday':card.birthday,'favourite':card.favourite,'skills':card.skills}
    return jsonify(response_json)

@api_bp.route('/user_info', methods=['POST'])
def get_info():
    json=request.json
    card= Card.query.filter(Card.id==json[0]['uID']).first()
    response_json={'name':card.name,
        'furigana':card.furigana,
        'birthday':card.birthday,
        'favourite':card.favourite,
        'skills':card.skills,
        'card_code':card.card_code
        }
    return jsonify(response_json)

@api_bp.route('/card_code', methods=['POST'])
def register_code():
    uID=request.json[0]['uID']
    code=request.json[0]['card_code']
    dictionary={'id':uID,'card_code':code}
    print(dictionary['card_code'])
    user_card=Card.query.filter(Card.card_code==code).all()
    print(len(user_card))
    if(len(user_card)>=1):
        flag=1
    else:
        flag=0
        makecode(dictionary)
    response_json={'card_code':code , 'flag':flag}
    return jsonify(response_json)

@api_bp.route('/add_gallery', methods=['POST'])
def add_gallery():
    print("addgallery")
    json=request.json
    print(json)
    card_code = json[0]['card_code']
    uID =json[0]['uID']
   
    dictionary={'card_code': card_code,'id':uID}
    print(dictionary)
    print(dictionary['id'])
    addname=addGallery(dictionary)
    
    response_json={'addname':addname}
    return jsonify(response_json)

@api_bp.route('/show_gallery', methods=['POST'])
def show_gallery():
    store_ids=[]
    respon=[]
    json=request.json
    uID =json[0]['uID']
    print("show_gallery")
    print(uID)
    card= Card.query.filter(Card.id==uID).first()
    print(card)
    for gallery in card.gallerys:
        print(gallery.store_id)
        store_ids.append(gallery.store_id)
    for i in store_ids:
        card= Card.query.filter(Card.id==i).first()
        data={
            'id':i,
            'name':card.name,
            'imgpath':card.imgpath
        }
        respon.append(data)
    return jsonify(respon)

@api_bp.route('/show_card', methods=['POST'])
def show_card():
    json=request.json
    print(json)
    uID =json[0]['uID']
    print("show_card")
    print(uID)
    card= Card.query.filter(Card.id==uID).first()
    respon={'name':card.name,
        'furigana':card.furigana,
        'birthday':card.birthday,
        'favourite':card.favourite,
        'skills':card.skills,
        'card_code':card.card_code
        }
    return jsonify(respon)
'''
req = request.json
return jsonify(req), 200
'''

'''
class Spam(Resource):
    def get(self):
        return [{'id': x.pk, 'name': x.name, 'note': x.note} for x in get_all()]

api = Api(api_bp)
api.add_resource(Spam, '/spam')
'''