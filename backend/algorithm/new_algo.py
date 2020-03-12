from config import *
from UserModel import *


candidates = User.objects()


def get_matches(data):
    """
    Returns a list of candidate objects.

    data: JSON data of the form
        {
        "requestor_email" : <requestor's email>,
        "title" : <name of request>,
        "location" : (latitude, longitude),
        "datetime" : YYYY-MM-DD, HH:SS AM/PM,
        "category" : <codename of category>,
        "description" : <description of request>
    }
    """
    return candidates
