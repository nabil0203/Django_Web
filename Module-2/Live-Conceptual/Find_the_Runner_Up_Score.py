# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

n = int(input())

my_list = list(map(int, input().split()))                         # list input as map


highest = max(my_list)                              # highest of the list is stored


temp_list = []                                      # temporay list taken to push the elements one after one except the highest

for i in range(0, n):
    if my_list[i] != highest:                       # condition -->> if not highest then Push into the list
        temp_list.append(my_list[i])


print(max(temp_list))                           # print the temporary list which doesn't contain the highest of the first list
