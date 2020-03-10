from mongoengine import *
from datetime import datetime
from config import *
from model.UserModel import User

# # todo: add default values and data length restrictions


# # It is suggested that the Preferences object be moved to the Request Model, because
# # requests will be based on Preferences.

# class RequestServices(EmbeddedDocument):
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

""" UPDATED REQUEST COLLECTION. 

class Request(Document):
    requestor_email = EmailField(unique=True,required=True)
    acceptor_email = EmailField(unique=True)
    title = StringField(required=True, max_length=25)
    description = StringField(required=True, max_length=280)
    gender = StringField(required=True)
    age = IntField(required=True)
    request_type = StringField(required=True) # Must be one of REN, RES, RENA, etc.
    time_of_request = DateTimeField(required=True)
    time_created = DateTimeField(required=True, default=datetime.utcnow)
    time_accepted = DateTimeField()
    is_completed = BooleanField(default=False)
    location = PointField(required=True)

    def json(self):
        req_dict = {
            requestor_email : self.requestor_email,
            acceptor_email : self.acceptor_email,
            title : self.title,
            time_of_request : self.time_of_request,
            gender : self.gender,
            age : self.age,
            request_type : self.request_type,
            description : self.description,
            time_created : self.time_created,
            time_accepted : self.time_accepted,
            is_completed : self.is_completed
        }
        return json.dump(req_dict)

"""


class Request(Document):
    requester_email = EmailField(unique=True, required=True)
    # requestor = ReferenceField(
    #     User, required=True, reverse_delete_rule=CASCADE)
    request_type = ListField(required=True)  # ["OPC", "OQC", "OQE"]
    # gender = StringField(required=True)
    # age = IntField(required=True)
    name = StringField(required=True, max_length=25)
    description = StringField(required=True, max_length=280)
    # request_location = PointField(required=True)
    time_created = DateTimeField(required=True, default=datetime.utcnow)
    time_accepted = DateTimeField()
    # expiry_request = DateField(required=True, default=datetime.utcnow)
    is_completed = BooleanField(default=False)
    # acceptor = ReferenceField(User)
    acceptor_email = EmailField()


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
