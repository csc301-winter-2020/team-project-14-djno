# remember to set the working directory outside backend
# this test is used for vectors
from algorithm.packer import PreferenceVector
import algorithm.util as util
import json

if __name__ == "__main__":
    test_dict = {"RENA": ["OPC"], "REN": ["OQE"], "asd": ["OQC"]}
    test_dict2 = {"RENA": ["OPC", "OPC"], "REN": ["OPC"], "asd": ["OPC"]}
    test_dict3 = {"RESA": 8, "REN": 11, "RENA": 100}
    v1 = PreferenceVector.build_vector(test_dict)
    v2 = PreferenceVector.build_vector(test_dict2)
    print(v1.count_approach({"OPC"}))
    print(v2.count_approach({"OPC"}))
    # v2 = PreferenceVector.build_vector(test_dict2)
    # v3 = PreferenceVector.build_vector(test_dict3)
    # assert v2 - v == 5
    # assert v3 - v == 8165
    import model.UserModel as model

    tObj = model.UserSettings(email="sadasd", education_navigation=["OPC"])
    tObj1 = model.UserSettings(email="adw", education_navigation=["OPC", "OQC"],
                               education_support=["OPC"])
    tt = [tObj, tObj1]
    r = util.sort_pref(tt, {"OPC"})
    assert r[0] == (
    {'REN': ['OPC', 'OQC'], 'RES': ['OPC'], 'RENA': [], 'RESA': [], 'RHN': [],
     'RHS': [], 'RLN': [], 'RLS': [], 'RWL': [], 'RPUD': [], 'RPUO': [],
     'RHMS': []}, {'email': 'adw'})
