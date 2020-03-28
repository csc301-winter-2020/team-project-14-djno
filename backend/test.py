#from service.user_service_test import TestUserService
#from service.request_service_test import TestRequestService
#from algorithm.new_algo_test1 import TestNewAlgo

from test.service.user_service_test import TestUserService
from test.service.request_service_test import TestRequestService
from test.algorithm.new_algo_test1 import TestNewAlgo
import unittest

import unittest

class testService(TestUserService):

    pass

class testService(TestRequestService):

    pass

class testService(TestNewAlgo):

    pass 


if __name__ == "__main__":
    unittest.main()