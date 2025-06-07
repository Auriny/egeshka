from itertools import *
from string import printable

k = 0
for x in product(printable[:8], repeat=5):
    if x[0] != '0' and int(x[0]) % 2 == 0 and x[-1] not in '26' \
            and (x.count('7') <= 2):
        k += 1

print(k)
