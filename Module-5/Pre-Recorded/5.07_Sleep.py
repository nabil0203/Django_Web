
import time
from datetime import datetime


start = datetime.now()
time.sleep(5)                           # delaying 5 sec
end = datetime.now()


print(end - start)