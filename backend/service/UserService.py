from config import *
from model.UserModel import *
from mongoengine import *
from mongoengine.errors import NotUniqueError
import json
from datetime import datetime

"""
This file include Any calls used to create, delete, modify, and view information about users.
"""


def create_update_user(data):
    """ data is in JSON format """
    new_user = User.from_json(data).save()
    return new_user


def create_user(gmail, coordinates=[0, 0]):
    """ Creates a new user using google login
    :param gmail, coordinates
    :return User object upon successful creation, None otherwise
    """
    try:
        new_user = User(
            email=gmail,
            point=coordinates
        )
        new_user.save()
        # print("New user created!")
        return new_user
    except Exception as e:
        print("User could not be created")
        print(e.with_traceback)
        return None


def get_user_by_email(email):
    """ Return the user with given email
    :param email
    :return User object if user exist, None otherwise
    """
    try:
        user = User.objects(email=email).get()
        return user
    except DoesNotExist:
        return None


def email_available(email):
    # This function only checks if the email account already
    # exists in our database. Only if it does not exist, will
    # we seek authentication from google.
    """Checks if a given email is available
    @:param email
    @:return True if email is available to use,  False otherwise
    If the email is already in use, it is not available
    """
    try:
        user = User.objects(email=email).get()
        return False
    except DoesNotExist:
        print('email is available')
        return True


def create_update_profile(data):
    return Profile.from_json(data).save()


def create_profile(email, first_name, last_name, date_of_birth, age, gender, location, image_url=""):
    """ Creates a new Profile Object and assigns it to the user with email <email>
    @:param email, first_name, last_name, date_of_birth, age, gender, location, image_url
    @:return Profile Object if creation was successful, None otherwise
    """
    try:
        profile = Profile(
            email=email,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            age=age,
            gender=gender,
            location=location,
            image_url=image_url)
        profile.save()
        return profile
    except:
        return None


def update_profile(email, first_name, last_name, date_of_birth, age, gender, location, image_url):
    """ Updates user's profile """
    profile = get_user_profile_by_email(email)
    if profile:
        profile.update(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            age=age,
            gender=gender,
            location=location,
            image_url=image_url
        )
        return True
    else:
        return False


def get_user_profile_by_email(email):
    """ Return the user profile with given email
    :param email
    :return Profile object if user exist, None otherwise
    """
    try:
        profile = Profile.objects(email=email).get()
        return profile
    except DoesNotExist:
        return None


def create_update_settings(data):
    return Settings.from_json(data).save()


def create_settings(email, gps, preferences, days, time_of_day):
    try:
        setting = Settings(
            email=email,
            location_enabled=gps,
            preferences=preferences,
            days=days,
            time_of_day=time_of_day
        )
        setting.save()
        return setting
    except:
        return None

# May not be needed


def update_settings(email, gps, preferences, days, time_of_day):
    """ Updates user's settings """
    settings = get_user_settings_by_email(email)
    if settings:
        settings.update(
            location_enabled=gps,
            preferences=preferences,
            days=days,
            time_of_day=time_of_day
        )
        return True
    else:
        return False


def get_user_settings_by_email(email):
    """ Return the user setting with given email
    :param email
    :return UserSettings object if user exist, None otherwise
    """
    try:
        user_settings = Settings.objects(email=email).get()
        return user_settings
    except DoesNotExist:
        return None


if __name__ == "__main__":
    connect('david', host=HOST_IP, port=PORT, username=USERNAME, password=PASSWORD,
            authentication_source=AUTHENTICATION_SOURCE)
    print("connected")

    # User.drop_collection()
    # Profile.drop_collection()
    # Settings.drop_collection()

    # Test create_update_user function
    email = "h5vhh@gmail.com"
    userData = {
        "email": email,
        "point": [-93.832722, 50.997865]
    }
    new_user = create_update_user(json.dumps(userData))
    assert get_user_by_email(email) != None, "user should be in db"

    # Test create_update_settings
    settingsData = {
        "email": email,
        "location_enabled": True,
        "preferences": ["OPC"],
        "days": ["Saturday"],
        "time_of_day": ["Afternoon"]
    }
    settings = create_update_settings(json.dumps(settingsData))
    assert get_user_settings_by_email(
        email) != None, "settings should be in db"

    # Test create_update_profile
    profileData = {
        "email": email,
        "first_name": "abc",
        "last_name": "xyz",
        "date_of_birth": "2016-05-22",
        "gender": "Other",
        "location": "PQR"
    }
    profile = create_update_profile(json.dumps(profileData))
    assert get_user_profile_by_email(email) != None, "profile should be in db"

    new_user.delete()
    settings.delete()
    profile.delete()

    disconnect()
    print("disconnected")