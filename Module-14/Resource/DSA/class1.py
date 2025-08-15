# List
numbers = [1, 2, 3, 4]

# Append নতুন element যোগ করা
numbers.append(5)

# Insert কোনো নির্দিষ্ট index এ element যোগ করা
numbers.insert(2, 10)

# Element মুছে ফেলা
numbers.remove(3)

# List traverse করা
for num in numbers:
    print(num)

# Dictionary
person = {"name": "Alice", "age": 30}

# নতুন key-value যোগ করা
person["city"] = "Dhaka"

# Value update করা
person["age"] = 31

# Value access করা
print(person["name"])

# Dictionary traverse করা
for key, value in person.items():
    print(f"{key}: {value}")

# Function definition
def greet(name):
    return f"Hello, {name}!"

# Function call
print(greet("Roky"))

# Function with multiple arguments
def add(a, b):
    return a + b

print(add(5, 3))