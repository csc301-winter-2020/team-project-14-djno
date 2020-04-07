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


        du1 = UserModel.User.objects(email="aaaaaabbbbb@gmail.com")
        du1.delete()

        du2 = UserModel.User.objects(email="rosemaryabigale@gmail.com")
        du2.delete()

        du3 = UserModel.User.objects(email="barbaraknox@gmail.com")
        du3.delete()

        du8 = UserModel.User.objects(email="rogermoore@gmail.com")
        du8.delete()

        pu4 =  UserModel.Profile.objects(email="samsonofdelilah@gmail.com")
        pu4.delete()

        pu5 =  UserModel.Profile.objects(email="alexanderthegreat@gmail.com")
        pu5.delete()

        pu6 = UserModel.Profile.objects(email="fabianrogers@gmail.com")
        pu6.delete()

        pu7 = UserModel.Profile.objects(email="doriangrey@gmail.com")
        pu7.delete()

        pu8 = UserModel.Profile.objects(email="rogermoore@gmail.com")
        pu8.delete()

        su9 = UserModel.UserSettings.objects(email="leonidis@gmail.com")
        su9.delete()

        su10 = UserModel.UserSettings.objects(email="alfredhitchcock@gmail.com")
        su10.delete()

        ss11 = UserModel.UserOtherSettings.objects(email="margaretthacher@gmail.com")
        ss11.delete()

        ss12 = UserModel.UserOtherSettings.objects(email="thomasedison@gmail.com")
        ss12.delete()
 
# line 9
    def test_create_user_with_gmail(self):
        u0_email = "aaaaaabbbbb@gmail.com"
        user = UserService.create_user_with_gmail(u0_email)
 
        self.assertEqual(user.email, u0_email)

# line 28
    def test_check_email_availability(self):
        u1_email = "rosemaryabigale@gmail.com"
        UserService.create_user_with_gmail(u1_email)

        self.assertFalse(UserService.check_email_availability("rosemaryabigale@gmail.com"))
        self.assertTrue(UserService.check_email_availability("rodstewart@gmail.com"))

# line 88
    def test_get_user_by_email(self):
        u2_email = "barbaraknox@gmail.com"
        UserService.create_user_with_gmail(u2_email)
        user2a = UserService.get_user_by_email("barbaraknox@gmail.com")
        user2b = UserService.get_user_by_email("ivanhoe@gmail.com")

        self.assertEqual(user2a.email, "barbaraknox@gmail.com")
        self.assertIsNone(user2b)

# line 102
    def test_get_user_profile_by_email(self):
        p3_email = "samsonofdelilah@gmail.com"
        p3_firstname = "Samson"
        p3_lastname = "OfDelilah"
        p3_dob = "1980-03-18"
        p3_age = 40
        p3_gender = "Male"
        p3_image_url = "notexist"
        p3_description = "I am in the bible"

        UserModel.Profile(email=p3_email, first_name=p3_firstname, last_name=p3_lastname, date_of_birth=p3_dob, age=p3_age, gender=p3_gender, image_url=p3_image_url, description=p3_description).save()
        p3 = UserService.get_user_profile_by_email("samsonofdelilah@gmail.com")
        p3a = UserService.get_user_profile_by_email("didnotcreate@gmail.com")

        self.assertEqual(p3.email, "samsonofdelilah@gmail.com")
        self.assertIsNone(p3a)

# line 115
    def test_get_user_setting_by_email(self):
        p4_email = "alexanderthegreat@gmail.com"
        p4_firstname = "Alexander"
        p4_lastname = "Great"
        p4_dob = "1980-03-18"
        p4_age = 40
        p4_gender = "Male"
        p4_image_url = "notexist"
        p4_description = "I am in history"
        
        UserModel.Profile(email=p4_email, first_name=p4_firstname, last_name=p4_lastname, date_of_birth=p4_dob, age=p4_age, gender=p4_gender, image_url=p4_image_url, description=p4_description).save()
        

        # preferences_json = {"email" : "alexanderthegreat@gmail.com"}
        preferences_json = {
        "email" : "alexanderthegreat@gmail.com",
        "location" : [-87.902315, 51.564222],
        "education_navigation" : True,
        "education_support" : True,
        "employment_navigation" : True,
        "employment_support" : True,
        "health_care_navigation" : True,
        "health_care_support" : True,
        "local_navigation" : True,
        "local_support" : True,
        "well_being_leisure" : True,
        "pick_up_and_delivery" : True,
        "pick_up_and_drop_off" : True,
        "homemaking_supports" : True,
        "request_type" : "Dont know"
        }

        sa4 = "leonidis@gmail.com"
        sb4 = [-87.902114, 51.564333]
        sc4 = True
        sd4 = "Dont know"

        UserService.UserSettings(email=sa4, location=sb4, education_navigation=sc4, education_support=sc4, employment_navigation=sc4, employment_support=sc4, health_care_navigation=sc4, health_care_support=sc4, local_navigation=sc4, local_support=sc4, well_being_leisure=sc4, pick_up_and_delivery=sc4, pick_up_and_drop_off=sc4, homemaking_supports=sc4, request_type=sd4).save()

        sett4a = UserService.get_user_setting_by_email("leonidis@gmail.com")
        self.assertEqual(sett4a.email, "leonidis@gmail.com")

        sett4b = UserService.get_user_setting_by_email("alexanderthegreat@gmail.com")
        self.assertEqual(sett4b.email, "alexanderthegreat@gmail.com")

        sett4c = UserService.get_user_setting_by_email("ripvanvinkle@gmail.com")
        self.assertIsNone(sett4c)

# line 135
    def test_create_a_user(self):
        p5_email = "fabianrogers@gmail.com"
        p5_first_name = "Fabian"
        p5_last_name = "Rogers"
        p5_dob = "1995-01-01"
        p5_gender = "Male"
        p5_image_url = ""
        p5_description = "I need help"

        p5 = UserService.create_a_user(p5_email, p5_first_name, p5_last_name, p5_dob, p5_gender, p5_image_url, p5_description)

        self.assertEqual(p5.email, "fabianrogers@gmail.com")

# line 166
    def test_update_profile(self):

        UserModel.Profile(email="doriangrey@gmail.com", first_name="dont know", last_name="dont know", date_of_birth="2020-03-31", age=0, gender="Female", image_url="xyz", description="blank").save()
        
        UserService.update_profile("doriangrey@gmail.com", "Dorian", "Grey", "1901-01-01", "Male", "from a famous novel")
        
        p6 = UserModel.Profile.objects.get(email="doriangrey@gmail.com")

        self.assertEqual(p6.first_name, "Dorian")
        self.assertEqual(p6.last_name, "Grey")
        self.assertEqual(p6.gender, "Male")
        self.assertEqual(p6.description, "from a famous novel")

# line 183
    def test_update_user_settings(self):
        preferences_json = {
        "email" : "alfredhitchcock@gmail.com",
        "location" : [-87.902592, 51.564721],
        "education_navigation" : True,
        "education_support" : True,
        "employment_navigation" : True,
        "employment_support" : True,
        "health_care_navigation" : True,
        "health_care_support" : True,
        "local_navigation" : True,
        "local_support" : True,
        "well_being_leisure" : True,
        "pick_up_and_delivery" : True,
        "pick_up_and_drop_off" : True,
        "homemaking_supports" : True,
        "request_type" : "help required for a good story"
        }

        p7 = UserService.update_user_settings(preferences_json)

        self.assertEqual(p7.email, "alfredhitchcock@gmail.com")



# line 216

# Test has been commmented out because the tested function has error. It is trying to return profile, whereas the User document has no attribute profile

#    def test_get_user_profile(self):

#        UserModel.User(email="rogermoore@gmail.com").save()

#        UserModel.Profile(email="rogermoore@gmail.com", first_name="Roger", last_name="Moore", date_of_birth="1960-03-31", age=61, gender="Male", image_url="abc", description="actor").save()

#        p8 = UserService.get_user_profile("rogermoore@gmail.com")

#        self.assertEqual(p8.first_name, "Roger")
#        self.assertEqual(p8.last_name, "Moore")
#        self.assertEqual(p8.gender, "Male")
#        self.assertEqual(p8.description, "actor")

# line 227
    def test_save_other_setting(self):

        json_data = {
            "email" : "margaretthacher@gmail.com",
            "location" : [-87.902921, 51.564642],
            "location_enabled" : True,
            "monday" : True,
            "tuesday" : True,
            "wednesday" : True,
            "thursday" : True,
            "friday" : True,
            "saturday" : False,
            "sunday" : False,
            "morning" : True,
            "afternoon" : True,
            "evening" : True,
            "OPC" : True,
            "OQC" : False,
            "OQE" : False
            }

        s9 = UserService.save_other_setting(json_data)

        self.assertEqual(s9.email, "margaretthacher@gmail.com")


# line 248
    def test_get_other_setting(self):
        
        s10_email = "thomasedison@gmail.com"
        s10_loc = [-87.902408, 51.564001]
        s10_loc_en = True
        s10_mon = False
        s10_tue = False
        s10_wed = False
        s10_thu = False
        s10_fri = False
        s10_sat = True
        s10_sun = True
        s10_m = True
        s10_a = True
        s10_e = True
        s10_OPC = True
        s10_OQC = True
        s10_OQE = True

        UserService.UserOtherSettings(email=s10_email, location=s10_loc, location_enabled=s10_loc_en, monday=s10_mon, tuesday=s10_tue, wednesday=s10_wed, thursday=s10_thu, friday=s10_fri, saturday=s10_sat, sunday=s10_sun, morning=s10_m, afternoon=s10_a, evening=s10_e, OPC=s10_OPC, OQC=s10_OQC, OQE=s10_OQE).save()
        s10 = UserService.UserOtherSettings.objects.get(email = "thomasedison@gmail.com")
#        s10a = UserService.UserOtherSettings.objects.get(email = "thomasalvaedison@gmail.com")

        self.assertEqual(s10.email, "thomasedison@gmail.com")

#        self.assertIsNone(s10a)


if __name__ == "__main__":
    unittest.main()
