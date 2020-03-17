import unittest
from datetime import datetime
from model.UserModel import *
from config import *
from service.UserService import *
from mongoengine import *


class TestNewAlgo(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        connect("david", host=HOST_IP, port=PORT,
                username=USERNAME, password=PASSWORD,
                authentication_source=AUTHENTICATION_SOURCE)
        print("connected")

        email1 = "chris@gmail.com"
        pref1 = Preferences(OPC=True, OQC=True, OQE=True)
        days1 = DayAvailability(Monday=True, Tuesday=True, Wednesday=True,
                                Thursday=True, Friday=True, Saturday=True, Sunday=True)
        time1 = TimeAvailability(Morning=True, Afternoon=True,
                                 Evening=True, Night=True)

        email2 = "jane@gmail.com"
        pref2 = Preferences(OPC=True, OQC=False, OQE=False)
        days2 = DayAvailability(Monday=False, Tuesday=False, Wednesday=False,
                                Thursday=False, Friday=False, Saturday=True, Sunday=True)
        time2 = TimeAvailability(Morning=False, Afternoon=False,
                                 Evening=True, Night=True)

        email3 = "julia@gmail.com"
        pref3 = Preferences(OPC=False, OQC=True, OQE=False)
        days3 = DayAvailability(Monday=True, Tuesday=False, Wednesday=True,
                                Thursday=False, Friday=True, Saturday=True, Sunday=False)
        time3 = TimeAvailability(Morning=True, Afternoon=True,
                                 Evening=False, Night=False)

        create_user(email1, [5, 5])
        create_profile(email1, "Chris", "Jones", "1995-05-22",
                       25, "Male", "Toronto", "")
        create_settings(email1, True, pref1, days1, time1)

        # User(email="chris@gmail.com",
        #      current_coordinates=[5, 5]
        #      ).save()
        # Profile(email="chris@gmail.com",
        #         first_name="Chris",
        #         last_name="Jones",
        #         date_of_birth="1995-05-22",
        #         age=25,
        #         gender="Male",
        #         location="Toronto"
        #         ).save()
        # Settings(email="chris@gmail.com",
        #          GPS=True,
        #          preferences=pref1,
        #          days=days1,
        #          time_of_day=time1,
        #          ).save()

        create_user(email2, [10, 4])
        create_profile(email2, "Jane", "Austin", "2000-01-27",
                       20, "Female", "Vancouver")
        create_settings(email2, True, pref2, days2, time2)

        # User(
        #     email="jane@gmail.com",
        #     current_coordinates=[10, 4]
        # ).save()
        # Profile(
        #     email="jane@gmail.com",
        #     first_name="Jane",
        #     last_name="Austin",
        #     date_of_birth="2000-01-27",
        #     age=20,
        #     gender="Female",
        #     location="Vancouver"
        # ).save()

        # Settings(email="jane@gmail.com",
        #          GPS=True,
        #          preferences=pref2,
        #          days=days2,
        #          time_of_day=time2,
        #          ).save()

        create_user(email3)
        create_profile(email3, "Julia", "Rose",
                       "1955-07-11", 65, "Female", "Ottawa")
        create_settings(email3, False, pref3, days3, time3)

        # User(
        #     email="julia@gmail.com"
        # ).save()
        # Profile(
        #     email="julia@gmail.com",
        #     first_name="Julia",
        #     last_name="Rose",
        #     date_of_birth="1956-07-11",
        #     age=65,
        #     gender="Female",
        #     location="Ottawa"
        # ).save()

        # Settings(email="julia@gmail.com",
        #          GPS=False,
        #          preferences=pref3,
        #          days=days3,
        #          time_of_day=time3,
        #          ).save()

        print("users created")

    @classmethod
    def tearDownClass(cls) -> None:
        User.drop_collection()
        Profile.drop_collection()
        Settings.drop_collection()

    def test_filter_by_preference(self):
        qSet1 = Settings.objects.filter_by_pref("OPC")
        qSet2 = Settings.objects.filter_by_pref("OQC")
        qSet3 = Settings.objects.filter_by_pref("OQE")

        for s in qSet1:
            # print(s.email)
            self.assertTrue(
                s.email in ["chris@gmail.com", "jane@gmail.com"])

        for s2 in qSet2:
            self.assertTrue(s2.email in ["chris@gmail.com", "julia@gmail.com"])

        for s3 in qSet3:
            self.assertTrue(s3.email in ["chris@gmail.com"])

    def test_filter_by_time(self):
        qSet1 = Settings.objects.filter_by_time("Morning")
        qSet2 = Settings.objects.filter_by_time("Afternoon")
        qSet3 = Settings.objects.filter_by_time("Evening")
        qSet4 = Settings.objects.filter_by_time("Night")

        for s1 in qSet1:
            self.assertTrue(s1.email in ["chris@gmail.com", "julia@gmail.com"])

        for s2 in qSet2:
            self.assertTrue(s2.email in ["chris@gmail.com", "julia@gmail.com"])

        for s3 in qSet3:
            self.assertTrue(s3.email in ["chris@gmail.com", "jane@gmail.com"])

        for s4 in qSet4:
            self.assertTrue(s4.email in ["chris@gmail.com", "jane@gmail.com"])

    def test_filter_by_day(self):
        qSet1 = Settings.objects.filter_by_day("Monday")
        qSet2 = Settings.objects.filter_by_day("Tuesday")
        qSet3 = Settings.objects.filter_by_day("Wednesday")
        qSet4 = Settings.objects.filter_by_day("Thursday")
        qSet5 = Settings.objects.filter_by_day("Friday")
        qSet6 = Settings.objects.filter_by_day("Saturday")
        qSet7 = Settings.objects.filter_by_day("Sunday")
        # TODO

    def test_filter_by_location(self):
        qSet1 = User.objects.filter_by_location([40, 5])
        for user in qSet1:
            print(user.email)
        # TODO: Getting an error

    def test_algo_1(self):
        pass


if __name__ == "__main__":
    unittest.main()
