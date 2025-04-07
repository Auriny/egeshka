for a in range(1, 1000):
    flag = False
    for x in range(1, 1000):
        check = ((x % 11 == 0) <= (x % 16 != 0)) or (x + a >= 219)
        if not check:
            flag = True
            break
    if not flag:
        print(a)