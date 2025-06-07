# https://openfipi.devinf.ru/task/551280
a = 2 * 729**2014 + 2 * 243**2016 - 2 * 81**2018 + 2 * 27**2020 - 2 * 9**2022 - 2024
kb9 = 0

while a > 0:
    if a % 27 > 9:
        kb9 += 1
    a //= 27

print(kb9)