# class is a buleprint

class Vehicle:
    wheels = 4
    engine = "Diesel Engine"

    def func_name(self):
        print("Inside class Function")

    def engine_start(self):
        print("Starting the Engine.....")



car1 = Vehicle()                                # 'car1' is an object of 'Vehicle' class
# Vehicle car1 = New Vehicle();                 # java oject declare


print(car1.wheels)
print(car1.engine)


car1.func_name()
car1.engine_start()
