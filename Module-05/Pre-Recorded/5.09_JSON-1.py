# https://www.geeksforgeeks.org/python-json/

# Convert Dictionary to JSON

# Serialization: Python --> JSON
# dumps() - method used


import json


data = {
    "Name" : "Nabil",
    "age" : 30,
    "city" : "dhaka",
    "is_logged_in" : True,              # output--> true
    "test" : None                       # output--> null
} 

json_string = json.dumps(data)                          # json.dumps() -->converts python into JSON
print(json_string)
