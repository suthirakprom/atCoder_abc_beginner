n, m = map(int, input().split())
newString = ""
for i in range(n): 
    string = input()
    newString = newString + string + " "
words = newString.split()
words.sort()
for i in words: 
    print(i, end="")