for n in range(4, 10000):
    s = '3' + n * '1'
    while ('31' in s) or ('211' in s) or ('1111' in s):
        s = s.replace('31', '1', 1)\
            .replace('211', '13', 1)\
            .replace('1111', '2', 1)
    sm = sum(map(int, s))
    if sm == 15:
        print(n)
        break
