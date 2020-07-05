from collections import Counter

w = Counter(input())
result = 'Yes'

for i in w.values():
    if i % 2 != 0:
        print('No')
        exit()

print(result)