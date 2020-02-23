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

class Profile(EmbeddedDocument):
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    date_of_birth = DateTimeField(required=True)
    gender = StringField(required=True)
    settings = EmbeddedDocumentField(UserSettings)
    user_id = StringField(unique=True, required=True)

# suggest the user authorization code received from google also be stored in the User object,
# just in case user disputes information in future, and we may need the authorization code
# to take up the matter with google. Although this aspect is not part of our app at this point
# but it may be good idea to store this information.

# If google login is used, no need to store password, since google will itself manage login authentication

# No need for a separate user_id, as the gmail account is our user id. 

# suggest email be changed to gmail

class User(Document):
    user_id = StringField(unique=True, required=True)
    password = StringField(required=True)  # todo, min length or store a hash
    email = EmailField(required=True)
    date_created = DateField(default=datetime.utcnow)

    meta = {
        "indexes": ["user_id"],
        "ordering": ["-date_created"]
    }
