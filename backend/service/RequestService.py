from datetime import datetime
from backend.model.RequestModel import *
from mongoengine import errors


"""
This file include Any calls used to create, delete, modify, and view information about Requests.
"""


def create_request(requester_user, assistance_required, assistance_offerred, description, request_location=None, request_time=datetime.utcnow):
    """Create a new request

    @:param requester_user, preferences, description, request_location, request_time
    @:return Request object if successful creation, false otherwise

    Check if requester is registered, check if preferences is not set, generate request_id with REQUEST_NUMBER variable
    from config
    """
    try:
        new_request = Request(
            requestor=requester_user,
            assistance_required=assistance_required,
            assistance_offerred=assistance_offerred,
            description=description
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


def get_request_by_id(request_id):
    """ Get the Request object associated with the given request_id

    :param request_id
    :return: the Request Object, or False if not found
    """
    try:
        request = Request.objects(request_id=request_id).get()
        return request
    except DoesNotExist:
        return False


def cancel_request_by_id(request_id):
    """ Cancel the Request object associated with the given request_id

    :param request_id
    :return: True if the cancel was successful, False otherwise
    """
    req = get_request_by_id(request_id)
    if not req:
        return False
    req.is_complete = True
    return True


def get_open_requests():
    """ Return a list of Requests that are not yet accepted

    :return: list of Requests
    """
    return list(Request.objects(is_complete=False))
