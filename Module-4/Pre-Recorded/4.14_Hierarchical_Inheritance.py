# Multiple Class inherits one same class
# A B C ---> 3 Classes
# B inherits A class
# C inherits A class



class Vehicle:

    def engine_type(self):
        print("Vehicle has an engine")


class Car(Vehicle):                                              # Car inherits Vechicles

    def num_doors(self):
        print("Car has 4 doors")


class Truck(Vehicle):                                            # Truck inherits Vechicles

    def load_capacity(self):
        print("load capacity is 10 tons")



car = Car()
car.engine_type()
car.num_doors()

truck = Truck()
truck.engine_type()
truck.load_capacity()
