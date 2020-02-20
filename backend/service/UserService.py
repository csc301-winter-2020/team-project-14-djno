from backend import config
"""
This file include Any calls used to create, delete, modify, and view information about users.
"""


def create_user(username, password, email):
    """Create a new user with given inputs:

    @:param username, password, email
    @:return User object if successful creation, false otherwise

    generate user_id with USER_NUMBER variable from config
    """


def username_available(username):
    """Checks if a given username is available

    @:param username
    @:return True if username is available to use, False otherwise

    If the username is already in use, it is not available
    """


def change_password(username, cur_password, new_password):
    """Changes the password of a user, given the correct old password of the user.

    @:param username, cur_password, new_password
    @:return True if change was successful

    Allow the change only if provided the correct current password
    """


def get_user_by_username(username):
    """ Return the user with given username

    :param username
    :return User object, or False if not found
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