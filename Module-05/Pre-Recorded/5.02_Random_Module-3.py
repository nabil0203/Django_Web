# generate random 4 digit pin


import random


def generate_pin():
    return random.randint(1000,9999)                        # provides a 4 digit int value --> between (1000-9999)

print("Your pin is: ", generate_pin())
