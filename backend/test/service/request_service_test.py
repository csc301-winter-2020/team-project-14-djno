import unittest
from datetime import datetime
from config import *
from mongoengine import *
from service import UserService
from model import UserModel
from service import RequestService
from model import RequestModel


class TestUserService(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        res = connect('test', host=HOST_IP, port=PORT, username=USERNAME,
                      password=PASSWORD,
                      authentication_source=AUTHENTICATION_SOURCE)
        print("The server is launching....")

    def setUp(self) -> None:
        # add some users with profile and preferences here
        UserService.create_user_with_gmail("jane@gmail.com")
        UserService.create_user_with_gmail("mike@gmail.com")

        UserService.create_a_user(
            "jane@gmail.com", "Jane", "Austin", "1995-10-22", "Female")
        UserService.create_a_user(
            "mike@gmail.com", "Mike", "Penn", "2000-05-14", "Male")

        UserService.update_user_settings({
            "email": "jane@gmail.com",
            "education_navigation": ["OPC"],
            "health_care_support": ["OPC", "OQC", "OQE"],
            "well_being_leisure": ["OQC"]
        })
        UserService.update_user_settings({
            "email": "mike@gmail.com",
            "education_support": ["OPC", "OQC", "OQE"],
            "employment_support": ["OPC", "OQC"],
            "local_support": ["OPC", "OQC"],
            "pick_up_and_drop_off": ["OPC", "OQC", "OQE"],
            "homemaking_supports": ["OQC"]
        })

    def create_request(self):
        # for now create the request_id manually here
        desc = "I need to borrow a Macbook charger for 30 minutes"
        req = RequestService.create_request(
            "jane@gmail.com", ["OQE"], "Charger", desc)

        self.assertEqual(req.requester_email, "jane@gmail.com")
        self.assertEqual(req.request_type, ["OQE"])
        self.assertEqual(req.name, "Charger")
        self.assertEqual(req.description, desc)

        return req

    def create_request_2(self):
        # for now create the request_id manually here
        desc = "I need someone to talk to ASAP"
        req = RequestService.create_request(
            "mike@gmail.com", ["OPC", "OQC"], "Chat", desc)

        self.assertEqual(req.requester_email, "mike@gmail.com")
        self.assertEqual(req.request_type, ["OPC", "OQC"])
        self.assertEqual(req.name, "Chat")
        self.assertEqual(req.description, desc)

    def create_request_3(self):
        # for now create the request_id manually here
        pass

    def complete_request(self):
        # for now create the request_id manually here
        pass

    # todo: add any further tests you feel appropriate

    # @classmethod
    # def tearDownClass(cls):
    #    UserModel.User.drop_collection()
    #    UserModel.Profile.drop_collection()
    #    RequestModel.Request.drop_collection()


if __name__ == "__main__":
    unittest.main()
