import heapq

# ==================== MIN HEAP ====================
print("="*50)
print("MIN HEAP (using heapq)")
print("="*50)

# Create a min heap
min_heap = []

# Insert elements
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 20)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 15)

print("Min Heap after insertions:", min_heap)
print("Smallest element (peek):", min_heap[0])

# Extract minimum
smallest = heapq.heappop(min_heap)
print(f"Extracted minimum: {smallest}")
print("Min Heap after extraction:", min_heap)

# Heapify a list
numbers = [30, 10, 50, 20, 40]
heapq.heapify(numbers)
print("\nHeapified list:", numbers)

print("\n")

# ==================== MAX HEAP ====================
print("="*50)
print("MAX HEAP (using negative values)")
print("="*50)

# Python heapq only supports min heap
# For max heap, we negate the values
max_heap = []

# Insert elements (negate for max heap behavior)
heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -20)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -15)

print("Max Heap (negated values):", max_heap)
print("Largest element (peek):", -max_heap[0])

# Extract maximum
largest = -heapq.heappop(max_heap)
print(f"Extracted maximum: {largest}")
print("Max Heap after extraction:", [-x for x in max_heap])

print("\n")

# ==================== PRIORITY QUEUE ====================
print("="*50)
print("PRIORITY QUEUE")
print("="*50)

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        # Lower priority number = higher priority
        heapq.heappush(self.heap, (priority, item))

    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)[1]
        return None

    def peek(self):
        if self.heap:
            return self.heap[0][1]
        return None

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)


# Example: Task scheduling with priority
pq = PriorityQueue()

pq.push("Write documentation", 3)
pq.push("Fix critical bug", 1)
pq.push("Code review", 2)
pq.push("Refactor code", 4)

print("Priority Queue Tasks (by priority):")
while not pq.is_empty():
    task = pq.pop()
    print(f"  - {task}")

print("\n")

# ==================== K LARGEST/SMALLEST ELEMENTS ====================
print("="*50)
print("K LARGEST/SMALLEST ELEMENTS")
print("="*50)

numbers = [10, 5, 20, 1, 15, 30, 25]

# Find 3 largest elements
k_largest = heapq.nlargest(3, numbers)
print(f"3 largest elements from {numbers}:")
print(f"  {k_largest}")

# Find 3 smallest elements
k_smallest = heapq.nsmallest(3, numbers)
print(f"\n3 smallest elements from {numbers}:")
print(f"  {k_smallest}")

print("\n")

# ==================== MERGE SORTED LISTS ====================
print("="*50)
print("MERGE SORTED LISTS")
print("="*50)

list1 = [1, 5, 9]
list2 = [2, 6, 10]
list3 = [3, 7, 11]

merged = list(heapq.merge(list1, list2, list3))
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"List 3: {list3}")
print(f"Merged: {merged}")
