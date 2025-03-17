# Ячейку таблицы можно считать «эпичной», если число в данной ячейке:
# встречается в этой строке ровно три раза;
# Определите наименьшее значение «эпичной» ячейки (число внутри нее).
# В ответе запишите только число.
f = open("9.7.txt")
epic = []
minimal = []
for stroka in f:
    lst = stroka.split()
    int_lst = [int(x) for x in lst]
    int_set = set(int_lst)
    if len(int_set) == 3:
        epic.append(int_lst)

for s in epic:
    for x in s:
        minimal.append(x)

# можно ваще было и просто min(minimal)
print(sorted(minimal)[1])
