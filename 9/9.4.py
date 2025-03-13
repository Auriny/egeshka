# Откройте файл электронной таблицы, содержащей в каждой строке семь натуральных чисел.
# Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
# — среди семи чисел совпадают ровно четыре числа;
# — среднее значение неповторяющихся чисел больше суммы повторяющихся чисел.
# В ответе запишите только число

f = open("9.4.txt")
count = 0
final_list = []
for stroka in f:
    spisok = stroka.split()
    int_spisok = [int(x) for x in spisok]

    set_4 = {x for x in int_spisok if int_spisok.count(x) == 4}
    spisok_repeating = [x for x in int_spisok if int_spisok.count(x) == 4]

    if set_4 and set_4.issubset(int_spisok):
        for x in spisok_repeating:
            if int_spisok != "None":

                final_list = final_list.append(x)
            print(int_spisok)
# :( не вышло