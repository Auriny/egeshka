from string import printable

for x in printable[:18]:
    a1 = int(f'11h{x}05', 18)
    a2 = int(f'3f{x}54{x}8', 18)
    a3 = int(f'g{x}{x}{x}9', 18)

    if (a1+a2+a3) % 14 == 0:
        print(x, (a1+a2+a3) // 14)

