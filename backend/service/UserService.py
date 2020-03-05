from backend.config import *
from backend.model.UserModel import *
from mongoengine import *

"""
This file include Any calls used to create, delete, modify, and view information about users.
"""


def create_user_with_gmail(gmail, id):
    """ Create a user using google login

    :param gmail, id, username
    :return: User object if successful creation, false otherwise
    """
    try:
        new_user = User(
            user_id=id,
            email=gmail
        ).save()
        return new_user
    except:
        return False


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


def create_user(gmail, name, tokenId=""):
    """Create a new user with given inputs:

    @:param tokenId, gmail, name
    @:return User object if successful creation, false otherwise

    generate user_id with USER_NUMBER variable from config
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


# suggest argument be changed from id to gmail, and that be used in all subsequent functions

def get_user_by_userId(id):
    """ Return the user with given userId

    :param userId
    :return User object if user exist, false otherwise
    """
    try:
        user = User.objects(user_id=id).get()
        return user
    except DoesNotExist:
        return False


def create_profile(user_id, first_name, last_name, date_of_birth, gender):
    """Create a new Profile Object and assign it to the user with user_id

    @:param user_id, first_name, last_name, date_of_birth, gender
    @:return Profile Object if creation was successful, false otherwise

    Check user_id exist
    """

    # check if user_id does not exist
    if not get_user_by_userId(user_id):
        return False

    try:
        profile = Profile(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            gender=gender)
        profile.save()
        return profile
    except:
        return False


def create_user_settings(user_id, location, preferences):
    # todo: add the preferences here, preferences is passed in as a json
    """Create settings for a user, and assign it to the user with user_id

    @:param user_id, location, preferences
    @:return True if creation was successful, false otherwise
    """
    userSettings = UserSettings(
        location=location,
        preferences=preferences)
    user = get_user_by_userId(user_id)
    if user == []:
        return False
    user.profile.settings = userSettings
    return True


def get_user_profile(id):
    """ Get the profile of user with id

    :param id
    :return: Profile object, or False
    """
    user = get_user_by_userId(id)
    if user == []:
        return False
    return user.profile

# user_0 = create_user("user_000", "pass_000", "tester@uoft.ca")
# print(user_0)

