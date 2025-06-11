from math import *

for kod in range(1, 100000):
    bit = ceil(log2(kod))
    byte = ceil(119*bit/8)

    if 125_300 * byte > 23*1024*1024:
        print(kod)
        break