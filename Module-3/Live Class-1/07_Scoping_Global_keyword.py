x = 5                   # global variable


def function_name():
    global x                        # turnig the x = 5 into x = 10
    x = 10
    print(x)


function_name()         # print 10
print(x)                # print 10



# after calling the funtion_name(), x = 5 turned into x = 10
# bcz, in the function_name(), we have used 'global'
# this changed the global x = 5 into x = 10
# ----> bairer variable funtion er vitore use kora hoy 'global' er maddhome
