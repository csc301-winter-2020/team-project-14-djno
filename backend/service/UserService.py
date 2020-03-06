from backend.config import *
from backend.model.UserModel import *
from mongoengine import *

"""
This file include Any calls used to create, delete, modify, and view information about users.
"""


def create_user_with_gmail(gmail):
    """ Create a user using google login

    :param gmail, id, username
    :return: User object if successful creation, false otherwise
    """
    try:
        new_user = User(
            email=gmail
        )
        new_user.save()
        return new_user
    except:
        return None

# not used right now
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

    # create_user function does not need name argument. Name is being stored in the create_profile function

# not used right now
def create_user(gmail, name, tokenId=""):
    """Create a new user with given inputs:

    @:param tokenId, gmail, name
    @:return User object if successful creation, false otherwise

    generate email with USER_NUMBER variable from config
    """

    # global user_number

    # if not username_available(username):
    #     return False
    # else:
    #     new_user = User(
    #         username=username,
    #         password=password,
    #         email=email
    #     ).save()

    #     new_user.save()
    # return new_user

    # if not username_available(gmail):
    #     return False
    # elif token_id == "":
    #     return False
    # else:
    #     new_user = User(
    #        email=email
    #     ).save()
    # return True


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

def get_user_setting_by_email(email):
    """ Return the user setting with given email

    :param email
    :return UserSettings object if user exist, None otherwise
    """
    try:
        user_settings = UserSettings.objects(email=email).get()
        return user_settings
    except DoesNotExist:
        return None


def create_profile(email, first_name, last_name, date_of_birth, gender):
    """Create a new Profile Object and assign it to the user with email

    @:param email, first_name, last_name, date_of_birth, gender
    @:return Profile Object if creation was successful, false otherwise

    Check email exist
    """

    # check if email does not exist
    if not get_user_by_email(email):
        return None

    try:
        profile = Profile(
            email=email,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            gender=gender)
        profile.save()
        return profile
    except:
        return None


def update_user_settings(email, **preferences_json):
    # todo: add the preferences here, preferences is passed in as a json
    """Create settings for a user, if it already exist, update it and assign it to the user with email

    @:param email, location, preferences
    @:return True if creation was successful, false otherwise
    """
    preferences_json["email"] = email
    # user setting not set, create it
    if get_user_setting_by_email(email) is None:
        try:
            user_settings = UserSettings(
                **preferences_json
            )
            user_settings.save()
        except:
            return None
        return user_settings
    return None

# not used right now
def get_user_profile(email):
    """ Get the profile of user with email

    :param emails
    :return: Profile object, or False
    """
    user = get_user_by_email(email)
    if user == []:
        return None
    return user.profile
