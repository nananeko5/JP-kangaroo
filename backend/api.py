from flask import Blueprint,request, jsonify
from flask_restful import Api, Resource
from models import get_all

api_bp = Blueprint('api', __name__, url_prefix='/api')


@api_bp.route('/spam', methods=['GET'])
def getUserList():

    res = "aaa"

    return jsonify(res), 200
@api_bp.route('/spam', methods=['POST'])
def createCard():

    req = request.json
    


    return jsonify(req), 200

'''
class Spam(Resource):
    def get(self):
        return [{'id': x.pk, 'name': x.name, 'note': x.note} for x in get_all()]

api = Api(api_bp)
api.add_resource(Spam, '/spam')
'''