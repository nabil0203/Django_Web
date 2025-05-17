# Create a Car class
# Create some Objects of Car


class Car:
    
    def __init__(self):                     # self method indicates the object of the class 'Car' (Constructor)
        self.brand = ""
        self.model = ""
        print("Object Created......")
        print("Constructor called Automatically.....")




car1 = Car()                 # object-1
car1.brand = "Toyota"
car1.model = "Corolla"
print(car1.brand, car1.model)




car2 = Car()                 # object-2
car2.brand = "Honda"
car2.model = "Civic"
print(car2.brand, car2.model)

