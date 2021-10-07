from flask import Flask
from flask import jsonify, request
from posts import posts
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/posts')
def index():
    lang = request.headers.get("Accept-Language",'en')[:2]
    

    p = list(map(lambda post: translate(post, lang),posts))
    return jsonify(p)

@app.route('/posts/<int:id>',methods=['POST'])
@cross_origin()
def buy(id):
    data = request.get_json()
    
    return jsonify(data)

def translate(post, lang):
    translation = next(t for t in post['translations'] if t['locale'] == lang)
    return {
        "id" :post['id'],
        "title": translation['title'],
        "description": translation['description'],
        "image":post['image'],
    }

app.run(port=5000)