import unittest
from datetime import datetime
from model.UserModel import User, Settings, Profile
from config import *
from service.UserService import *
from mongoengine import *
from new_algo import get_matches


class TestNewAlgo(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        connect("david", host=HOST_IP, port=PORT,
                username=USERNAME, password=PASSWORD,
                authentication_source=AUTHENTICATION_SOURCE)
        print("connected")

        createTestData()

    @classmethod
    def tearDownClass(cls) -> None:
        User.drop_collection()
        Profile.drop_collection()
        Settings.drop_collection()
        disconnect()

    def createTestData() -> None:
        email1 = "chris@gmail.com"
        email2 = "jane@gmail.com"
        email3 = "julia@gmail.com"

        settings1 = {
            "email": email1,
            "location_enabled": True,
            "preferences": ["OPC", "OQC", "OQE"],
            "days": days,
            "time_of_day": time_of_day
        }

        user1 = {
            "email": email1,
            point: [43.653225, -79.383186],
        }
