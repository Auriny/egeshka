from functools import *


@cache
def f(n):
    if n <= 2024:
        return n
    else:
        return 15 * n - 2024 + f(n - 1) + f(n - 2)

for i in range(1, 12346):
    f(i)

print(str(f(12345) - f(2345)).count('1'))
