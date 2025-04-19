# https://prnt.sc/I9Jf-ubPX7UQ

from ipaddress import *

for mask in range(33):
    net = ip_network('137.214.144.176/' + str(mask), 0)
    print(net, net.netmask)
