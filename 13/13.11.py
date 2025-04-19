# https://openfipi.devinf.ru/task/490050

from ipaddress import *

c = 0

for ip in ip_network("172.16.80.0/255.255.248.0"):
    if bin(int(ip))[2:].count('1') % 2 != 0:
        c += 1

print(c)