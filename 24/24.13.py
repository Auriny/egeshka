# https://prnt.sc/Tu1jNQvu2yx3

f = open('24.13.txt').readline().split('K')

for x, y, z, w in zip(f[0:], f[1:], f[2:], f[3:]):
    print(x, y, z, w, len(x + y + z + w))
    break