n = int(input())
j = 100
b = 0
ans = 0
for i in range(100, n):
    ans = (j*1)/100
    j += ans
    if(j != n): 
        b +=1
    else:
        break   
print(b)
