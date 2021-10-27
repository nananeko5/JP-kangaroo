from flask import Blueprint,request, jsonify
from flask_restful import Api, Resource
from models import get_all,insert,update,print_card
from models import Card
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
    # img = request.files['jpg']
    # filename = secure_filename(img.filename) # 危険な文字を削除（サニタイズ処理）
    # img_url = os.path.join(api_bp.config['UPLOAD_FOLDER'], filename) # ファイルの保存
    # if (len(filename) == 0):
    #     fd, tempPath = mkstemp()
    #     filename = os.path.basename(tempPath)
    #     os.close(fd)
    # img.save(img_url)
    # print(img_url)
    # img_url = img_url[1:]
    json=request.json
    name = json[0]['name']
    furigana = json[0]['furigana']
    birthday = json[0]['birthday']
    birthday = datetime.strptime(birthday, '%Y-%m-%d')
    favourite = json[0]['favourite']
    skills = json[0]['skills']
    uID =json[0]['uID']
   
    dictionary={'imgpath': "aaa",'name':name,'furigana':furigana,'id':uID,
                'birthday':birthday,'favourite':favourite,'skills':skills}

    if Card.query.filter(Card.id == dictionary['id']['uID']).scalar() != None:
        update(dictionary)
        print("update!!")
    else :
        insert(dictionary)
        print("insert!!")
    card = Card.query.filter(Card.id==dictionary['id']['uID']).first()
    response_json={'name':card.name,'furigana':card.furigana,'birthday':card.birthday,'favourite':card.favourite,'skills':card.skills}
    return jsonify(response_json)

@api_bp.route('/user_info', methods=['POST'])
def get_info():
    json=request.json
    card= Card.query.filter(Card.id==json[0]['uID']).first()
    response_json={'name':card.name,'furigana':card.furigana,'birthday':card.birthday,'favourite':card.favourite,'skills':card.skills}
    return jsonify(response_json)




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