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
def verify_login():
    data = request.get_json()
    print("Received: {}".format(data))

    if data is None or "token_id" not in data:
        return jsonify({"login_success": False}), 400

    try:
        email = data['email']
        session["email"] = email
        return jsonify({"login_success": True})

    except (ValueError, KeyError) as e:
        print(e)
        return jsonify({"login_success": False}), 400


@app.before_request
def if_login():
    print("filter processing...")
    print(session.get("email"))
    # print(request.endpoint)
    print(request.path)
    if request.endpoint == "static":
        if session.get("email") is None:
            print([x in request.path for x in APP_PAGE])
            if any([x in request.path for x in APP_PAGE]):
                print("not app page!")
                # return jsonify({"warning": "please login before you fetch data from servr"})
                return redirect("/index.html", code=302)
    if request.endpoint == "verify_login":
        pass
    else:
        if (session.get("email") is None and request.endpoint != "static"):
            # return redirect("/index.html", code=302)
            return redirect("/index.html", code=302)


@app.route("/sign-out", methods=["POST"])
def sign_out():
    session.clear()
    return jsonify({"sign-out": True})


@app.route("/users", methods=['POST'])
def create_a_user():
    # front-end should call this for new users, to create profile
    data = request.get_json()
    print("Received: {}".format(data))

    if data is None:
        reason = "data is None"
        print("Failed to create a profile:", reason)
        return jsonify({"create_a_user_success": False, "reason": reason}), 400
    try:
        first_name = data['first_name']
        last_name = data['last_name']
        date_of_birth = data['date_of_birth']
        gender = data['gender']
        email = session['email']
        image_url = "" if "image_url" not in data else data["image_url"]
        description = data['description']

        profile = service.create_a_user(
            email, first_name, last_name, date_of_birth, gender, image_url,
            description)

        if profile is None:
            reason = "unable to create a profile object"
            print("Failed to create a profile:", reason)
            return jsonify(
                {"create_a_user_success": False, "reason": "reason"}), 400
        else:
            return jsonify({"create_a_user_success": True})

    except (KeyError, ValueError) as e:
        reason = "missing key {}".format(e)
        print("Failed to create a profile:", reason)
        return jsonify({"create_a_user_success": False, "reason": reason}), 400


@app.route("/users/settings", methods=['POST'])
def update_a_user_settings():
    # front-end should call this for new users, to create settings
    data = request.get_json()
    print(data)
    if data is None:
        return jsonify({"update_a_user_settings_success": False}), 400
    try:
        user_settings = service.update_user_settings(data)
        if user_settings is None:
            return jsonify({"update_a_user_settings_success": False}), 400
        else:
            return jsonify({"update_a_user_settings_success": True})
    except (ValueError, KeyError) as e:
        print(e)
        return jsonify({"update_a_user_settings_success": False}), 400


@app.route("/users/<email>", methods=['GET'])
def get_a_user(email):
    print("Requesting user profile of ", email)

    user = service.get_user_profile_by_email(email)
    if user is None:
        return jsonify({"profile_exist": False})
    else:
        return jsonify({"profile_exist": True, "profile": user.json()})


@app.route("/match", methods=["POST", "GET"])
def perform_preference_match():
    data = request.get_json()
    if data is None:
        return jsonify({"warning": "please at least send a json..."})
    try:
        allPrefs = r_service.get_all_user_preferences()
        approach = data["request_type"][0]
        bonus_list = sort_pref(allPrefs, approach, data["location"])
        # print(bonus_list)
        # TODO: return the corresponding json on Friday
        returned_list = [y for x, y in bonus_list]
        print(returned_list)
        new_dict = {"email": data["email"], "request_type": approach,
                    "location": data["location"]}
        inv_a_maps = {v: k for k, v in a_maps.items()}
        # print(inv_a_maps)
        # print(sub)
        for key, constraint in sub_category.items():
            print("key: {}, approach: {}".format(key, approach))
            if key == approach:
                for way in constraint:
                    new_dict[inv_a_maps[way]] = True
            else:
                for way in constraint:
                    new_dict[inv_a_maps[way]] = False
        print("new dictionary!")
        print(new_dict)
        returned_list = [x for x in returned_list if
                         x["email"] != data["email"]]
        service.update_user_settings(new_dict)
        return jsonify(returned_list[:10]), 200
    except (KeyError, ValueError) as e:
        print(e)
        if "location" not in data:
            return jsonify({"warn": "You need a location for matching!"})
        return jsonify([]), 400


@app.route("/users/settings/<email>", methods=["GET"])
def get_user_setting(email):
    print("Getting setting emails...")
    data = service.get_user_setting_by_email(email)
    if data is None:
        return jsonify({})
    return data.to_json()


application = app

if __name__ == "__main__":
    # res = mongoengine.connect(DATABASE_NAME, host=HOST_IP, port=PORT, username=USERNAME, password=PASSWORD,
    #                           authentication_source=AUTHENTICATION_SOURCE)
    # Session(app)
    app.run(host="0.0.0.0", port=os.environ.get('PORT', 8080))
