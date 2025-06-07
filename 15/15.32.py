b = [x for x in range(50, 61)]
lst = []

def f(x):
    return (x % a == 0) or ((x in b) <= (x % 13 != 0))

for a in range(1, 2000):
    if all(f(x) for x in range(1, 2000)):
        lst.append(a)

print(max(lst))