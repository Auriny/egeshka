from string import *
from itertools import *

k = 0
al = printable[:14]
for x in product(al, repeat=5):
    if x.count('9') == 1 and \
            sum([x.count(s) for s in 'bcd']) <= 3:
        k += 1

print(k)
