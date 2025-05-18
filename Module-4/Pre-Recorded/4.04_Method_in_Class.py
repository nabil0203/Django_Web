class Car:


    def __init__(self, brand, model):                       # This is the constructor---> we need this constructor bcz "To receive the Arguments"
        self.brand = brand                                  # Assigns brand to the object
        self.model = model                                  # Assigns model to the object



    def display_details(self):                              # method
        print("Car brand: ",self.brand)
        print("Car Model: ",self.model)



car1 = Car("Honda", "Civic")                                 # Object created car1, Constructor called & passing Argumnents
car2 = Car("Toyota", "Corolla")                              # Object created car2, Constructor called & passing Argumnents


car1.display_details()
car2.display_details()