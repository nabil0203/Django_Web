# 'strftime' - used
# https://www.geeksforgeeks.org/python-strftime-function/


import datetime


now = datetime.datetime.now()                # took variable to use it below


# formatting date time by my own format

format_date_1 = now.strftime("%d~%m~%y")                         # %y--->shows year 2 digits 
format_date_2 = now.strftime("%d~%m~%Y")                         # %Y--->shows year 4 digits 
format_date_3 = now.strftime("%d~%B~%Y")                         # %B--->shows month in words 
format_date_4 = now.strftime("%d~%b~%Y")                         # %b--->shows month in words but short (February-->feb)
format_date_5 = now.strftime("%d~%b~%Y~%A")                      # %A--->shows the day
format_date_6 = now.strftime("%d~%b~%Y~%a")                      # %a--->shows the day but short(Monday-->Mon)

print("Custom date format-1:", format_date_1)
print("Custom date format-2:", format_date_2)
print("Custom date format-3:", format_date_3)
print("Custom date format-4:", format_date_4)
print("Custom date format-5:", format_date_5)
print("Custom date format-6:", format_date_6)




print("--------------------------------------------")





# formatting time time by my own format

format_time_1 = now.strftime("%H~%M~%S")                         # %H--->shows 24 hours format
format_time_2 = now.strftime("%I~%M~%S")                         # %I--->shows 12 hours format
format_time_3 = now.strftime("%I~%M~%S-%p")                      # %p--->shows am/pm

print("Custom time format-1:", format_time_1)
print("Custom time format-2:", format_time_2)
print("Custom time format-3:", format_time_3)

