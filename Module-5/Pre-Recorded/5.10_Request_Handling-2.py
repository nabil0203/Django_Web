# https://jsonplaceholder.typicode.com/



# GET request


import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")

print(response)
print(response.json())