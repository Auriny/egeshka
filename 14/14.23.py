# https://openfipi.devinf.ru/task/D4ACB2

a = 7 * 512**120 - 6 * 64**100 + 8**210 - 255
k0 = 0

while a > 0:
    if a % 8 == 0:
        k0 += 1
    a //= 8

print(k0)