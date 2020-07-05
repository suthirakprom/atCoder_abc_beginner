n = int(input())
a, b = map(int, input().split())
c = 0
for i in range(a, b+1):
    if(i%n==0):
        c += 1
        break
    else:
        c = 0
if(c==1):
    print("OK")
else:
    print("NG")
