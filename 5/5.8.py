# https://prnt.sc/8MtVOQSk9wgC

def f(n):
    bin_n = bin(n)[2:]

    for i in range(2):
        c = bin_n.count('1')
        bin_n += str(c % 2)

    return int(bin_n, 2)

for x in range(10000):
    if f(x) > 97:
        print(f(x))
        break
