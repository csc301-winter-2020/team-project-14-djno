import unittest
from datetime import datetime
from config import *
from mongoengine import *
from service import UserService
from model import UserModel
from service import RequestService
from model import RequestModel
import json

# TODO: The tests need to be updated with respect to current models

print('IN THE FILE')


class TestRequestService(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        connect("david", host=HOST_IP, port=PORT,
                username=USERNAME, password=PASSWORD,
                authentication_source=AUTHENTICATION_SOURCE)
        print("connected")

        r1 = RequestModel.Request.objects(requester_email="fredarrow@gmail.com")
        r1.delete()

        r2 = RequestModel.Request.objects(requester_email="zohanthegreat@gmail.com")
        r2.delete()

        r3 = RequestModel.Request.objects(requester_email="humphreyboggart@gmail.com")
        r3.delete()

        r4 = RequestModel.Request.objects(requester_email="robinsoncrusoe@gmail.com")
        r4.delete()

        r5 = RequestModel.Request.objects(requester_email="georgeforeman@gmail.com")
        r5.delete()
        
        s1 = UserModel.UserSettings.objects(email="oliverwright@gmail.com")
        s1.delete()
        
        s2 = UserModel.UserSettings.objects(email="jimmycarter@gmail.com")
        s2.delete()

        s3 = UserModel.UserSettings.objects(email="susanblack@gmail.com")
        s3.delete()

        p1 = UserModel.Profile.objects(email="amadeusmotzart@gmail.com")
        p1.delete()

        p2 = UserModel.Profile.objects(email="fredarrow@gmail.com")
        p2.delete()
        
        p3 = UserModel.Profile.objects(email="henrytheeighth@gmail.com")
        p3.delete()

        var1a = "oliverwright@gmail.com"
        var1b = "jimmycarter@gmail.com"
        var1c = "susanblack@gmail.com"
        var2a = [-87.902445, 51.564919]
        var2b = [-87.902777, 51.564156]
        var2c = [-87.902655, 51.564655]
        var3 = True
        var4 = "dont know"

        UserModel.UserSettings(email=var1a, location=var2a, education_navigation=var3, education_support=var3, employment_navigation=var3, employment_support=var3, health_care_navigation=var3, health_care_support=var3, local_navigation=var3, local_support=var3, well_being_leisure=var3, pick_up_and_delivery=var3, pick_up_and_drop_off=var3, homemaking_supports=var3, request_type=var4).save()
        
        UserModel.UserSettings(email=var1b, location=var2b, education_navigation=var3, education_support=var3, employment_navigation=var3, employment_support=var3, health_care_navigation=var3, health_care_support=var3, local_navigation=var3, local_support=var3, well_being_leisure=var3, pick_up_and_delivery=var3, pick_up_and_drop_off=var3, homemaking_supports=var3, request_type=var4).save()
        
        UserModel.UserSettings(email=var1c, location=var2c, education_navigation=var3, education_support=var3, employment_navigation=var3, employment_support=var3, health_care_navigation=var3, health_care_support=var3, local_navigation=var3, local_support=var3, well_being_leisure=var3, pick_up_and_delivery=var3, pick_up_and_drop_off=var3, homemaking_supports=var3, request_type=var4).save()
        
    
    def test_get_all_user_preferences(self):
        allusers =  RequestService.get_all_user_preferences()
        
        allusers2 = [allusers[0].email, allusers[1].email, allusers[2].email, allusers[3].email, allusers[4].email, allusers[5].email]
        allusers2.sort()

        self.assertEqual(allusers2[0], "alexanderthegreat@gmail.com")
        self.assertEqual(allusers2[1], "alfredhitchcock@gmail.com")
        self.assertEqual(allusers2[2], "jimmycarter@gmail.com")
        self.assertEqual(allusers2[3], "leonidis@gmail.com")
        self.assertEqual(allusers2[4], "oliverwright@gmail.com")
        self.assertEqual(allusers2[5], "susanblack@gmail.com")
        
    def test_create_request(self):
        # for now create the request_id manually here

        UserModel.Profile(email="fredarrow@gmail.com", first_name="Fred", last_name="Arrow", date_of_birth="1960-01-01", age=60, gender="Male", image_url="abc", description="human being").save()
        
        desc = "I need to borrow a Macbook charger for 30 minutes"
        req1 =  RequestService.create_request(
            "fredarrow@gmail.com", ["OPC"], "Fred Arrow", desc, None, datetime.utcnow)

        self.assertEqual(req1.requester_email, "fredarrow@gmail.com")
        self.assertEqual(req1.request_type, ["OPC"])
        self.assertEqual(req1.name, "Fred Arrow")
        self.assertEqual(req1.description, desc)

    def test_accept_request(self):

        UserModel.Profile(email="henrytheeighth@gmail.com", first_name="Henry", last_name="Eighth", date_of_birth="1961-01-01", age=59, gender="Male", image_url="abc", description="from a movie").save()

        req2 = RequestModel.Request(requester_email="zohanthegreat@gmail.com", request_type=["OPC"], name="Zohan", description="i need audience", time_created=datetime.utcnow).save()

        req2a = RequestService.accept_request(acceptor_user="henrytheeighth@gmail.com", request=req2, time_accepted=datetime.utcnow)

        self.assertEqual(req2a.acceptor_email, "henrytheeighth@gmail.com")

    def test_isRegistered(self):

        UserModel.Profile(email="amadeusmotzart@gmail.com", first_name="Amadeus", last_name="Motzart", date_of_birth="1961-01-01", age=59, gender="Male", image_url="abc", description="Musician").save()

        reqaa = RequestService.isRegistered("amadeusmotzart@gmail.com")
#        reqab = RequestService.isRegistered("wolfgangmotzart@gmail.com")

        self.assertTrue(reqaa)
#        self.assertFalse(reqab)

    def test_get_request_by_email(self):

        RequestModel.Request(requester_email="humphreyboggart@gmail.com", request_type=["OPC"], name="Humphrey", description="need a movie role", time_created=datetime.utcnow).save()

        req3a = RequestService.get_request_by_email("humphreyboggart@gmail.com")
#        req3b = RequestService.get_request_by_email("florencenightingale@gmail.com")

        self.assertEqual(req3a.requester_email, "humphreyboggart@gmail.com")
#        self.assertIsNone(req3b)

    def test_cancel_request_by_email(self):

        RequestModel.Request(requester_email="robinsoncrusoe@gmail.com", request_type=["OPC"], name="Robinson", description="need a ship", time_created=datetime.utcnow).save()

        req4a = RequestService.cancel_request_by_email("robinsoncrusoe@gmail.com")
#        req4b = RequestService.cancel_request_by_email("swissfamilyrobinson@gmail.com")

        self.assertTrue(req4a)
#        self.assertFalse(req4b)

    def test_get_open_requests(self):

        listlen = RequestService.get_open_requests()

        self.assertEqual(len(listlen), 4)

    def test_complete_request(self):

        RequestModel.Request(requester_email="georgeforeman@gmail.com", request_type=["OPC"], name="George Foreman", description="need a fight", time_created=datetime.utcnow).save()

        req5a = RequestService.complete_request("georgeforeman@gmail.com", "muhammadali@gmail.com")

        req5b = RequestModel.Request.objects.get(requester_email = "georgeforeman@gmail.com")

        self.assertTrue(req5a)
        self.assertEqual(req5b.acceptor_email, "muhammadali@gmail.com")



    
    # todo: add any further tests you feel appropriate


        
    


if __name__ == "__main__":
    unittest.main()