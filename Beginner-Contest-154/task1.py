S,T = input().split()
A,B = map(int, input().split())
U = input()
if U == S: 
    A = A-1
elif  U == T: 
    B = B-1
print(A,B)
