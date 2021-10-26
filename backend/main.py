from flask import Flask, render_template,jsonify
from api import api_bp
from models import get_all, init_db, insert
from random import *
from flask_cors import CORS

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg'])


app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myspa.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.register_blueprint(api_bp)

CORS(app)

@app.route('/', defaults={'path': ''})
@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        init_db(app)
    app.run()