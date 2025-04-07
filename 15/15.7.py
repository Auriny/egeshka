lst = []
for a in range(1, 1000):
    for x in range(1, 1000):
        check = ((x & 29 != 0) and (x & 39 != 0)) <= ((x & 59 == 0) <= (x & a != 0))
        if check:
            lst.append(a)

print(min(lst))