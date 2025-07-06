# 2:22
# A functionality of a Function
# does't return date directly
# it returns date periodically




# this is a normal function
# here the values of the list are returning all of them at once

# def normal_function():
#     numbers = [0, 1, 2, 3, 4, 5]
#     return numbers

# for value in normal_function():
#     print(value)





# this is a generator
# here the values of the list are returning(yield) all of them ONE BY ONE
# yeild is the keyword which is returning the values ONE BY ONE

def generator_example():
    numbers = [0, 1, 2, 3, 4, 5]
    for num in numbers:
        yield num

for value in generator_example():
    print(value)