# stack = []
#
# # Push
# stack.append('A')
# stack.append('B')
# stack.append('C')
# print("Stack: ", stack)
#
# # Peek
# topElement = stack[-1]
# print("Peek: ", topElement)
#
# # Pop
# poppedElement = stack.pop()
# print("Pop: ", poppedElement)
#
# # Stack after Pop
# print("Stack after Pop: ", stack)
#
# # isEmpty
# isEmpty =  bool(stack)
# print("isEmpty: ", isEmpty)
#
# # Size
# print("Size: ",len(stack))



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

