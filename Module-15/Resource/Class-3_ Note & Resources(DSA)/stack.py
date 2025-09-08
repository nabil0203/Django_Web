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


stack.push('https://www.prothomalo.com/')
stack.push('https://www.prothomalo.com/bangladesh')
stack.push('https://www.prothomalo.com/sports')
print("Stack after pushing:", stack.items)

last_url = stack.pop()
print("last_url:", last_url)
print("Stack after popping:", stack.items)

last_url = stack.pop()
print("last_url:", last_url)
print("Stack after popping:", stack.items)


print("Top item:", stack.peek())

stack.pop()
stack.pop()
print("Stack after popping:", stack.items)

print ("Is the stack empty?", stack.is_empty())

stack.push(2)
stack.push(3)

print("Stack after pushing 1, 2, 3:", stack.items)

print("Top item:", stack.peek())

popped_item = stack.pop()
print("Popped item:", popped_item)
print("Stack after popping:", stack.items)

print("Is the stack empty?", stack.is_empty())


math = [1,2,3,4,5,6,7,8,9,10]
a = math.pop()
a =  a + math.pop()
print(a)
a =  a + math.pop()
print(a)
