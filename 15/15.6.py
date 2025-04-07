for a in range(1, 1000):
    flag = False
    for x in range(1, 1000):
        check = ((x & 22 != 0) or (x & 9 != 0)) <= ((x & 50 == 0) <= (x & a != 0))
        if not check:
            flag = True
    if not flag:
        print(a)