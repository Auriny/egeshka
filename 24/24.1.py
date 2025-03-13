# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC...Z)
# Определите максимальное количество идущих подряд символов, среди которых не более одной буквы F.
from itertools import *

f = open('24.1.txt', 'r')
s = f.read()

alphabet = ["a", "b", "c", 'd', 'e', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for x in alphabet:
    while x in s:
        s = s.replace(x, "-")

print(s)
