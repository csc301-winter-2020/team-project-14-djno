from datetime import datetime
from model.RequestModel import Request
from mongoengine import *
from model.UserModel import User, Settings

"""
This file include Any calls used to create, delete, modify, and view information about Requests.
"""


def create_update_request(data):
    """ Creates/updates a request from JSON """
    new_request = Request.from_json(data).save()
    return new_request


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
            time_of_request=time,
            request_type=rtype,
            description=description,
        ).save()
        return new_request
    except Exception as e:
        print(e.with_traceback)
        return None


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
        User.objects(email=email).get()
        return True
    except DoesNotExist:
        return False


def get_requests_by_email(email):
    """ Get the Request objects associated with the given email

    :param email
    :return: the Request Objects querySet, or False if not found
    """
    try:
        requests = Request.objects(requestor_email=email)
        return requests
    except DoesNotExist:
        return False


# def cancel_request_by_email(email):
#     """ Cancel the Request object associated with the given email

#     :param email
#     :return: True if the cancel was successful, False otherwise
#     """
#     req = get_request_by_email(email)
#     if not req:
#         return False
#     req.update(
#         is_completed=True,
#         status="CANCELLED"
#     )
#     return True


def get_open_requests():
    """ Return a list of Requests that are not yet accepted

    :return: list of Requests
    """
    return list(Request.objects(status="POSTED"))


def get_all_user_preferences():
    """ For all users with preferences set, return them

    :return: a list of UserSettings object
    """
    return list(Settings.objects())
