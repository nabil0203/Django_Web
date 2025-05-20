# One class directly innherits multiple Classes
# A B C ---> 3 Classes
# C inherits A class
# C inherits B class


class Grandfather:

    def __init__(self, color, first_name):
        self.color = color
        self.first_name = first_name




class Father:

    def __init__(self, hobby):
#       super().__init__(color, first_name)                                      # doesn't Inherited from Grandfather
        self.hobby = hobby




class Children(Father, Grandfather):

    def __init__(self, fashion ,hobby, color, first_name):

        Father.__init__(self, hobby)                                            # Directly Inherits Feature of Grandfather
        Grandfather.__init__(self, color, first_name)                           # Directly Inherits Features of Father
        self.fashion = fashion                                                  # Own features of Child
        



child1 = Children("Young FASHION","Badminton", "Red", "Chowdhury" )



print(child1.fashion)
print(child1.color)
print(child1.first_name)

