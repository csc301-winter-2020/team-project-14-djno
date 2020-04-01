from mongoengine import *
from datetime import datetime
from config import d_rules, REQUEST_STATUS
# import json


class Request(Document):
    requestor_email = EmailField(required=True)
    acceptor_email = EmailField()
    title = StringField(required=True, max_length=25)
    point = PointField(required=True)  # location
    time_of_request = DateTimeField(required=True)
    request_type = StringField(required=True, choices=d_rules)
    description = StringField(required=True, max_length=280)
    time_created = DateTimeField(required=True, default=datetime.utcnow)
    time_accepted = DateTimeField()
    is_completed = BooleanField(
        default=False, required=True)
    # status = StringField(
    #     required=True, choices=REQUEST_STATUS, default="POSTED")

    def __str__(self):
        return self.to_json()

    def __repr__(self):
        return f"<Request: {self.email}>"
