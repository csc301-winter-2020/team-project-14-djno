from mongoengine import *
from datetime import datetime
from backend.config import *

res = connect(DATABASE_NAME, host=HOST_IP, port=PORT, username=USERNAME, password=PASSWORD,
              authentication_source=AUTHENTICATION_SOURCE)
#print(res)

# todo: add default values and data length restrictions


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


class UserSettings(Document):
    location_sharing_on = BooleanField(default=False)
    location = PointField()
    preferences = EmbeddedDocumentField(Preferences)  # References Preferences


class Profile(Document):
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    date_of_birth = DateTimeField(required=True)
    gender = StringField(required=True)
    settings = ReferenceField(UserSettings)  # References Settings


class User(Document):
    username = StringField(unique=True, required=True)
    password = StringField(required=True)  # todo, min length or store a hash
    email = EmailField(required=True)
    registered = BooleanField(default=False)  # *** set the to true when created profile
    profile = ReferenceField(Profile, default=None)  # References Profile
    date_created = DateField(default=datetime.utcnow)

    meta = {
        "indexes": ["user_id"],
        "ordering": ["-date_created"]
    }
