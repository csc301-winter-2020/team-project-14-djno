import unittest
from datetime import datetime
#from model.UserModel import User, Settings, Profile
from model import UserModel #new
from config import *
from service import UserService
#from UserService import *
from mongoengine import *
from algorithm import new_algo
#from new_algo import get_matches
import json


class TestNewAlgo(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        connect("david", host=HOST_IP, port=PORT,
                username=USERNAME, password=PASSWORD,
                authentication_source=AUTHENTICATION_SOURCE)
        print("connected")

        # Clear database

        du1 = UserService.User.objects(email="chris@gmail.com")
        du1.delete()
        du2 = UserService.User.objects(email="jane@gmail.com")
        du2.delete()
        du3 = UserService.User.objects(email="julia@gmail.com")
        du3.delete()
        du4 = UserService.User.objects(email="patrick@gmail.com")
        du4.delete()
        du5 = UserService.User.objects(email="alice@gmail.com")
        du5.delete()
        du6 = UserService.User.objects(email="robert@gmail.com")
        du6.delete()

        pu1 = UserService.Profile.objects(email="chris@gmail.com")
        pu1.delete()
        pu2 = UserService.Profile.objects(email="jane@gmail.com")
        pu2.delete()
        pu3 = UserService.Profile.objects(email="julia@gmail.com")
        pu3.delete()
        pu4 = UserService.Profile.objects(email="patrick@gmail.com")
        pu4.delete()
        pu5 = UserService.Profile.objects(email="alice@gmail.com")
        pu5.delete()
        pu6 = UserService.Profile.objects(email="robert@gmail.com")
        pu6.delete()

        su1 = UserService.Settings.objects(email="chris@gmail.com")
        su1.delete()
        su2 = UserService.Settings.objects(email="jane@gmail.com")
        su2.delete()
        su3 = UserService.Settings.objects(email="julia@gmail.com")
        su3.delete()
        su4 = UserService.Settings.objects(email="patrick@gmail.com")
        su4.delete()
        su5 = UserService.Settings.objects(email="alice@gmail.com")
        su5.delete()
        su6 = UserService.Settings.objects(email="robert@gmail.com")
        su6.delete()

        print("Database cleared")

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
            "preferences": p_rules,
            "days": days,
            "time_of_day": time_of_day
        }
        profile1 = {
            "email": email1,
            "first_name": "Chris",
            "last_name": "Jones",
            "date_of_birth": "1995-05-22",
            "age": 24,
            "gender": "Male",
            "location": "Toronto",
            "image_url": "abc"
        }
        user1 = {
            "email": email1,
            "point": [-79.383186, 43.653225]
        }
        ###################################################
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
            "age": 20,
            "gender": "Female",
            "location": "Toronto",
            "image_url": "abc"
        }
        user2 = {
            "email": email2,
            "point": [-79.397163, 43.661461]
        }
        ###################################################
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
            "age": 65,
            "gender": "Female",
            "location": "Etobicoke",
            "image_url": "abc"
        }
        user3 = {
            "email": email3,
            "point": [-79.506262, 43.598401]
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
            "age": 19,
            "gender": "Male",
            "location": "Fort Hope",    # airport
            "image_url": "abc"
        }
        user4 = {
            "email": email4,
            "point": [-87.906550, 51.561482]
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
            "age": 23,
            "gender": "Female",
            "location": "Red Lake",
            "image_url": "abc"
        }
        user5 = {
            "email": email5,
            "point": [-89.252862, 48.392472]  # Thunder Bay
        }
        #########################################################
        settings6 = {
            "email": email6,
            "location_enabled": True,
            "preferences": p_rules,
            "days": days,
            "time_of_day": ["Evening"]
        }
        profile6 = {
            "email": email6,
            "first_name": "Robert",
            "last_name": "Fisher",
            "date_of_birth": "1987-12-14",
            "age": 33,
            "gender": "Male",
            "location": "Toronto",
            "image_url": "abc"
        }
        user6 = {
            "email": email6,
            "point": [-93.832722, 50.997865]
        }

        u1 = UserService.create_update_user(json.dumps(user1))
        u2 = UserService.create_update_user(json.dumps(user2))
        u3 = UserService.create_update_user(json.dumps(user3))
        u4 = UserService.create_update_user(json.dumps(user4))
        u5 = UserService.create_update_user(json.dumps(user5))
        u6 = UserService.create_update_user(json.dumps(user6))

        # u1 = create_user(email1, [43.653225, -79.383186])
        # u2 = create_user(email2, [43.661461, -79.397163])
        # u3 = create_user(email3, [43.598401, -79.506262])
        # u4 = create_user(email4, [51.561482, -87.906550])
        # u5 = create_user(email5, [48.392472, -89.252862])
        # u6 = create_user(email6, [50.997865, -93.832722])

        u1.update(
            settings=UserService.create_update_settings(json.dumps(settings1)),
            profile=UserService.create_update_profile(json.dumps(profile1))
        )
        # u1.settings = create_update_settings(json.dumps(settings1))
        # u1.profile = create_update_profile(json.dumps(profile1))

        u2.update(
            settings=UserService.create_update_settings(json.dumps(settings2)),
            profile=UserService.create_update_profile(json.dumps(profile2))
        )

        # u2.settings = create_update_settings(json.dumps(settings2))
        # u2.profile = create_update_profile(json.dumps(profile2))

        u3.update(
            settings=UserService.create_update_settings(json.dumps(settings3)),
            profile=UserService.create_update_profile(json.dumps(profile3))
        )

        # u3.settings = create_update_settings(json.dumps(settings3))
        # u3.profile = create_update_profile(json.dumps(profile3))

        u4.update(
            settings=UserService.create_update_settings(json.dumps(settings4)),
            profile=UserService.create_update_profile(json.dumps(profile4))
        )

        # u4.settings = create_update_settings(json.dumps(settings4))
        # u4.profile = create_update_profile(json.dumps(profile4))

        u5.update(
            settings=UserService.create_update_settings(json.dumps(settings5)),
            profile=UserService.create_update_profile(json.dumps(profile5))
        )

        # u5.settings = create_update_settings(json.dumps(settings5))
        # u5.profile = create_update_profile(json.dumps(profile5))

        u6.update(
            settings=UserService.create_update_settings(json.dumps(settings6)),
            profile=UserService.create_update_profile(json.dumps(profile6))
        )

        # u6.settings = create_update_settings(json.dumps(settings6))
        # u6.profile = create_update_profile(json.dumps(profile6))

        # p1 = create_profile(email = 'chris@gmail.com', first_name = 'Chris', last_name ='Jones', date_of_birth = '1995-05-22', age=25, gender='Male', location = 'Toronto', image_url = 'abc')
        # u1.profile = p1
        # u1.save()

        # s1 = create_settings(email = 'chris@gmail.com', gps = True, preferences= ["OPC", "OQC", "OQE"], days= ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], time_of_day = ["Morning", "Afternoon", "Evening", "Night"])
        # u1.settings = s1
        # u1.save()

        # p2 = create_profile(email = 'jane@gmail.com', first_name = 'Jane', last_name ='Austin', date_of_birth = '2000-01-27', age=20, gender='Female', location = 'Toronto', image_url = 'abc')
        # u2.profile = p2
        # u2.save()

        # s2 = create_settings(email = 'jane@gmail.com', gps = True, preferences= ["OPC"], days= ["Saturday", "Sunday"], time_of_day = ["Evening", "Night"])
        # u2.settings = s2
        # u2.save()

        # p3 = create_profile(email = 'julia@gmail.com', first_name = 'Julia', last_name ='Rose', date_of_birth = '1955-07-11', age=65, gender='Female', location = 'Etobicoke', image_url = 'abc')
        # u3.profile = p3
        # u3.save()

        # s3 = create_settings(email = 'julia@gmail.com', gps = True, preferences= ["OQC"], days= ["Monday", "Wednesday", "Friday", "Saturday"], time_of_day = ["Morning", "Afternoon"])
        # u3.settings = s3
        # u3.save()

        # p4 = create_profile(email = 'patrick@gmail.com', first_name = 'Patrick', last_name ='Smith', date_of_birth = '1991-08-01', age=19, gender='Male', location = 'Markham', image_url = 'abc')
        # u4.profile = p4
        # u4.save()

        # s4 = create_settings(email = 'patrick@gmail.com.com', gps = True, preferences= ["OPC", "OQC"], days= ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], time_of_day = ["Evening", "Night"])
        # u4.settings = s4
        # u4.save()

        # p5 = create_profile(email = 'alice@gmail.com', first_name = 'Alice', last_name ='Moore', date_of_birth = '1997-02-20', age=23, gender='Female', location = 'Toronto', image_url = 'abc')
        # u5.profile = p5
        # u5.save()

        # s5 = create_settings(email = 'alice@gmail.com', gps = True, preferences= ["OPC", "OQE"], days= ["Saturday", "Sunday"], time_of_day = ["Morning", "Afternoon", "Evening", "Night"])
        # u5.settings = s5
        # u5.save()

        # p6 = create_profile(email = 'robert@gmail.com', first_name = 'Robert', last_name ='Fisher', date_of_birth = '1987-12-14', age=33, gender='Male', location = 'Toronto', image_url = 'abc')
        # u6.profile = p6
        # u6.save()

    #    s6 = create_settings(email = 'robert@gmail.com', gps = True, preferences= ["OPC", "OQC", "OQE"], days= ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], time_of_day = ["Evening"])
    #    u6.settings = s6
    #    u6.save()
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
            "location": [-79.383186, 43.653225],  # Downtown Toronto
            "datetime": datetime(2020, 3, 25, 17),  # Wednesday afternoon
            "category": "RHS",
            "description": "I need somebody to talk to"
        }
        candidates = new_algo.get_matches(data)
        expected_profile = UserService.get_user_profile_by_email("chris@gmail.com")
        # print("Expected: ", expected_profile)
        self.assertEqual(candidates[0], expected_profile)

    def test_algo_2(self):
        data = {
            "requestor_email": "james@gmail.com",
            "title": "need company",
            "location": [-87.906276, 51.561992],  # Fort Hope
            "datetime": datetime(2020, 3, 27, 19),  # Friday Evening
            "category": "RLN",
            "description": "New in town, need someone to show me around"
        }
        candidates = new_algo.get_matches(data)
        expected_profile = UserService.get_user_profile_by_email("patrick@gmail.com")
        # print("Expected: ", expected_profile)
        self.assertEqual(candidates[0], expected_profile)

    def test_algo_3(self):
        data = {
            "requestor_email": "jason@gmail.com",
            "title": "need company",
            "location": [-89.252862, 48.392472],  # Thunder Bay
            "datetime": datetime(2020, 3, 29, 21),  # Sunday Evening
            "category": "RHMS",
            "description": "Need someone to do weekly errands"
        }
        candidates = new_algo.get_matches(data)
        expected_profile = UserService.get_user_profile_by_email("alice@gmail.com")
        # print("Expected: ", expected_profile)
        self.assertEqual(candidates[0], expected_profile)

    def test_algo_4(self):
        data = {
            "requestor_email": "jason@gmail.com",
            "title": "need company",
            "location": [-93.832156, 50.997311],  # Red Lake
            "datetime": datetime(2020, 3, 29, 21),  # Sunday Evening
            "category": "RHMS",
            "description": "Need someone to do weekly errands"
        }
        candidates = new_algo.get_matches(data)
        expected_profile = UserService.get_user_profile_by_email("robert@gmail.com")
        # print("Expected: ", expected_profile)
        self.assertEqual(candidates[0], expected_profile)


if __name__ == "__main__":
    unittest.main()
