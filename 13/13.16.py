from ipaddress import *

c = 0

for ip in ip_network("10.48.96.0/255.255.240.0"):
    b = f'{ip:b}'
    if b.count('1') > b.count('0'):
        print(ip)
        c += 1

print(c)
