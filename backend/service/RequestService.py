from model.RequestModel import *
from mongoengine import errors

from model.UserModel import Profile, UserSettings

"""
This file include Any calls used to create, delete, modify, and view information about Requests.
"""


def create_request(requester_email, request_type, name, description, request_time=datetime.utcnow):
    """Create a new request

    @:param requester_email, request_type, description, request_time
    @:return Request object if successful creation, None otherwise

    Check if requester is registered, check if preferences is not set, generate request_id with REQUEST_NUMBER variable
    from config
    """
    if not is_registered(requester_email):
        return False

    try:
        new_request = Request(
            requester_email=requester_email,
            request_type=request_type,
            name=name,
            description=description,
            time_created=request_time
        ).save()
        return new_request
    except errors.__all__:
        return False


def accept_request(acceptor_user, request, time_accepted=datetime.utcnow):
    """ Accept an open request

    @:param acceptor_user, request, time_accepted
    :return: AcceptRequest object if Accept was successful, false otherwise

    Check if acceptor is registered, check if given request exists and is still open.
    """
    if not is_registered(acceptor_user) or request not in get_open_requests():
        return False
    request.is_completed = True
    request.acceptor_email = acceptor_user
    request.time_accepted = time_accepted
    return request


def is_registered(email):
    """Returns True iff user with <email> is registered"""
    try:
        Profile.objects(email=email).get()
        return True
    except errors.__all__:
        return False


def get_request_by_email(email):
    """ Get the Request object associated with the given email

    :param email
    :return: the Request Object, or False if not found
    """
    try:
        request = Request.objects(requester_email=email).get()   #request = Request.objects(email=email).get()
        return request
    except errors.__all__:
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
    return list(Request.objects(is_completed=False))  #return list(Request.objects(is_complete=False))


def get_all_user_preferences():
    """ For all users with preferences set, return them

    :return: a list of UserSettings object
    """
    # How to check if preferences are set?
    return list(UserSettings.objects())
    # we will use these for the people who are offering support


def complete_request(requester_email, acceptor_email):
    """ Set a given request to be completed by the acceptor email

    :param requester_email:
    :param acceptor_email:
    :return: True is successful, false otherwise
    """
    try:
        request = list(Request.objects(is_completed=False, requester_email=requester_email))[0]  #request = list(Request.objects(is_complete=False, requester_email=requester_email))[0]
        request.acceptor_email = acceptor_email
        request.save()

        return True

    except errors.__all__:
        return False


