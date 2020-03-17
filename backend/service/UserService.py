from config import *
from model.UserModel import *
from mongoengine import *
from mongoengine.errors import NotUniqueError

"""
This file include Any calls used to create, delete, modify, and view information about users.
"""


def create_user(gmail, coordinates=[0, 0]):
    """ Creates a new user using google login

    :param gmail, coordinates
    :return User object upon successful creation, None otherwise
    """
    try:
        new_user = User(
            email=gmail,
            current_coordinates=coordinates
        )
        new_user.save()
        return new_user
    except:
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


def create_profile(email, first_name, last_name, date_of_birth, age, gender, location, image_url):
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
            image_url=image_url)
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
        profile=Profile.objects(email = email).get()
        return profile
    except DoesNotExist:
        return None


def create_settings(email, gps, preferences, days, time_of_day):
    try:
        setting=Settings(
            email = email,
            GPS = gps,
            preferences = preferences,
            days = days,
            time_of_day = time_of_day
        )
        setting.save()
        return setting
    except:
        return None


def update_user_settings(email, gps, preferences, days, time_of_day):
    """ Updates user's settings """
    settings=get_user_settings_by_email(email)
    if settings:
        settings.update(
            GPS = gps,
            preferences = preferences,
            days = days,
            time_of_day = time_of_day
        )
        return True
    else:
        return False


def get_user_setting_by_email(email):
    """ Return the user setting with given email

    :param email
    :return UserSettings object if user exist, None otherwise
    """
    try:
        user_settings=Settings.objects(email = email).get()
        return user_settings
    except DoesNotExist:
        return None
