# Class 2 – Stacks & Queues

**Duration:** 90 minutes

---

## Topics to Discuss

### 1. Stack (LIFO – Last In First Out)
- **Core operations**:
  - `push(item)` → add to top
  - `pop()` → remove from top
  - `peek()` → see top without removing
  - `is_empty()`
- **Time complexity**: All O(1) when using `list.append()` and `list.pop()`
- **Python Implementations**:
  - Using `list`

- **Real-life applications**:
  - Undo/Redo in text editors
  - Browser back/forward
  - Function call stack in programming

---

### 2. Queue (FIFO – First In First Out)
- **Core operations**:
  - `enqueue(item)` → add to end
  - `dequeue()` → remove from front
  - `peek()` → see front without removing
  - `is_empty()`
- **Time complexity**: O(1) for `deque.append()` and `deque.popleft()`
- **Python Implementations**:
  - Using `collections.deque`
  - Using `queue.Queue` (thread-safe)
- **Real-life applications**:
  - Task scheduling
  - Printer jobs
  - Ticket booking systems

---

## Activities

### 1. Implement Stack
```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else None

    def peek(self):
        return self.items[-1] if self.items else None

    def is_empty(self):
        return len(self.items) == 0


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack after pushing 1, 2, 3:", stack.items)

print("Top item:", stack.peek())

popped_item = stack.pop()
print("Popped item:", popped_item)
print("Stack after popping:", stack.items)

print("Is the stack empty?", stack.is_empty())

```

### 2. Implement Queue
```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft() if self.items else None

    def peek(self):
        return self.items[0] if self.items else None

    def is_empty(self):
        return len(self.items) == 0


queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue after enqueuing 1, 2, 3:")
print(queue.items)

print("Dequeue:", queue.dequeue())
print("Queue after dequeue:")
print(queue.items)

print("Peek:", queue.peek())
print("Is the queue empty?", queue.is_empty())
```