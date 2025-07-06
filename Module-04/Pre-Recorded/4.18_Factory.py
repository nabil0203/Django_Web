# 

class Car:
    def driver(self):
        return "Diving a car"

class Bike:
    def driver(self):
        return "Riding a bike"
    
    

class Veichle_Factory:

    @staticmethod
    def get_vhicle(type):

        if type == "car":
             return Car()
        elif type == "bike":
            return Bike()
        else:
            return ValueError("Invalid option")
        


v1 = Veichle_Factory.get_vhicle("bike")                         # change between car & bike
print(v1.driver())
    