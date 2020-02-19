from backend import config


def create_user(username, password, email):
    """Create a new user with given inputs:

    @:param username, password, email
    @:return True if successful creation, false otherwise

    generate user_id with USER_NUMBER constant from config

    """


def username_available(username):
    """Checks if a given username is available

    @:param username
    @:return True if username is already used, False otherwise

    """


def change_password(username, cur_password, new_password):
    """Changes the password of a user, given the correct old password of the user.

    @:param username, cur_password, new_password
    @:return True if change was successful

    Allow the change only if provided the correct current password

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