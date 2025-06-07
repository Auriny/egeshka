from string import printable

for x in printable[:19]:
    a = int(f'348{x}79643', 19) + int(f'16{x}52', 19) + int(f'43{x}7', 19)

    if a % 18 == 0:
        print(x, a // 18)