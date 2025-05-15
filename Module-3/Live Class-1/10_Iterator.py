# 2:15
# whenever iterator is called, it gives just 1 value each time Serially



number = [1, 2, 3, 4, 5]

it = iter(number)               # variable = iter(list_name)


print(next(it))     # 1
print(next(it))     # 2
print(next(it))     # 3
print(next(it))     # 4
print(next(it))     # 5
# print(next(it))     # error, bcz there is no 6th element