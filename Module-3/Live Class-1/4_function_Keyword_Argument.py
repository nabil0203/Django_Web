# 1:10
# keyword argument
# Doesn't need to maintain the serial while passing argument
# how to write----> parameter = argument



def greetings(name, age):
    print("------------")
    print("Welcome to our home", name)
    print("Comfort yourself")
    print("I am", age, "years old")



greetings(age = 30, name = "Nabil")                             # keyword argument (no serial is maintained)
greetings("Kola", 100)
greetings("Mango", 665)
