# JSON to Python


import json


data = '{ 
  "Name" : "Nabil", 
  "age" : 30, 
  "city" : "dhaka", 
  "is_logged_in" : true
}'


text = json.loads(data)

print(type(text))
