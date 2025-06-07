def f(n):
    bin_n = bin(n)[2:]
    if bin_n.count('0') % 2 == 0:
        bin_n = '10' + bin_n + '1'
    else:
        bin_n = '10' + bin_n[2:] + '0'

    return bin_n

otv = []

for x in range(1, 5000):
    if int(f(x), 2) < 256:
        otv.append(int(f(x), 2))

print(max(otv))