def tree(n):
    for i in range(n):
        print(' ' * (n - (i + 1)),'*' * (2*i+1))
        print("")
    for i in range(2): 
        print(' ' * (n -  1), '*')
        print('')
    print(' ' * (n - (1 + 1)),'*' * (2*1+1))
tree(5)