# 51:30
# 'strftime'
# 'strptime'



from datetime import datetime



now = datetime.now()
print(now.strftime("%H:%m"))                                    # time to string




text = "02/03/2001"
a = datetime.strptime(text, "%d/%m/%Y")                         # string to time
print(a)
