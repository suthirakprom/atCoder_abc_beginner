# testing correctly but wrong answer to the bot
N,K = map(int, input().split())
res = 0
H = input().split()
H.sort()
numbers = [int(i) for i in H]
if K>=N:
    print(0)
else:
    for i in range(N-K):
        res += numbers[i]
    print(res)