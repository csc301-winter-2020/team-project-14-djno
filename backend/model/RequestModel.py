from mongoengine import *
from datetime import datetime
from config import *


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
    request_type = ListField(required=True)  # ["OPC", "OQC", "OQE"]
    name = StringField(required=True, max_length=NAME_MAX_LENGTH)
    description = StringField(required=True, max_length=DESCRIPTION_MAX_LENGTH)
    time_created = DateTimeField(required=True, default=datetime.utcnow)
    time_accepted = DateTimeField()
    is_completed = BooleanField(default=False)
    acceptor_email = EmailField()
