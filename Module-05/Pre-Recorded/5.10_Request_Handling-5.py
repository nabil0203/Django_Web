# https://jsonplaceholder.typicode.com/
# https://www.geeksforgeeks.org/python-requests-tutorial/


# DELETE request


import requests

# data = {'userId': 1, 'id': 1, 'title': 'testing(updated)'}

response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")                              # dhange----> /1 (which number is told)

print(response.status_code)