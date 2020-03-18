from datetime import datetime
from model.RequestModel import *
from mongoengine import errors
from model.UserModel import Profile, Settings

"""
This file include Any calls used to create, delete, modify, and view information about Requests.
"""


def create_request(email, name, location=[0, 0], time, rtype, description):
    """Creates a new request

    @:param email, name, location, time, rtype, description
    @:return Request object upon successful creation, None otherwise
    """
    if not isRegistered(email):
        return False
    try:
        new_request = Request(
            requestor_email=email,
            request_type=rtype,
            title=name,
            description=description,
            point=location,
            time_of_request=time
        ).save()
        return new_request
    except:
        return False


def accept_request(acceptor_user, request, time_accepted=datetime.utcnow):
    """ Accept an open request

    @:param acceptor_user, request, time_accepted
    :return: AcceptRequest object if Accept was successful, false otherwise

    Check if acceptor is registered, check if given request exists and is still open.
    """
    if not isRegistered(acceptor_user) or request not in get_open_requests():
        return False
    request.is_completed = True
    request.acceptor_email = acceptor_user
    request.time_accepted = time_accepted
    return request


def isRegistered(email):
    """Returns True iff user with <email> is registered"""
    try:
        Profile.objects(email=email).get()
        return True
    except DoesNotExist:
        return False


def get_request_by_email(email):
    """ Get the Request object associated with the given email

    :param email
    :return: the Request Object, or False if not found
    """
    try:
        request = Request.objects(email=email).get()
        return request
    except DoesNotExist:
        return False


def cancel_request_by_email(email):
    """ Cancel the Request object associated with the given email

    :param email
    :return: True if the cancel was successful, False otherwise
    """
    req = get_request_by_email(email)
    if not req:
        return False
    req.is_complete = True
    return True


def get_open_requests():
    """ Return a list of Requests that are not yet accepted

    :return: list of Requests
    """
    return list(Request.objects(is_complete=False))


def get_all_user_preferences():
    """ For all users with preferences set, return them

    :return: a list of UserSettings object
    """
    # How to check if preferences are set?
    return list(UserSettings.objects())
    # we will use these for the people who are offering support
