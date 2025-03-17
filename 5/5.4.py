def autobin(n):
    n_bin = bin(n)[2:]
    if n % 2 == 0:
        n_bin += '100'
    else:
        n_bin = '10' + n_bin
        n_bin += '001'
    return int(n_bin, 2)

lst = []

for N in range(50000):
    if autobin(N) > 500:
        lst.append(N)

print(min(lst))