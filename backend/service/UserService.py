from backend.config import *
from backend.model.UserModel import *
from mongoengine import *
"""
This file include Any calls used to create, delete, modify, and view information about users.
"""

# user_number = USER_NUMBER

def username_available(gmail, tokenId):  
    # This fucntion only checks if the gmail account already
    # exists in our database. Only if it does not exist, will
    # we seek authentication from google. So, we do not need
    # the tokenId argument here. 
    
    """Checks if a given gmail is available

    @:param gmail, tokenId
    @:return True if id is available to use, False otherwise

    If the username is already in use, it is not available
    """
    try:
        user = User.objects(gmail=gmail).get()
        return False  
    except DoesNotExist:
        print('username is available')
        return True 
    


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



def get_user_by_userId(id):
    """ Return the user with given userId

    :param userId
    :return User object, or empty list if not found
    """
    try:
        user = User.objects(user_id=id).get()
        return user
    except DoesNotExist:
        return []


def create_profile(user_id, first_name, last_name, date_of_birth, gender):
    """Create a new Profile Object and assign it to the user with user_id

    @:param user_id, first_name, last_name, date_of_birth, gender
    @:return True if creation was successful, false otherwise
    """
    profile = Profile(
        first_name=first_name,
        last_name=last_name,
        date_of_birth=date_of_birth,
        gender=gender)
    user = get_user_by_userId(user_id)
    if user == []:
        return False
    user.profile = profile
    return True


def create_user_settings(user_id, location_sharing_on, location, preferences):
    """Create settings for a user, and assign it to the user with user_id

    @:param user_id, location_sharing_on, location, preferences
    @:return True if creation was successful, false otherwise
    """
    userSettings = UserSettings(
        location_sharing_on=location_sharing_on,
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
