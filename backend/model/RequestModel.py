from mongoengine import *
from datetime import datetime
from backend.config import *
from backend.model.UserModel import User
from backend.model.UserModel import Preferences

# # todo: add default values and data length restrictions


# # It is suggested that the Preferences object be moved to the Request Model, because
# # requests will be based on Preferences.

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

# only those requests to qualify for matching which 1) are not expired 2) are not complete
# 3) do not have an acceptor.

# to facilitate matching, both assistance_required and assistance_offerred fields are kept

# function required to extend expiry
# funtion required to delete acceptance. Both, requester and accepto to have delete option
# no need to have an offer extending & accepting mechanism. I acceptor is not agreeable, 
# requestor may simply cancel acceptance.

class Request(Document):
    email = EmailField(unique=True, required=True)
    # requestor = ReferenceField(
    #     User, required=True, reverse_delete_rule=CASCADE)
    request_type = ListField(required=True)  #["OPC", "OQC", "OQE"]
    # gender = StringField(required=True)
    # age = IntField(required=True)
    #assistance_required = EmbeddedDocumentField(Preferences, required=True)
    #assistance_offerred = EmbeddedDocumentField(Preferences, required=True)
    description = StringField(required=True, max_length=280)
    # request_location = PointField(required=True)
    time_created = DateTimeField(required=True, default=datetime.utcnow)
    # expiry_request = DateField(required=True, default=datetime.utcnow)
    is_completed = BooleanField(required=True, default=False)
    # acceptor = ReferenceField(User)
    acceptor_id = IntField(required=True)
'''

class Request(Document):
    request_id = IntField(unique=True, required=True)
    requestor = ReferenceField(
        User, required=True, reverse_delete_rule=CASCADE)
    request_location = PointField(required=True)
    # may be a date in the future
    request_time = DateField(default=datetime.utcnow, required=True)
    gender = StringField(required=True)
    age = IntField(required=True)
    preferences = EmbeddedDocumentField(Preferences, required=True)
    description = StringField(required=True)  # todo add limit
    time_created = DateField(required=True, default=datetime.utcnow)
    # set to True when another user accept the request or is cancelled
    is_completed = BooleanField(required=True, default=False)
    acceptor = ReferenceField(User)

    meta = {
        "indexes": ["request_id"],
        "ordering": ["-is_complete", "request_id"]
    }


# class AcceptRequest(Document):
#     # Note some requests may never be accepted
#     request_id = IntField(unique=True, required=True)
#     acceptor_user = ReferenceField(User, required=True)
#     time_accepted = DateField(required=True, default=datetime.utcnow)
#     userId = StringField(required=True)

'''