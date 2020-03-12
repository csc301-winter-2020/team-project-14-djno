from datetime import datetime
from mongoengine import *
from config import *
import json


class UserSettings(Document):
    email = EmailField(unique=True, required=True)
    GPS = BooleanField(required=True)
    preferences = ListField(choices=p_rules, required=True)
    days = ListField(choices=days, required=True)
    time_of_day = ListField(choices=time_of_day, required=True)

    def json(self):
        settings_dict = {
            "email": self.email,
            "GPS": self.GPS,
            "preferences": self.preferences,
            "days": self.days,
            "time_of_day": self.time_of_day
        }
        return json.dump(settings_dict)


class User(Document):
    email = EmailField(unique=True, required=True)
    date_created = DateTimeField(default=datetime.utcnow)
    auth_code = StringField()

    def json(self):
        user_dict = {
            "email": self.email,
            "date_created": self.date_created,
            "Authentication code": self.auth_code
        }
        return json.dump(user_dict)

    meta = {
        "ordering": ["-date_created"]
    }


class Profile(Document):

    email = EmailField(unique=True, required=True)
    first_name = StringField(required=True, max_length=25)
    last_name = StringField(required=True, max_length=25)
    date_of_birth = DateField(required=True)
    age = IntField(required=True)
    gender = StringField(required=True)
    location = StringField(required=True, max_length=25)
    image_url = StringField()

    def json(self):
        profile_dict = {
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
            "age": self.age,
            "gender": self.gender,
            "location": self.location,
            "image_url": self.image_url
        }
        return json.dump(profile_dict)
