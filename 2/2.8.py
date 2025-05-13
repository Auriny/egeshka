# https://prnt.sc/uOsL_BhZTr1G

print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if ((z <= (not(y <= x))) or w) == 0:
                    print(w, x, y, z)