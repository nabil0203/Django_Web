# Parameterzied constructor
# 'this' in java = 'self' in python



class Car:


    def __init__(self, brand, model):
        self.brand = brand                      # this.brand = brand
        self.model = model                      # this.brand = brand



car1 = Car("Honda", "Civic")                            # Object created and Valur passed
print(car1.brand, car1.model)



car2 = Car("Toyota", "Corolla")                         # Object created and Valur passed
print(car2.brand, car2.model)

