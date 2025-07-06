# 38:50


# import greet                                  # not importing the whole module


from greet import greetings                     # (1)-->just importing a specific method of the module
# greet.greetings("Nabillllll")                 # no need to write the module name
greetings("Nabillllll")



from car import start as st                     # (2)-->importing a specific method as a different name
st()                                            # method called of the module




import person as pr                             # (3)-->even we can import the module with a differnt name
pr.habit()

