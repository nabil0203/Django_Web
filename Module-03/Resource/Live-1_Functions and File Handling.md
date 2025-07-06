# Functions and File Handling

---

## 1. **Writing Functions**

A function is a block of reusable code that performs a specific task.

```python
def greet():
    print("Hello, world!")
```

You call it using `greet()`.

---

## 2. **Function Parameters**

Parameters are variables you define in the function to accept input values.

```python
def greet(name):
    print(f"Hello, {name}!")
```

Here, `name` is a parameter. When calling the function, you provide an **argument**, like `greet("Alice")`.

---

## 3. **Keyword Arguments**

These are arguments passed with their parameter names for clarity and flexibility.

```python
def greet(name, message):
    print(f"{message}, {name}!")

greet(name="Alice", message="Good morning")
```

Keyword arguments allow you to skip the order of parameters.

---

## 4. **Return Statements**

Used to send back a result from a function to the caller.

```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result)
```

---

## 5. **Decorator**

A function that modifies another function's behavior without changing its code.

```python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

---

## 6. **Lambda Functions**

Anonymous, short functions written with the `lambda` keyword.

```python
square = lambda x: x * x
print(square(5))
```

Often used with `map()`, `filter()`, or `sorted()`.

---

## 7. **Creating Reusable Functions**

Functions should be written in a general way so they can be reused.

```python
def calculate_area(width, height):
    return width * height
```

You can now call `calculate_area(5, 10)` or reuse it elsewhere in your code.

---

## 8. **Scope: Local and Global Variables**

* **Local**: Defined inside a function, accessible only there.
* **Global**: Defined outside all functions, accessible anywhere.

```python
x = 10  # Global

def custom_function():
    x = 5  # Local
    print(x)

custom_function()  # Prints 5
print(x)        # Prints 10
```

Use `global` keyword to modify global variables inside functions.

---

## 9. **Reading from Files**

Reading data from files using built-in `open()`.

```python
with open('data.txt', 'r') as file:
    content = file.read()
    print(content)
```

`with` ensures the file is closed automatically.

---

## 10. **Iterator and Generator**

* **Iterator**: An object with `__iter__()` and `__next__()` methods.
* **Generator**: A function that yields values lazily using `yield`.

```python
# Generator example
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(3):
    print(num)
```

Generators are memory-efficient for large datasets.

---

### 10.1. **Iterators**

An **iterator** is an object that can be iterated (looped) over. It implements two special methods:

* `__iter__()` — returns the iterator object itself
* `__next__()` — returns the next value from the iterator

#### 🔹 How Iterators Work

Python objects like lists, tuples, sets, and strings are **iterable**, meaning they can be converted to an iterator using `iter()`.

```python
nums = [1, 2, 3]
it = iter(nums)

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# print(next(it))  # Raises StopIteration
```

When there are no more items, `StopIteration` is raised.

#### 🔹 Custom Iterator Example

You can make your own iterator by defining a class:

```python
class CountDown:
    def __init__(self, start):
        self.n = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        val = self.n
        self.n -= 1
        return val

cd = CountDown(3)
for num in cd:
    print(num)  # 3, 2, 1
```

---

### 10.2 **Generators**

A **generator** simplifies the process of creating an iterator.

#### 🔹 How They Work

A generator is a function that uses the `yield` keyword to return a value. Each time it's called, it "pauses" its state and resumes from where it left off.

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(3):
    print(i)  # 3, 2, 1
```

Each call to `next()` runs the function until the next `yield`.

---

```python
def daterange(start_date, end_date):
    """Iterates by day over a range of dates"""
    total_days = abs((end_date - start_date).days) + 1
    for day_number in range(total_days):
        if start_date <= end_date:
            yield start_date + timedelta(day_number)
        else:
            # date reverse traversal
            yield start_date - timedelta(day_number)
```

#### 🔹 Generator Expressions (Like List Comprehensions)

```python
squares = (x * x for x in range(5))
for s in squares:
    print(s)  # 0, 1, 4, 9, 16
```
