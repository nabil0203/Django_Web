

import requests


result = requests.get("https://eu.httpbin.org/get")             # get()---> requesting
print(result.text)




import json

data = json.loads(result.text)                                  # loads()----> to see in python           
print(data)
print(type(data))
print(data["headers"])                                          # only 'headers' dictionary



