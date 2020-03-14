from datetime import datetime
# from mongoengine import *
from config import *
from backend.model.UserModel import *

""" A filtering system """

# candidates = Profile.objects


def get_matches(data):
    """
    Returns a list of profile objects.

    data: JSON data of the form
        {
        "requestor_email" : <requestor's email>,
        "title" : <name of request>,
        "location" : (latitude, longitude),
        "datetime" : <datetime object>,
        "category" : <codename of category>,
        "description" : <description of request>
    }

    Output: [Profile]
    """
    corresp_pref = service_to_pref[data["category"]]
    day = data["datetime"].strftime('%A')
    time = data["datetime"].time
    time_of_day = get_time_of_day(time.hour)

    qSet1 = UserSettings.objects.get_matched_pref(corresp_pref)
    qSet2 = UserSettings.objects.get_matched_time(day, time_of_day)
    qSet3 = UserSettings.objects.get_gps(False)
    qSet4 = User.objects.get_nearby(data["location"])

    # Now I want to join qSets with Profile by "email". Use Aggregate function
    # with '$lookup'

    pipeline = []


def get_time_of_day(hour):
    if 0 <= hour <= 5:
        return "Night"
    if 6 <= hour <= 11:
        return "Morning"
    if 12 <= hour <= 17:
        return "Afternoon"
    if 18 <= hour <= 23:
        return "Evening"
    else:
        return "hour is invalid"


if __name__ == "__main__":
    connect(DATABASE_NAME, HOST_IP, PORT,
            AUTHENTICATION_SOURCE, USERNAME, PASSWORD)
