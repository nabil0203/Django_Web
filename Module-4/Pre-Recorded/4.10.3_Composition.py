# Composition
# Can't exist without one another
# Engine, Car


class Engine:
    def __init__(self, power):
        self.power = power


class Car:
    def __init__(self, brand, power):
        self.brand = brand
        self.engine = Engine(power)                             # directly creating an Object of 'Engine' class in 'self.engine'
                                                                # gari bananor sathe sathei ekta engine assign hoye jabe

    def show_details(self):
        print(f"{self.brand} has an Engine with {self.engine.power} HP")




# no object needed for 'Engine' class bcz already created in Car class

car1 = Car("Toyota", 950)

car1.show_details()
