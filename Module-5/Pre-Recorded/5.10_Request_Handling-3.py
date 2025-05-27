# https://jsonplaceholder.typicode.com/
# https://www.geeksforgeeks.org/python-requests-tutorial/



# POST request(created)
# POST request method requests that a web server accepts the data enclosed in the body of the request message, most likely for storing it


import requests

data = {'userId': 1, 'id': 1, 'title': 'testing'}

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)

print(response.status_code)                                                                     # ouput 201 means created