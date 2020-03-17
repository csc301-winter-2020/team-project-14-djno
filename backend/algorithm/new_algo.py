from datetime import datetime
# from mongoengine import *
from config import *
from backend.model.UserModel import *

""" A filtering system 

Example usage:

Say requester seeks helpers who are available on a Saturday afternoon for phone call
qSet1 = Settings.objects.filter_by_pref("OPC")
qSet2 = Settings.objects.filter_by_day("Saturday")
qSet3 = Settings.objects.filter_by_time("Afternoon")
qSet4 = User.objects.filter_by_location([1,1])

Now find users who satisfy all criteria
Step 1: For each qSet, get list of emails
Step 2: Convert each list into a set
Step 3: Find intersection of all sets

Then get corresp profile object
"""


def get_matches(data):
    """
    Returns a list of profile objects.

    data: JSON data of the form
        {
        "requestor_email" : <requestor's email>,
        "title" : <name of request>,
        "location" : [latitude, longitude],
        "datetime" : <datetime object>,
        "category" : <codename of category>,
        "description" : <description of request>
    }

    Output: [Profile], False otherwise
    """
    corresp_pref = service_to_pref[data["category"]]
    day = data["datetime"].strftime('%A')
    time = data["datetime"].time
    time_of_day = get_time_of_day(time.hour)

    if not time_of_day:
        return False
    if day not in days:
        return False

    qSet1 = Settings.objects.filter_by_pref(corresp_pref)
    qSet2 = Settings.objects.filter_by_time(time_of_day)
    qSet3 = Settings.objects.filter_by_day(day)
    qSet4 = User.objects.filter_by_location(data["location"])

    # TODO


def get_time_of_day(hour) -> str:
    if 0 <= hour <= 5:
        return "Night"
    if 6 <= hour <= 11:
        return "Morning"
    if 12 <= hour <= 17:
        return "Afternoon"
    if 18 <= hour <= 23:
        return "Evening"
    else:
        return False


if __name__ == "__main__":
    connect("david", HOST_IP, PORT,
            AUTHENTICATION_SOURCE, USERNAME, PASSWORD)
