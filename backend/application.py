import os

import mongoengine
from flask import Flask, redirect
from flask import jsonify, request, session

import service.RequestService as r_service
import service.UserService as service
from algorithm.util import sort_pref
from backend.algorithm import new_algo
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


@app.route("/user", methods=["POST"])
def user():
    data = request.get_json()
    if data is None:
        jsonify({"return_user_success": False}), 400
    return service.create_update_user(data).to_json()


# If this one works, don't need the two below
@app.route("/user/profile", methods=["POST"])
def profile():
    data = request.get_json()
    if data is None:
        return jsonify({"return_profile_success": False}), 400
    return service.create_update_profile(data).to_json()


@app.route("/user/profile/create", methods=['POST'])
def create_profile():
    data = request.get_json()
    # print(data)
    if data is None:
        return jsonify({"create_profile_success": False}), 400
    # use from_json method
    return profile_helper(data, True)


@app.route("/user/profile/update", methods=['POST'])
def update_profile():
    data = request.get_json()
    if data is None:
        return jsonify({"update_profile_success": False}), 400
    return profile_helper(data, False)


def profile_helper(data, flag):
    """ If flag, create a new profile. Otherwise update."""
    s = "create_profile_success" if flag else "update_profile_success"
    try:
        email = session['email']
        first_name = data['first_name']
        last_name = data['last_name']
        date_of_birth = data['date_of_birth']
        age = data['age']
        gender = data['gender']
        location = data['location']
        image_url = "" if "image_url" not in data else data["image_url"]
        if flag:
            profile = service.create_profile(
                email, first_name, last_name, date_of_birth, age, gender, location, image_url)
        else:
            profile = service.update_profile(
                email, first_name, last_name, date_of_birth, age, gender, location, image_url)
        # print(profile)
        if not profile:
            return jsonify({s: False}), 400
        else:
            return jsonify({s: True})
    except (KeyError, ValueError) as e:
        return jsonify({s: False}), 400


# If this one works, don't need the two below
@app.route("/user/settings", methods=["POST"])
def settings():
    data = request.get_json()
    if data is None:
        return jsonify({"return_settings_success": False}), 400
    return service.create_update_settings(data).to_json()


@app.route("/user/settings/create", methods=['POST'])
def create_settings():
    data = request.get_json()
    # print(data)
    if data is None:
        return jsonify({"create_settings_success": False}), 400
    return settings_helper(data, True)


@app.route("/user/settings/update", methods=['POST'])
def update_settings():
    data = request.get_json()
    # print(data)
    if data is None:
        return jsonify({"update_settings_success": False}), 400
    return settings_helper(data, False)


def settings_helper(data, flag):
    """ If flag, create a new settings. Otherwise update."""
    s = "create_settings_success" if flag else "update_settings_success"
    try:
        email = session['email']
        gps = data['gps']
        preferences = Preferences.from_json(data['preferences'])
        days = DayAvailability.from_json(data['days'])
        time = TimeAvailability.from_json(data['time_of_day'])
        if flag:
            settings = service.create_settings(
                email, gps, preferences, days, time)
        else:
            profile = service.update_settings(
                email, gps, preferences, days, time)
        if not settings:
            return jsonify({s: False}), 400
        else:
            return jsonify({s: True})
    except (KeyError, ValueError) as e:
        return jsonify({s: False}), 400


@app.route("/user/request", methods=["POST"])
def request():
    data = request.get_json()
    if data is None:
        return jsonify({"return_request_success": False}), 400
    return r_service.create_update_request(data).to_json()


@app.route("/user/<email>", methods=["GET"])
def get_user(email):
    user = service.get_user_by_email(email)
    if user:
        return user.to_json()
    else:
        return jsonify({}), 400


@app.route("/user/profile/<email>", methods=['GET'])
def get_user_profile(email):
    # print("the request is: ")
    # print(email)
    profile = service.get_user_profile_by_email(email)
    if profile is None:
        return jsonify({"profile_exist": False})
    else:
        return jsonify({"profile_exist": True, "profile": user.to_json()})


@app.route("/user/settings/<email>", methods=["GET"])
def get_user_settings(email):
    # print("getting setting emails...")
    settings = service.get_user_settings_by_email(email)
    if settings is None:
        return jsonify({"settings_exist": False})
    return jsonify({"settings_exist": True, "settings": settings.to_json()})


# @app.route("user/request/<email>", methods=["GET"])
# def get_user_request(email):
#     request = r_service.get_request_by_email()


@app.route("/match", methods=["POST", "GET"])
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


@app.route("/new_match", methods=["POST"])
def new_match():
    data = request.get_json()
    if data is None:
        return jsonify({"warning": "please at least send a json..."})
    rs = new_algo.get_matches(data)
    if rs:
        return jsonify(rs[:10]), 200
    else:
        return jsonify([]), 400


application = app

if __name__ == "__main__":
    # res = mongoengine.connect(DATABASE_NAME, host=HOST_IP, port=PORT, username=USERNAME, password=PASSWORD,
    #                           authentication_source=AUTHENTICATION_SOURCE)
    # Session(app)
    app.run(host="0.0.0.0", port=os.environ.get('PORT', 8080))
