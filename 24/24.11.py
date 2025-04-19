# Найди максимальную длину подстроки, в которой символы «a» и «d» не стоят рядом.

st = open("24.11.txt").readline().replace("ad", '*').replace("da", '*').split('*')
lst = [len(x) for x in st]
print(max(lst) + 2)