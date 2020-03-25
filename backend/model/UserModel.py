from datetime import datetime

from mongoengine import *

from config import *

# todo: add default values and data length restrictions


""" 
Updated UserSettings collection

class UserSettings(Document):
    email = EmailField(unique=True, required=True)
    GPS = BooleanField(required=True)
    preferences = ListField(choices=p_rules, required=True)
    days = ListField(choices=days, required=True)
    time_of_day = ListField(choices=time_to_str, required=True)

    def json(self):
        user_dict = {
            "email" : self.email,
            "GPS" : self.GPS,
            "preferences" : self.preferences,
            "days" : self.days,
            "time_of_day" : self.time_of_day
        }
        return json.dump(user_dict)
"""


class UserSettings(Document):
    email = EmailField(unique=True, required=True)
    location = PointField()  # todo: make this required
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
    request_type = StringField()


class User(Document):
    # username = StringField(unique=True, required=True)
    email = EmailField(unique=True, required=True)
    date_created = DateTimeField(default=datetime.utcnow)
    meta = {
        "ordering": ["-date_created"]
    }


class Profile(Document):
    email = EmailField(unique=True, required=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    date_of_birth = DateField(required=True)
    age = IntField(required=False)
    gender = StringField(required=True)
    image_url = StringField(
        required=True)  # Google auth login will always provide one.
    description = StringField(required=True, max_length=250)

    def json(self):
        return self.turn_to_dict()

    def turn_to_dict(self):
        return {
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
            "gender": self.gender,
            "image_url": self.image_url,
            "description": self.description
        }


class UserOtherSettings(Document):
    email = EmailField(unique=True, required=True)
    location = PointField()  # todo: make this required
    location_enabled = BooleanField(default=True)
    monday = BooleanField(default=False)
    tuesday = BooleanField(default=False)
    wednesday = BooleanField(default=False)
    thursday = BooleanField(default=False)
    friday = BooleanField(default=False)
    saturday = BooleanField(default=False)
    sunday = BooleanField(default=False)
    morning = BooleanField(default=False)
    afternoon = BooleanField(default=False)
    evening = BooleanField(default=False)
    OPC = BooleanField(default=False)
    OQC = BooleanField(default=False)
    OQE = BooleanField(default=False)
