# remember to set the working directory outside backend
# this test is used for vectors
from backend.algorithm.packer import PreferenceVector

if __name__ == "__main__":
    test_dict = {"RENA": "OPC", "REN": "OQE", "asd": "OQC"}
    test_dict2 = {"RENA": 8, "REN": 11}
    test_dict3 = {"RESA": 8, "REN": 11, "RENA": 100}
    v = PreferenceVector.build_vector(test_dict)
    assert v.count_approach({"OPC"}) == 1