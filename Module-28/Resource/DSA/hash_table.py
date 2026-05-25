# ==================== PYTHON DICTIONARY (HASH TABLE) ====================
print("="*50)
print("HASH TABLE (Python Dictionary)")
print("="*50)

# Python dictionaries are implemented as hash tables
# Key operations: O(1) average case

# Create a hash table
hash_table = {}

# Insert key-value pairs
hash_table["name"] = "Alice"
hash_table["age"] = 25
hash_table["city"] = "Dhaka"

print("Hash Table:", hash_table)

# Access value by key
print(f"Name: {hash_table['name']}")

# Update value
hash_table["age"] = 26
print(f"Updated age: {hash_table['age']}")

# Check if key exists
if "city" in hash_table:
    print(f"City found: {hash_table['city']}")
else:
    print("City key not found")

# Delete key-value pair
del hash_table["city"]
print("After deleting 'city':", hash_table)

print("\n")

# ==================== COUNTING FREQUENCY ====================
print("="*50)
print("COUNTING FREQUENCY (Common Use Case)")
print("="*50)

text = "hello world"
frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(f"Text: '{text}'")
print("Character frequency:", frequency)

# Alternative using get()
frequency2 = {}
for char in text:
    frequency2[char] = frequency2.get(char, 0) + 1

print("Using get():", frequency2)

print("\n")

# ==================== USING COLLECTIONS.COUNTER ====================
print("="*50)
print("USING collections.Counter")
print("="*50)

from collections import Counter

text = "programming"
counter = Counter(text)

print(f"Text: '{text}'")
print("Character count:", counter)
print(f"Most common 3: {counter.most_common(3)}")

# Count elements in a list
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
num_counter = Counter(numbers)
print(f"\nNumbers: {numbers}")
print("Number count:", num_counter)

print("\n")

# ==================== DEFAULTDICT ====================
print("="*50)
print("USING collections.defaultdict")
print("="*50)

from collections import defaultdict

# Group words by first letter
words = ["apple", "banana", "apricot", "cherry", "avocado", "blueberry"]
grouped = defaultdict(list)

for word in words:
    first_letter = word[0]
    grouped[first_letter].append(word)

print(f"Words: {words}")
print("Grouped by first letter:")
for letter, word_list in sorted(grouped.items()):
    print(f"  {letter}: {word_list}")

print("\n")

# ==================== TWO SUM PROBLEM ====================
print("="*50)
print("TWO SUM PROBLEM (Hash Table Application)")
print("="*50)

def two_sum(nums, target):
    """
    Find two numbers that add up to target
    Returns indices of the two numbers
    """
    hash_map = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement], i]
        hash_map[num] = i

    return None

numbers = [2, 7, 11, 15]
target = 9

result = two_sum(numbers, target)
print(f"Numbers: {numbers}")
print(f"Target: {target}")
if result:
    print(f"Indices: {result}")
    print(f"Values: {numbers[result[0]]} + {numbers[result[1]]} = {target}")

print("\n")

# ==================== CUSTOM HASH TABLE ====================
print("="*50)
print("CUSTOM HASH TABLE IMPLEMENTATION")
print("="*50)

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """Simple hash function"""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert key-value pair"""
        hash_index = self._hash(key)

        # Check if key already exists, update if so
        for i, (k, v) in enumerate(self.table[hash_index]):
            if k == key:
                self.table[hash_index][i] = (key, value)
                return

        # Add new key-value pair
        self.table[hash_index].append((key, value))

    def get(self, key):
        """Get value by key"""
        hash_index = self._hash(key)

        for k, v in self.table[hash_index]:
            if k == key:
                return v

        return None

    def delete(self, key):
        """Delete key-value pair"""
        hash_index = self._hash(key)

        for i, (k, v) in enumerate(self.table[hash_index]):
            if k == key:
                del self.table[hash_index][i]
                return True

        return False

    def display(self):
        """Display hash table"""
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"  Bucket {i}: {bucket}")


# Example usage
ht = HashTable(5)
ht.insert("name", "Bob")
ht.insert("age", 30)
ht.insert("city", "Dhaka")
ht.insert("country", "Bangladesh")

print("Custom Hash Table:")
ht.display()

print(f"\nGet 'name': {ht.get('name')}")
print(f"Get 'age': {ht.get('age')}")

ht.delete("city")
print("\nAfter deleting 'city':")
ht.display()
