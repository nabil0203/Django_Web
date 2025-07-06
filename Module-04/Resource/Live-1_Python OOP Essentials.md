# Python

## OOP Essentials

### 1. **Introduction to OOP**

* **Data** in the form of fields (often called attributes or properties) / variables
* **Code** in the form of methods (functions defined in the class) / functions

Core principles of OOP:
(Python doesn't strictly follow them)

* **Encapsulation**: Bundling data and methods together
* **Abstraction**: Hiding internal details and showing only functionality
* **Inheritance**: One class can inherit from another
* **Polymorphism**: Same method name can have different implementations

### 2. **Creating Classes and Objects**

**Class**: A blueprint for creating objects.
**Object**: An instance of a class.

```python
class Person:
    def greet(self):
        print("Hello!")

p = Person()  # Creating an object
p.greet()     # Calling a method
```

### 3. **Instance Variables and Methods**

**Instance Variables** are unique to each object.
**Instance Methods** operate on instance variables.

```python
class Dog:
    def __init__(self, name):
        self.name = name  # instance variable

    def speak(self):
        print(f"{self.name} says woof!")

d1 = Dog("Buddy")
d2 = Dog("Rocky")

d1.speak()  # Buddy says woof!
d2.speak()  # Rocky says woof!
```

### 4. **Class Variables and Methods**

**Class Variables** are shared across all instances.
**Class Methods** use `@classmethod` and take `cls` as the first parameter.

```python
class Car:
    wheels = 4  # class variable

    @classmethod
    def get_wheel_count(cls):
        return cls.wheels

print(Car.wheels)

c1 = Car()
c2 = Car()

Car.wheels = 10

print(c1.wheels) # 10
print(c2.wheels) # 10
```

### 5. **Constructors**

The constructor in Python is defined using the `__init__` method and is called automatically when an object is created.

```python
class Student:
    def __init__(self, name):
        self.name = name

s = Student("Alice")
print(s.name)  # Alice
```

### 6. **Static Method**

A method that doesn’t use instance (`self`) or class (`cls`). Defined with `@staticmethod`.

```python
class Math:
    @staticmethod
    def add(x, y):
        return x + y

print(Math.add(5, 3))  # 8
```

### 7. **Association, Aggregation, and Composition**

These define relationships between classes.

* **Association**: General relationship; one class uses another.
* **Aggregation**: "Has-a" relationship where the contained object can exist independently.
* **Composition**: "Has-a" relationship where the contained object cannot exist independently.

```python
# Association
class Driver:
    def drive(self, car):
        print("Driving", car.model)

# Aggregation
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self, engine):
        self.engine = engine  # Aggregation

# Composition
class Battery:
    def __init__(self):
        print("Battery created")

class ElectricCar:
    def __init__(self):
        self.battery = Battery()  # Composition
```

### 8. **Getter, Setter, and Read-only Property Using `@property`**

Used to encapsulate access to attributes.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):  # getter
        return self._radius

    @radius.setter
    def radius(self, value):  # setter
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be non-negative")

    @property
    def diameter(self):  # read-only property
        return self._radius * 2

c = Circle(5)
print(c.radius)    # 5
c.radius = 10
print(c.diameter)  # 20
```
