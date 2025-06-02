# https://prnt.sc/wHAGMBy2MFag

chisla = [int(x) for x in open('17.9.txt')]
max7 = max(x for x in chisla if str(x)[-1] == '7')

lst = []

for a, b in zip(chisla[0:], chisla[1:]):
    if str(a)[-1] == '3' or str(b)[-1] == '3':
        summa = a ** 2 + b ** 2
        if summa >= max7 ** 2:
            lst.append(summa)

print(len(lst), max(lst))
