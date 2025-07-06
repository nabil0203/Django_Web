# https://www.hackerrank.com/challenges/python-string-split-and-join/problem

x = input()

x = x.split(" ")            # spliting the words of the sentence 'x' one by one depending on Space
x = "-".join(x)             # joining the Words with '-'

print(x)