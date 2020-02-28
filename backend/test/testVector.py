# remember to set the working directory outside backend
# this test is used for vectors
from backend.algorithm.packer import PreferenceVector

if __name__ == "__main__":
    test_dict = {"RENA": 10, "REN": 12, "asd": 10}
    test_dict2 = {"RENA": 8, "REN": 11}
    test_dict3 = {"RENA": 8, "REN": 11, "RESA": 100}
    v = PreferenceVector.build_vector(test_dict)
    assert v == [12, 10]
    v2 = PreferenceVector.build_vector(test_dict2)
    v3 = PreferenceVector.build_vector(test_dict3)
    assert v2 - v == 5
    assert v3 - v2 == 10000