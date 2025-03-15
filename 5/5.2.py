def f(n):
    a = bin(n)[2:]

    for x in range(2):
        if a.count('1') > a.count('0'):
            a += '0'
        else:
            a = '11' + a

    return int(a, 2)

lst = []

for N in range(150000):
    if f(N) > 500:
        lst.append(N)

print(min(lst))
