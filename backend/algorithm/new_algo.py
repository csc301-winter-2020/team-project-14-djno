from config import *
from UserModel import *

""" A filtering system """

candidates = Profile.objects()


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
    coresp_pref = service_to_pref[data["category"]]
    UserSettings.objects(preferences=coresp_pref)
    return candidates


""" Pseudocode for Step 2

"""

""" Step 3

For time HH:MM AM/PM, get the HH part and check

    Convert given time to military time

"""
