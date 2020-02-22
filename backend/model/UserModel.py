from mongoengine import *
from datetime import datetime

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


class UserSettings(EmbeddedDocument):
    location_sharing_on = BooleanField(default=False)
    location = PointField()
    # Calendar/Availability
    preferences = EmbeddedDocumentField(Preferences)  # References Preferences


class Profile(EmbeddedDocument):
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    date_of_birth = DateTimeField(required=True)
    gender = StringField(required=True)
    settings = EmbeddedDocumentField(UserSettings)


class User(Document):
    user_id = StringField(unique=True, required=True)
    password = StringField(required=True)  # todo, min length or store a hash
    email = EmailField(required=True)
    date_created = DateField(default=datetime.utcnow)
    profile = EmbeddedDocumentField(Profile)

    meta = {
        "indexes": ["user_id"],
        "ordering": ["-date_created"]
    }
