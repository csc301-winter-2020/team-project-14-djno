from test.service.user_service_test import TestUserService
from test.service.request_service_test import TestRequestService

import unittest


class testService1(TestUserService):
    pass

class testService2(TestRequestService):
    pass

if __name__ == "__main__":
    unittest.main()
