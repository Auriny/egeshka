# Определи максимальное количество идущих подряд символов, среди которых не более одной буквы D.

st = open('24.9.txt').readline().split('D')
lst = [len(x) for x in st]
otv = []
for i in range(len(lst) - 1):
    otv.append(lst[i] + lst[i + 1])
print(max(otv) + 1)