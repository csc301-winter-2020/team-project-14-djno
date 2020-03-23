import unittest
from datetime import datetime
from model.UserModel import User, Settings, Profile
from config import *
from UserService import *
from mongoengine import *
from new_algo import get_matches
import json


class TestNewAlgo(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        connect("david", host=HOST_IP, port=PORT,
                username=USERNAME, password=PASSWORD,
                authentication_source=AUTHENTICATION_SOURCE)
        print("connected")

        # Clear database
        # User.drop_collection()
        # Profile.drop_collection()
        # Settings.drop_collection()
        # print("Database cleared")

        # Create Test Data
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
        profile1 = {
            "email": email1,
            "first_name": "Chris",
            "last_name": "Jones",
            "date_of_birth": "1995-05-22",
            "gender": "Male",
            "location": "Toronto"
        }
        user1 = {
            "email": email1,
            "point": [43.653225, -79.383186],
        }

        settings2 = {
            "email": email2,
            "location_enabled": True,
            "preferences": ["OPC"],
            "days": ["Saturday", "Sunday"],
            "time_of_day": ["Evening", "Night"]
        }
        profile2 = {
            "email": email2,
            "first_name": "Jane",
            "last_name": "Austin",
            "date_of_birth": "2000-01-27",
            "gender": "Female",
            "location": "Toronto"
        }
        user2 = {
            "email": email2,
            "point": [43.661461, -79.397163],
        }

        settings3 = {
            "email": email3,
            "location_enabled": True,
            "preferences": ["OQC"],
            "days": ["Monday", "Wednesday", "Friday", "Saturday"],
            "time_of_day": ["Morning", "Afternoon"]
        }
        profile3 = {
            "email": email3,
            "first_name": "Julia",
            "last_name": "Rose",
            "date_of_birth": "1955-07-11",
            "gender": "Female",
            "location": "Etobicoke"
        }
        user3 = {
            "email": email3,
            "point": [43.598401, -79.506262],
        }

        # create_update_user(json.dumps(user1))
        # create_update_user(json.dumps(user2))
        # create_update_user(json.dumps(user3))
        u1 = create_user(email1, [43.653225, -79.383186])
        u2 = create_user(email2, [43.661461, -79.397163])
        u3 = create_user(email3, [43.598401, -79.506262])

        u1.settings = create_update_settings(json.dumps(settings1))
        u1.profile = create_update_profile(json.dumps(profile1))

        u2.settings = create_update_settings(json.dumps(settings2))
        u2.profile = create_update_profile(json.dumps(profile2))

        u3.settings = create_update_settings(json.dumps(settings3))
        u3.profile = create_update_profile(json.dumps(profile3))

        print("Test data created")

    @classmethod
    def tearDownClass(cls) -> None:
        # User.drop_collection()
        # Profile.drop_collection()
        # Settings.drop_collection()
        disconnect()
        print("disconnected")

    def test_algo_1(self):
        data = {
            "requestor_email": "sarah@gmail.com",
            "title": "feeling lonely",
            "location": [43.653225, -79.383186],  # Downtown Toronto
            "datetime": datetime(2020, 3, 25, 17),  # Wednesday afternoon
            "category": "RHS",
            "description": "I need somebody to talk to"
        }
        candidates = get_matches(data)
        self.assertEquals(candidates[0].email, "chris@gmail.com")


if __name__ == "__main__":
    unittest.main()
