# https://prnt.sc/Z92lFNejNP9q

print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if x and (z <= w) and (not y):
                    print(w, x, y, z)