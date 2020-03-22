import json
import os

from flask import Flask, jsonify, request
from flask_cors import CORS


class User():
    def __init__(self, ID, Email=""):
        self.ID = ID
        self.Email = Email


app = Flask(__name__, static_url_path='', static_folder='static')
CORS(app)


### DO NOT modify this route ###
@app.route('/')
def hello_world():
    return 'server setup'


@app.route('/auth', methods=['POST'])
def store():
    data = request.get_json()
    print(data)
    uid = data["ID"]
    with open('data/' + uid + 'json', 'w') as outfile:
        json.dump(data, outfile)
    return jsonify(request.json)


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='localhost', debug=True, port=os.environ.get('PORT', 8080))
