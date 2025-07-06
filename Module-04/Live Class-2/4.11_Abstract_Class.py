# 1:57:00


# Just a hint what to built
# kisu ekta bananor jonne force kore dibe
# kono class ke baddho kore dite chai je, ei property/function ta lekhtei hobe



from abc import ABC, abstractmethod


class Shape(ABC):                                   # Abstruct Class
    @abstractmethod
    def area(self):                                 # area method
        pass


class Circle(Shape):
    def area(self):                                 # area method thaktei hobe, bcz Shape inherited & Shape is an Abstrct Class
        print("Area of a Circle")


class Square(Shape):
    def area(self):                                 # area method thaktei hobe, bcz Shape inherited & Shape is an Abstrct Class
        print("Area of a Square")




# s1 = Shape()                                      # Abstruct class er object directly banano jay na

c1 = Circle()
c1.area()