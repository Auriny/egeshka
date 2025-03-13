# Сколько существует девятеричных шестизначных чисел,
# в которых все цифры различны и никакие
# две чётные или две нечётные цифры не стоят рядом?

from itertools import *

count = 0

for slovo in permutations('012345678', 6):
    if ((slovo[0] in '2468') and \
            (slovo[1] in '1357') and \
            (slovo[2] in '02468') and \
            (slovo[3] in '1357') and \
            (slovo[4] in '02468') and \
            (slovo[5] in '1357')) or \
        ((slovo[0] in '1357') and \
         (slovo[1] in '02468') and \
         (slovo[2] in '1357') and \
         (slovo[3] in '02468') and \
         (slovo[4] in '1357') and \
         (slovo[5] in '02468')):
                count += 1
                print(slovo, count)
