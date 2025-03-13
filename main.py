# число 12, найти все делители
def find_divisors(n):
    divisiors_list = [n]
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisiors_list.append(i)
    return divisiors_list


for x in range(231035, 231065):
    if len(find_divisors(x)) == 4:
        print(find_divisors(x))
