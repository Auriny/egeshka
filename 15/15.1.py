lst = []
for A in range(1000000):
    for x in range(2):
        for y in range(2):
            if (2*x + 4*y < A) or (x > y) or (y > 15):
                lst.append(A)

print(min(lst))
