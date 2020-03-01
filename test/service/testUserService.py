from datetime import datetime

from backend.config import *
from mongoengine import *

from backend.service import UserService

if __name__ == "__main__":
    res = connect(DATABASE_NAME, host=HOST_IP, port=PORT, username=USERNAME, password=PASSWORD,
                  authentication_source=AUTHENTICATION_SOURCE)
    print("The server is launching....")
    # Session(app)
    # app.run(host="0.0.0.0", port=os.environ.get('PORT', 8080))

    u0_id = 000  # retrieved from google authentication
    u0_email = "aaabbb@gmail.com"
    
    u0_first_name = 'aaa'
    u0_last_name = 'bbb'
    u0_dob = datetime(year=2000, month=1, day=1)
    u0_gender = 'male'
    
    # create user_0
    user0 = UserService.create_user_with_gmail(u0_email, u0_id)

    # create profile for user_0
    user0_profile = UserService.create_profile(u0_id, u0_first_name, u0_last_name, u0_dob, u0_gender)
