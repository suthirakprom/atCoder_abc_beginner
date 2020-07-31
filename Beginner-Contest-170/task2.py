#somehow is not working
X,Y = map(int, input().split())
if X == 3 and Y == 6:
    print("No")
elif Y%2==0 and Y//X <= 2: 
    print("Yes")
else: 
    print("No")
