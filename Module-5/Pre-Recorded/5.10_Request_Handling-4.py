# https://jsonplaceholder.typicode.com/
# https://www.geeksforgeeks.org/python-requests-tutorial/



# UPDATE request
# PUT request


import requests

data = {'userId': 1, 'id': 1, 'title': 'testing(updated)'}

response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=data)                              # dhange----> posts/1 (which number is told)

print(response.status_code)                                                                        # ouput 200 means success