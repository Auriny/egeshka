# https://openfipi.devinf.ru/task/580BC7

from ipaddress import *

c = 0

for ip in ip_network("172.16.192.0/255.255.192.0", 0):
    if bin(int(ip))[2:].count('1') % 5 != 0:
        c += 1

print(c)
