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
        pass

    def test_create_user_with_email_repeating_email(self):
        pass

    def test_create_user_with_email_invalid_email(self):
        # use something like 'not_a_real_email.com' as the email input
        pass

    def test_get_user_by_userId_exist(self):
        # check for an existing id
        pass

    def test_get_user_by_userId_not_exist(self):
        # check for a not existing id
        pass

    def test_create_profile(self):
        pass

    def test_create_profile_id_does_not_exist(self):
        # make sure the User object with user_id exist, then create profile
        pass

    def test_create_profile_repeating_id(self):
        # to prevent 2 profile instances with the same id
        pass


    @classmethod
    def tearDownClass(cls):
        UserModel.User.drop_collection()
        UserModel.Profile.drop_collection()


if __name__ == "__main__":
    unittest.main()