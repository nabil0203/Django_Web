from datetime import datetime, timedelta


now = datetime.now()
print(now)


tomorrow = now + timedelta(days=1)
print(tomorrow)
