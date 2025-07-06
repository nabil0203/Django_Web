class Person:
    
    # varibale pass like parameter
    def __init__(self, name):
        self.name = name
        self.gender = "Male"

    def greet(self):
        print("Hello!")



p1 = Person("Alex")             # object
p2 = Person("John")             # object


print(p1.name)
print(p1.gender)

