# https://t.me/ege_informatica_skyeng/2769

from ipaddress import *

for mask in range(33):
    net = ip_network(f'137.214.144.176/{mask}', 0)
    print(net, net.netmask)