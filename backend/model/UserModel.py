from datetime import datetime
from mongoengine import *
from config import days, time_of_day, p_rules
# import json


class Settings(Document):
    email = EmailField(unique=True, required=True)
    location_enabled = BooleanField(required=True)
    preferences = ListField(choices=p_rules, max_length=3)
    days = ListField(choices=days, max_length=7)
    time_of_day = ListField(choices=time_of_day, max_length=4)

    def __str__(self):
        return self.to_json()

    def __repr__(self):
        return f"<Settings: {self.email}>"


class Profile(Document):
    email = EmailField(unique=True, required=True)
    first_name = StringField(required=True, max_length=25)
    last_name = StringField(required=True, max_length=25)
    date_of_birth = DateField(required=True)
    age = IntField()
    gender = StringField(required=True, choices=["Male", "Female", "Other"])
    location = StringField(required=True, max_length=25)  # City name
    description = StringField(required=True, max_length=250)
    image_url = StringField(required=True)
    # user = ReferenceField(User)

    def __str__(self):
        return self.to_json()

    def __repr__(self):
        return f"<Profile: {self.email}>"


class UserQuerySet(QuerySet):

    def filter_by_location(self, pt, max=5000, min=0):
        return self.filter(point__near={"type": "Point", "coordinates": pt},
                           point__max_distance=max, point__min_distance=min)


class User(Document):
    email = EmailField(unique=True, required=True)
    date_created = DateTimeField(default=datetime.utcnow)
    # auth_code = StringField()
    point = PointField()  # their coordinates [long,lat]
    settings = ReferenceField(Settings)
    profile = ReferenceField(Profile)

    def __str__(self):
        return self.to_json()

    def __repr__(self):
        return f"<User: {self.email}>"

    meta = {
        "ordering": ["-date_created"], "queryset_class": UserQuerySet
    }
