desk_book_minute = input().split()
lst = []
book_time_A = input().split()
book_time_B = input().split()
c = sorted(book_time_A + book_time_B)
total = 0
i = 0
while total <= int(desk_book_minute[2]):
    total = int(c[i]) + int(c[i+1])
    i += 1
print(i)

# wrong almost correct tho




