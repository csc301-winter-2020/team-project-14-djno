# database constants
DATABASE_NAME = 'mytest'
HOST_IP = '159.203.53.245'
PORT = 27017
USERNAME = 'admin'
PASSWORD = 'admin123'
AUTHENTICATION_SOURCE = 'admin'

# User
USER_NUMBER = 0

# Request
REQUEST_NUMBER = 0
REQUEST_STATUS = ["POSTED", "PENDING", "COMPLETED", "CANCELLED"]

p_rules = ["OPC", "OQC", "OQE"]
# valid attributes for a word vector
d_rules = ["REN", "RES", "RENA", "RESA",
           "RHN", "RHS", "RLN", "RLS",
           "RWL", "RPUD", "RPUO", "RHMS"]

a_maps = {
    "education_navigation": "REN",
    "education_support": "RES",
    "employment_navigation": "RENA",
    "employment_support": "RESA",
    "health_care_navigation": "RHN",
    "health_care_support": "RHS",
    "local_navigation": "RLN",
    "local_support": "RLS",
    "well_being_leisure": "RWL",
    "pick_up_and_delivery": "RPUD",
    "pick_up_and_drop_off": "RPUO",
    "homemaking_supports": "RHMS"
}

service_to_pref = {
    "REN": "OPC",
    "RENA": "OPC",
    "RHN": "OPC",
    "RLN": "OPC",
    "RES": "OQC",
    "RESA": "OQC",
    "RHS": "OQC",
    "RLS": "OQC",
    "RWL": "OQC",
    "RPUD": "OQE",
    "RPUO": "OQE",
    "RHMS": "OQE"
}

CLIENT_ID = "725608313090-l8vr2u5rc91jv9acqogiase3ioctkv02.apps.googleusercontent.com"
CLIENT_SECRET = "865katckHYM9Db2gcQ652k-T"
SECRET_KEY = b'_5y2"F4Q8z\n\xec]/'

APP_PAGE = ["index.html", "profile.html",
            "matching.html", "profile-deprecated.html",
            "make-a-reuest-deprecated.html",
            "setting-deprecated.html"]
# category for automatical matching
sub_category = {
    "OPC": ["REN", "RENA", "RHN", "RLN"],
    "OQC": ["RES", "RESA", "RHS", "RLS", "RWL"],
    "OQE": ["RPUD", "RPUO", "RHMS"]
}
