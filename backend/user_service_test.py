import unittest
from datetime import datetime
from config import *
from mongoengine import *
from UserService import *
from model import UserModel


class TestUserService(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        res = connect('david', host=HOST_IP, port=PORT, username=USERNAME, password=PASSWORD,
                      authentication_source=AUTHENTICATION_SOURCE)
        print("The server is launching....")
        '''
        u0_email = "axxxxx@gmail.com"
        v_email = "yxyx@gmail.com"
        v1_email = "vsvsvs@gmail.com"
        user_0 = create_user(u0_email,[10.653225, -12.383186])
        user1 =create_user(v1_email,[34.653225, -45.383186])
        user2 = create_user(v_email,[13.653225, -50.383186])
        #user = UserService.create_user(u0_email)
        '''

    
    def test_create_user(self):
        u0_email = "aaaaaabbbbb@gmail.com"
        user = create_user(u0_email, [11.653225, -15.383186])
 
        self.assertEqual(user.email, u0_email)

    
    def test_create_user_with_email_repeating_email(self):
        u1_email = "jack@gmail.com"

        u2_email = "jack@gmail.com"

        user1 = create_user(u1_email,[18.653225, -19.383186])
 
        self.assertEqual(user1.email, u1_email)
        #user2 = create_user(u1_email,[[18.653225, -19.383186]])

        self.assertFalse(create_user(u2_email, [55.653225, -69.383186]))
    

    def test_create_user_with_email_invalid_email(self):
        u3_email = "peter@fakeemail"

        self.assertFalse(create_user(u3_email), [20.653225, -20.383186])
   

    def test_get_user_by_gmail_exist(self):
        u4_email = "tripleh@gmail.com"
        user4 = create_user(u4_email, [52.653225, -68.383186])

        returned_user = get_user_by_email(u4_email)
        self.assertTrue(returned_user)
    

    def test_get_user_by_gmail_not_exist(self):
        u5_email = "jack5@gmail.com"

        returned_user = get_user_by_email(u5_email)
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

        user6 = create_user(u6_email, [22.653225, -29.383186])

        self.assertEqual(user6.email, u6_email)

        user_profile6 = create_profile(u6_email, u6_first_name, u6_last_name, u6_date_of_birth,
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

        user_profile = create_profile(u7_email, 'ab', 'c', '2019-09-24', 24, 'Male', "Toronto", "url_1")
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
        user1_profile = create_profile(u8_email, u8_first_name, u8_last_name, u8_date_of_birth, u8_age, u8_gender, u8_location, u8_url)

        self.assertEqual(user1_profile.first_name, u8_first_name)
        self.assertEqual(user1_profile.last_name, u8_last_name)
        self.assertEqual(user1_profile.date_of_birth, u8_date_of_birth)
        self.assertEqual(user1_profile.gender, u8_gender)

        self.assertEqual(user1_profile.email, u8_email)
        self.assertEqual(user1_profile.first_name, u8_first_name)
        self.assertEqual(user1_profile.last_name, u8_last_name)
        self.assertEqual(user1_profile.date_of_birth, u8_date_of_birth)
        self.assertEqual(user1_profile.age, u8_age)
        self.assertEqual(user1_profile.gender, u8_gender)
        self.assertEqual(user1_profile.location, u8_location)
        self.assertEqual(user1_profile.image_url, u8_url)


        #user2 = create_user(u9_email)
        user2_profile = create_profile(u9_email, u9_first_name, u9_last_name, u9_date_of_birth, u9_age, u9_gender, u9_location, u9_url)

        self.assertIsNone(user2_profile)

    '''
    def tearDown(self):
        UserModel.User.drop_collection()
        UserModel.Profile.drop_collection()
        UserModel.UserSettings.drop_collection()
    '''
if __name__ == "__main__":
    unittest.main()
