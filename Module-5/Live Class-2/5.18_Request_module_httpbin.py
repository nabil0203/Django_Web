# 1:50:15
# https://eu.httpbin.org/



import requests


result = requests.get("https://eu.httpbin.org/get")
print(result.text)



"""
we will get a dictionary, which is basically a JSON
so the request we are sending is a API Request (REST API)
"""

