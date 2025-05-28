# 38:50


# import greet                                  # not importing the whole module


from greet import greetings                     # just importing a specific method of the module
# greet.greetings("Nabillllll")                 # no need to write the module name
greetings("Nabillllll")



from car import start as st                     # importing a specific method as a different name
st()                                            # method called of the module




import person as pr                             # even we can import the module with a differnt name
pr.habit()

