# Class 1: Introduction to DSA & Python Basics

## Importance of DSA in Coding and Interviews
DSA (Data Structures and Algorithms) হচ্ছে একজন প্রোগ্রামারের problem-solving skills এবং logical thinking বোঝানোর সবচেয়ে গুরুত্বপূর্ণ উপায়।

- Interviews-এ প্রায় সব বড় কোম্পানি DSA-based coding problems করে থাকে।
- DSA জানলে যেকোনো programming problem efficiently solve করা যায় — যেমন time complexity কমিয়ে আনা যায়।

### উদাহরণ:
যদি আপনি একটা array তে কোনো element আছে কিনা খুঁজেন `O(n)` এ, আর কেউ যদি সেটাকে `O(log n)` এ করতে পারে (binary search দিয়ে), তাহলে সেইটা efficient solution।

---

## Python Basics Refresher

### List
Python এ dynamic array হিসেবে কাজ করে।  
**Example:**
```python

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
```

## Dictionary

Python এ key-value pair হিসেবে কাজ করে।  
**Example:**

```python
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
```

## Functions

Python এ function define করা হয় `def` keyword দিয়ে।  
**Example:**

```python
def greet(name):
    return f"Hello, {name}!"

# Function call
print(greet("Roky"))

# Function with multiple arguments
def add(a, b):
    return a + b

print(add(5, 3))
```

## 📚 Arrays (Python Lists) and Operations

Array বা list হলো **ordered collection**।

**Common operations:**
- **Insertion:** নতুন element যোগ করা (`append()`, `insert()`)
- **Deletion:** element মুছে ফেলা (`remove()`)
- **Searching:** element খোঁজা (`in`, `index()`)
- **Slicing:** উপ-লিস্ট বের করা (`list[1:3]`)

---

## ⏱️ Big-O Notation (Time & Space Complexity)

Big-O বোঝায় কোনো algorithm এর **growth rate**।

**Common complexities:**
- `O(1)` – constant time (e.g., accessing list index)
- `O(n)` – linear time (e.g., loop over list)
- `O(n^2)` – nested loop
- `O(log n)` – binary search

### কেন গুরুত্বপূর্ণ?
এটি বলে দেয় কোড **slow হবে নাকি fast**, এবং **memory কত খাবে**।



# 💼 Interview Questions (সাক্ষাৎকার প্রশ্নোত্তর)

| প্রশ্ন | উত্তর |
|--------|-------|
| **DSA কেন important?** | এটি আপনার logical thinking এবং efficiency বোঝায়। Coding interviews এর প্রায় ৮০% প্রশ্ন DSA ভিত্তিক। |
| **List এবং Dictionary এর পার্থক্য কী?** | List হলো ordered collection, আর Dictionary হলো key-value pair structure। |
| **Big-O notation কী?** | Algorithm এর performance বোঝায় — কত দ্রুত বা ধীরে কাজ করে। |
| **একটি list reverse করার time complexity কত?** | O(n) — কারণ প্রতিটি element একবার traverse করতে হয়। |
| **Dictionary তে খোঁজার সময় কত লাগে?** | Average case O(1) — hashing ব্যবহৃত হয়। |
| **Python এ mutable এবং immutable object এর পার্থক্য কী?** | Mutable objects পরিবর্তনযোগ্য (যেমন list, dict), immutable objects পরিবর্তন অযোগ্য (যেমন int, str, tuple)। |
| **Python এ pass by reference না pass by value?** | Python uses pass-by-object-reference (call-by-sharing) — object reference পাস হয়। |
| **List এর elements sort করতে কীভাবে করো?** | `list.sort()` দিয়ে in-place sort, অথবা `sorted(list)` দিয়ে নতুন sorted list পাওয়া যায়। |
| **Python এ function এর default argument কী?** | Function parameter এর ডিফল্ট মান, যা ইউজার না দিলে ব্যবহার হয়। |
| **Stack কী? কোন data structure?** | Stack হলো LIFO (Last In First Out) data structure, যেখানে শেষ element প্রথম বের হয়। |
| **Queue এবং Stack এর মধ্যে পার্থক্য কী?** | Queue FIFO (First In First Out), Stack LIFO। |
| **Recursion কী? সুবিধা কী?** | ফাংশন নিজেই নিজেকে কল করা, কোড সংক্ষিপ্ত করে এবং কিছু সমস্যা সহজ করে। |
| **Python এ lambda function কী?** | Anonymous (নামহীন) ছোট ফাংশন, এক লাইনে লেখা যায়। |
| **Iterable এবং Iterator এর পার্থক্য কী?** | Iterable হলো এমন object যা loop করা যায়, Iterator হলো iterable থেকে elements এক এক করে আনে। |
