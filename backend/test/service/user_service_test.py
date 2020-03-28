import unittest
from datetime import datetime
from config import *
from mongoengine import *
from service import UserService
from model import UserModel
import json




class TestUserService(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        res = connect('david', host=HOST_IP, port=PORT, username=USERNAME, password=PASSWORD,
                      authentication_source=AUTHENTICATION_SOURCE)
        print("The server is launching....")

        du0 = UserService.User.objects(email="aaaaaabbbbb@gmail.com")
        du0.delete()

        du1 = UserService.User.objects(email="scarlett@gmail.com")
        du1.delete()

        du4 = UserService.User.objects(email="tripleh@gmail.com")
        du4.delete()

        du6 = UserService.User.objects(email="michaeljackson@gmail.com")
        du6.delete()

        du7 = UserService.User.objects(email="newperson@gmail.com")
        du7.delete()

        du8 = UserService.User.objects(email="peterjackson@gmail.com")
        du8.delete()

        du10 = UserService.User.objects(email="wyatt@gmail.com")
        du10.delete()

        pu6 = UserService.Profile.objects(email="michaeljackson@gmail.com")
        pu6.delete()

        pu7 = UserService.Profile.objects(email="newperson@gmail.com")
        pu7.delete()

        pu8 = UserService.Profile.objects(email="peterjackson@gmail.com")
        pu8.delete()

        pu12 = UserService.Profile.objects(email="baxter@gmail.com")
        pu12.delete()

        su13 = UserService.Settings.objects(email="fernandez@gmail.com")
        su13.delete()

        su14 = UserService.Settings.objects(email="jacqueline@gmail.com")
        su14.delete()
 
 
    def test_create_user(self):
        u0_email = "aaaaaabbbbb@gmail.com"
        user = UserService.create_user(u0_email, [11.653225, -15.383186])
 
        self.assertEqual(user.email, u0_email)

    
    def test_create_user_with_email_repeating_email(self):
        u1_email = "scarlett@gmail.com"

        u2_email = "scarlett@gmail.com"

        user1 = UserService.create_user(u1_email,[18.653225, -19.383186])
 
        self.assertEqual(user1.email, u1_email)
        #user2 = create_user(u1_email,[[18.653225, -19.383186]])

        self.assertFalse(UserService.create_user(u2_email, [55.653225, -69.383186]))
    

    def test_create_user_with_email_invalid_email(self):
        u3_email = "peter@fakeemail"

        self.assertFalse(UserService.create_user(u3_email), [20.653225, -20.383186])
   

    def test_get_user_by_gmail_exist(self):
        u4_email = "tripleh@gmail.com"
        user4 = UserService.create_user(u4_email, [52.653225, -68.383186])

        returned_user = UserService.get_user_by_email(u4_email)
        self.assertTrue(returned_user)
    

    def test_get_user_by_gmail_not_exist(self):
        u5_email = "carter@gmail.com"

        returned_user = UserService.get_user_by_email(u5_email)
        self.assertFalse(returned_user)
    
    

    def test_create_profile(self):
        # email, first_name, last_name, date_of_birth, gender
        u6_email = "michaeljackson@gmail.com"
        u6_first_name = "michael"
        u6_last_name = "jackson"
        u6_date_of_birth = "2016-05-18"
        u6_age = 24 
        u6_gender = "Male"
        u6_location = "Vancouver"
        u6_url = "url_1"

        user6 = UserService.create_user(u6_email, [22.653225, -29.383186])

        self.assertEqual(user6.email, u6_email)

        user_profile6 = UserService.create_profile(u6_email, u6_first_name, u6_last_name, u6_date_of_birth,
         u6_age, u6_gender, u6_location, u6_url)

        self.assertEqual(user_profile6.email, u6_email)
        self.assertEqual(user_profile6.first_name, u6_first_name)
        self.assertEqual(user_profile6.last_name, u6_last_name)
        self.assertEqual(user_profile6.date_of_birth, u6_date_of_birth)
        self.assertEqual(user_profile6.age, u6_age)
        self.assertEqual(user_profile6.gender, u6_gender)
        self.assertEqual(user_profile6.location, u6_location)
        self.assertEqual(user_profile6.image_url, u6_url)



    def test_create_profile_email_does_not_exist(self):
         # email, first_name, last_name, date_of_birth, gender
        u7_email = "newperson@gmail.com"

        user_profile = UserService.create_profile(u7_email, 'ab', 'c', '2019-09-24', 24, 'Male', "Toronto", "url_1")
        self.assertEqual(u7_email, user_profile.email)


    def test_create_profile_repeating_email(self):
        # to prevent 2 profile instances with the same email
        u8_email = "peterjackson@gmail.com"
        u8_first_name = "peter"
        u8_last_name = "jackson"
        u8_date_of_birth = "2016-05-18"
        u8_age = 30
        u8_gender = "Male"
        u8_location = "Vancouver"
        u8_url = "url_2"

        u9_email = "peterjackson@gmail.com"
        u9_first_name = "peter"
        u9_last_name = "jackson"
        u9_date_of_birth = "2016-05-18"
        u9_age = 30
        u9_gender = "Male"
        u9_location = "Vancouver"
        u9_url = "url_3"

        #user1 = create_user(u8_email)
        p8 = UserService.create_profile(u8_email, u8_first_name, u8_last_name, u8_date_of_birth, u8_age, u8_gender, u8_location, u8_url)

        self.assertEqual(p8.first_name, u8_first_name)
        self.assertEqual(p8.last_name, u8_last_name)
        self.assertEqual(p8.date_of_birth, u8_date_of_birth)
        self.assertEqual(p8.gender, u8_gender)
        self.assertEqual(p8.email, u8_email)
        self.assertEqual(p8.age, u8_age)
        self.assertEqual(p8.location, u8_location)
        self.assertEqual(p8.image_url, u8_url)


        #user2 = create_user(u9_email)
        p9 = UserService.create_profile(u9_email, u9_first_name, u9_last_name, u9_date_of_birth, u9_age, u9_gender, u9_location, u9_url)

        self.assertIsNone(p9)

    def test_create_update_user(self):

        user10 = {
        "email": "wyatt@gmail.com",
        "point": [-87.902315, 51.564222]
        }

        u10 = UserService.create_update_user(json.dumps(user10))

        self.assertEqual(u10.email, "wyatt@gmail.com")

    def test_get_user_by_email(self):

        u10a = UserService.get_user_by_email("wyatt@gmail.com")
        u11 = UserService.get_user_by_email("corvin@gmail.com")

        self.assertEqual(u10a.email, "wyatt@gmail.com")
        self.assertIsNone(u11)

    def test_email_available(self):

        e1 = UserService.email_available("courage@gmail.com")
        e2 = UserService.email_available("wyatt@gmail.com")

        self.assertTrue(e1)
        self.assertFalse(e2)


    def test_create_update_profile(self):

        prof12 = {
        "email": "baxter@gmail.com",
        "first_name": "Baxter",
        "last_name": "Groon",
        "date_of_birth": "1967-11-11",
        "age": 53,
        "gender": "Male",
        "location": "Toronto",
        "image_url": "abc"
        }

        p12 = UserService.create_update_profile(json.dumps(prof12))

        self.assertEqual(p12.email, "baxter@gmail.com")


    def test_get_user_profile_by_email(self):
        tp12 = UserService.get_user_profile_by_email("baxter@gmail.com")

        self.assertTrue(tp12)
        self.assertEqual(tp12.email, "baxter@gmail.com")

    def test_update_profile(self):
        email = "baxter@gmail.com"
        first_name = "Baxter"
        last_name = "Groon"
        date_of_birth = "1957-11-11"
        age = 63
        gender = "Male"
        location = "Toronto"
        image_url = "abc"
        
        tp12a = UserService.update_profile(email, first_name, last_name, date_of_birth, age, gender, location, image_url)

        self.assertTrue(tp12a)

    def test_create_update_settings(self):
        sett13 = {
        "email": "fernandez@gmail.com",
        "location_enabled": True,
        "preferences": p_rules,
        "days": days,
        "time_of_day": ["Evening"]
        }

        s13 = UserService.create_update_settings(json.dumps(sett13))

        self.assertEqual(s13.email, "fernandez@gmail.com")

    
    def test_create_settings(self):
        email = "jacqueline@gmail.com"
        gps = True
        preferences = p_rules
        days = ["Monday", "Tuesday", "Wednesday"]
        time_of_day = ["Morning"]

        s14 = UserService.create_settings(email, gps, preferences, days, time_of_day)

        self.assertEqual(s14.email, "jacqueline@gmail.com")

    def test_get_user_settings_by_email(self):
        ts15 = UserService.get_user_settings_by_email("jacqueline@gmail.com")
        ts16 = UserService.get_user_settings_by_email("horatio@gmail.com")

        self.assertEqual(ts15.email, "jacqueline@gmail.com")
        self.assertIsNone(ts16)

    def test_update_settings(self):
        email = "jacqueline@gmail.com"
        gps = True
        preferences = p_rules
        days = ["Monday", "Tuesday", "Wednesday"]
        time_of_day = ["Afternoon"]

        ts17 = UserService.update_settings(email, gps, preferences, days, time_of_day)

        self.assertTrue(ts17)


if __name__ == "__main__":
    unittest.main()
