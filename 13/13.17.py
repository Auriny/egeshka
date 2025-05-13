# https://t.me/ege_informatica_skyeng/2766

from ipaddress import *

c = 0
for ip in ip_network("137.214.144.176/255.255.255.252", 0):
    c += 1
print(c)

# 2 способ

print(len([x for x in ip_network("137.214.144.176/255.255.255.252", 0)]))