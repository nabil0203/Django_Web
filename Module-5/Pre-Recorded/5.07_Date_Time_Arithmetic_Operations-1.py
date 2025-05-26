
from datetime import datetime, timedelta                            # only imported 'datetime' and 'timedelta' module


today = datetime.today().date()                                     # today
tommorow = today + timedelta(days = 1)                              # today + 1 day = tomorrow
yesterday = today - timedelta(days = 1)                             # today - 1 day = yesterday


print("Today-->", today)
print("Tomorrow-->", tommorow)
print("Yesterday-->", yesterday)