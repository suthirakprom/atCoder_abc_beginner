num = int(input())
re = 0
while num >= 500:
    re+=1000
    num-=500
while num >=5:
    re+=5
    num-=5
print(re)