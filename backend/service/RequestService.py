from datetime import datetime
from backend.model.RequestModel import *
from mongoengine import errors

from backend.model.UserModel import Profile, UserSettings

"""
This file include Any calls used to create, delete, modify, and view information about Requests.
"""


def create_request(requester_email, request_type, description, request_location=None, request_time=datetime.utcnow):
    """Create a new request

    @:param requester_email, request_type, description, request_location, request_time
    @:return Request object if successful creation, None otherwise

    Check if requester is registered, check if preferences is not set, generate request_id with REQUEST_NUMBER variable
    from config
    """
    try:
        new_request = Request(
            requester_email=requester_email,
            request_type=request_type,
            description=description,
            time_created=request_time
            # todo: add location
        ).save()
    except errors.__all__:
        return False


def accept_request(acceptor_user, request, time_accepted=datetime.utcnow):
    """ Accept an open request

    @:param acceptor_user, request, time_accepted
    :return: AcceptRequest object if Accept was successful, false otherwise

    Check if acceptor is registered, check if given request exists and is still open.
    """


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

    return list(UserSettings.objects())
    # we will use these for the people who are offering support
