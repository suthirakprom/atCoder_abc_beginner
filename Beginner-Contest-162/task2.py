N = int(input())
S = 0
for i in range(1, N+1):
    if i%3==0 or i%5==0 or (i%3==0 and i%5==0):
        continue
    S+=i
print(S)