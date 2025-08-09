
# Append = add an element at Last
# Append only needs the element, no need of the index

numbers = [1, 3, 4, 5, 2]

numbers.append(30)
print(numbers)





# Insert = add an element in a Specific index
# While Inserting we both need (Element + index)
# More control

arr = [7, 6, 2, 8, 1]


arr.insert(2, 10)                     # arr.insert(index, value)
print(arr)


arr.insert(-1, 11)                    # -1 means the before of last index
print(arr)


arr.insert(-2, 89)                    # -2 means the before and before of last index😆
print(arr)






# Remove
# removes the value from a list

a = [7, 26, 23, 84, 45]

a.remove(23)
print(a)


