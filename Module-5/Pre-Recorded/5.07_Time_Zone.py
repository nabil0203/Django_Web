
import pytz

from datetime import datetime, UTC


dhaka = pytz.timezone('Asia/Dhaka')
utc = datetime.now(UTC)


print(dhaka)                                        # Dhaka timezone(didn't understand clearly)
print(utc.astimezone(dhaka))                        # Time of Dhaka
print(utc)                                          # time of UTC

print(pytz.all_timezones)                         # shows a list of all timezone