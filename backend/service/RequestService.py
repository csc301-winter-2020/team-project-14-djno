from datetime import datetime
from model.RequestModel import *
from mongoengine import errors

from model.UserModel import Profile, UserSettings

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
        is_completed=True
    )
    request.reload()
    return request


def isRegistered(email):
    """Returns True iff user with <email> is registered"""
    try:
        Profile.objects(email=email).get()
        return True
    except errors.__all__:
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
    return list(Request.objects(is_completed=False))


def get_all_user_preferences():
    """ For all users with preferences set, return them
    :return: a list of UserSettings object
    """
    return list(Settings.objects())


def complete_request(requester_email, acceptor_email):
    """ Set a given request to be completed by the acceptor email
    :param requester_email:
    :param acceptor_email:
    :return: True is successful, false otherwise
    """
    try:
        request = list(Request.objects(is_complete=False,
                                       requester_email=requester_email))[0]
        request.acceptor_email = acceptor_email
        request.save()

        return True

    except errors.__all__:
        return False
