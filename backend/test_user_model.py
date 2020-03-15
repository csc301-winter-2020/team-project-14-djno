from model.UserModel import *
from config import *


connect("test", host=HOST_IP, port=PORT,
        username=USERNAME, password=PASSWORD,
        authentication_source=AUTHENTICATION_SOURCE)
print("connected")

# pref1 = Preferences(OPC=True, OQC=True, OQE=True)
# days1 = DayAvailability(Monday=True, Tuesday=True, Wednesday=True,
#                         Thursday=True, Friday=True, Saturday=True, Sunday=True)
# time1 = TimeAvailability(Morning=True, Afternoon=True,
#                          Evening=True, Night=True)

# Settings(email="chris@gmail.com",
#          GPS=True,
#          preferences=pref1,
#          days=days1,
#          time_of_day=time1,
#          ).save()

# pref1 = Preferences(OPC=True, OQC=False, OQE=False)
# days1 = DayAvailability(Monday=False, Tuesday=False, Wednesday=False,
#                         Thursday=False, Friday=False, Saturday=True, Sunday=True)
# time1 = TimeAvailability(Morning=False, Afternoon=False,
#                          Evening=True, Night=True)

# Settings(email="jane@gmail.com",
#          GPS=True,
#          preferences=pref1,
#          days=days1,
#          time_of_day=time1,
#          ).save()

# pref1 = Preferences(OPC=False, OQC=True, OQE=False)
# days1 = DayAvailability(Monday=True, Tuesday=False, Wednesday=True,
#                         Thursday=False, Friday=True, Saturday=True, Sunday=False)
# time1 = TimeAvailability(Morning=True, Afternoon=True,
#                          Evening=False, Night=False)

# Settings(email="julia@gmail.com",
#          GPS=False,
#          preferences=pref1,
#          days=days1,
#          time_of_day=time1,
#          ).save()

qSet = Settings.objects.filter_by_time("Morning")

for s in qSet:
    print(s.email)

print("done")
