#!/usr/bin/python3

def hex2ip(ipAddr):
    l = []
    for i in range(0,4):
        l.append(ipAddr[2*i:2*i+2])

    ip = ''

    for i in range(0,4):
        ip = ip + str(int(l[i],16))
        if (i is not 3):
            ip = ip + '.'

    return ip
