from mongoengine import *
from datetime import datetime
from config import *
import json


class Request(Document):

    requestor_email = EmailField(unique=True, required=True)
    acceptor_email = EmailField(unique=True)
    title = StringField(required=True, max_length=25)
    location = PointField(required=True)
    time_of_request = DateTimeField(required=True)
    # Must be one of REN, RES, RENA, etc.
    request_type = StringField(required=True)
    description = StringField(required=True, max_length=280)
    time_created = DateTimeField(required=True, default=datetime.utcnow)
    time_accepted = DateTimeField()
    is_completed = BooleanField(default=False)

    def json(self):
        req_dict = {
            "requestor_email": self.requestor_email,
            "acceptor_email": self.acceptor_email,
            "title": self.title,
            "location": self.location,
            "datetime": self.time_of_request,
            "category": self.request_type,
            "description": self.description,
            "time_created": self.time_created,
            "time_accepted": self.time_accepted,
            "is_completed": self.is_completed
        }
        return json.dump(req_dict)
