n = int(input())
m = n
count = 0
for i in range(n): 
    m = m - 1
    if m == 1: 
        n = n//2
    else:
        count += 1
for i in range(n): 
    count += 2

print(count)
