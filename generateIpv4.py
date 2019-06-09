#!/usr/bin/python3

# =========================================
# Execute this script as follows:
# python3 generateIpv4.py [base_ip] [delta]
# =========================================

from ip2hex import ip2hex
from hex2ip import hex2ip
import sys

# Define IPv4 address
ip = sys.argv[1]
# Convert it to hexadecimal (w/o 0x)
hex_ip = ip2hex(ip)
# Delta of IPv4 address
d = sys.argv[2]
# Get next IPv4 address
hex_ip2 = hex(int(hex_ip,16)+int(d))
# Pad hex number with zeros
hex_ip2 = hex_ip2[2:]
list_zeros = ['0']*(8-len(hex_ip2))
str_zeros = ''.join(list_zeros)
hex_ip2 = str_zeros + hex_ip2
# Convert to dot decimal IPv4 address format
ip2 = hex2ip(hex_ip2)

print("%s" % (ip2))
