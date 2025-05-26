# https://jsonplaceholder.typicode.com/



# POST request(created)


import requests

data = {'userId': 1, 'id': 1, 'title': 'testing'}

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)

print(response.status_code)                                                                     # ouput 201 means created