print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if ((not x) and y and z and (not w)) or ((not x) and y and (not z) and (not w))\
                        or (x and y and z and (not w)):
                    print(w, x, y, z)