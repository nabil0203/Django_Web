import random


print(random.random())                       # provides a float value between (0-1)
print(random.uniform(5,10))                  # provides a float value between (5-10)
print(random.uniform(55,60))                 # provides a float value between (55-60)
print(random.randint(3,40))                  # provides an int value between (3-40)
print(random.randint(1,1000))                # provides an int value between (1-1000)



                    
fruits = ["apple", "banana", "mango", "cherry"]
print(random.choice(fruits))                                # provides random elements from a list

random.shuffle(fruits)                                      # Shuffles the whole list
print(fruits)


