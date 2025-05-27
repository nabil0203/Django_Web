# https://jsonplaceholder.typicode.com/
# https://www.geeksforgeeks.org/python-requests-tutorial/


# GET request
# GET method is used to retrieve information from the given server using a given URL.


import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")

print(response)
print(response.json())