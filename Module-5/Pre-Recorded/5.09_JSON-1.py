# Convert Dictionary to JSON



import json

# Serialization: Python --> JSON

data = {
    "Name" : "Nabil",
    "age" : 30,
    "city" : "dhaka",
    "is_logged_in" : True,              # here-->True; output-->true
    "test" : None                       # here-->None; output-->null
} 

json_string = json.dumps(data, indent = 4)                          # indent used to show output organizedly
print(json_string)

