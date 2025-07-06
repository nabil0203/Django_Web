# Exploring Python Modules and Package

## 1. Creating and Using Modules

### What is a Module?

A module in Python is simply a file containing Python definitions and statements. The file name is the module name with the `.py` suffix. Modules allow you to logically organize your Python code.

### Creating a Module

To create a module:

1. Create a new `.py` file
2. Add your Python code (functions, classes, variables)

Example (`mymodule.py`):

```python
def greet(name):
    return f"Hello, {name}!"

def calculate_square(x):
    return x ** 2

PI = 3.14159
```

### Using a Module

You can import and use your module in another Python file:

```python
import mymodule

print(mymodule.greet("Alice"))
print(mymodule.calculate_square(5))
print(mymodule.PI)
```

### Import Variations

```python
# Import specific items
from mymodule import greet, PI
print(greet("Bob"))  # No need for module prefix

# Import with alias
import mymodule as mm
print(mm.greet("Charlie"))
```

### Module Search Path

When you import a module, Python searches for it in:

1. The current directory
2. Directories listed in PYTHONPATH
3. Installation-dependent default path (like site-packages)

You can view the search path with:

```python
import sys
print(sys.path)
```

## 2. Using Built-in Modules

Python comes with many built-in modules (the "standard library"). Here are some commonly used ones:

### math Module

```python
import math

print(math.sqrt(16))
print(math.pi)
print(math.factorial(5))
```

### datetime Module

```python
from datetime import datetime, timedelta

now = datetime.now()
print(now)

tomorrow = now + timedelta(days=1)
print(tomorrow)
```

### random Module

```python
import random

print(random.randint(1, 10))  # Random integer between 1 and 10
print(random.choice(['a', 'b', 'c']))  # Random item from list
random.shuffle([1, 2, 3, 4])  # Shuffles list in place
```

## 3. Installing and Using Packages with Pip

### What is pip?

pip is Python's package installer. It lets you install and manage additional packages not included in the standard library.

### Basic pip Commands

```bash
# Install a package
pip install package_name

# Install specific version
pip install package_name==1.0.4

# Upgrade a package
pip install --upgrade package_name

# Uninstall a package
pip uninstall package_name

# List installed packages
pip list

# Show package info
pip show package_name
```

### Example: Installing and Using the requests Package

```bash
pip install requests
```

```python
import requests

response = requests.get('https://api.github.com')
print(response.status_code)  # 200 if successful
print(response.json())  # Parsed JSON response
```

## 4. Python Standard Library Overview

The Python Standard Library is a collection of modules that come with Python. Here are some key components:

### File and Directory Access

- `os`: Operating system interfaces
- `os.path`: Common pathname manipulations
- `shutil`: High-level file operations
- `glob`: Unix-style pathname pattern expansion
- `tempfile`: Generate temporary files/directories

### Data Types

- `collections`: Specialized container datatypes
- `array`: Efficient arrays of numeric values
- `heapq`: Heap queue algorithm
- `bisect`: Array bisection algorithm
- `weakref`: Weak references

### Numeric and Math Modules

- `math`: Mathematical functions
- `cmath`: Mathematical functions for complex numbers
- `decimal`: Decimal fixed and floating point arithmetic
- `fractions`: Rational numbers
- `random`: Generate pseudo-random numbers

### Internet and Networking

- `socket`: Low-level networking interface
- `email`: Email message handling
- `json`: JSON encoder and decoder
- `urllib`: URL handling modules
- `http`: HTTP modules

### Development Tools

- `unittest`: Unit testing framework
- `doctest`: Test interactive Python examples
- `pdb`: The Python debugger
- `timeit`: Measure execution time of small code snippets
- `profile`: Python profiler

### Concurrent Execution

- `threading`: Thread-based parallelism
- `multiprocessing`: Process-based parallelism
- `queue`: Synchronized queue class
- `subprocess`: Subprocess management

### Runtime Services

- `sys`: System-specific parameters
- `atexit`: Exit handlers
- `time`: Time access and conversions
- `logging`: Logging facility
- `gc`: Garbage Collector interface
