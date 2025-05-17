a = [ [12, 15], ("hi", "hello")]


print(a)                        # whole 'a' is a List

print(a[0])                     # 0 index of List->'a' has another List->[12, 15]
print(a[0][0])                  # 0 index of List->'a' has another List->[12, 15] & at 0 index of [12, 15] is 12

print(a[1])                     # 1 index of List->'a' has tuple->("hi", "hello")
print(a[1][1])                  # 1 index of List->'a' has tuple->("hi", "hello") & at 1 index of ("hi", "hello") is hello
print(a[1][1][0])               # 1 index of List->'a' has tuple->("hi", "hello") & at 1 index of ("hi", "hello") is hello & at 0 index of hello is 'h'

