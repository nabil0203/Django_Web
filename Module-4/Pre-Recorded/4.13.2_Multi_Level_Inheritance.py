# Inherits One Another
# A B C ---> 3 Classes
# B inherits A class
# C inherits B class



class Grandfather:

    def __init__(self, color, first_name):
        self.color = color
        self.first_name = first_name


class Father(Grandfather):

    def __init__(self, hobby, color, first_name):
        super().__init__(color, first_name)                                 # Inheriting Grandfather
        self.hobby = hobby



class Children(Father):

    def __init__(self, fashion, hobby, color, first_name):
        super().__init__(hobby, color, first_name)                          # Inheriting Father ----->(As Father inherits Grandfather, therefore Ultimately Children is inheriting both Father & Grandfathe)
        self.fashion = fashion

    def info(self):
        print(self.first_name)
        print(self.color)
        print(self.fashion)
        print(self.hobby)



c1 = Children("styleish", "singing", "white", "rahman")
c1.info()
