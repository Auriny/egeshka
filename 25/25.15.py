def divs(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

k = 0
for num in range(93329, 93403):  # верхняя граница +1
    if divs(num) == 8:
        k += 1

print(k)
