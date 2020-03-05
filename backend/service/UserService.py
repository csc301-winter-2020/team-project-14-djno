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

def get_user_setting_by_userId(id):
    """ Return the user setting with given userId

    :param userId
    :return UserSettings object if user exist, false otherwise
    """
    try:
        user = UserSettings.objects(user_id=id).get()
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


def update_user_settings(user_id, location=None,  **preferences_json):
    # todo: add the preferences here, preferences is passed in as a json
    """Create settings for a user, if it already exist, update it and assign it to the user with user_id

    @:param user_id, location, preferences
    @:return True if creation was successful, false otherwise
    """

    # user setting not set, create it
    if get_user_setting_by_userId is False:
        try:
            user_settings = UserSettings(
                user_id=user_id,
                location=location,
                education_navigation=preferences_json["REN"],
                education_support=preferences_json["RES"],
                employment_navigation=preferences_json["RENA"],
                employment_support=preferences_json["RESA"],
                health_care_navigation=preferences_json["RHN"],
                health_care_support=preferences_json["RHS"],
                local_navigation=preferences_json["RLN"],
                local_support=preferences_json["RLS"],
                well_being_leisure=preferences_json["RWL"],
                pick_up_and_delivery=preferences_json["RPUD"],
                pick_up_and_drop_off=preferences_json["RPUO"],
                homemaking_supports=preferences_json["RHMS"]
            )
        except:
            return False
        return user_settings
    return False
    # todo:
    # update
    # else:
    #     try:
    #         user_settings = UserSettings(
    #             user_id=user_id,
    #             location=location,
    #             education_navigation=preferences_json["REN"],
    #             education_support=preferences_json["RES"],
    #             employment_navigation=preferences_json["RENA"],
    #             employment_support=preferences_json["RESA"],
    #             health_care_navigation=preferences_json["RHN"],
    #             health_care_support=preferences_json["RHS"],
    #             local_navigation=preferences_json["RLN"],
    #             local_support=preferences_json["RLS"],
    #             well_being_leisure=preferences_json["RWL"],
    #             pick_up_and_delivery=preferences_json["RPUD"],
    #             pick_up_and_drop_off=preferences_json["RPUO"],
    #             homemaking_supports=preferences_json["RHMS"]
    #         )
    #     except:
    #         return False
    #     return user_settings


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

