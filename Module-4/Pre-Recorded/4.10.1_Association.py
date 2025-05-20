# Association
# Multiple Class can exist without depending on each other
# here if we delete Laptop, then Student class will stay as it is


class Laptop:
    def __init__(self, brand):
        self.brand = brand



class Student:
    def __init__(self, name, laptop_obj):
        self.name = name
        self.laptop = laptop_obj

    def show_laptop_info(self):
        print(f"{self.name} has a {self.laptop.brand} Laptop")               # 'self.laptop.brand' ---> accessing the Brand of Laptop class from Student class
        



lp1 = Laptop("Asus")
st1 = Student("Rahim", lp1)                      # passing the Object 'lp1'

st1.show_laptop_info()