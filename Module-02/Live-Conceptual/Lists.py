# https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

x = int(input())
my_list = []

for i in range(x):
    y = input()

    command = y.split()                         # spliting the input each time
    operation = command[0]                      # 0 index of the Command is what operation required

    if operation == "insert":
        index = int(command[1])
        value = int(command[2])
        my_list.insert(index, value)

    elif operation == "print":
        print(my_list)

    elif operation == "remove":
        value = int(command[1])
        my_list.remove(value)

    elif operation == "append":
        value = int(command[1])
        my_list.append(value)

    elif operation == "sort":
        my_list.sort()

    elif operation == "pop":
        my_list.pop()

    elif operation == "reverse":
        my_list.reverse()
