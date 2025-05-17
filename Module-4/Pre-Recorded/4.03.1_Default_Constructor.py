# Default constructor
# 'this' in java = 'self' in python




class Car:


    def __init__(self):             # Constructor
        self.brand = ""
        self.model = ""
        
    


car1 = Car()                 # object created

car1.brand = "Toyota"
car1.model = "Corolla"
print(car1.brand, car1.model)