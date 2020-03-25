from mongoengine import *
from datetime import datetime
from config import *

# # todo: add default values and data length restrictions


# only those requests to qualify for matching which 1) are not expired 2) are not complete
# 3) do not have an acceptor.


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
