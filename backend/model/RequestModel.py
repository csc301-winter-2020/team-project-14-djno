from mongoengine import *
from datetime import datetime
from backend.config import *
from backend.model.UserModel import User
from backend.model.UserModel import Preferences

# todo: add default values and data length restrictions


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
