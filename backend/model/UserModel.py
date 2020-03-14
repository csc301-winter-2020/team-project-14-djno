from datetime import datetime

from mongoengine import *

from config import *

# todo: add default values and data length restrictions

# should we not have a disabilityType class?

# Suggest preferences not be hardcoded in the user. They be made part of RequestModel,
# so that they may be dynamically used

# class Preferences(EmbeddedDocument):
#     education_navigation = BooleanField()
#     education_support = BooleanField()
#     employment_navigation = BooleanField()
#     employment_support = BooleanField()
#     health_care_navigation = BooleanField()
#     health_care_support = BooleanField()
#     local_navigation = BooleanField()
#     local_support = BooleanField()
#     well_being_leisure = BooleanField()
#     pick_up_and_delivery = BooleanField()
#     pick_up_and_drop_off = BooleanField()
#     homemaking_supports = BooleanField()
# suggest that preferences be embedded in Profile, and not in UserSettings, because
# preferences are not related to location. They are more related to profile

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
    education_navigation = ListField(choices=p_rules)
    education_support = ListField(choices=p_rules)
    employment_navigation = ListField(choices=p_rules)
    employment_support = ListField(choices=p_rules)
    health_care_navigation = ListField(choices=p_rules)
    health_care_support = ListField(choices=p_rules)
    local_navigation = ListField(choices=p_rules)
    local_support = ListField(choices=p_rules)
    well_being_leisure = ListField(choices=p_rules)
    pick_up_and_delivery = ListField(choices=p_rules)
    pick_up_and_drop_off = ListField(choices=p_rules)
    homemaking_supports = ListField(choices=p_rules)
    # Calendar/Availability
    # preferences = EmbeddedDocumentField(Preferences)  # References Preferences


# suggest the user authorization code received from google also be stored in the User object,
# just in case user disputes information in future, and we may need the authorization code
# to take up the matter with google. Although this aspect is not part of our app at this point
# but it may be good idea to store this information.

# If google login is used, no need to store password, since google will itself manage login authentication


# suggest email be changed to gmail

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
    image_url = StringField()
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
            "image_url": self.image_url
        }
