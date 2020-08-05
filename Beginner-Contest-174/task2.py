import math
N, D = map(int, input().split())
lst = []
for i in range(N): 
    X= input().split()
    lst.append(X)

total = int(lst[0][0]) + int(lst[0][1])
print(lst)
print(type(lst))
print(lst[0][1], lst[1][0])
print(total)
