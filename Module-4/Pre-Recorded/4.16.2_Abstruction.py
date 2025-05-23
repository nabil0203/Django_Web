# Hide the inside Implementation


#importing the method to abstruct
from abc import ABC,abstractmethod


class Shape(ABC):
    def __init__(self,dm1,dm2):
        self.dm1 = dm1
        self.dm2 = dm2

    @abstractmethod                                   # abstruct method
    def area(self): 
        pass


class Triangle(Shape):
    def area(self):                                  # must override this 'area' method
        area = 0.5 * self.dm1 * self.dm2
        print("area of triangle:",area)


class Rectangle(Shape):
    def area(self):
        area = self.dm1 * self.dm2
        print("area of rectangle:",area)


# if we try to create an object of shape class it will throw error
# we cannot create any object of an abstruct class

s1 = Shape(10,20)
s1.area()

tri = Triangle(5,6)
rec = Rectangle(6,7)
tri.area()
rec.area()