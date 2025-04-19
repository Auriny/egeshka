# https://prnt.sc/a247hjWlzH-T

st = open('24.5.txt').readline()
print(max([len(x) for x in st.split('A') if x.count('E') >= 3]))
# тоже что и 24.6.py но в одну строку. файл тот же но
# для понимания пиздец