# https://prnt.sc/ZF1uMWuII8Uk

def f(n):
    n_bin = bin(n)[2:]
    n_bin += n_bin[-1]

    if n_bin.count('1') % 2 == 0:
        n_bin += '0'
    else:
        n_bin += '1'

    if n_bin.count('1') % 2 == 0:
        n_bin += '0'
    else:
        n_bin += '1'
    return int(n_bin, 2)

for i in range(1, 10000):
    if f(i) > 130:
        print(i)
        break
