from math import *

for kod in range(1, 100):
    bit = ceil(log2(kod))
    byte = ceil(246*bit/8)

    if 703_569 * byte <= 77*2**20:
        print(kod)