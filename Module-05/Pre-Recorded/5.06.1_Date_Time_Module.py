import datetime


now = datetime.datetime.now()                               # shows real time (year-month-day hour:min:sec:microsec)
print("Date & Time:", now)


todays_date = datetime.date.today()                         # shows only today's date
print("Today is:", todays_date)


real_time = datetime.datetime.now().time()                  # shows only time
print("Time is:", real_time)

