#!/usr/bin/python3

def ip2hex(ipAddr):
    # 'ipAddr' is an IPv4 address as string, i.e. '192.168.0.1'
    a=ipAddr.split('.')
    # {:02x} meaning: (2) digits, (0) padding, (x) lowercase
    # map(function(),variable): applies 'function()' to 'variable'
    # '*' to interpret 'variable' (list) as independent arguments
    hexIpAddr = '{:02x}{:02x}{:02x}{:02x}'.format(*map(int, a))
    return hexIpAddr
