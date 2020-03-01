import unittest
from datetime import datetime
from backend.config import *
from mongoengine import *
from backend.service import UserService
from backend.model import UserModel
from backend.service import RequestService
from backend.model import RequestModel


class TestUserService(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        res = connect(DATABASE_NAME, host=HOST_IP, port=PORT, username=USERNAME, password=PASSWORD,
                      authentication_source=AUTHENTICATION_SOURCE)
        print("The server is launching....")

    def setUp(self) -> None:
        # add some users with profile and preferences here
        pass

    def create_request(self):
        # for now create the request_id manually here
        pass

    def create_request_2(self):
        # for now create the request_id manually here
        pass

    def create_request_3(self):
        # for now create the request_id manually here
        pass

    def complete_request(self):
        # for now create the request_id manually here
        pass
    
    # todo: add any further tests you feel appropriate

    @classmethod
    def tearDownClass(cls):
        UserModel.User.drop_collection()
        UserModel.Profile.drop_collection()
        RequestModel.Request.drop_collection()

if __name__ == "__main__":
    unittest.main()