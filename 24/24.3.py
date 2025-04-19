stroka = open('24.3.txt').readline().replace('XX', '*').replace('YY', '*').replace('ZZ', '*')
spisok = stroka.split('*')
len_s = [len(x) for x in spisok]

print(max(len_s) + 1)
