import unittest
from mongoengine import *
from application import  *


class TestRoutes(unittest.TestCase):

    @classmethod
    def setUpClass(self) -> None:
        res = connect('david', host=HOST_IP, port=PORT, username=USERNAME, password=PASSWORD,
                      authentication_source=AUTHENTICATION_SOURCE)

        print("The server is launching....")


    def test_hello_world(self):
        response = app.test_client().get('/')

        assert response.status_code == 200

    def test_login_verify(self):
        response = app.test_client().get('/login')

        assert response.status_code == 200

    def test_signout(self):
        response = app.test_client().get('/signout')

        assert response.status_code == 200


    def test_user(self):
        response = app.test_client().get('/user')

        assert response.status_code == 200


    def test_create_profile(self):
        response = app.test_client().get('/user/profile/create')

        assert response.status_code == 200

    def test_update_profile(self):
        response = app.test_client().get('/user/profile/update')

        assert response.status_code == 200

    def test_settings(self):
        response = app.test_client().get('/user/settings')

        assert response.status_code == 200

    def test_create_settings(self):
        response = app.test_client().get('/user/settings/create')

        assert response.status_code == 200


    def test_update_settings(self):
        response = app.test_client().get('/user/settings/update')

        assert response.status_code == 200


    def test_request(self):
        response = app.test_client().get('/user/request')

        assert response.status_code == 200

    def test_get_user(self):
        response = app.test_client().get('/user/<"randomnaleesin@gmail.com">')

        assert response.status_code == 200

    def test_get_user_profile(self):
        response = app.test_client().get('/user/profile/<"randomnaleesin@gmail.com">')

        assert response.status_code == 200

    def test_get_user_settings(self):
        response = app.test_client().get('/user/settings/<"randomnaleesin@gmail.com">')

        assert response.status_code == 200


    def test_preference_match(self):
        response = app.test_client().get('/match')

        assert response.status_code == 200


    def test_new_match(self):
        response = app.test_client().get('/new_match')

        assert response.status_code == 200


if __name__ == "__main__":
    unittest.main()
