# Default Value constructor
# 'this' in java = 'self' in python





class Car:


    def __init__(self, brand = "Honda", model = "Civic"):
        self.brand = brand                                           # this.brand = brand
        self.model = model                                           # this.brand = brand



car1 = Car()                                             # Object created but value already declared
print(car1.brand, car1.model)



car2 = Car("Toyota", "Corolla")                         # Object created and Value passed
print(car2.brand, car2.model)

