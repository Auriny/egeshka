def perev(chislo, ss):
    otv = []
    while chislo > 0:
        ost = chislo % ss
        otv.append(ost)
        chislo = chislo // ss
    return otv[::-1]
print(perev(92, 52))