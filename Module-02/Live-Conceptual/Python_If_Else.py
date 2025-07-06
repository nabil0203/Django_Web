# https://www.hackerrank.com/challenges/py-if-else/problem

x = int(input())

if x % 2 != 0:
    print("Weird")
elif x % 2 == 0 and 2 <= x <= 5:
    print("Not Weird")
elif x % 2 == 0 and 6 <= x <= 20:
    print("Weird")
elif x % 2 == 0 and x > 20:
    print("Not Weird")
