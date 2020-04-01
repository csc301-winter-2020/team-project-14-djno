from datetime import datetime
from mongoengine import *
from config import *
from model.UserModel import User, Settings


def get_matches(data, max_dist=5000, n=10) -> list:
    """
    data: JSON data of the form
        {
        "requestor_email" : <requestor's email>,
        "title" : <name of request>,
        "location" : [latitude, longitude],
        "datetime" : <datetime obj / %Y-%m-%dT%H:%M>,
        "category" : <codename of category>,
        "description" : <description of request>
    }
    max_dist: the maximum distance in kilometres
    n: the maximum number of candidates returned
    """
    # Improved querying with respect to the updated models
    if isinstance(data["datetime"], datetime):
        dt = data["datetime"]
    else:
        dt = datetime.strptime(data["datetime"], "%Y-%m-%dT%H:%M")

    corresp_pref = service_to_pref[data["category"]]
    day = dt.strftime('%A')
    time = get_time_of_day(dt.time().hour)
    loc = data["location"]

    # print(corresp_pref, day, time, loc)

    good_settings = list(Settings.objects(
        Q(preferences=corresp_pref) & Q(days=day) & Q(time_of_day=time)))
    # print("Good settings: ", good_settings)

    qSet = User.objects.filter_by_location(loc, max_dist)
    # print("Localized: ", qSet)

    candidates = qSet.filter(settings__in=good_settings)
    # print("Candidates: ", candidates)

    profiles = [candidate.profile for candidate in candidates]
    # print("Profiles: ", profiles)

    rs = list(profiles)[:n]
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
