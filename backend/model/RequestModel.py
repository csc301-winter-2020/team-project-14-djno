from mongoengine import *
from datetime import datetime
from backend.config import *
from backend.model.UserModel import *

res = connect(DATABASE_NAME, host=HOST_IP, port=PORT, username=USERNAME, password=PASSWORD,
              authentication_source=AUTHENTICATION_SOURCE)

# todo: add default values and data length restrictions


class Request(Document):
    request_id = IntField(unique=True, required=True)
    requester_user_id = IntField(required=True)
    request_location = PointField()
    request_time = DateField()
    preferences = EmbeddedDocumentField(Preferences, required=True)
    description = StringField(required=True)  # add limit
    time_created = DateField(default=datetime.utcnow)
    is_complete = BooleanField(default=False)  # set to True when another user accept the request or is cancelled
    acceptor_user_id = IntField()  # the user who accepts this request
