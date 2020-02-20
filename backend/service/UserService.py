from backend.config import *
from backend.model.UserModel import *
from mongoengine import *
"""
This file include Any calls used to create, delete, modify, and view information about users.
"""

# user_number = USER_NUMBER


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
    pass

def username_available(gmail, tokenId):
    """Checks if a given gmail is available

    @:param gmail, tokenId
    @:return True if id is available to use, False otherwise

    If the username is already in use, it is not available
    """
    return True  # todo implement

def get_user_by_username(name):
    """ Return the user with given username

    :param username
    :return User object, or empty list if not found
    """


def create_profile(user_id, first_name, last_name, date_of_birth, gender):
    """Create a new Profile Object and assign it to the user with user_id

    @:param user_id, first_name, last_name, date_of_birth, gender
    @:return True if creation was successful, false otherwise
    """


def create_user_settings(user_id, location_sharing_on, location, preferences):
    """Create settings for a user, and assign it to the user with user_id

    @:param user_id, location_sharing_on, location, preferences
    @:return True if creation was successful, false otherwise
    """


def get_user_profile(username):
    """ Get the profile of user with username

    :param username
    :return: Profile object, or False
    """


# user_0 = create_user("user_000", "pass_000", "tester@uoft.ca")
# print(user_0)
