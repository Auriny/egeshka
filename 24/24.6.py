# https://prnt.sc/a247hjWlzH-T

st = open('24.6.txt').readline()
spisok = st.split('A')
lst = []

for el in spisok:
    if el.count('E') >= 3:
        lst.append(len(el))
    if len(el) == 282:
        print(el)  # выводим строку эту с пояснения ниже

print(max(lst))  # кончается на A и начинается на A НО
# тут ничего быть в строке не должно. мы нихуя не докидываем ни +1 и +2