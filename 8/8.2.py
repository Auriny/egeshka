# Сколько существует девятеричных шестизначных чисел,
# в которых все цифры различны и никакие
# две чётные или две нечётные цифры не стоят рядом?

from itertools import *
count = 0
for slovo in permutations('012345678', 6):
    slovo_1 = ''.join(slovo)\
        .replace('0', 'ч')\
        .replace('2', 'ч')\
        .replace('4', 'ч')\
        .replace('6', 'ч')\
        .replace('8', 'ч')\
        .replace('1', 'н')\
        .replace('3', 'н')\
        .replace('5', 'н')\
        .replace('7', 'н')
    if (slovo[0] != "0") and ('чч' not in slovo_1) and ('нн' not in slovo_1):
        count += 1
        print(slovo, slovo_1, count)