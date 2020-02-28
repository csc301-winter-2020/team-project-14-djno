from flask import Flask
from flask import jsonify, request, session
from backend.config import *
from mongoengine import *
import backend.service.UserService as service
from backend.algorithm.packer import PreferenceVector
import os
from flask_session import Session
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/login", methods=['POST'])
def login_verify():
    data = request.get_json()
    tokenId = data['tokenId']
    name = data['name']
    gmail = data['email']
    if (service.username_available(gmail)):
        session['tokenId'] = tokenId
        return jsonify({"userValid": True})
    else:
        if (tokenId and name and gmail):
            if not service.create_user(gmail, name, tokenId):
                return jsonify({"userValid": False})
        # TODO: call create_user here
    return jsonify({"userValid": True})
@app.route("/preference", methods=["POST"])
def preference_match():
    data = request.get_json()
    current_pref_v = PreferenceVector.build_vector(data)
    return "good"
if __name__ == "__main__":
    res = connect(DATABASE_NAME, host=HOST_IP, port=PORT, username=USERNAME, password=PASSWORD,
              authentication_source=AUTHENTICATION_SOURCE)
    print("The server is launchuing....")
    Session(app)
    app.run(host="0.0.0.0", port=os.environ.get('PORT', 8080))