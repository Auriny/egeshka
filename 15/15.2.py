def check(x, y):
    return ((x < 7) <= (x ** 2 < a)) and ((y ** 2 <= a) <= (y <= 9))

count = 0

for a in range(1, 200):
    if all(check(x, y) for x in range(1, 500) for y in range(1, 500)):
        count += 1
        print(count)