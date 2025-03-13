# В каждой строке электронной таблицы записаны пять целых положительных чисел.
# Определите, сколько в таблице строк, для которых выполнены следующие условия:
#
# — все числа в строке различны;
# — нечётных чисел больше, чем чётных;
# — сумма нечётных чисел меньше суммы чётных.
#
# В ответе запишите число — количество строк, для которых выполнены эти условия.

f = open("9.3.txt")
count = 0
for stroka in f:
    spisok = stroka.split()
    int_spisok = [int(x) for x in spisok]
    razl_spisok = [x for x in int_spisok if int_spisok.count(x) == 1]
    if len(razl_spisok) == 5:
        sorted_list = sorted(razl_spisok)
        chet_list = [x for x in sorted_list if x % 2 == 0]
        nechet_list = [x for x in sorted_list if x % 2 != 0]
        if (len(nechet_list) > len(chet_list)) and sum(nechet_list) < sum(chet_list):
            count += 1

print(count)
