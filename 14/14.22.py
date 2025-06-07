import string

for x in string.printable[:15]:
    a = int(f'97968{x}15', 15) + int(f'7{x}233', 15)

    if a % 14 == 0:
        print(x, a // 14)