# check Pre-recorded --> 5.10
# to ger e clear concept



import requests

response = requests.get("https://api.github.com")               # get() - method is used to hit/extract data from a url

print(response.json())                                          # json is uesd is to show the output only