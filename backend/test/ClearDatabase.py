from backend.model.UserModel import *
from backend.model.RequestModel import *

res = connect(DATABASE_NAME, host=HOST_IP, port=PORT, username=USERNAME,
              password=PASSWORD,
              authentication_source=AUTHENTICATION_SOURCE)
print("The server is launching....")

User.drop_collection()
Profile.drop_collection()
# UserSettings.drop_collection()
# Request.drop_collection()
# AcceptRequest.drop_collection()
