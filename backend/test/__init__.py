from backend.model.UserModel import *
from backend.model.RequestModel import *
from datetime import datetime

"""
Run this to generate tables in the database
"""

# creating an account for user_0
user_0 = User(
    user_id=0,
    username="William_000",
    password="William_000",
    email="William000@uoft.ca"
).save()

# creating profile for user_0
dob = datetime(year=2000, month=1, day=1)
user_0_profile = Profile(
    first_name="William",
    last_name="000",
    date_of_birth=dob,
    gender="male"
).save()
user_0.profile = user_0_profile  # set the profile for user_0
user_0.save()  # save

# create preferences for user_0
user_0_preferences = Preferences(
    education_navigation=False,
    education_support=False,
    employment_navigation=False,
    employment_support=False,
    health_care_navigation=False,
    health_care_support=False,
    local_navigation=False,
    local_support=False,
    well_being_leisure=False,
    pick_up_and_delivery=False,
    pick_up_and_drop_off=False,
    homemaking_supports=False
)

# create settings user_0
user_0_settings = UserSettings(
    location_sharing_on=False,
    preferences=user_0_preferences
).save()
user_0.profile.settings = user_0_settings
user_0.save()  # save

# let user_0 create a request
request_0 = Request(
    request_id=0,
    requester_user=user_0,
    request_location=user_0_settings.location,
    request_time=datetime.utcnow,
    preferences=user_0_settings.preferences,
    description="Looking for someone to play chess with"
).save()



