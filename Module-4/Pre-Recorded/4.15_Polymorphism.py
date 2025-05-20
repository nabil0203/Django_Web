# Polymorphism
# Method Overridding (Different Inherited class, Same Method)
# Method Overloading (Python doesn't support Overloading as Java/C++)




# Overridding
class GrandFather:
    def greet(self):
        print("GrandFather greets")


class Father(GrandFather):
    def greet(self):                                    # overriding
        print("Father greets")


class Children(Father):
    def greet(self):                                    # overriding
        print("Child greets")



gf = GrandFather()
f = Father()
c = Children()


gf.greet()
f.greet()
c.greet()






# Overloading
# Python doesn't support true method overloading like Java/C++. You can simulate it using default arguments or *args / **kwargs.


class Shape:
    def area(self, a, b=109):
        return a * b


p = Shape()
print(p.area(5))         # Output: 545
print(p.area(5, 10))     # Output: 50
