import os

import mongoengine
from flask import Flask, redirect
from flask import jsonify, request, session

import service.RequestService as r_service
import service.UserService as service
from algorithm.util import sort_pref
from config import *

app = Flask(__name__, static_url_path="", static_folder="static")
res = mongoengine.connect(DATABASE_NAME, host=HOST_IP, port=PORT,
                          username=USERNAME, password=PASSWORD,
                          authentication_source=AUTHENTICATION_SOURCE)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = SECRET_KEY
# sess = Session()
# sess.init_app(app)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def hello_world():
    # access_token = session.get("email")
    # if access_token is None:
    return redirect("/index.html", code=302)


# dont use this for now
@app.route("/login", methods=['POST'])
def login_verify():
    data = request.get_json()
    print("receiving...")
    print(data)
    if data is None:
        return jsonify({"login_success": False}), 400
    if "token_id" not in data:
        return jsonify({"login_success": False}), 400
    client_id = data["token_id"]
    print(data)
    try:
        email = data['email']
        session["email"] = email
        return jsonify({"login_success": True})
    except (ValueError, KeyError) as e:
        return jsonify({"login_success": False}), 400


@app.before_request
def if_login():
    print("filter processing...")
    print(session.get("email"))
    # print(request.endpoint)
    print(request.path)
    if (request.endpoint == "static"):
        if session.get("email") == None:
            print([x in request.path for x in APP_PAGE])
            if any([x in request.path for x in APP_PAGE]):
                print("not app page!")
                # return jsonify({"warning": "please login before you fetch data from servr"})
                return redirect("/index.html", code=302)
    if (request.endpoint == "login_verify"):
        pass
    else:
        if (session.get("email") == None and request.endpoint != "static"):
            # return redirect("/index.html", code=302)
            return redirect("/index.html", code=302)


@app.route("/signout", methods=["POST"])
def signout():
    session.clear()
    return jsonify({"signout": True})


@app.route("/user/profile", methods=['POST'])
def create_profile():
    # front-end should call this for new users, to create profile
    data = request.get_json()
    print(data)
    if data is None:
        return jsonify({"create_profile_success": False}), 400
    try:
        first_name = data['first_name']
        last_name = data['last_name']
        date_of_birth = data['date_of_birth']
        gender = data['gender']
        email = session['email']
        image_url = "" if "image_url" not in data else data["image_url"]
        profile = service.create_profile(
            email, first_name, last_name, date_of_birth, gender, image_url)
        print(profile)
        if profile is None:
            return jsonify({"create_profile_success": False}), 400
        else:
            return jsonify({"create_profile_success": True})
    except (KeyError, ValueError) as e:
        return jsonify({"create_profile_success": False}), 400


@app.route("/user/settings", methods=['POST'])
def update_settings():
    # front-end should call this for new users, to create settings
    data = request.get_json()
    print(data)
    if data is None:
        return jsonify({"update_settings_success": False}), 400
    try:
        user_settings = service.update_user_settings(data)
        if user_settings is None:
            return jsonify({"update_settings_success": False}), 400
        else:
            return jsonify({"update_settings_success": True})
    except (ValueError, KeyError) as e:
        return jsonify({"update_settings_success": False}), 400


@app.route("/user/email/<email>", methods=['GET'])
def user_page(email):
    print("the request is: ")
    print(email)
    user = service.get_user_profile_by_email(email)
    if user is None:
        return jsonify({"profile_exist": False})
    else:
        return jsonify({"profile_exist": True, "profile": user.json()})


@app.route("/match", methods=["POST"])
def preference_match():
    data = request.get_json()
    if data is None:
        return jsonify({"warning": "please at least send a json..."})
    try:
        allPrefs = r_service.get_all_user_preferences()
        approach = data["request_type"]
        bonus_list = sort_pref(allPrefs, approach)
        # TODO: return the corresponding json on Friday
        returned_list = [y for x, y in bonus_list]
        print(returned_list)
        return jsonify(returned_list[:10]), 200
    except (KeyError, ValueError) as e:
        return jsonify([]), 400


@app.route("/user/settings/<email>", methods=["GET"])
def get_user_setting(email):
    print("getting setting emails...")
    data = service.get_user_setting_by_email(email)
    if data is None:
        return jsonify({})
    return data.to_json()


application = app

if __name__ == "__main__":
    # res = mongoengine.connect(DATABASE_NAME, host=HOST_IP, port=PORT, username=USERNAME, password=PASSWORD,
    #                           authentication_source=AUTHENTICATION_SOURCE)
    print("The server is launching....")
    # Session(app)
    app.run(host="0.0.0.0", port=os.environ.get('PORT', 8080))
