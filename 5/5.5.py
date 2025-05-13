# https://prnt.sc/LtoFQV1y7wgc

def f(n):
    n_bin = bin(n)[2:]
    n_bin_lst = [x for x in n_bin]
    if sum(n_bin_lst) % 2 == 0:
        n_bin += '0'
        n_bin = '10' + n_bin[2:]
    else:
        n_bin += '1'
        n_bin = '11' + n_bin[2:]
    return int(n_bin, 2)


for x in range(1, 10000):
    if f(x) > 480:
        print(x)
        break
