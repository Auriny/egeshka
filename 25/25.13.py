def poisk_del(x):
    dels = []
    for d in range(2, x//2 + 2):
        if x % d == 0:
            dels.append(d)
    return dels

k = 0

for x in range(111, 10 ** 6 + 1, 111):
    s_x = str(x)
    if (s_x[0] == '1') and (s_x[-1] == '1') and ((len(s_x)) >= 5):
        if len(poisk_del(x)) == 6:
            k += 1
            print(x, k, poisk_del(x))