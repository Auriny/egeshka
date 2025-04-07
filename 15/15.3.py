c = [x for x in range(28, 61)]
z = [x for x in range(18, 80)]
a = []  # вагон для безбилетников

for x in range(1, 1000):
    check = (not (x in c) or (x in a)) or not (x in z)
    if not check:
        a.append(x)

print(len(a) - 1)  # мы отнимаем 1 т.к. длина линейки [1, 2, 3] на самом деле не 3, а 2
                                                    #   \/ \/  <--- 2 а не 3
