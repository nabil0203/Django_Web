import collections


fruits = ["apple", "banana", "mango", "apple", "cherry", "mango", "cherry", "cherry"]


print(collections.Counter(fruits))                                  # counts the elements

print(collections.Counter(fruits).most_common(2))                   # shows the most commom 2 elements