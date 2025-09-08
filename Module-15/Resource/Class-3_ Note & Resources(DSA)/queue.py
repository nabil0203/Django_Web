# queue = []
#
# # Enqueue
# queue.append('A')
# queue.append('B')
# queue.append('C')
# print("Queue: ", queue)
#
# # Peek
# frontElement = queue[0]
# print("Peek: ", frontElement)
#
# # Dequeue
# poppedElement = queue.pop(0)
# print("Dequeue: ", poppedElement)
#
# print("Queue after Dequeue: ", queue)
# #
# # isEmpty
# isEmpty = not bool(queue)
# print("isEmpty: ", isEmpty)
# #
# # Size
# print("Size: ", len(queue))
#
#
#
#


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

