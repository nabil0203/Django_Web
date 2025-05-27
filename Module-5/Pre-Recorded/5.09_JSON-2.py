# https://www.geeksforgeeks.org/python-json/

# Convert JSON to Dictionary



import json

# Deserialization: JSON --> Python

data = '{ "Name" : "Nabil", "age" : 30, "city" : "dhaka", "is_logged_in" : true}'



python_dict = json.loads(data)                                  # json.loads() -->converts JSON into python
print(python_dict)