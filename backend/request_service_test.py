import unittest
from datetime import datetime
from config import *
from mongoengine import *
from UserService import *
from model.UserModel import User, Settings, Profile
#from model import UserModel
from RequestService import *
from model.RequestModel import Request
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

    
    
#    def setUp(self) -> None:
        # add some users with profile and preferences here
        
        User.drop_collection()
        Profile.drop_collection()
        Request.drop_collection()
        Settings.drop_collection()
        
        
        
        u1 = create_user("fred@gmail.com", [43.653117, -79.383192])
        u2 = create_user("sean@gmail.com", [51.561482, -87.906550])
        u3 = create_user("nathan@gmail.com", [51.561482, -87.906550])
        u4 = create_user("chris@gmail.com", [43.653225, -79.383186])

        p1 = create_profile(
            "fred@gmail.com", "Fred", "Arrow", "1990-11-18", 30, "Male", "Toronto", "url_1")
        p2 = create_profile(
            "sean@gmail.com", "Sean", "Penn", "2001-08-10", 18, "Male", "Fort Hope", "url_1")
        p3 = create_profile(
            "nathan@gmail.com", "Nathan", "Grove", "1996-01-05", 24, "Male", "Toronto", "url_1")
        p4 = create_profile(
            'chris@gmail.com', 'Chris', 'Jones', '1995-05-22', 25, 'Male', 'Toronto', 'url_1')
        
        
        s1 = create_settings(
            "fred@gmail.com", True, ["OPC", "OQC", "OQE"], days, time_of_day)
        s2 = create_settings(
            "sean@gmail.com", True, ["OQC"], ["Monday"], ["Evening"])
        s3 = create_settings(
            "nathan@gmail.com", True, ["OPC", "OQC"], ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], ["Morning", "Afternoon", "Evening"])
        s4 = create_settings(
            'chris@gmail.com', True, ["OPC", "OQC", "OQE"], days, time_of_day)
        

        u1.profile = p1
        u1.settings = s1
        u1.save()

        u2.profile = p2
        u2.settings = s2
        u2.save()
        
        u3.profile = p3
        u3.settings = s3
        u3.save()

        u4.profile = p4
        u4.settings = s4
        u4.save()
        
        
        r1 = Request(requestor_email = "abcdefg@gmail.com", title = "ABCDEFG", point = [-89.252003, 48.392225], 
                    time_of_request = datetime(2020, 3, 28, 21), request_type = "RWL", description = "Hello").save()

#        UserService.update_user_settings({
#            "email": "jane@gmail.com",
#            "education_navigation": ["OPC"],
#            "health_care_support": ["OPC", "OQC", "OQE"],
#            "well_being_leisure": ["OQC"]
#        })
#        UserService.update_user_settings({
#            "email": "mike@gmail.com",
#            "education_support": ["OPC", "OQC", "OQE"],
#            "employment_support": ["OPC", "OQC"],
#            "local_support": ["OPC", "OQC"],
#            "pick_up_and_drop_off": ["OPC", "OQC", "OQE"],
#            "homemaking_supports": ["OQC"]
#        })

    def test_create_request(self):
        # for now create the request_id manually here
        desc = "I need to borrow a Macbook charger for 30 minutes"
        req1 = create_request(
            "fred@gmail.com", "Fred Arrow", [43.653117, -79.383192], datetime(2020, 3, 28, 21), "RHMS", desc)

        self.assertEqual(req1.requestor_email, "fred@gmail.com")
        self.assertEqual(req1.request_type, "RHMS")
        self.assertEqual(req1.title, "Fred Arrow")
        self.assertEqual(req1.description, desc)



    def test_create_request_2(self):
        # for now create the request_id manually here
        desc2 = "I need someone to talk to"
        req2 = create_request(
            "sean@gmail.com", "Sean Penn", [51.561482, -87.906550], datetime(2020, 3, 30, 19), "RWL", desc2)

        self.assertEqual(req2.requestor_email, "sean@gmail.com")
        self.assertEqual(req2.request_type, "RWL")
        self.assertEqual(req2.title, "Sean Penn")
        self.assertEqual(req2.description, desc2)

 
    def test_create_request_3(self):
        # for now create the request_id manually here
        desc3 = "I would like to initiate a chat with someone"
        req3 = create_request(
            "nathan@gmail.com", "Nathan Grove", [43.655878, -79.380382], datetime(2020, 3, 27, 11), "RWL", desc3)

        self.assertEqual(req3.requestor_email, "nathan@gmail.com")
        self.assertEqual(req3.request_type, "RWL")
        self.assertEqual(req3.title, "Nathan Grove")
        self.assertEqual(req3.description, desc3)
        

    def test_accept_request1(self):

        request = get_requests_by_email('"fred@gmail.com"')
        self.assertEqual(request.status, "POSTED")

        accept_request(acceptor_user="chris@gmail.com", request=request)
        self.assertEqual(request.status, "PENDING")
        self.assertEqual(request.acceptor_email, "chris@gmail.com")


    def test_accept_request2(self):

        request = get_requests_by_email("sean@gmail.com")
        self.assertEqual(request.status, "POSTED")

        accept_request(acceptor_user="chris@gmail.com", request=request)
        self.assertEqual(request.status, "PENDING")
        self.assertEqual(request.acceptor_email, "chris@gmail.com")


    def test_accept_request3(self):
        
        request = get_requests_by_email("nathan@gmail.com")

        self.assertEqual(request.status, "POSTED")
        accept_request(acceptor_user="chris@gmail.com", request=request)
        self.assertEqual(request.status, "PENDING")
        self.assertEqual(request.acceptor_email, "chris@gmail.com")


    def test_isRegistered1(self):
        checkuser = isRegistered("fred@gmail.com")

        self.assertEqual(checkuser, True)

    def test_isRegistered2(self):
        checkuser = isRegistered("sean@gmail.com")

        self.assertEqual(checkuser, True)

    def test_isRegistered3(self):
        checkuser = isRegistered("nathan@gmail.com")

        self.assertEqual(checkuser, True)

    def test_get_all_user_preferences(self):
        allusers = get_all_user_preferences()
        firstuserpref = len(allusers[0].preferences)
        seconduserpref = len(allusers[1].preferences)
        thirduserpref = len(allusers[2].preferences)

        self.assertTrue(firstuserpref>0)
        self.assertTrue(seconduserpref>0)
        self.assertTrue(thirduserpref>0)

    
    # todo: add any further tests you feel appropriate


        
    


if __name__ == "__main__":
    unittest.main()
