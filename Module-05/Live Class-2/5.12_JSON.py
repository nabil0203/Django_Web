# python to JSON
# dumps() -used


import json


data = {
    "a" : 5,
    "b" : True,
    "c" : "Nabil",
}


text = json.dumps(data)

print(repr(text))                   # output----> '{.......}' 
                                    # single quotation indicates it's a JSON
