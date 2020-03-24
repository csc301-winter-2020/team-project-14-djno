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
        email4 = "patrick@gmail.com"
        email5 = "alice@gmail.com"
        email6 = "robert@gmail.com"

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
            "age":24,
            "gender": "Male",
            "location": "Toronto",
            "image_url": "abc"
        }
        user1 = {
            "email": email1,
            "point": [43.653225, -79.383186]
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
            "age":20,
            "gender": "Female",
            "location": "Toronto",
            "image_url": "abc"
        }
        user2 = {
            "email": email2,
            "point": [43.661461, -79.397163]
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
            "age":65,
            "gender": "Female",
            "location": "Etobicoke",
            "image_url": "abc"
        }
        user3 = {
            "email": email3,
            "point": [43.598401, -79.506262]
        }
        ###########################################################

        settings4 = {
            "email": email4,
            "location_enabled": True,
            "preferences": ["OPC", "OQC"],
            "days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "time_of_day": ["Evening", "Night"]
        }
        profile4 = {
            "email": email4,
            "first_name": "Patrick",
            "last_name": "Smith",
            "date_of_birth": "1991-08-01",
            "age":19,
            "gender": "Male",
            "location": "Markham",
            "image_url": "abc"
        }
        user4 = {
            "email": email4,
            "point": [43.880277, -79.257261]
        }
        ###################################################
        settings5 = {
            "email": email5,
            "location_enabled": True,
            "preferences": ["OPC", "OQE"],
            "days": ["Saturday", "Sunday"],
            "time_of_day": time_of_day
        }
        profile5 = {
            "email": email5,
            "first_name": "Alice",
            "last_name": "Moore",
            "date_of_birth": "1997-02-20",
            "age":23,
            "gender": "Female",
            "location": "Toronto",
            "image_url": "abc"
        }
        user5 = {
            "email": email5,
            "point": [43.714072, -79.412324] # Lawrence Park Toronto 
        }
        #########################################################
        settings6 = {
            "email": email6,
            "location_enabled": True,
            "preferences": ["OPC", "OQC", "OQE"],
            "days": days,
            "time_of_day": ["Evening"]
        }
        profile6 = {
            "email": email6,
            "first_name": "Robert",
            "last_name": "Fisher",
            "date_of_birth": "1987-12-14",
            "age":33,
            "gender": "Male",
            "location": "Toronto",
            "image_url": "abc"
        }
        user6 = {
            "email": email6,
            "point": [43.784021, -79.360128]  # Don Valley Village, Toronto
        }

        # create_update_user(json.dumps(user1))
        # create_update_user(json.dumps(user2))
        # create_update_user(json.dumps(user3))
        u1 = create_user(email1, [43.653225, -79.383186])
        u2 = create_user(email2, [43.661461, -79.397163])
        u3 = create_user(email3, [43.598401, -79.506262])
        u4 = create_user(email4, [43.880277, -79.257261])
        u5 = create_user(email5, [43.714072, -79.412324])
        u6 = create_user(email6, [43.784021, -79.360128])

        u1.settings = create_update_settings(json.dumps(settings1))
        u1.profile = create_update_profile(json.dumps(profile1))

        u2.settings = create_update_settings(json.dumps(settings2))
        u2.profile = create_update_profile(json.dumps(profile2))

        u3.settings = create_update_settings(json.dumps(settings3))
        u3.profile = create_update_profile(json.dumps(profile3))

        u4.settings = create_update_settings(json.dumps(settings4))
        u4.profile = create_update_profile(json.dumps(profile4))

        u5.settings = create_update_settings(json.dumps(settings5))
        u5.profile = create_update_profile(json.dumps(profile5))

        u6.settings = create_update_settings(json.dumps(settings6))
        u6.profile = create_update_profile(json.dumps(profile6))

        p7 = Profile(email= 'bryan@gmail.com', first_name ='Bryan', last_name = 'Adams', date_of_birth = '1987-12-14', gender = 'Male', location = 'Toronto').save()

        p8 = create_profile(email='bbryan@gmail.com', first_name ='Bryan', last_name = 'Adams', date_of_birth = '1987-12-14', age=33, gender = 'Male', location = 'Toronto', image_url='abc')
        

        p9 = create_profile(email = 'chris@gmail.com', first_name = 'Chris', last_name ='Jones', date_of_birth = '1995-05-22', age=25, gender='Male', location = 'Toronto', image_url = 'abc')
        u1.profile = p9
        u1.save()

        s9 = create_settings(email = 'chris@gmail.com', gps = True, preferences= ["OPC", "OQC", "OQE"], days= ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], time_of_day = ["Morning", "Afternoon", "Evening", "Night"])
        u1.settings = s9
        u1.save()
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
