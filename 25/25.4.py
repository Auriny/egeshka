# Напиши программу, которая ищет среди целых чисел, принадлежащих числовому отрезку
# [201017; 201228] числа, имеющие ровно 6 различных натуральных делителей, кратных 2.
# Выведи первые три числа в порядке возрастания через пробел.

def search_div(x):
    div_list = []
    for div in range(2, x + 1):
        if (x % div == 0) and (div % 2 == 0):
            div_list.append(div)
    return div_list

for x in range(201017, 201228 + 1):
    if len(search_div(x)) == 6:
        print(x, search_div(10))