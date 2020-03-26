import os

import mongoengine
from flask import Flask, redirect, g
from flask import jsonify, request, session
from flask_socketio import SocketIO, send, emit, join_room, leave_room
import service.RequestService as r_service
import service.UserService as service
from algorithm.util import sort_pref
from config import *
import pickle
from collections import defaultdict
app = Flask(__name__, static_url_path="", static_folder="static")
res = mongoengine.connect(DATABASE_NAME, host=HOST_IP, port=PORT,
                          username=USERNAME, password=PASSWORD,
                          authentication_source=AUTHENTICATION_SOURCE)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = SECRET_KEY
# sess = Session()
# sess.init_app(app)
app.config['SECRET_KEY'] = SECRET_KEY
socket_app = SocketIO(app)
chat_target = defaultdict(list)
connected_id = set()
connected_listening_id = set()
@app.route('/')
def hello_world():
    # access_token = session.get("email")
    # if access_token is None:
    return redirect("/index.html", code=302)


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
    print("filter processing at {} for {}".format(
        request.path, session.get("email")))

    if request.endpoint == "static":
        if session.get("email") is None:
            if any([x in request.path for x in APP_PAGE]):
                print("Accessing main app without logging in")
                # return jsonify({"warning": "please login before you fetch data from servr"})
                return redirect("/login.html", code=302)
    if request.endpoint == "verify_login":
        pass
    else:
        if (session.get("email") is None and request.endpoint != "static"):
            # return redirect("/index.html", code=302)
            return redirect("/login.html", code=302)


@app.route("/sign-out", methods=["POST"])
def sign_out():
    session.clear()
    return jsonify({"sign_out": True})


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
        user_settings = service.save_other_setting(data)

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
        approach = data["request_type"]
        approach = service_to_pref[approach]
        bonus_list = sort_pref(allPrefs, approach, data["location"])
        # print(bonus_list)
        # TODO: return the corresponding json on Friday
        returned_list = [y for x, y in bonus_list]
        print("bonus")
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
        print("the following key has issue")
        print(e)
        if "location" not in data:
            return jsonify({"warn": "You need a location for matching!"})
        return jsonify([]), 400


@app.route("/users/settings/<email>", methods=["GET"])
def get_user_setting(email):
    print("Getting setting emails...")
    data = service.get_other_setting(email)

    # data is never None
    # if data is None:
    #     return jsonify({})

    # Create user setting if it does not exist
    if len(data) == 0:
        service.save_other_setting({"email": email})    # Create user setting
        data = service.get_other_setting(email)

    return data[0].to_json()


@socket_app.on("test")
def handle_testing(message):
    print("received message: ... {}".format(message))


@socket_app.on("connect")
def handle_connect():
    send("succeed!")


@socket_app.on("chat")
def handle_chat(message):
    print("{} is messaging to... {}".format(
        message["email"], message["target"]))
    print(message["target"] in chat_target)
    print(chat_target)
    if message["target"] in chat_target:
        email_target = message["target"]
        chat_to = chat_target[email_target][0]
        # join_room(message["target"])
        print("sending to...{}".format(chat_to))
        if chat_to in connected_id:
            emit(
                "chat", {"message": message["message"], "src": message["email"]}, room=chat_to)
        elif chat_to in connected_listening_id:
            emit("notify", {"message": message["message"], "src": message["email"]}, room=chat_to)
        else:
            emit("failed", {
                 "message": "The user you're sending to is not online"})
    else:
        emit("failed", {
             "message": "The user you're sending to is not connected to our app"})
    print("sid is: {}".format(request.sid))


@socket_app.on("join")
def start_join(message):
    connected_id.add(request.sid)
    chat_target[message["email"]].clear()
    chat_target[message["email"]].append(request.sid)
    # print("current chat_table: {}".format(chat_target))
    emit("joined", {"message": "you have joined!"})


@socket_app.on("disconnect")
def when_disconnect():
    print("disconnected!")
    print(connected_id)
    connected_id.discard(request.sid)
    connected_listening_id.discard(request.sid)
# for notification system
@socket_app.on("listening")
def when_listening(message):
    chat_target[message["email"]].clear()
    chat_target[message["email"]].append(request.sid)
    connected_listening_id.add(request.sid)
    emit("listened", {"message": "Listening to the server..."})
# @socket_app.on("connect")
# def handle_connect(message):

#     # send("Welcome: {}".format(name))
#     send("shit!")
# @socket_app.on("start_chat")
# def join_chat(message):
#     username = message["email"]
#     roomTarget = message["email"]


# @socket_app.on("leave_room")
# def leave_chat(message):
#     leave_room(message["email"])
# @socket_app.on("message")
# def dm_to(message):
#     send(pickle.dumps({"name": message["name"],
#             "msg": message["message"]}), room=message["target"])
application = socket_app

if __name__ == "__main__":
    # res = mongoengine.connect(DATABASE_NAME, host=HOST_IP, port=PORT, username=USERNAME, password=PASSWORD,
    #                           authentication_source=AUTHENTICATION_SOURCE)
    # Session(app)
    socket_app.run(app, host="0.0.0.0", port=os.environ.get('PORT', 8080))
