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

@app.route("/create_user_with_gmail", methods=['POST'])
def create_user_with_gmail():
    data = request.get_json()
    user_id = data['user_id']
    email = data['email']
    if not service.create_user_with_gmail(email, user_id):
        return jsonify({"user_creation_success": False})
    else:
        return jsonify({"user_creation_success": True})

@app.route("/login", methods=['POST'])
def login_verify():
    data = request.get_json()
    user_id = data['user_id']
    tokenID = data['token_id']

    if service.get_user_by_userId(user_id) is False:
        # user does not exist
        return jsonify({"login_success": False})
    else:
        session['tokenID'] = tokenID
        return jsonify({"login_success": True})

@app.route("/user/create_profile", methods=['POST'])
def create_profile():
    data = request.get_json()
    user_id = data['user_id']
    first_name = data['first_name']
    last_name = data['last_name']
    date_of_birth = data['date_of_birth']
    gender = data['gender']

    profile = service.create_profile(user_id, first_name, last_name, date_of_birth, gender)
    if profile is False:
        return jsonify({"create_profile_success": False})
    else:
        return jsonify({"create_profile_success": True})

@app.route("/user/<int:user_id>", methods=['GET'])
def user_page(user_id):
    # front-end should call this function once user have successfully logged in
    user = service.get_user_by_userId(user_id)
    if user is False:
        return jsonify({"profile_exist": False})
    else:
        return jsonify({"profile_exist": True, "profile": user.json()})

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