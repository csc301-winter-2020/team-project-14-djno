from datetime import datetime
from mongoengine import *
from config import *
from model.UserModel import User, Settings
from service.UserService import get_user_profile_by_email

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
    rs = []

    if not isinstance(data["datetime"], datetime) or data["category"] not in d_rules:
        return False

    corresp_pref = service_to_pref[data["category"]]
    day = data["datetime"].strftime('%A')
    time = data["datetime"].time
    time_of_day = get_time_of_day(time.hour)

    if not time_of_day or day not in days or corresp_pref not in p_rules:
        return False

    # Perform filters
    qSet1 = Settings.objects.filter_by_pref(corresp_pref)
    qSet2 = Settings.objects.filter_by_time(time_of_day)
    qSet3 = Settings.objects.filter_by_day(day)
    qSet4 = User.objects.filter_by_location(data["location"])

    # For each qSet, project out emails
    set1 = set([s1.email for s1 in qSet1])
    set2 = set([s2.email for s2 in qSet2])
    set3 = set([s3.email for s3 in qSet3])
    set4 = set([s4.email for s4 in qSet4])

    # Join above sets i.e. compute the intersection
    final_set = set1.intersection(set2).intersection(set3).intersection(set4)

    # Now get the corresponding profile objects
    rs = [get_user_profile_by_email(e) for e in final_set]

    return rs


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
    connect("david", host=HOST_IP, port=PORT,
            authentication_source=AUTHENTICATION_SOURCE, username=USERNAME, password=PASSWORD)
    print("connected")
