# https://prnt.sc/XqZK4vZggtaF
# https://prnt.sc/3zzgpE5GNUNP

st = open('24.7.txt').readline().split('A')  # почему 8? потому что с двух сторон A и тогда хватит 8
st_wo_B = [x for x in st if (not x.count('B')) and (len(x) >= 8)]

print(len(st_wo_B))