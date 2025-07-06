
from datetime import datetime, timedelta


now = datetime.today()                                              # real time
new_time = now + timedelta(hours = 5, minutes = 40)                 # real time + 5 hours 40 mins

print("The time is -->", now)
print("New time is -->", new_time)

