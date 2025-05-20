# One class Inherits Another Class
# A class inherits B class

class Grandfather:

    def __init__(self, color, first_name):
        self.color = color
        self.first_name = first_name


class Father(Grandfather):

    def __init__(self, hobby, color, first_name):
        super().__init__(color, first_name)                         # super() used to define the constructor of the parent class; this inherits from Grandfather
        self.hobby = hobby                                          # own feature of Father



g_father = Grandfather("Red", "Chowdhury")

father1 = Father("Cricket", "Black", "Chowdhury" )

print(father1.color)
print(father1.hobby)
print(father1.first_name)

