from datetime import datetime
from model.RequestModel import *
from mongoengine import errors
from model.UserModel import Profile, Settings

"""
This file include Any calls used to create, delete, modify, and view information about Requests.
"""


def create_request(email, name, location, time, rtype, description):
    """Creates a new request

    @:param email, name, location, time, rtype, description
    @:return Request object upon successful creation, None otherwise
    """
    if not isRegistered(email):
        return False
    try:
        new_request = Request(
            requestor_email=email,
            title=name,
            point=location,
            time_of_request=time
            request_type=rtype,
            description=description,
        ).save()
        return new_request
    except:
        return False


def accept_request(acceptor_user, request, time_accepted=datetime.utcnow):
    """ Accept an open request

    @:param acceptor_user, request, time_accepted
    @:return: AcceptRequest object if Accept was successful, false otherwise
    """
    if not isRegistered(acceptor_user) or request not in get_open_requests():
        return False
    request.update(
        acceptor_email=acceptor_user,
        time_accepted=time_accepted,
        status="PENDING"
    )
    request.reload()
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
        request = Request.objects(requestor_email=email).get()
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
    req.update(
        is_completed=True,
        status="CANCELLED"
    )
    return True


def get_open_requests():
    """ Return a list of Requests that are not yet accepted

    :return: list of Requests
    """
    return list(Request.objects(is_completed=False))


def get_all_user_preferences():
    """ For all users with preferences set, return them

    :return: a list of UserSettings object
    """
    return list(Settings.objects())
