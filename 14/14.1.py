def prov_bil(x, y):
    return ((x < 4) <= ((x * x) < a)) and (((y * y) <= a) <= (y <= 5))
count = 0
for a in range(1, 1000):
    if all(prov_bil(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        count += 1
        print(a, count)