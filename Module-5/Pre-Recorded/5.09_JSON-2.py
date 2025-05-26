# Convert JSON to Dictionary



import json

# Deserialization: JSON --> Python

data = '{ "Name" : "Nabil", "age" : 30, "city" : "dhaka", "is_logged_in" : true}'

python_dict = json.loads(data)
print(python_dict)