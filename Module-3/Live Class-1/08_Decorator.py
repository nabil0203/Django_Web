# 1:49
# A function that modifies another funtion's behaviour without changing its code
# Pass a 'function' as a parameter
# kono funtion call korar age/pore sob smy kono kaj korte hoile decorator use hoy




def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper


@my_decorator
def say_hello():
    print("Ami Nabil")



say_hello()




# say hello()--> called
# at first, python checks if say_hello() has any decorator or not
# there is a decorator function 'my_decorator()'
# it is mentioned by '@'
# at first the decorator function will be called not the 'say_hello()'
# 'my_decorator()' will take 'say_hello()' as a parameter 'func'
# inside the 'my_decorator()', there is a 'wrapper()' funtion
# the 'wrapper()' will be executed
# inside wrapper(), some a line is printed------->Before function call
# then the 'say_hello()' is called through the parameter 'func()'
# so it prints------->Ami Nabil
# then another line of wrapper printed------->After function call