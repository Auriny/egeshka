from math import sqrt


def rast(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def center(cluster):
    return min(cluster, key=lambda p: sum(rast(p, q) for q in cluster))


with open('Файл А.txt') as f:
    dots = [list(map(float, line.replace(',', '.').split())) for line in f]

cluster1 = [dot for dot in dots if dot[1] > 2]
cluster2 = [dot for dot in dots if dot[1] <= 2]

c1 = center(cluster1)
c2 = center(cluster2)

px = (c1[0] + c2[0]) / 2
py = (c1[1] + c2[1]) / 2

print(px * 1000, py * 1000)
