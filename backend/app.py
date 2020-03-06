from flask import Flask
from flask import jsonify, request, session
from backend.config import *
from mongoengine import *
import backend.service.UserService as service
import backend.service.RequestService as r_service
from backend.algorithm.packer import PreferenceVector
import os
from flask_session import Session
from backend.algorithm.util import sort_pref
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/google_login", methods=['POST'])
def google_login_verify():
        data = request.get_json()
        token_id = data['token_id']
        email = data['email']

        # if the this is a new user, create the account with gmail
        if service.get_user_by_email(email) is None:
            new_user = service.create_user_with_gmail(email)
            if new_user is None:
                return jsonify({"login_verify": False, "user_creation": False})
            else:
                # front end should open new page for user to fill out profile and preferences
                session['tokenID'] = token_id
                return jsonify({"login_verify": True, "user_creation": True})
        else:
            session['tokenID'] = token_id
            return jsonify({"login_verify": True, "user_creation": False})


# dont use this for now
@app.route("/login", methods=['POST'])
def login_verify():
    data = request.get_json()
    tokenID = data['token_id']
    email = data['email']
    if service.get_user_by_email(email) is None:
        # user does not exist
        return jsonify({"login_success": False})
    else:
        session['tokenID'] = tokenID
        session['email'] = email
        return jsonify({"login_success": True})

@app.route("/user/create_profile", methods=['POST'])
def create_profile():
    # front-end should call this for new users, to create profile
    data = request.get_json()
    first_name = data['first_name']
    last_name = data['last_name']
    date_of_birth = data['date_of_birth']
    gender = data['gender']
    email = data['email']

    profile = service.create_profile(email, first_name, last_name, date_of_birth, gender)
    if profile is None:
        return jsonify({"create_profile_success": False})
    else:
        return jsonify({"create_profile_success": True})

@app.route("/user/create_settings", methods=['POST'])
def update_settings():
    # front-end should call this for new users, to create settings
    data = request.get_json()
    email = data['email']

    user_settings = service.update_user_settings(email, data)
    if user_settings is None:
        return jsonify({"update_settings_success": False})
    else:
        return jsonify({"update_settings_success": True})

@app.route("/user/<email>", methods=['GET'])
def user_page(email):
    # front-end should call this function once user have successfully logged in and have profile set
    user = service.get_user_profile_by_email(email)
    if user is None:
        return jsonify({"profile_exist": False})
    else:
        return jsonify({"profile_exist": True, "profile": user.json()})

@app.route("/preference/match", methods=["POST"])
def preference_match():
    data = request.get_json()
    allPrefs = r_service.get_all_user_preferences()
    approach = data["request_type"]
    bonus_list = sort_pref(allPrefs, approach)
    # TODO: return the corresponding json on Friday
    returned_list = [y for x, y in bonus_list]
    return jsonify(returned_list), 200

if __name__ == "__main__":
    res = connect(DATABASE_NAME, host=HOST_IP, port=PORT, username=USERNAME, password=PASSWORD,
              authentication_source=AUTHENTICATION_SOURCE)
    print("The server is launchuing....")
    Session(app)
    app.run(host="0.0.0.0", port=os.environ.get('PORT', 8080))