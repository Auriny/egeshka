# https://prnt.sc/thk97j8UfaN-

from ipaddress import *

ip = ip_network("143.168.72.213/255.255.255.240", 0)
print(ip[-2])