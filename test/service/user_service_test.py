import unittest
from datetime import datetime
from backend.config import *
from mongoengine import *
from backend.service import UserService
from backend.model import UserModel


class TestUserService(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        res = connect(DATABASE_NAME, host=HOST_IP, port=PORT, username=USERNAME, password=PASSWORD,
                      authentication_source=AUTHENTICATION_SOURCE)
        print("The server is launching....")

    def test_create_user_with_gmail(self):
        u0_id = 000  # retrieved from google authentication
        u0_email = "aaabbb@gmail.com"
        user = UserService.create_user_with_gmail(u0_email, u0_id)

        self.assertEqual(user.user_id, u0_id)
        self.assertEqual(user.email, u0_email)
        self.assertTrue(user.third_party_login)

    def test_create_user_with_email_repeating_id(self):
        u1_id = 110  # retrieved from google authentication
        u1_email = "john@gmail.com"

        u2_id = 110  # retrieved from google authentication
        u2_email = "john2@gmail.com"

        user1 = UserService.create_user_with_gmail(u1_email, u1_id)

        self.assertEqual(user1.user_id, u1_id)
        self.assertEqual(user1.email, u1_email)
        
        self.assertFalse(UserService.create_user_with_gmail(u2_email, u2_id))
        

    def test_create_user_with_email_repeating_email(self):
        u1_id = 111  # retrieved from google authentication
        u1_email = "jack@gmail.com"

        u2_id = 112  # retrieved from google authentication
        u2_email = "jack@gmail.com"

        user1 = UserService.create_user_with_gmail(u1_email, u1_id)

        self.assertEqual(user1.user_id, u1_id)
        self.assertEqual(user1.email, u1_email)

        self.assertFalse(UserService.create_user_with_gmail(u2_email, u2_id))


    def test_create_user_with_email_invalid_email(self):
        # use something like 'not_a_real_email.com' as the email input

        u1_id = 113  # retrieved from google authentication
        u1_email = "peter@fake.com"

        self.assertFalse(UserService.create_user_with_gmail(u1_email, u1_id))


    def test_get_user_by_userId_exist(self):
        # check for an existing id
        u1_id = 114  # retrieved from google authentication
        u1_email = "elizabeth@gmail.com"

        user = UserService.create_user_with_gmail(u1_email, u1_id)

        returned_user = UserService.get_user_by_userId(user.user_id)

        self.assertEqual(returned_user.user_id, u1_id)
        self.assertEqual(returned_user.email, u1_email)
        

    def test_get_user_by_userId_not_exist(self):
        # check for a not existing id
        returned_user = UserService.get_user_by_userId(999)
        self.assertFalse(returned_user)


    def test_create_profile(self):
        # user_id, first_name, last_name, date_of_birth, gender
        u1_id = 115
        u1_email = "michaeljackson@gmail.com"
        u1_first_name = "michael"
        u1_last_name = "jackson"
        u1_date_of_birth = "2016-05-18"
        u1_gender = "male"

        user = UserService.create_user_with_gmail(u1_email, u1_id)
        user_profile = UserService.create_profile(u1_id, u1_first_name, u1_last_name, u1_date_of_birth, u1_gender)

        self.assertEqual(user_profile.user_id, u1_id)
        self.assertEqual(user_profile.first_name, u1_first_name)
        self.assertEqual(user_profile.last_name, u1_last_name)
        self.assertEqual(user_profile.date_of_birth, u1_date_of_birth)
        self.assertEqual(user_profile.gender, u1_gender)


    def test_create_profile_id_does_not_exist(self):
        # make sure the User object with user_id exist, then create profile
        user_profile = UserService.create_profile(999, 'ab', 'c', '2019-09-24', 'male')
        self.assertFalse(user_profile)
        

    def test_create_profile_repeating_id(self):
        # to prevent 2 profile instances with the same id
        u1_id = 116
        u1_email = "michaeljackson2@gmail.com"
        u1_first_name = "michael"
        u1_last_name = "jackson2"
        u1_date_of_birth = "2016-05-18"
        u1_gender = "male"

        u2_id = 116
        u2_email = "michaeljackson3@gmail.com"
        u2_first_name = "michael"
        u2_last_name = "jackson3"
        u2_date_of_birth = "2016-05-18"
        u2_gender = "male"

        user1 = UserService.create_user_with_gmail(u1_email, u1_id)
        user1_profile = UserService.create_profile(u1_id, u1_first_name, u1_last_name, u1_date_of_birth, u1_gender)

        self.assertEqual(user1_profile.user_id, u1_id)
        self.assertEqual(user1_profile.first_name, u1_first_name)
        self.assertEqual(user1_profile.last_name, u1_last_name)
        self.assertEqual(user1_profile.date_of_birth, u1_date_of_birth)
        self.assertEqual(user1_profile.gender, u1_gender)

        user2 = UserService.create_user_with_gmail(u2_email, u2_id)
        user2_profile = UserService.create_profile(u2_id, u2_first_name, u2_last_name, u2_date_of_birth, u2_gender)

        self.assertFalse(user2_profile)


    @classmethod
    def tearDownClass(cls):
        UserModel.User.drop_collection()
        UserModel.Profile.drop_collection()


if __name__ == "__main__":
    unittest.main()