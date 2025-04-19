# https://prnt.sc/aTmUMQRe_207

from ipaddress import *

c = 0

for ip in ip_network("137.224.124.176/255.255.255.248"):
    c += 1

print(c)