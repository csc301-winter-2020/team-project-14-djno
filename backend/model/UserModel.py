from mongoengine import *
from datetime import datetime

# todo: add default values and data length restrictions

# should we not have a disabilityType class?

# Suggest preferences not be hardcoded in the user. They be made part of RequestModel, 
# so that they may be dynamically used

class Preferences(EmbeddedDocument):
    education_navigation = BooleanField()
    education_support = BooleanField()
    employment_navigation = BooleanField()
    employment_support = BooleanField()
    health_care_navigation = BooleanField()
    health_care_support = BooleanField()
    local_navigation = BooleanField()
    local_support = BooleanField()
    well_being_leisure = BooleanField()
    pick_up_and_delivery = BooleanField()
    pick_up_and_drop_off = BooleanField()
    homemaking_supports = BooleanField()
    user_id = StringField(unique=True, required=True)
# suggest that preferences be embedded in Profile, and not in UserSettings, because 
# preferences are not related to location. They are more related to profile

class UserSettings(EmbeddedDocument):
    location_sharing_on = BooleanField(default=False)
    location = PointField()
    # Calendar/Availability
    preferences = EmbeddedDocumentField(Preferences)  # References Preferences
    user_id = StringField(unique=True, required=True)

# suggest the user authorization code received from google also be stored in the User object,
# just in case user disputes information in future, and we may need the authorization code
# to take up the matter with google. Although this aspect is not part of our app at this point
# but it may be good idea to store this information.

# If google login is used, no need to store password, since google will itself manage login authentication

# No need for a separate user_id, as the gmail account is our user id. 

# suggest email be changed to gmail

class User(Document):
    # username = StringField(unique=True, required=True)
    user_id = IntField(unique=True, required=True)
    email = EmailField(unique=True, required=True)
    third_party_login = BooleanField(required=True, default=True)
    date_created = DateTimeField(default=datetime.utcnow)

    meta = {
        "indexes": ["user_id"],
        "ordering": ["-date_created"]
    }

class Profile(Document):
    user_id = IntField(required=True, unique=True)  # todo: reference to User.user_id
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    date_of_birth = DateTimeField(required=True)
    gender = StringField(required=True)
    settings = EmbeddedDocumentField(UserSettings)

    meta = {
        "indexes": ["user_id"],
    }