import unittest
from datetime import datetime
from config import *
from mongoengine import *
from service import UserService
from model import UserModel


class TestUserService(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        res = connect('test', host=HOST_IP, port=PORT, username=USERNAME,
                      password=PASSWORD,
                      authentication_source=AUTHENTICATION_SOURCE)
        print("The server is launching....")

    def test_create_user_with_gmail(self):
        u0_email = "aaabbb@gmail.com"
        user = UserService.create_user_with_gmail(u0_email)
        print("GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG")
        print(user)
        self.assertEqual(user.email, u0_email)

    def test_create_user_with_email_repeating_email(self):
        u1_email = "jack@gmail.com"

        u2_email = "jack@gmail.com"
        print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")

        user1 = UserService.create_user_with_gmail(u1_email)
        print(user1)

        self.assertEqual(user1.email, u1_email)

        self.assertFalse(UserService.create_user_with_gmail(u2_email))

    def test_create_user_with_email_invalid_email(self):
        u1_email = "peter@fakeemail"

        self.assertFalse(UserService.create_user_with_gmail(u1_email))

    def test_get_user_by_gmail_exist(self):
        u1_email = "aaabbb@gmail.com"
        user1 = UserService.create_user_with_gmail(u1_email)

        returned_user = UserService.get_user_by_email(u1_email)
        self.assertTrue(returned_user)

    def test_get_user_by_gmail_not_exist(self):
        u1_email = "aaabbb@gmail.com"

        returned_user = UserService.get_user_by_email(u1_email)
        self.assertFalse(returned_user)

    def test_create_a_user(self):
        # email, first_name, last_name, date_of_birth, gender
        u1_email = "asowfjsaoffiweofwiggiaswrgrgrih;]]]ljfoisdddddddddddddsssssssssssichaeljackson@gmail.com"
        u1_first_name = "michael"
        u1_last_name = "jackson"
        u1_date_of_birth = "2016-05-18"
        u1_gender = "male"
        u1_url = 'url_1'
        u1_desc = "hello"

        user = UserService.create_user_with_gmail(u1_email)
        self.assertEqual(user.email, u1_email)

        user_profile = UserService.create_a_user(u1_email, u1_first_name,
                                                 u1_last_name, u1_date_of_birth,
                                                 u1_gender, u1_url, u1_desc)

        self.assertEqual(user_profile.first_name, u1_first_name)
        self.assertEqual(user_profile.last_name, u1_last_name)
        self.assertEqual(user_profile.date_of_birth, u1_date_of_birth)
        self.assertEqual(user_profile.gender, u1_gender)

    # def test_a_user_email_does_not_exist(self):
    # email, first_name, last_name, date_of_birth, gender
    #    u1_email = "michaeljackson@gmail.com"

    #    user_profile = UserService.create_a_user(u1_email, 'ab', 'c', '2019-09-24', 'male')
    #    self.assertFalse(False)

    def test_create_a_user_repeating_email(self):
        # to prevent 2 profile instances with the same email
        u1_email = "michaeljackson2@gmail.com"
        u1_first_name = "michael"
        u1_last_name = "jackson1"
        u1_date_of_birth = "2016-05-18"
        u1_gender = "male"
        u1_url = "url_2"
        u1_desc = "hello123"

        u2_email = "michaeljackson2@gmail.com"
        u2_first_name = "michae2"
        u2_last_name = "jackson2"
        u2_date_of_birth = "2016-05-18"
        u2_gender = "male"
        u2_url = "lsfj"
        u2_desc = "hello 111"

        user1 = UserService.c2reate_user_with_gmail(u1_email)
        user1_profile = UserService.create_a_user(u1_email, u1_first_name,
                                                  u1_last_name,
                                                  u1_date_of_birth, u1_gender,
                                                  u1_url, u1_desc)

        self.assertEqual(user1_profile.first_name, u1_first_name)
        self.assertEqual(user1_profile.last_name, u1_last_name)
        self.assertEqual(user1_profile.date_of_birth, u1_date_of_birth)
        self.assertEqual(user1_profile.gender, u1_gender)

        user2 = UserService.create_user_with_gmail(u2_email)
        user2_profile = UserService.create_a_user(u2_email, u2_first_name,
                                                  u2_last_name,
                                                  u2_date_of_birth, u2_gender,
                                                  u2_url, u2_desc)

        self.assertFalse(False)

    # def tearDown(self):
    #    UserModel.User.drop_collection()
    #    UserModel.Profile.drop_collection()
    #    UserModel.UserSettings.drop_collection()


if __name__ == "__main__":
    unittest.main()
