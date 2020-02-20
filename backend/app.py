from flask import Flask
from flask import jsonify, request
from backend.config import *
from mongoengine import *
import backend.service.UserService as service
import os

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
        return jsonify({"userValid": True})
        # TODO: implementing session
    else:
        if (tokenId and name and gmail):
            pass
        # TODO: call create_user here
        return jsonify({"userValid": False})

if __name__ == "__main__":
    res = connect(DATABASE_NAME, host=HOST_IP, port=PORT, username=USERNAME, password=PASSWORD,
              authentication_source=AUTHENTICATION_SOURCE)
    print("The server is launchuing....")
    app.run(host="0.0.0.0", port=os.environ.get('PORT', 8080))