# https://www.geeksforgeeks.org/python-json/

# Convert Dictionary to JSON



import json

# Serialization: Python --> JSON

data = {
    "Name" : "Nabil",
    "age" : 30,
    "city" : "dhaka",
    "is_logged_in" : True,              # output--> true
    "test" : None                       # output--> null
} 

json_string = json.dumps(data, indent = 4)                          # json.dumps() -->converts python into JSON
print(json_string)                                                  # indent used to show output organizedly

