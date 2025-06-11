from math import *

for n in range(1, 100000):
    bit = ceil(log2(n))
    byte = ceil(257 * bit / 8)

    if 295_740 * byte <= 33*1024*1024:
        print(n)
        