from datetime import datetime
from mongoengine import *
from config import days, time_of_day, p_rules
# import json


# class SettingsQuerySet(QuerySet):

#     def filter_by_pref(self, requested_pref):
#         # I know, DRY code but don't know of another way...
#         requested_pref = requested_pref.lower()
#         if requested_pref == "opc":
#             return self.filter(preferences__OPC=True)
#         if requested_pref == "oqc":
#             return self.filter(preferences__OQC=True)
#         if requested_pref == "oqe":
#             return self.filter(preferences__OQE=True)
#         else:
#             return False

#     def filter_by_gps(self, on):
#         return self.filter(GPS=on)

#     def filter_by_day(self, day):
#         # I know, DRY code but don't know of another way...
#         day = day.lower()
#         if day == "monday":
#             return self.filter(days__Monday=True)
#         if day == "tuesday":
#             return self.filter(days__Tuesday=True)
#         if day == "wednesday":
#             return self.filter(days__Wednesday=True)
#         if day == "thursday":
#             return self.filter(days__Thursday=True)
#         if day == "friday":
#             return self.filter(days__Friday=True)
#         if day == "saturday":
#             return self.filter(days__Saturday=True)
#         if day == "sunday":
#             return self.filter(days__Sunday=True)
#         else:
#             return False

#     def filter_by_time(self, time):
#         # I know, DRY code but don't know of another way...
#         time = time.lower()
#         if time == "morning":
#             return self.filter(time_of_day__Morning=True)
#         if time == "afternoon":
#             return self.filter(time_of_day__Afternoon=True)
#         if time == "evening":
#             return self.filter(time_of_day__Evening=True)
#         if time == "night":
#             return self.filter(time_of_day__Night=True)


# class Preferences(EmbeddedDocument):
#     OPC = BooleanField(required=True)
#     OQC = BooleanField(required=True)
#     OQE = BooleanField(required=True)


# class DayAvailability(EmbeddedDocument):
#     Monday = BooleanField(required=True)
#     Tuesday = BooleanField(required=True)
#     Wednesday = BooleanField(required=True)
#     Thursday = BooleanField(required=True)
#     Friday = BooleanField(required=True)
#     Saturday = BooleanField(required=True)
#     Sunday = BooleanField(required=True)


# class TimeAvailability(EmbeddedDocument):
#     Morning = BooleanField(required=True)
#     Afternoon = BooleanField(required=True)
#     Evening = BooleanField(required=True)
#     Night = BooleanField(required=True)


class Settings(Document):
    email = EmailField(unique=True, required=True)
    location_enabled = BooleanField(required=True)
    preferences = ListField(choices=p_rules, max_length=3)
    days = ListField(choices=days, max_length=7)
    time_of_day = ListField(choices=time_of_day, max_length=4)
    # user = ReferenceField(User)
    #preferences = EmbeddedDocumentField(Preferences)
    # Should we use DictField instead?
    #days = EmbeddedDocumentField(DayAvailability)
    # Should we use DictField instead?
    #time_of_day = EmbeddedDocumentField(TimeAvailability)
    # monday = BooleanField(required=True)
    # tuesday = BooleanField(required=True)
    # wednesday = BooleanField(required=True)
    # thursday = BooleanField(required=True)
    # friday = BooleanField(required=True)
    # saturday = BooleanField(required=True)
    # sunday = BooleanField(required=True)
    # morning = BooleanField(required=True)
    # afternoon = BooleanField(required=True)
    # evening = BooleanField(required=True)
    # night = BooleanField(required=True)
    # OPC = BooleanField(required=True)
    # OQC = BooleanField(required=True)
    # OQE = BooleanField(required=True)

    # There is a built-in to_json method.
    # May not need this
    # def json(self):
    #     settings_dict = {
    #         "email": self.email,
    #         "GPS": self.GPS,
    #         "preferences": self.preferences,
    #         "days": self.days,
    #         "time_of_day": self.time_of_day
    #     }
    #     return json.dumps(settings_dict)

    def __str__(self):
        return self.to_json()

    def __repr__(self):
        return f"<Settings: {self.email}>"

    #meta = {'queryset_class': SettingsQuerySet, 'indexes': ['email']}


class Profile(Document):

    email = EmailField(unique=True, required=True)
    first_name = StringField(required=True, max_length=25)
    last_name = StringField(required=True, max_length=25)
    date_of_birth = DateField(required=True)
    age = IntField()
    gender = StringField(required=True, choices=["Male", "Female", "Other"])
    location = StringField(required=True, max_length=25)  # City name
    image_url = StringField()
    # user = ReferenceField(User)

    # There is a built-in to_json method.
    # May not need this
    # def json(self):
    #     profile_dict = {
    #         "email": self.email,
    #         "first_name": self.first_name,
    #         "last_name": self.last_name,
    #         "date_of_birth": self.date_of_birth,
    #         "age": self.age,
    #         "gender": self.gender,
    #         "location": self.location,
    #         "image_url": self.image_url
    #     }
    #     return json.dumps(profile_dict)

    def __str__(self):
        return self.to_json()

    def __repr__(self):
        return f"<Profile: {self.email}>"

    # meta = {"ordering": ["-age", "-date_of_birth"], "indexes": ["email"]}


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

    # There is a built-in to_json method.
    # May not need this
    # def json(self):
    #     user_dict = {
    #         "email": self.email,
    #         "date_created": self.date_created,
    #         "Authentication code": self.auth_code,
    #         "current location": self.point
    #     }
    #     return json.dumps(user_dict)

    def __str__(self):
        return self.to_json()

    def __repr__(self):
        return f"<User: {self.email}>"

    meta = {
        "ordering": ["-date_created"], "queryset_class": UserQuerySet
    }
