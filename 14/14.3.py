znach = 3 * 200 ** 300 + 14 * 12 ** 1212 - 71 ** 17 - 1000
summa = 0
while znach > 0:
    tsifra = znach % 16 # перевод в 16 сс
    if tsifra <= 40:
        summa += tsifra
    znach = znach // 16
print(summa)