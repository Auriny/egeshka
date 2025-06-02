def f(n):
    bin_n = bin(n)[2:]
    bin_n += str(bin_n.count('1') + bin_n.count('1') % 2)
    bin_n = bin_n.count('1') * '1' + '0'
    r = int(bin_n, 2)